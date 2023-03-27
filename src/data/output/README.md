## DataSubstrate-minimal-1
### Input
```yaml
id: B2AI_SUBSTRATE:53

```
## UseCase-valid-1
### Input
```yaml
alternative_standards_and_tools:
- B2AI_STANDARD:123
- B2AI_STANDARD:555
category: UseCase
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
relevance_to_dgps:
- aireadi
- chorus
- voice
standards_and_tools_for_dgp_use:
- B2AI_STANDARD:5
- B2AI_STANDARD:10
use_case_category: acquisition
xref:
- B2AI_USECASE:123
- B2AI_USECASE:456

```
## DataSubstrate-valid-1
### Input
```yaml
category: DataSubstrate
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
## Organization-1
### Input
```yaml
category: Organization
description: US Agency for Healthcare Research and Quality
id: B2AI_ORGANIZATION:1
name: AHRQ
ror_id: ror:03jmfdf59
subclass_of:
- B2AI_ORGANIZATION:2
url: https://www.ahrq.gov/
wikidata_id: wikidata:Q4692008

```
## DataTopic-valid-1
### Input
```yaml
category: DataTopic
description: Data involving any study of living organisms at any scale.
edam_id: edam.topic:3070
id: B2AI_TOPIC:2
mesh_id: mesh:D001695
name: Biology
ncit_id: ncit:C16345
subclass_of:
- B2AI_TOPIC:1

```
## DataStandardOrTool-valid-1
### Input
```yaml
category: BiomedicalStandard
collection:
- datamodel
concerns_data_topic:
- B2AI_TOPIC:4
description: Observational Medical Outcomes Partnership Common Data Model
formal_specification: https://github.com/OHDSI/CommonDataModel
has_relevant_organization:
- B2AI_ORGANIZATION:76
id: B2AI_STANDARD:53
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
  id: B2AI_TOPIC:2
  mesh_id: mesh:D001695
  name: Biology
  ncit_id: ncit:C16345
  subclass_of:
  - B2AI_TOPIC:1
- id: B2AI_TOPIC:3
  name: Science

```
## Organization-minimal-1
### Input
```yaml
id: B2AI_ORGANIZATION:2

```
## UseCase-minimal-1
### Input
```yaml
id: B2AI_USECASE:1
use_case_category: acquisition

```
## DataStandardOrToolContainer-minimal-1
### Input
```yaml
data_standardortools_collection:
- id: B2AI_STANDARD:1
- id: B2AI_STANDARD:2

```
## UseCaseContainer-minimal-1
### Input
```yaml
use_cases:
- id: B2AI_USECASE:1
  use_case_category: acquisition
- id: B2AI_USECASE:2
  use_case_category: acquisition

```
## DataStandardOrTool-minimal-1
### Input
```yaml
id: B2AI_STANDARD:53

```
## DataSubstrateContainer-minimal-1
### Input
```yaml
data_substrates_collection:
- id: B2AI_SUBSTRATE:1
- id: B2AI_SUBSTRATE:2

```
## OrganizationContainer-minimal-1
### Input
```yaml
organizations:
- id: B2AI_ORGANIZATION:1
- id: B2AI_ORGANIZATION:2

```
## DataTopic-minimal-1
### Input
```yaml
id: B2AI_TOPIC:2

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
## UseCaseContainer-1i
### Input
```yaml
use_cases:
- id: B2AI_USECASE:1
  use_case_category: Acquisition
- id: B2AI_USECASE:2
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
## Organization-1i
### Input
```yaml
ROR_ID: ror_03jmfdf59
URL: null
Wikidata_ID: CHEBI:Q4692008
description: My Uncle Greg's Storage Unit
id: B2AI_ORGANIZATION:1
name: null
subclass_of: B2AI_ORGANIZATION:2

```
