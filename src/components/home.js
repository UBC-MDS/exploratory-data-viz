import React from 'react'
import { graphql, StaticQuery } from 'gatsby'

import Layout from './layout'
import { Link } from './link'
import Logo from '../../static/logo.svg'

import classes from '../styles/index.module.sass'

export default ({ lang = 'en' }) => {
    return (
        <StaticQuery
            query={query}
            render={data => {
                const chapters = data.allMarkdownRemark.edges
                    .filter(({ node }) => node.fields.lang === lang)
                    .map(({ node }) => ({
                        slug: node.fields.slug,
                        title: node.frontmatter.title,
                        description: node.frontmatter.description,
                    }))
                return (
                    <Layout isHome lang={lang}>
                        <Logo className={classes.logo} />
                        <section>
                                <h1 className={classes.subtitle}><center>Introduction to Machine Learning</center></h1>
                            <div className={classes.introduction}>
                                
                                        <p>
                                        <center>
                                        Welcome to Introduction to Machine Learning!
                                        This course is part of the  <u><strong><a href="https://extendedlearning.ubc.ca/programs/key-capabilities-data-science">Key Capabilities for Data Science program</a></strong></u> and covers topics related to machine learning; a topic  closely related to artificial intelligence (AI), data science, and statistics.
                                        This course covers the data science perspective on the introductory concepts in machine learning, with a focus on making predictions.
                                        Not only does it cover different models such as K-NN, decision trees and linear classifiers, but it also tackles important concepts needed to prepare and preprocess data before building them. 
                                        No course would be complete without knowing how to read the results. We cover different ways to evaluate your model and when to question your results. 
                                        Finally, we show you how to streamline the entire process by implementing pipelines in your workflow. 
                                        </center>
                                        </p>
                                        <p>
                                        <strong>Course prerequisites:</strong>  <u><a href="https://prog-learn.mds.ubc.ca/">Programming in Python for Data Science</a></u> 
                        </p>
                             </div>
                    </section>
                        {chapters.map(({ slug, title, description }) => (
                            <section key={slug} className={classes.chapter}>
                                <h2 className={classes.chapterTitle}>
                                    <Link hidden to={slug}>
                                        {title}
                                    </Link>
                                </h2>
                                <p className={classes.chapterDesc}>
                                    <Link hidden to={slug}>
                                        {description}
                                    </Link>
                                </p>
                            </section>
                        ))}
                    </Layout>
                )
            }}
        />
    )
}

const query = graphql`
    {
        allMarkdownRemark(
            sort: { fields: [frontmatter___title], order: ASC }
            filter: { frontmatter: { type: { eq: "chapter" } } }
        ) {
            edges {
                node {
                    fields {
                        slug
                        lang
                    }
                    frontmatter {
                        title
                        description
                    }
                }
            }
        }
    }
`
