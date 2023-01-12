
# Class: NamedThing


A generic grouping for any identifiable entity

URI: [standards_usecase_schema:NamedThing](https://w3id.org/bridge2ai/standards-usecase-schema/NamedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[UseCase],[NamedThing&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F]^-[UseCase])](https://yuml.me/diagram/nofunky;dir:TB/class/[UseCase],[NamedThing&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F]^-[UseCase])

## Children

 * [UseCase](UseCase.md) - Represents a UseCase

## Referenced by Class


## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | schema:Thing |

