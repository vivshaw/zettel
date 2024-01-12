tags:: aws, cloud

- a tool for grouping AWS accounts
- has a **management account:** the account your created it with
- and any number of **member accounts**
- has a tree structure: **Organization Root** at the top, and **Organizational Units** below, that can contain accounts or other OUs
- enables consolidated billing
- adding existing accounts requires an invite, but you can create new accounts directly within the org
- the usual architectural pattern is to have just one designated login account to hold all the [[AWS/IAM]] identities, and use role switching to access the other AWS accounts