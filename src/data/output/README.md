## DataTopic-1
### Input
```yaml
EDAM_ID: edam.topic:3070
MeSH_ID: mesh:D001695
NCIT_ID: ncit:C16345
description: Data involving any study of living organisms at any scale.
id: STANDARDSDATATOPIC:2
name: Biology
subclass_of:
- STANDARDSDATATOPIC:1

```
## DataStandardOrTool-1
### Input
```yaml
collection:
- datamodel
concerns_data_topic:
- STANDARDSDATATOPIC:4
description: Observational Medical Outcomes Partnership Common Data Model
formal_specification: https://github.com/OHDSI/CommonDataModel
has_relevant_organization:
- STANDARDSORGANIZATION:76
id: STANDARDSDATASTANDARDORTOOL:53
is_open: true
name: OMOP CDM
publication: doi:10.3233/978-1-61499-564-7-574
purpose_detail: Open community data standard designed to standardize the structure
  and content of observational data and to enable efficient analyses that can produce
  reliable evidence.
requires_registration: false
url: https://ohdsi.github.io/CommonDataModel/

```
## Organization-1
### Input
```yaml
ROR_ID: ror:03jmfdf59
URL: https://www.ahrq.gov/
Wikidata_ID: wikidata:Q4692008
description: US Agency for Healthcare Research and Quality
id: STANDARDSORGANIZATION:1
name: AHRQ
subclass_of:
- STANDARDSORGANIZATION:2

```
## UseCase-valid-1
### Input
```yaml
alternative_standards_and_tools:
- STANDARDSUSECASE:123
- STANDARDSUSECASE:555
data_substrates:
- STANDARDSUSECASE:abc
- STANDARDSUSECASE:xyz
data_topics:
- STANDARDSDATATOPIC:Image
- STANDARDSDATATOPIC:Clinical_Observations
description: "Collecting clinical data from patient visits involves the process of\
  \ gathering information about a patient's medical history, current symptoms, and\
  \ other relevant information during a healthcare appointment. This typically includes\
  \ taking a detailed medical history, conducting a physical examination, ordering\
  \ and interpreting diagnostic tests, and documenting the findings in the patient's\
  \ medical record. This may also include more focused evaluations, as with the AI-READI\
  \ project\u2019s assessments of cognitive function and visual acuity. Medical records\
  \ may include structured/unstructured text, values for lab results, and/or images."
enables:
- STANDARDSUSECASE:5
- STANDARDSUSECASE:13
- STANDARDSUSECASE:17
- STANDARDSUSECASE:19
id: STANDARDSUSECASE:1
involved_in_experimental_design: true
involved_in_metadata_management: true
involved_in_quality_control: false
known_limitations: xyz
name: Obtain patient data from records of clinical visits.
relevance_to_dgps:
- aireadi
- chorus
- voice
standards_and_tools_for_dgp_use:
- STANDARDSDATASTANDARDORTOOL:DICOM
- STANDARDSDATASTANDARDORTOOL:OMOP_CDM
use_case_category: acquisition
xref:
- STANDARDSUSECASE:abc
- STANDARDSUSECASE:xyz

```
## UseCaseContainer-minimal
### Input
```yaml
container_name: container_1
use_cases:
- id: STANDARDSUSECASE:1
  use_case_category: acquisition
- id: STANDARDSUSECASE:2
  use_case_category: acquisition

```
## UseCase-minimal-1
### Input
```yaml
id: STANDARDSUSECASE:1
use_case_category: acquisition

```
## DataSubstrate-1
### Input
```yaml
EDAM_ID: edam.format:3003
NCIT_ID: ncit:C153367
description: BED (Browser Extensible Data) format provides a flexible way to define
  the data lines that are displayed in a genome annotation track.
file_extensions:
- txt
- bed
id: STANDARDSDATASUBSTRATE:53
limitations:
- Sequences can get very long.
metadata_storage:
- file headers
name: BED
subclass_of:
- STANDARDSDATASUBSTRATE:1

```
## UseCase-invalid-1
### Input
```yaml
data_topics:
- STANDARDSDATATOPIC:Image
- STANDARDSDATATOPIC:Clinical_Observations
enables:
- STANDARDSUSECASE:5
- STANDARDSUSECASE:13
- STANDARDSUSECASE:17
- STANDARDSUSECASE:19
fake_slot: fake_value
id: STANDARDSUSECASE:1
involved_in_experimental_design: true
involved_in_metadata_management: true
involved_in_quality_control: false
relevance_to_dgps:
- aireadi
- chorus
- voice
standards_and_tools_for_dgp_use:
- STANDARDSDATASTANDARDORTOOL:DICOM
- STANDARDSDATASTANDARDORTOOL:OMOP_CDM
use_case_category: acquisition

```
## Organization-1i
### Input
```yaml
ROR_ID: ror_03jmfdf59
URL: null
Wikidata_ID: CHEBI:Q4692008
description: My Uncle Greg's Storage Unit
id: STANDARDSORGANIZATION:1
name: null
subclass_of: STANDARDSORGANIZATION:2

```
## DataStandardOrTool-1i
### Input
```yaml
collection: null
concerns data topic:
- STANDARDSDATATOPIC:4
description: Observational Medical Outcomes Partnership Common Data Model
formal_specification: https://github.com/OHDSI/CommonDataModel
has relevant organization:
- STANDARDSORGANIZATION:76
id: STANDARDSDATASTANDARDORTOOL:53
is_open_data: true
name: OMOP CDM
publication: doi:10.3233/978-1-61499-564-7-574
purpose_detail: Open community data standard designed to standardize the structure
  and content of observational data and to enable efficient analyses that can produce
  reliable evidence.
requires_registration: false
url: https://ohdsi.github.io/CommonDataModel/

```
## UseCase-1i
### Input
```yaml
alternative_standards_and_tools: null
data_substrates: null
data_topics:
- STANDARDSDATATOPIC:Image
- STANDARDSDATATOPIC:Clinical_Observations
description: "Collecting clinical data from patient visits involves the process of\
  \ gathering information about a patient's medical history, current symptoms, and\
  \ other relevant information during a healthcare appointment. This typically includes\
  \ taking a detailed medical history, conducting a physical examination, ordering\
  \ and interpreting diagnostic tests, and documenting the findings in the patient's\
  \ medical record. This may also include more focused evaluations, as with the AI-READI\
  \ project\u2019s assessments of cognitive function and visual acuity. Medical records\
  \ may include structured/unstructured text, values for lab results, and/or images."
enables:
- STANDARDSUSECASE:5
- STANDARDSUSECASE:13
- STANDARDSUSECASE:17
- STANDARDSUSECASE:19
id: 1
involved_in_experimental_design: true
involved_in_metadata_management: true
involved_in_quality_control: false
known_limitations: null
name: Obtain patient data from records of clinical visits.
relevance_to_dgps:
- 1
- 2
- 3
standards_and_tools_for_dgp_use:
- STANDARDSDATASTANDARDORTOOL:DICOM
- STANDARDSDATASTANDARDORTOOL:OMOP_CDM
use_case_category: Acquisition
xref: null

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
id: STANDARDSDATASUBSTRATE:53
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
