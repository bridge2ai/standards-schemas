# Enum: PersonStatus



URI: [PersonStatus](PersonStatus)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ALIVE | PATO:0001421 | the person is living |
| DEAD | PATO:0001422 | the person is deceased |
| UNKNOWN | None | the vital status is not known |




## Slots

| Name | Description |
| ---  | --- |
| [vital_status](vital_status.md) | living or dead status |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-usecase-schema




## LinkML Source

<details>
```yaml
name: PersonStatus
from_schema: https://w3id.org/bridge2ai/standards-usecase-schema
rank: 1000
permissible_values:
  ALIVE:
    text: ALIVE
    description: the person is living
    meaning: PATO:0001421
  DEAD:
    text: DEAD
    description: the person is deceased
    meaning: PATO:0001422
  UNKNOWN:
    text: UNKNOWN
    description: the vital status is not known
    todos:
    - map this to an ontology

```
</details>
