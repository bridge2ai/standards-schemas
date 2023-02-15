
# Class: DataTopic


Represents a general data topic for Bridge2AI data or the tools/standards applied to the data.

URI: [https://w3id.org/bridge2ai/standards-schema-all/DataTopic](https://w3id.org/bridge2ai/standards-schema-all/DataTopic)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DataStandardOrTool]-%20concerns_data_topic%200..*>[DataTopic&#124;EDAM_ID:edam_identifier%20%3F;MeSH_ID:mesh_identifier%20%3F;NCIT_ID:ncit_identifier%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[UseCase]-%20data_topics%200..*>[DataTopic],[NamedThing]^-[DataTopic],[UseCase],[DataStandardOrTool])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DataStandardOrTool]-%20concerns_data_topic%200..*>[DataTopic&#124;EDAM_ID:edam_identifier%20%3F;MeSH_ID:mesh_identifier%20%3F;NCIT_ID:ncit_identifier%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[UseCase]-%20data_topics%200..*>[DataTopic],[NamedThing]^-[DataTopic],[UseCase],[DataStandardOrTool])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

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
