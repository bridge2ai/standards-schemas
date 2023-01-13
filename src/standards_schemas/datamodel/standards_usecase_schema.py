# Auto generated from standards_usecase_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-01-13T11:57:29
# Schema: standards-usecase-schema
#
# id: https://w3id.org/bridge2ai/standards-usecase-schema
# description: Data schema for Bridge2AI Standards Use Cases.
# license: MIT

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
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
STANDARDSUSECASE = CurieNamespace('STANDARDSUSECASE', 'https://w3id.org/bridge2ai/standards-usecase-schema/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = STANDARDSUSECASE


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class UseCaseId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = STANDARDSUSECASE.NamedThing

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
    """
    Represents a use case for Bridge2AI standards.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = STANDARDSUSECASE.UseCase
    class_class_curie: ClassVar[str] = "STANDARDSUSECASE:UseCase"
    class_name: ClassVar[str] = "UseCase"
    class_model_uri: ClassVar[URIRef] = STANDARDSUSECASE.UseCase

    id: Union[str, UseCaseId] = None
    use_case_category: Optional[Union[str, "UseCaseCategory"]] = None
    known_limitations: Optional[str] = None
    relevance_to_dgps: Optional[Union[str, "DataGeneratingProject"]] = None
    data_types: Optional[str] = None
    data_substrates: Optional[str] = None
    standards_and_tools_for_dgp_use: Optional[str] = None
    alternative_standards_and_tools: Optional[str] = None
    enables: Optional[str] = None
    involved_in_experimental_design: Optional[str] = None
    involved_in_metadata_management: Optional[str] = None
    involved_in_quality_control: Optional[str] = None
    xrefs: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UseCaseId):
            self.id = UseCaseId(self.id)

        if self.use_case_category is not None and not isinstance(self.use_case_category, UseCaseCategory):
            self.use_case_category = UseCaseCategory(self.use_case_category)

        if self.known_limitations is not None and not isinstance(self.known_limitations, str):
            self.known_limitations = str(self.known_limitations)

        if self.relevance_to_dgps is not None and not isinstance(self.relevance_to_dgps, DataGeneratingProject):
            self.relevance_to_dgps = DataGeneratingProject(self.relevance_to_dgps)

        if self.data_types is not None and not isinstance(self.data_types, str):
            self.data_types = str(self.data_types)

        if self.data_substrates is not None and not isinstance(self.data_substrates, str):
            self.data_substrates = str(self.data_substrates)

        if self.standards_and_tools_for_dgp_use is not None and not isinstance(self.standards_and_tools_for_dgp_use, str):
            self.standards_and_tools_for_dgp_use = str(self.standards_and_tools_for_dgp_use)

        if self.alternative_standards_and_tools is not None and not isinstance(self.alternative_standards_and_tools, str):
            self.alternative_standards_and_tools = str(self.alternative_standards_and_tools)

        if self.enables is not None and not isinstance(self.enables, str):
            self.enables = str(self.enables)

        if self.involved_in_experimental_design is not None and not isinstance(self.involved_in_experimental_design, str):
            self.involved_in_experimental_design = str(self.involved_in_experimental_design)

        if self.involved_in_metadata_management is not None and not isinstance(self.involved_in_metadata_management, str):
            self.involved_in_metadata_management = str(self.involved_in_metadata_management)

        if self.involved_in_quality_control is not None and not isinstance(self.involved_in_quality_control, str):
            self.involved_in_quality_control = str(self.involved_in_quality_control)

        if self.xrefs is not None and not isinstance(self.xrefs, str):
            self.xrefs = str(self.xrefs)

        super().__post_init__(**kwargs)


@dataclass
class UseCaseCollection(YAMLRoot):
    """
    A holder for UseCase objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = STANDARDSUSECASE.UseCaseCollection
    class_class_curie: ClassVar[str] = "STANDARDSUSECASE:UseCaseCollection"
    class_name: ClassVar[str] = "UseCaseCollection"
    class_model_uri: ClassVar[URIRef] = STANDARDSUSECASE.UseCaseCollection

    entries: Optional[Union[Dict[Union[str, UseCaseId], Union[dict, UseCase]], List[Union[dict, UseCase]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=UseCase, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class UseCaseCategory(EnumDefinitionImpl):

    Acquisition = PermissibleValue(text="Acquisition",
                                             description="Acquisition")
    Integration = PermissibleValue(text="Integration",
                                             description="Integration")
    Standardization = PermissibleValue(text="Standardization",
                                                     description="Standardization")
    Modeling = PermissibleValue(text="Modeling",
                                       description="Modeling")
    Application = PermissibleValue(text="Application",
                                             description="Application")
    Assessment = PermissibleValue(text="Assessment",
                                           description="Assessment")

    _defn = EnumDefinition(
        name="UseCaseCategory",
    )

class DataGeneratingProject(EnumDefinitionImpl):

    CHoRUS = PermissibleValue(text="CHoRUS",
                                   description="CHoRUS: Collaborative Hospital Repository Uniting Standards. Using imaging, clinical, and other data collected in an ICU setting for diagnosis and risk prediction.")
    CM4AI = PermissibleValue(text="CM4AI",
                                 description="CM4AI: Cell Maps for AI. Mapping spatiotemporal architecture of human cells to interpret cell structure/function in health and disease.")
    Voice = PermissibleValue(text="Voice",
                                 description="Voice as a Biomarker of Health: Building an ethically sourced, bioaccoustic database to understand disease like never before.")

    _defn = EnumDefinition(
        name="DataGeneratingProject",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "AI-READI",
                PermissibleValue(text="AI-READI",
                                 description="AI-READI: Uncovering the details of how human health is restored after disease, using type 2 diabetes as a model.") )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=STANDARDSUSECASE.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=STANDARDSUSECASE.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=STANDARDSUSECASE.description, domain=None, range=Optional[str])

slots.use_case_category = Slot(uri=STANDARDSUSECASE.use_case_category, name="use_case_category", curie=STANDARDSUSECASE.curie('use_case_category'),
                   model_uri=STANDARDSUSECASE.use_case_category, domain=None, range=Optional[Union[str, "UseCaseCategory"]])

slots.known_limitations = Slot(uri=STANDARDSUSECASE.known_limitations, name="known_limitations", curie=STANDARDSUSECASE.curie('known_limitations'),
                   model_uri=STANDARDSUSECASE.known_limitations, domain=None, range=Optional[str])

slots.relevance_to_dgps = Slot(uri=STANDARDSUSECASE.relevance_to_dgps, name="relevance_to_dgps", curie=STANDARDSUSECASE.curie('relevance_to_dgps'),
                   model_uri=STANDARDSUSECASE.relevance_to_dgps, domain=None, range=Optional[Union[str, "DataGeneratingProject"]])

slots.data_types = Slot(uri=STANDARDSUSECASE.data_types, name="data_types", curie=STANDARDSUSECASE.curie('data_types'),
                   model_uri=STANDARDSUSECASE.data_types, domain=None, range=Optional[str])

slots.data_substrates = Slot(uri=STANDARDSUSECASE.data_substrates, name="data_substrates", curie=STANDARDSUSECASE.curie('data_substrates'),
                   model_uri=STANDARDSUSECASE.data_substrates, domain=None, range=Optional[str])

slots.standards_and_tools_for_dgp_use = Slot(uri=STANDARDSUSECASE.standards_and_tools_for_dgp_use, name="standards_and_tools_for_dgp_use", curie=STANDARDSUSECASE.curie('standards_and_tools_for_dgp_use'),
                   model_uri=STANDARDSUSECASE.standards_and_tools_for_dgp_use, domain=None, range=Optional[str])

slots.alternative_standards_and_tools = Slot(uri=STANDARDSUSECASE.alternative_standards_and_tools, name="alternative_standards_and_tools", curie=STANDARDSUSECASE.curie('alternative_standards_and_tools'),
                   model_uri=STANDARDSUSECASE.alternative_standards_and_tools, domain=None, range=Optional[str])

slots.enables = Slot(uri=STANDARDSUSECASE.enables, name="enables", curie=STANDARDSUSECASE.curie('enables'),
                   model_uri=STANDARDSUSECASE.enables, domain=None, range=Optional[str])

slots.involved_in_experimental_design = Slot(uri=STANDARDSUSECASE.involved_in_experimental_design, name="involved_in_experimental_design", curie=STANDARDSUSECASE.curie('involved_in_experimental_design'),
                   model_uri=STANDARDSUSECASE.involved_in_experimental_design, domain=None, range=Optional[str])

slots.involved_in_metadata_management = Slot(uri=STANDARDSUSECASE.involved_in_metadata_management, name="involved_in_metadata_management", curie=STANDARDSUSECASE.curie('involved_in_metadata_management'),
                   model_uri=STANDARDSUSECASE.involved_in_metadata_management, domain=None, range=Optional[str])

slots.involved_in_quality_control = Slot(uri=STANDARDSUSECASE.involved_in_quality_control, name="involved_in_quality_control", curie=STANDARDSUSECASE.curie('involved_in_quality_control'),
                   model_uri=STANDARDSUSECASE.involved_in_quality_control, domain=None, range=Optional[str])

slots.xrefs = Slot(uri=STANDARDSUSECASE.xrefs, name="xrefs", curie=STANDARDSUSECASE.curie('xrefs'),
                   model_uri=STANDARDSUSECASE.xrefs, domain=None, range=Optional[str])

slots.useCaseCollection__entries = Slot(uri=STANDARDSUSECASE.entries, name="useCaseCollection__entries", curie=STANDARDSUSECASE.curie('entries'),
                   model_uri=STANDARDSUSECASE.useCaseCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, UseCaseId], Union[dict, UseCase]], List[Union[dict, UseCase]]]])