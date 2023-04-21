# standards-schemas

Data schema for Bridge2AI Standards Schemas.

## Website

* [https://bridge2ai.github.io/standards-schemas](https://bridge2ai.github.io/standards-schemas)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [data](src/data) - example valid and invalid data
  * [standards_schemas](src/standards_schemas)
    * [datamodel](src/standards_schemas/datamodel) -- Generated python datamodels
    * [schema](src/standards_schemas/schema) -- LinkML schemas
* [tests](tests/) - python tests

## Developer Documentation

* `poetry install`: initiate poetry environment for development and build environment

### Project Generation

Use the `make` command to generate project artifacts:

* `make all`: make everything
* `make deploy`: deploys site
* `make combined-extras`: check schema against all examples in src/data/

## Credits

This project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)
