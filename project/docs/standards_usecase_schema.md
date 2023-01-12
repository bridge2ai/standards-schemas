
# standards-usecase-schema


**metamodel version:** 1.7.0

**version:** None


Data schema for Bridge2AI Standards Use Cases.


### Classes

 * [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity
     * [UseCase](UseCase.md) - Represents a UseCase
 * [UseCaseCollection](UseCaseCollection.md) - A holder for UseCase objects

### Mixins


### Slots

 * [age_in_years](age_in_years.md) - Number of years since birth
 * [birth_date](birth_date.md) - Date on which a person is born
 * [description](description.md) - A human-readable description for a thing
 * [id](id.md) - A unique identifier for a thing
 * [name](name.md) - A human-readable name for a thing
 * [primary_email](primary_email.md) - The main email address of a person
     * [UseCase➞primary_email](UseCase_primary_email.md)
 * [➞entries](useCaseCollection__entries.md)
 * [vital_status](vital_status.md) - living or dead status

### Enums

 * [PersonStatus](PersonStatus.md)

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
