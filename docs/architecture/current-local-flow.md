# Current Local Flow

The current local data flow demonstrates a full vertical slice from dataset selection to visualization.

## Mermaid Diagram

```mermaid
flowchart LR
    A[Dataset Catalog<br/>meteocat-weather selected] --> B[Ingestion<br/>landing JSON]
    B --> C[Landing Quality<br/>JSON validation]
    C --> D[Transformation<br/>bronze JSONL]
    D --> E[Bronze Quality<br/>JSONL validation]
    E --> F[Silver Transformation<br/>silver JSONL]
    F --> G[Silver Quality<br/>JSONL validation]
    G --> H[Orchestration<br/>run-summary.json]
    H --> I[Observability<br/>JSON and Markdown reports]
    I --> J[Dashboards<br/>static HTML]
```

## Local Artifact Types

The flow produces the following artifact types:

- **Landing**: `JSON`
- **Bronze**: `JSONL`
- **Silver**: `JSONL`
- **Observability**: `JSON` and `Markdown` reports
- **Dashboard**: static `HTML`

Note: Apache Parquet is currently being evaluated for future implementation but is not part of the current local MVP flow.
