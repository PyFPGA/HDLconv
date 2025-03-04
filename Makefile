#!/usr/bin/make

.PHONY: docs

all: docs lint test

docs:
	cd docs; make html

lint:
	pycodestyle hdlconv
	pylint -s n hdlconv
	git diff --check --cached

test:
	cd tests && bash run.sh

clean:
	py3clean .
	rm -fr docs/build
	rm -fr .pytest_cache
	rm -fr `find . -name results`
	rm -fr `find . -name __pycache__`
