---
title: "Firefox Hardening"
date: 2023-07-30T16:43:11+05:30
draft: false
author: "Sumit Patel"
tags: ["Firefox", "Linux"] 
description: "Making firefox more secure and usable by removing some craps and toggling security preferences using user.js file"
---


### Using firefox?

Firefox is the best browser for linux nerds and others who want browser other than chromium, it's being almost 2 decades of firefox and now it is filled with some craps which needs to be removed to increase the quality.

> Mozilla and Google have extended their current search deal to keep Google as the default search engine provider inside the Firefox browser until at least 2023, with an estimated price tag of around $400 million to $450 million per year.

Well, today we will see some of the steps to increase the security and surfing experience of firefox.

##  Update the user.js profile.


1. . Visit `about:profiles` on your firefox, don't touch any profile, create new.

2. click on `open directory`, it will open the location where that user profile exists.

3. create new file `user.js` in that directory

    ```bash
    vim user.js
    ```

Now here the game starts,

This file is used to toggle and set multiple preferences for firefox which cannot be changed directly using firefox ui.
So here we will be defining some the important user_preferences.

- Increase speed.

    ```javascript
    user_pref("nglayout.initialpaint.delay", 0);
    user_pref("nglayout.initialpaint.delay_in_oopif", 0);
    user_pref("content.notify.interval", 100000);
    user_pref("browser.startup.preXulSkeletonUI", false);
    ```

- Set the browser cache limit

    ```javascript
    user_pref("browser.cache.memory.max_entry_size", 153600);
    ```

- Increase tracking protections

    ```javascript
    user_pref("browser.contentblocking.category", "strict");
    user_pref("urlclassifier.trackingSkipURLs", "*.reddit.com, *.twitter.com, *.twimg.com, *.tiktok.com");
    user_pref("urlclassifier.features.socialtracking.skipURLs", "*.instagram.com, *.twitter.com, *.twimg.com");
    user_pref("privacy.query_stripping.strip_list", "__hsfp __hssc __hstc __s _hsenc _openstat dclid fbclid gbraid gclid hsCtaTracking igshid mc_eid ml_subscriber ml_subscriber_hash msclkid oft_c oft_ck oft_d oft_id oft_ids oft_k oft_lk oft_sk oly_anon_id oly_enc_id rb_clickid s_cid twclid vero_conv vero_id wbraid wickedid yclid");
    user_pref("browser.uitour.enabled", false);
    user_pref("privacy.globalprivacycontrol.enabled", true);
    user_pref("privacy.globalprivacycontrol.functionality.enabled", true);
    ```

- Avoid the usage of disk cache

    ```javascript
    user_pref("browser.cache.disk.enable", false);
    user_pref("browser.privatebrowsing.forceMediaMemoryCache", true);
    user_pref("browser.sessionstore.privacy_level", 2);
    ```

- Disable search prefecher/predictor 

    ```javascript
    user_pref("network.http.speculative-parallel-limit", 0);
    user_pref("network.dns.disablePrefetch", true);
    user_pref("browser.urlbar.speculativeConnect.enabled", false);
    user_pref("browser.places.speculativeConnect.enabled", false);
    user_pref("network.prefetch-next", false);
    user_pref("network.predictor.enabled", false);
    user_pref("network.predictor.enable-prefetch", false);
    ```

- Disable annoying search suggestions like: topsites, search engines, etc.

    ```javascript
    user_pref("browser.search.separatePrivateDefault.ui.enabled", true);
    user_pref("browser.urlbar.update2.engineAliasRefresh", true);
    user_pref("browser.search.suggest.enabled", false);
    user_pref("browser.urlbar.suggest.quicksuggest.sponsored", false);
    user_pref("browser.urlbar.suggest.quicksuggest.nonsponsored", false);
    user_pref("security.insecure_connection_text.enabled", true);
    user_pref("security.insecure_connection_text.pbmode.enabled", true);
    user_pref("network.IDN_show_punycode", true);
    user_pref("browser.urlbar.suggest.engines", false);
    user_pref("browser.urlbar.suggest.topsites", false);

    /* Adding some features */
    user_pref("browser.urlbar.suggest.calculator", true);
    user_pref("browser.urlbar.unitConversion.enabled", true);
    ```


- Disable cross site scripting

    ```javascript
    user_pref("network.auth.subresource-http-auth-allow", 1);
    user_pref("pdfjs.enableScripting", false);
    user_pref("extensions.postDownloadThirdPartyPrompt", false);
    user_pref("permissions.delegation.enabled", false);
    ```

- Disbale accessibility and location services.

    ```javascript
    user_pref("accessibility.force_disabled", 1);
    user_pref("identity.fxaccounts.enabled", false);
    user_pref("browser.tabs.firefox-view", false);
    user_pref("permissions.default.desktop-notification", 2);
    user_pref("permissions.default.geo", 2);
    user_pref("geo.provider.network.url", "https://location.services.mozilla.com/v1/geolocate?key=%MOZILLA_API_KEY%");
    user_pref("geo.provider.ms-windows-location", false); // WINDOWS
    user_pref("geo.provider.use_corelocation", false); // MAC
    user_pref("geo.provider.use_gpsd", false); // LINUX
    user_pref("geo.provider.use_geoclue", false); // LINUX
    user_pref("permissions.manager.defaultsUrl", "");
    user_pref("webchannel.allowObject.urlWhitelist", "");
    ```

- Disable pockets

    ```javascript
    user_pref("extensions.pocket.enabled", false);
    ```


By adding these preferences your firefox is now more secure, but you also need some other changes. 

### Ad-blocker (recommended)

1. UBlock origin 
2. AdGuard AdBlocker

Both are free and opensource.


### Search engine

Even after all these you need to change one more thing i.e `search engine`. By default google is set which sucks lot of user data and also show the ads in search results.
That's why we need to change search engine also.

1. [SearXNG](https://github.com/searxng/searxng)
2. [Startpage](https://www.startpage.com/en/)
3. [Brave](https://search.brave.com/default)

These are few safe search engines with minimal look & great results without **ads**.

To add any search engine, 
 * first visit the page of it.
 * click on search bar and click on `add search engine..`.

{{< image src="/search-engine.png" alt="Hello Friend" position="center" style="border-radius: 8px;" >}}


### Customize look with pywal (optional)

To customize look of firefox you can use pywal to generate colorscheme according to your wallpaper which can improve the look.
There's an extension for this called [`pywalfox`](https://addons.mozilla.org/en-US/firefox/addon/pywalfox/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search) which will be using.

* Install pywalfox
```bash
pip install pywalfox --break-system-packages
```

- Run command

```bash
pywalfox install
```

- Add the extension then, open it and click `Fetch pywal colors`.


### Set custom home/new tab (optional)

Read this [blog](/post/firefox-custom-new-tab-file/) to configure it.


### Set master password.

Yes, you need to set master password, by default when you save password it is stored in firefox's profile directory; which can be decrypted easily using tools like [firefox_decrypt](https://github.com/unode/firefox_decrypt.git); [see demo](/post/decrypt-browser-pass)

- Go to settings -> Privacy & Security -> under 'Login and Passwords' section.
- Check 'Use Primary Password' -> Enter you super secret master password.

&nbsp;

So that's how you can make your firefox more secure and usable.

&nbsp;

---

Reference: 
[Betterfox](https://github.com/yokoffing/Betterfox.git) | 
[Mozilla Support](https://support.mozilla.org/en-US/kb/how-to-fix-preferences-wont-save#)



