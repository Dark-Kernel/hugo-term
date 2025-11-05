---
Title: Easy ssh port forwarding
Author: Sumit Patel
---

1. Forward port server port (80) to localhost (8111).
```
ssh -L 8111:localhost:80 user@server
curl "http://localhost:8111" # on host
```
> _Your server:80 is mapped to localhost:8111._
> _Now in your host system you can access your server's local service._
> _[host]8111---<----[ssh]---<--80[server]_


2. Forward localhost port (5000) to server port (8011).
```
ssh -R 8011:localhost:5000 user@server
curl "http://localhost:8011" # on server
```
> _Your localhost:5000 is mapped to server:8011._
> _Now in server you can access your host systems local service._
> _[host]5000---->---[ssh]--->---8011[server]_
