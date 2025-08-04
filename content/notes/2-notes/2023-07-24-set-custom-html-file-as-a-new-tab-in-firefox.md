---
Title: "Set custom HTML file as a new tab in Firefox"
Published: 2023-07-24
author: Sumit Patel
description: "You might want to set up your custom HTML page which contains all the links which you want to access frequently or might want to use [StartTree](https"
tags: ["firefox", "html"]
---

You might want to set up your custom HTML page which contains all the links which you want to access frequently or might want to use [StartTree](https://github.com/Paul-Houser/StartTree) and something like that. [--more--]

We will be using AutoConfig, which is used to set and lock preferences that are not covered by group policy,
This requires an autoconfig.js file in the "defaults/pref" folder where the channel-prefs.js file is located that specifies to use autoconfig.cfg.

### Steps: 

1. Go the settings → Home → Set HomePage and new window  => cutom_urls → Enter the file path.

2. Set new tab to `Firefox Home`.

3. Make sure no other extension is managing your new tab, Go to Settings → Extension.

4. Create autoconfig.cfg file 

```bash
sudo vim /usr/lib/firefox/autoconfig.cfg
```  

Paste this:

```
//
var {classes:Cc,interfaces:Ci,utils:Cu} = Components;

/* set new tab page */
try {
  Cu.import("resource:///modules/AboutNewTab.jsm");
  var newTabURL = "file:///home/stroky/.cache/StartTree/index.html";
  AboutNewTab.newTabURL = newTabURL;
} catch(e){Cu.reportError(e);} // report errors in the Browser Console
```

    


5. Then create autoconfig.js

```
sudo vim /usr/lib/firefox/defaults/pref/autoconfig.js
```

Paste this:

```
// *First line must be a comment*
pref("general.config.filename", "autoconfig.cfg");
pref("general.config.obscure_value", 0);
pref("general.config.sandbox_enabled", false);
```


6. Quit the Firefox, and relaunch it.


And we are done.
&nbsp;
_______
Reference: 
[Mozilla support](https://support.mozilla.org/en-US/questions/1283835) |
[AutoConfig Docs](https://support.mozilla.org/en-US/kb/customizing-firefox-using-autoconfig)
