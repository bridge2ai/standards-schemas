
# Class: DataStandard


Represents a general purpose standard in the Bridge2AI Standards Registry.

URI: [https://w3id.org/bridge2ai/standards-schema-all/DataStandard](https://w3id.org/bridge2ai/standards-schema-all/DataStandard)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Organization],[DataTopic],[DataStandardOrTool],[DataStandard&#124;collection(i):StandardsCollectionTag%20*;purpose_detail(i):string%20%3F;is_open(i):boolean%20%3F;requires_registration(i):boolean%20%3F;url(i):uriorcurie%20%3F;publication(i):uriorcurie%20%3F;formal_specification(i):uriorcurie%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F]^-[BiomedicalStandard],[DataStandardOrTool]^-[DataStandard],[BiomedicalStandard])](https://yuml.me/diagram/nofunky;dir:TB/class/[Organization],[DataTopic],[DataStandardOrTool],[DataStandard&#124;collection(i):StandardsCollectionTag%20*;purpose_detail(i):string%20%3F;is_open(i):boolean%20%3F;requires_registration(i):boolean%20%3F;url(i):uriorcurie%20%3F;publication(i):uriorcurie%20%3F;formal_specification(i):uriorcurie%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F]^-[BiomedicalStandard],[DataStandardOrTool]^-[DataStandard],[BiomedicalStandard])

## Parents

 *  is_a: [DataStandardOrTool](DataStandardOrTool.md) - Represents a standard or tool in the Bridge2AI Standards Registry.

## Children

 * [BiomedicalStandard](BiomedicalStandard.md) - Represents a standard in the Bridge2AI Standards Registry with particular applications or relevance to clinical or biomedical research purposes.

## Referenced by Class


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
 * [collection](collection.md)  <sub>0..\*</sub>
     * Description: Tags for specific sets of standards.
     * Range: [StandardsCollectionTag](StandardsCollectionTag.md)
 * [concerns data topic](concerns_data_topic.md)  <sub>0..\*</sub>
     * Description: Subject standard is generally applied in the context of object data topic.
     * Range: [DataTopic](DataTopic.md)
 * [has relevant organization](has_relevant_organization.md)  <sub>0..\*</sub>
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
