
# Class: ModelRepository


Represents a resource in the Bridge2AI Standards Registry serving to curate and store computational models. To be a respository, the resource must not index models alone.

URI: [https://w3id.org/bridge2ai/standards-schema-all/ModelRepository](https://w3id.org/bridge2ai/standards-schema-all/ModelRepository)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Organization],[NamedThing],[DataStandardOrTool]^-[ModelRepository&#124;collection(i):StandardsCollectionTag%20*;purpose_detail(i):string%20%3F;is_open(i):boolean%20%3F;requires_registration(i):boolean%20%3F;url(i):uriorcurie%20%3F;publication(i):uriorcurie%20%3F;formal_specification(i):uriorcurie%20%3F;not_relevant_to_dgps(i):boolean%20%3F;id(i):uriorcurie;category(i):category_type%20%3F;name(i):string%20%3F;description(i):string%20%3F;contributor_name(i):string%20%3F;contributor_github_name(i):string%20%3F;contributor_orcid(i):uriorcurie%20%3F;contribution_date(i):date%20%3F],[DataTopic],[DataStandardOrTool])](https://yuml.me/diagram/nofunky;dir:TB/class/[Organization],[NamedThing],[DataStandardOrTool]^-[ModelRepository&#124;collection(i):StandardsCollectionTag%20*;purpose_detail(i):string%20%3F;is_open(i):boolean%20%3F;requires_registration(i):boolean%20%3F;url(i):uriorcurie%20%3F;publication(i):uriorcurie%20%3F;formal_specification(i):uriorcurie%20%3F;not_relevant_to_dgps(i):boolean%20%3F;id(i):uriorcurie;category(i):category_type%20%3F;name(i):string%20%3F;description(i):string%20%3F;contributor_name(i):string%20%3F;contributor_github_name(i):string%20%3F;contributor_orcid(i):uriorcurie%20%3F;contribution_date(i):date%20%3F],[DataTopic],[DataStandardOrTool])

## Parents

 *  is_a: [DataStandardOrTool](DataStandardOrTool.md) - Represents a standard or tool in the Bridge2AI Standards Registry.

## Attributes


### Inherited from DataStandardOrTool:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [category](category.md)  <sub>0..1</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
     * Range: [CategoryType](types/CategoryType.md)
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
 * [contributor_name](contributor_name.md)  <sub>0..1</sub>
     * Description: The name of the person who added this node.
     * Range: [String](types/String.md)
 * [contributor_github_name](contributor_github_name.md)  <sub>0..1</sub>
     * Description: The name of the github user who added this node.
     * Range: [String](types/String.md)
 * [contributor_orcid](contributor_orcid.md)  <sub>0..1</sub>
     * Description: The ORCiD of the person who added this node.
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * Example: ORCID:0000-0001-1234-5678 None
 * [contribution_date](contribution_date.md)  <sub>0..1</sub>
     * Description: The date on which the node was added.
     * Range: [Date](types/Date.md)
     * Example: 2023-03-20 None
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
 * [not_relevant_to_dgps](not_relevant_to_dgps.md)  <sub>0..1</sub>
     * Description: Is the standard or tool currently relevant to DGPs?
     * Range: [Boolean](types/Boolean.md)
