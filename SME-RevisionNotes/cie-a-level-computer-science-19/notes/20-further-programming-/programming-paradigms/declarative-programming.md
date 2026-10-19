---
note_id: "rn_wGYJ4q2M4P9drmPR"
title: "Declarative Programming"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/20-further-programming-/programming-paradigms/declarative-programming
path: 20-further-programming-/programming-paradigms/declarative-programming
updated_at: "2025-05-21T10:17:54.503Z"
spec_point_ids: ["spcpt_YZ8w2RRD5XPbkGKz"]
spec_point_codes: []
guided_study: false
---

# Declarative Programming

## Declarative programming

> **Spec point** — `spcpt_YZ8w2RRD5XPbkGKz`

## Declarative programming

### How do I write declarative code?

- Declarative programming is a paradigm where you describe **what** you want the program to accomplish, not **how** to do it
- **SQL** is a common example of declarative programming
- It allows you to **extract and manipulate data using queries**, without needing to specify the control flow
- SQL was covered in more detail in [Section 8 – SQL](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/8-databases-/data-definition-language-ddl-and-data-manipulation-language-dml/sql/)
- Declarative code is made up of:

  - **Facts** – things that are known or assumed to be true
  - **Rules** – logical relationships between facts
- Unlike imperative programming, where order and control flow are essential, declarative code allows you to define **facts and rules in any order**, and then write a **query** that uses them

- In the following examples, a logic-based declarative language (like **Prolog**) is used

#### Example: Facts about dog breeds

#### Interpreting clauses

- Each fact uses the format:

| Clause | Meaning |
|---|---|
| `type(poodle, companion).` | A poodle is a companion dog |
| `size(labrador, large).` | A Labrador is a large-sized dog |
| `shedding(bulldog, low).` | A bulldog has low shedding |

#### Sample queries

- Use queries to retrieve information from the facts

#### Key points

| Concept | Description |
|---|---|
| **Fact** | A statement like `type(beagle, hound).` that is always true |
| **Rule** | A logical relationship built from facts (not shown here) |
| **Query** | A question to the knowledge base, e.g. `size(X, medium).` |
| **Any order** | Facts and rules can appear in **any order** |
| **Result** | The interpreter **matches patterns** in queries against known facts |
