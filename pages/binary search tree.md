---
tags: data structures, tree (DS)
alias: BST
---

- a [[binary tree]] where every element in a node $n$'s left subtree is $\leq n$, and every element in the right subtree is $\geq n$. this is similar to a [[binary search]].
- you can iterate a BST in order easily, in $\Theta(n)$ time:
	- ```
	  iterate(n):
	  	if n != nil:
	        iterate(n.left)
	        print(n.key)
	        iterate(n.right)
	  ```
- the runtime of searching for an element is $O(h)$, where $h$ is the tree height
- you can find the maximum or minimum element by simply following the chain of left or right elements respectively. this is also $O(h)$
- you can find the next element in sorted order in $O(h):
	- ```
	  successor(n):
	  	if n.right != nil:
	      	return minimum(n.right)
	  	else:
	      	y = n.parent
	          while y != nil and n == y.right:
	          	n = y
	              y = y.parent
	          return y
	  ```
- to insert a node $n$, trace a path down the tree according to whether $n$ is larger or smaller until you hit a `nil`. this runs in $O(h)$.
- deletion is more complex. there are three cases:
	- if $n$ has no children, we can delete immediately.
	- if $n$ has one child, we can delete $n$ and elevate the child to take its place.
	- if $n$ has two children, we find its successor $m$ (in its right subtree). then:
		- $m$ replaces $n$
		- the rest of $n$'s right subtree becomes the new right subtree of $m$
		- $n$'s left subtree becomes $m$'s left subtree
- you can use a BST to implement a [[set]], [[dictionary]], or [[map (DS)]]
- one problem is, if your tree is really unbalanced, $h$ might be $\approx n$! that will give you bad performance. so, we may want a tree with a balancing mechanism.