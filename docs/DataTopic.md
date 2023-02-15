# Class: DataTopic
_Represents a general data topic for Bridge2AI data or the tools/standards applied to the data._




URI: [STANDARDSDATATOPIC:DataTopic](https://w3id.org/bridge2ai/standards-datatopic-schema/DataTopic)



```mermaid
 classDiagram
    class DataTopic
      NamedThing <|-- DataTopic
      
      DataTopic : description
      DataTopic : EDAM_ID
      DataTopic : id
      DataTopic : MeSH_ID
      DataTopic : name
      DataTopic : NCIT_ID
      DataTopic : subclass_of
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **DataTopic**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [EDAM_ID](EDAM_ID.md) | 0..1 <br/> [EdamIdentifier](EdamIdentifier.md) |  | direct |
| [MeSH_ID](MeSH_ID.md) | 0..1 <br/> [MeshIdentifier](MeshIdentifier.md) |  | direct |
| [NCIT_ID](NCIT_ID.md) | 0..1 <br/> [NcitIdentifier](NcitIdentifier.md) |  | direct |
| [id](id.md) | 1..1 <br/> [xsd:anyURI](xsd:anyURI) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [xsd:string](xsd:string) | A human-readable name for a thing | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [xsd:string](xsd:string) | A human-readable description for a thing | [NamedThing](NamedThing.md) |
| [subclass_of](subclass_of.md) | 0..* <br/> [NamedThing](NamedThing.md) | Holds between two classes where the domain class is a specialization of the r... | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [UseCase](UseCase.md) | [data_topics](data_topics.md) | range | [DataTopic](DataTopic.md) |
| [DataStandardOrTool](DataStandardOrTool.md) | [concerns_data_topic](concerns_data_topic.md) | range | [DataTopic](DataTopic.md) |
| [DataStandard](DataStandard.md) | [concerns_data_topic](concerns_data_topic.md) | range | [DataTopic](DataTopic.md) |
| [BiomedicalStandard](BiomedicalStandard.md) | [concerns_data_topic](concerns_data_topic.md) | range | [DataTopic](DataTopic.md) |
| [Registry](Registry.md) | [concerns_data_topic](concerns_data_topic.md) | range | [DataTopic](DataTopic.md) |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | [concerns_data_topic](concerns_data_topic.md) | range | [DataTopic](DataTopic.md) |
| [ModelRepository](ModelRepository.md) | [concerns_data_topic](concerns_data_topic.md) | range | [DataTopic](DataTopic.md) |
| [ReferenceDataOrDataset](ReferenceDataOrDataset.md) | [concerns_data_topic](concerns_data_topic.md) | range | [DataTopic](DataTopic.md) |
| [SoftwareOrTool](SoftwareOrTool.md) | [concerns_data_topic](concerns_data_topic.md) | range | [DataTopic](DataTopic.md) |
| [ReferenceImplementation](ReferenceImplementation.md) | [concerns_data_topic](concerns_data_topic.md) | range | [DataTopic](DataTopic.md) |
| [TrainingProgram](TrainingProgram.md) | [concerns_data_topic](concerns_data_topic.md) | range | [DataTopic](DataTopic.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-datatopic-schema





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | STANDARDSDATATOPIC:DataTopic |
| native | STANDARDSDATATOPIC:DataTopic |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataTopic
description: Represents a general data topic for Bridge2AI data or the tools/standards
  applied to the data.
from_schema: https://w3id.org/bridge2ai/standards-datatopic-schema
rank: 1000
is_a: NamedThing
slots:
- EDAM_ID
- MeSH_ID
- NCIT_ID

```
</details>

### Induced

<details>
```yaml
name: DataTopic
description: Represents a general data topic for Bridge2AI data or the tools/standards
  applied to the data.
from_schema: https://w3id.org/bridge2ai/standards-datatopic-schema
rank: 1000
is_a: NamedThing
attributes:
  EDAM_ID:
    name: EDAM_ID
    examples:
    - value: edam.data:0006
    from_schema: https://w3id.org/bridge2ai/standards-schema
    rank: 1000
    values_from:
    - edam.data
    - edam.format
    - edam.operation
    - edam.topic
    alias: EDAM_ID
    owner: DataTopic
    domain_of:
    - DataTopic
    - DataSubstrate
    range: edam identifier
  MeSH_ID:
    name: MeSH_ID
    examples:
    - value: MeSH:D014831
    from_schema: https://w3id.org/bridge2ai/standards-schema
    rank: 1000
    values_from:
    - MeSH
    alias: MeSH_ID
    owner: DataTopic
    domain_of:
    - DataTopic
    - DataSubstrate
    range: mesh identifier
  NCIT_ID:
    name: NCIT_ID
    examples:
    - value: NCIT:C92692
    from_schema: https://w3id.org/bridge2ai/standards-schema
    rank: 1000
    values_from:
    - NCIT
    alias: NCIT_ID
    owner: DataTopic
    domain_of:
    - DataTopic
    - DataSubstrate
    range: ncit identifier
  id:
    name: id
    description: A unique identifier for a thing.
    from_schema: https://w3id.org/bridge2ai/standards-schema
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: DataTopic
    domain_of:
    - NamedThing
    range: uriorcurie
    required: true
  name:
    name: name
    description: A human-readable name for a thing.
    from_schema: https://w3id.org/bridge2ai/standards-schema
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: DataTopic
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A human-readable description for a thing.
    from_schema: https://w3id.org/bridge2ai/standards-schema
    rank: 1000
    slot_uri: schema:description
    alias: description
    owner: DataTopic
    domain_of:
    - NamedThing
    range: string
  subclass_of:
    name: subclass_of
    description: Holds between two classes where the domain class is a specialization
      of the range class.
    from_schema: https://w3id.org/bridge2ai/standards-schema
    exact_mappings:
    - rdfs:subClassOf
    - MESH:isa
    narrow_mappings:
    - rdfs:subPropertyOf
    rank: 1000
    is_a: related_to
    domain: NamedThing
    multivalued: true
    inherited: true
    alias: subclass_of
    owner: DataTopic
    domain_of:
    - NamedThing
    range: NamedThing

```
</details>