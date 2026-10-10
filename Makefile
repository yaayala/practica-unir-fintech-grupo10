.PHONY: all $(MAKECMDGOALS)

run:
	docker run --rm --volume `pwd`:/opt/app --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py words.txt yes

.PHONY: run-local
run-local:
	python3 main.py words.txt yes

FILE ?= palabras_fernando.txt
DUP ?= no

.PHONY: run-file
run-file:
	python3 main.py $(FILE) $(DUP)