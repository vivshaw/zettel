tags:: stats, spc, measurement systems analysis

- in [[R]], we can use [[lolcat]]'s `msa.nominal.concordance()` to assess concordance (inter-rater agreement)
- we can also use `msa.nominal.internalconsistency()` to assess validity over time for one rater.
	- you'll need to use Bowker's test rather than [[McNemar's test]] for internal consistency. this package does that automagically for you.