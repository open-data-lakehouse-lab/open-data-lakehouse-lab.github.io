# Open Data Lakehouse Lab

Public documentation for the Open Data Lakehouse Lab project.

This is a personal open-source laboratory for building a multi-cloud open data lakehouse with public datasets, local cloud-like environments, Infrastructure as Code, data pipelines, analytics services and dashboards.

## Documentation Site

The documentation is built with Docusaurus and published to GitHub Pages.

Visit the live site: [https://open-data-lakehouse-lab.github.io](https://open-data-lakehouse-lab.github.io)

## Local Development

To run the documentation site locally:

1.  **Install dependencies:**
    ```bash
    npm install
    ```

2.  **Start the development server:**
    ```bash
    npm start
    ```

3.  **Build the production site:**
    ```bash
    npm run build
    ```

## Asset Management

To generate the operational website assets from the source brand assets:

```bash
pip install Pillow
python3 scripts/generate-brand-assets.py
```

## Project Status

This project is public, open source and independent. It is not affiliated with any company or organization.

## License

Unless otherwise noted:

- Documentation, articles, diagrams, dataset metadata, data dictionaries, schemas, data contracts and written content are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
- Software, scripts, Infrastructure as Code, SQL models, configuration files and executable assets are licensed under the [Apache License 2.0](LICENSE-CODE).

Original upstream datasets, when referenced, remain governed by their original source licenses and terms.
