
# Class: Organization


Represents a group or organization related to or responsible for one or more Bridge2AI standards.

URI: [https://w3id.org/bridge2ai/standards-schema-all/Organization](https://w3id.org/bridge2ai/standards-schema-all/Organization)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing]<related_to%200..*-%20[Organization&#124;ROR_ID:ror_identifier%20%3F;Wikidata_ID:wikidata_identifier%20%3F;URL:string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[DataStandardOrTool]-%20has_relevant_organization%200..*>[Organization],[OrganizationContainer]++-%20organizations%200..*>[Organization],[NamedThing]^-[Organization],[OrganizationContainer],[NamedThing],[DataStandardOrTool])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing]<related_to%200..*-%20[Organization&#124;ROR_ID:ror_identifier%20%3F;Wikidata_ID:wikidata_identifier%20%3F;URL:string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[DataStandardOrTool]-%20has_relevant_organization%200..*>[Organization],[OrganizationContainer]++-%20organizations%200..*>[Organization],[NamedThing]^-[Organization],[OrganizationContainer],[NamedThing],[DataStandardOrTool])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Referenced by Class

 *  **[DataStandardOrTool](DataStandardOrTool.md)** *[has_relevant_organization](has_relevant_organization.md)*  <sub>0..\*</sub>  **[Organization](Organization.md)**
 *  **None** *[organizations](organizations.md)*  <sub>0..\*</sub>  **[Organization](Organization.md)**

## Attributes


### Own

 * [ROR_ID](ROR_ID.md)  <sub>0..1</sub>
     * Range: [RorIdentifier](types/RorIdentifier.md)
     * Example: ROR:02mp31p96 None
 * [Wikidata_ID](Wikidata_ID.md)  <sub>0..1</sub>
     * Range: [WikidataIdentifier](types/WikidataIdentifier.md)
     * Example: WIKIDATA:Q282186 None
 * [URL](URL.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: https://www.zeiss.com/ None
 * [related_to](related_to.md)  <sub>0..\*</sub>
     * Description: A relationship that is asserted between two named things.
     * Range: [NamedThing](NamedThing.md)

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
