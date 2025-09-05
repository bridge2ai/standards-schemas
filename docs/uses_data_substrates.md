

# Slot: uses_data_substrates 


_The data part includes these data substrates. Must be a list of DataSubstrate objects, referenced with their B2AI_SUBSTRATE IDs._





URI: [https://w3id.org/bridge2ai/standards-schema-all/uses_data_substrates](https://w3id.org/bridge2ai/standards-schema-all/uses_data_substrates)
Alias: uses_data_substrates


## Inheritance

* [related_to](related_to.md)
    * **uses_data_substrates**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataPart](DataPart.md) | Represents a part of all datasets in a manifest |  no  |






## Properties

* Range: [DataSubstrate](DataSubstrate.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/uses_data_substrates |
| native | https://w3id.org/bridge2ai/standards-schema-all/uses_data_substrates |




## LinkML Source

<details>
```yaml
name: uses_data_substrates
description: The data part includes these data substrates. Must be a list of DataSubstrate
  objects, referenced with their B2AI_SUBSTRATE IDs.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: related_to
domain: DataPart
inherited: true
alias: uses_data_substrates
domain_of:
- DataPart
range: DataSubstrate
multivalued: true

```
</details>