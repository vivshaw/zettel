tags:: stats, [[relationship (stats)]]

- a [[one-sample test]] for whether a [[correlation]] differs from a given *non-zero* value, using [[Fisher's z-transformation]] to transform $r$ into a $z$-value, and a [[z-test]]
- calculated as: $Z_F = \dfrac{r_{tr} - \rho_{tr}}{\sqrt{\dfrac{1}{n - 3}}}$, where $r_{tr}$ and $\rho_{tr}$ are the transformed values.
- in [[R]], we can still use [[lolcat]]'s `cor.pearson.r.onesample()` just like we would with a [[t-test for correlation]], we just need to supply a value for `null.hypothesis.rho`.