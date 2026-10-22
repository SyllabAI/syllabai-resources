---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r6100
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r6100
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6100
  old_site_id: Q5
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: circles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: circles
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'Circles x^2+y^2=25 and x^2+y^2-24x-18y+125=0 shown to touch; touch point calculated — centre/radius plus tangency.'
      rationale: 'Canonical UGM title: “Can we show that these two circles touch?”; exam provenance: UCLES 1986 Q7'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1986 Q7
task: T-UGM-IMPORT-3
---

# Can we show that these two circles touch?

## Question

Show that the circles having equations \(x^2 + y^2 = 25\) and \(x^2 + y^2 - 24x - 18y + 125 = 0\) touch each other. Calculate the coordinates of the point at which they touch.

## Suggestion

Could I sketch the two circles and observe what is happening?

If the two circles touch, then in how many points do they intersect?

Could we solve the two equations simultaneously?

How could I do this as neatly as possible, and how many solutions would I expect?

## Solution

**Approach 1: Geometric**

The circle with equation \(x^2+y^2=25\) has its centre at the origin and radius \(5\).

We can complete the square for the equation \(x^2 + y^2 - 24x - 18y + 125 = 0\) to find its centre and radius: \[\begin{gathered} x^2 + y^2 - 24x - 18y + 125 = 0\\ \implies\quad (x-12)^2-12^2 + (y-9)^2 -9^2 + 125 = 0\\ \implies\quad (x-12)^2 + (y-9)^2 = 144+81-125\\ \implies\quad (x-12)^2 + (y-9)^2 = 100 \end{gathered}\] so this circle has centre \((12,9)\) and radius \(10\).

We can sketch these:

It seems as though the circles touch. Let’s prove that!

The length of the line joining the two centres \((0,0)\) and \((12,9)\) is (using Pythagoras) \[\sqrt{12^2+9^2}=\sqrt{144+81}=\sqrt{225}=15.\]

Alternatively, we can notice that \(9\) and \(12\) form the two short sides of right-angled triangle, which must be a \(3\)-\(4\)-\(5\) triangle scaled by a factor of \(3\), and therefore the diagonal length is \(3\times 5=15\).

Now the radii of the two circles are \(5\) and \(10\). Since \(5+10=15\) (the distance between the centres), the two circles touch.

To find the coordinates of the point where they touch, we can use similar triangles:

The small triangle has sides in the ratio \(a:b:5\) (base to height to hypotenuse), while in the large triangle, they are in the ratio \(12:9:15\). These ratios are the same, so \(a:b:5=4:3:5\), and the point of touching has coordinates \((4,3)\).

Another way to think about this is that the point of touching is \(\dfrac{5}{15}=\dfrac{1}{3}\) of the way along the line from \((0,0)\) to \((12,9)\), so it is at \((4,3)\).

**Approach 2: Algebraic**

For the circles to touch, we must show that they intersect at exactly one point.

We have the equations of the two circles: \[x^2 + y^2 = 25\] and \[x^2 + y^2 - 24x - 18y + 125 = 0.\]

Substituting the first equation into the second (or alternatively subtracting the first equation from the second) gives

\[\begin{align*} &25 - 24x - 18y + 125 = 0\\ \Longrightarrow\quad& 24x + 18y = 150\\ \Longrightarrow\quad& 4x + 3y = 25. \end{align*}\]

So if the two circles meet in two points, they must both lie on \(4x + 3y = 25.\)

We can rearrange

\(4x + 3y = 25\)

to get

\[x = \frac{1}{4}(25-3y)\]

and substitute into the equation

\(x^2 + y^2 = 25\)

:

\[\begin{align*} &\left(\frac{1}{4}(25-3y)\right)^2 +y^2 = 25\\ \iff\quad& 25y^2 - 150y + 225 = 0\\ \iff\quad& y^2 - 6y + 9 = 0\\ \iff\quad& (y-3)^2 = 0\\ \iff\quad& y = 3. \end{align*}\]

The quadratic equation has a repeated root, so has exactly one solution.

This means that the line \(4x + 3y = 25\) is a tangent to the circle \(x^2 + y^2 = 25.\)

We can find the corresponding

\(x\)

value by setting

\(y = 3\)

in the equation

\(4x + 3y = 25\)

:

\[\begin{align*} &4x + 3(3) = 25\\ \Longrightarrow\quad& x = 4. \end{align*}\]

Substituting

\[x = \frac{1}{4}(25-3y)\]

into the equation

\(x^2 + y^2 - 24x - 18y + 125 = 0,\)

we have

\[\begin{align*} &\left(\frac{1}{4}(25-3y)\right)^2 +y^2 -24\left(\frac{1}{4}(25-3y)\right)-18y+125= 0\\ \iff\quad& 25y^2 - 150y + 225 = 0\\ \iff\quad& y^2 - 6y + 9 = 0\\ \iff\quad& (y-3)^2 = 0\\ \iff\quad& y = 3. \end{align*}\]

This means that the line \(4x + 3y = 25\) is a tangent to the second circle also at \((4,3)\).

So the circles \(x^2 + y^2 = 25\) and \(x^2 + y^2 - 24x - 18y + 125 = 0\) touch at the point \((4,3)\).
