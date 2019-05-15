default: help

upgrade-dist-tools:
	pipenv run python -m pip install --upgrade setuptools wheel twine

# Install packages from Pipfile
install:
	pipenv run pipenv install --dev

# Run pylint
lint:
	pipenv run pylint ./setup.py unittest_prettify tests sample


# Run tests with pytest
test:
	pipenv run python tests.py


# Run tests with pytest and coverage
test-cov:
	pipenv run coverage run tests.py; \
	pipenv run coverage report -m


# Sort imports as PEP8
isort:
	pipenv run isort **/*.py

# Format code with black
format:
	pipenv run black unittest_prettify/ tests.py sample.py

# Upload coverage report o codecov.io
codecov:
	codecov --token=$${CODECOV_TOKEN}

# Create wheel from source
build: upgrade-dist-tools
	python setup.py sdist bdist_wheel


# Remove build files
clean:
	rm -rf build/ *.egg-info/ dist/


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
