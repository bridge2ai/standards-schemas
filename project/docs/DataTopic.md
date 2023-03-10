
# Class: DataTopic


Represents a general data topic for Bridge2AI data or the tools/standards applied to the data.

URI: [https://w3id.org/bridge2ai/standards-schema-all/DataTopic](https://w3id.org/bridge2ai/standards-schema-all/DataTopic)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DataStandardOrTool]-%20concerns_data_topic%200..*>[DataTopic&#124;edam_id:edam_identifier%20%3F;mesh_id:mesh_identifier%20%3F;ncit_id:ncit_identifier%20%3F;id(i):uriorcurie;category(i):category_type%20%3F;name(i):string%20%3F;description(i):string%20%3F],[UseCase]-%20data_topics%200..*>[DataTopic],[DataTopicContainer]++-%20data_topics_collection%200..*>[DataTopic],[NamedThing]^-[DataTopic],[UseCase],[DataTopicContainer],[DataStandardOrTool])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DataStandardOrTool]-%20concerns_data_topic%200..*>[DataTopic&#124;edam_id:edam_identifier%20%3F;mesh_id:mesh_identifier%20%3F;ncit_id:ncit_identifier%20%3F;id(i):uriorcurie;category(i):category_type%20%3F;name(i):string%20%3F;description(i):string%20%3F],[UseCase]-%20data_topics%200..*>[DataTopic],[DataTopicContainer]++-%20data_topics_collection%200..*>[DataTopic],[NamedThing]^-[DataTopic],[UseCase],[DataTopicContainer],[DataStandardOrTool])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Referenced by Class

 *  **[DataStandardOrTool](DataStandardOrTool.md)** *[concerns_data_topic](concerns_data_topic.md)*  <sub>0..\*</sub>  **[DataTopic](DataTopic.md)**
 *  **[NamedThing](NamedThing.md)** *[data_topics](data_topics.md)*  <sub>0..\*</sub>  **[DataTopic](DataTopic.md)**
 *  **None** *[data_topics_collection](data_topics_collection.md)*  <sub>0..\*</sub>  **[DataTopic](DataTopic.md)**

## Attributes


### Own

 * [edam_id](edam_id.md)  <sub>0..1</sub>
     * Range: [EdamIdentifier](types/EdamIdentifier.md)
     * Example: edam.data:0006 None
 * [mesh_id](mesh_id.md)  <sub>0..1</sub>
     * Range: [MeshIdentifier](types/MeshIdentifier.md)
     * Example: MeSH:D014831 None
 * [ncit_id](ncit_id.md)  <sub>0..1</sub>
     * Range: [NcitIdentifier](types/NcitIdentifier.md)
     * Example: NCIT:C92692 None

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
 * [related_to](related_to.md)  <sub>0..\*</sub>
     * Description: A relationship that is asserted between two named things.
     * Range: [NamedThing](NamedThing.md)
