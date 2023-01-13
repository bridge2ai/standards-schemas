

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "UseCase" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	use_case_category VARCHAR(15), 
	known_limitations TEXT, 
	relevance_to_dgps VARCHAR(8), 
	data_types TEXT, 
	data_substrates TEXT, 
	standards_and_tools_for_dgp_use TEXT, 
	alternative_standards_and_tools TEXT, 
	enables TEXT, 
	involved_in_experimental_design TEXT, 
	involved_in_metadata_management TEXT, 
	involved_in_quality_control TEXT, 
	xrefs TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "UseCaseCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);
