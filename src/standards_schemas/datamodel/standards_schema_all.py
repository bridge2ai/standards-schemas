# Auto generated from standards_schema_all.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-02-15T19:50:56
# Schema: standards-schema
#
# id: https://w3id.org/bridge2ai/standards-schema
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
STANDARDSDATASTANDARDORTOOL = CurieNamespace('STANDARDSDATASTANDARDORTOOL', 'https://w3id.org/bridge2ai/standards-datastandardortool-schema/')
STANDARDSDATATOPIC = CurieNamespace('STANDARDSDATATOPIC', 'https://w3id.org/bridge2ai/standards-datatopic-schema/')
STANDARDSUSECASE = CurieNamespace('STANDARDSUSECASE', 'https://w3id.org/bridge2ai/standards-usecase-schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/bridge2ai/standards-schema/')


# Types
class EdamIdentifier(Uriorcurie):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "edam identifier"
    type_model_uri = URIRef("https://w3id.org/bridge2ai/standards-schema/EdamIdentifier")


class MeshIdentifier(Uriorcurie):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "mesh identifier"
    type_model_uri = URIRef("https://w3id.org/bridge2ai/standards-schema/MeshIdentifier")


class NcitIdentifier(Uriorcurie):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ncit identifier"
    type_model_uri = URIRef("https://w3id.org/bridge2ai/standards-schema/NcitIdentifier")


class RorIdentifier(Uriorcurie):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ror identifier"
    type_model_uri = URIRef("https://w3id.org/bridge2ai/standards-schema/RorIdentifier")


class WikidataIdentifier(Uriorcurie):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "wikidata identifier"
    type_model_uri = URIRef("https://w3id.org/bridge2ai/standards-schema/WikidataIdentifier")


# Class references
class NamedThingId(URIorCURIE):
    pass


class UseCaseId(NamedThingId):
    pass


class DataTopicId(NamedThingId):
    pass


class DataSubstrateId(NamedThingId):
    pass


class DataStandardOrToolId(NamedThingId):
    pass


class OrganizationId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema/NamedThing")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema/NamedThing")

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class UseCase(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema/UseCase")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "UseCase"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema/UseCase")

    id: Union[str, UseCaseId] = None
    use_case_category: Union[str, "UseCaseCategory"] = None
    alternative_standards_and_tools: Optional[Union[Union[str, DataStandardOrToolId], List[Union[str, DataStandardOrToolId]]]] = empty_list()
    data_substrates: Optional[Union[Union[str, DataSubstrateId], List[Union[str, DataSubstrateId]]]] = empty_list()
    data_topics: Optional[Union[Union[str, DataTopicId], List[Union[str, DataTopicId]]]] = empty_list()
    enables: Optional[Union[Union[str, UseCaseId], List[Union[str, UseCaseId]]]] = empty_list()
    involved_in_experimental_design: Optional[Union[bool, Bool]] = None
    involved_in_metadata_management: Optional[Union[bool, Bool]] = None
    involved_in_quality_control: Optional[Union[bool, Bool]] = None
    known_limitations: Optional[str] = None
    relevance_to_dgps: Optional[Union[Union[str, "DataGeneratingProject"], List[Union[str, "DataGeneratingProject"]]]] = empty_list()
    standards_and_tools_for_dgp_use: Optional[Union[Union[str, DataStandardOrToolId], List[Union[str, DataStandardOrToolId]]]] = empty_list()
    xref: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UseCaseId):
            self.id = UseCaseId(self.id)

        if self._is_empty(self.use_case_category):
            self.MissingRequiredField("use_case_category")
        if not isinstance(self.use_case_category, UseCaseCategory):
            self.use_case_category = UseCaseCategory(self.use_case_category)

        if not isinstance(self.alternative_standards_and_tools, list):
            self.alternative_standards_and_tools = [self.alternative_standards_and_tools] if self.alternative_standards_and_tools is not None else []
        self.alternative_standards_and_tools = [v if isinstance(v, DataStandardOrToolId) else DataStandardOrToolId(v) for v in self.alternative_standards_and_tools]

        if not isinstance(self.data_substrates, list):
            self.data_substrates = [self.data_substrates] if self.data_substrates is not None else []
        self.data_substrates = [v if isinstance(v, DataSubstrateId) else DataSubstrateId(v) for v in self.data_substrates]

        if not isinstance(self.data_topics, list):
            self.data_topics = [self.data_topics] if self.data_topics is not None else []
        self.data_topics = [v if isinstance(v, DataTopicId) else DataTopicId(v) for v in self.data_topics]

        if not isinstance(self.enables, list):
            self.enables = [self.enables] if self.enables is not None else []
        self.enables = [v if isinstance(v, UseCaseId) else UseCaseId(v) for v in self.enables]

        if self.involved_in_experimental_design is not None and not isinstance(self.involved_in_experimental_design, Bool):
            self.involved_in_experimental_design = Bool(self.involved_in_experimental_design)

        if self.involved_in_metadata_management is not None and not isinstance(self.involved_in_metadata_management, Bool):
            self.involved_in_metadata_management = Bool(self.involved_in_metadata_management)

        if self.involved_in_quality_control is not None and not isinstance(self.involved_in_quality_control, Bool):
            self.involved_in_quality_control = Bool(self.involved_in_quality_control)

        if self.known_limitations is not None and not isinstance(self.known_limitations, str):
            self.known_limitations = str(self.known_limitations)

        if not isinstance(self.relevance_to_dgps, list):
            self.relevance_to_dgps = [self.relevance_to_dgps] if self.relevance_to_dgps is not None else []
        self.relevance_to_dgps = [v if isinstance(v, DataGeneratingProject) else DataGeneratingProject(v) for v in self.relevance_to_dgps]

        if not isinstance(self.standards_and_tools_for_dgp_use, list):
            self.standards_and_tools_for_dgp_use = [self.standards_and_tools_for_dgp_use] if self.standards_and_tools_for_dgp_use is not None else []
        self.standards_and_tools_for_dgp_use = [v if isinstance(v, DataStandardOrToolId) else DataStandardOrToolId(v) for v in self.standards_and_tools_for_dgp_use]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, str) else str(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class UseCaseContainer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema/UseCaseContainer")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "UseCaseContainer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema/UseCaseContainer")

    container_name: Optional[str] = None
    use_cases: Optional[Union[Dict[Union[str, UseCaseId], Union[dict, UseCase]], List[Union[dict, UseCase]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.container_name is not None and not isinstance(self.container_name, str):
            self.container_name = str(self.container_name)

        self._normalize_inlined_as_dict(slot_name="use_cases", slot_type=UseCase, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class DataTopic(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema/DataTopic")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DataTopic"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema/DataTopic")

    id: Union[str, DataTopicId] = None
    EDAM_ID: Optional[Union[str, EdamIdentifier]] = None
    MeSH_ID: Optional[Union[str, MeshIdentifier]] = None
    NCIT_ID: Optional[Union[str, NcitIdentifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataTopicId):
            self.id = DataTopicId(self.id)

        if self.EDAM_ID is not None and not isinstance(self.EDAM_ID, EdamIdentifier):
            self.EDAM_ID = EdamIdentifier(self.EDAM_ID)

        if self.MeSH_ID is not None and not isinstance(self.MeSH_ID, MeshIdentifier):
            self.MeSH_ID = MeshIdentifier(self.MeSH_ID)

        if self.NCIT_ID is not None and not isinstance(self.NCIT_ID, NcitIdentifier):
            self.NCIT_ID = NcitIdentifier(self.NCIT_ID)

        super().__post_init__(**kwargs)


@dataclass
class DataSubstrate(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema/DataSubstrate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DataSubstrate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema/DataSubstrate")

    id: Union[str, DataSubstrateId] = None
    EDAM_ID: Optional[Union[str, EdamIdentifier]] = None
    MeSH_ID: Optional[Union[str, MeshIdentifier]] = None
    NCIT_ID: Optional[Union[str, NcitIdentifier]] = None
    metadata_storage: Optional[Union[str, List[str]]] = empty_list()
    file_extensions: Optional[Union[str, List[str]]] = empty_list()
    limitations: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSubstrateId):
            self.id = DataSubstrateId(self.id)

        if self.EDAM_ID is not None and not isinstance(self.EDAM_ID, EdamIdentifier):
            self.EDAM_ID = EdamIdentifier(self.EDAM_ID)

        if self.MeSH_ID is not None and not isinstance(self.MeSH_ID, MeshIdentifier):
            self.MeSH_ID = MeshIdentifier(self.MeSH_ID)

        if self.NCIT_ID is not None and not isinstance(self.NCIT_ID, NcitIdentifier):
            self.NCIT_ID = NcitIdentifier(self.NCIT_ID)

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


@dataclass
class DataStandardOrTool(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["concerns_data_topic", "has_relevant_organization"]

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema/DataStandardOrTool")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DataStandardOrTool"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema/DataStandardOrTool")

    id: Union[str, DataStandardOrToolId] = None
    collection: Optional[Union[Union[str, "StandardsCollectionTag"], List[Union[str, "StandardsCollectionTag"]]]] = empty_list()
    concerns_data_topic: Optional[Union[Union[str, DataTopicId], List[Union[str, DataTopicId]]]] = empty_list()
    has_relevant_organization: Optional[Union[Union[str, OrganizationId], List[Union[str, OrganizationId]]]] = empty_list()
    purpose_detail: Optional[str] = None
    is_open: Optional[Union[bool, Bool]] = None
    requires_registration: Optional[Union[bool, Bool]] = None
    url: Optional[Union[str, URIorCURIE]] = None
    publication: Optional[Union[str, URIorCURIE]] = None
    formal_specification: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        super().__post_init__(**kwargs)


@dataclass
class Organization(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["related_to"]

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema/Organization")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/bridge2ai/standards-schema/Organization")

    id: Union[str, OrganizationId] = None
    ROR_ID: Optional[Union[str, RorIdentifier]] = None
    Wikidata_ID: Optional[Union[str, WikidataIdentifier]] = None
    URL: Optional[str] = None
    related_to: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        if self.ROR_ID is not None and not isinstance(self.ROR_ID, RorIdentifier):
            self.ROR_ID = RorIdentifier(self.ROR_ID)

        if self.Wikidata_ID is not None and not isinstance(self.Wikidata_ID, WikidataIdentifier):
            self.Wikidata_ID = WikidataIdentifier(self.Wikidata_ID)

        if self.URL is not None and not isinstance(self.URL, str):
            self.URL = str(self.URL)

        if not isinstance(self.related_to, list):
            self.related_to = [self.related_to] if self.related_to is not None else []
        self.related_to = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.related_to]

        super().__post_init__(**kwargs)


# Enumerations
class UseCaseCategory(EnumDefinitionImpl):

    acquisition = PermissibleValue(text="acquisition")
    integration = PermissibleValue(text="integration")
    standardization = PermissibleValue(text="standardization")
    modeling = PermissibleValue(text="modeling")
    application = PermissibleValue(text="application")
    assessment = PermissibleValue(text="assessment")

    _defn = EnumDefinition(
        name="UseCaseCategory",
    )

class DataGeneratingProject(EnumDefinitionImpl):

    aireadi = PermissibleValue(text="aireadi")
    chorus = PermissibleValue(text="chorus",
                                   meaning=None)
    cm4ai = PermissibleValue(text="cm4ai",
                                 meaning=None)
    voice = PermissibleValue(text="voice",
                                 meaning=None)

    _defn = EnumDefinition(
        name="DataGeneratingProject",
    )

class StandardsCollectionTag(EnumDefinitionImpl):

    audiovisual = PermissibleValue(text="audiovisual")
    deprecated = PermissibleValue(text="deprecated")
    fileformat = PermissibleValue(text="fileformat")
    toolkit = PermissibleValue(text="toolkit")
    clinicaldata = PermissibleValue(text="clinicaldata")
    multimodal = PermissibleValue(text="multimodal")
    text = PermissibleValue(text="text")
    cloudplatform = PermissibleValue(text="cloudplatform")
    cloudservice = PermissibleValue(text="cloudservice")
    codesystem = PermissibleValue(text="codesystem")
    datamodel = PermissibleValue(text="datamodel")
    dataregistry = PermissibleValue(text="dataregistry")
    softwareregistry = PermissibleValue(text="softwareregistry")
    datavisualization = PermissibleValue(text="datavisualization")
    notebookplatform = PermissibleValue(text="notebookplatform")
    datasheets = PermissibleValue(text="datasheets")
    machinelearningframework = PermissibleValue(text="machinelearningframework")
    workflowlanguage = PermissibleValue(text="workflowlanguage")
    diagnosticinstrument = PermissibleValue(text="diagnosticinstrument")
    drugdata = PermissibleValue(text="drugdata")
    eyedata = PermissibleValue(text="eyedata")
    markuplanguage = PermissibleValue(text="markuplanguage")
    graphdataplatform = PermissibleValue(text="graphdataplatform")
    guidelines = PermissibleValue(text="guidelines")
    minimuminformationschema = PermissibleValue(text="minimuminformationschema")
    modelcards = PermissibleValue(text="modelcards")
    obofoundry = PermissibleValue(text="obofoundry")
    ontologyregistry = PermissibleValue(text="ontologyregistry")
    policy = PermissibleValue(text="policy")
    proteindata = PermissibleValue(text="proteindata")
    referencegenome = PermissibleValue(text="referencegenome")
    scrnaseqanalysis = PermissibleValue(text="scrnaseqanalysis")
    speechdata = PermissibleValue(text="speechdata")
    standardsregistry = PermissibleValue(text="standardsregistry")

    _defn = EnumDefinition(
        name="StandardsCollectionTag",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=DEFAULT_.description, domain=None, range=Optional[str])

slots.xref = Slot(uri=DEFAULT_.xref, name="xref", curie=DEFAULT_.curie('xref'),
                   model_uri=DEFAULT_.xref, domain=None, range=Optional[Union[str, List[str]]])

slots.use_case_category = Slot(uri=DEFAULT_.use_case_category, name="use_case_category", curie=DEFAULT_.curie('use_case_category'),
                   model_uri=DEFAULT_.use_case_category, domain=NamedThing, range=Optional[Union[str, "UseCaseCategory"]])

slots.known_limitations = Slot(uri=DEFAULT_.known_limitations, name="known_limitations", curie=DEFAULT_.curie('known_limitations'),
                   model_uri=DEFAULT_.known_limitations, domain=NamedThing, range=Optional[str])

slots.relevance_to_dgps = Slot(uri=DEFAULT_.relevance_to_dgps, name="relevance_to_dgps", curie=DEFAULT_.curie('relevance_to_dgps'),
                   model_uri=DEFAULT_.relevance_to_dgps, domain=None, range=Optional[Union[Union[str, "DataGeneratingProject"], List[Union[str, "DataGeneratingProject"]]]])

slots.data_topics = Slot(uri=DEFAULT_.data_topics, name="data_topics", curie=DEFAULT_.curie('data_topics'),
                   model_uri=DEFAULT_.data_topics, domain=NamedThing, range=Optional[Union[Union[str, DataTopicId], List[Union[str, DataTopicId]]]])

slots.data_substrates = Slot(uri=DEFAULT_.data_substrates, name="data_substrates", curie=DEFAULT_.curie('data_substrates'),
                   model_uri=DEFAULT_.data_substrates, domain=NamedThing, range=Optional[Union[Union[str, DataSubstrateId], List[Union[str, DataSubstrateId]]]])

slots.standards_and_tools_for_dgp_use = Slot(uri=DEFAULT_.standards_and_tools_for_dgp_use, name="standards_and_tools_for_dgp_use", curie=DEFAULT_.curie('standards_and_tools_for_dgp_use'),
                   model_uri=DEFAULT_.standards_and_tools_for_dgp_use, domain=NamedThing, range=Optional[Union[Union[str, DataStandardOrToolId], List[Union[str, DataStandardOrToolId]]]])

slots.alternative_standards_and_tools = Slot(uri=DEFAULT_.alternative_standards_and_tools, name="alternative_standards_and_tools", curie=DEFAULT_.curie('alternative_standards_and_tools'),
                   model_uri=DEFAULT_.alternative_standards_and_tools, domain=NamedThing, range=Optional[Union[Union[str, DataStandardOrToolId], List[Union[str, DataStandardOrToolId]]]])

slots.enables = Slot(uri=DEFAULT_.enables, name="enables", curie=DEFAULT_.curie('enables'),
                   model_uri=DEFAULT_.enables, domain=NamedThing, range=Optional[Union[Union[str, UseCaseId], List[Union[str, UseCaseId]]]])

slots.involved_in_experimental_design = Slot(uri=DEFAULT_.involved_in_experimental_design, name="involved_in_experimental_design", curie=DEFAULT_.curie('involved_in_experimental_design'),
                   model_uri=DEFAULT_.involved_in_experimental_design, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.involved_in_metadata_management = Slot(uri=DEFAULT_.involved_in_metadata_management, name="involved_in_metadata_management", curie=DEFAULT_.curie('involved_in_metadata_management'),
                   model_uri=DEFAULT_.involved_in_metadata_management, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.involved_in_quality_control = Slot(uri=DEFAULT_.involved_in_quality_control, name="involved_in_quality_control", curie=DEFAULT_.curie('involved_in_quality_control'),
                   model_uri=DEFAULT_.involved_in_quality_control, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.EDAM_ID = Slot(uri=DEFAULT_.EDAM_ID, name="EDAM_ID", curie=DEFAULT_.curie('EDAM_ID'),
                   model_uri=DEFAULT_.EDAM_ID, domain=None, range=Optional[Union[str, EdamIdentifier]])

slots.MeSH_ID = Slot(uri=DEFAULT_.MeSH_ID, name="MeSH_ID", curie=DEFAULT_.curie('MeSH_ID'),
                   model_uri=DEFAULT_.MeSH_ID, domain=None, range=Optional[Union[str, MeshIdentifier]])

slots.NCIT_ID = Slot(uri=DEFAULT_.NCIT_ID, name="NCIT_ID", curie=DEFAULT_.curie('NCIT_ID'),
                   model_uri=DEFAULT_.NCIT_ID, domain=None, range=Optional[Union[str, NcitIdentifier]])

slots.metadata_storage = Slot(uri=DEFAULT_.metadata_storage, name="metadata_storage", curie=DEFAULT_.curie('metadata_storage'),
                   model_uri=DEFAULT_.metadata_storage, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.file_extensions = Slot(uri=DEFAULT_.file_extensions, name="file_extensions", curie=DEFAULT_.curie('file_extensions'),
                   model_uri=DEFAULT_.file_extensions, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.limitations = Slot(uri=DEFAULT_.limitations, name="limitations", curie=DEFAULT_.curie('limitations'),
                   model_uri=DEFAULT_.limitations, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.collection = Slot(uri=DEFAULT_.collection, name="collection", curie=DEFAULT_.curie('collection'),
                   model_uri=DEFAULT_.collection, domain=NamedThing, range=Optional[Union[Union[str, "StandardsCollectionTag"], List[Union[str, "StandardsCollectionTag"]]]])

slots.concerns_data_topic = Slot(uri=DEFAULT_.concerns_data_topic, name="concerns_data_topic", curie=DEFAULT_.curie('concerns_data_topic'),
                   model_uri=DEFAULT_.concerns_data_topic, domain=DataStandardOrTool, range=Optional[Union[Union[str, DataTopicId], List[Union[str, DataTopicId]]]])

slots.has_relevant_organization = Slot(uri=DEFAULT_.has_relevant_organization, name="has_relevant_organization", curie=DEFAULT_.curie('has_relevant_organization'),
                   model_uri=DEFAULT_.has_relevant_organization, domain=DataStandardOrTool, range=Optional[Union[Union[str, OrganizationId], List[Union[str, OrganizationId]]]])

slots.purpose_detail = Slot(uri=DEFAULT_.purpose_detail, name="purpose_detail", curie=DEFAULT_.curie('purpose_detail'),
                   model_uri=DEFAULT_.purpose_detail, domain=NamedThing, range=Optional[str])

slots.is_open = Slot(uri=DEFAULT_.is_open, name="is_open", curie=DEFAULT_.curie('is_open'),
                   model_uri=DEFAULT_.is_open, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.requires_registration = Slot(uri=DEFAULT_.requires_registration, name="requires_registration", curie=DEFAULT_.curie('requires_registration'),
                   model_uri=DEFAULT_.requires_registration, domain=NamedThing, range=Optional[Union[bool, Bool]])

slots.url = Slot(uri=DEFAULT_.url, name="url", curie=DEFAULT_.curie('url'),
                   model_uri=DEFAULT_.url, domain=NamedThing, range=Optional[Union[str, URIorCURIE]])

slots.URL = Slot(uri=DEFAULT_.URL, name="URL", curie=DEFAULT_.curie('URL'),
                   model_uri=DEFAULT_.URL, domain=None, range=Optional[str])

slots.publication = Slot(uri=DEFAULT_.publication, name="publication", curie=DEFAULT_.curie('publication'),
                   model_uri=DEFAULT_.publication, domain=NamedThing, range=Optional[Union[str, URIorCURIE]])

slots.formal_specification = Slot(uri=DEFAULT_.formal_specification, name="formal_specification", curie=DEFAULT_.curie('formal_specification'),
                   model_uri=DEFAULT_.formal_specification, domain=NamedThing, range=Optional[Union[str, URIorCURIE]])

slots.ROR_ID = Slot(uri=DEFAULT_.ROR_ID, name="ROR_ID", curie=DEFAULT_.curie('ROR_ID'),
                   model_uri=DEFAULT_.ROR_ID, domain=None, range=Optional[Union[str, RorIdentifier]])

slots.Wikidata_ID = Slot(uri=DEFAULT_.Wikidata_ID, name="Wikidata_ID", curie=DEFAULT_.curie('Wikidata_ID'),
                   model_uri=DEFAULT_.Wikidata_ID, domain=None, range=Optional[Union[str, WikidataIdentifier]])

slots.related_to = Slot(uri=DEFAULT_.related_to, name="related_to", curie=DEFAULT_.curie('related_to'),
                   model_uri=DEFAULT_.related_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.node_property = Slot(uri=DEFAULT_.node_property, name="node property", curie=DEFAULT_.curie('node_property'),
                   model_uri=DEFAULT_.node_property, domain=NamedThing, range=Optional[str])

slots.container_name = Slot(uri=DEFAULT_.container_name, name="container_name", curie=DEFAULT_.curie('container_name'),
                   model_uri=DEFAULT_.container_name, domain=None, range=Optional[str])

slots.use_cases = Slot(uri=DEFAULT_.use_cases, name="use_cases", curie=DEFAULT_.curie('use_cases'),
                   model_uri=DEFAULT_.use_cases, domain=None, range=Optional[Union[Dict[Union[str, UseCaseId], Union[dict, UseCase]], List[Union[dict, UseCase]]]])

slots.UseCase_use_case_category = Slot(uri=DEFAULT_.use_case_category, name="UseCase_use_case_category", curie=DEFAULT_.curie('use_case_category'),
                   model_uri=DEFAULT_.UseCase_use_case_category, domain=UseCase, range=Union[str, "UseCaseCategory"])