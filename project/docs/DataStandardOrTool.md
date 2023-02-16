
# Class: DataStandardOrTool


Represents a standard or tool in the Bridge2AI Standards Registry.

URI: [https://w3id.org/bridge2ai/standards-schema-all/DataStandardOrTool](https://w3id.org/bridge2ai/standards-schema-all/DataStandardOrTool)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TrainingProgram],[SoftwareOrTool],[Registry],[ReferenceImplementation],[ReferenceDataOrDataset],[Organization],[OntologyOrVocabulary],[NamedThing],[ModelRepository],[DataTopic],[Organization]<has_relevant_organization%200..*-%20[DataStandardOrTool&#124;collection:StandardsCollectionTag%20*;purpose_detail:string%20%3F;is_open:boolean%20%3F;requires_registration:boolean%20%3F;url:uriorcurie%20%3F;publication:uriorcurie%20%3F;formal_specification:uriorcurie%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[DataTopic]<concerns_data_topic%200..*-%20[DataStandardOrTool],[UseCase]-%20alternative_standards_and_tools%200..*>[DataStandardOrTool],[DataStandardOrToolContainer]++-%20data_standardortools_collection%200..*>[DataStandardOrTool],[UseCase]-%20standards_and_tools_for_dgp_use%200..*>[DataStandardOrTool],[DataStandardOrTool]^-[TrainingProgram],[DataStandardOrTool]^-[SoftwareOrTool],[DataStandardOrTool]^-[Registry],[DataStandardOrTool]^-[ReferenceImplementation],[DataStandardOrTool]^-[ReferenceDataOrDataset],[DataStandardOrTool]^-[OntologyOrVocabulary],[DataStandardOrTool]^-[ModelRepository],[DataStandardOrTool]^-[DataStandard],[NamedThing]^-[DataStandardOrTool],[UseCase],[DataStandardOrToolContainer],[DataStandard])](https://yuml.me/diagram/nofunky;dir:TB/class/[TrainingProgram],[SoftwareOrTool],[Registry],[ReferenceImplementation],[ReferenceDataOrDataset],[Organization],[OntologyOrVocabulary],[NamedThing],[ModelRepository],[DataTopic],[Organization]<has_relevant_organization%200..*-%20[DataStandardOrTool&#124;collection:StandardsCollectionTag%20*;purpose_detail:string%20%3F;is_open:boolean%20%3F;requires_registration:boolean%20%3F;url:uriorcurie%20%3F;publication:uriorcurie%20%3F;formal_specification:uriorcurie%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[DataTopic]<concerns_data_topic%200..*-%20[DataStandardOrTool],[UseCase]-%20alternative_standards_and_tools%200..*>[DataStandardOrTool],[DataStandardOrToolContainer]++-%20data_standardortools_collection%200..*>[DataStandardOrTool],[UseCase]-%20standards_and_tools_for_dgp_use%200..*>[DataStandardOrTool],[DataStandardOrTool]^-[TrainingProgram],[DataStandardOrTool]^-[SoftwareOrTool],[DataStandardOrTool]^-[Registry],[DataStandardOrTool]^-[ReferenceImplementation],[DataStandardOrTool]^-[ReferenceDataOrDataset],[DataStandardOrTool]^-[OntologyOrVocabulary],[DataStandardOrTool]^-[ModelRepository],[DataStandardOrTool]^-[DataStandard],[NamedThing]^-[DataStandardOrTool],[UseCase],[DataStandardOrToolContainer],[DataStandard])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Children

 * [DataStandard](DataStandard.md) - Represents a general purpose standard in the Bridge2AI Standards Registry.
 * [ModelRepository](ModelRepository.md) - Represents a resource in the Bridge2AI Standards Registry serving to curate and store computational models. To be a respository, the resource must not index models alone.
 * [OntologyOrVocabulary](OntologyOrVocabulary.md) - A set of concepts and categories, potentially defined or accompanied by their hierarchical relationships.
 * [ReferenceDataOrDataset](ReferenceDataOrDataset.md) - Represents a resource in the Bridge2AI Standards Registry serving as a standardized, reusable data source.
 * [ReferenceImplementation](ReferenceImplementation.md) - Represents an implementation of one or more standards or tools in the Bridge2AI Standards Registry, whether as a full specification in a particular language or as an application to a specific use case.
 * [Registry](Registry.md) - Represents a resource in the Bridge2AI Standards Registry serving to curate and/or index other resources.
 * [SoftwareOrTool](SoftwareOrTool.md) - Represents a piece of software or computational tool in the Bridge2AI Standards Registry.
 * [TrainingProgram](TrainingProgram.md) - Represents a training program for skills and experience related to standards or tools in the Bridge2AI Standards Registry.

## Referenced by Class

 *  **[NamedThing](NamedThing.md)** *[alternative_standards_and_tools](alternative_standards_and_tools.md)*  <sub>0..\*</sub>  **[DataStandardOrTool](DataStandardOrTool.md)**
 *  **None** *[data_standardortools_collection](data_standardortools_collection.md)*  <sub>0..\*</sub>  **[DataStandardOrTool](DataStandardOrTool.md)**
 *  **[NamedThing](NamedThing.md)** *[standards_and_tools_for_dgp_use](standards_and_tools_for_dgp_use.md)*  <sub>0..\*</sub>  **[DataStandardOrTool](DataStandardOrTool.md)**

## Attributes


### Own

 * [collection](collection.md)  <sub>0..\*</sub>
     * Description: Tags for specific sets of standards.
     * Range: [StandardsCollectionTag](StandardsCollectionTag.md)
 * [concerns_data_topic](concerns_data_topic.md)  <sub>0..\*</sub>
     * Description: Subject standard is generally applied in the context of object data topic.
     * Range: [DataTopic](DataTopic.md)
 * [has_relevant_organization](has_relevant_organization.md)  <sub>0..\*</sub>
     * Description: Subject standard is managed or otherwise guided buy the object organization(s).
     * Range: [Organization](Organization.md)
 * [purpose_detail](purpose_detail.md)  <sub>0..1</sub>
     * Description: Text description of the standard or tool.
     * Range: [String](types/String.md)
 * [is_open](is_open.md)  <sub>0..1</sub>
     * Description: Is the standard or tool FAIR and available free of cost?
     * Range: [Boolean](types/Boolean.md)
 * [requires_registration](requires_registration.md)  <sub>0..1</sub>
     * Description: Does usage of the standard or tool require registrion of a user or group with some organization or managerial body?
     * Range: [Boolean](types/Boolean.md)
 * [url](url.md)  <sub>0..1</sub>
     * Description: URL for basic documentation of the standard or tool.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [publication](publication.md)  <sub>0..1</sub>
     * Description: Relevant publication for the standard or tool. Prefer a DOI or PUBMED.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [formal_specification](formal_specification.md)  <sub>0..1</sub>
     * Description: Relevant code repository or other location for a formal specification of the standard or tool. Often a URL, particularly to a Git repository.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing.
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing.
     * Range: [String](types/String.md)
 * [subclass_of](subclass_of.md)  <sub>0..\*</sub>
     * Description: Holds between two classes where the domain class is a specialization of the range class.
     * Range: [NamedThing](NamedThing.md)
