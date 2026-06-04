# Weather Local Vertical Slice

This page describes the first local Weather MVP vertical slice of the Open Data Lakehouse Lab.

## Overview

The goal of this vertical slice is to demonstrate a complete data flow from catalog selection to dashboard generation in a local environment, without requiring cloud credentials or complex infrastructure.

- **MVP Dataset**: `meteocat-weather`
- **Deployment Mode**: Local-first
- **Cloud Dependency**: None (works without cloud credentials)
- **Offline Mode**: Sample/offline mode is available for testing and development.

## Supported Meteocat Resources

The current implementation supports the following Meteocat resources:

- `stations-metadata`
- `variables-metadata`
- `measured-variable`

## Data Flow

The flow currently focuses on the following stages:

1. **Dataset Catalog Selection**: Selecting `meteocat-weather`.
2. **Ingestion**: Generating landing JSON files. Real Meteocat ingestion exists as an opt-in feature for selected resources.
3. **Landing Quality**: JSON validation checks.
4. **Transformation**: Converting landing JSON to bronze JSONL.
5. **Bronze Quality**: JSONL validation checks.
6. **Orchestration**: Generating a run summary.
7. **Observability**: Producing JSON and Markdown reports.
8. **Dashboards**: Generating a static HTML dashboard.

## Security and Credentials

- **API Keys**: Real API keys are never committed to the repositories.
- **Opt-in Ingestion**: Real ingestion requires a local configuration with valid API keys.

## Local Execution

At a high level, the flow can be executed using the CLI tools provided in each repository.

### Orchestrated execution

The preferred way to run the full vertical slice is through the orchestration CLI:

```bash
odl-orchestration run weather-mvp-local \
  --catalog-path ../datasets-catalog \
  --ingestion-repo-path ../ingestion \
  --transformation-repo-path ../transformation \
  --quality-repo-path ../quality \
  --workspace-dir ./workspace
```

### Individual component execution

Individual steps can also be executed manually using their respective CLIs:

```bash
# Ingestion
odl-ingestion ingest \
  --dataset meteocat-weather \
  --catalog-path ../datasets-catalog \
  --target local \
  --output-dir ./data \
  --mode sample

# Transformation
odl-transformation transform \
  --dataset meteocat-weather \
  --resource stations-metadata \
  --input-path ./examples/landing/meteocat/stations-metadata.json \
  --output-dir ./data

# Quality checks (Landing)
odl-quality check landing \
  --dataset meteocat-weather \
  --resource stations-metadata \
  --input-path ./examples/landing/stations-metadata.json

# Quality checks (Bronze)
odl-quality check bronze \
  --dataset meteocat-weather \
  --resource stations-metadata \
  --input-path ./examples/bronze/stations-metadata.jsonl

# Observability
odl-observability inspect run \
  --run-summary-path ./examples/run-summary.json

# Dashboards
odl-dashboards render observability \
  --report-path ./examples/run-observability-report.json \
  --output-dir ./dashboard
```

## Status

:::caution Not Production Ready
This is a laboratory MVP vertical slice. It is intended for learning and experimentation and is not ready for production use.
:::
