## DataSubstrate-minimal-1
### Input
```yaml
id: STANDARDSDATASUBSTRATE:53

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
## DataSubstrate-valid-1
### Input
```yaml
description: BED (Browser Extensible Data) format provides a flexible way to define
  the data lines that are displayed in a genome annotation track.
edam_id: edam.format:3003
id: STANDARDSDATASUBSTRATE:53
metadata_storage:
- file headers
name: BED
ncit_id: ncit:C153367
subclass_of:
- STANDARDSDATASUBSTRATE:1

```
## Organization-1
### Input
```yaml
description: US Agency for Healthcare Research and Quality
id: STANDARDSORGANIZATION:1
name: AHRQ
ror_id: ror:03jmfdf59
subclass_of:
- STANDARDSORGANIZATION:2
url: https://www.ahrq.gov/
wikidata_id: wikidata:Q4692008

```
## DataTopic-valid-1
### Input
```yaml
description: Data involving any study of living organisms at any scale.
edam_id: edam.topic:3070
id: STANDARDSDATATOPIC:2
mesh_id: mesh:D001695
name: Biology
ncit_id: ncit:C16345
subclass_of:
- STANDARDSDATATOPIC:1

```
## DataStandardOrToolContainer-valid-1
### Input
```yaml
data_standardortools_collection:
- id: STANDARDSDATASTANDARDORTOOL:1
- id: STANDARDSDATASTANDARDORTOOL:2

```
## DataStandardOrTool-valid-1
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
## DataTopicContainer-valid-1
### Input
```yaml
data_topics_collection:
- description: Data involving any study of living organisms at any scale.
  edam_id: edam.topic:3070
  id: STANDARDSDATATOPIC:2
  mesh_id: mesh:D001695
  name: Biology
  ncit_id: ncit:C16345
  subclass_of:
  - STANDARDSDATATOPIC:1
- id: STANDARDSDATATOPIC:3
  name: Science

```
## Organization-minimal-1
### Input
```yaml
id: STANDARDSORGANIZATION:2

```
## UseCase-minimal-1
### Input
```yaml
id: STANDARDSUSECASE:1
use_case_category: acquisition

```
## UseCaseContainer-minimal-1
### Input
```yaml
use_cases:
- id: STANDARDSUSECASE:1
  use_case_category: acquisition
- id: STANDARDSUSECASE:2
  use_case_category: acquisition

```
## DataStandardOrTool-minimal-1
### Input
```yaml
id: STANDARDSDATASTANDARDORTOOL:53

```
## DataSubstrateContainer-minimal-1
### Input
```yaml
data_substrates_collection:
- id: STANDARDSDATASUBSTRATE:1
- id: STANDARDSDATASUBSTRATE:2

```
## OrganizationContainer-minimal-1
### Input
```yaml
organizations:
- id: STANDARDSORGANIZATION:1
- id: STANDARDSORGANIZATION:2

```
## DataTopic-minimal-1
### Input
```yaml
id: STANDARDSDATATOPIC:2

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
## UseCaseContainer-1i
### Input
```yaml
use_cases:
- id: STANDARDSUSECASE:1
  use_case_category: Acquisition
- id: STANDARDSUSECASE:2
  use_case_category: Acquisition

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
name: Obtain patient data from records of clinical visits.
relevance_to_dgps:
- 1
- 2
- 3
standards_and_tools_for_dgp_use:
- STANDARDSDATASTANDARDORTOOL:DICOM
- STANDARDSDATASTANDARDORTOOL:OMOP_CDM
use_case_category: Acquisition

```
## DataStandardOrTool-1i
### Input
```yaml
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
