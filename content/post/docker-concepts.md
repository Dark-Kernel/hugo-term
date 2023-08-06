---
title: "Docker"
date: 2023-08-06
draft: false
author: "Sumit Patel"
tags: ["Docker", "Networking"] 
description: "Almost Everything you need to know about docker."
---


# Docker

> These are required from fresher DevOps.

Used in deployment using containerization method. To run an application in isolated environment.


* Docker engine is connected to host kernel
* No need to allocate resources, Uses shared resources.

* Components: 
    1. dockerd -> Executed in background and use containerd to manage containers.
    2. dockercli -> an interface for docker.
    3. containerd -> lowest level.

> Docker engine is service which allow you to run any OS, which uses dockercli and dockerd

#### Basic commands:

* Run a container by pulling image:

    ```bash
    sudo docker run -d -e MYSQL_ROOT_PASSWORD=test@123 mysql:latest
    ```
* To get lists running containers:
    ```bash
    docker ps 
    ```
    You can use `-a` option to list stopped containers aswell.

* To get access to container use below command:

    ```bash
    docker exec -it <containerid> sh
    ```
* Command to stop & remove container
    ```bash
    # Stop
    docker stop <containerid>
    # remove
    docker remove <containerid>
    ```
* To remove all unused images.
    ```bash
    docker image prune
    ```
* To remove all stopped containers.
    ```bash
    docker container prune
    ```
> prune, can be used to remove unused images, containers, network, etc. Mostly used to clear the disk space.

* We can also force to remove
    ```bash
    docker image prune --all --force
    ```
 

&nbsp;

---

&nbsp;


## Docker Advanced.

> These are required from senior DevOps.

* Volumnes
* Network
* Compose (2/3 tier)
* Multistage docker build
* Docker push to docker hub


### 1. Docker Volumes

It stores a copy of your container to your system too.
So whenever docker container crashes this copy can be used.
> Data is stored in container till it is in running status, after container is exited data is gone. That's why docker volume is used to save data.


Example: 

1. Clone an app and deploy with docker.

    ```bash
    git clone https://github.com/LondheShubham153/django-todo-cicd.git
    cd django-todo-cicd
    docker build . -t django-app
    docker run -d -p 8000:8000 django-app:latest
    ```

    Now when if we create new container of same image, our data will be vanished. So to avoid this we can create and mount volume devices to containers to continue with same data.

2. Create directory, where we will store data.

    ```bash
    mkdir /var/django-app
    ```
3. Create volume 

    ```bash
    docker volume create django-app-volume --opt type=none --opt device=/home/user/django-app/ --opt o=bind  
    ```

    - device: location, s3, disk or direcory
    - o=bind: two way communication, if you update someting on device or container both will be synced.


4. List volumes, `local` is default volume.
    
    ```bash
    docker volume ls 
    ``` 

5. Mount volume to container.
    
    ```bash
    docker run -d --mount source=django-app-volume,target=/data -p 8000:8000 django-app:latest
    ```

    - target: to which we want to you want to store in volumnet

> Volume device data and container's data is synced in real time.

**Example:** 
* Get into container: 

    ```bash
    docker exec -it <id> bash
    ```
* Do some changes, like create new file:

    ```bash
    echo "super secret" > file.txt
    exit
    ```

Now, check on device location, and changes will be reflected there. Every data will be synced.
**This is called data persistence.**

&nbsp;

---


&nbsp;


### 2. Docker networking 

Used to create a network where we can connect multiple application.

Types: 

- Default bridge
- Custom bridge (User defined)
- Host network
- Mac VLAN network
- None
- Overlay
- IPVLan

When you install docker new interface is created something like `docker0`.

When you create new container, it is gone through docker network to access on other interfaces.

* List docker networks

```bash
docker network ls 
```
> By default 3 types of network are already present in docker, Other needs to be created. 
> **Bridge is used by default.**

#### 1. Default bridge: 

  Provide internet access from inside, other can't access from outside until you publish any port.
when you bridge network is used docker0 interface create a bridge network with your active interface and then we have to bind ports to access.

```bash
docker run -d -p 80:80 nginx
```


#### 2. Custom bridge

Used to create isolated network environment.
It is used to created a application group, where containers can access each other who are in that network

Create custom bridge:

```bash
docker network create myapp
```

Run container using custom bridge:

```bash
docker run -d --network myapp nginx
docker run -d --network myapp mysql 
``` 

Now nginx & mysql can communicate easily, even with name of container.

```bash
docker inspect myapp
```


#### 3. Host

```bash
docker run -d --network host nginx
```
When you using host network container directorly connects to your systems networks instead of docker0, This means that container is running same as an application which is using some port like nodejs app or mysql which are accessible on your host network.
It is running on hosts ip.

#### 4. Mac VLAN

**Modes: bridge & 802.1q**

If you want to associate your container with Mac address, to pretend like a device not container. 
It simply allows containers to have a Mac address this allow containers to appear as physical device.
> Directly connect you docker container with your physical network. (router,switch)

 
###### bridge (default):

Create network
```bash
docker network create -d macvlan \
--subnet=<subnet> \
--gateway=<gateway> \
-o parent=eth0 \
my-vlan 
```

- `-o` for options.
- parent is the physical network interface like wlan0, eth0. enp5s0, etc.

User network

```bash
docker run -itd --rm --network my-vlan \
--ip 192.168.0.33 
--name myapp
nginx
```

Now, if you try to ping your other network device from container you might face issue,

This is the downside of `Macvlan`: 
Your containers have different mac but they share same port socket on physical network, It breaks the security because you can have only 1 or 2 mac address on one port and that's what cause the issue.

To fix this we have to enable promiscuous mode. 

- First enable it on physical network
```bash
sudo ip link set enp0s3 promisc on 
```
- reboot your host.

Now it is directly connected to your home network/ physical network, You can directly use the ip.

###### 802.1q: 

By using second type you can create a subinterface from your physical which contains there own network.

* Create Macvlan with 802.1q mode network
```bash
docker network create -d macvlan \
--subnet=<subnet> \
--gateway=<gateway> \
-o parent=eth0.20 \
my-vlan 
```

#### 5. None

Used to create an application with no internet access, with no incoming and outgoing traffic. If you want to create a dummy data container you can use this.

```bash
docker run -d --network none nginx
```

#### 6. Overlay 

Used for communication between multiple docker daemon hosts. This helps containers running on different hosts to communicate easily.  Example: k8s cluster, docker swarm, etc.

**Create and use:**

```bash
docker network create --driver=overlay my-overlay-network
docker run -d --network=my-overlay-network my-service
```


#### 7. IPVLan

This solves the Macvlan problem promiscuous stuffs.

**Modes: L2 & L3**

###### L2: 
Its same like Macvlan, there are assingned mac, they allow the host to share its macaddress with the containers, It means your mac address with exactly match with your host but will have ip address on network.

**Create network:**

```bash
docker network create -d ipvlan \
--subnet=10.7.1.0/24 \
--gateway=10.7.1.3 \
-o parent=enp0s3 \
my-ipvlan
```

**Use in containers:**
```bash
docker run -itd --rm --network my-ipvlan \
--ip 10.7.1.92
--name myapp busybox
```


###### L3: 
Its all about layer3, We are connecting to host, host as a router. they connect to host physical network interfac. they connect to host physical network interface, This means no broadcast traffic not going to repond arp requests.
The problem is, it cannot access internet and not anyone can access it. Because it is not in routing table, then why to deploy? Everyting is a game of more control you can do some crazy isolation with your containers.

**Create network:**

```bash
docker network create -d ipvlan \
--subnet=192.168.94.0/24 \
-o parent=enp0s3 -o ipvlan_mode=l3 \
--subnet=192.168.95.0/24
my-ipvlanl3
```
- Here we used two subnets, because we have to do that if want to create more than 1 network which are going to use the same physical interface


**Use in container:**

```bash
docker run -itd --rm --network my-ipvlanl3 \
--ip 192.168.94.7
--name myapp
busybox
```
If you have more than one subnet you need to specify the ip address,
Here both the subnet can talk to each other.

Now, to give access to the internet we need add a new static routing in your router page.


---


&nbsp;

### 3. Docker compose.

Used to run multiple container/microservices and different tier application.


>3 tier application architecture:

    1. presentation layer/tier (UI/Frontend)
    2. Business layer/tier (Backend)
    3. Database layer/tier


>2 tier application
    
    1. Backend
    2. DB

> Configuration language: YML/YAML (key: value) 

We need YAML language to write docker-compose file, which contains all the stages and everything including ports, volumes, networks, etc.


Syntax:

{{< code language="yaml" title="docker-compose.yml" id="1">}}
version: '3'
services: 
    backend: 
        build: 
            context: . # Dockerfile exist in current dir.
        ports:
            - 5000:5000
    mysql:
        image: mysql:5.7
        volumes: 
            - mysql-data:/var/storage # to use volume
{{< /code >}}
Example: 

```bash
git clone https://github.com/LondheShubham153/two-tier-flask-app.git 
cd two-tier-flask-app
```
Create env file:
```bash
vim .env
```
{{< code language="env" title=".env" id="1">}}
MYSQL_HOST=mysql
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_DB=your_database
{{< /code >}}

To start container run: 
```bash
docker-compose up --build
```
To stop run:
```bash
docker-compose down
```

&nbsp;

---

&nbsp;

### 4. Multistage docker build

Multistage is used to reduce the size of docker image.
We use multiple `FROM` or base images for different steps as per requirements.
Dockerfile is single stage build.

we use `FROM` to get base image, after the work of base image is done, use another `FROM`.
So the first `FROM` becomes stage1 and compressed to binary, and is injected to next stage by using `COPY`.

#### Normal Single stage build:

{{< code language="dockerfile" title="Dockerfile" id="1">}}
FROM python:3.9
WORKDIR app
COPY . .
RUN pip install flask
CMD ["python","app.py"]
{{< /code >}}
Build: 
```bash
docker build . -t normal-flask
```
**size: 1.01GB**

#### After making it Multistage build: 

```dockerfile
# Stage 1
FROM python:3.9 AS big-stage

WORKDIR /app

COPY . .

# Stage 2
FROM python:3.9-slim-bullseye 

COPY --from=big-stage /app /app

RUN pip install flask

CMD ["python","app.py"]
```

Build: 
```bash
docker build . -t multi-flask
```

**size: 135M**

Check the difference: 

```bash
$ docker images | grep flask
multi-flask     latest   0b5e33bbbf39   About a minute ago   135MB
normal-flask    latest   9a499f6df793   5 minutes ago        1.01GB
```

&nbsp;

---

### 5. Docker push

1. Create new account in [Dockerhub](hub.docker.com)
    
    ```bash
    docker login
    ``` 

2. Login with your username and password.

3. Tag your image correctly to push, replace `user` with your username:

    ```bash
    docker image tag multi-flask:latest user/multi-flask-app:latest
    ```

4. Finally push it.

    ```bash
    docker push <user>/multi-flask-app
    ```







