

CREATE TABLE "BiomedicalStandard" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	related_to TEXT, 
	concerns_data_topic TEXT, 
	has_relevant_organization TEXT, 
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataStandard" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	related_to TEXT, 
	concerns_data_topic TEXT, 
	has_relevant_organization TEXT, 
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataStandardOrTool" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	related_to TEXT, 
	concerns_data_topic TEXT, 
	has_relevant_organization TEXT, 
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataStandardOrToolContainer" (
	data_standardortools_collection TEXT, 
	PRIMARY KEY (data_standardortools_collection)
);

CREATE TABLE "DataSubstrate" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	related_to TEXT, 
	edam_id TEXT, 
	mesh_id TEXT, 
	ncit_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataSubstrateContainer" (
	data_substrates_collection TEXT, 
	PRIMARY KEY (data_substrates_collection)
);

CREATE TABLE "DataTopic" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	related_to TEXT, 
	edam_id TEXT, 
	mesh_id TEXT, 
	ncit_id TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DataTopicContainer" (
	data_topics_collection TEXT, 
	PRIMARY KEY (data_topics_collection)
);

CREATE TABLE "ModelRepository" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	related_to TEXT, 
	concerns_data_topic TEXT, 
	has_relevant_organization TEXT, 
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	related_to TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "OntologyOrVocabulary" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	related_to TEXT, 
	concerns_data_topic TEXT, 
	has_relevant_organization TEXT, 
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Organization" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	ror_id TEXT, 
	wikidata_id TEXT, 
	url TEXT, 
	related_to TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "OrganizationContainer" (
	organizations TEXT, 
	PRIMARY KEY (organizations)
);

CREATE TABLE "ReferenceDataOrDataset" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	related_to TEXT, 
	concerns_data_topic TEXT, 
	has_relevant_organization TEXT, 
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ReferenceImplementation" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	related_to TEXT, 
	concerns_data_topic TEXT, 
	has_relevant_organization TEXT, 
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Registry" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	related_to TEXT, 
	concerns_data_topic TEXT, 
	has_relevant_organization TEXT, 
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "SoftwareOrTool" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	related_to TEXT, 
	concerns_data_topic TEXT, 
	has_relevant_organization TEXT, 
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TrainingProgram" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	related_to TEXT, 
	concerns_data_topic TEXT, 
	has_relevant_organization TEXT, 
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "UseCase" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	related_to TEXT, 
	use_case_category VARCHAR(15) NOT NULL, 
	known_limitations TEXT, 
	data_topics TEXT, 
	data_substrates TEXT, 
	standards_and_tools_for_dgp_use TEXT, 
	alternative_standards_and_tools TEXT, 
	enables TEXT, 
	involved_in_experimental_design BOOLEAN, 
	involved_in_metadata_management BOOLEAN, 
	involved_in_quality_control BOOLEAN, 
	PRIMARY KEY (id)
);

CREATE TABLE "UseCaseContainer" (
	use_cases TEXT, 
	PRIMARY KEY (use_cases)
);

CREATE TABLE "BiomedicalStandard_collection" (
	backref_id TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY (backref_id, collection), 
	FOREIGN KEY(backref_id) REFERENCES "BiomedicalStandard" (id)
);

CREATE TABLE "DataStandard_collection" (
	backref_id TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY (backref_id, collection), 
	FOREIGN KEY(backref_id) REFERENCES "DataStandard" (id)
);

CREATE TABLE "DataStandardOrTool_collection" (
	backref_id TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY (backref_id, collection), 
	FOREIGN KEY(backref_id) REFERENCES "DataStandardOrTool" (id)
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

CREATE TABLE "ModelRepository_collection" (
	backref_id TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY (backref_id, collection), 
	FOREIGN KEY(backref_id) REFERENCES "ModelRepository" (id)
);

CREATE TABLE "OntologyOrVocabulary_collection" (
	backref_id TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY (backref_id, collection), 
	FOREIGN KEY(backref_id) REFERENCES "OntologyOrVocabulary" (id)
);

CREATE TABLE "ReferenceDataOrDataset_collection" (
	backref_id TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY (backref_id, collection), 
	FOREIGN KEY(backref_id) REFERENCES "ReferenceDataOrDataset" (id)
);

CREATE TABLE "ReferenceImplementation_collection" (
	backref_id TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY (backref_id, collection), 
	FOREIGN KEY(backref_id) REFERENCES "ReferenceImplementation" (id)
);

CREATE TABLE "Registry_collection" (
	backref_id TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY (backref_id, collection), 
	FOREIGN KEY(backref_id) REFERENCES "Registry" (id)
);

CREATE TABLE "SoftwareOrTool_collection" (
	backref_id TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY (backref_id, collection), 
	FOREIGN KEY(backref_id) REFERENCES "SoftwareOrTool" (id)
);

CREATE TABLE "TrainingProgram_collection" (
	backref_id TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY (backref_id, collection), 
	FOREIGN KEY(backref_id) REFERENCES "TrainingProgram" (id)
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
