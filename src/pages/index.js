import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header style={{padding: '4rem 0', textAlign: 'center', background: 'var(--ifm-color-primary)', color: 'white'}}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div style={{display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '1rem', marginTop: '2rem'}}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/introduction/overview">
            Get Started
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="Personal open-source laboratory for building a multi-cloud open data lakehouse.">
      <HomepageHeader />
      <main>
        <section style={{padding: '3rem 0'}}>
          <div className="container">
            <div className="row">
              <div className="col col--4">
                <h3>Multi-Cloud</h3>
                <p>Explore data patterns across Azure, AWS, and GCP using local emulators.</p>
              </div>
              <div className="col col--4">
                <h3>Open Standards</h3>
                <p>Built with open data formats and industry-standard protocols.</p>
              </div>
              <div className="col col--4">
                <h3>Infrastructure as Code</h3>
                <p>Reproducible environments using modern IaC tools.</p>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
