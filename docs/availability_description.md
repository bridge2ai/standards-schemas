

# Slot: availability_description 


_A description of the availability of the data set, including any restrictions on access or use._





URI: [https://w3id.org/bridge2ai/standards-schema-all/availability_description](https://w3id.org/bridge2ai/standards-schema-all/availability_description)
Alias: availability_description


## Inheritance

* [node_property](node_property.md)
    * **availability_description**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataSet](DataSet.md) | Represents a data set by its metadata |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| "Datasets require additional permissions. Please visit https://example.com for more information." |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/availability_description |
| native | https://w3id.org/bridge2ai/standards-schema-all/availability_description |




## LinkML Source

<details>
```yaml
name: availability_description
description: A description of the availability of the data set, including any restrictions
  on access or use.
examples:
- value: '"Datasets require additional permissions. Please visit https://example.com
    for more information."'
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
is_a: node_property
domain: DataSet
alias: availability_description
domain_of:
- DataSet
range: string
required: false

```
</details>