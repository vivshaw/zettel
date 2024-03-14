tags:: ml
alias:: modeling

- model development is iterative!
	- your algorithm, data, and hyperparameters are all inputs to your model. you should analyze them as you iterate.
	- there's a lot of emphasis these days on state-of-the-art algorithms. but in many cases, an off-the-shelf algorithm may be good enough, and you should actually focus on getting great data!
- milestones to tackle:
	- doing well on the training set
	- doing well on the dev/test sets
	- doing well on the project goals! this is not the same as being accurate on a test set- it means meeting the business or organizational need! when low error rates not be enough?
		- when performance is more important on disproportionately important examples. search is often like this with navigational queries (as opposed to informational or transactional ones)
		- performance on key slices of the dataset- e.g., ensuring the algo doesn't discriminate against minorities. or, ensuring your recommender recommends stuff within all your major product segments
		- skewed data distributions- you can achieve 99% accuracy on a dataset that's 99% `False` with just: `print("False")`. but that's not useful at all! you need to make sure your algorithm isn't accidentally doing this. e.g., medical algorithms on rare diseases
- options establishing baselines:
	- compare against human-level performance! a model's performance might look OK, but be well below what a human can do. or, it might look low, but turn out to be already as good as is feasible!
		- this is more useful for unstructured data! humans evolved to be great at looking at images and listening to audio. but we didn't evolve to be great at looking at giant spreadsheets. so HLP might not be as useful for structured data
	- literature search for SOTA results
	- quick-and-dirty implementation
	- performance of an older system, if you're replacing one
- baselines are critical because they help you understand what might and might not be possible.
- how to get started from scratch:
	- start with a literature search to see what's possible, and don't obsess with hitting the SOTA.
	- find open-source versions if possible. a decent model with great data is probably good enough!
	- consider deployment constraints, _if_ you're relatively confident it will work, you already have a baseline, and you know the constraints. but if it's round 1 and you don't know any of this, maybe ignore deployment and just take a stab at it.
	- sanity check! start by trying to overfit a very small dataset