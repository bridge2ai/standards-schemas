

# Slot: use_case_category 


_Category of the UseCase. Not all projects will incorporate use cases in all categories. This is multivalued, as a use case may span categories._





URI: [https://w3id.org/bridge2ai/standards-schema-all/use_case_category](https://w3id.org/bridge2ai/standards-schema-all/use_case_category)
Alias: use_case_category


## Inheritance

* [node_property](node_property.md)
    * **use_case_category**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UseCase](UseCase.md) | Represents a use case for Bridge2AI standards |  yes  |







## Properties

* Range: [UseCaseCategory](UseCaseCategory.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/use_case_category |
| native | https://w3id.org/bridge2ai/standards-schema-all/use_case_category |




## LinkML Source

<details>
```yaml
name: use_case_category
description: Category of the UseCase. Not all projects will incorporate use cases
  in all categories. This is multivalued, as a use case may span categories.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: node_property
domain: NamedThing
alias: use_case_category
domain_of:
- UseCase
range: UseCaseCategory
multivalued: true

```
</details>