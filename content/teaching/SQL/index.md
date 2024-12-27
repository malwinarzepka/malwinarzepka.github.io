---
title: Big Data Analysis
summary: Practical course on the basics of the Structured Query Language (SQL) using Microsoft Server environment. 
date: 2023-10-24
type: docs
math: false
tags:
  - SQL
image:
 # caption: 'Embed rich media such as videos and LaTeX math'

Course structure: |
  I develop my courses for full-time and part-time students, taking into account their needs and limitations. The course covers everything from data queries and programming to table joins and subqueries for full-time students. Part-time students focus on filtering, aggregate functions, and grouping to gain essential competencies they can use in their careers.
  Each class has an introduction, examples, and hands-on tasks. These individual or small-group tasks enable students contribute and reinforce their learning. After students do the exercises, I check them right away. providing fast comments to confirm understanding and address any errors immediately.

The overarching goals of my Big Data Analysis class include: |-

  - Developing proficiency in SQL for data querying.

  - Building an understanding of relational databases and how to integrate data across multiple tables.

  - Enhancing analytical thinking through problem-solving exercises based on state of the art instructional materials.

  - Cultivating data interpretation skills to support decision-making and insights generation.

Materials used in class: |
  - ["SQL Queries for Mere Mortals: A Hands-On Guide to Data Manipulation in SQL", 4th Edition by John L. Viescas] (https://www.oreilly.com/library/view/sql-queries-for/9780134858432/)
  - Supplementary materials include free online courses so Students can experience working with different versions of SQL, for example [codecademy] (https://www.codecademy.com/learn/learn-sql)

#[Hugo Blox Builder](https://hugoblox.com) is designed to give technical content creators a seamless experience. You can focus on the content and the Hugo Blox Builder which this template is built upon handles the rest.

#**Embed videos, podcasts, code, LaTeX math, and even test students!**

#On this page, you'll find some examples of the types of technical content that can be rendered with Hugo Blox.



## Test students

#Provide a simple yet fun self-assessment by revealing the solutions to challenges with the `spoiler` shortcode:

#```markdown
#{{</* spoiler text="👉 Click to view the solution" */>}}
#You found me!
#{{</* /spoiler */>}}
#```

#renders as

#{{< spoiler text="👉 Click to view the solution" >}} You found me 🎉 {{< /spoiler >}}

## Math

#Hugo Blox Builder supports a Markdown extension for $\LaTeX$ math. You can enable this feature by toggling the `math` option in your `config/_default/params.yaml` file.

#To render _inline_ or _block_ math, wrap your LaTeX math with `{{</* math */>}}$...${{</* /math */>}}` or `{{</* math */>}}$$...$${{</* /math */>}}`, respectively.

#{{% callout note %}}
#We wrap the LaTeX math in the Hugo Blox _math_ shortcode to prevent Hugo rendering our math as Markdown.
#{{% /callout %}}

#Example **math block**:

#```latex
#{{</* math */>}}
#$$
#\gamma_{n} = \frac{ \left | \left (\mathbf x_{n} - \mathbf x_{n-1} \right )^T \left [\nabla F (\mathbf x_{n}) - \nabla F (\mathbf x_{n-1}) \right ] \right |}{\left \|\nabla F(\mathbf{x}_{n}) - \nabla F(\mathbf{x}_{n-1}) \right \|^2}
#$$
#{{</* /math */>}}
#```

#renders as

#{{< math >}}
#$$\gamma_{n} = \frac{ \left | \left (\mathbf x_{n} - \mathbf x_{n-1} \right )^T \left [\nabla F (\mathbf x_{n}) - \nabla F (\mathbf x_{n-1}) \right ] \right |}{\left \|\nabla F(\mathbf{x}_{n}) - \nabla F(\mathbf{x}_{n-1}) \right \|^2}$$
#{{< /math >}}

#Example **inline math** `{{</* math */>}}$\nabla F(\mathbf{x}_{n})${{</* /math */>}}` renders as {{< math >}}$\nabla F(\mathbf{x}_{n})${{< /math >}}.

#Example **multi-line math** using the math linebreak (`\\`):

#```latex
#{{</* math */>}}
#$$f(k;p_{0}^{*}) = \begin{cases}p_{0}^{*} & \text{if }k=1, \\
#1-p_{0}^{*} & \text{if }k=0.\end{cases}$$
#{{</* /math */>}}
#```

#renders as

#{{< math >}}

#$$
#f(k;p_{0}^{*}) = \begin{cases}p_{0}^{*} & \text{if }k=1, \\
#1-p_{0}^{*} & \text{if }k=0.\end{cases}
#$$

#{{< /math >}}

## Code

#Hugo Blox Builder utilises Hugo's Markdown extension for highlighting code syntax. The code theme can be selected in the `config/_default/params.yaml` file.


 #   ```python
 #   import pandas as pd
 #   data = pd.read_csv("data.csv")
 #   data.head()
 #   ```

#renders as

#```python
#import pandas as pd
#data = pd.read_csv("data.csv")
#data.head()
#```

## Inline Images

#```go
#{{</* icon name="python" */>}} Python
#```

#renders as

#{{< icon name="python" >}} Python

## Did you find this page helpful? Consider sharing it 🙌
---