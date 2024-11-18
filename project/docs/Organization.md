
# Class: Organization

Represents a group or organization related to or responsible for one or more Bridge2AI standards.

URI: [https://w3id.org/bridge2ai/standards-schema-all/Organization](https://w3id.org/bridge2ai/standards-schema-all/Organization)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing]<related_to(i)%200..*-%20[Organization&#124;ror_id:ror_identifier%20%3F;wikidata_id:wikidata_identifier%20%3F;url:uriorcurie%20%3F;id(i):uriorcurie;category(i):category_type%20%3F;name(i):string%20%3F;description(i):string%20%3F;contributor_name(i):string%20%3F;contributor_github_name(i):string%20%3F;contributor_orcid(i):uriorcurie%20%3F;contribution_date(i):date%20%3F],[DataStandardOrTool]-%20has_relevant_organization%200..*>[Organization],[OrganizationContainer]++-%20organizations%200..*>[Organization],[NamedThing]^-[Organization],[OrganizationContainer],[NamedThing],[DataStandardOrTool])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing]<related_to(i)%200..*-%20[Organization&#124;ror_id:ror_identifier%20%3F;wikidata_id:wikidata_identifier%20%3F;url:uriorcurie%20%3F;id(i):uriorcurie;category(i):category_type%20%3F;name(i):string%20%3F;description(i):string%20%3F;contributor_name(i):string%20%3F;contributor_github_name(i):string%20%3F;contributor_orcid(i):uriorcurie%20%3F;contribution_date(i):date%20%3F],[DataStandardOrTool]-%20has_relevant_organization%200..*>[Organization],[OrganizationContainer]++-%20organizations%200..*>[Organization],[NamedThing]^-[Organization],[OrganizationContainer],[NamedThing],[DataStandardOrTool])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Referenced by Class

 *  **[DataStandardOrTool](DataStandardOrTool.md)** *[has_relevant_organization](has_relevant_organization.md)*  <sub>0..\*</sub>  **[Organization](Organization.md)**
 *  **None** *[organizations](organizations.md)*  <sub>0..\*</sub>  **[Organization](Organization.md)**

## Attributes


### Own

 * [ror_id](ror_id.md)  <sub>0..1</sub>
     * Description: Unique ROR identifier.
     * Range: [RorIdentifier](types/RorIdentifier.md)
     * Example: ROR:02mp31p96 None
 * [wikidata_id](wikidata_id.md)  <sub>0..1</sub>
     * Description: Unique Wikidata identifier.
     * Range: [WikidataIdentifier](types/WikidataIdentifier.md)
     * Example: WIKIDATA:Q282186 None
 * [url](url.md)  <sub>0..1</sub>
     * Description: URL for basic documentation of the standard or tool.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [related_to](related_to.md)  <sub>0..\*</sub>
     * Description: A relationship that is asserted between two named things.
     * Range: [NamedThing](NamedThing.md)

### Inherited from NamedThing:

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
