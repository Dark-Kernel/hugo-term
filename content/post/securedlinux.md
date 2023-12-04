---
title: "Secure Your Linux Server"
date: 2023-12-04
draft: false
author: "Sumit Patel"
tags: ["linux", "server", "secure", "ssh", "firewall" ] 
description: "Secure you linux server with simple steps."
cover: /isSecured.jpg
---


Almost everyone thinks Linux is more secure, right? Well, hold your penguins, because the truth is as slippery as a buttered-up Tux sliding on ice.

# Is linux actually secured?


Simple answer No. yeah, Linux is considered secure, but not straight out of the box, particularly when dealing with minimalist distributions like Arch, Gentoo, and Void Linux. Which ships with literally nothing out of the box.
Not even a firewall :) Shocking, I know. In this case, Windows suddenly looks like it's rocking a cyberpunk suit, and Linux seems to have left the house without pants.

{{< figure src="/window-cyber.jpg" alt="Hello Friend" position="center" style="border-radius: 8px;" caption="cyberpunk windows" >}}

> Yeah, your whole life was a lie :)

But wait, before you hit the panic button and decide to replace your Linux partition with Windows, there's a plot twist. If you're an everyday Linux user, you're still in the safe zone. Why? 

Let's rewind to the 1990s when Windows dominated the desktop operating system market with its proprietary MS-DOS. Windows maintained this monopoly for years, making Linux a relatively secure option for normal users. Confused? Allow me to elaborate.

In this scenario, users and the operating system share the stage, but there's a third player – hackers. With the majority using Windows, hackers found it convenient to focus on exploiting vulnerabilities in a single OS.

This led to a period where Windows users were constantly under attack.


But, and it's a significant *but,* it doesn't mean Linux lacks security; it's simply not inherently secure out of the box. With the right configurations and additional security measures, Linux can surpass Windows security levels by a considerable margin. So, while Windows may seem like it's dressed in cyber armor from the get-go, Linux is more of a security project waiting for customization.


But wait, this doesn't mean Linux is just chilling in a hammock, sipping coconut water, and avoiding cyber-attacks. No, it's like the VIP of hacking targets, especially on servers. Linux is like the hottest party spot, and hackers RSVP every day. 




Well, you got the problem; but what about the solution? 

**Here you go** 

# Secure your linux server.

There are plenty of ways you can secure your server but here i will mention only the important one.

# 1. Network Filtering 

   You might already heard about this thing, but most likely never tried ;)

   It is nothing but securing linux in network.

   For this just open your `/etc/sysctl.d/local.conf`

    
   {{< code language="bash" title="/etc/sysctl.d/local.conf" id="1">}}
   
   # Turn on Source Address Verification in all interfaces to
   # prevent some spoofing attacks
   #net.ipv4.conf.default.rp_filter=1
   net.ipv4.conf.all.rp_filter=1
   
   # Ignore echo broadcast requests to prevent being part of smurf attacks
   net.ipv4.icmp_echo_ignore_broadcasts=1
   
   # Enable TCP/IP SYN cookies to protect against SYN flood attacks.
   # See http://lwn.net/Articles/277146/
   net.ipv4.tcp_syncookies=1
   
   # ipv6 settings (no autoconfiguration)
   net.ipv6.conf.default.autoconf=0
   net.ipv6.conf.default.accept_dad=0
   net.ipv6.conf.default.accept_ra=0
   net.ipv6.conf.default.accept_ra_defrtr=0
   net.ipv6.conf.default.accept_ra_rtr_pref=0
   net.ipv6.conf.default.accept_ra_pinfo=0
   net.ipv6.conf.default.accept_source_route=0
   net.ipv6.conf.default.accept_redirects=0
   net.ipv6.conf.default.forwarding=0
   net.ipv6.conf.all.autoconf=0
   net.ipv6.conf.all.accept_dad=0
   net.ipv6.conf.all.accept_ra=0
   net.ipv6.conf.all.accept_ra_defrtr=0
   net.ipv6.conf.all.accept_ra_rtr_pref=0
   net.ipv6.conf.all.accept_ra_pinfo=0
   net.ipv6.conf.all.accept_source_route=0
   net.ipv6.conf.all.accept_redirects=0
   net.ipv6.conf.all.forwarding=0
   
   {{< /code >}}
   

# 2. Secure SSH server

   1. Edit the configuration file 
       ```bash
       sudo vim /etc/ssh/sshd_config
       ```

   2. Toggle these options

       ```bash
       PermitRootLogin no
       X11Forwarding no
       AllowUsers <your username>
       PubkeyAuthentication yes
       ChallengeResponseAuthentication no
       Port 2202 # use random port instead of 22 
       ```

   3. Restart your sshd service.

       ```bash
       # For systemd
       sudo systemctl restart ssh.service

       # For sysVinit
       sudo service sshd restart

       # For runit
       sudo sv restart sshd
       ```

       Make sure you have created your keys, then add your host system's key to `.ssh/authorized_keys` file in server or use below command
       ```bash
       ssh-copy-id -i ~/.ssh/id_rsa.pub <server ip>
       ```

# 3. Setup firewall

   Now, here you have two choices: 
   * Use ufw
   * Use Iptables directly

   For UFW.

   ```bash
   sudo apt install ufw -y
   ```

   Enable it.

   ```bash
   sudo ufw enable
   ```



# 4. Limit SUDO

   To limit the sudo access use the `sudoers` file.

   Edit it.

   ```bash
   sudo vim /etc/sudoers
   ```

   Add your user with privileges.

   ```bash
   ## User privilege specification
   
   root ALL=(ALL:ALL) ALL
   <user> <privileges>
   ```



# 5. Use SELinux

   Final suggestion, it is very powerful but sometimes it's annoying. Without learning it don't install it on your server, or you will waste your day in figuring out why you are not able to access your nginx webserver on port 80 ;)

 
# 6. Other Tips & Tools
    
   - Stop & disable all unnecessary services, this will probably reduce the attack surface.
   - Enforce strict memory access controls.

   After all these, you can also configure, 

   * Security & system auditing tool - `lynis`
   * Intrusion detection system - `psad`
   * Eliminate bruteforce - `fail2ban`
    

--- 




##### In the end, Linux isn't just secure; it's a security ninja doing a moonwalk while wearing a fedora 󰱸 . 

{{< image src="/linux-punk.jpg" alt="Hello Friend" position="center" style="border-radius: 8px;" >}}





<!-- But this doesn't means Linux is not targetted, opposite it is more targgeted but on servers Linux is mostly used in server, it is targeted every day, hackers find vulnerability for linux and our linux community fixes those loopholes ;) -->


<!-- From 1990, Windows captured the market of desktop operation system and have the monopoly till now. Though I still respect windows because in the world of Unix and Linux windows introduced it's own msdos which is now running on almost 90% of desktop computers. -->
<!-- And this makes linux secured for normal users, didn't got? let me explain. --> 


<!-- In this scenario between user and OS one more enitity exists called hackers, as majority of user are using windows so they started targeting windows. As it makes easier for hackers to target only one OS. So, after that windows users were under the attack. -->


<!-- But, but, but, it doesn't mean linux is not secured, it is *not secured by default*, but we can secure it and it can be secured 100x of windows. -->




