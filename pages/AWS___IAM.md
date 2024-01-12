tags:: aws, security

- **Identity and Access Management** lets you set up users, roles, and groups within your AWS account.
- IAM is a globally resilient service, but each AWS account has its own dedicated IAM instance
- IAM is cost-free
- IAM is fully trusted by your AWS account- this means you can use an IAM user, role, or group to do anything you need to do within AWS
- types of IAM identity:
	- **user:** represents a human or application that needs access to your account.
		- for long-term use by a specific principal
		- 💡**you can only have 5000 users per account**
		- 💡**a user can only be in 10 groups**
	- **group:** a collection of related users- e.g., finance team, dev team, etc.
		- not a principal of its own!
		- there's no default "All Users" group- if you want one, you have to make and manage it.
		- 💡**there's a limit of 300 groups per account!** but, you can file a ticket for an increase
		- 💡**groups can't have nesting!**
	- **role:** can be used by AWS services, or to grant external access to your account
		- typically shared by multiple principals
		- they are short-term. you assume a role, you use that role's perms for a little while, then you are no longer that role
		- has a **trust policy**, which says who can assume the role, and a **permissions poliy**, which says what the role can do
		- can use 'em to link up an external [[IDP]] with AWS, or for situations with >5000 users
		- a **Service-Linked Role** is tied to a specific service. might either be created by that service, or by you. can't delete 'em until they're no longer used.
			- you can use the PassRole permission to let users attach a role to a service
- IAM manages each identity's permissions with **policies**- these are documents granting or denying access to AWS services
- 3 roles of IAM:
	- **an IDP** (identity provider)- creates, changes, and deletes identities
	- **authentication**- proves that you are the identity you claim to be
	- **authorization**- allows or denies access to resources
- **access keys:**
	- an IAM user may have a maximum of 2 access keys configured
	- an access key must be deactivated before it can be removed
- **IAM Policies** are attached to identities, and written in JSON.
	- has a version and one or more statements
	- each statement grants or deny permissions to an AWS resource, like so:
		- **Sid:** optional field, naming what this statement does
		- **Affect:** allow or deny the action?
		- **Action:** what actions are covered by this statement?
		- **Resource:** what AWS resources are covered by this statement? use [[AWS/ARN]] to reference specific resources.
	- how are conflicts resolved? via a cascade in this order:
		- explicit denies
		  logseq.order-list-type:: number
		- explicit allows
		  logseq.order-list-type:: number
		- default, implicit deny
		  logseq.order-list-type:: number
	- two main types of policies: **inline**, which are attached directly to identities, and **managed**, which are reusable
		- since managed are reusable and easier to update, you should default to these!
		- inline should be used just in case of exceptions
		- AWS gives you a default set of managed policies, but you can also create your own