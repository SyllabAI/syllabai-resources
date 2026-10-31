## CSS

### **What is CSS?**

* Cascading style sheet
* Used to style webpages
* Two types
  * Embedded/inline
  * External

### **Embedded**

* Used to apply style properties within HTML sheet
* Format:
  * …style = “attribute: specification”>
  * Inline CSS for e.g. <table border=”1”
    **<span class="underline">style= “width:200px”</span>**>
* To add several attributes, add a semicolon to separate them and then use the same format
  * For e.g. < table style=
    “width:29%***<span class="underline">;</span>*** margin-left:
    auto\*\*<span class="underline">;</span>\*\*”>
* For inline CSS, adding -style= “….”- is mandatory.

### **External**

* External CSS sheets are separate sheets that style the webpage.
* To use, they are required to be attached to the main HTML file using the tag:
  * `<link rel=“stylesheet” type=”text/css” href=”sourcefile.css”>`
  * The tag is placed in the head tag of the html file. Several html sheets can be attached.
  * Preference is given to the sheet placed last in the head tag
* Format for external CSS
  * h1 { property: value ;}
  * for e.g. h1 { color:#000000;}
    * ↑ Element source is taken from HTML script linked

### **CSS Tags**

#### Colours

* Colours can be in hexadecimal
  * hashtag before the hexadecimal is mandatory
  * e.g. #000000
  * F full capacity
  * 0 is the least capacity
* Some colours can be written in words. Such as black or white.

#### Fonts

* Fonts are given priority from first to last in order
* To add multiple fonts, add commas.
  * Eg. h1 { font-family: Arial, Calibri, sans-serif;}

#### Tables

* Tables have many attributes to help style them
  * Cell padding: creates space between text and cell border
  * Cell spacing: creates space between individual cells
  * Borders
  * Background colour: background tags in the tables only apply to the tables.
* Individual td or th headings can also be specified in CSS

<table> <thead> <tr class="header"> <th>Table tags</th> <th>format</th> </tr> </thead> <tbody> <tr class="odd"> <td>cell padding</td> <td><p>Table { padding :40px;}</p></td> </tr> <tr class="even"> <td>cell spacing</td> <td><p>Table { spacing : 30px;}</p> </tr> <tr class="odd"> <td>borders</td> <td><p>Table { border-width:3px;}</p><p>Table { border-color: #000098;}</p><p>Table { border-style: solid;}</p><p>Table { background-color: #009499;}</p></td> </tr> <tr class="even"> <td>Td/th tags</td> <td><p>td { font-size: 3;}</p><p>td { font-family: Calibri;}</p><p>td { color: #000000;}</p></td> </tr> <tr class="odd"> <td>Dimensions</td> <td><p>table { width:50px;}</p><p>table { height:60px;}</p></td> </tr> </tbody> </table>

* body { background-repeat: no-repeat;}
* body {background-position: top/left/right/bottom;}
* h1 {text-align: left/right/top/bottom;}



