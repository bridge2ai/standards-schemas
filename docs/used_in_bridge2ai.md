

# Slot: used_in_bridge2ai 


_True if the entity is used, developed, or otherwise related to work in the Bridge2AI consortium. If false, the entity is not explicitly related to Bridge2AI. If not specified, it is not known if the entity is related to Bridge2AI._





URI: [https://w3id.org/bridge2ai/standards-schema-all/used_in_bridge2ai](https://w3id.org/bridge2ai/standards-schema-all/used_in_bridge2ai)
Alias: used_in_bridge2ai


## Inheritance

* [node_property](node_property.md)
    * **used_in_bridge2ai**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Manifest](Manifest.md) | Represents a manifest |  no  |
| [DataSubstrate](DataSubstrate.md) | Represents a data substrate for Bridge2AI data |  no  |
| [NamedThing](NamedThing.md) | A generic grouping for any identifiable entity |  no  |
| [BiomedicalStandard](BiomedicalStandard.md) | Represents a standard in the Bridge2AI Standards Registry with particular app... |  no  |
| [UseCase](UseCase.md) | Represents a use case for Bridge2AI standards |  no  |
| [DataStandardOrTool](DataStandardOrTool.md) | Represents a standard or tool in the Bridge2AI Standards Registry |  no  |
| [DataStandard](DataStandard.md) | Represents a general purpose standard in the Bridge2AI Standards Registry |  no  |
| [TrainingProgram](TrainingProgram.md) | Represents a training program for skills and experience related to standards ... |  no  |
| [ModelRepository](ModelRepository.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | A set of concepts and categories, potentially defined or accompanied by their... |  no  |
| [DataTopic](DataTopic.md) | Represents a general data topic for Bridge2AI data or the tools/standards app... |  no  |
| [Application](Application.md) | A set of details describing a specific application of a resource (e |  no  |
| [Organization](Organization.md) | Represents a group or organization related to or responsible for one or more ... |  no  |
| [DataSet](DataSet.md) | Represents a data set by its metadata |  no  |
| [SoftwareOrTool](SoftwareOrTool.md) | Represents a piece of software or computational tool in the Bridge2AI Standar... |  no  |
| [ReferenceImplementation](ReferenceImplementation.md) | Represents an implementation of one or more standards or tools in the Bridge2... |  no  |
| [Registry](Registry.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |
| [AnatomicalEntity](AnatomicalEntity.md) | A subcellular location, cell type or gross anatomical part |  no  |






## Properties

* Range: [Boolean](Boolean.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/used_in_bridge2ai |
| native | https://w3id.org/bridge2ai/standards-schema-all/used_in_bridge2ai |




## LinkML Source

<details>
```yaml
name: used_in_bridge2ai
description: True if the entity is used, developed, or otherwise related to work in
  the Bridge2AI consortium. If false, the entity is not explicitly related to Bridge2AI.
  If not specified, it is not known if the entity is related to Bridge2AI.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: node_property
domain: NamedThing
alias: used_in_bridge2ai
domain_of:
- NamedThing
range: boolean

```
</details>