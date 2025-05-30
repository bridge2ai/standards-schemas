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
