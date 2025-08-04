---
Title: "Fix go: go.mod file not found in current directory or any parent directory; see 'go help modules'"
Published: 2023-08-25
author: Sumit Patel
description: "1. First initialize `go mod`."
tags: ["go", "golang"]
---

1. First initialize `go mod`.

```bash
go mod init <file.go>
```

2. Install modules

```bash
go mod tidy
```

And you are done.


Reference: [ StackOverflow ](https://stackoverflow.com/questions/66894200/error-message-go-go-mod-file-not-found-in-current-directory-or-any-parent-dire)
