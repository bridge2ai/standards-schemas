## DataTopic-minimal-1
### Input
```yaml
category: B2AI_TOPIC:DataTopic
description: A minimal but valid data topic example that conforms to the schema
id: B2AI_TOPIC:2
name: Minimal DataTopic Example

```
## DataSubstrate-valid-1
### Input
```yaml
category: B2AI_SUBSTRATE:DataSubstrate
contribution_date: '2023-02-02'
contributor_name: Kiran Neelam
contributor_orcid: ORCID:0000-0001-1276-5602
description: BED (Browser Extensible Data) format provides a flexible way to define
  the data lines that are displayed in a genome annotation track.
edam_id: edam.format:3003
id: B2AI_SUBSTRATE:53
metadata_storage:
- file headers
name: BED
ncit_id: ncit:C153367
subclass_of:
- B2AI_SUBSTRATE:1

```
## BiomedicalStandard-OMOP-valid-1
### Input
```yaml
category: B2AI_STANDARD:BiomedicalStandard
collection:
- datamodel
- clinicaldata
concerns_data_topic:
- B2AI_TOPIC:4
- B2AI_TOPIC:5
- B2AI_TOPIC:29
contribution_date: '2024-12-20'
contributor_name: Harry Caufield
contributor_orcid: ORCID:0000-0001-5705-7831
description: The Observational Medical Outcomes Partnership (OMOP) Common Data Model
  (CDM) is a standardized data model that enables systematic analysis of disparate
  observational databases. The CDM provides a common format and content, as well as
  standard vocabularies to encode healthcare data from diverse sources. It is designed
  to standardize the structure and content of observational data to enable efficient
  analyses that can produce reliable evidence.
formal_specification: https://ohdsi.github.io/CommonDataModel/
has_application:
- category: B2AI:Application
  datasheet:
  - https://example.org/omop-trajectory-datasheet
  description: Deep learning model that analyzes patient timelines in OMOP CDM format
    to predict disease progression and treatment outcomes across multiple conditions.
  id: B2AI_APP:210
  name: OMOP-based Patient Trajectory Prediction
  references:
  - https://doi.org/10.1093/jamia/example-omop
has_relevant_organization:
- B2AI_ORG:75
id: B2AI_STANDARD:243
is_open: true
name: OMOP Common Data Model
publication: https://doi.org/10.1093/jamia/ocv153
purpose_detail: OMOP CDM is designed to standardize observational health data from
  electronic health records, administrative claims, and disease registries, enabling
  large-scale analytics and machine learning across diverse healthcare datasets.
requires_registration: false
responsible_organization:
- B2AI_ORG:75
url: https://www.ohdsi.org/data-standardization/the-common-data-model/

```
## Application-minimal-1
### Input
```yaml
category: B2AI:Application
description: A minimal but valid application example that conforms to the schema
id: B2AI_APP:1
name: Minimal Application Example

```
## OrganizationContainer-minimal-1
### Input
```yaml
organizations:
- category: B2AI_ORG:Organization
  description: A minimal but valid organization container example that conforms to
    the schema
  id: B2AI_ORG:container1
  name: Minimal OrganizationContainer Example

```
## UseCaseContainer-minimal-1
### Input
```yaml
use_cases:
- category: B2AI_USECASE:UseCase
  description: A minimal but valid use case container example that conforms to the
    schema
  id: B2AI_USECASE:container1
  name: Minimal UseCaseContainer Example
  use_case_category:
  - acquisition

```
## OntologyOrVocabulary-SNOMEDCT-valid-1
### Input
```yaml
category: B2AI_STANDARD:OntologyOrVocabulary
collection:
- obofoundry
- clinicaldata
concerns_data_topic:
- B2AI_TOPIC:4
- B2AI_TOPIC:5
contribution_date: '2024-12-20'
contributor_name: Harry Caufield
contributor_orcid: ORCID:0000-0001-5705-7831
description: SNOMED CT (Systematized Nomenclature of Medicine -- Clinical Terms) is
  a comprehensive clinical terminology that provides a standardized way to represent
  clinical information across the entire healthcare spectrum. It contains more than
  350,000 active concepts with unique meanings organized into hierarchies, enabling
  semantic interoperability between healthcare systems and supporting clinical documentation,
  decision support, and analytics.
formal_specification: https://confluence.ihtsdotools.org/display/DOCSTART
has_relevant_organization:
- B2AI_ORG:130
id: B2AI_STANDARD:180
is_open: false
name: SNOMED CT
publication: https://doi.org/10.1093/jamia/ocu011
purpose_detail: SNOMED CT serves as a clinical reference terminology enabling consistent
  representation and sharing of clinical data across systems, supporting clinical
  care delivery, research, and health information exchange worldwide.
requires_registration: true
responsible_organization:
- B2AI_ORG:130
url: https://www.snomed.org/

```
## DataSet-valid-1
### Input
```yaml
category: B2AI_DATA:DataSet
contribution_date: '2024-03-05'
contributor_name: "Verena Ead\xE1n"
contributor_orcid: ORCID:0000-0005-1292-5161
data_url: https://example.com/data
datasheet_url: https://example.com/datasheet
description: This dataset is the June 2024 (v2) release of data for the Artificial
  Intelligence in Cell Phenotypes project. It includes data on cell phenotypes and
  their relationships to various biological processes.
documentation_url: https://example.com/docs
has_files:
- some_top_level_file.csv
has_parts:
- B2AI_TOPIC:4
id: B2AI_DATA:3
is_public: true
name: Artificial Intelligence in Cell Phenotypes - June 2024 Release
produced_by:
- B2AI_ORG:1
substrates:
- B2AI_SUBSTRATE:1
topics:
- B2AI_TOPIC:4

```
## DataSetContainer-valid-1
### Input
```yaml
data_collection:
- category: B2AI_DATA:DataSet
  description: A valid data set example that conforms to the schema
  id: B2AI_DATA:1
  name: Valid DataSet Example

```
## Application-valid-1
### Input
```yaml
category: B2AI:Application
contribution_date: '2024-11-15'
contributor_github_name: erodriguez
contributor_name: Elena Rodriguez
contributor_orcid: ORCID:0000-0002-3456-7890
datasheet:
- https://example.com/datasheets/sepsis-ai-model-card.pdf
- https://example.com/datasheets/sepsis-ai-datasheet.pdf
description: An artificial intelligence application that uses machine learning models
  to predict early onset of sepsis in hospitalized patients. The system integrates
  electronic health record data standardized using FHIR (Fast Healthcare Interoperability
  Resources) to enable real-time risk assessment and alert generation for clinical
  care teams.
has_application:
- category: B2AI:Application
  contribution_date: '2024-11-15'
  contributor_github_name: erodriguez
  contributor_name: Elena Rodriguez
  contributor_orcid: ORCID:0000-0002-3456-7890
  datasheet:
  - https://example.com/datasheets/mobile-alerting-datasheet.pdf
  description: Mobile application component that receives alerts from the AI-powered
    clinical decision support system and notifies healthcare providers in real-time.
  id: B2AI_APP:102
  name: Mobile Alerting Component
  references:
  - https://doi.org/10.1000/example.mobile.alerting.2024
id: B2AI_APP:101
name: AI-Powered Clinical Decision Support for Sepsis Prediction
references:
- https://doi.org/10.1000/example.sepsis.ai.2024
- https://arxiv.org/abs/2401.12345
related_to:
- B2AI_STANDARD:105
- B2AI_DATA:42
- B2AI_USECASE:8
used_in_bridge2ai: true

```
## Organization-1
### Input
```yaml
category: B2AI_ORG:Organization
contribution_date: '2023-05-05'
contributor_name: Radha Chris
contributor_orcid: ORCID:0000-0005-1555-5773
description: US Agency for Healthcare Research and Quality
id: B2AI_ORG:1
name: AHRQ
ror_id: ror:03jmfdf59
subclass_of:
- B2AI_ORG:2
url: https://www.ahrq.gov/
wikidata_id: wikidata:Q4692008

```
## DataStandardOrTool-valid-1
### Input
```yaml
category: B2AI_STANDARD:DataStandardOrTool
collection:
- datamodel
concerns_data_topic:
- B2AI_TOPIC:4
contribution_date: '2023-03-03'
contributor_name: Guadalupe Nurul
contributor_orcid: ORCID:0000-0005-1272-5161
description: Observational Medical Outcomes Partnership Common Data Model
formal_specification: https://github.com/OHDSI/CommonDataModel
has_relevant_organization:
- B2AI_ORG:76
id: B2AI_STANDARD:53
is_open: true
name: OMOP CDM
publication: doi:10.3233/978-1-61499-564-7-574
purpose_detail: Open community data standard designed to standardize the structure
  and content of observational data and to enable efficient analyses that can produce
  reliable evidence.
requires_registration: false
responsible_organization:
- B2AI_ORG:76
url: https://ohdsi.github.io/CommonDataModel/

```
## DataStandardOrTool-minimal-1
### Input
```yaml
category: B2AI_STANDARD:DataStandardOrTool
description: A minimal but valid data standard or tool example that conforms to the
  schema
id: B2AI_STANDARD:53
name: Minimal DataStandardOrTool Example

```
## UseCase-valid-1
### Input
```yaml
alternative_standards_and_tools:
- B2AI_STANDARD:123
- B2AI_STANDARD:555
category: B2AI_USECASE:UseCase
contribution_date: '2023-01-01'
contributor_name: Sashi Wattana
contributor_orcid: ORCID:0000-0001-1234-5678
data_substrates:
- B2AI_SUBSTRATE:12
- B2AI_SUBSTRATE:34
data_topics:
- B2AI_TOPIC:5
- B2AI_TOPIC:6
description: "Collecting clinical data from patient visits involves the process of\
  \ gathering information about a patient's medical history, current symptoms, and\
  \ other relevant information during a healthcare appointment. This typically includes\
  \ taking a detailed medical history, conducting a physical examination, ordering\
  \ and interpreting diagnostic tests, and documenting the findings in the patient's\
  \ medical record. This may also include more focused evaluations, as with the AI-READI\
  \ project\u2019s assessments of cognitive function and visual acuity. Medical records\
  \ may include structured/unstructured text, values for lab results, and/or images."
enables:
- B2AI_USECASE:5
- B2AI_USECASE:13
- B2AI_USECASE:17
- B2AI_USECASE:19
id: B2AI_USECASE:1
involved_in_experimental_design: true
involved_in_metadata_management: true
involved_in_quality_control: false
known_limitations: xyz
name: Obtain patient data from records of clinical visits.
use_case_category:
- acquisition
xref:
- B2AI_USECASE:123
- B2AI_USECASE:456

```
## DataSet-minimal-1
### Input
```yaml
category: B2AI_DATA:DataSet
description: A minimal but valid dataset example that conforms to the schema
id: B2AI_DATA:3
name: Minimal Dataset Example

```
## DataTopic-valid-1
### Input
```yaml
category: B2AI_TOPIC:DataTopic
contribution_date: '2023-04-04'
contributor_name: Pitsiulaaq Mtendere
contributor_orcid: ORCID:0000-0002-1245-5763
description: Data involving any study of living organisms at any scale.
edam_id: edam.topic:3070
id: B2AI_TOPIC:2
mesh_id: mesh:D001695
name: Biology
ncit_id: ncit:C16345
subclass_of:
- B2AI_TOPIC:1

```
## DataSubstrate-minimal-1
### Input
```yaml
category: B2AI_SUBSTRATE:DataSubstrate
description: A minimal but valid data substrate example that conforms to the schema
id: B2AI_SUBSTRATE:53
name: Minimal DataSubstrate Example

```
## DataSubstrateContainer-minimal-1
### Input
```yaml
data_substrates_collection:
- category: B2AI_SUBSTRATE:DataSubstrate
  description: A minimal but valid data substrate container example that conforms
    to the schema
  id: B2AI_SUBSTRATE:container1
  name: Minimal DataSubstrateContainer Example

```
## DataStandardOrToolContainer-minimal-1
### Input
```yaml
data_standardortools_collection:
- category: B2AI_STANDARD:DataStandardOrTool
  description: A minimal but valid data standard or tool container example that conforms
    to the schema
  id: B2AI_STANDARD:container1
  name: Minimal DataStandardOrToolContainer Example

```
## DataTopic-valid-2
### Input
```yaml
category: B2AI_TOPIC:DataTopic
contributor_github_name: laverne
contributor_name: Laverne Billie
contributor_orcid: ORCID:0000-0001-5555-7811
description: Images obtained through one or more brain imaging techniques, including
  computed tomography, positron emission tomography, magnetic resonance imaging, or
  imaging of associated body structures (e.g., angiography).
edam_id: edam.data:3424
id: B2AI_TOPIC:22
mesh_id: mesh:D059906
name: Neurologic Imaging
ncit_id: ncit:C173635
subclass_of:
- B2AI_TOPIC:15
topic_involves_anatomy:
- uberon:0000955

```
## DataStandard-FHIR-valid-1
### Input
```yaml
category: B2AI_STANDARD:DataStandard
collection:
- datamodel
- clinicaldata
concerns_data_topic:
- B2AI_TOPIC:4
- B2AI_TOPIC:5
contribution_date: '2024-12-20'
contributor_name: Harry Caufield
contributor_orcid: ORCID:0000-0001-5705-7831
description: Fast Healthcare Interoperability Resources (FHIR) is a standard for exchanging
  healthcare information electronically. It provides a modular framework of components
  called resources that can be assembled into working systems to solve clinical and
  administrative problems. FHIR combines the best features of HL7's v2, v3 and CDA
  product lines while leveraging the latest web standards.
formal_specification: https://www.hl7.org/fhir/overview.html
has_application:
- category: B2AI:Application
  datasheet:
  - https://example.org/cds-datasheet
  description: AI-powered clinical decision support system that analyzes FHIR-formatted
    patient data to provide real-time recommendations for diagnosis and treatment
    planning.
  id: B2AI_APP:200
  name: FHIR-based Clinical Decision Support
  references:
  - https://doi.org/10.1093/jamia/example1
- category: B2AI:Application
  datasheet:
  - https://example.org/risk-prediction-datasheet
  description: Machine learning application that processes FHIR-based electronic health
    records to predict patient readmission risk and adverse outcomes.
  id: B2AI_APP:201
  name: FHIR Patient Risk Prediction
  references:
  - https://doi.org/10.1038/s41746-example
has_relevant_organization:
- B2AI_ORG:50
id: B2AI_STANDARD:105
is_open: true
name: HL7 FHIR
publication: https://doi.org/10.1016/j.jbi.2019.103175
purpose_detail: FHIR is designed to enable healthcare information exchange across
  different systems and organizations, supporting clinical care delivery, research,
  and public health reporting.
requires_registration: false
responsible_organization:
- B2AI_ORG:50
url: https://www.hl7.org/fhir/

```
## DataStandard-with-application-valid-1
### Input
```yaml
category: B2AI_STANDARD:DataStandard
collection:
- datamodel
- clinicaldata
- standards_process_maturity_final
- implementation_maturity_production
concerns_data_topic:
- B2AI_TOPIC:15
contribution_date: '2024-07-10'
contributor_github_name: athompson
contributor_name: Alexandra Thompson
contributor_orcid: ORCID:0000-0002-5555-6666
description: International standard for medical imaging information and related data
  exchange. DICOM enables the integration of medical imaging devices, PACS, and other
  systems from multiple manufacturers into a picture archiving and communication system.
formal_specification: https://github.com/dicom/dicom-standard
has_application:
- category: B2AI:Application
  contribution_date: '2024-10-20'
  contributor_name: Dr. Sarah Chen
  contributor_orcid: ORCID:0000-0003-1111-2222
  datasheet:
  - https://example.com/lung-nodule-ai-model-card.pdf
  description: Deep learning system that analyzes chest CT images in DICOM format
    to automatically detect and characterize pulmonary nodules, assisting radiologists
    in early lung cancer screening programs.
  id: B2AI_APP:201
  name: AI-Assisted Lung Nodule Detection in CT Scans
  references:
  - https://doi.org/10.1000/lung.nodule.ai.2024
- category: B2AI:Application
  contribution_date: '2024-09-15'
  contributor_name: Dr. Michael Park
  contributor_orcid: ORCID:0000-0003-2222-3333
  datasheet:
  - https://example.com/brain-tumor-segmentation-datasheet.pdf
  description: Convolutional neural network pipeline for automatic segmentation and
    classification of brain tumors in DICOM MRI sequences, supporting treatment planning
    and surgical navigation.
  id: B2AI_APP:202
  name: Automated Brain Tumor Segmentation
  references:
  - https://doi.org/10.1000/brain.tumor.seg.2024
  - https://arxiv.org/abs/2403.56789
- category: B2AI:Application
  contribution_date: '2024-08-30'
  contributor_name: Dr. James Liu
  contributor_orcid: ORCID:0000-0003-3333-4444
  description: Multi-task learning model for detecting diabetic retinopathy, age-related
    macular degeneration, and glaucoma from DICOM-formatted fundus photographs, enabling
    automated screening in ophthalmology clinics.
  id: B2AI_APP:203
  name: Retinal Disease Classification from Fundus Images
  references:
  - https://doi.org/10.1000/retinal.ai.2024
has_relevant_organization:
- B2AI_ORG:200
- B2AI_ORG:201
id: B2AI_STANDARD:201
is_open: true
name: DICOM (Digital Imaging and Communications in Medicine)
publication: doi:10.1148/radiology.148.1.6856849
purpose_detail: Facilitates storage, transmission, and display of medical images across
  heterogeneous systems while preserving clinical context and patient information.
requires_registration: false
responsible_organization:
- B2AI_ORG:200
url: https://www.dicomstandard.org/
used_in_bridge2ai: true

```
## DataTopicContainer-valid-1
### Input
```yaml
data_topics_collection:
- category: B2AI_TOPIC:DataTopic
  description: Data involving any study of living organisms at any scale.
  edam_id: edam.topic:3070
  id: B2AI_TOPIC:2
  mesh_id: mesh:D001695
  name: Biology
  ncit_id: ncit:C16345
  subclass_of:
  - B2AI_TOPIC:1
- category: B2AI_TOPIC:DataTopic
  description: A broad data topic encompassing all scientific disciplines
  id: B2AI_TOPIC:3
  name: Science

```
## DataStandard-WFDB-valid-1
### Input
```yaml
category: B2AI_STANDARD:DataStandard
collection:
- clinicaldata
concerns_data_topic:
- B2AI_TOPIC:4
- B2AI_TOPIC:36
contribution_date: '2024-12-20'
contributor_name: Harry Caufield
contributor_orcid: ORCID:0000-0001-5705-7831
description: The WaveForm DataBase (WFDB) format is a widely-used standard for storing
  physiological signals and annotations. Originally developed for cardiac signals,
  WFDB now supports a wide range of physiological waveform data including ECG, EEG,
  blood pressure, and respiratory waveforms. The format consists of binary signal
  files and text header files that describe the signal properties, making it efficient
  for long-term physiological recordings while maintaining compatibility across platforms.
formal_specification: https://physionet.org/physiotools/wag/header-5.htm
has_application:
- category: B2AI:Application
  datasheet:
  - https://example.org/wfdb-arrhythmia-datasheet
  description: Recurrent neural network that processes WFDB-formatted ECG signals
    to automatically detect and classify cardiac arrhythmias in real-time monitoring
    applications.
  id: B2AI_APP:230
  name: WFDB Arrhythmia Detection
  references:
  - https://doi.org/10.1161/CIRCEP.example
- category: B2AI:Application
  datasheet:
  - https://example.org/wfdb-icu-datasheet
  description: Multi-modal deep learning system that analyzes WFDB-formatted vital
    sign waveforms to predict adverse events in intensive care unit patients.
  id: B2AI_APP:231
  name: WFDB Critical Care Event Prediction
  references:
  - https://doi.org/10.1097/CCM.example
has_relevant_organization:
- B2AI_ORG:140
id: B2AI_STANDARD:202
is_open: true
name: WaveForm DataBase (WFDB) Format
publication: https://doi.org/10.13026/C2V30W
purpose_detail: WFDB format enables standardized storage and exchange of physiological
  signal data for clinical care, research, and algorithm development, particularly
  for cardiology and critical care applications.
requires_registration: false
responsible_organization:
- B2AI_ORG:140
url: https://physionet.org/content/wfdb/

```
## SoftwareOrTool-BIDS-valid-1
### Input
```yaml
category: B2AI_STANDARD:SoftwareOrTool
collection:
- datamodel
- minimuminformationschema
concerns_data_topic:
- B2AI_TOPIC:22
- B2AI_TOPIC:5
contribution_date: '2024-12-20'
contributor_name: Harry Caufield
contributor_orcid: ORCID:0000-0001-5705-7831
description: The Brain Imaging Data Structure (BIDS) is a specification for organizing
  and describing neuroimaging and behavioral data. BIDS prescribes a file structure
  and naming convention to organize data files and includes standardized metadata
  schemas for describing experimental details. It supports multiple neuroimaging modalities
  including MRI, EEG, MEG, iEEG, and PET, making neuroimaging datasets machine-readable
  and enabling automated data processing pipelines.
formal_specification: https://bids-specification.readthedocs.io/
has_application:
- category: B2AI:Application
  datasheet:
  - https://example.org/bids-alzheimers-datasheet
  description: Convolutional neural network trained on BIDS-formatted structural MRI
    data to predict Alzheimer's disease progression from baseline and longitudinal
    neuroimaging features.
  id: B2AI_APP:220
  name: BIDS-based Alzheimer's Disease Prediction
  references:
  - https://doi.org/10.1016/j.neuroimage.example
- category: B2AI:Application
  datasheet:
  - https://example.org/bids-fmri-datasheet
  description: Deep learning framework that processes BIDS-formatted functional MRI
    data to classify cognitive states and decode brain activity patterns.
  id: B2AI_APP:221
  name: BIDS fMRI Pattern Classification
  references:
  - https://doi.org/10.1038/nn.example
has_relevant_organization:
- B2AI_ORG:85
has_training_resource:
- B2AI_STANDARD:900
id: B2AI_STANDARD:33
is_open: true
name: Brain Imaging Data Structure (BIDS)
publication: https://doi.org/10.1038/sdata.2016.44
purpose_detail: BIDS facilitates data sharing, reproducibility, and collaboration
  in neuroimaging research by providing a standardized format that can be automatically
  validated and processed by analysis tools.
requires_registration: false
responsible_organization:
- B2AI_ORG:85
url: https://bids.neuroimaging.io/

```
## Organization-minimal-1
### Input
```yaml
category: B2AI_ORG:Organization
description: A minimal but valid organization example that conforms to the schema
id: B2AI_ORG:2
name: Minimal Organization Example

```
## UseCase-minimal-1
### Input
```yaml
category: B2AI_USECASE:UseCase
description: A minimal but valid use case example that conforms to the schema
id: B2AI_USECASE:1
name: Minimal UseCase Example
use_case_category:
- acquisition

```
## DataSubstrate-1i
### Input
```yaml
EDAM_ID: edam.format:3003
NCIT_ID: ncit:C153367
description: BED (Browser Extensible Data) format provides a flexible way to define
  the data lines that are displayed in a genome annotation track.
file_extensions:
- txt
- bed
id: B2AI_SUBSTRATE:53
limitations: Sequences can get very long.
metadata_storage: 5
name: BED
subclass_of: 100

```
## DataTopic-1i
### Input
```yaml
EDAM_ID: edam.topic:3070
MeSH_ID: mesh:D001695
NCIT_ID: ncit:C16345
description: Good fish for sandwiches.
id: tuna fish
name: Biology
subclass_of: 1

```
## UseCase-1i
### Input
```yaml
alternative_standards_and_tools: null
data_topics:
- B2AI_TOPIC:Image
- B2AI_TOPIC::Clinical_Observations
description: "Collecting clinical data from patient visits involves the process of\
  \ gathering information about a patient's medical history, current symptoms, and\
  \ other relevant information during a healthcare appointment. This typically includes\
  \ taking a detailed medical history, conducting a physical examination, ordering\
  \ and interpreting diagnostic tests, and documenting the findings in the patient's\
  \ medical record. This may also include more focused evaluations, as with the AI-READI\
  \ project\u2019s assessments of cognitive function and visual acuity. Medical records\
  \ may include structured/unstructured text, values for lab results, and/or images."
enables:
- B2AI_USECASE:5
- B2AI_USECASE:13
- B2AI_USECASE:17
- B2AI_USECASE:19
id: 1
involved_in_experimental_design: true
involved_in_metadata_management: true
involved_in_quality_control: Not applicable
name: Obtain patient data from records of clinical visits.
relevance_to_dgps:
- 1
- 2
- 3
standards_and_tools_for_dgp_use:
- B2AI_STANDARD:DICOM
- B2AI_STANDARD:OMOP_CDM
use_case_category: Acquisition

```
## Organization-1i
### Input
```yaml
ROR_ID: ror_03jmfdf59
URL: null
Wikidata_ID: CHEBI:Q4692008
description: My Uncle Greg's Storage Unit
id: B2AI_ORG:1
name: null
subclass_of: B2AI_ORG:2

```
## UseCaseContainer-1i
### Input
```yaml
use_cases:
- id: B2AI_USECASE:1
  use_case_category: Acquisition
- id: B2AI_USECASE:2
  use_case_category: Acquisition

```
## DataStandardOrTool-1i
### Input
```yaml
concerns data topic:
- B2AI_TOPIC:4
description: Observational Medical Outcomes Partnership Common Data Model
formal_specification: https://github.com/OHDSI/CommonDataModel
has relevant organization:
- B2AI_ORGANIZATION:76
id: B2AI_STANDARD:53
is_open_data: true
name: OMOP CDM
publication: doi:10.3233/978-1-61499-564-7-574
purpose_detail: Open community data standard designed to standardize the structure
  and content of observational data and to enable efficient analyses that can produce
  reliable evidence.
requires_registration: 3
url: https://ohdsi.github.io/CommonDataModel/

```
