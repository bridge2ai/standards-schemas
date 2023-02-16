## Add your own custom Makefile targets here

RUN = poetry run
.PHONY: combined-extras examples-clean

examples-clean:
	@echo running examples-clean
	rm -rf src/data/output

combined-extras: examples-clean src/data/output

src/data/output: src/standards_schemas/schema/standards_schema_all.yaml
	@echo making src/data/output
	mkdir -p $@
	$(RUN) linkml-run-examples \
		--counter-example-input-directory src/data/invalid-examples \
		--input-directory src/data/valid-examples \
		--output-directory $@ \
		--schema $< > $@/README.md
