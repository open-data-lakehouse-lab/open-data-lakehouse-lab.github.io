# Implemented Repositories

The following repositories have been implemented or initialized to support the current local MVP vertical slice.

| Repository | Current Role | Current Status | Main CLI/Tooling | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `datasets-catalog` | Dataset metadata and selection | Foundation implemented | YAML / Python | Contains `meteocat-weather` definition. |
| `ingestion` | Data fetching and landing | Local MVP slice implemented | Python | Supports real and sample ingestion. |
| `transformation` | Data processing (Bronze) | Local MVP slice implemented | Python | Focuses on JSON to JSONL conversion. |
| `quality` | Data validation | Local MVP slice implemented | Python / local quality checks | Validates Landing and Bronze artifacts. |
| `orchestration` | Pipeline coordination | Local MVP slice implemented | Python / CLI | Manages multi-resource Weather workflow. |
| `observability` | Monitoring and reporting | Local MVP slice implemented | Python / Markdown | Generates run summaries and reports. |
| `dashboards` | Data visualization | Local MVP slice implemented | Python / Static HTML | Generates static dashboards from processed data. |

## Status Definitions

- **Foundation implemented**: Basic structure, configuration, and core logic are in place.
- **Local MVP slice implemented**: Repository fully supports the `meteocat-weather` local vertical slice.
- **Production-ready**: Not yet achieved. The project remains in a laboratory/MVP stage.
