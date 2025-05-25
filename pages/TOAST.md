---
tags: db, Postgres 
---

- The Oversized-Attribute Storage Technique is a method that Postgres uses to store large values. instead of keeping it in the column, it keeps a pointer, and stores the actual data somewhere else, in a dedicated TOAST table (where it will be chunked nicely).
- not every data type supports it! only variable length ones