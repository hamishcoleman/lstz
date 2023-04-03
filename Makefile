
NAME := lstz
DESTDIR ?= installdir
INSTALLDIR := $(DESTDIR)/$(NAME)

describe := $(shell git describe --dirty)
tarfile := $(NAME)-$(describe).tar.gz

TESTFILES+=lstz.py
COV_PERCENT=76

all:
	false

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

clean:
	rm -rf htmlcov .coverage __pycache__/ .pytest_cache
