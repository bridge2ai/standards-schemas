

CREATE TABLE "DataStandardOrTool" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	concerns_data_topic TEXT, 
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataTopic" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"EDAM_ID" TEXT, 
	"MeSH_ID" TEXT, 
	"NCIT_ID" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "UseCase" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	alternative_standards_and_tools TEXT, 
	data_topics TEXT, 
	enables TEXT, 
	involved_in_experimental_design BOOLEAN, 
	involved_in_metadata_management BOOLEAN, 
	involved_in_quality_control BOOLEAN, 
	known_limitations TEXT, 
	standards_and_tools_for_dgp_use TEXT, 
	use_case_category VARCHAR(15) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "UseCaseContainer" (
	container_name TEXT, 
	use_cases TEXT, 
	PRIMARY KEY (container_name, use_cases)
);

CREATE TABLE "DataSubstrate" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"EDAM_ID" TEXT, 
	"MeSH_ID" TEXT, 
	"NCIT_ID" TEXT, 
	"UseCase_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("UseCase_id") REFERENCES "UseCase" (id)
);

CREATE TABLE "Organization" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"ROR_ID" TEXT, 
	"Wikidata_ID" TEXT, 
	"URL" TEXT, 
	"DataStandardOrTool_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DataStandardOrTool_id") REFERENCES "DataStandardOrTool" (id)
);

CREATE TABLE "DataStandardOrTool_collection" (
	backref_id TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY (backref_id, collection), 
	FOREIGN KEY(backref_id) REFERENCES "DataStandardOrTool" (id)
);

CREATE TABLE "UseCase_relevance_to_dgps" (
	backref_id TEXT, 
	relevance_to_dgps VARCHAR(7), 
	PRIMARY KEY (backref_id, relevance_to_dgps), 
	FOREIGN KEY(backref_id) REFERENCES "UseCase" (id)
);

CREATE TABLE "UseCase_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "UseCase" (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"Organization_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);

CREATE TABLE "DataSubstrate_metadata_storage" (
	backref_id TEXT, 
	metadata_storage TEXT, 
	PRIMARY KEY (backref_id, metadata_storage), 
	FOREIGN KEY(backref_id) REFERENCES "DataSubstrate" (id)
);

CREATE TABLE "DataSubstrate_file_extensions" (
	backref_id TEXT, 
	file_extensions TEXT, 
	PRIMARY KEY (backref_id, file_extensions), 
	FOREIGN KEY(backref_id) REFERENCES "DataSubstrate" (id)
);

CREATE TABLE "DataSubstrate_limitations" (
	backref_id TEXT, 
	limitations TEXT, 
	PRIMARY KEY (backref_id, limitations), 
	FOREIGN KEY(backref_id) REFERENCES "DataSubstrate" (id)
);
