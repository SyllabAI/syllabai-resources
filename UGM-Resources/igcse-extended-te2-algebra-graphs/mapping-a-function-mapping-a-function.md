---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-functions/mapping-a-function
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-functions
- type/package-of-problems
- level/introducing
resource_identity:
  ugm_id: mapping-a-function
  station: thinking-about-functions
  station_title: Thinking about Functions
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Introducing
  ref: 7480
  old_site_id: null
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: thinking-about-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-functions
    validation_status: SUGGESTED
  spec_points:
  - code: E2.13.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Mapping diagrams to visualise functions — E2.13.1 register.
      rationale: 'Canonical UGM title: “Mapping a function”; exam provenance: This resource is based on
        ideas developed by [Martin Flashman](http://users.humboldt.edu/flashman/).'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: This resource is based on ideas developed by [Martin Flashman](http://users.humboldt.edu/flashman/).
task: T-UGM-IMPORT-19
assets:
- path: https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure8.svg
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure20.svg
  kind: figure
interactive:
- src: //www.geogebratube.org/material/iframe/id/VNy9ty37/width/600/height/493/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
- src: //www.geogebratube.org/material/iframe/id/yasPkSXz/width/600/height/493/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Mapping a function

> Excerpt: Students are introduced to using mapping diagrams as a way to visualise a function; this is developed in later resources to visualise derivatives and then to understand the chain rule.

## Warm-up

In this resource, we will explore linear functions and how they can be represented. This is interesting in its own right, and also gives us a tool to think about an important idea in calculus. We will take this further in [Mapping a derivative](https://undergroundmathematics.org/introducing-calculus/mapping-a-derivative).

Here are mapping diagrams representing functions of the form \(f(x)=ax+b\) for \(x\in\mathbb{R}\).

(In these diagrams, the left-hand numberline is the input and the right-hand one is the output, for example in Diagram 1, \(f(1)=3\).)

oh, there's no print-max-width option :-(

| > [figure: figure 1 is two parallel numberlines, left one centred on zero, right one centred on zero, both going up in steps of one, five arrows from left line to right line, from 0 to 0, from one half to 1.5, from 1 to 3, from minus one half to minus 1.5, from minus 1 to minus 3 — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure1.svg`] (image not included in the text import; path of record). Diagram 1 | > [figure: looks identical to figure 1 except now numberlines are renumbered: left one is centred at 2, right one is centred at 6, still going up in steps of one — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure2.svg`] (image not included in the text import; path of record). Diagram 2 | > [figure: looks identical to figure 1 except now numberlines are renumbered: left one is centred at 2, right one is centred at 6, both lines now go up in steps of 0.01 — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure3.svg`] (image not included in the text import; path of record). Diagram 3 |
| --- | --- | --- |
| > [figure: looks identical to figure 1 except now numberlines are renumbered: left one is centred at 2, right one is centred at 7, still going up in steps of one — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure4.svg`] (image not included in the text import; path of record). Diagram 4 | > [figure: looks identical to figure 1 except now numberlines are renumbered: left one is centred at 1, right one is centred at 1, still going up in steps of one — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure5.svg`] (image not included in the text import; path of record). Diagram 5 | > [figure: looks identical to figure 1 except now numberlines are renumbered: left one is centred at 1, right one is centred at 2, both lines now go up in steps of 0.1 — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure6.svg`] (image not included in the text import; path of record). Diagram 6 |

- What do you notice about these diagrams and the functions they represent? (You might find it helpful to work out some or all of the functions first.)
- What features do the diagrams and functions have in common? What are the differences between them?

## Warm-up ideas

Here are mapping diagrams representing six functions of the form \(f(x)=ax+b\) for \(x\in\mathbb{R}\).

(In these diagrams, the left-hand numberline is the input and the right-hand one is the output, for example in Diagram 1, \(f(1)=3\).)

| > [figure: diagram 1 is two parallel numberlines, left one centred on zero, right one centred on zero, both going up in steps of one, five arrows from left line to right line, from 0 to 0, from one half to 1.5, from 1 to 3, from minus one half to minus 1.5, from minus 1 to minus 3 — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure1.svg`] (image not included in the text import; path of record). Diagram 1 | > [figure: diagram 2: it looks identical to diagram 1 except now numberlines are renumbered: left one is centred at 2, right one is centred at 6, still going up in steps of one — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure2.svg`] (image not included in the text import; path of record). Diagram 2 | > [figure: diagram 3: it looks identical to diagram 1 except now numberlines are renumbered: left one is centred at 2, right one is centred at 6, both lines now go up in steps of 0.01 — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure3.svg`] (image not included in the text import; path of record). Diagram 3 |
| --- | --- | --- |
| > [figure: diagram 4: it looks identical to diagram 1 except now numberlines are renumbered: left one is centred at 2, right one is centred at 7, still going up in steps of one — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure4.svg`] (image not included in the text import; path of record). Diagram 4 | > [figure: diagram 5: it looks identical to diagram 1 except now numberlines are renumbered: left one is centred at 1, right one is centred at 1, still going up in steps of one — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure5.svg`] (image not included in the text import; path of record). Diagram 5 | > [figure: diagram 6: it looks identical to diagram 1 except now numberlines are renumbered: left one is centred at 1, right one is centred at 2, both lines now go up in steps of 0.1 — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure6.svg`] (image not included in the text import; path of record). Diagram 6 |

- What do you notice about these diagrams and the functions they represent? (You might find it helpful to work out some or all of the functions first.)
- What features do the diagrams and functions have in common? What are the differences between them?

Here are some features we noticed about these diagrams and functions.

- We notice that if we ignore the scales on the numberlines, all of the diagrams look identical.
- If we look at the scales, we notice that the scales on the input (left) and output (right) numberlines go up in the same step size as each other: in Diagrams 1, 2, 4 and 5, the step size is \(1\); in Diagram 6 the step size is \(0.1\), and in Diagram 3 the step size is \(0.01\).
- The middle arrow is horizontal in all of the diagrams.
- The function \(f(x)=ax+b\) represented by each diagram can be worked out either by observation or using algebra. For example, for Diagram 6: \[\begin{align*} f(1.0) &= 1.0a + b = 2.0\\ f(1.1) &= 1.1a + b = 2.3 \end{align*}\]  This gives us simultaneous equations for \(a\) and \(b\); subtracting these gives \(0.1a=0.3\), so \(a=3\) and then \(b=-1\). So \(f(x)=3x-1\).  The functions represented by each diagram are as follows:      Diagram 1   \(f(x)=3x\)     Diagram 2   \(f(x)=3x\)     Diagram 3   \(f(x)=3x\)     Diagram 4   \(f(x)=3x+1\)     Diagram 5   \(f(x)=3x-2\)     Diagram 6   \(f(x)=3x-1\)
- It is interesting to note that they are all of the form \(f(x)=3x+b\). The first three diagrams all representing the function \(f(x)=3x\) look the same except for their numberlines: they are centred in different places, and have different scales.  So we wonder: Does every mapping diagram of a function of the form \(f(x)=3x+b\) look the same, no matter what the scale is? If so, can you justify this? If not, can you find an example which is different?  We could do all sorts of things to modify the diagram, for example: draw the numberlines a different distance apart, not have the centre arrow horizonal, have different scales on the two numberlines, draw a different number of arrows, or draw the arrow start points a different distance apart. So when we think about this question, we will assume that we keep all of these things the same, and the only things we change are the choice of \(b\) and the scale on the numberlines.   **Solution**   Let’s draw a general mapping diagram for \(f(x)=3x+b\), and see what we observe. We centre the left numberline at \(c\), so the right numberline will be centred at \(3c+b\). We let the step size on the numberlines be \(s\), so the tick mark above \(c\) is at \(c+s\). This is what our mapping diagram now looks like, with just two arrows drawn for simplicity:  > [figure: two parallel numberlines, left one centred on c, with the mark above it at c plus s; the right one is centred on 3 c plus b, and there is are two arrows, one from c horizontally to 3 c plus b and one from c plus s to 3 times c plus s close bracket plus b — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure7.svg`] (image not included in the text import; path of record).  The non-horizontal arrow starts at \(c+s\) on the input numberline, which is one tick mark above \(c\), the start of the horizontal arrow. On the output numberline, the non-horizontal arrow ends at \(3(c+s)+b=(3c+b)+3s\), which is \(3s\) above the horizontal arrow, represented by three tick marks on the numberline. So this arrow always goes from one tick mark above the centre to three tick marks above, regardless of the choice of \(b\), \(c\) or \(s\), and so this arrow will always look the same. We can extend this argument to other arrows: instead of starting at \(c+s\), an arrow will start at \(c+ks\), which is \(k\) tick marks above the centre, and it will end at \((3c+b)+3ks\), which is \(3k\) tick marks above the centre. So the mapping diagram (when centred in this way) will always look the same.

## Problem

### Other multiples

In the [Warm-up](https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/), we looked at mapping diagrams for functions of the form \(f(x)=3x+b\).

We also used certain conventions when we drew those mapping diagrams, both to allow for fair comparison and to restrict the number of things we varied between the diagrams:

- the numberlines are a fixed distance apart
- the scales on the two numberlines are equal (so \(\quantity{1}{cm}\) represents the same difference on each numberline)
- the centre arrow is horizontal
- the arrow start points are a fixed distance apart

What would the mapping diagrams of other functions of the form \(f(x)=ax+b\) look like?

Using the same conventions, draw mapping diagrams for these functions. You can choose what your centre input value will be and what scale you will use.

- \(f(x)=2x+1\)
- \(f(x)=\frac{1}{2}x-1\)
- \(f(x)=x\)
- \(f(x)=-x\)
- \(f(x)=-2x+2\)
- another function of your choosing

What do you notice?

You can download [blank mapping diagrams](https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/assets/mapping-diagrams.pdf) or [small blank mapping diagrams](https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/assets/mapping-diagrams-small.pdf) for this.

### Extending the arrows

We could extend the arrows into straight lines, as shown here for \(f(x)=3x\), with just one arrow extended so far:

> [figure: two parallel numberlines, left one centred on zero, right one centred on zero, both going up in steps of one, five arrows from left line to right line, starting at minus 1, minus a half, zero, a half and one, with the arrow from a half to 1.5 extended in both directions beyond the numberlines — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure8.svg`] (image not included in the text import; path of record).

- What patterns do you notice when you extend the arrows for different linear functions?
- What does this tell you about the nature of linear functions?

You can explore this further using the first of the [interactivities](https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/interactivities).

#### A chance to reflect

How does this mapping diagram representation of a linear function \(f(x)=ax+b\) relate to the representation as the graph of \(y=ax+b\)?

- Which features of the function are clearer in one representation rather than the other?
- How are the features in one representation related to features in the other?

We have used several conventions in drawing our mapping diagrams. Many of them may seem sensible, but it is interesting to ask what would happen if we changed them. Possibly one of the most surprising conventions that we have used is to always make our centre arrow horizontal, by lining up the right-hand numberline appropriately.

How would things change if we did not require this? For example, what would \(f(x)=3x+1\) look like if we centred both numberlines at \(0\)? You can also explore this using the second of the [interactivities](https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/interactivities).

You may also like to ponder what would happen if we changed our other conventions.

**Taking it further: changing the conventions**

## Things you might have noticed

### Other multiples

What would the mapping diagrams of other functions of the form \(f(x)=ax+b\) look like?

Using the same conventions, draw mapping diagrams for these functions. You can choose what your centre input value will be and what scale you will use.

What do you notice?

Here are mapping diagrams of our original \(f(x)=3x\) together with the other functions given. We have decided to centre each of the input numberlines on zero and use a scale of one unit per tick mark; as we discovered in the Warm-up, this makes no difference to the mapping diagram, only to the labelling.

| > [figure: mapping diagram of f of x equals 3 x with five arrows starting at minus one up to one — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure1.svg`] (image not included in the text import; path of record). \(f(x)=3x\) | > [figure: mapping diagram of f of x equals 2 x plus 1 with five arrows starting at minus one up to one — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure9.svg`] (image not included in the text import; path of record). \(f(x)=2x+1\) | > [figure: mapping diagram of f of x equals half x minus 1 with five arrows starting at minus one up to one — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure10.svg`] (image not included in the text import; path of record). \(f(x)=\frac{1}{2}x-1\) |
| --- | --- | --- |
| > [figure: mapping diagram of f of x equals x with five arrows starting at minus one up to one — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure11.svg`] (image not included in the text import; path of record). \(f(x)=x\) | > [figure: mapping diagram of f of x equals minus x with five arrows starting at minus one up to one — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure12.svg`] (image not included in the text import; path of record). \(f(x)=-x\) | > [figure: mapping diagram of f of x equals minus 2 x plus 2 with five arrows starting at minus one up to one — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure13.svg`] (image not included in the text import; path of record). \(f(x)=-2x+2\) |

Clearly, the multiplier \(a\) in \(f(x)=ax+b\) makes a significant difference to the mapping diagrams:

- \(f(x)=2x\) is less “spread out” than \(f(x)=3x\), and \(f(x)=\frac{1}{2}x\) results in the arrows becoming closer together on the output numberline.
- \(f(x)=x\) consists of parallel arrows.
- \(f(x)=-x\) and \(f(x)=-2x\) both lead to arrows which cross themselves. (Incidentally, this is one way to see that multiplying an inequality by a negative number reverses the inequality.)

As we saw in the Warm-up, though, the mapping diagram for \(f(x)=ax+b\) remains the same if we change the “\(+b\)” part (as long as we stick to our conventions).

What would \(f(x)=0x\) look like?

### Extending the arrows

We could extend the arrows into straight lines.

- What patterns do you notice when you extend the arrows for different linear functions?
- What does this tell you about the nature of linear functions?

You can explore this further using the first of the [interactivities](https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/interactivities).

Here are the mapping diagrams for the same six functions as above, with extended lines.

| > [figure: mapping diagram of f of x equals 3 x with five arrows starting at minus one up to one, and the arrows extended into lines — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure14.svg`] (image not included in the text import; path of record). \(f(x)=3x\) | > [figure: mapping diagram of f of x equals 2 x plus 1 with five arrows starting at minus one up to one, and the arrows extended into lines — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure15.svg`] (image not included in the text import; path of record). \(f(x)=2x+1\) | > [figure: mapping diagram of f of x equals half x minus 1 with five arrows starting at minus one up to one, and the arrows extended into lines — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure16.svg`] (image not included in the text import; path of record). \(f(x)=\frac{1}{2}x-1\) |
| --- | --- | --- |
| > [figure: mapping diagram of f of x equals x with five arrows starting at minus one up to one, and the arrows extended into lines — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure17.svg`] (image not included in the text import; path of record). \(f(x)=x\) | > [figure: mapping diagram of f of x equals minus x with five arrows starting at minus one up to one, and the arrows extended into lines — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure18.svg`] (image not included in the text import; path of record). \(f(x)=-x\) | > [figure: mapping diagram of f of x equals minus 2 x plus 2 with five arrows starting at minus one up to one, and the arrows extended into lines — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure19.svg`] (image not included in the text import; path of record). \(f(x)=-2x+2\) |

The extended lines all meet at a single point (except for the function \(f(x)=x\)), which we could think of as a centre of enlargement or a focal point. This means that we can describe a linear function as a **scaling** of the left-hand numberline into the right-hand one.

What is the scale factor for each of the functions considered above (such as \(f(x)=3x\), \(f(x)=2x+1\), \(f(x)=\frac{1}{2}x-1\) and so on)? Can you suggest a general rule?

The scale factor for \(f(x)=3x\) is \(3\), for \(f(x)=2x+1\) is \(2\), for \(f(x)=\frac{1}{2}x\) is \(\frac{1}{2}\), for \(f(x)=x\) is \(1\), for \(f(x)=-x\) is \(-1\) and for \(f(x)=-2x+2\) is \(-2\).

The general rule seems to be that the scale factor for \(f(x)=ax+b\) is \(a\).

**A general rule**

**Some further questions:**

- Can you prove that every linear function behaves in this way: that it is a scaling of the left-hand numberline into the right-hand one?
- Can you find a rule for the location of the focal point for \(f(x)=ax+b\)?

If we can find a focal point for all of the lines, then we will have answered most of the first question as well.

The easiest case for calculations is when we have a function \(f(x)=ax\) (so \(b=0\)), and we centre our numberlines on the arrow from \(0\) to \(0\). (And we know from earlier that this doesn’t change what the mapping diagram looks like.) If we put a coordinate system on our diagram, and imagine that our numberlines cross the \(x\)-axis at the origin and \((1,0)\), then our diagram looks like this:

> [figure: two unlabelled vertical numberlines, the left one is the y axis and the right one is at x equals 1, there is an arrow from 0 comma k to 1 comma a k — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure20.svg`] (image not included in the text import; path of record).

An arrow then goes from the point with coordinates \((0,k)\), which represents some value of function input, to \((1,ak)\). It doesn’t even matter what the scale is on the numberlines: the arrow will still go from \((0,k)\) to \((1,ak)\) for some value of \(k\).

The gradient of this line is then \(\dfrac{ak-k}{1-0}=ak-k\), and so it has equation (in our “normal” \(x\)-\(y\) coordinate system) \(y=(ak-k)x+k\). This line will meet the \(x\)-axis when \(y=0\), so \(x=\dfrac{-k}{ak-k}=\dfrac{1}{1-a}\). This does not depend on \(k\), so *every* line must pass through the point \(\left(\dfrac{1}{1-a},0\right)\).

This means that the lines all pass through a single focal point.

But we have already seen that this is not true for the function \(f(x)=x\). Where does the argument fail in this case?

Using this formula, we can also say something about the location of the focal point, depending on the value of \(a\):

| Value of \(a\) | Location of focal point |
| --- | --- |
| \(a>1\) | to left of left-hand (input) numberline |
| \(0<a<1\) | to right of right-hand (output) numberline |
| \(a<0\) | between the numberlines |
| \(a=0\) | on the right-hand (output) numberline |

This also shows that the transformation from the left-hand (input) numberline to the right-hand (output) numberline is a scaling: the scale factor is clearly just \(a\) from the same diagram, as the line segment from \((0,0)\) to \((0,k)\) becomes the line segment from \((1,0)\) to \((1,ak)\).

The same argument also works if we consider the more general case where we centre the diagram on a different arrow, or if we have a function \(f(x)=ax+b\) instead. Can you see why?

**Solution**

### Taking it further: changing the conventions

Here are the mapping diagrams for \(f(x)=3x+1\) with the left one centred as we have been doing, and the right one with both numberlines centred at \(0\). For each one, we have drawn five arrows starting at \(-1\), \(-\frac{1}{2}\), \(0\), \(\frac{1}{2}\) and \(1\).

| > [figure: mapping diagram of f of x equals 3 x plus 1 with five arrows starting at minus one up to one, and the arrows extended into lines, left numberline centred at zero, right numberline centred at 1 — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure21.svg`] (image not included in the text import; path of record). \(f(x)=3x+1\) | > [figure: mapping diagram of f of x equals 2 x plus 1 with five arrows starting at minus one up to one, and the arrows extended into lines, both numberlines centred at zero — `https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/images/function-diagrams-figure22.svg`] (image not included in the text import; path of record). \(f(x)=3x+1\) |
| --- | --- |

Some observations we might make:

- The second diagram looks fairly similar to the first in many ways.
- The focal point is the same distance away from the left-hand numberline in both diagrams.
- The second diagram looks just like our earlier diagrams if we imagine the left-hand numberline being centred on \(-\frac{1}{2}\).
- The second diagram looks like the first, just with the right-hand numberline moved up by \(1\) unit and everything else pulled along with it. (The technical name for this transformation is a [shear](https://undergroundmathematics.org/glossary/shear).)

Can you explain these observations?

## Interactivities

In this interactivity, as in the Warm-up section, the output numberline is “locked” to the input one, so that the centre of the input numberline maps to the centre of the output numberline.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/VNy9ty37/width/600/height/493/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/VNy9ty37)

---

In this version of the interactivity, the output numberline can be centred independently of the input line.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/yasPkSXz/width/600/height/493/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/yasPkSXz)
