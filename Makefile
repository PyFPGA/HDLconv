#!/usr/bin/make

.PHONY: docs

all: docs lint test

docs:
	bash docgen.sh

lint:
	pycodestyle hdlconv
	pylint -s n hdlconv
	git diff --check --cached

test:
	cd tests && bash run.sh

clean:
	py3clean .
	rm -fr .pytest_cache
	rm -fr `find . -name __pycache__`
