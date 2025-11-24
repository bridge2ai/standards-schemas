

# Slot: datasets 


_The manifest includes these datasets. Must be a list of Dataset objects, referenced with their B2AI_DATA IDs._





URI: [https://w3id.org/bridge2ai/standards-schema-all/datasets](https://w3id.org/bridge2ai/standards-schema-all/datasets)
Alias: datasets


## Inheritance

* [node_property](node_property.md)
    * **datasets**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Manifest](Manifest.md) | Represents a manifest |  no  |






## Properties

* Range: [DataSet](DataSet.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/datasets |
| native | https://w3id.org/bridge2ai/standards-schema-all/datasets |




## LinkML Source

<details>
```yaml
name: datasets
description: The manifest includes these datasets. Must be a list of Dataset objects,
  referenced with their B2AI_DATA IDs.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: node_property
domain: Manifest
alias: datasets
domain_of:
- Manifest
range: DataSet
multivalued: true

```
</details>