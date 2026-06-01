# Lakehouse Layers

We implement the Medallion architecture to organize data based on its quality and structure.

- **Landing / Raw:** Exact copy of source data.
- **Bronze:** Raw data with minimal processing, converted to table format.
- **Silver:** Cleaned, filtered, and augmented data.
- **Gold:** Aggregated data ready for business consumption and analytics.
