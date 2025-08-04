---
Title: "Shell Scripting"
Published: 2023-07-23
author: Sumit Patel
description: "Shell provides an interface between the user and the kernel and executes programs called commands."
tags: ["shell", "bash"]
---

Shell provides an interface between the user and the kernel and executes programs called commands.

Different shells:

* sh  => Bourne shell
* ksh => korn shell [--more--]
* bash => Bourne again shell
* csh => c shell
* zsh = z shell

Most popular one is `Bash` and it is used in shell scripting.


#### Script File 

1. Shell script file should end with `.sh` or it should have shebang `#!`.

    ```bash
    #!/bin/bash

    echo "Hello world"
    ```

    Shebang defines the interpreter to use to interpret the script.

2. Script is exectued line by line.
3. It also have programming concepts like conditional statement, loops, etc.
4. To execute the script you can use either ways
    
    1. Make it executable and execute like binary
        
        ```bash
        chmod +x script.sh
        ./script.sh
        ```
    2. Execute directly using interpreter 
        
        ```bash
        bash script.sh
        ```

---
&nbsp;

* #### Variables

    Variable store some values
    ```bash
    #!/bin/bash

    name="tester"
    echo "hello $name"

    read -p "Enter you age: " age
    echo "your age is $age"
    ```
    - read: It is used for user input, `age` is variable in which we are storing that user input.
    - $ is use to access variable content.

&nbsp;

* #### Arguments

    Arguments are values which is provided at runtime

    ```bash
    #!/bin/bash
    
    echo "File name is: $0"
    echo "Hello $1"
    echo "Creating file $2" && touch $2 
    ```
    
    Execute 
    
    ```bash
    ./script tester myfile2
    ```
    
    Output

    ```bash
    File name is: /tmp/script
    Hello tester
    Creating file myfile2
    ```
    - $1,$2,.. $n This is how we access arguments.
    - $0 is the first argument, which is the name of file.
    - $# This returns the count of arguments.
    - $@ This represents all the arguments.
   
   &nbsp;
        
---
&nbsp; 

* #### Loops

    Execute until a specific condition is met.
    
    ##### Example:
    ```bash
    #!/bin/bash

    dir=/home/user/scripts/*.sh
    for files in $dir
    do
        echo $files
    done
    ```
    This script print all .sh files in that directory.
    
    ##### Example 2: Script to add multiple users.

    ```bash
    #!/bin/bash

    read -p "Enter the number of users: " user_num

    for (( i=1; i<=$user_num; i++ ))
    do
        read -p "Enter username: " user
        read -s -p "Enter pass: " pass
        sudo useradd -m $user
        echo "$user:$pass" | sudo chpasswd
        echo "Done"
    done

    cat /etc/passwd | grep $user
    ```

&nbsp;

* #### If else statement

    Execute something on some condition

    ```bash
    #!/bin/bash

    name="tester"

    if [ $name == "tester" ]
    then
            echo "yes, tester logged in"
    else 
            echo "Invalid user"
    fi
    ```

    &nbsp;
---
    
#### Example script.

1. Install  nginx and serve page using script.
    ```bash
    # Update system
    sudo apt update

    # Install nginx
    sudo apt install nginx -y

    # Start & enable nginx service
    sudo systemctl enable --now nginx

    # Serve the page
    sudo rm /var/www/html/*.html && echo "Hello world" | sudo tee /var/www/html/index.html 
    ```

2. Backup script

    ```bash
    #!/bin/bash

    src=/home/user/devops/script
    tgt=/home/user/backups
    filename=$(date +'%d-%m-%Y').tar.gz
    tar -cvzf $tgt/$filename $src 

    echo "Completed!"
    ```

    You can create crontab for this.

    ```bash
    crontab -e
    ```
    ```cron
    * * * * * /path/to/backup/script
    ```

That's it.
