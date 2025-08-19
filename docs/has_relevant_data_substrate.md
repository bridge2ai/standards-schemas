

# Slot: has_relevant_data_substrate 


_Subject standard has some relationship to the object data substrate(s), including whether it is intended to be used with the data substrate, or whether it is implemented through the data substrate._





URI: [https://w3id.org/bridge2ai/standards-schema-all/has_relevant_data_substrate](https://w3id.org/bridge2ai/standards-schema-all/has_relevant_data_substrate)
Alias: has_relevant_data_substrate


## Inheritance

* [related_to](related_to.md)
    * **has_relevant_data_substrate**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Registry](Registry.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | A set of concepts and categories, potentially defined or accompanied by their... |  no  |
| [SoftwareOrTool](SoftwareOrTool.md) | Represents a piece of software or computational tool in the Bridge2AI Standar... |  no  |
| [TrainingProgram](TrainingProgram.md) | Represents a training program for skills and experience related to standards ... |  no  |
| [DataStandardOrTool](DataStandardOrTool.md) | Represents a standard or tool in the Bridge2AI Standards Registry |  no  |
| [DataStandard](DataStandard.md) | Represents a general purpose standard in the Bridge2AI Standards Registry |  no  |
| [ReferenceImplementation](ReferenceImplementation.md) | Represents an implementation of one or more standards or tools in the Bridge2... |  no  |
| [BiomedicalStandard](BiomedicalStandard.md) | Represents a standard in the Bridge2AI Standards Registry with particular app... |  no  |
| [ModelRepository](ModelRepository.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |







## Properties

* Range: [DataSubstrate](DataSubstrate.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/has_relevant_data_substrate |
| native | https://w3id.org/bridge2ai/standards-schema-all/has_relevant_data_substrate |




## LinkML Source

<details>
```yaml
name: has_relevant_data_substrate
description: Subject standard has some relationship to the object data substrate(s),
  including whether it is intended to be used with the data substrate, or whether
  it is implemented through the data substrate.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: related_to
domain: DataStandardOrTool
inherited: true
alias: has_relevant_data_substrate
domain_of:
- DataStandardOrTool
range: DataSubstrate
multivalued: true

```
</details>