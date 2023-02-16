
# Class: NamedThing




URI: [https://w3id.org/bridge2ai/standards-schema/NamedThing](https://w3id.org/bridge2ai/standards-schema/NamedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[UseCase],[Organization],[Organization]-%20related_to%200..*>[NamedThing&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F],[NamedThing]^-[UseCase],[NamedThing]^-[Organization],[NamedThing]^-[DataTopic],[NamedThing]^-[DataSubstrate],[NamedThing]^-[DataStandardOrTool],[DataTopic],[DataSubstrate],[DataStandardOrTool])](https://yuml.me/diagram/nofunky;dir:TB/class/[UseCase],[Organization],[Organization]-%20related_to%200..*>[NamedThing&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F],[NamedThing]^-[UseCase],[NamedThing]^-[Organization],[NamedThing]^-[DataTopic],[NamedThing]^-[DataSubstrate],[NamedThing]^-[DataStandardOrTool],[DataTopic],[DataSubstrate],[DataStandardOrTool])

## Children

 * [DataStandardOrTool](DataStandardOrTool.md)
 * [DataSubstrate](DataSubstrate.md)
 * [DataTopic](DataTopic.md)
 * [Organization](Organization.md)
 * [UseCase](UseCase.md)

## Referenced by Class

 *  **[NamedThing](NamedThing.md)** *[related_to](related_to.md)*  <sub>0..\*</sub>  **[NamedThing](NamedThing.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
