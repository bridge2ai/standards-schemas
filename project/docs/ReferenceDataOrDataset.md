
# Class: ReferenceDataOrDataset


Represents a resource in the Bridge2AI Standards Registry serving as a standardized, reusable data source.

URI: [https://w3id.org/bridge2ai/standards-schema-all/ReferenceDataOrDataset](https://w3id.org/bridge2ai/standards-schema-all/ReferenceDataOrDataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DataStandardOrTool]^-[ReferenceDataOrDataset&#124;collection(i):StandardsCollectionTag%20*;purpose_detail(i):string%20%3F;is_open(i):boolean%20%3F;requires_registration(i):boolean%20%3F;url(i):uriorcurie%20%3F;publication(i):uriorcurie%20%3F;formal_specification(i):uriorcurie%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Organization],[NamedThing],[DataTopic],[DataStandardOrTool])](https://yuml.me/diagram/nofunky;dir:TB/class/[DataStandardOrTool]^-[ReferenceDataOrDataset&#124;collection(i):StandardsCollectionTag%20*;purpose_detail(i):string%20%3F;is_open(i):boolean%20%3F;requires_registration(i):boolean%20%3F;url(i):uriorcurie%20%3F;publication(i):uriorcurie%20%3F;formal_specification(i):uriorcurie%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Organization],[NamedThing],[DataTopic],[DataStandardOrTool])

## Parents

 *  is_a: [DataStandardOrTool](DataStandardOrTool.md) - Represents a standard or tool in the Bridge2AI Standards Registry.

## Attributes


### Inherited from DataStandardOrTool:

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
 * [related_to](related_to.md)  <sub>0..\*</sub>
     * Description: A relationship that is asserted between two named things.
     * Range: [NamedThing](NamedThing.md)
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
