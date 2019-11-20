tcr:
	./tcr.sh

ci-build: test-with-coverage type-check style-check coverage-report

test:
	python -m unittest discover tests

test-with-coverage:
	coverage run -m unittest discover tests

type-check:
	mypy savetheprince/ tests/

style-check:
	flake8 .

coverage-report:
	coverage report
