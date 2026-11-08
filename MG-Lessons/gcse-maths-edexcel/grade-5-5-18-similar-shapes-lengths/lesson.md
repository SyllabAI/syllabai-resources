# grade-5-5-18-similar-shapes-lengths — lesson

_Lane: `gcse-maths-edexcel` · grade 5 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## What similar shapes mean

Similar shapes have the same shape but can be different sizes. Their corresponding angles are equal, and every corresponding length is changed by the same scale factor.

To find corresponding sides, match the vertices first, then compare sides in the same positions. This matters when a shape has been rotated, reflected, or labelled in a different order.

If one side is multiplied by $k$, every other corresponding side is also multiplied by $k$. This is the key length rule in every similar-shapes question.

## The scale-factor method

To calculate the scale factor, identify one complete matching pair of sides. From shape 1 to shape 2, the scale factor $k$ is found using this ratio:

$$$k = \frac{\text{shape 2 length}}{\text{shape 1 length}}$$

Apply this multiplier to every corresponding length to find missing values. If you are moving from the larger shape back to the smaller one, you must divide by $k$ instead of multiplying.

Always perform a sanity check at the end of your calculation. A side on the larger shape should result in a larger value, while a side on the smaller shape should be smaller.

## Worked example: missing lengths in similar triangles

![Two similar triangles ABC and PQR with corresponding sides colour-matched, AB = 10 cm, AC = 24 cm, PQ = 15 cm, QR = 27 cm, and unknowns BC and PR](../assets/001-459854b2-ca94-488c-b54f-1b37e078b407.jpeg)

We match the vertices first: $A \leftrightarrow P$, $B \leftrightarrow Q$, $C \leftrightarrow R$. So $AB \leftrightarrow PQ$, $AC \leftrightarrow PR$, and $BC \leftrightarrow QR$.

Find the scale factor from $ABC$ to $PQR$: $k = \frac{PQ}{AB} = \frac{15}{10} = 1.5$. Because $PQR$ is the larger triangle, we multiply lengths from $ABC$ by $1.5$.

Use $AC \leftrightarrow PR$: $PR = 24 \times 1.5 = 36$ cm. This is on the larger triangle, so multiplying is the correct direction.

Use $BC \leftrightarrow QR$ and work backwards: $BC = 27 \div 1.5 = 18$ cm. Dividing makes sense here because $BC$ is on the smaller triangle.

## Parallel lines inside triangles

![Triangle ACD with points B on AC and E on AD, segment BE parallel to CD, AB = 6 cm, BC = 4 cm, AE = 7.5 cm, CD = 15 cm, and unknowns BE and ED](../assets/002-222131cd-91d6-4055-8c04-27cf4cc3ca40.jpeg)

Because $BE$ is parallel to $CD$, triangles $ABE$ and $ACD$ have equal corresponding angles, so they are similar. First find the whole side $AC = AB + BC = 6 + 4 = 10$ cm.

Now find the scale factor from the small triangle to the whole triangle: $$k = \frac{AC}{AB} = \frac{10}{6} = \frac{5}{3}$$ This means every whole-triangle length is $\frac{5}{3}$ times the matching small-triangle length.

Use $AE \leftrightarrow AD$ to find the whole sloping side: $AD = 7.5 \times \frac{5}{3} = 12.5$ cm. The question wants the extra part, so $ED = AD - AE = 12.5 - 7.5 = 5$ cm.

Use $BE \leftrightarrow CD$ for the other missing side: $BE = 15 \div \frac{5}{3} = 9$ cm. Always check whether you need a whole side, a small side, or just the leftover section.

## Ratios and showing rectangles are not similar

A ratio can hide the scale factor. If $AB:AC = 2:5$, then the scale factor from $AB$ to $AC$ is $\frac{5}{2} = 2.5$.

For rectangles, all angles are right angles already, so the real test is whether the side scale factors match. Compare length with length and width with width.

Example: rectangle A is $120$ mm by $70$ mm and rectangle B is $150$ mm by $90$ mm. Here $k_{\text{length}} = \frac{150}{120} = 1.25$ but $k_{\text{width}} = \frac{90}{70} \approx 1.29$, so the rectangles are not similar.

## Check yourself

1. Which statement guarantees that two shapes are mathematically similar?

   - All matching angles are equal and all corresponding sides have the same scale factor ✔

   - They have the same area

   - They are both triangles

   - They have one equal side

   _Explanation:_ A is correct because similar shapes need both equal corresponding angles and one constant multiplier for all matching lengths. C is a common wrong answer because two triangles can have very different shapes unless their angles and side ratios match.

2. The scale factor from a smaller triangle to a larger triangle is $1.5$. If a corresponding side on the smaller triangle is $12$ cm, what is the matching side on the larger triangle?

   - $$8$ cm

   - $$15$ cm

   - $$18$ cm ✔

   - $$30$ cm

   _Explanation:_ C is correct because $12 \times 1.5 = 18$. A is the most common wrong answer because it comes from dividing by $1.5$, but dividing would move from the larger shape back to the smaller one.

3. Rectangle A is $120$ mm by $70$ mm and rectangle B is $150$ mm by $90$ mm. Which is the best reason they are not similar?

   - The side differences are not equal

   - $$\frac{150}{120} = 1.25$ but $\frac{90}{70} \approx 1.29$, so the scale factors do not match ✔

   - They are not similar because one rectangle is larger

   - They are similar because all rectangles have equal angles

   _Explanation:_ B is correct because similar rectangles need the same multiplier for both length and width. D is the most common wrong answer because equal angles are not enough on their own; rectangles can have different length-to-width ratios.
