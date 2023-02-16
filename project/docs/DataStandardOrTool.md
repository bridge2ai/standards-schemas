
# Class: DataStandardOrTool




URI: [https://w3id.org/bridge2ai/standards-schema/DataStandardOrTool](https://w3id.org/bridge2ai/standards-schema/DataStandardOrTool)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Organization],[NamedThing],[DataTopic],[Organization]<has_relevant_organization%200..*-%20[DataStandardOrTool&#124;collection:StandardsCollectionTag%20*;purpose_detail:string%20%3F;is_open:boolean%20%3F;requires_registration:boolean%20%3F;url:uriorcurie%20%3F;publication:uriorcurie%20%3F;formal_specification:uriorcurie%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[DataTopic]<concerns_data_topic%200..*-%20[DataStandardOrTool],[UseCase]-%20alternative_standards_and_tools%200..*>[DataStandardOrTool],[UseCase]-%20standards_and_tools_for_dgp_use%200..*>[DataStandardOrTool],[NamedThing]^-[DataStandardOrTool],[UseCase])](https://yuml.me/diagram/nofunky;dir:TB/class/[Organization],[NamedThing],[DataTopic],[Organization]<has_relevant_organization%200..*-%20[DataStandardOrTool&#124;collection:StandardsCollectionTag%20*;purpose_detail:string%20%3F;is_open:boolean%20%3F;requires_registration:boolean%20%3F;url:uriorcurie%20%3F;publication:uriorcurie%20%3F;formal_specification:uriorcurie%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[DataTopic]<concerns_data_topic%200..*-%20[DataStandardOrTool],[UseCase]-%20alternative_standards_and_tools%200..*>[DataStandardOrTool],[UseCase]-%20standards_and_tools_for_dgp_use%200..*>[DataStandardOrTool],[NamedThing]^-[DataStandardOrTool],[UseCase])

## Parents

 *  is_a: [NamedThing](NamedThing.md)

## Referenced by Class

 *  **[NamedThing](NamedThing.md)** *[alternative_standards_and_tools](alternative_standards_and_tools.md)*  <sub>0..\*</sub>  **[DataStandardOrTool](DataStandardOrTool.md)**
 *  **[NamedThing](NamedThing.md)** *[standards_and_tools_for_dgp_use](standards_and_tools_for_dgp_use.md)*  <sub>0..\*</sub>  **[DataStandardOrTool](DataStandardOrTool.md)**

## Attributes


### Own

 * [collection](collection.md)  <sub>0..\*</sub>
     * Range: [StandardsCollectionTag](StandardsCollectionTag.md)
 * [concerns_data_topic](concerns_data_topic.md)  <sub>0..\*</sub>
     * Range: [DataTopic](DataTopic.md)
 * [has_relevant_organization](has_relevant_organization.md)  <sub>0..\*</sub>
     * Range: [Organization](Organization.md)
 * [purpose_detail](purpose_detail.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [is_open](is_open.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [requires_registration](requires_registration.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [url](url.md)  <sub>0..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [publication](publication.md)  <sub>0..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [formal_specification](formal_specification.md)  <sub>0..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
