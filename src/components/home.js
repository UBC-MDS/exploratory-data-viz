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
                                <h1 className={classes.subtitle}><center>Exploratory Data Visualization</center></h1>
                            <div className={classes.introduction}>
                                
                                        <p>
                                        <center>
                                        Welcome to Data Visualization! This course is part of the  <u><strong><a href="https://extendedlearning.ubc.ca/programs/key-capabilities-data-science">Key Capabilities for Data Science program</a></strong></u> and covers topics related to data visualization.
                                        </center>
                                         </p>
                                         <p> 
                                         <center>
 In this course we will learn how to (and how not to) visualize data. We will learn about visualization grammar and how it's implemented in the "Altair" package to create our figures. In addition to common statistical visualizations, we will learn how to tell stories with data, create geographical visualizations, and bring out plots to life by adding interactive elements. Together, these skills will allow us to create effective data visualizations that strengthen our own exploratory data analysis skills and our ability to communicate insights to others.
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
