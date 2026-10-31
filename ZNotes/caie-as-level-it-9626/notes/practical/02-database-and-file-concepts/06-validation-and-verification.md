## Validation and verification

  - Validation- Validation rules can be applied to data in the database

  - Types of validation
    
      - Lookup in list
    
      - Range
    
      - Data type
    
      - Format
    
      - Length
    
      - Presence

![](../../../assets/9ae003d26d44-image063.png)

<table>
<thead>
<tr class="header">
<th>
<p><strong>Rule</strong></p>
</th>
<th>
<p><strong>Type</strong></p>
</th>
<th>
<p><strong>Purpose</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>
<p>“M” or “F”</p>
</td>
<td>
<p>Lookup in list</p>
</td>
<td>
<p>Must be either “M” or “F”</p>
</td>
</tr>
<tr class="even">
<td>
<p>IN(“Mrs.”, “Mr.”, “Miss”, “Dr”)</p>
</td>
<td>
<p>Lookup in list</p>
</td>
<td>
<p>Must be any of the values in the list</p>
</td>
</tr>
<tr class="odd">
<td>
<p>&gt;DATE()</p>
</td>
<td>
<p>Range</p>
</td>
<td>
<p>Must be after today’s date</p>
</td>
</tr>
<tr class="even">
<td>
<p>&gt;28/03/1980</p>
</td>
<td>
<p>Range</p>
</td>
<td>
<p>Must be after the date listed</p>
</td>
</tr>
<tr class="odd">
<td>
<p>Between 3 And 10</p>
</td>
<td>
<p>Range</p>
</td>
<td>
<p>Value must be greater than 3 but less than 10</p>
</td>
</tr>
<tr class="even">
<td>
<p>&gt;2</p>
</td>
<td>
<p>Range</p>
</td>
<td>
<p>Value must be greater than 2</p>
</td>
</tr>
<tr class="odd">
<td>
<p>Like “[A-Z][A-Z]”</p>
</td>
<td>
<p>Data type</p>
</td>
<td>
<p>Must be two text characters</p>
</td>
</tr>
<tr class="even">
<td>
<p>Like”*@*.*”</p>
</td>
<td>
<p>Format</p>
</td>
<td>
<p>Email address</p>
</td>
</tr>
<tr class="odd">
<td>
<p>IS NOT NULL</p>
</td>
<td>
<p>Presence</p>
</td>
<td>
<p>Field must not be empty</p>
</td>
</tr>
</tbody>
</table>
