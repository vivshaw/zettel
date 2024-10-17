tags:: stats

- used to measure inter-rater reliability for [[qualitative data]]. measures "the proportion of agreement in excess of chance".
- calculated as:
	- $\kappa = \dfrac{P_{Agreement} - P_{Chance\ Agreement}}{1 - P_{Chance\ Agreement}}$
- we can also think about $\kappa_{Max}$, which is the maximum agreement we could see under the observed asymmetry. (if there were no asymmetry, there would be perfect agreement!) this can be interpreted as indicating differences involving scale use.
- in [[R]], we might use `chisq.test()` together with [[lolcat]]'s `cor.cohen.kappa.onesample.1969.fleiss()`
	- in situations with multiple raters, we may need to use Light's kappa. this can be done with the IRR package's `kappam.light()`