---
tags: aws, cloud, security
alias: service control policy
---

- SCPs are **account permissions boundaries**. they limit what the account can do.
	- this *includes* the account root user!
	- they don't grant permissions. they just determine what can and can't be allowed in identity policies.
- can be attached to an [[AWS/Organization]], or to an organizational unit (OU), or to an individual account
	- the management account is never affected by them!
- can be used in two ways:
	- **deny list** - the default. your account will come with a `FullAWSAccess` policy, and you'll add any denials you want. explicit denials will always win over the allow
		- less secure, but less admin overhead!
	- **allow list** - remove the `FullAWSAccess` policy. now you need to explicitly specify what you want to allow.
		- more secure, but more overhead- you can make mistakes and not allow the right things!
- how do they interact with [[AWS/IAM]] identity policies?
	- it's a Venn diagram. to allow an entity to do something, the identity policies must grant it *permissions*, and the SCP must not _forbid_ it. only doubly-allowed stuff is really allowed.