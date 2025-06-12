

# Slot: topics 


_Subject data set is relevant to the topic(s) listed in this slot. Must be a DataTopic object, referenced with its B2AI_TOPIC ID._





URI: [https://w3id.org/bridge2ai/standards-schema-all/topics](https://w3id.org/bridge2ai/standards-schema-all/topics)
Alias: topics


## Inheritance

* [related_to](related_to.md)
    * **topics**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataSet](DataSet.md) | Represents a data set by its metadata |  no  |







## Properties

* Range: [DataTopic](DataTopic.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/topics |
| native | https://w3id.org/bridge2ai/standards-schema-all/topics |




## LinkML Source

<details>
```yaml
name: topics
description: Subject data set is relevant to the topic(s) listed in this slot. Must
  be a DataTopic object, referenced with its B2AI_TOPIC ID.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: related_to
domain: DataSet
inherited: true
alias: topics
domain_of:
- DataSet
range: DataTopic
multivalued: true

```
</details>