

# Class: Application 


_A set of details describing a specific application of a resource (e.g., a standard or a dataset) to a specific purpose. In the context of Bridge2AI, this will generally refer to an artificial intelligence-driven application. The related_to slot can be used to link to other relevant entities, such as other Applications, UseCases, DataSets, or Standards. Application objects have unique identifiers with the prefix B2AI_APP. This allows an Application to be referenced from other objects if needed. The category slot for Application objects should always be set to B2AI:Application for clarity._





URI: [https://w3id.org/bridge2ai/standards-schema-all/Application](https://w3id.org/bridge2ai/standards-schema-all/Application)





```mermaid
 classDiagram
    class Application
    click Application href "../Application/"
      NamedThing <|-- Application
        click NamedThing href "../NamedThing/"
      
      Application : category
        
      Application : contribution_date
        
      Application : contributor_github_name
        
      Application : contributor_name
        
      Application : contributor_orcid
        
      Application : datasheet
        
      Application : description
        
      Application : has_application
        
          
    
        
        
        Application --> "*" Application : has_application
        click Application href "../Application/"
    

        
      Application : id
        
      Application : name
        
      Application : references
        
      Application : related_to
        
          
    
        
        
        Application --> "*" NamedThing : related_to
        click NamedThing href "../NamedThing/"
    

        
      Application : subclass_of
        
          
    
        
        
        Application --> "*" NamedThing : subclass_of
        click NamedThing href "../NamedThing/"
    

        
      Application : used_in_bridge2ai
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **Application**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [datasheet](datasheet.md) | * <br/> [Uriorcurie](Uriorcurie.md) | List of one or more URLs pointing to related datasheets in the Datasheets for... | direct |
| [references](references.md) | * <br/> [Uriorcurie](Uriorcurie.md) | List of one or more URLs pointing to related publications, preprints, or othe... | direct |
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
| [has_application](has_application.md) | * <br/> [Application](Application.md) | A list of one or more specific applications of this entity to a specific purp... | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NamedThing](NamedThing.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [AnatomicalEntity](AnatomicalEntity.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [Application](Application.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [DataStandardOrTool](DataStandardOrTool.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [DataStandard](DataStandard.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [BiomedicalStandard](BiomedicalStandard.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [Registry](Registry.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [OntologyOrVocabulary](OntologyOrVocabulary.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [ModelRepository](ModelRepository.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [SoftwareOrTool](SoftwareOrTool.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [ReferenceImplementation](ReferenceImplementation.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [TrainingProgram](TrainingProgram.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [DataSet](DataSet.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [DataSubstrate](DataSubstrate.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [DataTopic](DataTopic.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [Organization](Organization.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [UseCase](UseCase.md) | [has_application](has_application.md) | range | [Application](Application.md) |
| [Manifest](Manifest.md) | [has_application](has_application.md) | range | [Application](Application.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/Application |
| native | https://w3id.org/bridge2ai/standards-schema-all/Application |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Application
description: A set of details describing a specific application of a resource (e.g.,
  a standard or a dataset) to a specific purpose. In the context of Bridge2AI, this
  will generally refer to an artificial intelligence-driven application. The related_to
  slot can be used to link to other relevant entities, such as other Applications,
  UseCases, DataSets, or Standards. Application objects have unique identifiers with
  the prefix B2AI_APP. This allows an Application to be referenced from other objects
  if needed. The category slot for Application objects should always be set to B2AI:Application
  for clarity.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
is_a: NamedThing
slots:
- datasheet
- references

```
</details>

### Induced

<details>
```yaml
name: Application
description: A set of details describing a specific application of a resource (e.g.,
  a standard or a dataset) to a specific purpose. In the context of Bridge2AI, this
  will generally refer to an artificial intelligence-driven application. The related_to
  slot can be used to link to other relevant entities, such as other Applications,
  UseCases, DataSets, or Standards. Application objects have unique identifiers with
  the prefix B2AI_APP. This allows an Application to be referenced from other objects
  if needed. The category slot for Application objects should always be set to B2AI:Application
  for clarity.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
is_a: NamedThing
attributes:
  datasheet:
    name: datasheet
    description: List of one or more URLs pointing to related datasheets in the Datasheets
      for Datasets format.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: datasheet
    owner: Application
    domain_of:
    - Application
    range: uriorcurie
    multivalued: true
  references:
    name: references
    description: List of one or more URLs pointing to related publications, preprints,
      or other references.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    is_a: node_property
    domain: NamedThing
    alias: references
    owner: Application
    domain_of:
    - Application
    range: uriorcurie
    multivalued: true
  id:
    name: id
    description: A unique identifier for a thing.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: Application
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
    owner: Application
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
    owner: Application
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
    owner: Application
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
    owner: Application
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
    owner: Application
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
    owner: Application
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
    owner: Application
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
    owner: Application
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
    owner: Application
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
    owner: Application
    domain_of:
    - NamedThing
    range: boolean
  has_application:
    name: has_application
    description: A list of one or more specific applications of this entity to a specific
      purpose.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    domain: NamedThing
    alias: has_application
    owner: Application
    domain_of:
    - NamedThing
    range: Application
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>