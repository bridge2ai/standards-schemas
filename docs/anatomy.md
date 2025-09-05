

# Slot: anatomy 


_Relevant anatomical locations, including gross anatomical parts, cell types, and subcellular locations._





URI: [https://w3id.org/bridge2ai/standards-schema-all/anatomy](https://w3id.org/bridge2ai/standards-schema-all/anatomy)
Alias: anatomy


## Inheritance

* [node_property](node_property.md)
    * **anatomy**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataPart](DataPart.md) | Represents a part of all datasets in a manifest |  no  |






## Properties

* Range: [AnatomicalEntity](AnatomicalEntity.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/anatomy |
| native | https://w3id.org/bridge2ai/standards-schema-all/anatomy |




## LinkML Source

<details>
```yaml
name: anatomy
description: Relevant anatomical locations, including gross anatomical parts, cell
  types, and subcellular locations.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: node_property
domain: NamedThing
alias: anatomy
domain_of:
- DataPart
range: AnatomicalEntity
multivalued: true

```
</details>