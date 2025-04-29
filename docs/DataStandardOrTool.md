

# Class: DataStandardOrTool


_Represents a standard or tool in the Bridge2AI Standards Registry._





URI: [https://w3id.org/bridge2ai/standards-schema-all/:DataStandardOrTool](https://w3id.org/bridge2ai/standards-schema-all/:DataStandardOrTool)






```mermaid
 classDiagram
    class DataStandardOrTool
    click DataStandardOrTool href "../DataStandardOrTool"
      NamedThing <|-- DataStandardOrTool
        click NamedThing href "../NamedThing"
      

      DataStandardOrTool <|-- DataStandard
        click DataStandard href "../DataStandard"
      DataStandardOrTool <|-- Registry
        click Registry href "../Registry"
      DataStandardOrTool <|-- OntologyOrVocabulary
        click OntologyOrVocabulary href "../OntologyOrVocabulary"
      DataStandardOrTool <|-- ModelRepository
        click ModelRepository href "../ModelRepository"
      DataStandardOrTool <|-- ReferenceDataOrDataset
        click ReferenceDataOrDataset href "../ReferenceDataOrDataset"
      DataStandardOrTool <|-- SoftwareOrTool
        click SoftwareOrTool href "../SoftwareOrTool"
      DataStandardOrTool <|-- ReferenceImplementation
        click ReferenceImplementation href "../ReferenceImplementation"
      DataStandardOrTool <|-- TrainingProgram
        click TrainingProgram href "../TrainingProgram"
      
      
      DataStandardOrTool : category
        
      DataStandardOrTool : collection
        
          
    
    
    DataStandardOrTool --> "*" StandardsCollectionTag : collection
    click StandardsCollectionTag href "../StandardsCollectionTag"

        
      DataStandardOrTool : concerns_data_topic
        
          
    
    
    DataStandardOrTool --> "*" DataTopic : concerns_data_topic
    click DataTopic href "../DataTopic"

        
      DataStandardOrTool : contribution_date
        
      DataStandardOrTool : contributor_github_name
        
      DataStandardOrTool : contributor_name
        
      DataStandardOrTool : contributor_orcid
        
      DataStandardOrTool : description
        
      DataStandardOrTool : formal_specification
        
      DataStandardOrTool : has_relevant_organization
        
          
    
    
    DataStandardOrTool --> "*" Organization : has_relevant_organization
    click Organization href "../Organization"

        
      DataStandardOrTool : has_training_resource
        
          
    
    
    DataStandardOrTool --> "*" DataStandardOrTool : has_training_resource
    click DataStandardOrTool href "../DataStandardOrTool"

        
      DataStandardOrTool : id
        
      DataStandardOrTool : is_open
        
      DataStandardOrTool : name
        
      DataStandardOrTool : publication
        
      DataStandardOrTool : purpose_detail
        
      DataStandardOrTool : related_to
        
          
    
    
    DataStandardOrTool --> "*" NamedThing : related_to
    click NamedThing href "../NamedThing"

        
      DataStandardOrTool : requires_registration
        
      DataStandardOrTool : responsible_organization
        
          
    
    
    DataStandardOrTool --> "*" Organization : responsible_organization
    click Organization href "../Organization"

        
      DataStandardOrTool : subclass_of
        
          
    
    
    DataStandardOrTool --> "*" NamedThing : subclass_of
    click NamedThing href "../NamedThing"

        
      DataStandardOrTool : url
        
      DataStandardOrTool : used_in_bridge2ai
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **DataStandardOrTool**
        * [DataStandard](DataStandard.md)
        * [Registry](Registry.md)
        * [OntologyOrVocabulary](OntologyOrVocabulary.md)
        * [ModelRepository](ModelRepository.md)
        * [ReferenceDataOrDataset](ReferenceDataOrDataset.md)
        * [SoftwareOrTool](SoftwareOrTool.md)
        * [ReferenceImplementation](ReferenceImplementation.md)
        * [TrainingProgram](TrainingProgram.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [collection](collection.md) | * <br/> [StandardsCollectionTag](StandardsCollectionTag.md) | Tags for specific sets of standards | direct |
| [concerns_data_topic](concerns_data_topic.md) | * <br/> [DataTopic](DataTopic.md) | Subject standard is generally applied in the context of object data topic | direct |
| [has_relevant_organization](has_relevant_organization.md) | * <br/> [Organization](Organization.md) | Subject standard has some relationship to the object organization(s), includi... | direct |
| [has_training_resource](has_training_resource.md) | * <br/> [DataStandardOrTool](DataStandardOrTool.md) | Relevant training resources, standard usage manuals, or other documentation f... | direct |
| [purpose_detail](purpose_detail.md) | 0..1 <br/> [String](String.md) | Text description of the standard or tool | direct |
| [is_open](is_open.md) | 0..1 <br/> [Boolean](Boolean.md) | Is the standard or tool FAIR and available free of cost? | direct |
| [requires_registration](requires_registration.md) | 0..1 <br/> [Boolean](Boolean.md) | Does usage of the standard or tool require registration of a user or group wi... | direct |
| [url](url.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | URL for basic documentation of the standard or tool | direct |
| [publication](publication.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Relevant publication for the standard or tool | direct |
| [formal_specification](formal_specification.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Relevant code repository or other location for a formal specification of the ... | direct |
| [responsible_organization](responsible_organization.md) | * <br/> [Organization](Organization.md) | Organization(s) responsible for providing and/or supporting the standard or t... | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [category](category.md) | 0..1 <br/> [CategoryType](CategoryType.md) | CURIE for the high level ontology class in which this entity is categorized | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human-readable name for a thing | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [NamedThing](NamedThing.md) |
| [subclass_of](subclass_of.md) | * <br/> [NamedThing](NamedThing.md) | Holds between two classes where the domain class is a specialization of the r... | [NamedThing](NamedThing.md) |
| [related_to](related_to.md) | * <br/> [NamedThing](NamedThing.md) | A relationship that is asserted between two named things | [NamedThing](NamedThing.md) |
| [contributor_name](contributor_name.md) | 0..1 <br/> [String](String.md) | The name of the person who added this node | [NamedThing](NamedThing.md) |
| [contributor_github_name](contributor_github_name.md) | 0..1 <br/> [String](String.md) | The name of the github user who added this node | [NamedThing](NamedThing.md) |
| [contributor_orcid](contributor_orcid.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | The ORCiD of the person who added this node | [NamedThing](NamedThing.md) |
| [contribution_date](contribution_date.md) | 0..1 <br/> [Date](Date.md) | The date on which the node was added | [NamedThing](NamedThing.md) |
| [used_in_bridge2ai](used_in_bridge2ai.md) | 0..1 <br/> [Boolean](Boolean.md) | True if the entity is used, developed, or otherwise related to work in the Br... | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DataStandardOrTool](DataStandardOrTool.md) | [concerns_data_topic](concerns_data_topic.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [DataStandardOrTool](DataStandardOrTool.md) | [has_relevant_organization](has_relevant_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [DataStandardOrTool](DataStandardOrTool.md) | [has_training_resource](has_training_resource.md) | range | [DataStandardOrTool](DataStandardOrTool.md) |
| [DataStandardOrTool](DataStandardOrTool.md) | [responsible_organization](responsible_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [DataStandard](DataStandard.md) | [concerns_data_topic](concerns_data_topic.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [DataStandard](DataStandard.md) | [has_relevant_organization](has_relevant_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [DataStandard](DataStandard.md) | [has_training_resource](has_training_resource.md) | range | [DataStandardOrTool](DataStandardOrTool.md) |
| [DataStandard](DataStandard.md) | [responsible_organization](responsible_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [BiomedicalStandard](BiomedicalStandard.md) | [concerns_data_topic](concerns_data_topic.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [BiomedicalStandard](BiomedicalStandard.md) | [has_relevant_organization](has_relevant_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [BiomedicalStandard](BiomedicalStandard.md) | [has_training_resource](has_training_resource.md) | range | [DataStandardOrTool](DataStandardOrTool.md) |
| [BiomedicalStandard](BiomedicalStandard.md) | [responsible_organization](responsible_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [Registry](Registry.md) | [concerns_data_topic](concerns_data_topic.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [Registry](Registry.md) | [has_relevant_organization](has_relevant_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [Registry](Registry.md) | [has_training_resource](has_training_resource.md) | range | [DataStandardOrTool](DataStandardOrTool.md) |
| [Registry](Registry.md) | [responsible_organization](responsible_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | [concerns_data_topic](concerns_data_topic.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | [has_relevant_organization](has_relevant_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | [has_training_resource](has_training_resource.md) | range | [DataStandardOrTool](DataStandardOrTool.md) |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | [responsible_organization](responsible_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [ModelRepository](ModelRepository.md) | [concerns_data_topic](concerns_data_topic.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [ModelRepository](ModelRepository.md) | [has_relevant_organization](has_relevant_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [ModelRepository](ModelRepository.md) | [has_training_resource](has_training_resource.md) | range | [DataStandardOrTool](DataStandardOrTool.md) |
| [ModelRepository](ModelRepository.md) | [responsible_organization](responsible_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [ReferenceDataOrDataset](ReferenceDataOrDataset.md) | [concerns_data_topic](concerns_data_topic.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [ReferenceDataOrDataset](ReferenceDataOrDataset.md) | [has_relevant_organization](has_relevant_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [ReferenceDataOrDataset](ReferenceDataOrDataset.md) | [has_training_resource](has_training_resource.md) | range | [DataStandardOrTool](DataStandardOrTool.md) |
| [ReferenceDataOrDataset](ReferenceDataOrDataset.md) | [responsible_organization](responsible_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [SoftwareOrTool](SoftwareOrTool.md) | [concerns_data_topic](concerns_data_topic.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [SoftwareOrTool](SoftwareOrTool.md) | [has_relevant_organization](has_relevant_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [SoftwareOrTool](SoftwareOrTool.md) | [has_training_resource](has_training_resource.md) | range | [DataStandardOrTool](DataStandardOrTool.md) |
| [SoftwareOrTool](SoftwareOrTool.md) | [responsible_organization](responsible_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [ReferenceImplementation](ReferenceImplementation.md) | [concerns_data_topic](concerns_data_topic.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [ReferenceImplementation](ReferenceImplementation.md) | [has_relevant_organization](has_relevant_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [ReferenceImplementation](ReferenceImplementation.md) | [has_training_resource](has_training_resource.md) | range | [DataStandardOrTool](DataStandardOrTool.md) |
| [ReferenceImplementation](ReferenceImplementation.md) | [responsible_organization](responsible_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [TrainingProgram](TrainingProgram.md) | [concerns_data_topic](concerns_data_topic.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [TrainingProgram](TrainingProgram.md) | [has_relevant_organization](has_relevant_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [TrainingProgram](TrainingProgram.md) | [has_training_resource](has_training_resource.md) | range | [DataStandardOrTool](DataStandardOrTool.md) |
| [TrainingProgram](TrainingProgram.md) | [responsible_organization](responsible_organization.md) | domain | [DataStandardOrTool](DataStandardOrTool.md) |
| [DataStandardOrToolContainer](DataStandardOrToolContainer.md) | [data_standardortools_collection](data_standardortools_collection.md) | range | [DataStandardOrTool](DataStandardOrTool.md) |
| [UseCase](UseCase.md) | [standards_and_tools_for_dgp_use](standards_and_tools_for_dgp_use.md) | range | [DataStandardOrTool](DataStandardOrTool.md) |
| [UseCase](UseCase.md) | [alternative_standards_and_tools](alternative_standards_and_tools.md) | range | [DataStandardOrTool](DataStandardOrTool.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/:DataStandardOrTool |
| native | https://w3id.org/bridge2ai/standards-schema-all/:DataStandardOrTool |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataStandardOrTool
description: Represents a standard or tool in the Bridge2AI Standards Registry.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
is_a: NamedThing
slots:
- collection
- concerns_data_topic
- has_relevant_organization
- has_training_resource
- purpose_detail
- is_open
- requires_registration
- url
- publication
- formal_specification
- responsible_organization

```
</details>

### Induced

<details>
```yaml
name: DataStandardOrTool
description: Represents a standard or tool in the Bridge2AI Standards Registry.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
is_a: NamedThing
attributes:
  collection:
    name: collection
    description: Tags for specific sets of standards.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: collection
    owner: DataStandardOrTool
    domain_of:
    - DataStandardOrTool
    range: StandardsCollectionTag
    multivalued: true
  concerns_data_topic:
    name: concerns_data_topic
    description: Subject standard is generally applied in the context of object data
      topic.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: related_to
    domain: DataStandardOrTool
    inherited: true
    alias: concerns_data_topic
    owner: DataStandardOrTool
    domain_of:
    - DataStandardOrTool
    range: DataTopic
    multivalued: true
  has_relevant_organization:
    name: has_relevant_organization
    description: Subject standard has some relationship to the object organization(s),
      including as a user. This is distinct from the responsible organization, which
      is the group providing or supporting the standard or tool.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: related_to
    domain: DataStandardOrTool
    inherited: true
    alias: has_relevant_organization
    owner: DataStandardOrTool
    domain_of:
    - DataStandardOrTool
    range: Organization
    multivalued: true
  has_training_resource:
    name: has_training_resource
    description: Relevant training resources, standard usage manuals, or other documentation
      for the standard or tool.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: has_training_resource
    owner: DataStandardOrTool
    domain_of:
    - DataStandardOrTool
    range: DataStandardOrTool
    multivalued: true
  purpose_detail:
    name: purpose_detail
    description: Text description of the standard or tool.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: purpose_detail
    owner: DataStandardOrTool
    domain_of:
    - DataStandardOrTool
    range: string
  is_open:
    name: is_open
    description: Is the standard or tool FAIR and available free of cost?
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: is_open
    owner: DataStandardOrTool
    domain_of:
    - DataStandardOrTool
    range: boolean
  requires_registration:
    name: requires_registration
    description: Does usage of the standard or tool require registration of a user
      or group with some organization or managerial body?
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: requires_registration
    owner: DataStandardOrTool
    domain_of:
    - DataStandardOrTool
    range: boolean
  url:
    name: url
    description: URL for basic documentation of the standard or tool.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: url
    owner: DataStandardOrTool
    domain_of:
    - DataStandardOrTool
    - Organization
    range: uriorcurie
  publication:
    name: publication
    description: Relevant publication for the standard or tool. Prefer a DOI or PUBMED.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: publication
    owner: DataStandardOrTool
    domain_of:
    - DataStandardOrTool
    range: uriorcurie
  formal_specification:
    name: formal_specification
    description: Relevant code repository or other location for a formal specification
      of the standard or tool. Often a URL, particularly to a Git repository.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: formal_specification
    owner: DataStandardOrTool
    domain_of:
    - DataStandardOrTool
    range: uriorcurie
  responsible_organization:
    name: responsible_organization
    description: Organization(s) responsible for providing and/or supporting the standard
      or tool.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: DataStandardOrTool
    alias: responsible_organization
    owner: DataStandardOrTool
    domain_of:
    - DataStandardOrTool
    range: Organization
    multivalued: true
  id:
    name: id
    description: A unique identifier for a thing.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: DataStandardOrTool
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
    owner: DataStandardOrTool
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
    owner: DataStandardOrTool
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
    owner: DataStandardOrTool
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
    owner: DataStandardOrTool
    domain_of:
    - NamedThing
    range: NamedThing
    multivalued: true
  related_to:
    name: related_to
    description: A relationship that is asserted between two named things.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    domain: NamedThing
    inherited: true
    alias: related_to
    owner: DataStandardOrTool
    domain_of:
    - NamedThing
    - Organization
    symmetric: true
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
    owner: DataStandardOrTool
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
    owner: DataStandardOrTool
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
    owner: DataStandardOrTool
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
    owner: DataStandardOrTool
    domain_of:
    - NamedThing
    range: date
  used_in_bridge2ai:
    name: used_in_bridge2ai
    description: True if the entity is used, developed, or otherwise related to work
      in the Bridge2AI consortium. If false, the entity is not explicitly related
      to Bridge2AI. If not specified, it is not known if the entity is related to
      Bridge2AI.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: used_in_bridge2ai
    owner: DataStandardOrTool
    domain_of:
    - NamedThing
    range: boolean

```
</details>