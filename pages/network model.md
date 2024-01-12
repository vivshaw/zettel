tags:: db
aliases:: CODASYAL model

- a generalization of the older [[heirarchical model]]
- stores data in records that can each have any number of parents and children. they reference them via pointers
- to find records, you must walk a path through the data, traversing pointer-by-pointer
- competed with the [[relational DB]] and lost! it had better performance on limited hardware, but was much harder to use and less flexible.