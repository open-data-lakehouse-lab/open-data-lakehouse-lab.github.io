# Current Status

This page tracks the current progress and roadmap of the Open Data Lakehouse Lab.

## Milestones Status

### M0 - Foundation
- **Status**: Mostly completed for core local repositories.
- **Details**: Basic infrastructure, project structure, and documentation site are established.

### M1 - Weather MVP Local Slice
- **Status**: In progress / First local vertical slice implemented.
- **Details**: The `meteocat-weather` dataset flow is functional in a local environment, covering catalog selection through to static dashboard generation.

## Implementation Details

| Feature | Status | Notes |
| :--- | :--- | :--- |
| **Cloud/Local Azure Lab** | Foundation exists | Not yet integrated into the MVP flow. |
| **Real Cloud Deployment** | Not implemented | Currently focusing on local-first development. |
| **Medallion - Bronze** | Implemented | JSONL format used. |
| **Medallion - Silver/Gold** | Not implemented | Future modeling work required. |
| **Advanced Dashboards** | Not implemented | Currently using static HTML generation. |
| **External Observability Stack** | Not selected | Evaluating options (e.g., Prometheus, Grafana, ELK). |

## Roadmap Notes

The project follows an incremental approach. Current efforts are focused on stabilizing the local MVP flow before moving towards cloud integration and more complex data modeling (Silver/Gold layers).
