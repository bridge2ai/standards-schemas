# Slot: EDAM_ID

URI: [STANDARDS:EDAM_ID](https://w3id.org/bridge2ai/standards-schema/EDAM_ID)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[DataTopic](DataTopic.md) | Represents a general data topic for Bridge2AI data or the tools/standards app...
[DataSubstrate](DataSubstrate.md) | Represents a data substrate for Bridge2AI data






## Properties

* Range: [EdamIdentifier](EdamIdentifier.md)








## Examples

| Value |
| --- |
| edam.data:0006 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema




## LinkML Source

<details>
```yaml
name: EDAM_ID
examples:
- value: edam.data:0006
from_schema: https://w3id.org/bridge2ai/standards-schema
rank: 1000
values_from:
- edam.data
- edam.format
- edam.operation
- edam.topic
alias: EDAM_ID
domain_of:
- DataTopic
- DataSubstrate
range: edam identifier

```
</details>