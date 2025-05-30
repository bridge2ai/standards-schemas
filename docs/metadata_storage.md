

# Slot: metadata_storage 


_Data Substrate in which metadata is stored._





URI: [https://w3id.org/bridge2ai/standards-schema-all/metadata_storage](https://w3id.org/bridge2ai/standards-schema-all/metadata_storage)
Alias: metadata_storage


## Inheritance

* [node_property](node_property.md)
    * **metadata_storage**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataSubstrate](DataSubstrate.md) | Represents a data substrate for Bridge2AI data |  no  |







## Properties

* Range: [String](String.md)&nbsp;or&nbsp;<br />[DataSubstrate](DataSubstrate.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/metadata_storage |
| native | https://w3id.org/bridge2ai/standards-schema-all/metadata_storage |




## LinkML Source

<details>
```yaml
name: metadata_storage
description: Data Substrate in which metadata is stored.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: node_property
domain: NamedThing
alias: metadata_storage
domain_of:
- DataSubstrate
range: string
multivalued: true
any_of:
- range: DataSubstrate
- equals_string: file headers

```
</details>