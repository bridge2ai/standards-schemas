# Slot: subclass_of
_Holds between two classes where the domain class is a specialization of the range class._


URI: [STANDARDS:subclass_of](https://w3id.org/bridge2ai/standards-schema/subclass_of)




## Inheritance

* [related_to](related_to.md)
    * **subclass_of**







## Properties

* Range: [NamedThing](NamedThing.md)
* Multivalued: True








## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema




## LinkML Source

<details>
```yaml
name: subclass of
description: Holds between two classes where the domain class is a specialization
  of the range class.
from_schema: https://w3id.org/bridge2ai/standards-schema
exact_mappings:
- rdfs:subClassOf
- MESH:isa
narrow_mappings:
- rdfs:subPropertyOf
rank: 1000
is_a: related to
domain: NamedThing
multivalued: true
inherited: true
alias: subclass_of
range: NamedThing

```
</details>