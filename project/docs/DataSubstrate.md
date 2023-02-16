
# Class: DataSubstrate


Represents a data substrate for Bridge2AI data. This may be a high-level data structure or a specific implementation of that structure. Interpret as "data, in this form or format", as compared to DataStandard, which refers to the set of rules defining a standard. For example, data in TSV format is represented as a DataSubstrate but the concept of TSV format is a DataStandard.

URI: [https://w3id.org/bridge2ai/standards-schema-all/DataSubstrate](https://w3id.org/bridge2ai/standards-schema-all/DataSubstrate)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[UseCase]-%20data_substrates%200..*>[DataSubstrate&#124;EDAM_ID:edam_identifier%20%3F;MeSH_ID:mesh_identifier%20%3F;NCIT_ID:ncit_identifier%20%3F;metadata_storage:string%20*;file_extensions:string%20*;limitations:string%20*;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[DataSubstrateContainer]++-%20data_substrates_collection%200..*>[DataSubstrate],[NamedThing]^-[DataSubstrate],[UseCase],[DataSubstrateContainer])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[UseCase]-%20data_substrates%200..*>[DataSubstrate&#124;EDAM_ID:edam_identifier%20%3F;MeSH_ID:mesh_identifier%20%3F;NCIT_ID:ncit_identifier%20%3F;metadata_storage:string%20*;file_extensions:string%20*;limitations:string%20*;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[DataSubstrateContainer]++-%20data_substrates_collection%200..*>[DataSubstrate],[NamedThing]^-[DataSubstrate],[UseCase],[DataSubstrateContainer])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Referenced by Class

 *  **[NamedThing](NamedThing.md)** *[data_substrates](data_substrates.md)*  <sub>0..\*</sub>  **[DataSubstrate](DataSubstrate.md)**
 *  **None** *[data_substrates_collection](data_substrates_collection.md)*  <sub>0..\*</sub>  **[DataSubstrate](DataSubstrate.md)**

## Attributes


### Own

 * [EDAM_ID](EDAM_ID.md)  <sub>0..1</sub>
     * Range: [EdamIdentifier](types/EdamIdentifier.md)
     * Example: edam.data:0006 None
 * [MeSH_ID](MeSH_ID.md)  <sub>0..1</sub>
     * Range: [MeshIdentifier](types/MeshIdentifier.md)
     * Example: MeSH:D014831 None
 * [NCIT_ID](NCIT_ID.md)  <sub>0..1</sub>
     * Range: [NcitIdentifier](types/NcitIdentifier.md)
     * Example: NCIT:C92692 None
 * [metadata_storage](metadata_storage.md)  <sub>0..\*</sub>
     * Description: Data Substrate in which metadata is stored.
     * Range: [String](types/String.md)
 * [file_extensions](file_extensions.md)  <sub>0..\*</sub>
     * Description: Commonly used file extensions for this substrate.
     * Range: [String](types/String.md)
 * [limitations](limitations.md)  <sub>0..\*</sub>
     * Description: Potential obstacles particular to this substrate or implementation. 
     * Range: [String](types/String.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing.
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing.
     * Range: [String](types/String.md)
 * [subclass_of](subclass_of.md)  <sub>0..\*</sub>
     * Description: Holds between two classes where the domain class is a specialization of the range class.
     * Range: [NamedThing](NamedThing.md)
