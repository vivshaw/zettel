tags:: books, devops, software engineering

- **Foreward/Intro**
	- this book dispels the myth that there's a tradefoff between speed and safety.
		- it shows a path to get an organization from "deploying once in a while" to "deploying multiple times per day"
		- this doesn't just make the engineers happy- it has real business value! it lets you explore the market, respond to problems, and release new features faster.
		- _and_, it's correlated with quicker recovery from outages.
	- it's not one-size-fits-all, and there are common traps you'll fall into if you try that
		- instead, you need to move to outcome-based team structures. e.g. [[OKR]]s
	- this only works if there's senior leadership support. with actions as well as words
- # Part 1: What We Found
- **Ch. 1: Accelerate**
  collapsed:: true
	- "business as usual" isn't good enough. we need to accelerate delivery of value to the custojmer- in the form of goods and services, market engagement to detect demand, anticipation of regulatory changes, risk response...
	- in the modern world, software is at the core of this
	- the practices developed by the [[devops]] movement are what this book will address and measure
	- **focus on capabilities, not maturity.**
		- > The key to successful change is measuring and understanding the right things with a focus on capabilities [...]
		  (p. 31)
	- why are maturity models bad?
		- maturity models are about arriving at a final state and being "done". but businesses should aim for [[continuous improvement]]
		  logseq.order-list-type:: number
		- maturity models are often a linear, one-size-fits-all formula. that doesn't track the diversity of real-world business.
		  logseq.order-list-type:: number
		- maturity models don't care about outcomes. but we _should_- we should be measuring what matters to us, then figuring out what levers to pull (capabilities) to influence it
		  logseq.order-list-type:: number
		- maturity models judge by a static level of tech progress. but tech is not static!
		  logseq.order-list-type:: number
	- we should use evidence to guide our efforts!
		- technology age, whether ops or dev team deploy, and whether a change approval board exists are all often cited as making a difference, but empirically they don't!
		- this book finds 24 empirically-supported capabilities to build. that's what the rest of the book is about!
- **Ch. 2: Measuring Performance**
	- flaws in previous attempt to measure performance:
		- they focus on *outputs* (e.g., LOC, PR count, story points) rather than *outcomes*. but outputs prioritize busywork!
		- they focus on *local maxima* over *global maxima*
	- measuring utilization is bad! low utilization is a problem, but 100% utilization is _also_ a problem- you lose all slack capacity for unplanned work, changes, and improvement
	- a package of four metrics for **global outcomes**- two tempo measures, and two stability measures:
		- **delivery lead time:** how long does it take to go from code committed, to code live in prod? alternatively, the time it takes for the build -> test -> deployment flow. (a proxy for lead time in general, but measuring the earlier phases of design & development is too squishy and vague)
		- **deployment frequency:** how often do you deploy? (a proxy for batch size- we want frequent, small changes, rather than huge, slow changes.)
			- small batches are important- they enable fast feedback via AB testing
		- **time to restore service:** when we have an incident, how long does it take to resolve it?
		- **change failure rate:** what % of changes to production fail?
	- used [[cluster analysis]] over 4 years of survey data. this located consistent clusters of high, medium, and low performers.
		- these measures are demonstrated to be statistically valid
		- the high performers showed both higher tempo _and_ higher stability. so there is no tradeoff!
		- some oddities with medium performers- in 2016 having _worse_ stability than low performers, but not other years. hypothesized due to these orgs being midway through rearchitecting
	- ok, this measures engineering performance- but does it have an impact on business performance?
		- sure does- high-performing cluster was twice as likely to exceed ROI targets as low performers
		- also overperformed on non-financial measures like quantity targets, customer satisfaction, etc
	- this has impacts on outsourcing/build-vs-buy decisions. it's a bad call to outsource business-critical software- you need to be bringing delivery capabilities into your org's core priorities. conversely, it's a bad call to in-house non-strategic software like payroll.
	- critical caveat: these measures need to be considered in tandem with company culture. toxic cultures lead to the use of measurements as a tool of control, and in turn reaction against that leads to bad measurements. so, you need to develop a healthy eng culture first!
- **Ch. 3: Measuring and Changing Culture**
	- "culture is king" - but how do we _measure_ something as squishy and abstract as culture?
	- org culture exists at three levels:
		- **basic assumptions** - the things we "just know", formed implicitly over time by working together and making sense of what we experience
		- **values** - visible, explicit collective values and norms of the org
		- **artifacts** - mission statements, technology, procedures, rituals, etc
	- a model defined by [[Ron Westrum]], operating at the values level, and supplying a typology of cultures:
		- **pathological** - power-oriented organizations, characterized by fear and threat. folsk hoard or withhold info for power or propaganda
		- **bureaucratic** - rule-oriented organizations, characterized by departments "protecting turf", working "by the book", red tape
		- **generative** - performance-oriented organizations, which focus on the mission. everything is subordinated to how we effectively accomplish our goals
	- Westrum's characteristics of good information
		- it provides answers to the question the receiver needs answered
		- it's timely
		- it is presented effectively
	- survey used a [[Likert scale]] to assess statements generated from Westrum's model
	- how'd the stats do? great! the model was found to have [[discriminant validity]], [[convergent validity]], and [[reliability (statistics)]], and found that culture impacted both delivery performance and org performance
	- how does generative culture enable information processing?
		- in generative orgs, folks collaborate more effectively and with more trust
		- in generative orgs, the mission is primary
		- in generative orgs, the playing field is more level
	- Google's research into high-performing teams- they thought they'd find a set of individual traits and skills that make you a high performer, but instead they found that who's on a team matters less than how they work and are structured
	- how do orgs deal with accidents? pathological orgs look for "a throat to choke" - finding and blaming the responsible person
		- so, "human error" is not good enough in [[incident response]]! human error tshould be the _start_ of an investigation, not the end. our goal should be finding ways to make human error less likely or less costly, not to point blame
	- how to change culture?
		- first change what people *do*. changing how they *think* comes later.
		- hypothesis: implementing a particular set of practices (agile/lean management, and continuous delivery) impacts culture
		- in fact, they do! survey found that both sets of practices impact culture