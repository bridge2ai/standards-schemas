# Enum: UseCaseCategory 




_Category of use case. These define the high-level purpose of a task or activity as part of a broader research effort or other data-related project. They are not mutually exclusive and one use case may involve multiple categories._



URI: [UseCaseCategory](UseCaseCategory.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| acquisition | None | Acquisition |
| integration | None | Integration |
| standardization | None | Standardization |
| modeling | None | Modeling |
| application | None | Application |
| assessment | None | Assessment |




## Slots

| Name | Description |
| ---  | --- |
| [use_case_category](use_case_category.md) | Category of the UseCase |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/standards-schema-all






## LinkML Source

<details>
```yaml
name: UseCaseCategory
description: Category of use case. These define the high-level purpose of a task or
  activity as part of a broader research effort or other data-related project. They
  are not mutually exclusive and one use case may involve multiple categories.
from_schema: https://w3id.org/bridge2ai/standards-schema-all
rank: 1000
permissible_values:
  acquisition:
    text: acquisition
    description: Acquisition. The use case involves the collection of data from one
      or more sources, including data generation, data capture, and data entry.
  integration:
    text: integration
    description: Integration. The use case involves the combination of data from multiple
      sources, including data harmonization, data linkage, and data aggregation.
  standardization:
    text: standardization
    description: Standardization. The use case involves the application of standards
      to data, including data normalization, data validation, and quality control.
  modeling:
    text: modeling
    description: Modeling. The use case involves the development of models, including
      predictive models, statistical models, and machine learning models.
  application:
    text: application
    description: Application. The use case involves the use of data for a specific
      scientific or otherwise productive purpose, including data analysis, data visualization,
      and data interpretation. This also includes clinical decision support, patient
      care, and other applications of data in a biomedical context.
  assessment:
    text: assessment
    description: Assessment. The use case involves the evaluation of data quality,
      data provenance, and data utility, including the assessment of standards, data
      tools, and data resources. Note this differs from the standardization category,
      which involves the application of standards to data.

```
</details>
