---
tags: algorithm, math, compsci, search
---

- problem: given a sorted list of elements, does a given element exist in the list?
- we start by looking in the middle. if it's the right element, we end! otherwise, we check if the middle element was greater or lesser than our target, then go to the midpoint of the relevant half of the array and repeat.