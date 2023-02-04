# Class: Organization
_Represents a group or organization related to or responsible for one or more Bridge2AI standards._




URI: [STANDARDSORGANIZATION:Organization](STANDARDSORGANIZATION:Organization)


```mermaid
 classDiagram
    class Organization
      NamedThing <|-- Organization
      
      Organization : description
      Organization : id
      Organization : name
      Organization : ROR_ID
      Organization : URL
      Organization : Wikidata_ID
      
```




## Inheritance
* [NamedThing](NamedThing.md)
    * **Organization**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ROR_ID](ROR_ID.md) | 0..1 <br/> [RorIdentifier](RorIdentifier.md) |  | direct |
| [Wikidata_ID](Wikidata_ID.md) | 0..1 <br/> [WikidataIdentifier](WikidataIdentifier.md) |  | direct |
| [URL](URL.md) | 0..1 <br/> NONE |  | direct |
| [id](id.md) | 1..1 <br/> [xsd:anyURI](xsd:anyURI) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> NONE | A human-readable description for a thing | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> NONE | A human-readable name for a thing | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DataStandardOrTool](DataStandardOrTool.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [DataStandard](DataStandard.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [BiomedicalStandard](BiomedicalStandard.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [Registry](Registry.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [ModelRepository](ModelRepository.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [ReferenceDataOrDataset](ReferenceDataOrDataset.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [SoftwareOrTool](SoftwareOrTool.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [ReferenceImplementation](ReferenceImplementation.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [TrainingProgram](TrainingProgram.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-organization-schema





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | STANDARDSORGANIZATION:Organization |
| native | STANDARDSORGANIZATION:Organization |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Organization
description: Represents a group or organization related to or responsible for one
  or more Bridge2AI standards.
from_schema: https://w3id.org/bridge2ai/standards-organization-schema
rank: 1000
is_a: NamedThing
slots:
- ROR_ID
- Wikidata_ID
- URL

```
</details>

### Induced

<details>
```yaml
name: Organization
description: Represents a group or organization related to or responsible for one
  or more Bridge2AI standards.
from_schema: https://w3id.org/bridge2ai/standards-organization-schema
rank: 1000
is_a: NamedThing
attributes:
  ROR_ID:
    name: ROR_ID
    examples:
    - value: ROR:02mp31p96
    from_schema: https://w3id.org/bridge2ai/standards-organization-schema
    rank: 1000
    values_from:
    - ROR
    alias: ROR_ID
    owner: Organization
    domain_of:
    - Organization
    range: ror identifier
  Wikidata_ID:
    name: Wikidata_ID
    examples:
    - value: WIKIDATA:Q282186
    from_schema: https://w3id.org/bridge2ai/standards-organization-schema
    rank: 1000
    values_from:
    - WIKIDATA
    alias: Wikidata_ID
    owner: Organization
    domain_of:
    - Organization
    range: wikidata identifier
  URL:
    name: URL
    examples:
    - value: https://www.zeiss.com/
    from_schema: https://w3id.org/bridge2ai/standards-organization-schema
    rank: 1000
    alias: URL
    owner: Organization
    domain_of:
    - Organization
  id:
    name: id
    description: A unique identifier for a thing.
    from_schema: https://w3id.org/bridge2ai/standards-schema
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: Organization
    domain_of:
    - NamedThing
    range: uriorcurie
    required: true
  name:
    name: name
    description: A human-readable name for a thing.
    from_schema: https://w3id.org/bridge2ai/standards-schema
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: Organization
    domain_of:
    - NamedThing
  description:
    name: description
    description: A human-readable description for a thing.
    from_schema: https://w3id.org/bridge2ai/standards-schema
    rank: 1000
    slot_uri: schema:description
    alias: description
    owner: Organization
    domain_of:
    - NamedThing

```
</details>