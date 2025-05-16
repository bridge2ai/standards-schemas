

# Slot: subclass_of 


_Holds between two classes where the domain class is a specialization of the range class._





URI: [https://w3id.org/bridge2ai/standards-schema-all/subclass_of](https://w3id.org/bridge2ai/standards-schema-all/subclass_of)
Alias: subclass_of


## Inheritance

* [related_to](related_to.md)
    * **subclass_of**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | A set of concepts and categories, potentially defined or accompanied by their... |  no  |
| [TrainingProgram](TrainingProgram.md) | Represents a training program for skills and experience related to standards ... |  no  |
| [DataTopic](DataTopic.md) | Represents a general data topic for Bridge2AI data or the tools/standards app... |  no  |
| [DataStandard](DataStandard.md) | Represents a general purpose standard in the Bridge2AI Standards Registry |  no  |
| [NamedThing](NamedThing.md) | A generic grouping for any identifiable entity |  no  |
| [Organization](Organization.md) | Represents a group or organization related to or responsible for one or more ... |  no  |
| [ReferenceDataOrDataset](ReferenceDataOrDataset.md) | Represents a resource in the Bridge2AI Standards Registry serving as a standa... |  no  |
| [SoftwareOrTool](SoftwareOrTool.md) | Represents a piece of software or computational tool in the Bridge2AI Standar... |  no  |
| [ModelRepository](ModelRepository.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |
| [UseCase](UseCase.md) | Represents a use case for Bridge2AI standards |  no  |
| [DataSet](DataSet.md) | Represents a data set produced by a group in the Bridge2AI consortium |  no  |
| [Registry](Registry.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |
| [DataSubstrate](DataSubstrate.md) | Represents a data substrate for Bridge2AI data |  no  |
| [ReferenceImplementation](ReferenceImplementation.md) | Represents an implementation of one or more standards or tools in the Bridge2... |  no  |
| [DataStandardOrTool](DataStandardOrTool.md) | Represents a standard or tool in the Bridge2AI Standards Registry |  no  |
| [AnatomicalEntity](AnatomicalEntity.md) | A subcellular location, cell type or gross anatomical part |  no  |
| [BiomedicalStandard](BiomedicalStandard.md) | Represents a standard in the Bridge2AI Standards Registry with particular app... |  no  |







## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/subclass_of |
| native | https://w3id.org/bridge2ai/standards-schema-all/subclass_of |
| exact | rdfs:subClassOf, MESH:isa |
| narrow | rdfs:subPropertyOf |




## LinkML Source

<details>
```yaml
name: subclass_of
description: Holds between two classes where the domain class is a specialization
  of the range class.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
exact_mappings:
- rdfs:subClassOf
- MESH:isa
narrow_mappings:
- rdfs:subPropertyOf
rank: 1000
is_a: related_to
domain: NamedThing
inherited: true
alias: subclass_of
domain_of:
- NamedThing
range: NamedThing
multivalued: true

```
</details>