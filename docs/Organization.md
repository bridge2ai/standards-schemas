

# Class: Organization


_Represents a group or organization related to or responsible for one or more Bridge2AI standards._





URI: [https://w3id.org/bridge2ai/standards-schema-all/:Organization](https://w3id.org/bridge2ai/standards-schema-all/:Organization)






```mermaid
 classDiagram
    class Organization
    click Organization href "../Organization"
      NamedThing <|-- Organization
        click NamedThing href "../NamedThing"
      
      Organization : category
        
      Organization : contribution_date
        
      Organization : contributor_github_name
        
      Organization : contributor_name
        
      Organization : contributor_orcid
        
      Organization : description
        
      Organization : id
        
      Organization : name
        
      Organization : related_to
        
          
    
    
    Organization --> "*" NamedThing : related_to
    click NamedThing href "../NamedThing"

        
      Organization : ror_id
        
      Organization : subclass_of
        
          
    
    
    Organization --> "*" NamedThing : subclass_of
    click NamedThing href "../NamedThing"

        
      Organization : url
        
      Organization : wikidata_id
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **Organization**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ror_id](ror_id.md) | 0..1 <br/> [RorIdentifier](RorIdentifier.md) | Unique ROR identifier | direct |
| [wikidata_id](wikidata_id.md) | 0..1 <br/> [WikidataIdentifier](WikidataIdentifier.md) | Unique Wikidata identifier | direct |
| [url](url.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | URL for basic documentation of the standard or tool | direct |
| [related_to](related_to.md) | * <br/> [NamedThing](NamedThing.md) | A relationship that is asserted between two named things | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [category](category.md) | 0..1 <br/> [CategoryType](CategoryType.md) | CURIE for the high level ontology class in which this entity is categorized | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human-readable name for a thing | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [NamedThing](NamedThing.md) |
| [subclass_of](subclass_of.md) | * <br/> [NamedThing](NamedThing.md) | Holds between two classes where the domain class is a specialization of the r... | [NamedThing](NamedThing.md) |
| [contributor_name](contributor_name.md) | 0..1 <br/> [String](String.md) | The name of the person who added this node | [NamedThing](NamedThing.md) |
| [contributor_github_name](contributor_github_name.md) | 0..1 <br/> [String](String.md) | The name of the github user who added this node | [NamedThing](NamedThing.md) |
| [contributor_orcid](contributor_orcid.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | The ORCiD of the person who added this node | [NamedThing](NamedThing.md) |
| [contribution_date](contribution_date.md) | 0..1 <br/> [Date](Date.md) | The date on which the node was added | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DataStandardOrTool](DataStandardOrTool.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [DataStandardOrTool](DataStandardOrTool.md) | [responsible_organization](responsible_organization.md) | range | [Organization](Organization.md) |
| [DataStandard](DataStandard.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [DataStandard](DataStandard.md) | [responsible_organization](responsible_organization.md) | range | [Organization](Organization.md) |
| [BiomedicalStandard](BiomedicalStandard.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [BiomedicalStandard](BiomedicalStandard.md) | [responsible_organization](responsible_organization.md) | range | [Organization](Organization.md) |
| [Registry](Registry.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [Registry](Registry.md) | [responsible_organization](responsible_organization.md) | range | [Organization](Organization.md) |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | [responsible_organization](responsible_organization.md) | range | [Organization](Organization.md) |
| [ModelRepository](ModelRepository.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [ModelRepository](ModelRepository.md) | [responsible_organization](responsible_organization.md) | range | [Organization](Organization.md) |
| [ReferenceDataOrDataset](ReferenceDataOrDataset.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [ReferenceDataOrDataset](ReferenceDataOrDataset.md) | [responsible_organization](responsible_organization.md) | range | [Organization](Organization.md) |
| [SoftwareOrTool](SoftwareOrTool.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [SoftwareOrTool](SoftwareOrTool.md) | [responsible_organization](responsible_organization.md) | range | [Organization](Organization.md) |
| [ReferenceImplementation](ReferenceImplementation.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [ReferenceImplementation](ReferenceImplementation.md) | [responsible_organization](responsible_organization.md) | range | [Organization](Organization.md) |
| [TrainingProgram](TrainingProgram.md) | [has_relevant_organization](has_relevant_organization.md) | range | [Organization](Organization.md) |
| [TrainingProgram](TrainingProgram.md) | [responsible_organization](responsible_organization.md) | range | [Organization](Organization.md) |
| [OrganizationContainer](OrganizationContainer.md) | [organizations](organizations.md) | range | [Organization](Organization.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/:Organization |
| native | https://w3id.org/bridge2ai/standards-schema-all/:Organization |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Organization
description: Represents a group or organization related to or responsible for one
  or more Bridge2AI standards.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
is_a: NamedThing
slots:
- ror_id
- wikidata_id
- url
- related_to

```
</details>

### Induced

<details>
```yaml
name: Organization
description: Represents a group or organization related to or responsible for one
  or more Bridge2AI standards.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
is_a: NamedThing
attributes:
  ror_id:
    name: ror_id
    description: Unique ROR identifier.
    examples:
    - value: ROR:02mp31p96
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    values_from:
    - ROR
    alias: ror_id
    owner: Organization
    domain_of:
    - Organization
    range: ror_identifier
  wikidata_id:
    name: wikidata_id
    description: Unique Wikidata identifier.
    examples:
    - value: WIKIDATA:Q282186
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    values_from:
    - WIKIDATA
    alias: wikidata_id
    owner: Organization
    domain_of:
    - Organization
    range: wikidata_identifier
  url:
    name: url
    description: URL for basic documentation of the standard or tool.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: url
    owner: Organization
    domain_of:
    - DataStandardOrTool
    - Organization
    range: uriorcurie
  related_to:
    name: related_to
    description: A relationship that is asserted between two named things.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    domain: NamedThing
    inherited: true
    alias: related_to
    owner: Organization
    domain_of:
    - NamedThing
    - Organization
    symmetric: true
    range: NamedThing
    multivalued: true
  id:
    name: id
    description: A unique identifier for a thing.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: Organization
    domain_of:
    - NamedThing
    range: uriorcurie
    required: true
  category:
    name: category
    description: CURIE for the high level ontology class in which this entity is categorized.
      Corresponds to the label for the entity type class, e.g., "B2AI_STANDARD:DataStandard".
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: type
    domain: NamedThing
    designates_type: true
    alias: category
    owner: Organization
    domain_of:
    - NamedThing
    range: category_type
  name:
    name: name
    description: A human-readable name for a thing.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: Organization
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A human-readable description for a thing.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    slot_uri: schema:description
    alias: description
    owner: Organization
    domain_of:
    - NamedThing
    range: string
  subclass_of:
    name: subclass_of
    description: Holds between two classes where the domain class is a specialization
      of the range class.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    exact_mappings:
    - rdfs:subClassOf
    - MESH:isa
    narrow_mappings:
    - rdfs:subPropertyOf
    rank: 1000
    is_a: related_to
    domain: NamedThing
    inherited: true
    alias: subclass_of
    owner: Organization
    domain_of:
    - NamedThing
    range: NamedThing
    multivalued: true
  contributor_name:
    name: contributor_name
    description: The name of the person who added this node.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: contributor_name
    owner: Organization
    domain_of:
    - NamedThing
    range: string
  contributor_github_name:
    name: contributor_github_name
    description: The name of the github user who added this node.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: contributor_github_name
    owner: Organization
    domain_of:
    - NamedThing
    range: string
  contributor_orcid:
    name: contributor_orcid
    description: The ORCiD of the person who added this node.
    examples:
    - value: ORCID:0000-0001-1234-5678
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: contributor_orcid
    owner: Organization
    domain_of:
    - NamedThing
    range: uriorcurie
  contribution_date:
    name: contribution_date
    description: The date on which the node was added.
    examples:
    - value: '2023-03-20'
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: contribution_date
    owner: Organization
    domain_of:
    - NamedThing
    range: date

```
</details>