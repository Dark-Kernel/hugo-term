+++
title = "Decrypt firefox's & chrome's  saved passwords"
date = "2023-07-29"
author = "Sumit Patel"
tags = ["Firefox", "Chrome"] 
description = "Decrypting firefox/chrome saved passwords using available python tools."
+++


## Firefox 

There are many tools available out there to decrypt firefox passwords, but we will using [firefox_decrypt](https://github.com/unode/firefox_decrypt.git) tool. Which is efficient and fast.

Steps:

1. First clone it to local system and `cd` into it.

    ```bash
    git clone https://github.com/unode/firefox_decrypt.git 
    cd firefox_decrypt
    ```

2. Here we have our script `firefox_decrypt.py`, execute it with `-h` option to get help menu.

    ```bash
    python firefox_decrypt.py -h
    ```

3. Get all the available profiles using `-l` option.

    ```bash
    python firefox_decrypt.py -l 
    ```

4. Decrypt passwords, use any format like json, tabular, human, etc.

    ```bash
    python firefox_decrypt.py -f tabular
    ```

5. Select your profile number 1 / 2 / 3 ... 

And voila, you have your passwords.



## Chrome

There are tools too to decrypt google chrome's password, and we will use [decrypt-chrome-passwords](https://github.com/ohyicong/decrypt-chrome-passwords)

Steps: 

1. First clone the repository to local and `cd` into it.

    ```bash
    git clone https://github.com/ohyicong/decrypt-chrome-passwords
    cd decrypt-chrome-passwords
    ```

2. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

3. Decrypt passwords using `decrypt_chrome_password.py`.

    ```bash
    python decrypt_chrome_password.py
    ```

 And now, we have all the credentials.


## How to secure your passwords?

We just saw how we can easily decrypt passwords from browser dumps, so now to avoid this kinds of thing we can secure our passwords using either ways

#### Firefox 

- Using extensions: Bitwarden, 1Password, Lastpass, etc.
- Using Primary/Master under settings ->  Privacy & security -> Login & Passwords.

#### Chrome

- Using extensions same as firefox.
> chrome doesn't provide built-in feature of master/primary password. 



So that's it. 

