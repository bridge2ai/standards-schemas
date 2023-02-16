
# Class: DataTopic




URI: [https://w3id.org/bridge2ai/standards-schema/DataTopic](https://w3id.org/bridge2ai/standards-schema/DataTopic)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DataStandardOrTool]-%20concerns_data_topic%200..*>[DataTopic&#124;EDAM_ID:edam_identifier%20%3F;MeSH_ID:mesh_identifier%20%3F;NCIT_ID:ncit_identifier%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[UseCase]-%20data_topics%200..*>[DataTopic],[NamedThing]^-[DataTopic],[UseCase],[DataStandardOrTool])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DataStandardOrTool]-%20concerns_data_topic%200..*>[DataTopic&#124;EDAM_ID:edam_identifier%20%3F;MeSH_ID:mesh_identifier%20%3F;NCIT_ID:ncit_identifier%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[UseCase]-%20data_topics%200..*>[DataTopic],[NamedThing]^-[DataTopic],[UseCase],[DataStandardOrTool])

## Parents

 *  is_a: [NamedThing](NamedThing.md)

## Referenced by Class

 *  **[DataStandardOrTool](DataStandardOrTool.md)** *[concerns_data_topic](concerns_data_topic.md)*  <sub>0..\*</sub>  **[DataTopic](DataTopic.md)**
 *  **[NamedThing](NamedThing.md)** *[data_topics](data_topics.md)*  <sub>0..\*</sub>  **[DataTopic](DataTopic.md)**

## Attributes


### Own

 * [EDAM_ID](EDAM_ID.md)  <sub>0..1</sub>
     * Range: [EdamIdentifier](types/EdamIdentifier.md)
     * Example: edam.data:0006 None
 * [MeSH_ID](MeSH_ID.md)  <sub>0..1</sub>
     * Range: [MeshIdentifier](types/MeshIdentifier.md)
     * Example: MeSH:D014831 None
 * [NCIT_ID](NCIT_ID.md)  <sub>0..1</sub>
     * Range: [NcitIdentifier](types/NcitIdentifier.md)
     * Example: NCIT:C92692 None

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
