# [Why and When Can Deep but Not Shallow -- Networks Avoid the Curse of Dimensionality](https://arxiv.org/pdf/1611.00740.pdf)
### Tomaso Poggio - 2017

## Summary

- Deep Networks can avoid the [**Curse of Dimensionality**](#COD) problem when approximating functions of a specific class: [**local compositional functions**](#LCF)


#### [Curse of Dimensionality](#COD)

#### [Local Compositional Functions](#LCF)

**Compositional Function**: a function that can be composed from other functions.
- Example: $f(x_1, x_2, ..., x_n) = h_1(h_2(x_1, x_2), h_3(x_n))$

**Input Size** of a function: the number of input variables of the function

**Local Compositional Function**: a compositional function $f$ where $InputSize(h)\le k << InputSize(f)$ for all component functions $h$