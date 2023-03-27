
# Class: UseCase


Represents a use case for Bridge2AI standards.

URI: [https://w3id.org/bridge2ai/standards-schema-all/UseCase](https://w3id.org/bridge2ai/standards-schema-all/UseCase)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[UseCase]<enables%200..*-%20[UseCase&#124;use_case_category:UseCaseCategory;known_limitations:string%20%3F;relevance_to_dgps:DataGeneratingProject%20*;involved_in_experimental_design:boolean%20%3F;involved_in_metadata_management:boolean%20%3F;involved_in_quality_control:boolean%20%3F;xref:uriorcurie%20*;id(i):uriorcurie;category(i):category_type%20%3F;name(i):string%20%3F;description(i):string%20%3F;contributor_name(i):string%20%3F;contributor_github_name(i):string%20%3F;contributor_orcid(i):uriorcurie%20%3F;contribution_date(i):date%20%3F],[DataStandardOrTool]<alternative_standards_and_tools%200..*-%20[UseCase],[DataStandardOrTool]<standards_and_tools_for_dgp_use%200..*-%20[UseCase],[DataSubstrate]<data_substrates%200..*-%20[UseCase],[DataTopic]<data_topics%200..*-%20[UseCase],[UseCaseContainer]++-%20use_cases%200..*>[UseCase],[NamedThing]^-[UseCase],[UseCaseContainer],[NamedThing],[DataTopic],[DataSubstrate],[DataStandardOrTool])](https://yuml.me/diagram/nofunky;dir:TB/class/[UseCase]<enables%200..*-%20[UseCase&#124;use_case_category:UseCaseCategory;known_limitations:string%20%3F;relevance_to_dgps:DataGeneratingProject%20*;involved_in_experimental_design:boolean%20%3F;involved_in_metadata_management:boolean%20%3F;involved_in_quality_control:boolean%20%3F;xref:uriorcurie%20*;id(i):uriorcurie;category(i):category_type%20%3F;name(i):string%20%3F;description(i):string%20%3F;contributor_name(i):string%20%3F;contributor_github_name(i):string%20%3F;contributor_orcid(i):uriorcurie%20%3F;contribution_date(i):date%20%3F],[DataStandardOrTool]<alternative_standards_and_tools%200..*-%20[UseCase],[DataStandardOrTool]<standards_and_tools_for_dgp_use%200..*-%20[UseCase],[DataSubstrate]<data_substrates%200..*-%20[UseCase],[DataTopic]<data_topics%200..*-%20[UseCase],[UseCaseContainer]++-%20use_cases%200..*>[UseCase],[NamedThing]^-[UseCase],[UseCaseContainer],[NamedThing],[DataTopic],[DataSubstrate],[DataStandardOrTool])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Referenced by Class

 *  **[NamedThing](NamedThing.md)** *[enables](enables.md)*  <sub>0..\*</sub>  **[UseCase](UseCase.md)**
 *  **None** *[use_cases](use_cases.md)*  <sub>0..\*</sub>  **[UseCase](UseCase.md)**

## Attributes


### Own

 * [UseCase➞use_case_category](UseCase_use_case_category.md)  <sub>1..1</sub>
     * Description: Category of the UseCase. Not all projects will incorporate use cases in all categories.
     * Range: [UseCaseCategory](UseCaseCategory.md)
 * [known_limitations](known_limitations.md)  <sub>0..1</sub>
     * Description: Any current obstacles to implementing this use case. This could be a selection from one or more predefined categories including lack of standards, lack of relevant patient cohort, lack of funding, etc.
     * Range: [String](types/String.md)
 * [relevance_to_dgps](relevance_to_dgps.md)  <sub>0..\*</sub>
     * Description: Relevance of the use case to one or more DGPs.
     * Range: [DataGeneratingProject](DataGeneratingProject.md)
 * [data_topics](data_topics.md)  <sub>0..\*</sub>
     * Description: Relevance of the use case to one or more data topics.
     * Range: [DataTopic](DataTopic.md)
 * [data_substrates](data_substrates.md)  <sub>0..\*</sub>
     * Description: Relevance of the use case to one or more data substrates.
     * Range: [DataSubstrate](DataSubstrate.md)
 * [standards_and_tools_for_dgp_use](standards_and_tools_for_dgp_use.md)  <sub>0..\*</sub>
     * Description: List of identifiers of standards and tools; those planned to be used, or already in use, by one or more Bridge2AI DGPs in addressing this use case, from those in the Standards Registry, or TBD if standards/tools not yet finalized for this use case.
     * Range: [DataStandardOrTool](DataStandardOrTool.md)
 * [alternative_standards_and_tools](alternative_standards_and_tools.md)  <sub>0..\*</sub>
     * Description: List of identifiers of standards and tools; those not explicitly planned to be used, by one or more Bridge2AI DGPs in addressing this use case but serving as viable alternatives, from those in the Standards Registry.
     * Range: [DataStandardOrTool](DataStandardOrTool.md)
 * [enables](enables.md)  <sub>0..\*</sub>
     * Description: Other use case(s) this use case supports or makes possible.
     * Range: [UseCase](UseCase.md)
 * [involved_in_experimental_design](involved_in_experimental_design.md)  <sub>0..1</sub>
     * Description: True if use case is likely to be implemented as part of an experimental procedure or collection of data to be used as part of an experiment.
     * Range: [Boolean](types/Boolean.md)
 * [involved_in_metadata_management](involved_in_metadata_management.md)  <sub>0..1</sub>
     * Description: True if use case is likely to be implemented as part of metadata indexing, sample tracking, or any other storage of high-level data properties. Includes use cases in which metadata will be collected along with data.
     * Range: [Boolean](types/Boolean.md)
 * [involved_in_quality_control](involved_in_quality_control.md)  <sub>0..1</sub>
     * Description: True is use case is likely to be implemented as part of data validation operations.
     * Range: [Boolean](types/Boolean.md)
 * [xref](xref.md)  <sub>0..\*</sub>
     * Description: URI of corresponding class in an ontology of experimental procedures, in CURIE form.
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [category](category.md)  <sub>0..1</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the entity type class, e.g., "BiomedicalStandard".
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
