

# Slot: mesh_id 


_Unique MeSH identifier_





URI: [https://w3id.org/bridge2ai/standards-schema-all/mesh_id](https://w3id.org/bridge2ai/standards-schema-all/mesh_id)
Alias: mesh_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataSubstrate](DataSubstrate.md) | Represents a data substrate for Bridge2AI data |  no  |
| [DataTopic](DataTopic.md) | Represents a general data topic for Bridge2AI data or the tools/standards app... |  no  |







## Properties

* Range: [MeshIdentifier](MeshIdentifier.md)






## Examples

| Value |
| --- |
| mesh:D014831 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/mesh_id |
| native | https://w3id.org/bridge2ai/standards-schema-all/mesh_id |




## LinkML Source

<details>
```yaml
name: mesh_id
description: Unique MeSH identifier
examples:
- value: mesh:D014831
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
values_from:
- mesh
alias: mesh_id
domain_of:
- DataSubstrate
- DataTopic
range: mesh_identifier

```
</details>