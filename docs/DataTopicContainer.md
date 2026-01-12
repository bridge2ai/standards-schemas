

# Class: DataTopicContainer 


_A container for DataTopics._





URI: [https://w3id.org/bridge2ai/standards-schema-all/DataTopicContainer](https://w3id.org/bridge2ai/standards-schema-all/DataTopicContainer)






```mermaid
 classDiagram
    class DataTopicContainer
    click DataTopicContainer href "../DataTopicContainer"
      DataTopicContainer : data_topics_collection
        
          
    
        
        
        DataTopicContainer --> "*" DataTopic : data_topics_collection
        click DataTopic href "../DataTopic"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [data_topics_collection](data_topics_collection.md) | * <br/> [DataTopic](DataTopic.md) | Collection of associated data topics | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/DataTopicContainer |
| native | https://w3id.org/bridge2ai/standards-schema-all/DataTopicContainer |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataTopicContainer
description: A container for DataTopics.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
slots:
- data_topics_collection

```
</details>

### Induced

<details>
```yaml
name: DataTopicContainer
description: A container for DataTopics.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
attributes:
  data_topics_collection:
    name: data_topics_collection
    description: Collection of associated data topics.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    alias: data_topics_collection
    owner: DataTopicContainer
    domain_of:
    - DataTopicContainer
    range: DataTopic
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>