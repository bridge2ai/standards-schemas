# Auto generated from standards_schema_all.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-06-12T11:10:08
# Schema: standards-schema-all
#
# id: https://w3id.org/bridge2ai/standards-schema-all
# description: High-level classes for Bridge2AI Standards schemas.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
B2AI = CurieNamespace('B2AI', 'https://w3id.org/bridge2ai/standards-schema/')
B2AI_DATA = CurieNamespace('B2AI_DATA', 'https://w3id.org/bridge2ai/standards-dataset-schema/')
B2AI_ORG = CurieNamespace('B2AI_ORG', 'https://w3id.org/bridge2ai/standards-organization-schema/')
B2AI_STANDARD = CurieNamespace('B2AI_STANDARD', 'https://w3id.org/bridge2ai/standards-datastandardortool-schema/')
B2AI_SUBSTRATE = CurieNamespace('B2AI_SUBSTRATE', 'https://w3id.org/bridge2ai/standards-datasubstrate-schema/')
B2AI_TOPIC = CurieNamespace('B2AI_TOPIC', 'https://w3id.org/bridge2ai/standards-datatopic-schema/')
B2AI_USECASE = CurieNamespace('B2AI_USECASE', 'https://w3id.org/bridge2ai/standards-usecase-schema/')
MESH = CurieNamespace('MESH', 'http://id.nlm.nih.gov/mesh/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NCIT = CurieNamespace('ncit', 'http://purl.obolibrary.org/obo/NCIT_')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
UBERON = CurieNamespace('uberon', 'http://purl.obolibrary.org/obo/uberon/core#')
WIKIDATA = CurieNamespace('wikidata', 'http://www.wikidata.org/wiki/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/bridge2ai/standards-schema-all/')


# Types
class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the model. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "category_type"
    type_model_uri = URIRef("https://w3id.org/bridge2ai/standards-schema-all/CategoryType")


class EdamIdentifier(Uriorcurie):
    """ Identifier from EDAM ontology """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "edam_identifier"
    type_model_uri = URIRef("https://w3id.org/bridge2ai/standards-schema-all/EdamIdentifier")


class MeshIdentifier(Uriorcurie):
    """ Identifier from Medical Subject Headings (MeSH) biomedical vocabulary. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "mesh_identifier"
    type_model_uri = URIRef("https://w3id.org/bridge2ai/standards-schema-all/MeshIdentifier")


class NcitIdentifier(Uriorcurie):
    """ Identifier from NCIT reference terminology with broad coverage of the cancer domain. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "ncit_identifier"
    type_model_uri = URIRef("https://w3id.org/bridge2ai/standards-schema-all/NcitIdentifier")


class RorIdentifier(Uriorcurie):
    """ Identifier from Research Organization Registry. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "ror_identifier"
    type_model_uri = URIRef("https://w3id.org/bridge2ai/standards-schema-all/RorIdentifier")


class WikidataIdentifier(Uriorcurie):
    """ Identifier from Wikidata open knowledge base. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "wikidata_identifier"
    type_model_uri = URIRef("https://w3id.org/bridge2ai/standards-schema-all/WikidataIdentifier")


# Class references
class NamedThingId(URIorCURIE):
    pass


class AnatomicalEntityId(NamedThingId):
    pass


class DataStandardOrToolId(NamedThingId):
    pass


class DataStandardId(DataStandardOrToolId):
    pass


class BiomedicalStandardId(DataStandardId):
    pass


class RegistryId(DataStandardOrToolId):
    pass


class OntologyOrVocabularyId(DataStandardOrToolId):
    pass


class ModelRepositoryId(DataStandardOrToolId):
    pass


class SoftwareOrToolId(DataStandardOrToolId):
    pass


class ReferenceImplementationId(DataStandardOrToolId):
    pass


class TrainingProgramId(DataStandardOrToolId):
    pass


class DataSetId(NamedThingId):
    pass


class DataSubstrateId(NamedThingId):
    pass


class DataTopicId(NamedThingId):
    pass


class OrganizationId(NamedThingId):
    pass


class UseCaseId(NamedThingId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to"]

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/NamedThing")

    id: Union[str, NamedThingId] = None
    category: Optional[Union[str, CategoryType]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    subclass_of: Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]] = empty_list()
    related_to: Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]] = empty_list()
    contributor_name: Optional[str] = None
    contributor_github_name: Optional[str] = None
    contributor_orcid: Optional[Union[str, URIorCURIE]] = None
    contribution_date: Optional[Union[str, XSDDate]] = None
    used_in_bridge2ai: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        self.category = str(self.class_class_curie)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.subclass_of]

        if not isinstance(self.related_to, list):
            self.related_to = [self.related_to] if self.related_to is not None else []
        self.related_to = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.related_to]

        if self.contributor_name is not None and not isinstance(self.contributor_name, str):
            self.contributor_name = str(self.contributor_name)

        if self.contributor_github_name is not None and not isinstance(self.contributor_github_name, str):
            self.contributor_github_name = str(self.contributor_github_name)

        if self.contributor_orcid is not None and not isinstance(self.contributor_orcid, URIorCURIE):
            self.contributor_orcid = URIorCURIE(self.contributor_orcid)

        if self.contribution_date is not None and not isinstance(self.contribution_date, XSDDate):
            self.contribution_date = XSDDate(self.contribution_date)

        if self.used_in_bridge2ai is not None and not isinstance(self.used_in_bridge2ai, Bool):
            self.used_in_bridge2ai = Bool(self.used_in_bridge2ai)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "category"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class AnatomicalEntity(NamedThing):
    """
    A subcellular location, cell type or gross anatomical part
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to"]

    class_class_uri: ClassVar[URIRef] = B2AI["AnatomicalEntity"]
    class_class_curie: ClassVar[str] = "B2AI:AnatomicalEntity"
    class_name: ClassVar[str] = "AnatomicalEntity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/AnatomicalEntity")

    id: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class DataStandardOrTool(NamedThing):
    """
    Represents a standard or tool in the Bridge2AI Standards Registry.
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to", "concerns_data_topic", "has_relevant_organization", "has_relevant_data_substrate"]

    class_class_uri: ClassVar[URIRef] = B2AI_STANDARD["DataStandardOrTool"]
    class_class_curie: ClassVar[str] = "B2AI_STANDARD:DataStandardOrTool"
    class_name: ClassVar[str] = "DataStandardOrTool"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/DataStandardOrTool")

    id: Union[str, DataStandardOrToolId] = None
    collection: Optional[Union[Union[str, "StandardsCollectionTag"], list[Union[str, "StandardsCollectionTag"]]]] = empty_list()
    concerns_data_topic: Optional[Union[Union[str, DataTopicId], list[Union[str, DataTopicId]]]] = empty_list()
    has_relevant_organization: Optional[Union[Union[str, OrganizationId], list[Union[str, OrganizationId]]]] = empty_list()
    has_training_resource: Optional[Union[Union[str, DataStandardOrToolId], list[Union[str, DataStandardOrToolId]]]] = empty_list()
    purpose_detail: Optional[str] = None
    is_open: Optional[Union[bool, Bool]] = None
    requires_registration: Optional[Union[bool, Bool]] = None
    url: Optional[Union[str, URIorCURIE]] = None
    publication: Optional[Union[str, URIorCURIE]] = None
    formal_specification: Optional[Union[str, URIorCURIE]] = None
    responsible_organization: Optional[Union[Union[str, OrganizationId], list[Union[str, OrganizationId]]]] = empty_list()
    has_relevant_data_substrate: Optional[Union[Union[str, DataSubstrateId], list[Union[str, DataSubstrateId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataStandardOrToolId):
            self.id = DataStandardOrToolId(self.id)

        if not isinstance(self.collection, list):
            self.collection = [self.collection] if self.collection is not None else []
        self.collection = [v if isinstance(v, StandardsCollectionTag) else StandardsCollectionTag(v) for v in self.collection]

        if not isinstance(self.concerns_data_topic, list):
            self.concerns_data_topic = [self.concerns_data_topic] if self.concerns_data_topic is not None else []
        self.concerns_data_topic = [v if isinstance(v, DataTopicId) else DataTopicId(v) for v in self.concerns_data_topic]

        if not isinstance(self.has_relevant_organization, list):
            self.has_relevant_organization = [self.has_relevant_organization] if self.has_relevant_organization is not None else []
        self.has_relevant_organization = [v if isinstance(v, OrganizationId) else OrganizationId(v) for v in self.has_relevant_organization]

        if not isinstance(self.has_training_resource, list):
            self.has_training_resource = [self.has_training_resource] if self.has_training_resource is not None else []
        self.has_training_resource = [v if isinstance(v, DataStandardOrToolId) else DataStandardOrToolId(v) for v in self.has_training_resource]

        if self.purpose_detail is not None and not isinstance(self.purpose_detail, str):
            self.purpose_detail = str(self.purpose_detail)

        if self.is_open is not None and not isinstance(self.is_open, Bool):
            self.is_open = Bool(self.is_open)

        if self.requires_registration is not None and not isinstance(self.requires_registration, Bool):
            self.requires_registration = Bool(self.requires_registration)

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        if self.publication is not None and not isinstance(self.publication, URIorCURIE):
            self.publication = URIorCURIE(self.publication)

        if self.formal_specification is not None and not isinstance(self.formal_specification, URIorCURIE):
            self.formal_specification = URIorCURIE(self.formal_specification)

        if not isinstance(self.responsible_organization, list):
            self.responsible_organization = [self.responsible_organization] if self.responsible_organization is not None else []
        self.responsible_organization = [v if isinstance(v, OrganizationId) else OrganizationId(v) for v in self.responsible_organization]

        if not isinstance(self.has_relevant_data_substrate, list):
            self.has_relevant_data_substrate = [self.has_relevant_data_substrate] if self.has_relevant_data_substrate is not None else []
        self.has_relevant_data_substrate = [v if isinstance(v, DataSubstrateId) else DataSubstrateId(v) for v in self.has_relevant_data_substrate]

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class DataStandard(DataStandardOrTool):
    """
    Represents a general purpose standard in the Bridge2AI Standards Registry.
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to", "concerns_data_topic", "has_relevant_organization", "has_relevant_data_substrate"]

    class_class_uri: ClassVar[URIRef] = B2AI_STANDARD["DataStandard"]
    class_class_curie: ClassVar[str] = "B2AI_STANDARD:DataStandard"
    class_name: ClassVar[str] = "DataStandard"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/DataStandard")

    id: Union[str, DataStandardId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataStandardId):
            self.id = DataStandardId(self.id)

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class BiomedicalStandard(DataStandard):
    """
    Represents a standard in the Bridge2AI Standards Registry with particular applications or relevance to clinical or
    biomedical research purposes.
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to", "concerns_data_topic", "has_relevant_organization", "has_relevant_data_substrate"]

    class_class_uri: ClassVar[URIRef] = B2AI_STANDARD["BiomedicalStandard"]
    class_class_curie: ClassVar[str] = "B2AI_STANDARD:BiomedicalStandard"
    class_name: ClassVar[str] = "BiomedicalStandard"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/BiomedicalStandard")

    id: Union[str, BiomedicalStandardId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiomedicalStandardId):
            self.id = BiomedicalStandardId(self.id)

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class Registry(DataStandardOrTool):
    """
    Represents a resource in the Bridge2AI Standards Registry serving to curate and/or index other resources.
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to", "concerns_data_topic", "has_relevant_organization", "has_relevant_data_substrate"]

    class_class_uri: ClassVar[URIRef] = B2AI_STANDARD["Registry"]
    class_class_curie: ClassVar[str] = "B2AI_STANDARD:Registry"
    class_name: ClassVar[str] = "Registry"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/Registry")

    id: Union[str, RegistryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegistryId):
            self.id = RegistryId(self.id)

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class OntologyOrVocabulary(DataStandardOrTool):
    """
    A set of concepts and categories, potentially defined or accompanied by their hierarchical relationships.
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to", "concerns_data_topic", "has_relevant_organization", "has_relevant_data_substrate"]

    class_class_uri: ClassVar[URIRef] = B2AI_STANDARD["OntologyOrVocabulary"]
    class_class_curie: ClassVar[str] = "B2AI_STANDARD:OntologyOrVocabulary"
    class_name: ClassVar[str] = "OntologyOrVocabulary"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/OntologyOrVocabulary")

    id: Union[str, OntologyOrVocabularyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyOrVocabularyId):
            self.id = OntologyOrVocabularyId(self.id)

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class ModelRepository(DataStandardOrTool):
    """
    Represents a resource in the Bridge2AI Standards Registry serving to curate and store computational models. To be
    a repository, the resource must not index models alone.
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to", "concerns_data_topic", "has_relevant_organization", "has_relevant_data_substrate"]

    class_class_uri: ClassVar[URIRef] = B2AI_STANDARD["ModelRepository"]
    class_class_curie: ClassVar[str] = "B2AI_STANDARD:ModelRepository"
    class_name: ClassVar[str] = "ModelRepository"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/ModelRepository")

    id: Union[str, ModelRepositoryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelRepositoryId):
            self.id = ModelRepositoryId(self.id)

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class SoftwareOrTool(DataStandardOrTool):
    """
    Represents a piece of software or computational tool in the Bridge2AI Standards Registry.
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to", "concerns_data_topic", "has_relevant_organization", "has_relevant_data_substrate"]

    class_class_uri: ClassVar[URIRef] = B2AI_STANDARD["SoftwareOrTool"]
    class_class_curie: ClassVar[str] = "B2AI_STANDARD:SoftwareOrTool"
    class_name: ClassVar[str] = "SoftwareOrTool"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/SoftwareOrTool")

    id: Union[str, SoftwareOrToolId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoftwareOrToolId):
            self.id = SoftwareOrToolId(self.id)

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class ReferenceImplementation(DataStandardOrTool):
    """
    Represents an implementation of one or more standards or tools in the Bridge2AI Standards Registry, whether as a
    full specification in a particular language or as an application to a specific use case.
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to", "concerns_data_topic", "has_relevant_organization", "has_relevant_data_substrate"]

    class_class_uri: ClassVar[URIRef] = B2AI_STANDARD["ReferenceImplementation"]
    class_class_curie: ClassVar[str] = "B2AI_STANDARD:ReferenceImplementation"
    class_name: ClassVar[str] = "ReferenceImplementation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/ReferenceImplementation")

    id: Union[str, ReferenceImplementationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReferenceImplementationId):
            self.id = ReferenceImplementationId(self.id)

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class TrainingProgram(DataStandardOrTool):
    """
    Represents a training program for skills and experience related to standards or tools in the Bridge2AI Standards
    Registry.
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to", "concerns_data_topic", "has_relevant_organization", "has_relevant_data_substrate"]

    class_class_uri: ClassVar[URIRef] = B2AI_STANDARD["TrainingProgram"]
    class_class_curie: ClassVar[str] = "B2AI_STANDARD:TrainingProgram"
    class_name: ClassVar[str] = "TrainingProgram"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/TrainingProgram")

    id: Union[str, TrainingProgramId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TrainingProgramId):
            self.id = TrainingProgramId(self.id)

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class DataStandardOrToolContainer(YAMLRoot):
    """
    A container for DataStandardOrTool(s).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = B2AI_STANDARD["DataStandardOrToolContainer"]
    class_class_curie: ClassVar[str] = "B2AI_STANDARD:DataStandardOrToolContainer"
    class_name: ClassVar[str] = "DataStandardOrToolContainer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/DataStandardOrToolContainer")

    data_standardortools_collection: Optional[Union[dict[Union[str, DataStandardOrToolId], Union[dict, DataStandardOrTool]], list[Union[dict, DataStandardOrTool]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="data_standardortools_collection", slot_type=DataStandardOrTool, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSet(NamedThing):
    """
    Represents a data set by its metadata. This may or may not be produced by a group in the Bridge2AI consortium.
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to", "has_files", "has_parts", "produced_by", "substrates", "topics"]

    class_class_uri: ClassVar[URIRef] = B2AI_DATA["DataSet"]
    class_class_curie: ClassVar[str] = "B2AI_DATA:DataSet"
    class_name: ClassVar[str] = "DataSet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/DataSet")

    id: Union[str, DataSetId] = None
    has_files: Optional[Union[str, list[str]]] = empty_list()
    has_parts: Optional[Union[Union[str, DataSetId], list[Union[str, DataSetId]]]] = empty_list()
    produced_by: Optional[Union[Union[str, OrganizationId], list[Union[str, OrganizationId]]]] = empty_list()
    data_url: Optional[Union[str, URIorCURIE]] = None
    documentation_url: Optional[Union[str, URIorCURIE]] = None
    datasheet_url: Optional[Union[str, URIorCURIE]] = None
    is_public: Optional[Union[bool, Bool]] = None
    substrates: Optional[Union[Union[str, DataSubstrateId], list[Union[str, DataSubstrateId]]]] = empty_list()
    topics: Optional[Union[Union[str, DataTopicId], list[Union[str, DataTopicId]]]] = empty_list()
    is_bridge2ai_data: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSetId):
            self.id = DataSetId(self.id)

        if not isinstance(self.has_files, list):
            self.has_files = [self.has_files] if self.has_files is not None else []
        self.has_files = [v if isinstance(v, str) else str(v) for v in self.has_files]

        if not isinstance(self.has_parts, list):
            self.has_parts = [self.has_parts] if self.has_parts is not None else []
        self.has_parts = [v if isinstance(v, DataSetId) else DataSetId(v) for v in self.has_parts]

        if not isinstance(self.produced_by, list):
            self.produced_by = [self.produced_by] if self.produced_by is not None else []
        self.produced_by = [v if isinstance(v, OrganizationId) else OrganizationId(v) for v in self.produced_by]

        if self.data_url is not None and not isinstance(self.data_url, URIorCURIE):
            self.data_url = URIorCURIE(self.data_url)

        if self.documentation_url is not None and not isinstance(self.documentation_url, URIorCURIE):
            self.documentation_url = URIorCURIE(self.documentation_url)

        if self.datasheet_url is not None and not isinstance(self.datasheet_url, URIorCURIE):
            self.datasheet_url = URIorCURIE(self.datasheet_url)

        if self.is_public is not None and not isinstance(self.is_public, Bool):
            self.is_public = Bool(self.is_public)

        if not isinstance(self.substrates, list):
            self.substrates = [self.substrates] if self.substrates is not None else []
        self.substrates = [v if isinstance(v, DataSubstrateId) else DataSubstrateId(v) for v in self.substrates]

        if not isinstance(self.topics, list):
            self.topics = [self.topics] if self.topics is not None else []
        self.topics = [v if isinstance(v, DataTopicId) else DataTopicId(v) for v in self.topics]

        if self.is_bridge2ai_data is not None and not isinstance(self.is_bridge2ai_data, Bool):
            self.is_bridge2ai_data = Bool(self.is_bridge2ai_data)

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class DataSetContainer(YAMLRoot):
    """
    A container for DataSets.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = B2AI_DATA["DataSetContainer"]
    class_class_curie: ClassVar[str] = "B2AI_DATA:DataSetContainer"
    class_name: ClassVar[str] = "DataSetContainer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/DataSetContainer")

    data_collection: Optional[Union[dict[Union[str, DataSetId], Union[dict, DataSet]], list[Union[dict, DataSet]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="data_collection", slot_type=DataSet, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSubstrate(NamedThing):
    """
    Represents a data substrate for Bridge2AI data. This may be a high-level data structure or a specific
    implementation of that structure. Interpret as "data, in this form or format", as compared to DataStandard, which
    refers to the set of rules defining a standard. For example, data in TSV format is represented as a DataSubstrate
    but the concept of TSV format is a DataStandard.
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to"]

    class_class_uri: ClassVar[URIRef] = B2AI_SUBSTRATE["DataSubstrate"]
    class_class_curie: ClassVar[str] = "B2AI_SUBSTRATE:DataSubstrate"
    class_name: ClassVar[str] = "DataSubstrate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/DataSubstrate")

    id: Union[str, DataSubstrateId] = None
    edam_id: Optional[Union[str, EdamIdentifier]] = None
    mesh_id: Optional[Union[str, MeshIdentifier]] = None
    ncit_id: Optional[Union[str, NcitIdentifier]] = None
    metadata_storage: Optional[Union[str, list[str]]] = empty_list()
    file_extensions: Optional[Union[str, list[str]]] = empty_list()
    limitations: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSubstrateId):
            self.id = DataSubstrateId(self.id)

        if self.edam_id is not None and not isinstance(self.edam_id, EdamIdentifier):
            self.edam_id = EdamIdentifier(self.edam_id)

        if self.mesh_id is not None and not isinstance(self.mesh_id, MeshIdentifier):
            self.mesh_id = MeshIdentifier(self.mesh_id)

        if self.ncit_id is not None and not isinstance(self.ncit_id, NcitIdentifier):
            self.ncit_id = NcitIdentifier(self.ncit_id)

        if not isinstance(self.metadata_storage, list):
            self.metadata_storage = [self.metadata_storage] if self.metadata_storage is not None else []
        self.metadata_storage = [v if isinstance(v, str) else str(v) for v in self.metadata_storage]

        if not isinstance(self.file_extensions, list):
            self.file_extensions = [self.file_extensions] if self.file_extensions is not None else []
        self.file_extensions = [v if isinstance(v, str) else str(v) for v in self.file_extensions]

        if not isinstance(self.limitations, list):
            self.limitations = [self.limitations] if self.limitations is not None else []
        self.limitations = [v if isinstance(v, str) else str(v) for v in self.limitations]

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class DataSubstrateContainer(YAMLRoot):
    """
    A container for DataSubstrates.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = B2AI_SUBSTRATE["DataSubstrateContainer"]
    class_class_curie: ClassVar[str] = "B2AI_SUBSTRATE:DataSubstrateContainer"
    class_name: ClassVar[str] = "DataSubstrateContainer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/DataSubstrateContainer")

    data_substrates_collection: Optional[Union[dict[Union[str, DataSubstrateId], Union[dict, DataSubstrate]], list[Union[dict, DataSubstrate]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="data_substrates_collection", slot_type=DataSubstrate, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataTopic(NamedThing):
    """
    Represents a general data topic for Bridge2AI data or the tools/standards applied to the data.
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to", "topic_involves_anatomy"]

    class_class_uri: ClassVar[URIRef] = B2AI_TOPIC["DataTopic"]
    class_class_curie: ClassVar[str] = "B2AI_TOPIC:DataTopic"
    class_name: ClassVar[str] = "DataTopic"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/DataTopic")

    id: Union[str, DataTopicId] = None
    edam_id: Optional[Union[str, EdamIdentifier]] = None
    mesh_id: Optional[Union[str, MeshIdentifier]] = None
    ncit_id: Optional[Union[str, NcitIdentifier]] = None
    topic_involves_anatomy: Optional[Union[Union[str, AnatomicalEntityId], list[Union[str, AnatomicalEntityId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataTopicId):
            self.id = DataTopicId(self.id)

        if self.edam_id is not None and not isinstance(self.edam_id, EdamIdentifier):
            self.edam_id = EdamIdentifier(self.edam_id)

        if self.mesh_id is not None and not isinstance(self.mesh_id, MeshIdentifier):
            self.mesh_id = MeshIdentifier(self.mesh_id)

        if self.ncit_id is not None and not isinstance(self.ncit_id, NcitIdentifier):
            self.ncit_id = NcitIdentifier(self.ncit_id)

        if not isinstance(self.topic_involves_anatomy, list):
            self.topic_involves_anatomy = [self.topic_involves_anatomy] if self.topic_involves_anatomy is not None else []
        self.topic_involves_anatomy = [v if isinstance(v, AnatomicalEntityId) else AnatomicalEntityId(v) for v in self.topic_involves_anatomy]

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class DataTopicContainer(YAMLRoot):
    """
    A container for DataTopics.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = B2AI_TOPIC["DataTopicContainer"]
    class_class_curie: ClassVar[str] = "B2AI_TOPIC:DataTopicContainer"
    class_name: ClassVar[str] = "DataTopicContainer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/DataTopicContainer")

    data_topics_collection: Optional[Union[dict[Union[str, DataTopicId], Union[dict, DataTopic]], list[Union[dict, DataTopic]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="data_topics_collection", slot_type=DataTopic, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(NamedThing):
    """
    Represents a group or organization related to or responsible for one or more Bridge2AI standards.
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to"]

    class_class_uri: ClassVar[URIRef] = B2AI_ORG["Organization"]
    class_class_curie: ClassVar[str] = "B2AI_ORG:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/Organization")

    id: Union[str, OrganizationId] = None
    ror_id: Optional[Union[str, RorIdentifier]] = None
    wikidata_id: Optional[Union[str, WikidataIdentifier]] = None
    url: Optional[Union[str, URIorCURIE]] = None
    related_to: Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        if self.ror_id is not None and not isinstance(self.ror_id, RorIdentifier):
            self.ror_id = RorIdentifier(self.ror_id)

        if self.wikidata_id is not None and not isinstance(self.wikidata_id, WikidataIdentifier):
            self.wikidata_id = WikidataIdentifier(self.wikidata_id)

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        if not isinstance(self.related_to, list):
            self.related_to = [self.related_to] if self.related_to is not None else []
        self.related_to = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.related_to]

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class OrganizationContainer(YAMLRoot):
    """
    A container for Organizations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = B2AI_ORG["OrganizationContainer"]
    class_class_curie: ClassVar[str] = "B2AI_ORG:OrganizationContainer"
    class_name: ClassVar[str] = "OrganizationContainer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/OrganizationContainer")

    organizations: Optional[Union[dict[Union[str, OrganizationId], Union[dict, Organization]], list[Union[dict, Organization]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="organizations", slot_type=Organization, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UseCase(NamedThing):
    """
    Represents a use case for Bridge2AI standards.
    """
    _inherited_slots: ClassVar[list[str]] = ["subclass_of", "related_to"]

    class_class_uri: ClassVar[URIRef] = B2AI_USECASE["UseCase"]
    class_class_curie: ClassVar[str] = "B2AI_USECASE:UseCase"
    class_name: ClassVar[str] = "UseCase"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/UseCase")

    id: Union[str, UseCaseId] = None
    use_case_category: Union[Union[str, "UseCaseCategory"], list[Union[str, "UseCaseCategory"]]] = None
    known_limitations: Optional[str] = None
    relevant_to_gcs: Optional[Union[Union[str, OrganizationId], list[Union[str, OrganizationId]]]] = empty_list()
    data_topics: Optional[Union[Union[str, DataTopicId], list[Union[str, DataTopicId]]]] = empty_list()
    data_substrates: Optional[Union[Union[str, DataSubstrateId], list[Union[str, DataSubstrateId]]]] = empty_list()
    standards_and_tools_for_gc_use: Optional[Union[Union[str, DataStandardOrToolId], list[Union[str, DataStandardOrToolId]]]] = empty_list()
    alternative_standards_and_tools: Optional[Union[Union[str, DataStandardOrToolId], list[Union[str, DataStandardOrToolId]]]] = empty_list()
    enables: Optional[Union[Union[str, UseCaseId], list[Union[str, UseCaseId]]]] = empty_list()
    involved_in_experimental_design: Optional[Union[bool, Bool]] = None
    involved_in_metadata_management: Optional[Union[bool, Bool]] = None
    involved_in_quality_control: Optional[Union[bool, Bool]] = None
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UseCaseId):
            self.id = UseCaseId(self.id)

        if self._is_empty(self.use_case_category):
            self.MissingRequiredField("use_case_category")
        if not isinstance(self.use_case_category, list):
            self.use_case_category = [self.use_case_category] if self.use_case_category is not None else []
        self.use_case_category = [v if isinstance(v, UseCaseCategory) else UseCaseCategory(v) for v in self.use_case_category]

        if self.known_limitations is not None and not isinstance(self.known_limitations, str):
            self.known_limitations = str(self.known_limitations)

        if not isinstance(self.relevant_to_gcs, list):
            self.relevant_to_gcs = [self.relevant_to_gcs] if self.relevant_to_gcs is not None else []
        self.relevant_to_gcs = [v if isinstance(v, OrganizationId) else OrganizationId(v) for v in self.relevant_to_gcs]

        if not isinstance(self.data_topics, list):
            self.data_topics = [self.data_topics] if self.data_topics is not None else []
        self.data_topics = [v if isinstance(v, DataTopicId) else DataTopicId(v) for v in self.data_topics]

        if not isinstance(self.data_substrates, list):
            self.data_substrates = [self.data_substrates] if self.data_substrates is not None else []
        self.data_substrates = [v if isinstance(v, DataSubstrateId) else DataSubstrateId(v) for v in self.data_substrates]

        if not isinstance(self.standards_and_tools_for_gc_use, list):
            self.standards_and_tools_for_gc_use = [self.standards_and_tools_for_gc_use] if self.standards_and_tools_for_gc_use is not None else []
        self.standards_and_tools_for_gc_use = [v if isinstance(v, DataStandardOrToolId) else DataStandardOrToolId(v) for v in self.standards_and_tools_for_gc_use]

        if not isinstance(self.alternative_standards_and_tools, list):
            self.alternative_standards_and_tools = [self.alternative_standards_and_tools] if self.alternative_standards_and_tools is not None else []
        self.alternative_standards_and_tools = [v if isinstance(v, DataStandardOrToolId) else DataStandardOrToolId(v) for v in self.alternative_standards_and_tools]

        if not isinstance(self.enables, list):
            self.enables = [self.enables] if self.enables is not None else []
        self.enables = [v if isinstance(v, UseCaseId) else UseCaseId(v) for v in self.enables]

        if self.involved_in_experimental_design is not None and not isinstance(self.involved_in_experimental_design, Bool):
            self.involved_in_experimental_design = Bool(self.involved_in_experimental_design)

        if self.involved_in_metadata_management is not None and not isinstance(self.involved_in_metadata_management, Bool):
            self.involved_in_metadata_management = Bool(self.involved_in_metadata_management)

        if self.involved_in_quality_control is not None and not isinstance(self.involved_in_quality_control, Bool):
            self.involved_in_quality_control = Bool(self.involved_in_quality_control)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)
        self.category = str(self.class_class_curie)


@dataclass(repr=False)
class UseCaseContainer(YAMLRoot):
    """
    A container for UseCase.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = B2AI_USECASE["UseCaseContainer"]
    class_class_curie: ClassVar[str] = "B2AI_USECASE:UseCaseContainer"
    class_name: ClassVar[str] = "UseCaseContainer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema-all/UseCaseContainer")

    use_cases: Optional[Union[dict[Union[str, UseCaseId], Union[dict, UseCase]], list[Union[dict, UseCase]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="use_cases", slot_type=UseCase, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class StandardsCollectionTag(EnumDefinitionImpl):
    """
    Tags for specific sets of standards.
    """
    audiovisual = PermissibleValue(
        text="audiovisual",
        description="Audiovisual Standard")
    deprecated = PermissibleValue(
        text="deprecated",
        description="Deprecated")
    fileformat = PermissibleValue(
        text="fileformat",
        description="File Format")
    toolkit = PermissibleValue(
        text="toolkit",
        description="Bioinformatics Toolkit")
    clinicaldata = PermissibleValue(
        text="clinicaldata",
        description="Clinical Data")
    multimodal = PermissibleValue(
        text="multimodal",
        description="Multimodal Data Integration")
    text = PermissibleValue(
        text="text",
        description="Text Data")
    cloudplatform = PermissibleValue(
        text="cloudplatform",
        description="Cloud Research Platform")
    cloudservice = PermissibleValue(
        text="cloudservice",
        description="Cloud Service")
    codesystem = PermissibleValue(
        text="codesystem",
        description="Code System")
    datamodel = PermissibleValue(
        text="datamodel",
        description="Data Model")
    dataregistry = PermissibleValue(
        text="dataregistry",
        description="Data Registry")
    softwareregistry = PermissibleValue(
        text="softwareregistry",
        description="Software Registry")
    datavisualization = PermissibleValue(
        text="datavisualization",
        description="Data Visualization")
    notebookplatform = PermissibleValue(
        text="notebookplatform",
        description="Notebook Platform")
    datasheets = PermissibleValue(
        text="datasheets",
        description="Datasheets")
    machinelearningframework = PermissibleValue(
        text="machinelearningframework",
        description="Machine Learning Framework")
    workflowlanguage = PermissibleValue(
        text="workflowlanguage",
        description="Workflow Language")
    diagnosticinstrument = PermissibleValue(
        text="diagnosticinstrument",
        description="Diagnostic Instrument")
    drugdata = PermissibleValue(
        text="drugdata",
        description="Drug Data")
    eyedata = PermissibleValue(
        text="eyedata",
        description="Eye Data")
    markuplanguage = PermissibleValue(
        text="markuplanguage",
        description="Markup Language")
    graphdataplatform = PermissibleValue(
        text="graphdataplatform",
        description="Graph Data Platform")
    guidelines = PermissibleValue(
        text="guidelines",
        description="Guidelines")
    minimuminformationschema = PermissibleValue(
        text="minimuminformationschema",
        description="Minimum Information Schema")
    modelcards = PermissibleValue(
        text="modelcards",
        description="Model Cards")
    obofoundry = PermissibleValue(
        text="obofoundry",
        description="OBO Foundry")
    ontologyregistry = PermissibleValue(
        text="ontologyregistry",
        description="Ontology Registry")
    policy = PermissibleValue(
        text="policy",
        description="Policy")
    proteindata = PermissibleValue(
        text="proteindata",
        description="Protein Data")
    referencegenome = PermissibleValue(
        text="referencegenome",
        description="Reference Genome")
    scrnaseqanalysis = PermissibleValue(
        text="scrnaseqanalysis",
        description="scRNA-seq Analysis")
    speechdata = PermissibleValue(
        text="speechdata",
        description="Speech Data")
    standardsregistry = PermissibleValue(
        text="standardsregistry",
        description="Standards Registry")
    has_ai_application = PermissibleValue(
        text="has_ai_application",
        description="""Has a direct AI application, defined as standards/tools that are: associated with ML or neural networks; schemas, or have schemas; data models; associated with DICOM; associated with AI; associated with standards used within Bridge2AI""")
    standards_process_maturity_final = PermissibleValue(
        text="standards_process_maturity_final",
        description="""This standard has undergone a review process by one or more SDOs and has been determined to be in a mature state. Future revisions may still be possible.""")
    standards_process_maturity_draft = PermissibleValue(
        text="standards_process_maturity_draft",
        description="This standard is undergoing a review process by one or more SDOs to determine its maturity.")
    standards_process_maturity_development = PermissibleValue(
        text="standards_process_maturity_development",
        description="""This standard is in its initial development stages and has not yet entered a review process, or is early in the process and still likely to be extensively revised.""")
    implementation_maturity_production = PermissibleValue(
        text="implementation_maturity_production",
        description="""This standard has one or more implementations appropriate for production use, i.e., in use cases and environments where adherence to the standard is expected to be fully consistent.""")
    implementation_maturity_pilot = PermissibleValue(
        text="implementation_maturity_pilot",
        description="""This standard has one or more implementations intended for testing or evaluation purposes but may not be appropriate for production applications.""")

    _defn = EnumDefinition(
        name="StandardsCollectionTag",
        description="Tags for specific sets of standards.",
    )

class UseCaseCategory(EnumDefinitionImpl):
    """
    Category of use case. These define the high-level purpose of a task or activity as part of a broader research
    effort or other data-related project. They are not mutually exclusive and one use case may involve multiple
    categories.
    """
    acquisition = PermissibleValue(
        text="acquisition",
        description="""Acquisition. The use case involves the collection of data from one or more sources, including data generation, data capture, and data entry.""")
    integration = PermissibleValue(
        text="integration",
        description="""Integration. The use case involves the combination of data from multiple sources, including data harmonization, data linkage, and data aggregation.""")
    standardization = PermissibleValue(
        text="standardization",
        description="""Standardization. The use case involves the application of standards to data, including data normalization, data validation, and quality control.""")
    modeling = PermissibleValue(
        text="modeling",
        description="""Modeling. The use case involves the development of models, including predictive models, statistical models, and machine learning models.""")
    application = PermissibleValue(
        text="application",
        description="""Application. The use case involves the use of data for a specific scientific or otherwise productive purpose, including data analysis, data visualization, and data interpretation. This also includes clinical decision support, patient care, and other applications of data in a biomedical context.""")
    assessment = PermissibleValue(
        text="assessment",
        description="""Assessment. The use case involves the evaluation of data quality, data provenance, and data utility, including the assessment of standards, data tools, and data resources. Note this differs from the standardization category, which involves the application of standards to data.""")

    _defn = EnumDefinition(
        name="UseCaseCategory",
        description="""Category of use case. These define the high-level purpose of a task or activity as part of a broader research effort or other data-related project. They are not mutually exclusive and one use case may involve multiple categories.""",
    )

# Slots
class slots:
    pass

slots.node_property = Slot(uri=B2AI.node_property, name="node_property", curie=B2AI.curie('node_property'),
                   model_uri=DEFAULT_.node_property, domain=NamedThing, range=Optional[str])

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.type = Slot(uri=B2AI.type, name="type", curie=B2AI.curie('type'),
                   model_uri=DEFAULT_.type, domain=NamedThing, range=Optional[str])

slots.category = Slot(uri=B2AI.category, name="category", curie=B2AI.curie('category'),
                   model_uri=DEFAULT_.category, domain=NamedThing, range=Optional[Union[str, CategoryType]])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=DEFAULT_.description, domain=None, range=Optional[str])

slots.edam_id = Slot(uri=B2AI.edam_id, name="edam_id", curie=B2AI.curie('edam_id'),
                   model_uri=DEFAULT_.edam_id, domain=None, range=Optional[Union[str, EdamIdentifier]])

slots.mesh_id = Slot(uri=B2AI.mesh_id, name="mesh_id", curie=B2AI.curie('mesh_id'),
                   model_uri=DEFAULT_.mesh_id, domain=None, range=Optional[Union[str, MeshIdentifier]])

slots.ncit_id = Slot(uri=B2AI.ncit_id, name="ncit_id", curie=B2AI.curie('ncit_id'),
                   model_uri=DEFAULT_.ncit_id, domain=None, range=Optional[Union[str, NcitIdentifier]])

slots.url = Slot(uri=B2AI.url, name="url", curie=B2AI.curie('url'),
                   model_uri=DEFAULT_.url, domain=NamedThing, range=Optional[Union[str, URIorCURIE]])

slots.xref = Slot(uri=B2AI.xref, name="xref", curie=B2AI.curie('xref'),
                   model_uri=DEFAULT_.xref, domain=NamedThing, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.contributor_name = Slot(uri=B2AI.contributor_name, name="contributor_name", curie=B2AI.curie('contributor_name'),
                   model_uri=DEFAULT_.contributor_name, domain=NamedThing, range=Optional[str])

slots.contributor_github_name = Slot(uri=B2AI.contributor_github_name, name="contributor_github_name", curie=B2AI.curie('contributor_github_name'),
                   model_uri=DEFAULT_.contributor_github_name, domain=NamedThing, range=Optional[str])

slots.contributor_orcid = Slot(uri=B2AI.contributor_orcid, name="contributor_orcid", curie=B2AI.curie('contributor_orcid'),
                   model_uri=DEFAULT_.contributor_orcid, domain=NamedThing, range=Optional[Union[str, URIorCURIE]])

slots.contribution_date = Slot(uri=B2AI.contribution_date, name="contribution_date", curie=B2AI.curie('contribution_date'),
                   model_uri=DEFAULT_.contribution_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.related_to = Slot(uri=B2AI.related_to, name="related_to", curie=B2AI.curie('related_to'),
                   model_uri=DEFAULT_.related_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.subclass_of = Slot(uri=B2AI.subclass_of, name="subclass_of", curie=B2AI.curie('subclass_of'),
                   model_uri=DEFAULT_.subclass_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.used_in_bridge2ai = Slot(uri=B2AI.used_in_bridge2ai, name="used_in_bridge2ai", curie=B2AI.curie('used_in_bridge2ai'),
                   model_uri=DEFAULT_.used_in_bridge2ai, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.collection = Slot(uri=B2AI_STANDARD.collection, name="collection", curie=B2AI_STANDARD.curie('collection'),
                   model_uri=DEFAULT_.collection, domain=NamedThing, range=Optional[Union[Union[str, "StandardsCollectionTag"], list[Union[str, "StandardsCollectionTag"]]]])

slots.purpose_detail = Slot(uri=B2AI_STANDARD.purpose_detail, name="purpose_detail", curie=B2AI_STANDARD.curie('purpose_detail'),
                   model_uri=DEFAULT_.purpose_detail, domain=NamedThing, range=Optional[str])

slots.is_open = Slot(uri=B2AI_STANDARD.is_open, name="is_open", curie=B2AI_STANDARD.curie('is_open'),
                   model_uri=DEFAULT_.is_open, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.use_conditions = Slot(uri=B2AI_STANDARD.use_conditions, name="use_conditions", curie=B2AI_STANDARD.curie('use_conditions'),
                   model_uri=DEFAULT_.use_conditions, domain=NamedThing, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.requires_registration = Slot(uri=B2AI_STANDARD.requires_registration, name="requires_registration", curie=B2AI_STANDARD.curie('requires_registration'),
                   model_uri=DEFAULT_.requires_registration, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.concerns_data_topic = Slot(uri=B2AI_STANDARD.concerns_data_topic, name="concerns_data_topic", curie=B2AI_STANDARD.curie('concerns_data_topic'),
                   model_uri=DEFAULT_.concerns_data_topic, domain=DataStandardOrTool, range=Optional[Union[Union[str, DataTopicId], list[Union[str, DataTopicId]]]])

slots.publication = Slot(uri=B2AI_STANDARD.publication, name="publication", curie=B2AI_STANDARD.curie('publication'),
                   model_uri=DEFAULT_.publication, domain=NamedThing, range=Optional[Union[str, URIorCURIE]])

slots.formal_specification = Slot(uri=B2AI_STANDARD.formal_specification, name="formal_specification", curie=B2AI_STANDARD.curie('formal_specification'),
                   model_uri=DEFAULT_.formal_specification, domain=NamedThing, range=Optional[Union[str, URIorCURIE]])

slots.has_relevant_organization = Slot(uri=B2AI_STANDARD.has_relevant_organization, name="has_relevant_organization", curie=B2AI_STANDARD.curie('has_relevant_organization'),
                   model_uri=DEFAULT_.has_relevant_organization, domain=DataStandardOrTool, range=Optional[Union[Union[str, OrganizationId], list[Union[str, OrganizationId]]]])

slots.has_training_resource = Slot(uri=B2AI_STANDARD.has_training_resource, name="has_training_resource", curie=B2AI_STANDARD.curie('has_training_resource'),
                   model_uri=DEFAULT_.has_training_resource, domain=NamedThing, range=Optional[Union[Union[str, DataStandardOrToolId], list[Union[str, DataStandardOrToolId]]]])

slots.data_standardortools_collection = Slot(uri=B2AI_STANDARD.data_standardortools_collection, name="data_standardortools_collection", curie=B2AI_STANDARD.curie('data_standardortools_collection'),
                   model_uri=DEFAULT_.data_standardortools_collection, domain=None, range=Optional[Union[dict[Union[str, DataStandardOrToolId], Union[dict, DataStandardOrTool]], list[Union[dict, DataStandardOrTool]]]])

slots.responsible_organization = Slot(uri=B2AI_STANDARD.responsible_organization, name="responsible_organization", curie=B2AI_STANDARD.curie('responsible_organization'),
                   model_uri=DEFAULT_.responsible_organization, domain=DataStandardOrTool, range=Optional[Union[Union[str, OrganizationId], list[Union[str, OrganizationId]]]])

slots.has_relevant_data_substrate = Slot(uri=B2AI_STANDARD.has_relevant_data_substrate, name="has_relevant_data_substrate", curie=B2AI_STANDARD.curie('has_relevant_data_substrate'),
                   model_uri=DEFAULT_.has_relevant_data_substrate, domain=DataStandardOrTool, range=Optional[Union[Union[str, DataSubstrateId], list[Union[str, DataSubstrateId]]]])

slots.data_collection = Slot(uri=B2AI_DATA.data_collection, name="data_collection", curie=B2AI_DATA.curie('data_collection'),
                   model_uri=DEFAULT_.data_collection, domain=None, range=Optional[Union[dict[Union[str, DataSetId], Union[dict, DataSet]], list[Union[dict, DataSet]]]])

slots.data_url = Slot(uri=B2AI_DATA.data_url, name="data_url", curie=B2AI_DATA.curie('data_url'),
                   model_uri=DEFAULT_.data_url, domain=DataSet, range=Optional[Union[str, URIorCURIE]])

slots.documentation_url = Slot(uri=B2AI_DATA.documentation_url, name="documentation_url", curie=B2AI_DATA.curie('documentation_url'),
                   model_uri=DEFAULT_.documentation_url, domain=DataSet, range=Optional[Union[str, URIorCURIE]])

slots.datasheet_url = Slot(uri=B2AI_DATA.datasheet_url, name="datasheet_url", curie=B2AI_DATA.curie('datasheet_url'),
                   model_uri=DEFAULT_.datasheet_url, domain=DataSet, range=Optional[Union[str, URIorCURIE]])

slots.has_files = Slot(uri=B2AI_DATA.has_files, name="has_files", curie=B2AI_DATA.curie('has_files'),
                   model_uri=DEFAULT_.has_files, domain=DataSet, range=Optional[Union[str, list[str]]])

slots.has_parts = Slot(uri=B2AI_DATA.has_parts, name="has_parts", curie=B2AI_DATA.curie('has_parts'),
                   model_uri=DEFAULT_.has_parts, domain=DataSet, range=Optional[Union[Union[str, DataSetId], list[Union[str, DataSetId]]]])

slots.is_public = Slot(uri=B2AI_DATA.is_public, name="is_public", curie=B2AI_DATA.curie('is_public'),
                   model_uri=DEFAULT_.is_public, domain=DataSet, range=Optional[Union[bool, Bool]])

slots.produced_by = Slot(uri=B2AI_DATA.produced_by, name="produced_by", curie=B2AI_DATA.curie('produced_by'),
                   model_uri=DEFAULT_.produced_by, domain=DataSet, range=Optional[Union[Union[str, OrganizationId], list[Union[str, OrganizationId]]]])

slots.substrates = Slot(uri=B2AI_DATA.substrates, name="substrates", curie=B2AI_DATA.curie('substrates'),
                   model_uri=DEFAULT_.substrates, domain=DataSet, range=Optional[Union[Union[str, DataSubstrateId], list[Union[str, DataSubstrateId]]]])

slots.topics = Slot(uri=B2AI_DATA.topics, name="topics", curie=B2AI_DATA.curie('topics'),
                   model_uri=DEFAULT_.topics, domain=DataSet, range=Optional[Union[Union[str, DataTopicId], list[Union[str, DataTopicId]]]])

slots.is_bridge2ai_data = Slot(uri=B2AI_DATA.is_bridge2ai_data, name="is_bridge2ai_data", curie=B2AI_DATA.curie('is_bridge2ai_data'),
                   model_uri=DEFAULT_.is_bridge2ai_data, domain=DataSet, range=Optional[Union[bool, Bool]])

slots.metadata_storage = Slot(uri=B2AI_SUBSTRATE.metadata_storage, name="metadata_storage", curie=B2AI_SUBSTRATE.curie('metadata_storage'),
                   model_uri=DEFAULT_.metadata_storage, domain=NamedThing, range=Optional[Union[str, list[str]]])

slots.file_extensions = Slot(uri=B2AI_SUBSTRATE.file_extensions, name="file_extensions", curie=B2AI_SUBSTRATE.curie('file_extensions'),
                   model_uri=DEFAULT_.file_extensions, domain=NamedThing, range=Optional[Union[str, list[str]]])

slots.limitations = Slot(uri=B2AI_SUBSTRATE.limitations, name="limitations", curie=B2AI_SUBSTRATE.curie('limitations'),
                   model_uri=DEFAULT_.limitations, domain=NamedThing, range=Optional[Union[str, list[str]]])

slots.data_substrates_collection = Slot(uri=B2AI_SUBSTRATE.data_substrates_collection, name="data_substrates_collection", curie=B2AI_SUBSTRATE.curie('data_substrates_collection'),
                   model_uri=DEFAULT_.data_substrates_collection, domain=None, range=Optional[Union[dict[Union[str, DataSubstrateId], Union[dict, DataSubstrate]], list[Union[dict, DataSubstrate]]]])

slots.data_topics_collection = Slot(uri=B2AI_TOPIC.data_topics_collection, name="data_topics_collection", curie=B2AI_TOPIC.curie('data_topics_collection'),
                   model_uri=DEFAULT_.data_topics_collection, domain=None, range=Optional[Union[dict[Union[str, DataTopicId], Union[dict, DataTopic]], list[Union[dict, DataTopic]]]])

slots.topic_involves_anatomy = Slot(uri=B2AI_TOPIC.topic_involves_anatomy, name="topic_involves_anatomy", curie=B2AI_TOPIC.curie('topic_involves_anatomy'),
                   model_uri=DEFAULT_.topic_involves_anatomy, domain=DataTopic, range=Optional[Union[Union[str, AnatomicalEntityId], list[Union[str, AnatomicalEntityId]]]])

slots.ror_id = Slot(uri=B2AI_ORG.ror_id, name="ror_id", curie=B2AI_ORG.curie('ror_id'),
                   model_uri=DEFAULT_.ror_id, domain=None, range=Optional[Union[str, RorIdentifier]])

slots.wikidata_id = Slot(uri=B2AI_ORG.wikidata_id, name="wikidata_id", curie=B2AI_ORG.curie('wikidata_id'),
                   model_uri=DEFAULT_.wikidata_id, domain=None, range=Optional[Union[str, WikidataIdentifier]])

slots.organizations = Slot(uri=B2AI_ORG.organizations, name="organizations", curie=B2AI_ORG.curie('organizations'),
                   model_uri=DEFAULT_.organizations, domain=None, range=Optional[Union[dict[Union[str, OrganizationId], Union[dict, Organization]], list[Union[dict, Organization]]]])

slots.use_case_category = Slot(uri=B2AI_USECASE.use_case_category, name="use_case_category", curie=B2AI_USECASE.curie('use_case_category'),
                   model_uri=DEFAULT_.use_case_category, domain=NamedThing, range=Optional[Union[Union[str, "UseCaseCategory"], list[Union[str, "UseCaseCategory"]]]])

slots.known_limitations = Slot(uri=B2AI_USECASE.known_limitations, name="known_limitations", curie=B2AI_USECASE.curie('known_limitations'),
                   model_uri=DEFAULT_.known_limitations, domain=NamedThing, range=Optional[str])

slots.relevant_to_gcs = Slot(uri=B2AI_USECASE.relevant_to_gcs, name="relevant_to_gcs", curie=B2AI_USECASE.curie('relevant_to_gcs'),
                   model_uri=DEFAULT_.relevant_to_gcs, domain=None, range=Optional[Union[Union[str, OrganizationId], list[Union[str, OrganizationId]]]])

slots.data_topics = Slot(uri=B2AI_USECASE.data_topics, name="data_topics", curie=B2AI_USECASE.curie('data_topics'),
                   model_uri=DEFAULT_.data_topics, domain=NamedThing, range=Optional[Union[Union[str, DataTopicId], list[Union[str, DataTopicId]]]])

slots.data_substrates = Slot(uri=B2AI_USECASE.data_substrates, name="data_substrates", curie=B2AI_USECASE.curie('data_substrates'),
                   model_uri=DEFAULT_.data_substrates, domain=NamedThing, range=Optional[Union[Union[str, DataSubstrateId], list[Union[str, DataSubstrateId]]]])

slots.standards_and_tools_for_gc_use = Slot(uri=B2AI_USECASE.standards_and_tools_for_gc_use, name="standards_and_tools_for_gc_use", curie=B2AI_USECASE.curie('standards_and_tools_for_gc_use'),
                   model_uri=DEFAULT_.standards_and_tools_for_gc_use, domain=NamedThing, range=Optional[Union[Union[str, DataStandardOrToolId], list[Union[str, DataStandardOrToolId]]]])

slots.alternative_standards_and_tools = Slot(uri=B2AI_USECASE.alternative_standards_and_tools, name="alternative_standards_and_tools", curie=B2AI_USECASE.curie('alternative_standards_and_tools'),
                   model_uri=DEFAULT_.alternative_standards_and_tools, domain=NamedThing, range=Optional[Union[Union[str, DataStandardOrToolId], list[Union[str, DataStandardOrToolId]]]])

slots.enables = Slot(uri=B2AI_USECASE.enables, name="enables", curie=B2AI_USECASE.curie('enables'),
                   model_uri=DEFAULT_.enables, domain=NamedThing, range=Optional[Union[Union[str, UseCaseId], list[Union[str, UseCaseId]]]])

slots.involved_in_experimental_design = Slot(uri=B2AI_USECASE.involved_in_experimental_design, name="involved_in_experimental_design", curie=B2AI_USECASE.curie('involved_in_experimental_design'),
                   model_uri=DEFAULT_.involved_in_experimental_design, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.involved_in_metadata_management = Slot(uri=B2AI_USECASE.involved_in_metadata_management, name="involved_in_metadata_management", curie=B2AI_USECASE.curie('involved_in_metadata_management'),
                   model_uri=DEFAULT_.involved_in_metadata_management, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.involved_in_quality_control = Slot(uri=B2AI_USECASE.involved_in_quality_control, name="involved_in_quality_control", curie=B2AI_USECASE.curie('involved_in_quality_control'),
                   model_uri=DEFAULT_.involved_in_quality_control, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.use_cases = Slot(uri=B2AI_USECASE.use_cases, name="use_cases", curie=B2AI_USECASE.curie('use_cases'),
                   model_uri=DEFAULT_.use_cases, domain=None, range=Optional[Union[dict[Union[str, UseCaseId], Union[dict, UseCase]], list[Union[dict, UseCase]]]])

slots.UseCase_use_case_category = Slot(uri=B2AI_USECASE.use_case_category, name="UseCase_use_case_category", curie=B2AI_USECASE.curie('use_case_category'),
                   model_uri=DEFAULT_.UseCase_use_case_category, domain=UseCase, range=Union[Union[str, "UseCaseCategory"], list[Union[str, "UseCaseCategory"]]])