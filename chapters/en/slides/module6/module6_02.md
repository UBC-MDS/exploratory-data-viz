---
type: slides
---

# Visualizing Geographic Data

Notes: In this module we will see how we can plot maps with Altair, both
as single color backgrounds and by linking values to different countries
and states on the maps.

---

## Geographical file formats

``` json
// This truncated example does not contain all border coordinates for Colorado
{
  "type": "Feature",
  "id": 8,
  "properties": {"name": "Colorado"},
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [[-106.32056285448942,40.998675790862656],[-106.19134826714341,40.99813863734313],
       [-105.27607827344248,40.99813863734313],[-104.9422739227986,40.99813863734313],
       [-104.05212898774828,41.00136155846029],[-103.57475287338661,41.00189871197981],
       [-106.32056285448942,40.998675790862656]]
    ]
  }
}
```

Notes: Up until now, all the data we have plotted in Altair have been
read from CSV-file as tidy dataframes. To visualize data on maps we will
be using file formats that are designed specifically for geographic
data.

These are called GeoJSON and TopoJSON and are saved as plain text file,
but with rules for how store geographic data such as coordinates. You
can see an example of how they look in this slide.

---

## Creating a map in Altair

``` python
import altair as alt
from vega_datasets import data

world_map = alt.topo_feature(data.world_110m.url, 'countries')
alt.Chart(world_map).mark_geoshape()
```

<iframe src="/module6/charts/02/unnamed-chunk-1.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: The vega sample data sets contain a TopoJSON dataset for the
world and the US, so let’s use that here.

Altair work directly with GeoJSON files, so to use the TopoJSON sample
data, we use the `alt.topo_feature` help function so that Altair can
read the TopoJSON file correctly.

We then use `mark_geoshape` to visualize this geographic TopoJSON data
in the form of a map. Since the data contains the border coordinates of
each country, we can see these drawn as white lines in the chart on this
slide.

But why does Antarctica look so much bigger than the rest of the world?

---

## Changing the projection gives a more accurate representation of areas

``` python
alt.Chart(world_map).mark_geoshape().project(type='equalEarth')
```

<iframe src="/module6/charts/02/unnamed-chunk-2.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: Since the Earth is a sphere it is not entirely straightforward
how to represent the areas of the different parts of the world on a 2D
visualization.

The reason Antarctica looked so giant in the previous slide is because
of how the spheres is being stretched when it is projected onto a 2D
surface.

The default projection method for maps is often `mercator`, but it
causes heavy distortion of the relative areas of land masses, which get
worse the closer to the poles we come.

Fortunately, many people are moving away from using the projection
because it gives an incorrect impression of how the world looks. A
commonly used alternative is the `equalEarth` projection, which focuses
on correctly representing the relative areas of all landmasses.

Some of the most noticeable differences in this projection are that
Africa appears much bigger and Greenland, Antarctica and Russia appear
notably smaller. Africa is in fact 15x the area of Greenland, far from
the `mercator` projection which shows them as roughly the same size.

---

## The fill and border colors of countries can be changed

``` python
alt.Chart(world_map).mark_geoshape(
    color='black', stroke='#706545', strokeWidth=1
).project(type='equalEarth')
```

<iframe src="/module6/charts/02/unnamed-chunk-3.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: We can change the color of both the filled are and the border for
each country. Just like with other colors in Altair, we can use either a
named color or and exact hex-code.

Here we also make the stroke width slightly larger so that it is easier
to see the country borders.

---

## We can zoom and pan the map

``` python
alt.Chart(world_map).mark_geoshape(
    color='#2a1d0c', stroke='#706545', strokeWidth=0.5
).project(type='equalEarth', scale=500, translate=[140, 610])
```

<iframe src="/module6/charts/02/unnamed-chunk-4.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: By default Altair automatically adjusts the projection so that
all the data fits within the width and height of the chart.

We can change this via the projections parameters `scale` (zoom level)
and `translate` (panning). Here we adjust them to zoom in and center the
map on Europe. Getting the panning right when zooming in can take a bit
of fiddling.

---

## Working with individual countries can show regional details

``` python
state_map = alt.topo_feature(data.us_10m.url, 'states')
alt.Chart(state_map).mark_geoshape().project(type='equalEarth')
```

<iframe src="/module6/charts/02/unnamed-chunk-5.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: If we want information on regions within a country, we have to
use a geo/topojson file that contains this info. There is already one in
the vega demo datasets for the US, which is the one we are using here.

The loading of the data is exactly the same as previously, but as you
can see, the `equalEarth` projection is not very suitable for a single
country.

The US it is very small and both Alaska and Hawaii are shown far away
from the rest of the country.

---

## There are special projections for some countries such as the US

``` python
alt.Chart(state_map).mark_geoshape().project(type='albersUsa')
```

<iframe src="/module6/charts/02/unnamed-chunk-6.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: There special US projection `albersUsa` is much preferred when
only showing this country. You might recognize the projection from maps
that you have seen elsewhere such as on the news. Characteristic is the
placement of Alaska and Hawaii close to the rest of the country.

---

## Coloring individual regions differently

``` python
(alt.Chart(state_map).mark_geoshape().encode(
    color='id:Q')
.project(type='albersUsa'))
```

<iframe src="/module6/charts/02/unnamed-chunk-7.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: So far we have seen how to visualize region in a uniform color,
but often we want to use color to represent amounts within regions so
that we can contrast them with each other. How can we do this in Altair?

As you can see in this slide, we can use `encode` together with
`mark_geojson`, the same way we have used it with the other marks. This
type of visualization can be thought of as a geographical heatmap and is
often referred to as a “choropleth map”.

The `'id'` field here comes from the sample topojson file. If we opened
up and looked at this file, we would find that it does contains a field
called `'id'`, which is a numerical identifier for each state in
alphabetical order.

Because we are not using a pandas dataframe, we mush specify the type of
data in the column. Here we are specifying it a quantitative for
demonstration purposes because the legend would become very long if we
specified it as ordinal or nominal.

---

## Visualizing data from another dataframe on a map

``` python
import pandas as pd

state_pop = pd.read_csv('data/us_population_and_coordinates.csv')
state_pop[:5]
```

```out
        state  id  population  latitude  longitude
0     Alabama   1     4863300   32.7794   -86.8287
1      Alaska   2      741894   64.0685  -152.2782
2     Arizona   4     6931071   34.2744  -111.6602
3    Arkansas   5     2988248   34.8938   -92.4426
4  California   6    39250017   37.1841  -119.4696
```

Notes: So far we have learned how to visualize maps, but we haven’t
really been able to ask and answer any data question.

Although any arbitrary information could be put in a geojson file, they
often only contain spatial coordinates and we need to link any variables
of interest from another data set together with the JSON file.

For example, we might have this table with the population for each
state. So how do we link these two tables together?

---

## Linking datasets together via lookups

``` python
(alt.Chart(state_map).mark_geoshape().transform_lookup(
    lookup='id',
    from_=alt.LookupData(state_pop, 'id', ['population']))
.encode(color='population:Q')
.project(type='albersUsa'))
```

<iframe src="/module6/charts/02/unnamed-chunk-9.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: We could perform the linkage manually, by adding the relevant
fields to the json file, but this would be a tedious process.

There are some libraries, such as geopandas which can ameliorate this
situation, but we could also use Altair directly to save time.

To link two datasets together, Altair uses the `transform_lookup` method
to *look up* the data column we want to use from the dataframe via a
shared key column and add it to the plotted data. This process is
similar to using `merge` in pandas.

You could see in the previous slide that there exists an ID column and
this contain the state IDs in alphabetical order, just like the geojson
so we can use that for the lookup.

The columns we want to fetch from the dataframe are passed in a list,
and here we have specified only the population, which we use to color
the states accordingly to how many people live in each state.

---

## Choropleths can be misleading since the area of each region matters

``` python
us_map = (alt.Chart(state_map).mark_geoshape(color='lightgray', stroke='white')
          .project(type='albersUsa'))
points = alt.Chart(state_pop).mark_circle().encode(
    longitude='longitude',
    latitude='latitude',
    size='population')
(us_map + points).configure_view(stroke=None)
```

<iframe src="/module6/charts/02/unnamed-chunk-10.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: One drawback with choropleth maps is that they rely on the area
of each region, even if it is unrelated to the measure we are studying.

For example, just because the states in the midwest of the US have a
large area, they are very prominent in the choropleth map we made on the
last slide although their population is actually really small.

On the other hand, if there was a state that had a small area, but a
large population, we would not see it in the choropleth map. These
issues are often discussed around the US election, where different
approach are used to illustrate that the weight of each states vote is
not tied to the area of the state.

On effective way to convey this message is to use a map as a background
and plot points on top that are scaled according to the measure of
interest.

To achieve this in Altair, we need one pair of coordinates to plot for
each state, which we have in the column `latitude` and `longitude`
(these represent the geometric center of each state).

We then plot these coordinates on top of a map using the special
`longitude` and `latitude` parameters and set the size of the points to
be relative the population parameter.

Finally, we remove the square grey outline by setting the stroke to
`None`.

Now it is much easier to see that many of the states in Eastern USA have
a population several times that in the Midwest, although their area is
smaller.

---

# Let’s apply what we learned!

Notes: <br>
