
# Class: NamedThing

A generic grouping for any identifiable entity

URI: [https://w3id.org/bridge2ai/standards-schema-all/NamedThing](https://w3id.org/bridge2ai/standards-schema-all/NamedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[UseCase],[Organization],[NamedThing]<related_to%200..*-%20[NamedThing&#124;id:uriorcurie;category:category_type%20%3F;name:string%20%3F;description:string%20%3F;contributor_name:string%20%3F;contributor_github_name:string%20%3F;contributor_orcid:uriorcurie%20%3F;contribution_date:date%20%3F],[NamedThing]<subclass_of%200..*-%20[NamedThing],[NamedThing]^-[UseCase],[NamedThing]^-[Organization],[NamedThing]^-[DataTopic],[NamedThing]^-[DataSubstrate],[NamedThing]^-[DataStandardOrTool],[NamedThing]^-[AnatomicalEntity],[DataTopic],[DataSubstrate],[DataStandardOrTool],[AnatomicalEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[UseCase],[Organization],[NamedThing]<related_to%200..*-%20[NamedThing&#124;id:uriorcurie;category:category_type%20%3F;name:string%20%3F;description:string%20%3F;contributor_name:string%20%3F;contributor_github_name:string%20%3F;contributor_orcid:uriorcurie%20%3F;contribution_date:date%20%3F],[NamedThing]<subclass_of%200..*-%20[NamedThing],[NamedThing]^-[UseCase],[NamedThing]^-[Organization],[NamedThing]^-[DataTopic],[NamedThing]^-[DataSubstrate],[NamedThing]^-[DataStandardOrTool],[NamedThing]^-[AnatomicalEntity],[DataTopic],[DataSubstrate],[DataStandardOrTool],[AnatomicalEntity])

## Children

 * [AnatomicalEntity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part
 * [DataStandardOrTool](DataStandardOrTool.md) - Represents a standard or tool in the Bridge2AI Standards Registry.
 * [DataSubstrate](DataSubstrate.md) - Represents a data substrate for Bridge2AI data. This may be a high-level data structure or a specific implementation of that structure. Interpret as "data, in this form or format", as compared to DataStandard, which refers to the set of rules defining a standard. For example, data in TSV format is represented as a DataSubstrate but the concept of TSV format is a DataStandard.
 * [DataTopic](DataTopic.md) - Represents a general data topic for Bridge2AI data or the tools/standards applied to the data.
 * [Organization](Organization.md) - Represents a group or organization related to or responsible for one or more Bridge2AI standards.
 * [UseCase](UseCase.md) - Represents a use case for Bridge2AI standards.

## Referenced by Class

 *  **[NamedThing](NamedThing.md)** *[related_to](related_to.md)*  <sub>0..\*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[subclass_of](subclass_of.md)*  <sub>0..\*</sub>  **[NamedThing](NamedThing.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [category](category.md)  <sub>0..1</sub>
     * Description: CURIE for the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "B2AI_STANDARD:DataStandard".
     * Range: [CategoryType](types/CategoryType.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing.
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing.
     * Range: [String](types/String.md)
 * [subclass_of](subclass_of.md)  <sub>0..\*</sub>
     * Description: Holds between two classes where the domain class is a specialization of the range class.
     * Range: [NamedThing](NamedThing.md)
 * [related_to](related_to.md)  <sub>0..\*</sub>
     * Description: A relationship that is asserted between two named things.
     * Range: [NamedThing](NamedThing.md)
 * [contributor_name](contributor_name.md)  <sub>0..1</sub>
     * Description: The name of the person who added this node.
     * Range: [String](types/String.md)
 * [contributor_github_name](contributor_github_name.md)  <sub>0..1</sub>
     * Description: The name of the github user who added this node.
     * Range: [String](types/String.md)
 * [contributor_orcid](contributor_orcid.md)  <sub>0..1</sub>
     * Description: The ORCiD of the person who added this node.
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * Example: ORCID:0000-0001-1234-5678 None
 * [contribution_date](contribution_date.md)  <sub>0..1</sub>
     * Description: The date on which the node was added.
     * Range: [Date](types/Date.md)
     * Example: 2023-03-20 None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | schema:Thing |