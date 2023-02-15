# Slot: related_to
_A relationship that is asserted between two named things._


URI: [STANDARDS:related_to](https://w3id.org/bridge2ai/standards-schema/related_to)




## Inheritance

* **related_to**
    * [concerns_data_topic](concerns_data_topic.md)
    * [has_relevant_organization](has_relevant_organization.md)
    * [subclass_of](subclass_of.md)





## Applicable Classes

| Name | Description |
| --- | --- |
[Organization](Organization.md) | Represents a group or organization related to or responsible for one or more ...






## Properties

* Range: [NamedThing](NamedThing.md)
* Multivalued: True








## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema




## LinkML Source

<details>
```yaml
name: related_to
description: A relationship that is asserted between two named things.
from_schema: https://w3id.org/bridge2ai/standards-schema
rank: 1000
domain: NamedThing
multivalued: true
inherited: true
alias: related_to
domain_of:
- Organization
symmetric: true
range: NamedThing

```
</details>