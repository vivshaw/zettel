---
tags: linux, hardware
---

- LVM lets you group one or more physical volumes or partitions into a *volume group*, then define any number of *logical volumes* you like atop that
- you can freely resize logical volumes, as long as there's space
	- but you need to resize the [[FS]] too! use `resize2fs`
- utils:
	- `pvdisplay` will show you configured physical volumes
	- `vgdisplay` will show you configured volume groups
	- `pvcreate` creates physical volumes
	- `vgcreate` creates volume groups
	- `lvcreate` creates logical volumes
	- `lvresize` resizes existing logical volumes
	- `resize2fs` resizes filesystems to fit the LV they live on