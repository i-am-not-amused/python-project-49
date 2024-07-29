# Install dependencies
install:
	poetry install

# Build the source and wheels archives
build:
	poetry build

# Publish build package to the remote repository
publish: install build
	poetry publish --dry-run

# Install package
package-install:
	python3 -m pip install --user dist/*.whl


# Game scripts
brain-games:
	poetry run brain-games
