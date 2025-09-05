

# Class: OrganizationContainer 


_A container for Organizations._





URI: [https://w3id.org/bridge2ai/standards-schema-all/OrganizationContainer](https://w3id.org/bridge2ai/standards-schema-all/OrganizationContainer)





```mermaid
 classDiagram
    class OrganizationContainer
    click OrganizationContainer href "../OrganizationContainer/"
      OrganizationContainer : organizations
        
          
    
        
        
        OrganizationContainer --> "*" Organization : organizations
        click Organization href "../Organization/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [organizations](organizations.md) | * <br/> [Organization](Organization.md) | Collection of associated organizations | direct |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/bridge2ai/standards-schema-all/OrganizationContainer |
| native | https://w3id.org/bridge2ai/standards-schema-all/OrganizationContainer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OrganizationContainer
description: A container for Organizations.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
slots:
- organizations

```
</details>

### Induced

<details>
```yaml
name: OrganizationContainer
description: A container for Organizations.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
attributes:
  organizations:
    name: organizations
    description: Collection of associated organizations.
    from_schema: https://w3id.org/bridge2ai/standards-schema-all
    rank: 1000
    alias: organizations
    owner: OrganizationContainer
    domain_of:
    - OrganizationContainer
    range: Organization
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>