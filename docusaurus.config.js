import {themes as githubThemes} from 'prism-react-renderer';
import {themes as draculaThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Open Data Lakehouse Lab',
  tagline: 'A personal open-source laboratory for building a multi-cloud open data lakehouse.',
  // favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://open-data-lakehouse-lab.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'open-data-lakehouse-lab', // Usually your GitHub org/user name.
  projectName: 'open-data-lakehouse-lab.github.io', // Usually your repo name.
  trailingSlash: false,

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  markdown: {
    mermaid: true,
    anchors: {
      maintainCase: true,
    },
    format: 'mdx',
  },
  themes: ['@docusaurus/theme-mermaid'],

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          editUrl:
            'https://github.com/open-data-lakehouse-lab/open-data-lakehouse-lab.github.io/tree/main/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      // image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'Open Data Lakehouse Lab',
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Documentation',
          },
          {
            href: 'https://github.com/open-data-lakehouse-lab/open-data-lakehouse-lab.github.io',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Introduction',
                to: '/docs/introduction/overview',
              },
              {
                label: 'Architecture',
                to: '/docs/architecture/overview',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/open-data-lakehouse-lab/open-data-lakehouse-lab.github.io',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Open Data Lakehouse Lab. Built with Docusaurus.`,
      },
      prism: {
        theme: githubThemes.github,
        darkTheme: draculaThemes.dracula,
      },
    }),
};

export default config;
