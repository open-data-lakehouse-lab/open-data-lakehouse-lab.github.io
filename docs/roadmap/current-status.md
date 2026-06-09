# Current Status

This page tracks the current progress and roadmap of the Open Data Lakehouse Lab.

## Milestones Status

### M0 - Foundation
- **Status**: Mostly completed for core local repositories.
- **Details**: Basic infrastructure, project structure, and documentation site are established.

### M1 - Weather MVP Local Slice
- **Status**: In progress / First local vertical slice implemented.
- **Details**: The `meteocat-weather` dataset flow is functional in a local environment, covering catalog selection through to static dashboard generation. First local multi-resource E2E run with Silver and optional landing contract validation verified successfully.

## Implementation Details

| Feature | Status | Notes |
| :--- | :--- | :--- |
| **Cloud/Local Azure Lab** | Foundation exists | Not yet integrated into the MVP flow. |
| **Real Cloud Deployment** | Not implemented | Currently focusing on local-first development. |
| **Real API Ingestion Hardening** | Implemented | Meteocat real API ingestion mode hardened (opt-in). |
| **Medallion - Bronze** | Implemented | JSONL format used. |
| **Medallion - Silver** | Implemented | Silver JSONL foundation. |
| **Medallion - Gold** | Not implemented | Future modeling work required. |
| **Data Contracts** | Draft | Optional landing contract validation supported. |
| **Advanced Dashboards** | Not implemented | Currently using static HTML generation. |
| **External Observability Stack** | Not selected | Evaluating options (e.g., Prometheus, Grafana, ELK). |

## Roadmap Notes

The project follows an incremental approach. Current efforts are focused on stabilizing the local MVP flow before moving towards cloud integration and more complex data modeling (Gold layers). First local multi-resource E2E run with Silver and optional landing contract validation verified successfully. Silver exists as a local foundation, not final analytics model. Meteocat real API ingestion hardening implemented (opt-in). Live API verification remains future work. Contracts are draft/minimal/internal.
