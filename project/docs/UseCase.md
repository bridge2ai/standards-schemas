
# Class: UseCase


Represents a use case for Bridge2AI standards.

URI: [STANDARDSUSECASE:UseCase](https://w3id.org/bridge2ai/standards-usecase-schema/UseCase)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[UseCaseCollection]++-%20entries%200..*>[UseCase&#124;use_case_category:UseCaseCategory%20%3F;known_limitations:string%20%3F;relevance_to_dgps:DataGeneratingProject%20%3F;data_types:string%20%3F;data_substrates:string%20%3F;standards_and_tools_for_dgp_use:string%20%3F;alternative_standards_and_tools:string%20%3F;enables:string%20%3F;involved_in_experimental_design:string%20%3F;involved_in_metadata_management:string%20%3F;involved_in_quality_control:string%20%3F;xrefs:string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[NamedThing]^-[UseCase],[UseCaseCollection],[NamedThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[UseCaseCollection]++-%20entries%200..*>[UseCase&#124;use_case_category:UseCaseCategory%20%3F;known_limitations:string%20%3F;relevance_to_dgps:DataGeneratingProject%20%3F;data_types:string%20%3F;data_substrates:string%20%3F;standards_and_tools_for_dgp_use:string%20%3F;alternative_standards_and_tools:string%20%3F;enables:string%20%3F;involved_in_experimental_design:string%20%3F;involved_in_metadata_management:string%20%3F;involved_in_quality_control:string%20%3F;xrefs:string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[NamedThing]^-[UseCase],[UseCaseCollection],[NamedThing])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Referenced by Class

 *  **None** *[➞entries](useCaseCollection__entries.md)*  <sub>0..\*</sub>  **[UseCase](UseCase.md)**

## Attributes


### Own

 * [use_case_category](use_case_category.md)  <sub>0..1</sub>
     * Description: Category of the UseCase. Not all projects will incorporate use cases in all categories.
     * Range: [UseCaseCategory](UseCaseCategory.md)
 * [known_limitations](known_limitations.md)  <sub>0..1</sub>
     * Description: Any current obstacles to implementing this use case. This could be a selection from one or more predefined categories including lack of standards, lack of relevant patient cohort, lack of funding, etc.
     * Range: [String](types/String.md)
 * [relevance_to_dgps](relevance_to_dgps.md)  <sub>0..1</sub>
     * Description: Relevance of the use case to one or more DGPs.
     * Range: [DataGeneratingProject](DataGeneratingProject.md)
 * [data_types](data_types.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [data_substrates](data_substrates.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [standards_and_tools_for_dgp_use](standards_and_tools_for_dgp_use.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [alternative_standards_and_tools](alternative_standards_and_tools.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [enables](enables.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [involved_in_experimental_design](involved_in_experimental_design.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [involved_in_metadata_management](involved_in_metadata_management.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [involved_in_quality_control](involved_in_quality_control.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [xrefs](xrefs.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing
     * Range: [String](types/String.md)
