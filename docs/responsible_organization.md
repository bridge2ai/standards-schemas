

# Slot: responsible_organization


_Organization(s) responsible for providing and/or supporting the standard or tool._





URI: [https://w3id.org/bridge2ai/standards-schema-all/:responsible_organization](https://w3id.org/bridge2ai/standards-schema-all/:responsible_organization)




## Inheritance

* [node_property](node_property.md)
    * **responsible_organization**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReferenceDataOrDataset](ReferenceDataOrDataset.md) | Represents a resource in the Bridge2AI Standards Registry serving as a standa... |  no  |
| [DataStandard](DataStandard.md) | Represents a general purpose standard in the Bridge2AI Standards Registry |  no  |
| [ModelRepository](ModelRepository.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |
| [DataStandardOrTool](DataStandardOrTool.md) | Represents a standard or tool in the Bridge2AI Standards Registry |  no  |
| [BiomedicalStandard](BiomedicalStandard.md) | Represents a standard in the Bridge2AI Standards Registry with particular app... |  no  |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | A set of concepts and categories, potentially defined or accompanied by their... |  no  |
| [SoftwareOrTool](SoftwareOrTool.md) | Represents a piece of software or computational tool in the Bridge2AI Standar... |  no  |
| [ReferenceImplementation](ReferenceImplementation.md) | Represents an implementation of one or more standards or tools in the Bridge2... |  no  |
| [TrainingProgram](TrainingProgram.md) | Represents a training program for skills and experience related to standards ... |  no  |
| [Registry](Registry.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |







## Properties

* Range: [Organization](Organization.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/:responsible_organization |
| native | https://w3id.org/bridge2ai/standards-schema-all/:responsible_organization |




## LinkML Source

<details>
```yaml
name: responsible_organization
description: Organization(s) responsible for providing and/or supporting the standard
  or tool.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: node_property
domain: DataStandardOrTool
alias: responsible_organization
domain_of:
- DataStandardOrTool
range: Organization
multivalued: true

```
</details>