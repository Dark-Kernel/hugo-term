+++
title = "Markdown test"
author = "Sumit Patel"
+++



### List 


1. item1
2. Item2

* Bullet

> Block quote

```html
  // your code here
```

```bash:code.sh
#!/bin/bash

echo "Hello world"
exit 0;
```


### Code block title

{{< code language="css" title="Really cool snippet" id="1">}}
pre {
  background: #1a1a1d;
  padding: 20px;
  border-radius: 8px;
  font-size: 1rem;
  overflow: auto;

  @media (--phone) {
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  code {
    background: none !important;
    color: #ccc;
    padding: 0;
    font-size: inherit;
  }
}
{{< /code >}}


{{<code language="bash" title="Simple cool shell script">}}
#!/bin/bash

echo "Hello World"
exit 0;
{{< /code >}}



{{< disqus >}}

