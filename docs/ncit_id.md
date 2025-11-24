

# Slot: ncit_id 


_Unique NCIt Identifier_





URI: [https://w3id.org/bridge2ai/standards-schema-all/ncit_id](https://w3id.org/bridge2ai/standards-schema-all/ncit_id)
Alias: ncit_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataTopic](DataTopic.md) | Represents a general data topic for Bridge2AI data or the tools/standards app... |  no  |
| [DataSubstrate](DataSubstrate.md) | Represents a data substrate for Bridge2AI data |  no  |






## Properties

* Range: [NcitIdentifier](NcitIdentifier.md)





## Examples

| Value |
| --- |
| ncit:C92692 |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/ncit_id |
| native | https://w3id.org/bridge2ai/standards-schema-all/ncit_id |




## LinkML Source

<details>
```yaml
name: ncit_id
description: Unique NCIt Identifier
examples:
- value: ncit:C92692
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
values_from:
- ncit
alias: ncit_id
domain_of:
- DataSubstrate
- DataTopic
range: ncit_identifier

```
</details>