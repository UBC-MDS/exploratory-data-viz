---
type: slides
---

<!-- #region -->

# Telling stories with visualizations

Notes: In this module we will see how we can add a narrative to our
visualizations. Together, our narrative and our visualizations will be
telling a data story. This does not mean that we will be making up fairy
tales about our data but that we will guide the reader through the most
important insights that we have found.

---

## How to tell a story

-   Start with an have a hook
-   explain
-   Leave the reader curios about the next fig

Notes: An effective story often peaks the readers’ interest up front,
and makes them interested in reading further. For example, we could
start with a visually striking figure, an important problem that begs
for a solution, or reveal data that challenges the reader’s previous
knowledge.

When making a data story exciting it is important to still remain
fact-based to avoid that our story comes across as the headlines of a
clickbait article.

When telling a story, it is also important to tailor it to the audience
and context to ensure that it is of the right technical difficulty and
detail.

To practice storytelling, we will show an [example based on articles on
deforestation from Our World in
Data](https://ourworldindata.org/forests-and-deforestation).

---

## A tail of global deforestation

<!-- #endregion -->

``` python
import pandas as pd
import altair as alt

# TODO save wrangled data and change to area plot shoing both tropical and temperate deforestation
forest_loss = pd.read_csv('data/global-forest-loss.csv', parse_dates=['decade'])
forest_loss['cumulative_hectar_lost_millions'] = forest_loss['hectar_lost_millions'].cumsum()

alt.Chart(forest_loss).mark_line().encode(
    x='decade',
    y=alt.Y('cumulative_hectar_lost_millions'))
```

<iframe src="/module6/charts/01/unnamed-chunk-1.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: As we can see in this slide the total forest loss during the last
300 years is about 1.5 billion hectare. That’s almost twice the area of
Australia!

To put this into a historical perspective the world has lost 1/6 of its
forest in the last 100 years, which is as much as in the previous 9000
years combined.

Although we can see that global deforestation has been slowing down
since the 80s, it is still progressing at an unsustainable rate.

Of the deforestation today, 95% occurs in tropical regions, which is
particularly severe since old rain forests are not easily replaced after
they are cut down.

---

## Half of the tropical deforestation is localized to only two countries

``` python
deforestation_regions = pd.read_csv('data/region-share-tropical-deforestation.csv')
alt.Chart(deforestation_regions).mark_bar().encode(
    x='Share of commodity-driven deforestation',
    y=alt.Y('Entity', title='', sort='x'))
```

<iframe src="/module6/charts/01/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Permanent loss of forest (or “deforestation”) is a big problem
that leads to species extinction, land erosion, and accelerates climate
change.

Although the consequences of deforestation has global consequences, we
can see in this chart that forest loss is not evenly distributed across
the world.

In particular, Brazil and Indonesia stand out as the two countries
account for about half of the commodity-driven deforestation around the
world.

Notably, the chart above only shows deforestation that is driven by
commodities, such as the need for new pastures for cattle or fields to
grow crops, but this accounts for most of the tropical deforestation.

It would be easy to jump to conclusions upon seeing a chart like this
and blaming the countries with high local deforestation rate, but it
that really fair?

How much of this deforestation is really driven by local needs versus
how much is due to exports to other countries?

---

## A large part of deforestation is driven by exported commodities

``` python
# TODO save wrangled data
deforestation_exported = pd.read_csv('data/share-deforestation-exported.csv', parse_dates=['Year']).query('Entity in ["Brazil", "Indonesia"]') 
alt.Chart(deforestation_exported).mark_line().encode(
    y='share_deforestation_exported',
    x=alt.Y('Year', title=''),
    color=alt.Color('Entity'))
```

<iframe src="/module6/charts/01/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: This chart shows the share of deforestation that is due to
exported goods from 2005 to 2013.

As we can see, a large part of the deforestation in both countries is
driven by other countries. Particularly in Indonesia, where around half
the country’s deforestation stems from interest outside Indonesia.

To recap, this story has shown us global forest areas are at an all time
low and still shrinking. And although much of the deforestation
localized to just a few countries, it is driven by global interests.

This could be the end of our story if the main aspect we wanted to
highlight was that much of deforestation is a global problem that needs
to be solved through international collaborations.

If we wanted to tell a longer story, we next as “Which are the
commodities that drive most of the deforestation?”, which is something
that the reader might already have in mind since the previous slide.
Let’s explore this next.

---

## Demand for beef is the biggest reason for deforestation in Brazil

``` python
# TODO save wrangled data
brazil_drivers = pd.read_csv('data/drivers-forest-loss-brazil-amazon.csv').query('Year > 2003')
brazil_drivers = brazil_drivers.melt(id_vars=['Entity', 'Code', 'Year'], var_name='type', value_name='deforestation_hectares').groupby('type').sum().reset_index()
alt.Chart(brazil_drivers).mark_bar().encode(
    x='deforestation_hectares',
    y=alt.Y('type', title='', sort='x'))
```

<iframe src="/module6/charts/01/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: This slide shows the biggest drivers of deforestation in Brazil
between the years 2003 and 2013.

We can see that loss of forest is dominated by the demand for beef,
which leads to permanent clearing of forest to create pastures for
cattle grazing.

There is also a smaller contributions from small scale clearings, fires,
and commercial crops.

Although beef is the major culprit in rain forest deforestation, it
could be the case that our demand for more food has simply increased and
cattle herds are an effective use of land to create food for human
consumption. Let’s flip to the next slide to find out!

---

## Beef is highly inefficient use of land to generate calories

``` python
# TODO save wrangled data
land_use = pd.read_csv('data/land-use-kcal-poore.csv').rename(columns={'Land use per 1000kcal (Poore & Nemecek, 2018)': 'Land use per 1000kcal (m2)'}).query('Entity in ["Barley", "Maize", "Rice", "Tofu (soybeans)", "Cassava", "Bananas", "Eggs", "Poultry Meat", "Dark Chocolate", "Milk", "Cheese", "Coffee", "Lamb & Mutton", "Beef (beef herd)"]')
alt.Chart(land_use).mark_bar().encode(
    alt.X('Land use per 1000kcal (m2)'),
    alt.Y('Entity', sort='x', title=''))
```

<iframe src="/module6/charts/01/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: The plot in this slide reveals that herding cattle for the
purpose of beef production is one of the most inefficient ways to
produce food for human consumption.

Together with the large demand for beef products this inefficient use of
land creates an unfortunate situation in Brazil where a lot of tropical
forest is being cut down to make room for new pastures.

When telling a story, it is important to not jump to conclusions or
suggest that solutions to problems are simpler than what they might
really be.

So far we have seen that beef is a major contributing factor to
deforestation in Brazil, but there are many more aspect of the food
production chain that we have not considered, such as the use of other
resources

Changing beef for other products would be highly beneficial, but how
achievable it is and what cost is associated with making the change we
don’t know from the data we have explored here.

Let’s continue our story by looking at the same breakdown for Indonesia,
is beef production the biggest issue there as well?

---

## Palm oil is the biggest contributor to deforestation in Indonesia

``` python
# TODO save wrangled data
indonesia_drivers = pd.read_csv('data/deforestation-drivers-indonesia.csv').query('2013 > Year > 2003').groupby('Entity').sum().reset_index()
alt.Chart(indonesia_drivers, title='Palm oil was the leading cause of deforestation between 2003 and 2013 in Indonesia').mark_bar().encode(
    x='deforestation_hectares',
    y=alt.Y('Entity', title='', sort='x'))
```

<iframe src="/module6/charts/01/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: This slide shows the biggest drivers of deforestation in
Indonesia between the years 2003 and 2013.

Here, it is palm oil that drives most of the deforestation, although
small scale clearings, timber plantation, and grasslands also contribute
substantially. You might have read many negative things about palm oil
already, as it has been in media’s focus due to its link to tropical
deforestation.

From this chart alone it surely seems that decreasing palm oil
production would lead to less deforestation.

But if palm oil production would decrease while the world’s demand for
vegetable oils remains constant, another oil crop would need to take its
place.

Similar to what we did for beef, let’s explore how efficient palm oil
and its alternatives are when it comes to land use versus yield.

---

## Palm oil is the most efficient use of land for vegetable oil production

``` python
oil_land_use = pd.read_csv('data/area-land-needed-to-global-oil.csv')
alt.Chart(oil_land_use).mark_bar().encode(
    alt.Y('Entity', title='', sort='x'),
    alt.X('Area needed to meet global vegetable oil demand (ha)'))
```

<iframe src="/module6/charts/01/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: This chart shows how many hectares would be needed for the crops
of common vegetable oils to meet the entire world’s oil demands.

It turns out that palm oil is the most efficient use of land for the
amount of oil produced! If we wanted to replace it with e.g. olive oil,
we would need almost 10x the land used.

Just as with beef, the story of palm oil is more complex that we can
show in a single visualization and it is not as easy as saying that we
should use palm oil solely based on the criteria of efficiency.

For example, the type of land where the oil crop grows matters.
Replacing tropical forests containing rich biodiversity with palm oil
plantages has a more severe impact than switching to other oil crops on
already cultivated land elsewhere in the world.

---

## Summary and recap

TODO Not a 100% of what to put in this slide, bullets points of the
transcript? Or maybe the bullets points from the first slide again.

Notes: When writing a data narrative, it can be effective to recap what
you have said in the end. This doesn’t have to involve showing the plots
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