
# Class: UseCase




URI: [https://w3id.org/bridge2ai/standards-schema/UseCase](https://w3id.org/bridge2ai/standards-schema/UseCase)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DataStandardOrTool]<standards_and_tools_for_dgp_use%200..*-%20[UseCase&#124;involved_in_experimental_design:boolean%20%3F;involved_in_metadata_management:boolean%20%3F;involved_in_quality_control:boolean%20%3F;known_limitations:string%20%3F;relevance_to_dgps:DataGeneratingProject%20*;use_case_category:UseCaseCategory;xref:string%20*;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[UseCase]<enables%200..*-%20[UseCase],[DataTopic]<data_topics%200..*-%20[UseCase],[DataSubstrate]<data_substrates%200..*-%20[UseCase],[DataStandardOrTool]<alternative_standards_and_tools%200..*-%20[UseCase],[UseCaseContainer]++-%20use_cases%200..*>[UseCase],[NamedThing]^-[UseCase],[UseCaseContainer],[NamedThing],[DataTopic],[DataSubstrate],[DataStandardOrTool])](https://yuml.me/diagram/nofunky;dir:TB/class/[DataStandardOrTool]<standards_and_tools_for_dgp_use%200..*-%20[UseCase&#124;involved_in_experimental_design:boolean%20%3F;involved_in_metadata_management:boolean%20%3F;involved_in_quality_control:boolean%20%3F;known_limitations:string%20%3F;relevance_to_dgps:DataGeneratingProject%20*;use_case_category:UseCaseCategory;xref:string%20*;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[UseCase]<enables%200..*-%20[UseCase],[DataTopic]<data_topics%200..*-%20[UseCase],[DataSubstrate]<data_substrates%200..*-%20[UseCase],[DataStandardOrTool]<alternative_standards_and_tools%200..*-%20[UseCase],[UseCaseContainer]++-%20use_cases%200..*>[UseCase],[NamedThing]^-[UseCase],[UseCaseContainer],[NamedThing],[DataTopic],[DataSubstrate],[DataStandardOrTool])

## Parents

 *  is_a: [NamedThing](NamedThing.md)

## Referenced by Class

 *  **[NamedThing](NamedThing.md)** *[enables](enables.md)*  <sub>0..\*</sub>  **[UseCase](UseCase.md)**
 *  **None** *[use_cases](use_cases.md)*  <sub>0..\*</sub>  **[UseCase](UseCase.md)**

## Attributes


### Own

 * [alternative_standards_and_tools](alternative_standards_and_tools.md)  <sub>0..\*</sub>
     * Range: [DataStandardOrTool](DataStandardOrTool.md)
 * [data_substrates](data_substrates.md)  <sub>0..\*</sub>
     * Range: [DataSubstrate](DataSubstrate.md)
 * [data_topics](data_topics.md)  <sub>0..\*</sub>
     * Range: [DataTopic](DataTopic.md)
 * [enables](enables.md)  <sub>0..\*</sub>
     * Range: [UseCase](UseCase.md)
 * [involved_in_experimental_design](involved_in_experimental_design.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [involved_in_metadata_management](involved_in_metadata_management.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [involved_in_quality_control](involved_in_quality_control.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [known_limitations](known_limitations.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [relevance_to_dgps](relevance_to_dgps.md)  <sub>0..\*</sub>
     * Range: [DataGeneratingProject](DataGeneratingProject.md)
 * [standards_and_tools_for_dgp_use](standards_and_tools_for_dgp_use.md)  <sub>0..\*</sub>
     * Range: [DataStandardOrTool](DataStandardOrTool.md)
 * [UseCase➞use_case_category](UseCase_use_case_category.md)  <sub>1..1</sub>
     * Range: [UseCaseCategory](UseCaseCategory.md)
 * [xref](xref.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
