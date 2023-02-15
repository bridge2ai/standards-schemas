
# Class: NamedThing


A generic grouping for any identifiable entity

URI: [https://w3id.org/bridge2ai/standards-schema-all/NamedThing](https://w3id.org/bridge2ai/standards-schema-all/NamedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[UseCase],[Organization],[NamedThing]<subclass_of%200..*-%20[NamedThing&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F],[Organization]-%20related_to%200..*>[NamedThing],[NamedThing]^-[UseCase],[NamedThing]^-[Organization],[NamedThing]^-[DataTopic],[NamedThing]^-[DataSubstrate],[NamedThing]^-[DataStandardOrTool],[DataTopic],[DataSubstrate],[DataStandardOrTool])](https://yuml.me/diagram/nofunky;dir:TB/class/[UseCase],[Organization],[NamedThing]<subclass_of%200..*-%20[NamedThing&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F],[Organization]-%20related_to%200..*>[NamedThing],[NamedThing]^-[UseCase],[NamedThing]^-[Organization],[NamedThing]^-[DataTopic],[NamedThing]^-[DataSubstrate],[NamedThing]^-[DataStandardOrTool],[DataTopic],[DataSubstrate],[DataStandardOrTool])

## Children

 * [DataStandardOrTool](DataStandardOrTool.md) - Represents a standard or tool in the Bridge2AI Standards Registry.
 * [DataSubstrate](DataSubstrate.md) - Represents a data substrate for Bridge2AI data. This may be a high-level data structure or a specific implementation of that structure. Interpret as "data, in this form or format", as compared to DataStandard, which refers to the set of rules defining a standard. For example, data in TSV format is represented as a DataSubstrate but the concept of TSV format is a DataStandard.
 * [DataTopic](DataTopic.md) - Represents a general data topic for Bridge2AI data or the tools/standards applied to the data.
 * [Organization](Organization.md) - Represents a group or organization related to or responsible for one or more Bridge2AI standards.
 * [UseCase](UseCase.md) - Represents a use case for Bridge2AI standards.

## Referenced by Class

 *  **[NamedThing](NamedThing.md)** *[related_to](related_to.md)*  <sub>0..\*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[subclass_of](subclass_of.md)*  <sub>0..\*</sub>  **[NamedThing](NamedThing.md)**

## Attributes


### Own

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | schema:Thing |

