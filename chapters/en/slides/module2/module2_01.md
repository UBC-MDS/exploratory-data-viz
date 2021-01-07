---
type: slides
---

# Effective Use of Visual Channels

Notes: So far we have seen how to use points and lines to represent data
visually. In this lecture, we will see how we can also use areas and
bars for this purpose. Before we dive in to the code, let’s discuss how
different visual channels, such as position, area, etc, can impact how
easy it is for us to accurately interpret the plotted data.

As in many cases, an efficient way to learn this topic is through
personal experience. Please follow along in the exercises on the next
two slides to see which visual channels you find the most effective.

---

## Comparing sizes is easier for some geometrical objects than for others

![](/module2/circle-comparison.png)

Notes: In the image in this slide, try to estimate how many times larger
the big circle is compared to the small one.

---

## Comparing sizes is easier for some geometrical objects than for others

![](/module2/bar-comparison.png)

Notes: In the image in this slide, try to estimate how many times larger
the big bar is compared to the small one.

---

## Both the circles and rectangles differ by 7x

<img src="/module2/7x.png" style="width:60.0%" />

Notes: In both cases the answer is seven times bigger. Even if you
guessed both of these exactly correct, most people find it is much
easier to compare the length or position of the bars rather than the
area of the circles. For the circles, you might even have hesitated at
exactly what to compare when we said “how many time *larger*”, were you
supposed to compare the area or the diameter? This is less ambiguous for
bars as long as their widths are kept the same.

This is important to keep in mind, especially when communicating to
others via visualization, but also when creating plots for yourself.
These two examples are originally from [Jeffrey Heer’s PyData
talk](https://www.youtube.com/watch?v=hsfWtPH2kDg), who is visualization
researcher at the university of Washington and whose research group
created D3 and VegaLite (which Altair is based on).

---

## Summary of visual channel efficiency

<img src="/module2/visual-channels-rank.png" style="width:80.0%" />

Notes: Even if you got both these right yourself, the fact that many
people prefer one over the other means that in order for you to create
effective visualizations you need to know which visual channels are the
easiest for humans to decode. Luckily, there has been plenty of research
in this area, which can be summarizes in the schematic on this slide.

Position is by far the best and therefore we should put our most
important comparison there. Using position often means that we can’t use
other things such as length or angle (like the angle in a pie chart),
but we can add size or color to represent other relationships. Even if
it is hard to tell exact information from these (is this color/dot 2x
darker/bigger than another?) they are good to give and idea of trends in
the data (are these dots darker/bigger than the others?

---

## Don’t use 3D without a good reason

### Unnecessary 3D makes plot interpretation harder

![](/module2/bad-3d-barchart.png)

Notes: The biggest issues with using 3D is when it is used unnecessarily
(like a 3D bar or pie chart), as the only way to compare position (like
a 3D scatter plot), and when they are represented on a 2D medium like a
paper where they can’t be rotated. In this slide we see a 3D bar chart,
where it looks like the values of the bars are around A=0.7, B=1.7,
C=2.7 and D=3.7. However, this is only because of the angle of the
camera in the plot, the actual values here of A, B, C, and D are
actually 1, 2, 3, and 4, respectively.

---

## Meaningful 3D can facilitate plot interpretation

![](https://media.github.ubc.ca/user/1751/files/da4e1b00-0fd3-11eb-940d-0b06a28a0186)

Notes: Sometimes 3D can be useful, like a topographical map or a protein
folding visualization. But be cautious, we saw above that even in
naturally 3D systems like blood vessels it is still mentally more
complex when they are 3D. [Claus Wilke’s has a good
chapter](https://clauswilke.com/dataviz/no-3d.html) on this if you are
interested to read more.

There is also some [interesting work done with the Rayshader
library](https://www.tylermw.com/3d-ggplots-with-rayshader/) that maps
3D in an intuitive way and incorporates reasonable camera rotation
around the objects. This slide contains is an example of visualizing the
bend in space time via the 3D depth channel, eliminating the need for an
additional 2D plot.

---

## Properly designed visualizations help saving lives

![](/module2/blood-vessels-40.png)

Notes: How much these best practices actually matters might be a bit
abstract until you gain personal experience from it, Therefore, I want
to include a concrete example of how changing visualization method
improved an important clinical outcome.

Heart disease is the most common cause of death, yearly killing almost 9
million people, or as many as diabetes, dementia, neonatal conditions
respiratory infections all together. By detecting regions of low shear
stress in the arteries around the heart, doctors are able to identify
patients that are on their way to develop heart disease and take action
early to improve the patient’s survival chances. To evaluate the shear
stress in the arteries, the regular practice is to use a digital 3D
representation of the artery colored according to the amount of sheer
stress which is what you can see in this picture. The colormap changes
from blue for the areas of interest (low stress) to cyan, green, yellow,
and red for higher stress.

A few years ago, a research group set out to test how effective this
type of visualization was compared to a couple of alternatives. When
using the visualization you see in this slide, about 40% of the areas of
low shear stress were correctly identified by doctors.

---

## Changing the color scale almost doubled the accuracy

![](/module2/blood-vessels-70.png)

Notes: The first thing this research group tested was the effect of
testing the color scale to one that is easier to interpret and makes the
important areas of low shear stress stand out more, since they are
highlighted in a bright red color, and the rest are in black and white.
By this seemingly small modification, they identified that the
percentage of correct analysis almost doubled, from 40% to 70%. We will
talk more about choosing correct color scales at the later modules of
this course.

---

## Changing from 3D to 2D improved the further accuracy

![](/module2/blood-vessels-90.png)

Notes: The next modification the researcher tested was to change from a
3D representation of the blood vessels to a 2D representation. Although
a 3D representation is more anatomically correct here, it is also more
cognitively demanding for us to process, and some areas can cover others
so it is harder to get a quick overview of the vessels. In the 2D
visualization, the blood vessels and their branching points are shown in
a schematic that is less cognitively demanding to interpret. This
representation was also shown to be more effective, as 90% of the low
shear stress areas were now correctly identified.

Overall, these two tweaks more than doubled the outcome accuracy, from
40% to 90%. A huge increase from modification that might have seemed to
be a mere matter of taste unless you knew visualization theory! So, if
anyone tells you that visualization of data is not as important as other
components, you can tell them about this study and ask them what kind of
visualization they want their doctor to look at when analysing their
arteries.

---

# Let’s apply what we learned!

Notes: <br>
