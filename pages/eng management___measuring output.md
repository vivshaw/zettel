---
alias: measuring output, measuring velocity
tags: metrics, performance
---

- metrics like GitHub PR count or LOC can be extremely perverse. you should be worried when these are a key indicator.
	- it is possible to maximize these by _worsening_ the quality of your work. ship more bugs so you can ship more bugfixes. write more verbose code instead of less. add multi-step processes where none are needed. these will all drive up those metrics, while slowing you down
	- focusing on these will deemphasize everything else: code review, running interviews, mentorship, giving presos, writing project docs...
	- if your output target is too low, people will hit it and then stop. if it is too high, people will grind for it and burn out.
- an insight from a coworker on when these metrics are and aren't useful:
	- > PR & LOC stuff is pretty much only useful *if you don't understand what the person did*. For example, it can be useful for a CTO or director to sort by PR/LOC and get curious about outliers, because they have no responsibility to know what any individual IC is doing. PR/LOC stuff should be almost useless to a line manager because they should already know what the IC is doing in more meaningful terms. So, perhaps if an exec notices a low velocity, they follow up with the EM for a meaningful explanation of what's happening.
	  To call out the other side, if a manager is realizing a performance issue via PR counts (_especially_ as part of an exercise that happens only every 6 months), that report has effectively been unmanaged.
	  In perf review calibration, the conversation should be about consequences, not PR/LOC ("Because of this report <this happened>" or "If this report weren't here <this would have happened>")
- when you must use these metrics, use distributions. compare individuals against the distro of the organization, as well as comparing the team as a whole against the rest of the org. get a sense of outliers, not numerical targets.
	- think about both negative _and positive_ outliers! if someone's cranking out massive numbers of PRs, is it just 'cause they're naturally fast, or are they sprinting toward burnout?
	- don't neglect the team. some teams just are working on harder / slower problems, or vice-versa. don't punish individuals for their team domain, evaluate them on themselves