---
Title: Update Groups Without Logging Out
Author: Sumit Patel
---

_UseCase: After updating a group, you want to take effect of it without logging out._

1. Use `newgrp` command followed by group name you updated
```
newgrp <group>
```

2. Now check if changes were made.
```
id $USER 
```
