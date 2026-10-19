---
note_id: "rn_KjChdSnSXGqsfFMq"
title: "CSS"
source: https://www.savemyexams.com/igcse/ict/cie/21/revision-notes/12-website-authoring/css-in-the-presentation-layer/css
path: 12-website-authoring/css-in-the-presentation-layer/css
updated_at: "2024-05-21T07:51:12.406Z"
spec_point_ids: ["spcpt_35wpGMsnXG2m7pWn", "spcpt_NGPZx23qsM8Cr4xg", "spcpt_mjyYsb4nDVGJZCJN"]
spec_point_codes: []
guided_study: false
---

# CSS

## What is CSS?

- Cascading Style Sheets (CSS) **define the style or appearance** of a webpage
- CSS uses selectors such as classes or IDs
- CSS can be **placed within HTML or externally in a file**
- Multiple pieces of CSS can be combined
- Where CSS is used within the HTML, this will be used rather than any external CSS styling and will override the external stylesheet

## Attached & Inline

> **Spec point** — `spcpt_35wpGMsnXG2m7pWn`

## Attached & Inline

### What is an attached stylesheet?

- An attached stylesheet is a separate CSS file that is linked to the HTML page by a hyperlink
- Attached stylesheets mean they can be edited separately to the HTML
- This allows for the same styles to be reused across multiple pages

#### Relative file paths for attached stylesheets

- **Relative file paths** are used for linked stylesheets because they refer to the location of the CSS file relative to the current HTML file
- This makes the code more portable and easier to manage
- E.g. if the CSS file is in the same folder as the HTML file, the path would be `"styles.css"`
- If the CSS file is in a subfolder named `css`, the path would be `"css/styles.css"`

### What is an inline stylesheet?

- Inline stylesheets are written directly within a HTML tag using the `style `attribute
- The styles only apply to the webpage they are written into

#### Hierarchy of multiple attached stylesheets and inline styles

- If there are multiple styles defined for the same HTML element, the** style closest to the element takes priority**
- This is called the **cascading** order
- The cascading order, from highest to lowest priority, is:

  1. **Inline styles (inside an HTML element)**
  2. **External and internal styles (in the head section)**
  3. **Browser default**

## Styles

> **Spec point** — `spcpt_NGPZx23qsM8Cr4xg`

## Styles

### What are CSS styles?

- Styles **control the visual properties** of an element in the body of a webpage
- Examples of elements that can be styled are:

  - **Backgrounds**
  - **Fonts**
  - **Tables**

#### Backgrounds

- **Background colour**: Set the background colour using the `background-color` property

  - E.g. `background-color: blue;`
- **Background images**: Set a background image using the `background-image` property

  - E.g. `background-image: url("image.jpg");`

#### Fonts

- Control the appearance of text with **font properties**
- This includes `font-size`, `font-family`, `color`, `text-align`, and more

#### Tables

- CSS is used to style HTML tables, allowing users to define the appearance of the **table**, **table rows**, **table headers**, and **table data cells**

  - **Size**: Control the width and height of a table using `width` and `height`.
  
    - E.g. `width: 100%; height: 200px;`
  - **Background colour**: Use `background-color` to set the background.
  
    - E.g. `background-color: yellow;`
  - **Borders**: Apply a border using the `border` property including colour, thickness, and visibility.
  
    - E.g: `border: 2px solid black;`
  - **Collapsed borders**: Use `border-collapse: collapse;` to make borders appear as a single line
  - **Spacing**: Control the space between cells with `border-spacing`.
  
    - E.g. `border-spacing: 5px;`
  - **Padding**: Define the space between cell content and its border with `padding`.
  
    - E.g. `padding: 10px;`

## Classes

> **Spec point** — `spcpt_mjyYsb4nDVGJZCJN`

## Classes

### What are CSS classes?

- Classes allow styles to be grouped together and applied to multiple elements
- Classes act at reusable templates
- To define a class, use a period (.) followed by the class name
- To apply a class to an HTML element, use the `class` attribute

#### Background colour

- Use the `background-color` property

#### Background images

- Use the `background-image` property

#### Font properties

- Control the font size, family, colour, and alignment

#### Size

- Control the width and height with `width` and `height`

#### Background colour

- Use `background-color` to set the background

#### Horizontal and vertical alignment

- Use `text-align` (horizontal) and `vertical-align` (vertical)

#### Spacing, padding, borders

- Use `padding` for space inside the cell, and `border` for cell borders

#### Collapsed borders

- Use `border-collapse: collapse;` the table class to remove spaces between cell borders

> **Worked Example**
> A teacher is creating a web page in HTML to display on the school’s intranet.
> All colour codes must be in hexadecimal. It has the following style sheet attached:
> 
> Having tested the web page the teacher needs to make some changes to the style sheet.
> 
> Write down the CSS to:
> 
> a. edit style h1 so that the font is Comic Sans or, if not available, Arial or, if this is not available, the browser’s default sans-serif font.
> 
> **[3]**
> 
> b. add a markup to the table style to set a 3-pixel wide, dashed external border.
> 
> **[4]**
> 
> c. edit style h3 so that the colour is set to black.
> 
> **[1]**
> 
> d. add a markup to the start of style h2 to display the text as bold.
> 
> **[2]**
> 
> **Answers**
> 
> **a.** font-family: "Comic Sans", Arial, sans-serif;
> 
> **Final answer:** **"Comic Sans", [1]**
> **Arial, [1]**
> **sans-serif; [1]**
> **Must be in the correct order**
> 
> **b.** table {border-color: #000000; border-style: dashed; border-width: 3px  }
> 
> **Final answer:** **border-style: [1]**
> **dashed; [1]**
> **border-width: [1]**
> **3px [1]**
> 
> **c.** h3 {color:  #000000;
> 
> **Final answer:** **#000000; [1]**
> 
> **d.** h2 { font-weight: bold;
> 
> **Final answer:** **font-weight: [1]**
> **bold; [1]**
