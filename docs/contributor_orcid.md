

# Slot: contributor_orcid


_The ORCiD of the person who added this node._





URI: [https://w3id.org/bridge2ai/standards-schema-all/:contributor_orcid](https://w3id.org/bridge2ai/standards-schema-all/:contributor_orcid)




## Inheritance

* [node_property](node_property.md)
    * **contributor_orcid**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NamedThing](NamedThing.md) | A generic grouping for any identifiable entity |  no  |
| [ReferenceDataOrDataset](ReferenceDataOrDataset.md) | Represents a resource in the Bridge2AI Standards Registry serving as a standa... |  no  |
| [DataStandard](DataStandard.md) | Represents a general purpose standard in the Bridge2AI Standards Registry |  no  |
| [ModelRepository](ModelRepository.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |
| [AnatomicalEntity](AnatomicalEntity.md) | A subcellular location, cell type or gross anatomical part |  no  |
| [DataStandardOrTool](DataStandardOrTool.md) | Represents a standard or tool in the Bridge2AI Standards Registry |  no  |
| [BiomedicalStandard](BiomedicalStandard.md) | Represents a standard in the Bridge2AI Standards Registry with particular app... |  no  |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | A set of concepts and categories, potentially defined or accompanied by their... |  no  |
| [DataSet](DataSet.md) | Represents a data set produced by a group in the Bridge2AI consortium |  no  |
| [DataTopic](DataTopic.md) | Represents a general data topic for Bridge2AI data or the tools/standards app... |  no  |
| [SoftwareOrTool](SoftwareOrTool.md) | Represents a piece of software or computational tool in the Bridge2AI Standar... |  no  |
| [ReferenceImplementation](ReferenceImplementation.md) | Represents an implementation of one or more standards or tools in the Bridge2... |  no  |
| [UseCase](UseCase.md) | Represents a use case for Bridge2AI standards |  no  |
| [TrainingProgram](TrainingProgram.md) | Represents a training program for skills and experience related to standards ... |  no  |
| [DataSubstrate](DataSubstrate.md) | Represents a data substrate for Bridge2AI data |  no  |
| [Organization](Organization.md) | Represents a group or organization related to or responsible for one or more ... |  no  |
| [Registry](Registry.md) | Represents a resource in the Bridge2AI Standards Registry serving to curate a... |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)






## Examples

| Value |
| --- |
| ORCID:0000-0001-1234-5678 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/:contributor_orcid |
| native | https://w3id.org/bridge2ai/standards-schema-all/:contributor_orcid |




## LinkML Source

<details>
```yaml
name: contributor_orcid
description: The ORCiD of the person who added this node.
examples:
- value: ORCID:0000-0001-1234-5678
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: node_property
domain: NamedThing
alias: contributor_orcid
domain_of:
- NamedThing
range: uriorcurie

```
</details>