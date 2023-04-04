# Slot: topic_involves_anatomy
_A relationship between a DataTopic and an anatomical entity._


URI: [https://w3id.org/bridge2ai/standards-schema-all/:topic_involves_anatomy](https://w3id.org/bridge2ai/standards-schema-all/:topic_involves_anatomy)




## Inheritance

* [related_to](related_to.md)
    * **topic_involves_anatomy**





## Applicable Classes

| Name | Description |
| --- | --- |
[DataTopic](DataTopic.md) | Represents a general data topic for Bridge2AI data or the tools/standards app...






## Properties

* Range: [AnatomicalEntity](AnatomicalEntity.md)
* Multivalued: True








## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## LinkML Source

<details>
```yaml
name: topic_involves_anatomy
description: A relationship between a DataTopic and an anatomical entity.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
exact_mappings:
- RO:0004026
rank: 1000
is_a: related_to
domain: DataTopic
multivalued: true
inherited: true
alias: topic_involves_anatomy
domain_of:
- DataTopic
range: AnatomicalEntity

```
</details>