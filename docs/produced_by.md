

# Slot: produced_by 


_Subject data set was produced by the organization(s) listed in this slot. Must be an Organization object, referenced with its B2AI_ORG ID._





URI: [https://w3id.org/bridge2ai/standards-schema-all/produced_by](https://w3id.org/bridge2ai/standards-schema-all/produced_by)
Alias: produced_by


## Inheritance

* [related_to](related_to.md)
    * **produced_by**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataSet](DataSet.md) | Represents a data set by its metadata |  no  |







## Properties

* Range: [Organization](Organization.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/produced_by |
| native | https://w3id.org/bridge2ai/standards-schema-all/produced_by |




## LinkML Source

<details>
```yaml
name: produced_by
description: Subject data set was produced by the organization(s) listed in this slot.
  Must be an Organization object, referenced with its B2AI_ORG ID.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: related_to
domain: DataSet
inherited: true
alias: produced_by
domain_of:
- DataSet
range: Organization
multivalued: true

```
</details>