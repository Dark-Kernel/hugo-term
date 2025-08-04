---
Title: "Install .deb in Arch"
Published: 2025-06-25
author: Sumit Patel
description: "1. It's just an archive"
tags: ["deb", "arch"]
---

1. It's just an archive

```
bsdtar -xf "package_0.1.0-1_amd64.deb" data.tar.xz
tar xf data.tar.xz
```

[--more--]

this will give `usr` directory containing binary in `usr/bin/` and other data in `usr/share`


```
❯ tree usr
usr
├── bin
│   └── somebinary
└── share
    ├── applications
    │   └── io.github.some.package.desktop
    ├── doc
    │   └── package
    │       └── copyright
    └── icons
        └── hicolor
            └── scalable
                └── apps
                    └── io.github.some.package.svg

10 directories, 4 files
```

2. One liner:

```
bsdtar -O -xf "package.1.0-1_amd64.deb" data.tar.xz | bsdtar -xf -
```
