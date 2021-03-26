---
type: slides
---

# Telling stories with visualizations

Notes: In this module we will see how we can add a narrative to our
visualizations. Together, our narrative and our visualizations will tell
a data story.

This does not mean that we will be making up fairy tales about our data,
but that we will guide the reader through the most important insights
that we have found.

---

## How to tell a data story

-   Peak your audience’s interest
-   Make the reader curious about the next figure
-   Present facts in an engaging way without hyperbole
-   Tailor it to the audience you have in mind

Notes: An effective story often peaks the readers’ interest up front,
and makes them want to learn more. To do this, we could start with a
striking figure, an important problem that begs for a solution, or
reveal data that challenges the reader’s previous knowledge.

When making a data story exciting it is important that is remains based
in fact. We do not want our story to resemble headlines of a clickbait
article.

When telling a story, it is also important to tailor it to the audience
and context. This ensures that it is of the right technical difficulty
and detail.

To practice storytelling, we will explore an [example based on articles
on deforestation from Our World in
Data](https://ourworldindata.org/forests-and-deforestation).

---

## A tail of global deforestation

``` python
import pandas as pd
import altair as alt

forest_loss = pd.read_csv('data/global-forest-loss.csv', parse_dates=['decade'])
title = 'Forest loss is still increasing rapidly world wide'
alt.Chart(forest_loss, title=title).mark_line().encode(
    alt.X('decade', title=''),
    alt.Y('cumulative_hectar_lost_millions',
            title='Cumulative lost forest area (million ha)'))
```

<iframe src="/module6/charts/01/unnamed-chunk-1.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: As we can see in this slide, the total global forest loss during
the last 300 years is about 1.5 billion hectares. That’s almost twice
the area of Australia!

To put this into a historical perspective the world has lost 1/6 of its
forest in the last 100 years, which is as much as in the previous 9000
years combined.

Although we can see that global deforestation has been slowing down
since the 1980s, it is still progressing at an unsustainable rate.

95% of the deforestation today occurs in tropical regions. This is
particularly alarming given that trees in the tropical rain forests are
not easily replaced after they are cut down.

---

## Half of the tropical deforestation is localized to only two countries

``` python
top_deforestation_regions = pd.read_csv('data/region-share-tropical-deforestation.csv')
title = 'Brazil and Indonesia account for almost half of global deforestation'
alt.Chart(top_deforestation_regions, title=title).mark_bar().encode(
    x='Share of commodity-driven deforestation (%)',
    y=alt.Y('Region', title='', sort='x'))
```

<iframe src="/module6/charts/01/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Permanent loss of forest (or “deforestation”) is a big problem
that leads to species extinction, land erosion, and accelerates climate
change.

Although the consequences of deforestation are of global impact, we can
see in this chart that forest loss is not evenly distributed across the
world.

In particular, Brazil and Indonesia stand. These the two countries
account for roughly half of the commodity-driven deforestation around
the world.

Notably, this chart only shows deforestation that is driven by
commodities, such as the need for new pastures for cattle or fields to
grow crops, but this accounts for most of the tropical deforestation.

It would be easy to jump to conclusions upon seeing a chart like this
and only blame the countries with high local deforestation rates, but it
that really fair?

How much of this deforestation is really driven by local needs? And how
much is due to exports to other countries?

---

## A large part of deforestation is driven by exported commodities

``` python
deforestation_exported = pd.read_csv('data/share-deforestation-exported.csv', parse_dates=['Year'])
title = 'Exported commodities contribute heavily to deforestation'
alt.Chart(deforestation_exported, title=title).mark_line().encode(
    alt.X('Year', title=''),
    alt.Y('share_deforestation_exported', title='Exported deforestation (%)'),
    color='Region')
```

<iframe src="/module6/charts/01/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: This chart shows the percentage share of deforestation that is
due to exported goods from 2005 to 2013 for Brazil and Indonesia.

As we can see, a large part of the deforestation in both countries is
driven by the demand from other countries. This is most striking in
Indonesia, where the materials from around half the country’s
deforestation ends up in exported goods.

So far, this story has shown us that global forest areas are at an all
time low and likely still shrinking. Much of the deforestation appears
to be localized to just a few countries, yet it is driven by global
demands for forest products.

This could be the end of our story if the main narrative we want to
communicate is that deforestation is truly a global problem that needs
to be solved through international collaborations.

However, our story seems to leave some questions unanswered that our
audience will likely be asking, such as which are the commodities that
drive most of the deforestation? Given that we have data to answer this
question, let’s not end our story here!

---

## Demand for beef is the biggest reason for deforestation in Brazil

``` python
brazil_drivers = pd.read_csv('data/drivers-deforestation_2003-2013_brazil.csv')
title = 'Cattle pasture was the biggest deforestation driver in Brazil 2003-2013'
alt.Chart(brazil_drivers, title=title).mark_bar().encode(
    alt.X('deforestation_hectares', title='Deforested area (ha)'),
    alt.Y('driver', title='', sort='x'))
```

<iframe src="/module6/charts/01/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: This slide shows the biggest drivers of deforestation in Brazil
between the years 2003 and 2013.

We can see that loss of forest is dominated by the demand for beef,
which leads to permanent clearing of forest to create pastures for
cattle grazing.

There is also a smaller contributions from small scale clearings, fires,
and commercial crops. Small scale clearings results in land used for
combination of purposes such as residencies, orchards, croplands, and
pastures.

Importantly, our data does not contain information about how much of
each commodity is due to demand outside Brazil, so we should refrain
from drawing conclusions about this. However, export data for each
commodity would be useful data to collect next if we were aiming to
explore our story in this direction.

Although beef is the major contributor to rain forest deforestation, it
could be the case that our demand for more food has simply increased and
cattle herds are an effective use of land to create food for human
consumption. Let’s flip to the next slide to find out!

---

## Beef is highly inefficient use of land to generate calories

``` python
land_use = pd.read_csv('data/land-use-per-kcal.csv')
title = 'Beef require the most land per 1000 kcal of food generated'
alt.Chart(land_use, title=title).mark_bar().encode(
    alt.X('Land use per 1000kcal (m2)'),
    alt.Y('Commodity', sort='x', title=''))
```

<iframe src="/module6/charts/01/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: The plot in this slide reveals that raising cattle for the
purpose of beef production is one of the most inefficient ways to
produce food for human consumption.

Armed with this knowledge (and the data to back it up), we could suggest
that one way to decrease deforestation in Brazil may be to decrease the
global demand for beef, while increasing the demand for other
protein-rich foods that can be grown in Brazil in a more efficient way.

Together with the large demand for beef products this inefficient use of
land creates an unfortunate situation in Brazil where a lot of tropical
forest is being cut down to make room for new pastures.

When telling a story, it is important to not jump to conclusions or
suggest that solutions to problems are simpler than what they might
really be.

So far we have seen that beef is a major contributing factor to
deforestation in Brazil, but there are many more aspect of the food
production chain that we have not considered.

Changing beef for other products could be highly beneficial, but it
could also be challenging and costly up front to implement. In telling
this story, it would be important to also include these uncertainties
and potential challenges.

Let’s continue our story by looking at the same breakdown for Indonesia,
is beef production the biggest issue there as well?

---

## Palm oil is the biggest contributor to deforestation in Indonesia

``` python
indonesia_drivers = pd.read_csv('data/drivers-deforestation_2003-2013_indonesia.csv')
title = 'Palm oil was the biggest contribtutor in Indonesia 2003-2013' 
alt.Chart(indonesia_drivers, title=title).mark_bar().encode(
    alt.X('deforestation_hectares', title='Deforested area (ha)'),
    alt.Y('driver', title='', sort='x'))
```

<iframe src="/module6/charts/01/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: This slide shows the biggest drivers of deforestation in
Indonesia between the years 2003 and 2013.

Here, we see that most of the deforested land in Indonesia is used for
palm oil plantations. Much of deforested land is also used for small
scale clearings, timber plantations, and grasslands. Again, it is
important to remember that we don’t have the data for how much of each
commodity is exported, so we can make claims about this.

Perhaps you have have read or heard negative things about palm oil in
the past? It has been of focus of late in the media, due to its link to
tropical deforestation.

From this chart alone, we might want to recommend that decreasing palm
oil production might be a good intervention to reduce deforestation in
Indonesia.

However, if this were to be done, we would need another oil crop would
need to take its place to keep up with the world’s demand for vegetable
oils.

Let’s explore how efficient palm oil and its alternatives are when it
comes to land use versus yield.

---

## Palm oil is the most efficient use of land for vegetable oil production

``` python
oil_land_use = pd.read_csv('data/area-land-needed-to-global-oil.csv')
title = 'Palm trees are a the most efficient oil crop'
alt.Chart(oil_land_use, title=title).mark_bar().encode(
    alt.Y('Commodity', title='', sort='x'),
    alt.X('Area needed to meet global vegetable oil demand (ha)'))
```

<iframe src="/module6/charts/01/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: This chart shows how many hectares would be needed for the crops
of common vegetable oils to meet the entire world’s oil demands.

It turns out that palm oil is the most efficient use of land for the
amount of oil produced! For example, if we wanted to replace it with
olive oil, we would need almost 10x the land to do so!

So does it make sense for Indonesia to keep clearing forests and
creating more palm plantations because they are the most efficient oil
crop?

No, our conclusions cannot stop here. Things are not so simple. The type
of land where the oil crop grows also matters.

Replacing tropical forests containing rich biodiversity with palm oil
plantations has a more severe, negative impact on the environment
compared to changing the type of oil crops being grown on land that has
already been deforested and used for agriculture elsewhere in the world.

Therefore it is important that palm oil plantages are grown in a
sustainable way that is compatible with preserving the tropical forests
in Indonesia.

Just as with Brazil and it’s use of pasture from deforested land to
raise cattle for beef, the story of palm oil is more complex then we can
illustrate in a single visualization.

---

## Summary and recap

-   Peak your audience’s interest
-   Make the reader curious about the next figure
-   Present facts in an engaging way without hyperbole
-   Tailor it to the audience you have in mind

Notes: This slide recaps the main points about how to tell an effective
story.

When writing a data narrative, it can be effective to summarize what you
have said in the end. This doesn’t have to involve showing the plots
again, and you could choose to highlight some of the key messages in
text.

Our story of deforestation drivers in Indonesia and Brazil has informed
our audience about the main reasons why tropical forests are being cut
down today.

We tried peaking the reader’s interest by illustrating the scale of the
problem in the beginning and then delved deeper into both areas that
have been completely new to them and topics they might have read about
previously.

We also made sure to state any caveats where our visualizations did not
intend to reveal the full complexity of the situation, but highlight a
few main findings.

If we evoked **your** curiosity and you want to learn more about this
topic, you can [visit this article about deforestation drivers from Our
World in Data](https://ourworldindata.org/drivers-of-deforestation),
which also reviews the latest research in this topic.

---

# Let’s apply what we learned

<br>
