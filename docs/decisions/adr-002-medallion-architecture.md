# ADR 002: Medallion Architecture for Data Layers

## Status

Accepted

## Context

To ensure data quality and reliability, we need a clear structure for our data lakehouse.

## Decision

We will follow the Medallion Architecture (Bronze, Silver, Gold layers).

## Consequences

- **Bronze:** Raw data from sources.
- **Silver:** Cleaned and standardized data.
- **Gold:** Curated, business-ready data for analytics and reporting.
