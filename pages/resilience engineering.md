---
tags: engineering
alias: reseng
---

- important thinkers
	- [[Erik Hollnagel]]
	- [[David D. Woods]]
- [[resilience]], as applied to the discipline of engineering
	- not to be confused with [[psychological resilience]]!
- questions we might ask:
	- what happens in the system?
	- what happens in the environment the system lives in?
	- are we looking at function or structure?
- 4 cornerstones of resilience engineering, from [[Hollnagel]]:
	- knowing what has happened
	- knowing what to expect
	- knowing what to look for
	- knowing what to do
- or, SAAL:
	- **sensing** - monitoring the system's state. could be quantitative or qualitative data. might involve analysis or communication of that data
	- **anticipating** - imagining possible outcomes. is forward-looking in time. might involve making assumptions, like modeling or simulating. might involve making a strategy. might involve reasoning about frequency.
	- **adapting** - changing the system's state to improve performance. might be adapting to either known or unknown circumstances. could involve prepared responses. may be an activation threshold. might involve readiness resources.
	- **learning** - creating new knowledge to inform the system. we might ask: how? why? how often? what went right? what went wrong? making use of the new knowledge might involve a cycle of integration -> implementation -> verification -> maintenance
- it's just as important, if not moreso, to look at _what goes right_, not just what goes wrong!
- we might need to look at the same system from different perspectives- individual vs. group, interior vs. exterior. these perspectives are influenced by human values, time, space... how humans assign meanings matters, not just technical measurement. some of those lenses and what they might guide us to think about:
	- individual interior: beliefs & attitudes, pathologies, fears, personal tastes
	- group interior: ideologies & worldviews, shared values, understandings, disagreements
	- individual exterior: behaviors impacted, behaviors involved, health impact
	- group exterior: ecological systems, social systems, economic systems, institituional systems. the "foo-technical" world that intersects with our system.