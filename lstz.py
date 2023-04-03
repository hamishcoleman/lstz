#!/usr/bin/env python3
#
# List timezones
#
# TODO: install packages:
#       python3-tz
#

import collections
import datetime
import os
import pytz
import sys
import yaml


default_db = yaml.safe_load("""---
home: Australia/Melbourne

zones:
    Australia/Melbourne: Melbourne
    Hongkong: HongKong
    Europe/London: London
    America/New_York: New York

colours:
    hours:
        0: sleep
        1: sleep
        2: sleep
        3: sleep
        4: sleep
        5: sleep
        6: sleep
        7: other
        8: other
        9: work
        10: work
        11: work
        12: work
        13: work
        14: work
        15: work
        16: work
        17: other
        18: other
        19: other
        20: other
        21: other
        22: other
        23: sleep

    codes:
        other: "\\e[0m"     # normal
        work: "\\e[0;1m"    # bold
        sleep: "\\e[0;2m"   # dim
        normal: "\\e[0m"
        hilight: "\\e[7m"   # reverse
""")


def str_table(rows, columns, orderby):
    """Given an array of dicts, do a simple table print"""
    result = list()
    line = list()
    widths = collections.defaultdict(lambda: 0)

    def get_col_str(row, column):
        val = getattr(row, column, None)

        if val is None and isinstance(row, dict):
            if column in row:
                val = row[column]

        if callable(val):
            val = val()

        if val is None:
            return None

        return str(val)

    def display_width(s):
        """Attempt to ignore escape sequences when calculating len"""
        while True:
            try:
                start = s.index("\033[")
            except ValueError:
                # No more escapes found
                return len(s)

            end = s.index("m", start)

            s = s[:start] + s[end+1:]

    if len(rows) == 0:
        # No data to show, be sure not to truncate the column headings
        for col in columns:
            widths[col] = len(col)
    else:
        for row in rows:
            for col in columns:
                # TODO: cache data for use in render loop
                data = get_col_str(row, col)
                if data is not None:
                    widths[col] = max(widths[col], display_width(data))

    for col in columns:
        if widths[col] == 0:
            widths[col] = 1
        line += ["{:{}.{}} ".format(col, widths[col], widths[col])]
    result += [''.join(line)]

    # if orderby is not None:
    #     rows = sorted(rows, key=lambda row: row.get(orderby, 0))

    for row in rows:
        line = list()
        for col in columns:
            data = get_col_str(row, col)
            if data is None:
                data = ''
            line += ["{:{}} ".format(data, widths[col])]
        result += [''.join(line)]

    return result


def test_str_table():
    rows = [
        {
            "a": 1,
            "b": "beeblebrox",
            "c": "count",
        },
        {
            "a": 2,
            "b": "butter",
            "c": "confusion",
        },
    ]

    columns = ["a", "b", "c"]

    result = str_table(rows, columns, None)

    expected = [
        "a b          c         ",
        "1 beeblebrox count     ",
        "2 butter     confusion ",
    ]

    assert result == expected


class Zone:
    def __init__(self, name):
        self.tz = pytz.timezone(name)
        self.name = self.tz.zone
        self.reference = None
        self.home = None
        self.colours = None

    def tzname(self):
        return self.tz.tzname(self.reference)

    def _offset_hours(self):
        """Return the offset in hours from the home zone"""
        dt = self.reference
        home_offset = self.home.tz.utcoffset(dt).total_seconds() / 3600
        self_offset = self.tz.utcoffset(dt).total_seconds() / 3600

        offset = self_offset - home_offset

        return offset

    def offset(self):
        offset = self._offset_hours()

        if offset == 0:
            # home symbol
            return "\u2302".rjust(3)

        if offset.is_integer():
            offset = int(offset)
            return f"{offset:+d}".rjust(3)

        # TODO: deal with non integer offsets better
        offset = int(offset)
        return f"~{offset:+d}".rjust(3)

    def time(self):
        dt = self.reference
        self_time = dt.astimezone(self.tz)
        self_date = self_time.date()
        home_date = dt.astimezone(self.home.tz).date()
        offset = (self_date - home_date).days

        if offset == 0:
            offset_str = ""
        else:
            offset_str = f"{offset:+d}"

        return self_time.strftime("%H:%M") + offset_str

    def _hour_dt(self, hour):
        """Calculate an hour of the day in the reference day and then represent
        that same time but in the self zone"""

        midnight = self.reference.astimezone(self.home.tz).replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

        hour_dt = midnight + datetime.timedelta(hours=hour)
        return hour_dt.astimezone(self.tz)

    def _str_hour(self, hour):
        hour_now = self.reference.astimezone(self.home.tz).hour
        hour_nr = self._hour_dt(hour).hour

        hours = self.colours["hours"]
        codes = self.colours["codes"]
        hour_colour = codes[hours[hour_nr]]

        if hour == hour_now:
            # higlight the current hour
            hilight = codes["hilight"]
        else:
            hilight = ""

        if hour_nr == 0:
            hour_str = "  "
        else:
            hour_str = f"{hour_nr:2}"

        return hour_colour + hilight + hour_str + codes["normal"]

    def hours(self):
        r = []
        for i in range(24):
            r += [self._str_hour(i)]
        s = ' '.join(r)
        return s


def test_zone_simple():
    zone = Zone("Australia/Melbourne")
    assert zone.name == "Australia/Melbourne"
    zone.name = "Melbourne"
    assert zone.name == "Melbourne"

    zone.reference = datetime.datetime(2023, 2, 4, 5, 6, 7)
    assert zone.tzname() == "AEDT"


def test_zone_offset():
    home = Zone("Europe/London")
    zone = Zone("Australia/Melbourne")

    zone.reference = datetime.datetime(2023, 2, 4, 5, 6, 7)

    zone.home = home
    assert zone.offset() == "+11"

    zone.home = zone
    assert zone.offset() == "\u2302".rjust(3)

    # TODO: non integer offset zones


def test_zone_time():
    home = Zone("Europe/London")
    zone = Zone("Australia/Melbourne")

    zone.reference = datetime.datetime(2023, 2, 4, 5, 6, 7)

    zone.home = home
    assert zone.time() == "16:06"

    # TODO: times that have both positive and negative days vs home


def test_zone_hour():
    home = Zone("Europe/London")
    zone = Zone("Australia/Melbourne")

    zone.reference = datetime.datetime(2023, 2, 4, 5, 6, 7)
    zone.colours = {
        "hours": {
            0: "test_code1",
            16: "test_code2",
            17: "test_code3",
        },
        "codes": {
            "test_code1": "A",
            "test_code2": "B",
            "test_code3": "C",
            "hilight": "h",
            "normal": "n",
        },
    }

    zone.home = home
    assert zone._str_hour(5) == "Bh16n"
    assert zone._str_hour(6) == "C17n"
    assert zone._str_hour(13) == "A  n"


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = os.path.expanduser("~/.config/lstz/tz.yml")

    db = default_db

    try:
        fh = open(filename, "r", encoding="utf8")
        db.update(yaml.safe_load(fh))
    except FileNotFoundError:
        pass
        # print(f"{filename}: Not found, using defaults")

    # TODO: arg parser
    dt = datetime.datetime.now()

    # create the objects
    for name, this in db["zones"].items():
        zone = Zone(name)
        zone.reference = dt
        zone.colours = db["colours"]

        if isinstance(this, str):
            zone.name = this

        db["zones"][name] = zone

    home = db["zones"][db["home"]]
    for zone in db["zones"].values():
        zone.home = home

    lines = str_table(db["zones"].values(), [
        "offset",
        "name",
        "tzname",
        "time",
        "hours",
    ], None)

    # print them
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
