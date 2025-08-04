---
Title: "Linux stuffs"
Published: 2023-07-22
author: Sumit Patel
description: "```bash"
tags: ["linux"]
---


```bash
echo "Hello world"
```

We are going to learn: [--more--]

1. User / group
2. grep, awk, find.
3. File permission
4. ssh/scp
5. systemctl


* #### Groups: collection of users

    ```bash
    sudo groupadd devops
    ```
    use the `/etc/group` file to get groups
    > **Whenever you create a user it creates groups also with the same name.**


    * Add user to group


        whenever you add a user to a group you modify the user.

        ```bash 
        sudo usermod -aG devops user1
        ```
   - To add multiple users, we can also use gpasswd to add user

        ```bash
        sudo gpasswd -M user1,user2,user3 testers
        ```
   - Delete user form group

        ```bash
        sudo gpasswd -d user2 testers
        ```
    - Delete group

        ```bash
        sudo groupdel testers
        ```
    - Use chgrp to change  group of file

        ```bash
        sudo chgrp tester file.txt
        ```
###### 
___

* #### File permissions:
    
    Numeric Permissions:

    * r - read = 4
    * w - write = 2
    * x - execute = 1 
   
    &nbsp;

     - There are three set of permissions for: 

        * U - User/Owner 
        * G - Group
        * O - Others
    
    &nbsp;
    
    - Combinations

        _ U _ . _ G _ . _ O _ => rwx rwx rwx 

                        
        ##### Example: 

        U - read+write = 4+2 => 6 
    
        G - read+executable = 4+1 => 5

        O - read = 4 => 4

        > Final permission numeric == 654 
    
    &nbsp;

    - User `chmod` command to modify permissions

        ```bash
        chmod 700 file.txt
        ```
&nbsp;
---


* #### Find files

    - Grep: To find anything inside file or name of files.
    
        + Find some keyword or filename in directory.

        ```bash
        grep -r keyword /home/ubuntu/
        ```
        `-r` is for searching recursively inside directotries

        + grep something inside file

        ```bash
        grep keyword file.txt
        ```
        + Search case insensitive

        ```bash
        grep -i keyword file.txt
        ```
        ``-i`` stands for case insensitive, by default grep is case sensitive.

        &nbsp;


    * AWK:

        + Find `TRACE` from log and print column 1,2,5 

        ```bash
        awk '/TRACE/ {print $1,$2,$5}' errors.log
        ```
        + Get the exact line number

        ```bash
        awk '/TRACE/ {print NR,$1,$2,$5}' errors.log
        ```
        + User condition using `NR` => row number 
        
        ```bash
        awk 'NR>=1 && NR<=20 && /TRACE/ {print NR,$1,$2,$5}' errors.log
        ```

    &nbsp;



    * Find: 

        + Find files with specific extension 

            ```bash
            find *.txt
            ```

        + Find files in some directory with specific ending

            ```bash
            find dir/ *.log
            ```

        + Find files by a particular owner

            ```bash
            find dir/ -user ubuntu
            ```

        + Find files by a particular group

            ```bash
            find dir/ -group devops
            ```

    &nbsp;


* #### SSH:

    * Keys: 
        + Public key (id_rsa.pub)
        + private key (id_rsa)
            
            > Public key must be known by the server where you want to connect, and you must also have private key to connect.
        
        &nbsp;
    * Create keys:

        ```bash
        ssh-keygen
        ```
   
        Keys are stored in `~/.ssh/` directory. 

    * Connect using keys:

        1. Permission must be 400

            ```bash
            chmod 400 key.pem
            ```
        2. connect 

            ```bash
            ssh -i /path/to/key.pem user@ipaddress
            ```
        3. Types `yes` when asked.


    
    * scp from host system to server

        ```bash
        scp -i "key.pem" file.txt user@ipadd:/home/user/file.txt
        ```
    * scp from server to our host system

        ```bash
        scp -i "key.pem" user@ipadd:/home/user/file .
        ```

       &nbsp;

* #### Systemctl

    It is a Service controller, services like `docker`, `apache2`, `sshd`, `nginx`, etc.

    * Start any service
      
        ```bash
        sudo systemctl start <service> 
        ```
    
    * Stop any service
      
        ```bash
        sudo systemctl stop <service>
        ```
    
    * Check status of any service
        
        ```bash
        sudo systemctl status <service>
        ```

