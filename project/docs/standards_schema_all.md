
# standards-schema-all


**metamodel version:** 1.7.0

**version:** None


High-level classes for Bridge2AI Standards schemas.


### Classes

 * [DataStandardOrToolContainer](DataStandardOrToolContainer.md) - A container for DataStandardOrTool(s).
 * [DataSubstrateContainer](DataSubstrateContainer.md) - A container for DataSubstrates.
 * [DataTopicContainer](DataTopicContainer.md) - A container for DataTopics.
 * [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity
     * [DataStandardOrTool](DataStandardOrTool.md) - Represents a standard or tool in the Bridge2AI Standards Registry.
         * [DataStandard](DataStandard.md) - Represents a general purpose standard in the Bridge2AI Standards Registry.
             * [BiomedicalStandard](BiomedicalStandard.md) - Represents a standard in the Bridge2AI Standards Registry with particular applications or relevance to clinical or biomedical research purposes.
         * [ModelRepository](ModelRepository.md) - Represents a resource in the Bridge2AI Standards Registry serving to curate and store computational models. To be a respository, the resource must not index models alone.
         * [OntologyOrVocabulary](OntologyOrVocabulary.md) - A set of concepts and categories, potentially defined or accompanied by their hierarchical relationships.
         * [ReferenceDataOrDataset](ReferenceDataOrDataset.md) - Represents a resource in the Bridge2AI Standards Registry serving as a standardized, reusable data source.
         * [ReferenceImplementation](ReferenceImplementation.md) - Represents an implementation of one or more standards or tools in the Bridge2AI Standards Registry, whether as a full specification in a particular language or as an application to a specific use case.
         * [Registry](Registry.md) - Represents a resource in the Bridge2AI Standards Registry serving to curate and/or index other resources.
         * [SoftwareOrTool](SoftwareOrTool.md) - Represents a piece of software or computational tool in the Bridge2AI Standards Registry.
         * [TrainingProgram](TrainingProgram.md) - Represents a training program for skills and experience related to standards or tools in the Bridge2AI Standards Registry.
     * [DataSubstrate](DataSubstrate.md) - Represents a data substrate for Bridge2AI data. This may be a high-level data structure or a specific implementation of that structure. Interpret as "data, in this form or format", as compared to DataStandard, which refers to the set of rules defining a standard. For example, data in TSV format is represented as a DataSubstrate but the concept of TSV format is a DataStandard.
     * [DataTopic](DataTopic.md) - Represents a general data topic for Bridge2AI data or the tools/standards applied to the data.
     * [Organization](Organization.md) - Represents a group or organization related to or responsible for one or more Bridge2AI standards.
     * [UseCase](UseCase.md) - Represents a use case for Bridge2AI standards.
 * [OrganizationContainer](OrganizationContainer.md) - A container for Organizations.
 * [UseCaseContainer](UseCaseContainer.md) - A container for UseCase.

### Mixins


### Slots

 * [EDAM_ID](EDAM_ID.md)
 * [MeSH_ID](MeSH_ID.md)
 * [NCIT_ID](NCIT_ID.md)
 * [ROR_ID](ROR_ID.md)
 * [URL](URL.md)
 * [Wikidata_ID](Wikidata_ID.md)
 * [data_standardortools_collection](data_standardortools_collection.md)
 * [data_substrates_collection](data_substrates_collection.md)
 * [data_topics_collection](data_topics_collection.md)
 * [description](description.md) - A human-readable description for a thing.
 * [id](id.md) - A unique identifier for a thing.
 * [name](name.md) - A human-readable name for a thing.
 * [node property](node_property.md) - A grouping for any property that holds between a node and a value.
     * [alternative_standards_and_tools](alternative_standards_and_tools.md) - List of identifiers of standards and tools; those not explicitly planned to be used, by one or more Bridge2AI DGPs in addressing this use case but serving as viable alternatives, from those in the Standards Registry.
     * [collection](collection.md) - Tags for specific sets of standards.
     * [data_substrates](data_substrates.md) - Relevance of the use case to one or more data substrates.
     * [data_topics](data_topics.md) - Relevance of the use case to one or more data topics.
     * [enables](enables.md) - Other use case(s) this use case supports or makes possible.
     * [file_extensions](file_extensions.md) - Commonly used file extensions for this substrate.
     * [formal_specification](formal_specification.md) - Relevant code repository or other location for a formal specification of the standard or tool. Often a URL, particularly to a Git repository.
     * [involved_in_experimental_design](involved_in_experimental_design.md) - True if use case is likely to be implemented as part of an experimental procedure or collection of data to be used as part of an experiment.
     * [involved_in_metadata_management](involved_in_metadata_management.md) - True if use case is likely to be implemented as part of metadata indexing, sample tracking, or any other storage of high-level data properties. Includes use cases in which metadata will be collected along with data.
     * [involved_in_quality_control](involved_in_quality_control.md) - True is use case is likely to be implemented as part of data validation operations.
     * [is_open](is_open.md) - Is the standard or tool FAIR and available free of cost?
     * [known_limitations](known_limitations.md) - Any current obstacles to implementing this use case. This could be a selection from one or more predefined categories including lack of standards, lack of relevant patient cohort, lack of funding, etc.
     * [limitations](limitations.md) - Potential obstacles particular to this substrate or implementation. 
     * [metadata_storage](metadata_storage.md) - Data Substrate in which metadata is stored.
     * [publication](publication.md) - Relevant publication for the standard or tool. Prefer a DOI or PUBMED.
     * [purpose_detail](purpose_detail.md) - Text description of the standard or tool.
     * [requires_registration](requires_registration.md) - Does usage of the standard or tool require registrion of a user or group with some organization or managerial body?
     * [standards_and_tools_for_dgp_use](standards_and_tools_for_dgp_use.md) - List of identifiers of standards and tools; those planned to be used, or already in use, by one or more Bridge2AI DGPs in addressing this use case, from those in the Standards Registry, or TBD if standards/tools not yet finalized for this use case.
     * [url](url.md) - URL for basic documentation of the standard or tool.
     * [use_case_category](use_case_category.md) - Category of the UseCase. Not all projects will incorporate use cases in all categories.
         * [UseCase➞use_case_category](UseCase_use_case_category.md)
     * [xref](xref.md) - URI of corresponding class in an ontology of experimental procedures, in CURIE form.
 * [organizations](organizations.md)
 * [related_to](related_to.md) - A relationship that is asserted between two named things.
     * [concerns_data_topic](concerns_data_topic.md) - Subject standard is generally applied in the context of object data topic.
     * [has_relevant_organization](has_relevant_organization.md) - Subject standard is managed or otherwise guided buy the object organization(s).
     * [subclass_of](subclass_of.md) - Holds between two classes where the domain class is a specialization of the range class.
 * [relevance_to_dgps](relevance_to_dgps.md) - Relevance of the use case to one or more DGPs.
 * [use_cases](use_cases.md)

### Enums

 * [DataGeneratingProject](DataGeneratingProject.md) - One of the Bridge2AI Data Generating Projects.
 * [StandardsCollectionTag](StandardsCollectionTag.md) - Tags for specific sets of standards.
 * [UseCaseCategory](UseCaseCategory.md) - Category of use case.

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [EdamIdentifier](types/EdamIdentifier.md)  ([Uriorcurie](types/Uriorcurie.md)) 
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [MeshIdentifier](types/MeshIdentifier.md)  ([Uriorcurie](types/Uriorcurie.md)) 
 * [NcitIdentifier](types/NcitIdentifier.md)  ([Uriorcurie](types/Uriorcurie.md)) 
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [RorIdentifier](types/RorIdentifier.md)  ([Uriorcurie](types/Uriorcurie.md)) 
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
 * [WikidataIdentifier](types/WikidataIdentifier.md)  ([Uriorcurie](types/Uriorcurie.md)) 
