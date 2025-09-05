

# Slot: has_files 


_Subject data set has the file(s) listed in this slot as parts. Note that each file is not a data set and does not have its own ID in the registry. For data sets that are parts of this data set, use the `has_parts` slot._





URI: [https://w3id.org/bridge2ai/standards-schema-all/has_files](https://w3id.org/bridge2ai/standards-schema-all/has_files)
Alias: has_files


## Inheritance

* [related_to](related_to.md)
    * **has_files**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataSet](DataSet.md) | Represents a data set by its metadata |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/has_files |
| native | https://w3id.org/bridge2ai/standards-schema-all/has_files |




## LinkML Source

<details>
```yaml
name: has_files
description: Subject data set has the file(s) listed in this slot as parts. Note that
  each file is not a data set and does not have its own ID in the registry. For data
  sets that are parts of this data set, use the `has_parts` slot.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: related_to
domain: DataSet
inherited: true
alias: has_files
domain_of:
- DataSet
range: string
multivalued: true

```
</details>