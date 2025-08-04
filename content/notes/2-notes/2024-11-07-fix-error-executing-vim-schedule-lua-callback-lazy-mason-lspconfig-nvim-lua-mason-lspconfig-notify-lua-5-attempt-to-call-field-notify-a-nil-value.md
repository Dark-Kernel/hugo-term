---
Title: "Fix Error executing vim.schedule lua callback: ...lazy/mason-lspconfig.nvim/lua/mason-lspconfig/notify.lua :5: attempt to call field 'notify' (a nil value)"
Published: 2024-11-07
author: Sumit Patel
description: "1. Open init.vim and add this line"
tags: ["nvim", "error"]
---


1. Open init.vim and add this line

```
lua require('lspconfig').lua_ls.setup({})
```

Reference: [Reddit](https://www.reddit.com/r/neovim/comments/15jceyb/lspconfig_error_attempt_to_index_local_user/)
