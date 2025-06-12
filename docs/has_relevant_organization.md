

# Slot: has_relevant_organization 


_Subject standard has some relationship to the object organization(s), including as a user. This is distinct from the responsible organization, which is the group providing or supporting the standard or tool._





URI: [https://w3id.org/bridge2ai/standards-schema-all/has_relevant_organization](https://w3id.org/bridge2ai/standards-schema-all/has_relevant_organization)
Alias: has_relevant_organization


## Inheritance

* [related_to](related_to.md)
    * **has_relevant_organization**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | A set of concepts and categories, potentially defined or accompanied by their... |  no  |
| [DataStandardOrTool](DataStandardOrTool.md) | Represents a standard or tool in the Bridge2AI Standards Registry |  no  |
| [Registry](Registry.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |
| [SoftwareOrTool](SoftwareOrTool.md) | Represents a piece of software or computational tool in the Bridge2AI Standar... |  no  |
| [ReferenceImplementation](ReferenceImplementation.md) | Represents an implementation of one or more standards or tools in the Bridge2... |  no  |
| [DataStandard](DataStandard.md) | Represents a general purpose standard in the Bridge2AI Standards Registry |  no  |
| [BiomedicalStandard](BiomedicalStandard.md) | Represents a standard in the Bridge2AI Standards Registry with particular app... |  no  |
| [ModelRepository](ModelRepository.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |
| [TrainingProgram](TrainingProgram.md) | Represents a training program for skills and experience related to standards ... |  no  |







## Properties

* Range: [Organization](Organization.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/has_relevant_organization |
| native | https://w3id.org/bridge2ai/standards-schema-all/has_relevant_organization |




## LinkML Source

<details>
```yaml
name: has_relevant_organization
description: Subject standard has some relationship to the object organization(s),
  including as a user. This is distinct from the responsible organization, which is
  the group providing or supporting the standard or tool.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: related_to
domain: DataStandardOrTool
inherited: true
alias: has_relevant_organization
domain_of:
- DataStandardOrTool
range: Organization
multivalued: true

```
</details>