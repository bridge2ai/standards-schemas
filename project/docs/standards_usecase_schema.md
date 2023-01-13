
# standards-usecase-schema


**metamodel version:** 1.7.0

**version:** None


Data schema for Bridge2AI Standards Use Cases.


### Classes

 * [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity
     * [UseCase](UseCase.md) - Represents a use case for Bridge2AI standards.
 * [UseCaseCollection](UseCaseCollection.md) - A holder for UseCase objects

### Mixins


### Slots

 * [alternative_standards_and_tools](alternative_standards_and_tools.md)
 * [data_substrates](data_substrates.md)
 * [data_types](data_types.md)
 * [description](description.md) - A human-readable description for a thing
 * [enables](enables.md)
 * [id](id.md) - A unique identifier for a thing
 * [involved_in_experimental_design](involved_in_experimental_design.md)
 * [involved_in_metadata_management](involved_in_metadata_management.md)
 * [involved_in_quality_control](involved_in_quality_control.md)
 * [known_limitations](known_limitations.md) - Any current obstacles to implementing this use case. This could be a selection from one or more predefined categories including lack of standards, lack of relevant patient cohort, lack of funding, etc.
 * [name](name.md) - A human-readable name for a thing
 * [relevance_to_dgps](relevance_to_dgps.md) - Relevance of the use case to one or more DGPs.
 * [standards_and_tools_for_dgp_use](standards_and_tools_for_dgp_use.md)
 * [➞entries](useCaseCollection__entries.md)
 * [use_case_category](use_case_category.md) - Category of the UseCase. Not all projects will incorporate use cases in all categories.
 * [xrefs](xrefs.md)

### Enums

 * [DataGeneratingProject](DataGeneratingProject.md)
 * [UseCaseCategory](UseCaseCategory.md)

### Subsets


### Types


#### Built in

 * **Bool**
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
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
