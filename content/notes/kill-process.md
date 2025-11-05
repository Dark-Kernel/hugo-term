---
Title: Kill process on specific port
Author: Sumit Patel
---

1. Kill process on port 80
```bash
kill -9 $(lsof -t -i:80)
```

2. Another method: 
```bash
fuser -k 80/tcp
```



