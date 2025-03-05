

# Slot: id


_A unique identifier for a thing._





URI: [schema:identifier](http://schema.org/identifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomedicalStandard](BiomedicalStandard.md) | Represents a standard in the Bridge2AI Standards Registry with particular app... |  no  |
| [SoftwareOrTool](SoftwareOrTool.md) | Represents a piece of software or computational tool in the Bridge2AI Standar... |  no  |
| [ReferenceDataOrDataset](ReferenceDataOrDataset.md) | Represents a resource in the Bridge2AI Standards Registry serving as a standa... |  no  |
| [ModelRepository](ModelRepository.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |
| [DataStandardOrTool](DataStandardOrTool.md) | Represents a standard or tool in the Bridge2AI Standards Registry |  no  |
| [Organization](Organization.md) | Represents a group or organization related to or responsible for one or more ... |  no  |
| [UseCase](UseCase.md) | Represents a use case for Bridge2AI standards |  no  |
| [DataTopic](DataTopic.md) | Represents a general data topic for Bridge2AI data or the tools/standards app... |  no  |
| [AnatomicalEntity](AnatomicalEntity.md) | A subcellular location, cell type or gross anatomical part |  no  |
| [DataSubstrate](DataSubstrate.md) | Represents a data substrate for Bridge2AI data |  no  |
| [TrainingProgram](TrainingProgram.md) | Represents a training program for skills and experience related to standards ... |  no  |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | A set of concepts and categories, potentially defined or accompanied by their... |  no  |
| [ReferenceImplementation](ReferenceImplementation.md) | Represents an implementation of one or more standards or tools in the Bridge2... |  no  |
| [DataStandard](DataStandard.md) | Represents a general purpose standard in the Bridge2AI Standards Registry |  no  |
| [NamedThing](NamedThing.md) | A generic grouping for any identifiable entity |  no  |
| [Registry](Registry.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:identifier |
| native | https://w3id.org/bridge2ai/standards-schema-all/:id |




## LinkML Source

<details>
```yaml
name: id
description: A unique identifier for a thing.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
slot_uri: schema:identifier
identifier: true
alias: id
domain_of:
- NamedThing
range: uriorcurie
required: true

```
</details>