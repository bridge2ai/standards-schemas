
# Class: DataSubstrate




URI: [https://w3id.org/bridge2ai/standards-schema/DataSubstrate](https://w3id.org/bridge2ai/standards-schema/DataSubstrate)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[UseCase]-%20data_substrates%200..*>[DataSubstrate&#124;EDAM_ID:edam_identifier%20%3F;MeSH_ID:mesh_identifier%20%3F;NCIT_ID:ncit_identifier%20%3F;metadata_storage:string%20*;file_extensions:string%20*;limitations:string%20*;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[NamedThing]^-[DataSubstrate],[UseCase])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[UseCase]-%20data_substrates%200..*>[DataSubstrate&#124;EDAM_ID:edam_identifier%20%3F;MeSH_ID:mesh_identifier%20%3F;NCIT_ID:ncit_identifier%20%3F;metadata_storage:string%20*;file_extensions:string%20*;limitations:string%20*;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[NamedThing]^-[DataSubstrate],[UseCase])

## Parents

 *  is_a: [NamedThing](NamedThing.md)

## Referenced by Class

 *  **[NamedThing](NamedThing.md)** *[data_substrates](data_substrates.md)*  <sub>0..\*</sub>  **[DataSubstrate](DataSubstrate.md)**

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
     * Range: [String](types/String.md)
 * [file_extensions](file_extensions.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [limitations](limitations.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
