---
tags: Linux, os
---

- if I need to increase the file descriptor limit, I can use [[systemctl]]: `sysctl fs.inotify.max_user_watches=524288` or similar