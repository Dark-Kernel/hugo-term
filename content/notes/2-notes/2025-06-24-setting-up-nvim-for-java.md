---
Title: "Setting up nvim for java"
Published: 2025-06-24
author: Sumit Patel
description: "1. Install`jdtls` from the mason using `:MasonInstall jdtls` or `:Mason`"
tags: ["nvim", "jdtls", "java"]
---

1. Install`jdtls` from the mason using `:MasonInstall jdtls` or `:Mason`
2. Then add jdtls in list of lsp's :

```lua
local servers = { 'clangd', 'rust_analyzer', 'pyright', 'ts_ls', 'gopls', 'jdtls' }
```
[--more--]

2. If your are working with just basic java files, Initialize git in you working directory and create .project file. 

```
git init
touch .project
```

3. Now, open any java file and check if `jdtls` lsp is attached using `:LspInfo`, check for this:

```
- 1 client(s) attached to this buffer
- Client: `jdtls` (id: 1, bufnr: [1])
```

if `bufnr` is > 0 then, it worked.

Reference: [ChatGPT](https://chatgpt.com/share/685aaac3-16e4-8010-88d2-1a02989e89e5)
