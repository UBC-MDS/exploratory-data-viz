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

<center>
<img src="/module5/iraqs-bloody-toll.png" width="35%"></img>
</center>

<http://www.simonscarr.com/iraqs-bloody-toll>

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

<center>
<img src="/module5/iraq-death-on-the-decline.png" width="35%"></img>
</center>

<https://www.infoworld.com/article/3088166/why-how-to-lie-with-statistics-did-us-a-disservice.html>

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

<center>
<img src="/module5/napoleon.png" width="100%"></img>
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

<center>
<img src="/module5/napoleon-pie.png" width="50%"></img>
</center>

<https://socviz.co/lookatdata.html#lookatdata>

Notes: In the board meeting, this pie chart is likely more effective in
communicating the take home message: the Napolean army was decimated as
a result of this military campaign.

This infomation is simple enough that a pie is effective, but in general
we should be careful when using pie charts

---

## Including many categories in pie charts makes them hard to interpret

<center>
<img src="/module5/pie-bar-categories.png" width="70%"></img>
</center>

<https://github.com/glosophy/CatoDataVizGuidelines/blob/master/PocketStyleBook.pdf>

Notes: When there are too many categories in a pie chart, it becomes
difficult to compare them with each other. Both because the colors can
be hard to distinguish and because the angle and area of the pie slices
is not

In most cases, it is more effective to use position as the visual
channel to convey a comparison instead area and angle.

A bar chart is often a superior alternative to a pie chart, and when in
doubt chose the bar chart for counts, percentages, and proportions.

``` python
```

---

# Let’s apply what we learned!

Notes: <br>
