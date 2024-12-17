

# Slot: category


_Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard"._





URI: [https://w3id.org/bridge2ai/standards-schema-all/:category](https://w3id.org/bridge2ai/standards-schema-all/:category)




## Inheritance

* [type](type.md)
    * **category**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Registry](Registry.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | A set of concepts and categories, potentially defined or accompanied by their... |  no  |
| [BiomedicalStandard](BiomedicalStandard.md) | Represents a standard in the Bridge2AI Standards Registry with particular app... |  no  |
| [Organization](Organization.md) | Represents a group or organization related to or responsible for one or more ... |  no  |
| [UseCase](UseCase.md) | Represents a use case for Bridge2AI standards |  no  |
| [SoftwareOrTool](SoftwareOrTool.md) | Represents a piece of software or computational tool in the Bridge2AI Standar... |  no  |
| [ModelRepository](ModelRepository.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |
| [ReferenceImplementation](ReferenceImplementation.md) | Represents an implementation of one or more standards or tools in the Bridge2... |  no  |
| [NamedThing](NamedThing.md) | A generic grouping for any identifiable entity |  no  |
| [ReferenceDataOrDataset](ReferenceDataOrDataset.md) | Represents a resource in the Bridge2AI Standards Registry serving as a standa... |  no  |
| [TrainingProgram](TrainingProgram.md) | Represents a training program for skills and experience related to standards ... |  no  |
| [DataStandard](DataStandard.md) | Represents a general purpose standard in the Bridge2AI Standards Registry |  no  |
| [DataSubstrate](DataSubstrate.md) | Represents a data substrate for Bridge2AI data |  no  |
| [DataTopic](DataTopic.md) | Represents a general data topic for Bridge2AI data or the tools/standards app... |  no  |
| [DataStandardOrTool](DataStandardOrTool.md) | Represents a standard or tool in the Bridge2AI Standards Registry |  no  |
| [AnatomicalEntity](AnatomicalEntity.md) | A subcellular location, cell type or gross anatomical part |  no  |







## Properties

* Range: [CategoryType](CategoryType.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/:category |
| native | https://w3id.org/bridge2ai/standards-schema-all/:category |




## LinkML Source

<details>
```yaml
name: category
description: Name of the high level ontology class in which this entity is categorized.
  Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: type
domain: NamedThing
designates_type: true
alias: category
domain_of:
- NamedThing
range: category_type

```
</details>