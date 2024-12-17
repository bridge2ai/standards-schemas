-- # Class: "NamedThing" Description: "A generic grouping for any identifiable entity"
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
-- # Class: "AnatomicalEntity" Description: "A subcellular location, cell type or gross anatomical part"
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
-- # Class: "DataStandardOrTool" Description: "Represents a standard or tool in the Bridge2AI Standards Registry."
--     * Slot: purpose_detail Description: Text description of the standard or tool.
--     * Slot: is_open Description: Is the standard or tool FAIR and available free of cost?
--     * Slot: requires_registration Description: Does usage of the standard or tool require registration of a user or group with some organization or managerial body?
--     * Slot: url Description: URL for basic documentation of the standard or tool.
--     * Slot: publication Description: Relevant publication for the standard or tool. Prefer a DOI or PUBMED.
--     * Slot: formal_specification Description: Relevant code repository or other location for a formal specification of the standard or tool. Often a URL, particularly to a Git repository.
--     * Slot: not_relevant_to_dgps Description: Is the standard or tool currently relevant to DGPs?
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
--     * Slot: DataStandardOrToolContainer_id Description: Autocreated FK slot
-- # Class: "DataStandard" Description: "Represents a general purpose standard in the Bridge2AI Standards Registry."
--     * Slot: purpose_detail Description: Text description of the standard or tool.
--     * Slot: is_open Description: Is the standard or tool FAIR and available free of cost?
--     * Slot: requires_registration Description: Does usage of the standard or tool require registration of a user or group with some organization or managerial body?
--     * Slot: url Description: URL for basic documentation of the standard or tool.
--     * Slot: publication Description: Relevant publication for the standard or tool. Prefer a DOI or PUBMED.
--     * Slot: formal_specification Description: Relevant code repository or other location for a formal specification of the standard or tool. Often a URL, particularly to a Git repository.
--     * Slot: not_relevant_to_dgps Description: Is the standard or tool currently relevant to DGPs?
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
-- # Class: "BiomedicalStandard" Description: "Represents a standard in the Bridge2AI Standards Registry with particular applications or relevance to clinical or biomedical research purposes."
--     * Slot: purpose_detail Description: Text description of the standard or tool.
--     * Slot: is_open Description: Is the standard or tool FAIR and available free of cost?
--     * Slot: requires_registration Description: Does usage of the standard or tool require registration of a user or group with some organization or managerial body?
--     * Slot: url Description: URL for basic documentation of the standard or tool.
--     * Slot: publication Description: Relevant publication for the standard or tool. Prefer a DOI or PUBMED.
--     * Slot: formal_specification Description: Relevant code repository or other location for a formal specification of the standard or tool. Often a URL, particularly to a Git repository.
--     * Slot: not_relevant_to_dgps Description: Is the standard or tool currently relevant to DGPs?
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
-- # Class: "Registry" Description: "Represents a resource in the Bridge2AI Standards Registry serving to curate and/or index other resources."
--     * Slot: purpose_detail Description: Text description of the standard or tool.
--     * Slot: is_open Description: Is the standard or tool FAIR and available free of cost?
--     * Slot: requires_registration Description: Does usage of the standard or tool require registration of a user or group with some organization or managerial body?
--     * Slot: url Description: URL for basic documentation of the standard or tool.
--     * Slot: publication Description: Relevant publication for the standard or tool. Prefer a DOI or PUBMED.
--     * Slot: formal_specification Description: Relevant code repository or other location for a formal specification of the standard or tool. Often a URL, particularly to a Git repository.
--     * Slot: not_relevant_to_dgps Description: Is the standard or tool currently relevant to DGPs?
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
-- # Class: "OntologyOrVocabulary" Description: "A set of concepts and categories, potentially defined or accompanied by their hierarchical relationships."
--     * Slot: purpose_detail Description: Text description of the standard or tool.
--     * Slot: is_open Description: Is the standard or tool FAIR and available free of cost?
--     * Slot: requires_registration Description: Does usage of the standard or tool require registration of a user or group with some organization or managerial body?
--     * Slot: url Description: URL for basic documentation of the standard or tool.
--     * Slot: publication Description: Relevant publication for the standard or tool. Prefer a DOI or PUBMED.
--     * Slot: formal_specification Description: Relevant code repository or other location for a formal specification of the standard or tool. Often a URL, particularly to a Git repository.
--     * Slot: not_relevant_to_dgps Description: Is the standard or tool currently relevant to DGPs?
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
-- # Class: "ModelRepository" Description: "Represents a resource in the Bridge2AI Standards Registry serving to curate and store computational models. To be a repository, the resource must not index models alone."
--     * Slot: purpose_detail Description: Text description of the standard or tool.
--     * Slot: is_open Description: Is the standard or tool FAIR and available free of cost?
--     * Slot: requires_registration Description: Does usage of the standard or tool require registration of a user or group with some organization or managerial body?
--     * Slot: url Description: URL for basic documentation of the standard or tool.
--     * Slot: publication Description: Relevant publication for the standard or tool. Prefer a DOI or PUBMED.
--     * Slot: formal_specification Description: Relevant code repository or other location for a formal specification of the standard or tool. Often a URL, particularly to a Git repository.
--     * Slot: not_relevant_to_dgps Description: Is the standard or tool currently relevant to DGPs?
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
-- # Class: "ReferenceDataOrDataset" Description: "Represents a resource in the Bridge2AI Standards Registry serving as a standardized, reusable data source."
--     * Slot: purpose_detail Description: Text description of the standard or tool.
--     * Slot: is_open Description: Is the standard or tool FAIR and available free of cost?
--     * Slot: requires_registration Description: Does usage of the standard or tool require registration of a user or group with some organization or managerial body?
--     * Slot: url Description: URL for basic documentation of the standard or tool.
--     * Slot: publication Description: Relevant publication for the standard or tool. Prefer a DOI or PUBMED.
--     * Slot: formal_specification Description: Relevant code repository or other location for a formal specification of the standard or tool. Often a URL, particularly to a Git repository.
--     * Slot: not_relevant_to_dgps Description: Is the standard or tool currently relevant to DGPs?
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
-- # Class: "SoftwareOrTool" Description: "Represents a piece of software or computational tool in the Bridge2AI Standards Registry."
--     * Slot: purpose_detail Description: Text description of the standard or tool.
--     * Slot: is_open Description: Is the standard or tool FAIR and available free of cost?
--     * Slot: requires_registration Description: Does usage of the standard or tool require registration of a user or group with some organization or managerial body?
--     * Slot: url Description: URL for basic documentation of the standard or tool.
--     * Slot: publication Description: Relevant publication for the standard or tool. Prefer a DOI or PUBMED.
--     * Slot: formal_specification Description: Relevant code repository or other location for a formal specification of the standard or tool. Often a URL, particularly to a Git repository.
--     * Slot: not_relevant_to_dgps Description: Is the standard or tool currently relevant to DGPs?
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
-- # Class: "ReferenceImplementation" Description: "Represents an implementation of one or more standards or tools in the Bridge2AI Standards Registry, whether as a full specification in a particular language or as an application to a specific use case."
--     * Slot: purpose_detail Description: Text description of the standard or tool.
--     * Slot: is_open Description: Is the standard or tool FAIR and available free of cost?
--     * Slot: requires_registration Description: Does usage of the standard or tool require registration of a user or group with some organization or managerial body?
--     * Slot: url Description: URL for basic documentation of the standard or tool.
--     * Slot: publication Description: Relevant publication for the standard or tool. Prefer a DOI or PUBMED.
--     * Slot: formal_specification Description: Relevant code repository or other location for a formal specification of the standard or tool. Often a URL, particularly to a Git repository.
--     * Slot: not_relevant_to_dgps Description: Is the standard or tool currently relevant to DGPs?
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
-- # Class: "TrainingProgram" Description: "Represents a training program for skills and experience related to standards or tools in the Bridge2AI Standards Registry."
--     * Slot: purpose_detail Description: Text description of the standard or tool.
--     * Slot: is_open Description: Is the standard or tool FAIR and available free of cost?
--     * Slot: requires_registration Description: Does usage of the standard or tool require registration of a user or group with some organization or managerial body?
--     * Slot: url Description: URL for basic documentation of the standard or tool.
--     * Slot: publication Description: Relevant publication for the standard or tool. Prefer a DOI or PUBMED.
--     * Slot: formal_specification Description: Relevant code repository or other location for a formal specification of the standard or tool. Often a URL, particularly to a Git repository.
--     * Slot: not_relevant_to_dgps Description: Is the standard or tool currently relevant to DGPs?
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
-- # Class: "DataStandardOrToolContainer" Description: "A container for DataStandardOrTool(s)."
--     * Slot: id Description: 
-- # Class: "DataSubstrate" Description: "Represents a data substrate for Bridge2AI data. This may be a high-level data structure or a specific implementation of that structure. Interpret as "data, in this form or format", as compared to DataStandard, which refers to the set of rules defining a standard. For example, data in TSV format is represented as a DataSubstrate but the concept of TSV format is a DataStandard."
--     * Slot: edam_id Description: Unique EDAM identifier
--     * Slot: mesh_id Description: Unique MeSH identifier
--     * Slot: ncit_id Description: Unique NCIt Identifier
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
--     * Slot: DataSubstrateContainer_id Description: Autocreated FK slot
-- # Class: "DataSubstrateContainer" Description: "A container for DataSubstrates."
--     * Slot: id Description: 
-- # Class: "DataTopic" Description: "Represents a general data topic for Bridge2AI data or the tools/standards applied to the data."
--     * Slot: edam_id Description: Unique EDAM identifier
--     * Slot: mesh_id Description: Unique MeSH identifier
--     * Slot: ncit_id Description: Unique NCIt Identifier
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
--     * Slot: DataTopicContainer_id Description: Autocreated FK slot
-- # Class: "DataTopicContainer" Description: "A container for DataTopics."
--     * Slot: id Description: 
-- # Class: "Organization" Description: "Represents a group or organization related to or responsible for one or more Bridge2AI standards."
--     * Slot: ror_id Description: Unique ROR identifier.
--     * Slot: wikidata_id Description: Unique Wikidata identifier.
--     * Slot: url Description: URL for basic documentation of the standard or tool.
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
--     * Slot: OrganizationContainer_id Description: Autocreated FK slot
-- # Class: "OrganizationContainer" Description: "A container for Organizations."
--     * Slot: id Description: 
-- # Class: "UseCase" Description: "Represents a use case for Bridge2AI standards."
--     * Slot: known_limitations Description: Any current obstacles to implementing this use case. This could be a selection from one or more predefined categories including lack of standards, lack of relevant patient cohort, lack of funding, etc.
--     * Slot: involved_in_experimental_design Description: True if use case is likely to be implemented as part of an experimental procedure or collection of data to be used as part of an experiment.
--     * Slot: involved_in_metadata_management Description: True if use case is likely to be implemented as part of metadata indexing, sample tracking, or any other storage of high-level data properties. Includes use cases in which metadata will be collected along with data.
--     * Slot: involved_in_quality_control Description: A value of True indicates a use case is likely to be implemented as part of data validation operations.
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: category Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
--     * Slot: contributor_name Description: The name of the person who added this node.
--     * Slot: contributor_github_name Description: The name of the github user who added this node.
--     * Slot: contributor_orcid Description: The ORCiD of the person who added this node.
--     * Slot: contribution_date Description: The date on which the node was added.
--     * Slot: UseCaseContainer_id Description: Autocreated FK slot
-- # Class: "UseCaseContainer" Description: "A container for UseCase."
--     * Slot: id Description: 
-- # Class: "NamedThing_subclass_of" Description: ""
--     * Slot: NamedThing_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "NamedThing_related_to" Description: ""
--     * Slot: NamedThing_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "AnatomicalEntity_subclass_of" Description: ""
--     * Slot: AnatomicalEntity_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "AnatomicalEntity_related_to" Description: ""
--     * Slot: AnatomicalEntity_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "DataStandardOrTool_collection" Description: ""
--     * Slot: DataStandardOrTool_id Description: Autocreated FK slot
--     * Slot: collection Description: Tags for specific sets of standards.
-- # Class: "DataStandardOrTool_concerns_data_topic" Description: ""
--     * Slot: DataStandardOrTool_id Description: Autocreated FK slot
--     * Slot: concerns_data_topic_id Description: Subject standard is generally applied in the context of object data topic.
-- # Class: "DataStandardOrTool_has_relevant_organization" Description: ""
--     * Slot: DataStandardOrTool_id Description: Autocreated FK slot
--     * Slot: has_relevant_organization_id Description: Subject standard is managed or otherwise guided buy the object organization(s).
-- # Class: "DataStandardOrTool_has_training_resource" Description: ""
--     * Slot: DataStandardOrTool_id Description: Autocreated FK slot
--     * Slot: has_training_resource_id Description: Relevant training resources, standard usage manuals, or other documentation for the standard or tool.
-- # Class: "DataStandardOrTool_subclass_of" Description: ""
--     * Slot: DataStandardOrTool_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "DataStandardOrTool_related_to" Description: ""
--     * Slot: DataStandardOrTool_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "DataStandard_collection" Description: ""
--     * Slot: DataStandard_id Description: Autocreated FK slot
--     * Slot: collection Description: Tags for specific sets of standards.
-- # Class: "DataStandard_concerns_data_topic" Description: ""
--     * Slot: DataStandard_id Description: Autocreated FK slot
--     * Slot: concerns_data_topic_id Description: Subject standard is generally applied in the context of object data topic.
-- # Class: "DataStandard_has_relevant_organization" Description: ""
--     * Slot: DataStandard_id Description: Autocreated FK slot
--     * Slot: has_relevant_organization_id Description: Subject standard is managed or otherwise guided buy the object organization(s).
-- # Class: "DataStandard_has_training_resource" Description: ""
--     * Slot: DataStandard_id Description: Autocreated FK slot
--     * Slot: has_training_resource_id Description: Relevant training resources, standard usage manuals, or other documentation for the standard or tool.
-- # Class: "DataStandard_subclass_of" Description: ""
--     * Slot: DataStandard_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "DataStandard_related_to" Description: ""
--     * Slot: DataStandard_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "BiomedicalStandard_collection" Description: ""
--     * Slot: BiomedicalStandard_id Description: Autocreated FK slot
--     * Slot: collection Description: Tags for specific sets of standards.
-- # Class: "BiomedicalStandard_concerns_data_topic" Description: ""
--     * Slot: BiomedicalStandard_id Description: Autocreated FK slot
--     * Slot: concerns_data_topic_id Description: Subject standard is generally applied in the context of object data topic.
-- # Class: "BiomedicalStandard_has_relevant_organization" Description: ""
--     * Slot: BiomedicalStandard_id Description: Autocreated FK slot
--     * Slot: has_relevant_organization_id Description: Subject standard is managed or otherwise guided buy the object organization(s).
-- # Class: "BiomedicalStandard_has_training_resource" Description: ""
--     * Slot: BiomedicalStandard_id Description: Autocreated FK slot
--     * Slot: has_training_resource_id Description: Relevant training resources, standard usage manuals, or other documentation for the standard or tool.
-- # Class: "BiomedicalStandard_subclass_of" Description: ""
--     * Slot: BiomedicalStandard_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "BiomedicalStandard_related_to" Description: ""
--     * Slot: BiomedicalStandard_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "Registry_collection" Description: ""
--     * Slot: Registry_id Description: Autocreated FK slot
--     * Slot: collection Description: Tags for specific sets of standards.
-- # Class: "Registry_concerns_data_topic" Description: ""
--     * Slot: Registry_id Description: Autocreated FK slot
--     * Slot: concerns_data_topic_id Description: Subject standard is generally applied in the context of object data topic.
-- # Class: "Registry_has_relevant_organization" Description: ""
--     * Slot: Registry_id Description: Autocreated FK slot
--     * Slot: has_relevant_organization_id Description: Subject standard is managed or otherwise guided buy the object organization(s).
-- # Class: "Registry_has_training_resource" Description: ""
--     * Slot: Registry_id Description: Autocreated FK slot
--     * Slot: has_training_resource_id Description: Relevant training resources, standard usage manuals, or other documentation for the standard or tool.
-- # Class: "Registry_subclass_of" Description: ""
--     * Slot: Registry_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "Registry_related_to" Description: ""
--     * Slot: Registry_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "OntologyOrVocabulary_collection" Description: ""
--     * Slot: OntologyOrVocabulary_id Description: Autocreated FK slot
--     * Slot: collection Description: Tags for specific sets of standards.
-- # Class: "OntologyOrVocabulary_concerns_data_topic" Description: ""
--     * Slot: OntologyOrVocabulary_id Description: Autocreated FK slot
--     * Slot: concerns_data_topic_id Description: Subject standard is generally applied in the context of object data topic.
-- # Class: "OntologyOrVocabulary_has_relevant_organization" Description: ""
--     * Slot: OntologyOrVocabulary_id Description: Autocreated FK slot
--     * Slot: has_relevant_organization_id Description: Subject standard is managed or otherwise guided buy the object organization(s).
-- # Class: "OntologyOrVocabulary_has_training_resource" Description: ""
--     * Slot: OntologyOrVocabulary_id Description: Autocreated FK slot
--     * Slot: has_training_resource_id Description: Relevant training resources, standard usage manuals, or other documentation for the standard or tool.
-- # Class: "OntologyOrVocabulary_subclass_of" Description: ""
--     * Slot: OntologyOrVocabulary_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "OntologyOrVocabulary_related_to" Description: ""
--     * Slot: OntologyOrVocabulary_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "ModelRepository_collection" Description: ""
--     * Slot: ModelRepository_id Description: Autocreated FK slot
--     * Slot: collection Description: Tags for specific sets of standards.
-- # Class: "ModelRepository_concerns_data_topic" Description: ""
--     * Slot: ModelRepository_id Description: Autocreated FK slot
--     * Slot: concerns_data_topic_id Description: Subject standard is generally applied in the context of object data topic.
-- # Class: "ModelRepository_has_relevant_organization" Description: ""
--     * Slot: ModelRepository_id Description: Autocreated FK slot
--     * Slot: has_relevant_organization_id Description: Subject standard is managed or otherwise guided buy the object organization(s).
-- # Class: "ModelRepository_has_training_resource" Description: ""
--     * Slot: ModelRepository_id Description: Autocreated FK slot
--     * Slot: has_training_resource_id Description: Relevant training resources, standard usage manuals, or other documentation for the standard or tool.
-- # Class: "ModelRepository_subclass_of" Description: ""
--     * Slot: ModelRepository_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "ModelRepository_related_to" Description: ""
--     * Slot: ModelRepository_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "ReferenceDataOrDataset_collection" Description: ""
--     * Slot: ReferenceDataOrDataset_id Description: Autocreated FK slot
--     * Slot: collection Description: Tags for specific sets of standards.
-- # Class: "ReferenceDataOrDataset_concerns_data_topic" Description: ""
--     * Slot: ReferenceDataOrDataset_id Description: Autocreated FK slot
--     * Slot: concerns_data_topic_id Description: Subject standard is generally applied in the context of object data topic.
-- # Class: "ReferenceDataOrDataset_has_relevant_organization" Description: ""
--     * Slot: ReferenceDataOrDataset_id Description: Autocreated FK slot
--     * Slot: has_relevant_organization_id Description: Subject standard is managed or otherwise guided buy the object organization(s).
-- # Class: "ReferenceDataOrDataset_has_training_resource" Description: ""
--     * Slot: ReferenceDataOrDataset_id Description: Autocreated FK slot
--     * Slot: has_training_resource_id Description: Relevant training resources, standard usage manuals, or other documentation for the standard or tool.
-- # Class: "ReferenceDataOrDataset_subclass_of" Description: ""
--     * Slot: ReferenceDataOrDataset_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "ReferenceDataOrDataset_related_to" Description: ""
--     * Slot: ReferenceDataOrDataset_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "SoftwareOrTool_collection" Description: ""
--     * Slot: SoftwareOrTool_id Description: Autocreated FK slot
--     * Slot: collection Description: Tags for specific sets of standards.
-- # Class: "SoftwareOrTool_concerns_data_topic" Description: ""
--     * Slot: SoftwareOrTool_id Description: Autocreated FK slot
--     * Slot: concerns_data_topic_id Description: Subject standard is generally applied in the context of object data topic.
-- # Class: "SoftwareOrTool_has_relevant_organization" Description: ""
--     * Slot: SoftwareOrTool_id Description: Autocreated FK slot
--     * Slot: has_relevant_organization_id Description: Subject standard is managed or otherwise guided buy the object organization(s).
-- # Class: "SoftwareOrTool_has_training_resource" Description: ""
--     * Slot: SoftwareOrTool_id Description: Autocreated FK slot
--     * Slot: has_training_resource_id Description: Relevant training resources, standard usage manuals, or other documentation for the standard or tool.
-- # Class: "SoftwareOrTool_subclass_of" Description: ""
--     * Slot: SoftwareOrTool_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "SoftwareOrTool_related_to" Description: ""
--     * Slot: SoftwareOrTool_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "ReferenceImplementation_collection" Description: ""
--     * Slot: ReferenceImplementation_id Description: Autocreated FK slot
--     * Slot: collection Description: Tags for specific sets of standards.
-- # Class: "ReferenceImplementation_concerns_data_topic" Description: ""
--     * Slot: ReferenceImplementation_id Description: Autocreated FK slot
--     * Slot: concerns_data_topic_id Description: Subject standard is generally applied in the context of object data topic.
-- # Class: "ReferenceImplementation_has_relevant_organization" Description: ""
--     * Slot: ReferenceImplementation_id Description: Autocreated FK slot
--     * Slot: has_relevant_organization_id Description: Subject standard is managed or otherwise guided buy the object organization(s).
-- # Class: "ReferenceImplementation_has_training_resource" Description: ""
--     * Slot: ReferenceImplementation_id Description: Autocreated FK slot
--     * Slot: has_training_resource_id Description: Relevant training resources, standard usage manuals, or other documentation for the standard or tool.
-- # Class: "ReferenceImplementation_subclass_of" Description: ""
--     * Slot: ReferenceImplementation_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "ReferenceImplementation_related_to" Description: ""
--     * Slot: ReferenceImplementation_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "TrainingProgram_collection" Description: ""
--     * Slot: TrainingProgram_id Description: Autocreated FK slot
--     * Slot: collection Description: Tags for specific sets of standards.
-- # Class: "TrainingProgram_concerns_data_topic" Description: ""
--     * Slot: TrainingProgram_id Description: Autocreated FK slot
--     * Slot: concerns_data_topic_id Description: Subject standard is generally applied in the context of object data topic.
-- # Class: "TrainingProgram_has_relevant_organization" Description: ""
--     * Slot: TrainingProgram_id Description: Autocreated FK slot
--     * Slot: has_relevant_organization_id Description: Subject standard is managed or otherwise guided buy the object organization(s).
-- # Class: "TrainingProgram_has_training_resource" Description: ""
--     * Slot: TrainingProgram_id Description: Autocreated FK slot
--     * Slot: has_training_resource_id Description: Relevant training resources, standard usage manuals, or other documentation for the standard or tool.
-- # Class: "TrainingProgram_subclass_of" Description: ""
--     * Slot: TrainingProgram_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "TrainingProgram_related_to" Description: ""
--     * Slot: TrainingProgram_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "DataSubstrate_metadata_storage" Description: ""
--     * Slot: DataSubstrate_id Description: Autocreated FK slot
--     * Slot: metadata_storage Description: Data Substrate in which metadata is stored.
-- # Class: "DataSubstrate_file_extensions" Description: ""
--     * Slot: DataSubstrate_id Description: Autocreated FK slot
--     * Slot: file_extensions Description: Commonly used file extensions for this substrate.
-- # Class: "DataSubstrate_limitations" Description: ""
--     * Slot: DataSubstrate_id Description: Autocreated FK slot
--     * Slot: limitations Description: Potential obstacles particular to this substrate or implementation.
-- # Class: "DataSubstrate_subclass_of" Description: ""
--     * Slot: DataSubstrate_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "DataSubstrate_related_to" Description: ""
--     * Slot: DataSubstrate_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "DataTopic_topic_involves_anatomy" Description: ""
--     * Slot: DataTopic_id Description: Autocreated FK slot
--     * Slot: topic_involves_anatomy_id Description: A relationship between a DataTopic and an anatomical entity.
-- # Class: "DataTopic_subclass_of" Description: ""
--     * Slot: DataTopic_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "DataTopic_related_to" Description: ""
--     * Slot: DataTopic_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "Organization_related_to" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.
-- # Class: "Organization_subclass_of" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "UseCase_use_case_category" Description: ""
--     * Slot: UseCase_id Description: Autocreated FK slot
--     * Slot: use_case_category Description: Category of the UseCase. Not all projects will incorporate use cases in all categories. This is multivalued, as a use case may span categories.
-- # Class: "UseCase_relevance_to_dgps" Description: ""
--     * Slot: UseCase_id Description: Autocreated FK slot
--     * Slot: relevance_to_dgps Description: Relevance of the use case to one or more DGPs.
-- # Class: "UseCase_data_topics" Description: ""
--     * Slot: UseCase_id Description: Autocreated FK slot
--     * Slot: data_topics_id Description: Relevance of the use case to one or more data topics.
-- # Class: "UseCase_data_substrates" Description: ""
--     * Slot: UseCase_id Description: Autocreated FK slot
--     * Slot: data_substrates_id Description: Relevance of the use case to one or more data substrates.
-- # Class: "UseCase_standards_and_tools_for_dgp_use" Description: ""
--     * Slot: UseCase_id Description: Autocreated FK slot
--     * Slot: standards_and_tools_for_dgp_use_id Description: List of identifiers of standards and tools; those planned to be used, or already in use, by one or more Bridge2AI DGPs in addressing this use case, from those in the Standards Registry. If no value is provided here, the use case may not have a direct relationship to a standard or tool.
-- # Class: "UseCase_alternative_standards_and_tools" Description: ""
--     * Slot: UseCase_id Description: Autocreated FK slot
--     * Slot: alternative_standards_and_tools_id Description: List of identifiers of standards and tools; those not explicitly planned to be used, by one or more Bridge2AI DGPs in addressing this use case but serving as viable alternatives, from those in the Standards Registry.
-- # Class: "UseCase_enables" Description: ""
--     * Slot: UseCase_id Description: Autocreated FK slot
--     * Slot: enables_id Description: List of other use case(s) this use case supports or makes possible.
-- # Class: "UseCase_xref" Description: ""
--     * Slot: UseCase_id Description: Autocreated FK slot
--     * Slot: xref Description: URI of corresponding class in an ontology of experimental procedures, in CURIE form.
-- # Class: "UseCase_subclass_of" Description: ""
--     * Slot: UseCase_id Description: Autocreated FK slot
--     * Slot: subclass_of_id Description: Holds between two classes where the domain class is a specialization of the range class.
-- # Class: "UseCase_related_to" Description: ""
--     * Slot: UseCase_id Description: Autocreated FK slot
--     * Slot: related_to_id Description: A relationship that is asserted between two named things.

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	PRIMARY KEY (id)
);
CREATE TABLE "AnatomicalEntity" (
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	PRIMARY KEY (id)
);
CREATE TABLE "DataStandard" (
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	not_relevant_to_dgps BOOLEAN, 
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	PRIMARY KEY (id)
);
CREATE TABLE "BiomedicalStandard" (
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	not_relevant_to_dgps BOOLEAN, 
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	PRIMARY KEY (id)
);
CREATE TABLE "Registry" (
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	not_relevant_to_dgps BOOLEAN, 
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	PRIMARY KEY (id)
);
CREATE TABLE "OntologyOrVocabulary" (
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	not_relevant_to_dgps BOOLEAN, 
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	PRIMARY KEY (id)
);
CREATE TABLE "ModelRepository" (
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	not_relevant_to_dgps BOOLEAN, 
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	PRIMARY KEY (id)
);
CREATE TABLE "ReferenceDataOrDataset" (
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	not_relevant_to_dgps BOOLEAN, 
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	PRIMARY KEY (id)
);
CREATE TABLE "SoftwareOrTool" (
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	not_relevant_to_dgps BOOLEAN, 
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	PRIMARY KEY (id)
);
CREATE TABLE "ReferenceImplementation" (
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	not_relevant_to_dgps BOOLEAN, 
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	PRIMARY KEY (id)
);
CREATE TABLE "TrainingProgram" (
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	not_relevant_to_dgps BOOLEAN, 
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	PRIMARY KEY (id)
);
CREATE TABLE "DataStandardOrToolContainer" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "DataSubstrateContainer" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "DataTopicContainer" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "OrganizationContainer" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "UseCaseContainer" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "DataStandardOrTool" (
	purpose_detail TEXT, 
	is_open BOOLEAN, 
	requires_registration BOOLEAN, 
	url TEXT, 
	publication TEXT, 
	formal_specification TEXT, 
	not_relevant_to_dgps BOOLEAN, 
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	"DataStandardOrToolContainer_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DataStandardOrToolContainer_id") REFERENCES "DataStandardOrToolContainer" (id)
);
CREATE TABLE "DataSubstrate" (
	edam_id TEXT, 
	mesh_id TEXT, 
	ncit_id TEXT, 
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	"DataSubstrateContainer_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DataSubstrateContainer_id") REFERENCES "DataSubstrateContainer" (id)
);
CREATE TABLE "DataTopic" (
	edam_id TEXT, 
	mesh_id TEXT, 
	ncit_id TEXT, 
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	"DataTopicContainer_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DataTopicContainer_id") REFERENCES "DataTopicContainer" (id)
);
CREATE TABLE "Organization" (
	ror_id TEXT, 
	wikidata_id TEXT, 
	url TEXT, 
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	"OrganizationContainer_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("OrganizationContainer_id") REFERENCES "OrganizationContainer" (id)
);
CREATE TABLE "UseCase" (
	known_limitations TEXT, 
	involved_in_experimental_design BOOLEAN, 
	involved_in_metadata_management BOOLEAN, 
	involved_in_quality_control BOOLEAN, 
	id TEXT NOT NULL, 
	category TEXT, 
	name TEXT, 
	description TEXT, 
	contributor_name TEXT, 
	contributor_github_name TEXT, 
	contributor_orcid TEXT, 
	contribution_date DATE, 
	"UseCaseContainer_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("UseCaseContainer_id") REFERENCES "UseCaseContainer" (id)
);
CREATE TABLE "NamedThing_subclass_of" (
	"NamedThing_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("NamedThing_id", subclass_of_id), 
	FOREIGN KEY("NamedThing_id") REFERENCES "NamedThing" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "NamedThing_related_to" (
	"NamedThing_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("NamedThing_id", related_to_id), 
	FOREIGN KEY("NamedThing_id") REFERENCES "NamedThing" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "AnatomicalEntity_subclass_of" (
	"AnatomicalEntity_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("AnatomicalEntity_id", subclass_of_id), 
	FOREIGN KEY("AnatomicalEntity_id") REFERENCES "AnatomicalEntity" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "AnatomicalEntity_related_to" (
	"AnatomicalEntity_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("AnatomicalEntity_id", related_to_id), 
	FOREIGN KEY("AnatomicalEntity_id") REFERENCES "AnatomicalEntity" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "DataStandard_collection" (
	"DataStandard_id" TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY ("DataStandard_id", collection), 
	FOREIGN KEY("DataStandard_id") REFERENCES "DataStandard" (id)
);
CREATE TABLE "DataStandard_subclass_of" (
	"DataStandard_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("DataStandard_id", subclass_of_id), 
	FOREIGN KEY("DataStandard_id") REFERENCES "DataStandard" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "DataStandard_related_to" (
	"DataStandard_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("DataStandard_id", related_to_id), 
	FOREIGN KEY("DataStandard_id") REFERENCES "DataStandard" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "BiomedicalStandard_collection" (
	"BiomedicalStandard_id" TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY ("BiomedicalStandard_id", collection), 
	FOREIGN KEY("BiomedicalStandard_id") REFERENCES "BiomedicalStandard" (id)
);
CREATE TABLE "BiomedicalStandard_subclass_of" (
	"BiomedicalStandard_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("BiomedicalStandard_id", subclass_of_id), 
	FOREIGN KEY("BiomedicalStandard_id") REFERENCES "BiomedicalStandard" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "BiomedicalStandard_related_to" (
	"BiomedicalStandard_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("BiomedicalStandard_id", related_to_id), 
	FOREIGN KEY("BiomedicalStandard_id") REFERENCES "BiomedicalStandard" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "Registry_collection" (
	"Registry_id" TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY ("Registry_id", collection), 
	FOREIGN KEY("Registry_id") REFERENCES "Registry" (id)
);
CREATE TABLE "Registry_subclass_of" (
	"Registry_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("Registry_id", subclass_of_id), 
	FOREIGN KEY("Registry_id") REFERENCES "Registry" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "Registry_related_to" (
	"Registry_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("Registry_id", related_to_id), 
	FOREIGN KEY("Registry_id") REFERENCES "Registry" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "OntologyOrVocabulary_collection" (
	"OntologyOrVocabulary_id" TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY ("OntologyOrVocabulary_id", collection), 
	FOREIGN KEY("OntologyOrVocabulary_id") REFERENCES "OntologyOrVocabulary" (id)
);
CREATE TABLE "OntologyOrVocabulary_subclass_of" (
	"OntologyOrVocabulary_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("OntologyOrVocabulary_id", subclass_of_id), 
	FOREIGN KEY("OntologyOrVocabulary_id") REFERENCES "OntologyOrVocabulary" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "OntologyOrVocabulary_related_to" (
	"OntologyOrVocabulary_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("OntologyOrVocabulary_id", related_to_id), 
	FOREIGN KEY("OntologyOrVocabulary_id") REFERENCES "OntologyOrVocabulary" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "ModelRepository_collection" (
	"ModelRepository_id" TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY ("ModelRepository_id", collection), 
	FOREIGN KEY("ModelRepository_id") REFERENCES "ModelRepository" (id)
);
CREATE TABLE "ModelRepository_subclass_of" (
	"ModelRepository_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("ModelRepository_id", subclass_of_id), 
	FOREIGN KEY("ModelRepository_id") REFERENCES "ModelRepository" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "ModelRepository_related_to" (
	"ModelRepository_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("ModelRepository_id", related_to_id), 
	FOREIGN KEY("ModelRepository_id") REFERENCES "ModelRepository" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "ReferenceDataOrDataset_collection" (
	"ReferenceDataOrDataset_id" TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY ("ReferenceDataOrDataset_id", collection), 
	FOREIGN KEY("ReferenceDataOrDataset_id") REFERENCES "ReferenceDataOrDataset" (id)
);
CREATE TABLE "ReferenceDataOrDataset_subclass_of" (
	"ReferenceDataOrDataset_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("ReferenceDataOrDataset_id", subclass_of_id), 
	FOREIGN KEY("ReferenceDataOrDataset_id") REFERENCES "ReferenceDataOrDataset" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "ReferenceDataOrDataset_related_to" (
	"ReferenceDataOrDataset_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("ReferenceDataOrDataset_id", related_to_id), 
	FOREIGN KEY("ReferenceDataOrDataset_id") REFERENCES "ReferenceDataOrDataset" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "SoftwareOrTool_collection" (
	"SoftwareOrTool_id" TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY ("SoftwareOrTool_id", collection), 
	FOREIGN KEY("SoftwareOrTool_id") REFERENCES "SoftwareOrTool" (id)
);
CREATE TABLE "SoftwareOrTool_subclass_of" (
	"SoftwareOrTool_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("SoftwareOrTool_id", subclass_of_id), 
	FOREIGN KEY("SoftwareOrTool_id") REFERENCES "SoftwareOrTool" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "SoftwareOrTool_related_to" (
	"SoftwareOrTool_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("SoftwareOrTool_id", related_to_id), 
	FOREIGN KEY("SoftwareOrTool_id") REFERENCES "SoftwareOrTool" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "ReferenceImplementation_collection" (
	"ReferenceImplementation_id" TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY ("ReferenceImplementation_id", collection), 
	FOREIGN KEY("ReferenceImplementation_id") REFERENCES "ReferenceImplementation" (id)
);
CREATE TABLE "ReferenceImplementation_subclass_of" (
	"ReferenceImplementation_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("ReferenceImplementation_id", subclass_of_id), 
	FOREIGN KEY("ReferenceImplementation_id") REFERENCES "ReferenceImplementation" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "ReferenceImplementation_related_to" (
	"ReferenceImplementation_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("ReferenceImplementation_id", related_to_id), 
	FOREIGN KEY("ReferenceImplementation_id") REFERENCES "ReferenceImplementation" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "TrainingProgram_collection" (
	"TrainingProgram_id" TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY ("TrainingProgram_id", collection), 
	FOREIGN KEY("TrainingProgram_id") REFERENCES "TrainingProgram" (id)
);
CREATE TABLE "TrainingProgram_subclass_of" (
	"TrainingProgram_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("TrainingProgram_id", subclass_of_id), 
	FOREIGN KEY("TrainingProgram_id") REFERENCES "TrainingProgram" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "TrainingProgram_related_to" (
	"TrainingProgram_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("TrainingProgram_id", related_to_id), 
	FOREIGN KEY("TrainingProgram_id") REFERENCES "TrainingProgram" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "DataStandardOrTool_collection" (
	"DataStandardOrTool_id" TEXT, 
	collection VARCHAR(24), 
	PRIMARY KEY ("DataStandardOrTool_id", collection), 
	FOREIGN KEY("DataStandardOrTool_id") REFERENCES "DataStandardOrTool" (id)
);
CREATE TABLE "DataStandardOrTool_concerns_data_topic" (
	"DataStandardOrTool_id" TEXT, 
	concerns_data_topic_id TEXT, 
	PRIMARY KEY ("DataStandardOrTool_id", concerns_data_topic_id), 
	FOREIGN KEY("DataStandardOrTool_id") REFERENCES "DataStandardOrTool" (id), 
	FOREIGN KEY(concerns_data_topic_id) REFERENCES "DataTopic" (id)
);
CREATE TABLE "DataStandardOrTool_has_relevant_organization" (
	"DataStandardOrTool_id" TEXT, 
	has_relevant_organization_id TEXT, 
	PRIMARY KEY ("DataStandardOrTool_id", has_relevant_organization_id), 
	FOREIGN KEY("DataStandardOrTool_id") REFERENCES "DataStandardOrTool" (id), 
	FOREIGN KEY(has_relevant_organization_id) REFERENCES "Organization" (id)
);
CREATE TABLE "DataStandardOrTool_has_training_resource" (
	"DataStandardOrTool_id" TEXT, 
	has_training_resource_id TEXT, 
	PRIMARY KEY ("DataStandardOrTool_id", has_training_resource_id), 
	FOREIGN KEY("DataStandardOrTool_id") REFERENCES "DataStandardOrTool" (id), 
	FOREIGN KEY(has_training_resource_id) REFERENCES "DataStandardOrTool" (id)
);
CREATE TABLE "DataStandardOrTool_subclass_of" (
	"DataStandardOrTool_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("DataStandardOrTool_id", subclass_of_id), 
	FOREIGN KEY("DataStandardOrTool_id") REFERENCES "DataStandardOrTool" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "DataStandardOrTool_related_to" (
	"DataStandardOrTool_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("DataStandardOrTool_id", related_to_id), 
	FOREIGN KEY("DataStandardOrTool_id") REFERENCES "DataStandardOrTool" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "DataStandard_concerns_data_topic" (
	"DataStandard_id" TEXT, 
	concerns_data_topic_id TEXT, 
	PRIMARY KEY ("DataStandard_id", concerns_data_topic_id), 
	FOREIGN KEY("DataStandard_id") REFERENCES "DataStandard" (id), 
	FOREIGN KEY(concerns_data_topic_id) REFERENCES "DataTopic" (id)
);
CREATE TABLE "DataStandard_has_relevant_organization" (
	"DataStandard_id" TEXT, 
	has_relevant_organization_id TEXT, 
	PRIMARY KEY ("DataStandard_id", has_relevant_organization_id), 
	FOREIGN KEY("DataStandard_id") REFERENCES "DataStandard" (id), 
	FOREIGN KEY(has_relevant_organization_id) REFERENCES "Organization" (id)
);
CREATE TABLE "DataStandard_has_training_resource" (
	"DataStandard_id" TEXT, 
	has_training_resource_id TEXT, 
	PRIMARY KEY ("DataStandard_id", has_training_resource_id), 
	FOREIGN KEY("DataStandard_id") REFERENCES "DataStandard" (id), 
	FOREIGN KEY(has_training_resource_id) REFERENCES "DataStandardOrTool" (id)
);
CREATE TABLE "BiomedicalStandard_concerns_data_topic" (
	"BiomedicalStandard_id" TEXT, 
	concerns_data_topic_id TEXT, 
	PRIMARY KEY ("BiomedicalStandard_id", concerns_data_topic_id), 
	FOREIGN KEY("BiomedicalStandard_id") REFERENCES "BiomedicalStandard" (id), 
	FOREIGN KEY(concerns_data_topic_id) REFERENCES "DataTopic" (id)
);
CREATE TABLE "BiomedicalStandard_has_relevant_organization" (
	"BiomedicalStandard_id" TEXT, 
	has_relevant_organization_id TEXT, 
	PRIMARY KEY ("BiomedicalStandard_id", has_relevant_organization_id), 
	FOREIGN KEY("BiomedicalStandard_id") REFERENCES "BiomedicalStandard" (id), 
	FOREIGN KEY(has_relevant_organization_id) REFERENCES "Organization" (id)
);
CREATE TABLE "BiomedicalStandard_has_training_resource" (
	"BiomedicalStandard_id" TEXT, 
	has_training_resource_id TEXT, 
	PRIMARY KEY ("BiomedicalStandard_id", has_training_resource_id), 
	FOREIGN KEY("BiomedicalStandard_id") REFERENCES "BiomedicalStandard" (id), 
	FOREIGN KEY(has_training_resource_id) REFERENCES "DataStandardOrTool" (id)
);
CREATE TABLE "Registry_concerns_data_topic" (
	"Registry_id" TEXT, 
	concerns_data_topic_id TEXT, 
	PRIMARY KEY ("Registry_id", concerns_data_topic_id), 
	FOREIGN KEY("Registry_id") REFERENCES "Registry" (id), 
	FOREIGN KEY(concerns_data_topic_id) REFERENCES "DataTopic" (id)
);
CREATE TABLE "Registry_has_relevant_organization" (
	"Registry_id" TEXT, 
	has_relevant_organization_id TEXT, 
	PRIMARY KEY ("Registry_id", has_relevant_organization_id), 
	FOREIGN KEY("Registry_id") REFERENCES "Registry" (id), 
	FOREIGN KEY(has_relevant_organization_id) REFERENCES "Organization" (id)
);
CREATE TABLE "Registry_has_training_resource" (
	"Registry_id" TEXT, 
	has_training_resource_id TEXT, 
	PRIMARY KEY ("Registry_id", has_training_resource_id), 
	FOREIGN KEY("Registry_id") REFERENCES "Registry" (id), 
	FOREIGN KEY(has_training_resource_id) REFERENCES "DataStandardOrTool" (id)
);
CREATE TABLE "OntologyOrVocabulary_concerns_data_topic" (
	"OntologyOrVocabulary_id" TEXT, 
	concerns_data_topic_id TEXT, 
	PRIMARY KEY ("OntologyOrVocabulary_id", concerns_data_topic_id), 
	FOREIGN KEY("OntologyOrVocabulary_id") REFERENCES "OntologyOrVocabulary" (id), 
	FOREIGN KEY(concerns_data_topic_id) REFERENCES "DataTopic" (id)
);
CREATE TABLE "OntologyOrVocabulary_has_relevant_organization" (
	"OntologyOrVocabulary_id" TEXT, 
	has_relevant_organization_id TEXT, 
	PRIMARY KEY ("OntologyOrVocabulary_id", has_relevant_organization_id), 
	FOREIGN KEY("OntologyOrVocabulary_id") REFERENCES "OntologyOrVocabulary" (id), 
	FOREIGN KEY(has_relevant_organization_id) REFERENCES "Organization" (id)
);
CREATE TABLE "OntologyOrVocabulary_has_training_resource" (
	"OntologyOrVocabulary_id" TEXT, 
	has_training_resource_id TEXT, 
	PRIMARY KEY ("OntologyOrVocabulary_id", has_training_resource_id), 
	FOREIGN KEY("OntologyOrVocabulary_id") REFERENCES "OntologyOrVocabulary" (id), 
	FOREIGN KEY(has_training_resource_id) REFERENCES "DataStandardOrTool" (id)
);
CREATE TABLE "ModelRepository_concerns_data_topic" (
	"ModelRepository_id" TEXT, 
	concerns_data_topic_id TEXT, 
	PRIMARY KEY ("ModelRepository_id", concerns_data_topic_id), 
	FOREIGN KEY("ModelRepository_id") REFERENCES "ModelRepository" (id), 
	FOREIGN KEY(concerns_data_topic_id) REFERENCES "DataTopic" (id)
);
CREATE TABLE "ModelRepository_has_relevant_organization" (
	"ModelRepository_id" TEXT, 
	has_relevant_organization_id TEXT, 
	PRIMARY KEY ("ModelRepository_id", has_relevant_organization_id), 
	FOREIGN KEY("ModelRepository_id") REFERENCES "ModelRepository" (id), 
	FOREIGN KEY(has_relevant_organization_id) REFERENCES "Organization" (id)
);
CREATE TABLE "ModelRepository_has_training_resource" (
	"ModelRepository_id" TEXT, 
	has_training_resource_id TEXT, 
	PRIMARY KEY ("ModelRepository_id", has_training_resource_id), 
	FOREIGN KEY("ModelRepository_id") REFERENCES "ModelRepository" (id), 
	FOREIGN KEY(has_training_resource_id) REFERENCES "DataStandardOrTool" (id)
);
CREATE TABLE "ReferenceDataOrDataset_concerns_data_topic" (
	"ReferenceDataOrDataset_id" TEXT, 
	concerns_data_topic_id TEXT, 
	PRIMARY KEY ("ReferenceDataOrDataset_id", concerns_data_topic_id), 
	FOREIGN KEY("ReferenceDataOrDataset_id") REFERENCES "ReferenceDataOrDataset" (id), 
	FOREIGN KEY(concerns_data_topic_id) REFERENCES "DataTopic" (id)
);
CREATE TABLE "ReferenceDataOrDataset_has_relevant_organization" (
	"ReferenceDataOrDataset_id" TEXT, 
	has_relevant_organization_id TEXT, 
	PRIMARY KEY ("ReferenceDataOrDataset_id", has_relevant_organization_id), 
	FOREIGN KEY("ReferenceDataOrDataset_id") REFERENCES "ReferenceDataOrDataset" (id), 
	FOREIGN KEY(has_relevant_organization_id) REFERENCES "Organization" (id)
);
CREATE TABLE "ReferenceDataOrDataset_has_training_resource" (
	"ReferenceDataOrDataset_id" TEXT, 
	has_training_resource_id TEXT, 
	PRIMARY KEY ("ReferenceDataOrDataset_id", has_training_resource_id), 
	FOREIGN KEY("ReferenceDataOrDataset_id") REFERENCES "ReferenceDataOrDataset" (id), 
	FOREIGN KEY(has_training_resource_id) REFERENCES "DataStandardOrTool" (id)
);
CREATE TABLE "SoftwareOrTool_concerns_data_topic" (
	"SoftwareOrTool_id" TEXT, 
	concerns_data_topic_id TEXT, 
	PRIMARY KEY ("SoftwareOrTool_id", concerns_data_topic_id), 
	FOREIGN KEY("SoftwareOrTool_id") REFERENCES "SoftwareOrTool" (id), 
	FOREIGN KEY(concerns_data_topic_id) REFERENCES "DataTopic" (id)
);
CREATE TABLE "SoftwareOrTool_has_relevant_organization" (
	"SoftwareOrTool_id" TEXT, 
	has_relevant_organization_id TEXT, 
	PRIMARY KEY ("SoftwareOrTool_id", has_relevant_organization_id), 
	FOREIGN KEY("SoftwareOrTool_id") REFERENCES "SoftwareOrTool" (id), 
	FOREIGN KEY(has_relevant_organization_id) REFERENCES "Organization" (id)
);
CREATE TABLE "SoftwareOrTool_has_training_resource" (
	"SoftwareOrTool_id" TEXT, 
	has_training_resource_id TEXT, 
	PRIMARY KEY ("SoftwareOrTool_id", has_training_resource_id), 
	FOREIGN KEY("SoftwareOrTool_id") REFERENCES "SoftwareOrTool" (id), 
	FOREIGN KEY(has_training_resource_id) REFERENCES "DataStandardOrTool" (id)
);
CREATE TABLE "ReferenceImplementation_concerns_data_topic" (
	"ReferenceImplementation_id" TEXT, 
	concerns_data_topic_id TEXT, 
	PRIMARY KEY ("ReferenceImplementation_id", concerns_data_topic_id), 
	FOREIGN KEY("ReferenceImplementation_id") REFERENCES "ReferenceImplementation" (id), 
	FOREIGN KEY(concerns_data_topic_id) REFERENCES "DataTopic" (id)
);
CREATE TABLE "ReferenceImplementation_has_relevant_organization" (
	"ReferenceImplementation_id" TEXT, 
	has_relevant_organization_id TEXT, 
	PRIMARY KEY ("ReferenceImplementation_id", has_relevant_organization_id), 
	FOREIGN KEY("ReferenceImplementation_id") REFERENCES "ReferenceImplementation" (id), 
	FOREIGN KEY(has_relevant_organization_id) REFERENCES "Organization" (id)
);
CREATE TABLE "ReferenceImplementation_has_training_resource" (
	"ReferenceImplementation_id" TEXT, 
	has_training_resource_id TEXT, 
	PRIMARY KEY ("ReferenceImplementation_id", has_training_resource_id), 
	FOREIGN KEY("ReferenceImplementation_id") REFERENCES "ReferenceImplementation" (id), 
	FOREIGN KEY(has_training_resource_id) REFERENCES "DataStandardOrTool" (id)
);
CREATE TABLE "TrainingProgram_concerns_data_topic" (
	"TrainingProgram_id" TEXT, 
	concerns_data_topic_id TEXT, 
	PRIMARY KEY ("TrainingProgram_id", concerns_data_topic_id), 
	FOREIGN KEY("TrainingProgram_id") REFERENCES "TrainingProgram" (id), 
	FOREIGN KEY(concerns_data_topic_id) REFERENCES "DataTopic" (id)
);
CREATE TABLE "TrainingProgram_has_relevant_organization" (
	"TrainingProgram_id" TEXT, 
	has_relevant_organization_id TEXT, 
	PRIMARY KEY ("TrainingProgram_id", has_relevant_organization_id), 
	FOREIGN KEY("TrainingProgram_id") REFERENCES "TrainingProgram" (id), 
	FOREIGN KEY(has_relevant_organization_id) REFERENCES "Organization" (id)
);
CREATE TABLE "TrainingProgram_has_training_resource" (
	"TrainingProgram_id" TEXT, 
	has_training_resource_id TEXT, 
	PRIMARY KEY ("TrainingProgram_id", has_training_resource_id), 
	FOREIGN KEY("TrainingProgram_id") REFERENCES "TrainingProgram" (id), 
	FOREIGN KEY(has_training_resource_id) REFERENCES "DataStandardOrTool" (id)
);
CREATE TABLE "DataSubstrate_metadata_storage" (
	"DataSubstrate_id" TEXT, 
	metadata_storage TEXT, 
	PRIMARY KEY ("DataSubstrate_id", metadata_storage), 
	FOREIGN KEY("DataSubstrate_id") REFERENCES "DataSubstrate" (id)
);
CREATE TABLE "DataSubstrate_file_extensions" (
	"DataSubstrate_id" TEXT, 
	file_extensions TEXT, 
	PRIMARY KEY ("DataSubstrate_id", file_extensions), 
	FOREIGN KEY("DataSubstrate_id") REFERENCES "DataSubstrate" (id)
);
CREATE TABLE "DataSubstrate_limitations" (
	"DataSubstrate_id" TEXT, 
	limitations TEXT, 
	PRIMARY KEY ("DataSubstrate_id", limitations), 
	FOREIGN KEY("DataSubstrate_id") REFERENCES "DataSubstrate" (id)
);
CREATE TABLE "DataSubstrate_subclass_of" (
	"DataSubstrate_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("DataSubstrate_id", subclass_of_id), 
	FOREIGN KEY("DataSubstrate_id") REFERENCES "DataSubstrate" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "DataSubstrate_related_to" (
	"DataSubstrate_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("DataSubstrate_id", related_to_id), 
	FOREIGN KEY("DataSubstrate_id") REFERENCES "DataSubstrate" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "DataTopic_topic_involves_anatomy" (
	"DataTopic_id" TEXT, 
	topic_involves_anatomy_id TEXT, 
	PRIMARY KEY ("DataTopic_id", topic_involves_anatomy_id), 
	FOREIGN KEY("DataTopic_id") REFERENCES "DataTopic" (id), 
	FOREIGN KEY(topic_involves_anatomy_id) REFERENCES "AnatomicalEntity" (id)
);
CREATE TABLE "DataTopic_subclass_of" (
	"DataTopic_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("DataTopic_id", subclass_of_id), 
	FOREIGN KEY("DataTopic_id") REFERENCES "DataTopic" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "DataTopic_related_to" (
	"DataTopic_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("DataTopic_id", related_to_id), 
	FOREIGN KEY("DataTopic_id") REFERENCES "DataTopic" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "Organization_related_to" (
	"Organization_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("Organization_id", related_to_id), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "Organization_subclass_of" (
	"Organization_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("Organization_id", subclass_of_id), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "UseCase_use_case_category" (
	"UseCase_id" TEXT, 
	use_case_category VARCHAR(15) NOT NULL, 
	PRIMARY KEY ("UseCase_id", use_case_category), 
	FOREIGN KEY("UseCase_id") REFERENCES "UseCase" (id)
);
CREATE TABLE "UseCase_relevance_to_dgps" (
	"UseCase_id" TEXT, 
	relevance_to_dgps VARCHAR(7), 
	PRIMARY KEY ("UseCase_id", relevance_to_dgps), 
	FOREIGN KEY("UseCase_id") REFERENCES "UseCase" (id)
);
CREATE TABLE "UseCase_data_topics" (
	"UseCase_id" TEXT, 
	data_topics_id TEXT, 
	PRIMARY KEY ("UseCase_id", data_topics_id), 
	FOREIGN KEY("UseCase_id") REFERENCES "UseCase" (id), 
	FOREIGN KEY(data_topics_id) REFERENCES "DataTopic" (id)
);
CREATE TABLE "UseCase_data_substrates" (
	"UseCase_id" TEXT, 
	data_substrates_id TEXT, 
	PRIMARY KEY ("UseCase_id", data_substrates_id), 
	FOREIGN KEY("UseCase_id") REFERENCES "UseCase" (id), 
	FOREIGN KEY(data_substrates_id) REFERENCES "DataSubstrate" (id)
);
CREATE TABLE "UseCase_standards_and_tools_for_dgp_use" (
	"UseCase_id" TEXT, 
	standards_and_tools_for_dgp_use_id TEXT, 
	PRIMARY KEY ("UseCase_id", standards_and_tools_for_dgp_use_id), 
	FOREIGN KEY("UseCase_id") REFERENCES "UseCase" (id), 
	FOREIGN KEY(standards_and_tools_for_dgp_use_id) REFERENCES "DataStandardOrTool" (id)
);
CREATE TABLE "UseCase_alternative_standards_and_tools" (
	"UseCase_id" TEXT, 
	alternative_standards_and_tools_id TEXT, 
	PRIMARY KEY ("UseCase_id", alternative_standards_and_tools_id), 
	FOREIGN KEY("UseCase_id") REFERENCES "UseCase" (id), 
	FOREIGN KEY(alternative_standards_and_tools_id) REFERENCES "DataStandardOrTool" (id)
);
CREATE TABLE "UseCase_enables" (
	"UseCase_id" TEXT, 
	enables_id TEXT, 
	PRIMARY KEY ("UseCase_id", enables_id), 
	FOREIGN KEY("UseCase_id") REFERENCES "UseCase" (id), 
	FOREIGN KEY(enables_id) REFERENCES "UseCase" (id)
);
CREATE TABLE "UseCase_xref" (
	"UseCase_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("UseCase_id", xref), 
	FOREIGN KEY("UseCase_id") REFERENCES "UseCase" (id)
);
CREATE TABLE "UseCase_subclass_of" (
	"UseCase_id" TEXT, 
	subclass_of_id TEXT, 
	PRIMARY KEY ("UseCase_id", subclass_of_id), 
	FOREIGN KEY("UseCase_id") REFERENCES "UseCase" (id), 
	FOREIGN KEY(subclass_of_id) REFERENCES "NamedThing" (id)
);
CREATE TABLE "UseCase_related_to" (
	"UseCase_id" TEXT, 
	related_to_id TEXT, 
	PRIMARY KEY ("UseCase_id", related_to_id), 
	FOREIGN KEY("UseCase_id") REFERENCES "UseCase" (id), 
	FOREIGN KEY(related_to_id) REFERENCES "NamedThing" (id)
);