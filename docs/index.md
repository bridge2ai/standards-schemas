# standards-schema-all

High-level classes for Bridge2AI Standards schemas.

URI: https://w3id.org/bridge2ai/standards-schema-all

Name: standards-schema-all



## Classes

| Class | Description |
| --- | --- |
| [DataPart](DataPart.md) | Represents a part of all datasets in a manifest |
| [DataSetContainer](DataSetContainer.md) | A container for DataSets |
| [DataStandardOrToolContainer](DataStandardOrToolContainer.md) | A container for DataStandardOrTool(s) |
| [DataSubstrateContainer](DataSubstrateContainer.md) | A container for DataSubstrates |
| [DataTopicContainer](DataTopicContainer.md) | A container for DataTopics |
| [ManifestContainer](ManifestContainer.md) | A container for Manifests |
| [NamedThing](NamedThing.md) | A generic grouping for any identifiable entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AnatomicalEntity](AnatomicalEntity.md) | A subcellular location, cell type or gross anatomical part |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataSet](DataSet.md) | Represents a data set by its metadata |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataStandardOrTool](DataStandardOrTool.md) | Represents a standard or tool in the Bridge2AI Standards Registry |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataStandard](DataStandard.md) | Represents a general purpose standard in the Bridge2AI Standards Registry |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiomedicalStandard](BiomedicalStandard.md) | Represents a standard in the Bridge2AI Standards Registry with particular app... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ModelRepository](ModelRepository.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OntologyOrVocabulary](OntologyOrVocabulary.md) | A set of concepts and categories, potentially defined or accompanied by their... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ReferenceImplementation](ReferenceImplementation.md) | Represents an implementation of one or more standards or tools in the Bridge2... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Registry](Registry.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SoftwareOrTool](SoftwareOrTool.md) | Represents a piece of software or computational tool in the Bridge2AI Standar... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TrainingProgram](TrainingProgram.md) | Represents a training program for skills and experience related to standards ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataSubstrate](DataSubstrate.md) | Represents a data substrate for Bridge2AI data |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataTopic](DataTopic.md) | Represents a general data topic for Bridge2AI data or the tools/standards app... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Manifest](Manifest.md) | Represents a manifest |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Organization](Organization.md) | Represents a group or organization related to or responsible for one or more ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UseCase](UseCase.md) | Represents a use case for Bridge2AI standards |
| [OrganizationContainer](OrganizationContainer.md) | A container for Organizations |
| [UseCaseContainer](UseCaseContainer.md) | A container for UseCase |



## Slots

| Slot | Description |
| --- | --- |
| [alternative_standards_and_tools](alternative_standards_and_tools.md) | List of identifiers of standards and tools; those not explicitly planned to b... |
| [anatomy](anatomy.md) | Relevant anatomical locations, including gross anatomical parts, cell types, ... |
| [availability_description](availability_description.md) | A description of the availability of the data set, including any restrictions... |
| [category](category.md) | CURIE for the high level ontology class in which this entity is categorized |
| [collection](collection.md) | Tags for specific sets of standards |
| [concerns_data_topic](concerns_data_topic.md) | Subject standard is generally applied in the context of object data topic |
| [concerns_data_topics](concerns_data_topics.md) | The data part includes these data topics |
| [contribution_date](contribution_date.md) | The date on which the node was added |
| [contributor_github_name](contributor_github_name.md) | The name of the github user who added this node |
| [contributor_name](contributor_name.md) | The name of the person who added this node |
| [contributor_orcid](contributor_orcid.md) | The ORCiD of the person who added this node |
| [data_collection](data_collection.md) | Collection of associated DataSet objects |
| [data_part_description](data_part_description.md) | Description of the data part |
| [data_part_name](data_part_name.md) | Name of the data part |
| [data_parts](data_parts.md) | Collection of associated DataPart objects |
| [data_standardortools_collection](data_standardortools_collection.md) | Collection of associated data standards or tools |
| [data_substrates](data_substrates.md) | Relevance of the use case to one or more data substrates |
| [data_substrates_collection](data_substrates_collection.md) | Collection of associated data substrates |
| [data_topics](data_topics.md) | Relevance of the use case to one or more data topics |
| [data_topics_collection](data_topics_collection.md) | Collection of associated data topics |
| [data_url](data_url.md) | URL where the data set can be accessed |
| [datasets](datasets.md) | The manifest includes these datasets |
| [datasheet_url](datasheet_url.md) | URL where the datasheet for the data set can be accessed |
| [description](description.md) | A human-readable description for a thing |
| [documentation_url](documentation_url.md) | URL where documentation for the data set can be accessed |
| [edam_id](edam_id.md) | Unique EDAM identifier |
| [enables](enables.md) | List of other use case(s) this use case supports or makes possible |
| [file_extensions](file_extensions.md) | Commonly used file extensions for this substrate |
| [formal_specification](formal_specification.md) | Relevant code repository or other location for a formal specification of the ... |
| [has_files](has_files.md) | Subject data set has the file(s) listed in this slot as parts |
| [has_parts](has_parts.md) | Subject data set has the data set(s) listed in this slot as parts |
| [has_relevant_data_substrate](has_relevant_data_substrate.md) | Subject standard has some relationship to the object data substrate(s), inclu... |
| [has_relevant_organization](has_relevant_organization.md) | Subject standard has some relationship to the object organization(s), includi... |
| [has_training_resource](has_training_resource.md) | Relevant training resources, standard usage manuals, or other documentation f... |
| [id](id.md) | A unique identifier for a thing |
| [involved_in_experimental_design](involved_in_experimental_design.md) | True if use case is likely to be implemented as part of an experimental proce... |
| [involved_in_metadata_management](involved_in_metadata_management.md) | True if use case is likely to be implemented as part of metadata indexing, sa... |
| [involved_in_quality_control](involved_in_quality_control.md) | A value of True indicates a use case is likely to be implemented as part of d... |
| [is_bridge2ai_data](is_bridge2ai_data.md) | True if the data set is produced by a Bridge2AI consortium group |
| [is_open](is_open.md) | Is the standard or tool FAIR and available free of cost? |
| [is_public](is_public.md) | True if the data set is publicly available |
| [known_limitations](known_limitations.md) | Any current obstacles to implementing this use case |
| [limitations](limitations.md) | Potential obstacles particular to this substrate or implementation |
| [manifest_collection](manifest_collection.md) | Collection of associated Manifest objects |
| [mesh_id](mesh_id.md) | Unique MeSH identifier |
| [metadata_storage](metadata_storage.md) | Data Substrate in which metadata is stored |
| [name](name.md) | A human-readable name for a thing |
| [ncit_id](ncit_id.md) | Unique NCIt Identifier |
| [node_property](node_property.md) | A grouping for any property that holds between a node and a value |
| [notes](notes.md) | Any additional notes about the manifest or the data part |
| [organization](organization.md) | The manifest corresponds to this organization |
| [organizations](organizations.md) | Collection of associated organizations |
| [produced_by](produced_by.md) | Subject data set was produced by the organization(s) listed in this slot |
| [publication](publication.md) | Relevant publication for the standard or tool |
| [purpose_detail](purpose_detail.md) | Text description of the standard or tool |
| [related_to](related_to.md) | A relationship that is asserted between two named things |
| [relevant_to_gcs](relevant_to_gcs.md) | Bridge2AI Grand Challenges related to this use case, generally because they a... |
| [requires_registration](requires_registration.md) | Does usage of the standard or tool require registration of a user or group wi... |
| [responsible_organization](responsible_organization.md) | Organization(s) responsible for providing and/or supporting the standard or t... |
| [ror_id](ror_id.md) | Unique ROR identifier |
| [standards_and_tools](standards_and_tools.md) | The data part includes these standards and tools |
| [standards_and_tools_for_gc_use](standards_and_tools_for_gc_use.md) | List of identifiers of standards and tools; those planned to be used, or alre... |
| [subclass_of](subclass_of.md) | Holds between two classes where the domain class is a specialization of the r... |
| [substrates](substrates.md) | Subject data set is relevant to the substrate(s) listed in this slot |
| [topic_involves_anatomy](topic_involves_anatomy.md) | A relationship between a DataTopic and an anatomical entity |
| [topics](topics.md) | Subject data set is relevant to the topic(s) listed in this slot |
| [type](type.md) | A generic slot for any label corresponding to the label for an entity type as... |
| [url](url.md) | URL for basic documentation of the standard or tool |
| [use_case_category](use_case_category.md) | Category of the UseCase |
| [use_cases](use_cases.md) | Collection of associated use cases |
| [use_conditions](use_conditions.md) | Applicable conditions on use, as defined by the Data Use Ontology (DUO) |
| [used_in_bridge2ai](used_in_bridge2ai.md) | True if the entity is used, developed, or otherwise related to work in the Br... |
| [uses_data_substrates](uses_data_substrates.md) | The data part includes these data substrates |
| [wikidata_id](wikidata_id.md) | Unique Wikidata identifier |
| [xref](xref.md) | URI of corresponding class in an ontology of experimental procedures, in CURI... |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [StandardsCollectionTag](StandardsCollectionTag.md) | Tags for specific sets of standards |
| [UseCaseCategory](UseCaseCategory.md) | Category of use case |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [CategoryType](CategoryType.md) | A primitive type in which the value denotes a class within the model |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [EdamIdentifier](EdamIdentifier.md) | Identifier from EDAM ontology |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [MeshIdentifier](MeshIdentifier.md) | Identifier from Medical Subject Headings (MeSH) biomedical vocabulary |
| [NcitIdentifier](NcitIdentifier.md) | Identifier from NCIT reference terminology with broad coverage of the cancer ... |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [RorIdentifier](RorIdentifier.md) | Identifier from Research Organization Registry |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |
| [WikidataIdentifier](WikidataIdentifier.md) | Identifier from Wikidata open knowledge base |


## Subsets

| Subset | Description |
| --- | --- |
