
# Class: AnatomicalEntity

A subcellular location, cell type or gross anatomical part

URI: [https://w3id.org/bridge2ai/standards-schema-all/AnatomicalEntity](https://w3id.org/bridge2ai/standards-schema-all/AnatomicalEntity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DataTopic],[DataTopic]-%20topic_involves_anatomy%200..*>[AnatomicalEntity&#124;id(i):uriorcurie;category(i):category_type%20%3F;name(i):string%20%3F;description(i):string%20%3F;contributor_name(i):string%20%3F;contributor_github_name(i):string%20%3F;contributor_orcid(i):uriorcurie%20%3F;contribution_date(i):date%20%3F],[NamedThing]^-[AnatomicalEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DataTopic],[DataTopic]-%20topic_involves_anatomy%200..*>[AnatomicalEntity&#124;id(i):uriorcurie;category(i):category_type%20%3F;name(i):string%20%3F;description(i):string%20%3F;contributor_name(i):string%20%3F;contributor_github_name(i):string%20%3F;contributor_orcid(i):uriorcurie%20%3F;contribution_date(i):date%20%3F],[NamedThing]^-[AnatomicalEntity])

## Identifier prefixes

 * uberon

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Referenced by Class

 *  **[DataTopic](DataTopic.md)** *[topic_involves_anatomy](topic_involves_anatomy.md)*  <sub>0..\*</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**

## Attributes


### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [category](category.md)  <sub>0..1</sub>
     * Description: CURIE for the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "B2AI_STANDARD:DataStandard".
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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | uberon:0001062 |
|  | | wikidata:Q4936952 |
| **Narrow Mappings:** | | ncit:C12219 |