pep8:
	flake8 ./service ./test
run:
	python3 ./main.py

run-test:
	coverage run -m pytest
	coverage report