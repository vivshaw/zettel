tags:: ml, mlops, error analysis

- from [[Andrew Ng]], one technique would be: grab a handful of examples your algorithm misrecognizes, go through them by hand, and look for and tag patterns. for example, if you're doing speech recognition, maybe you'll find that examples with car noise or background voices are misrecognized. or for a recommender system, maybe you'll find that it recommends poorly for a specific demographic.
	- tag those in your dataset! then you can focus in on the ones that give you the greatest opportunity for improvement.
	- for each tag, what fraction of errors have that tag?
	- for each tag, of all data with that tag, what fraction is misclassified?
- when prioritizing, think about not just accuracy vs [[HLP]] for a given category, but:
	- the % of the dataset that falls into that category. no use in getting awesome with a category that only makes up 0.1% of your dataset. but a small improvement to a category of 90% of your dataset will be more impactful than expected
	- how hard it is to improve. you might have room to improve, but hit diminishing returns!
	- how important it is to improve. if it's core to your business case, you might need to nail it even if there are bigger opportunities elsewhere.
- once you've decided what to improve, you should:
	- collect more data in those categories
	- or if you can't, use [[data augmentation]] to generate more data
	- improve the data quality and labeling accuracy