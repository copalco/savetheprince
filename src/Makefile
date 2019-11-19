tcr:
	./tcr.sh

ci-build: test type-check

test:
	python -m unittest discover tests

type-check:
	mypy savetheprince/ tests/
