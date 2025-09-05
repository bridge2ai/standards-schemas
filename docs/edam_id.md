

# Slot: edam_id 


_Unique EDAM identifier_





URI: [https://w3id.org/bridge2ai/standards-schema-all/edam_id](https://w3id.org/bridge2ai/standards-schema-all/edam_id)
Alias: edam_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataSubstrate](DataSubstrate.md) | Represents a data substrate for Bridge2AI data |  no  |
| [DataTopic](DataTopic.md) | Represents a general data topic for Bridge2AI data or the tools/standards app... |  no  |






## Properties

* Range: [EdamIdentifier](EdamIdentifier.md)





## Examples

| Value |
| --- |
| edam.data:0006 |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/edam_id |
| native | https://w3id.org/bridge2ai/standards-schema-all/edam_id |




## LinkML Source

<details>
```yaml
name: edam_id
description: Unique EDAM identifier
examples:
- value: edam.data:0006
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
values_from:
- edam.data
- edam.format
- edam.operation
- edam.topic
alias: edam_id
domain_of:
- DataSubstrate
- DataTopic
range: edam_identifier

```
</details>