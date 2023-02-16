
# standards-schema


**metamodel version:** 1.7.0

**version:** None





### Classes

 * [NamedThing](NamedThing.md)
     * [DataStandardOrTool](DataStandardOrTool.md)
     * [DataSubstrate](DataSubstrate.md)
     * [DataTopic](DataTopic.md)
     * [Organization](Organization.md)
     * [UseCase](UseCase.md)
 * [UseCaseContainer](UseCaseContainer.md)

### Mixins


### Slots

 * [EDAM_ID](EDAM_ID.md)
 * [MeSH_ID](MeSH_ID.md)
 * [NCIT_ID](NCIT_ID.md)
 * [ROR_ID](ROR_ID.md)
 * [URL](URL.md)
 * [Wikidata_ID](Wikidata_ID.md)
 * [container_name](container_name.md)
 * [description](description.md)
 * [id](id.md)
 * [name](name.md)
 * [node property](node_property.md)
     * [alternative_standards_and_tools](alternative_standards_and_tools.md)
     * [collection](collection.md)
     * [data_substrates](data_substrates.md)
     * [data_topics](data_topics.md)
     * [enables](enables.md)
     * [file_extensions](file_extensions.md)
     * [formal_specification](formal_specification.md)
     * [involved_in_experimental_design](involved_in_experimental_design.md)
     * [involved_in_metadata_management](involved_in_metadata_management.md)
     * [involved_in_quality_control](involved_in_quality_control.md)
     * [is_open](is_open.md)
     * [known_limitations](known_limitations.md)
     * [limitations](limitations.md)
     * [metadata_storage](metadata_storage.md)
     * [publication](publication.md)
     * [purpose_detail](purpose_detail.md)
     * [requires_registration](requires_registration.md)
     * [standards_and_tools_for_dgp_use](standards_and_tools_for_dgp_use.md)
     * [url](url.md)
     * [use_case_category](use_case_category.md)
         * [UseCase➞use_case_category](UseCase_use_case_category.md)
 * [related_to](related_to.md)
     * [concerns_data_topic](concerns_data_topic.md)
     * [has_relevant_organization](has_relevant_organization.md)
 * [relevance_to_dgps](relevance_to_dgps.md)
 * [use_cases](use_cases.md)
 * [xref](xref.md)

### Enums

 * [DataGeneratingProject](DataGeneratingProject.md)
 * [StandardsCollectionTag](StandardsCollectionTag.md)
 * [UseCaseCategory](UseCaseCategory.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [EdamIdentifier](types/EdamIdentifier.md)  ([Uriorcurie](types/Uriorcurie.md)) 
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [MeshIdentifier](types/MeshIdentifier.md)  ([Uriorcurie](types/Uriorcurie.md)) 
 * [NcitIdentifier](types/NcitIdentifier.md)  ([Uriorcurie](types/Uriorcurie.md)) 
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [RorIdentifier](types/RorIdentifier.md)  ([Uriorcurie](types/Uriorcurie.md)) 
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
 * [WikidataIdentifier](types/WikidataIdentifier.md)  ([Uriorcurie](types/Uriorcurie.md)) 
