

# Slot: has_parts


_Subject data set has the data set(s) listed in this slot as parts. Note that each part is itself a data set, with its own ID in the registry. For specific files, use the `has_files` slot._





URI: [https://w3id.org/bridge2ai/standards-schema-all/:has_parts](https://w3id.org/bridge2ai/standards-schema-all/:has_parts)




## Inheritance

* [related_to](related_to.md)
    * **has_parts**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataSet](DataSet.md) | Represents a data set produced by a group in the Bridge2AI consortium |  no  |







## Properties

* Range: [DataSet](DataSet.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/:has_parts |
| native | https://w3id.org/bridge2ai/standards-schema-all/:has_parts |




## LinkML Source

<details>
```yaml
name: has_parts
description: Subject data set has the data set(s) listed in this slot as parts. Note
  that each part is itself a data set, with its own ID in the registry. For specific
  files, use the `has_files` slot.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: related_to
domain: DataSet
inherited: true
alias: has_parts
domain_of:
- DataSet
range: DataSet
multivalued: true

```
</details>