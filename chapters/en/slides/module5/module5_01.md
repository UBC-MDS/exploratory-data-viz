---
type: slides
---

# Effective figures for communication

Notes: So far we have learned how to understand Altair’s visualization
grammar, how to create several different types of plots, and how to use
these when exploring data on our own.

In this module we will learn the principles of effective figure design
for communication and see how we can implement these using Altair.

---

## Figure design allows us to tell different stories from the same data

[From
Infoworld](https://www.infoworld.com/article/3088166/why-how-to-lie-with-statistics-did-us-a-disservice.html)

<center>
<img src="/module5/iraqs-bloody-toll.png" width="35%"></img>
</center>

Notes: When designing figures for presentation, we have the possibility
to tell different stories from the same underlying data.

On this slide, you can see an award winning figure describing the
“bloody toll” from the American war in Iraq. This figure has been
purposely designed to draw your attention to the blood-like red color
and the downward facing bars which brings up association with dripping
blood.

The title also clearly highlights the negative aspects of this data.

Now let’s look at another figure of the same data.

---

## Figure design allows us to tell different stories from the same data

[From
Infoworld](https://www.infoworld.com/article/3088166/why-how-to-lie-with-statistics-did-us-a-disservice.html)

<center>
<img src="/module5/iraq-death-on-the-decline.png" width="35%"></img>
</center>

Notes: This figure paints an entirely different picture of the event. It
focuses on the recent declining trend in deaths, uses a positive green
color, and has the bars facing upwards.

Both figures are correct and both use the same data, but they convey
starkly distinct messages.

This also serves to illustrate that understanding the principles behind
designing figures for communication does not only help you create
effective visualizations, it is also of great help when interpreting
figures made by others.

---

## Figure design should be adopted to the target audience and situation

[From Kieran Healy’s Data Visualization: A practical
introduction](https://socviz.co/lookatdata.html#lookatdata)

<center>
<img src="/module5/napoleon.png" width="85%"></img>
</center>

Notes: This is an elegant figure that goes into excquisite detail about
how Napoleon’s army gradually shrank in numbers as the march against the
Russian empire in the early 1800s.

The width of the line is the number of soldiers in the army and the
color represents whether the are marching against Moscow (gold/brown) or
retreating back to France (black). The bottom of the chart shows how the
temperature changed during the campaign.

It does take a few seconds to digest the graph when you first see it,
but once you have familiarized yourself with it, you appreciate how you
can see in detail the army progress as it moved through Europe.

This is a great visualization when the reader has time to sit down with
the plot for a while and when you believe your target audience will
appreciate this level of detail?

But what if you are presenting this as part of a slide deck in a board
meeting and only can spend a few seconds describing the plot? It would
likely be too complicated to digest and the take home message might be
lost.

---

## Figure design should be adopted to the target audience and situation

[From Kieran Healy’s Data Visualization: A practical
introduction](https://socviz.co/lookatdata.html#lookatdata)

<center>
<img src="/module5/napoleon-pie.png" width="50%"></img>
</center>

Notes: In the board meeting, this pie chart is likely more effective in
communicating the take home message: the Napolean army was decimated as
a result of this military campaign.

Although we said earlier in this course that we should generally avoid
using pie charts, here the information is simple enough that a pie chart
is very effective.

---

## Breaking an axis is often misleading

[From The
Economist](https://medium.economist.com/mistakes-weve-drawn-a-few-8cdd8a42d368)

<center>
<img src="/module5/broken-axis.png" width="70%"></img>
</center>

Notes: In this module we will also visit a few best practices in
visualization design and learn why they are effective.

We can see one of these on this slide. Breaking the value axis of a
chart can lead to that the differences between the values look much
bigger than they are.

In the left chart of this slide the value axis is broken resulting in
the top bar being only 1.5x longer than the second longest bar when the
difference is in fact more than 5x as can be seen in the right most
chart.

This example is from [an article in The Economist where they critique
their past visualization
mistakes](https://medium.economist.com/mistakes-weve-drawn-a-few-8cdd8a42d368),
which is an effective way to learn.

---

## Appropriate choice of colours makes visualizations much more effective

<iframe src="/module5/charts/lightness-vs-hues.html" width="100%" height="420px" style="border:none;">
</iframe>

Notes: On this slide we have represented the values of one of the
dataframe columns with different color combinations. Using the correct
color combination might at first seem like a matter of aesthetics rather
than an important part of data visualization, but it can have a profound
impact on how we interpret plots.

Without knowing the details of how the color combinations in this slide
were created or even what makes for a good combination of colors, we can
immediately see that it is easier to interpret the plot on the right.

Having the slight variation from light to dark blue is a more natural
mapping for a range of values compared to the wide array of different
colors used in the left plot.

We will learn why this is in a few slide decks!

---

## Descriptive figure and axis titles are critical for effective visualizations

<center>
<img src="/module5/iraqs-bloody-toll-without-title.png" width="35%"></img>
</center>

Notes: This is the same figure we showed on the first slide, but with
one small modification, can you see what it is?

What we have done is removed the title from the top of the figure. This
relatively small change makes the figure much less striking.

While the graphics still stand out, we’re not hit with a powerful
take-home message immediately when we look at the plot.

Even if our audience would have the time to study this figure in detail
and read all the text, it will likely not be as memorable without the
striking title.

Later in this module we will learn not just how to create effective
figure titles but also how to label our axes effectively.

---

# Let’s apply what we learned!

Notes: <br>
