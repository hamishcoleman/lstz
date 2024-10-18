
NAME := lstz
DESTDIR ?= installdir
INSTALLDIR := $(DESTDIR)/usr/bin

describe := $(shell git describe --dirty)
tarfile := $(NAME)-$(describe).tar.gz

TESTFILES+=lstz.py
COV_PERCENT=76

all:
	@echo Pure Python package - nothing to build

build-dep:
	apt-get install \
            python3-pytest \
            python3-tz \

install:
	mkdir -p $(INSTALLDIR)
	install -p lstz.py $(INSTALLDIR)/lstz

tar:    $(tarfile)

$(tarfile):
	$(MAKE) install
	tar -v -c -z -C $(DESTDIR) -f $(tarfile) .

test:
	pytest-3 \
            $(TESTFILES)

cover:
	pytest-3 \
            -vv \
            --cov=. \
            --cov-report=html \
            --cov-report=term \
            --cov-fail-under=$(COV_PERCENT) \
            $(TESTFILES)

lint:
	flake8

# A quick way to generate a dpkg from a checkout.
#
VERSION:=$(shell git describe --abbrev=7 --dirty)
DEBEMAIL?=builder@example.com
DEBFULLNAME?="Auto Build"
export DEBEMAIL
export DEBFULLNAME
.PHONY: dpkg
dpkg:
	rm -f debian/changelog
	dch --create --empty --package lstz -v ${VERSION}-1 --no-auto-nmu local package Auto Build
	env -u CFLAGS dpkg-buildpackage -rfakeroot -d -us -uc

clean:
	rm -rf htmlcov .coverage __pycache__/ .pytest_cache
