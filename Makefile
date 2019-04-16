default: help

upgrade-dist-tools:
	python -m pip install --upgrade setuptools wheel twine

# Install packages from Pipfile
install:
	pipenv install --dev

# Run pylint
lint:
	pipenv run pylint ./setup.py django_test_prettify tests


# Run tests with pytest
test:
	pytest -s --verbose ./tests


# Run tests with pytest and coverage
test-cov:
	pytest -s --verbose --cov-report term-missing --cov=django_test_prettify ./tests


# Upload coverage report o codecov.io
codecov:
	codecov --token=$${CODECOV_TOKEN}

# Create wheel from source
build: upgrade-dist-tools
	python setup.py sdist bdist_wheel


# Remove build files
clean:
	rm -rf build/ *.egg-info/ dist/

# Sort imports as PEP8
isort:
	isort **/*.py


# Upload dist content to test.pypi.org
upload-test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*


# Upload dist content to pypi.org
upload:
	twine upload  dist/*

# Display this help
help:
	@ echo
	@ echo '  Usage:'
	@ echo ''
	@ echo '	make <target> [flags...]'
	@ echo ''
	@ echo '  Targets:'
	@ echo ''
	@ awk '/^#/{ comment = substr($$0,3) } comment && /^[a-zA-Z][a-zA-Z0-9_-]+ ?:/{ print "   ", $$1, comment }' ./Makefile | column -t -s ':' | sort
	@ echo ''
	@ echo '  Flags:'
	@ echo ''
	@ awk '/^#/{ comment = substr($$0,3) } comment && /^[a-zA-Z][a-zA-Z0-9_-]+ ?\?=/{ print "   ", $$1, $$2, comment }' ./Makefile | column -t -s '?=' | sort
	@ echo ''
