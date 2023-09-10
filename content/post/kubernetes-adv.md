---
title: "Kubernetes Voyage: Advanced Ship Steering"
date: 2023-09-10
draft: false
author: "Sumit Patel"
tags: ["Kubernetes", "containers", "persistentVolumes"] 
description: "Let's get hands on with advanced topics."
---
<!-- cover: "/kubernetes_logo.svg" -->


We will learn

- pods vs container
- Deployments
- Services
- Auto-healing concept
- config maps & secrets 
- persistent volume 

&nbsp;

Let's get started.


### Pods vs Containers

| Pods  | Container |
| ----------- | ----------- | 
| Unit of conainers | Single container by containerization tool.
| Contains one or more Conainers | Only single container
|Crashed free    | Can be crashed if some error occurs
|Can be Scheduled       | Can't be scheduled |


&nbsp;

---


### Configuration file

To create pods we have to use a configuration file in `YAML`, which is also called `manifest` in k8s 

We need manifest file for almost everything in kubernetes. 


- Kind:

    To create maifest file for a paritcular service we have to define a `kind` keyword. `kind` defines what type of manifest file is, like for Pods, Service or Deployment, etc.

    Example:
    
    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:   # Extra data. # object
      name: nginx  # Any name can be used.
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
    ```


- Namespace: 

    logical entity allow you to isolate your resources, like pods, volumne, deploymnets, etc.
You can create multiple namaspcae for different resources, it is a type of group.

    > Default name space is already present, and everything is created under it until you specify any other namespace in manifest.

    ```bash
    kubectl create namespace nginx
    ```
    
    ```bash
    kubectl get namespace
    ````
    Example:
     
    {{< code language="yaml" title="Pod.yml" id="1">}}
apiVersion: v1
kind: Pod
metadata:   # Extra data. # object
  name: nginx  # Any name can be used.
  namespace: nginx
spec:
  containers:
  - name: nginx
    image: nginx:latest
    ports: # If you don't  specify then also it will assume.
    - containerPort: 80
    {{< /code >}}


- To apply the manifest file to your cluster command: 

    ```bash
    kubectl apply -f pod.yml
    ```

    This will send request to api server, then it will to scheduler (resposnisble fo managing pods) and then it send back to api server and then configuration will be stored.

- To fetch the pods information from master we can use the below command:
    ```bash
    kubectl get pods -n nginx
    ```
    
    `-n`: namespace, by default it only looks for resources in to default namespace.


&nbsp;

---

### Deployment

 Deployment is a desired state.
It is also written in manifest file and `kind` will be set to `Deployment`. It is used to create replicaset of templates, 
It is a configuration of pods. It is a desired(required) state of your pods. You can also provide some data in pods while deployment using this manifest.

Example:

 {{< code language="yaml" title="deployment.yml" >}}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:  # select all nginx labels
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
 {{< /code >}}

- `replicas`: Number of pods clone / replications
- `labels`: Configuration is for, name of the replica.


Actions: 

1. Apply the deployment:

    ```bash
    kubectl apply -f deployment.yml 
    ```

2. Get the nodes with more wider output.

    ```bash
    kubectl get nodes -n nginx -o wide
    ```

    ```output
    NAME               STATUS   ROLES                  AGE     VERSION   INTERNAL-IP     EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION   CONTAINER-RUNTIME      
    ip-172-31-55-54    Ready    <none>                 4d23h   v1.20.0   172.31.55.54    <none>        Ubuntu 22.04.3 LTS   6.2.0-1011-aws   docker://24.0.5        
    ip-172-31-57-166   Ready    control-plane,master   5d      v1.20.0   172.31.57.166   <none>        Ubuntu 22.04.3 LTS   6.2.0-1011-aws   docker://24.0.5
    
    ```

3. Get your deployment status.

    ```bash
    kubectl get deployment -n nginx
    ```

    ```output
    NAME               READY   UP-TO-DATE   AVAILABLE   AGE                                        │
    nginx-deployment   3/3     3            3           23m
    ```

4. Get detail information about your deployment.

    ```bash
    kubectl describe deployment 
    ```

5. Apply Rolling update to deployment like scaling:  # No need to edit the file. 
    
    ```bash
    kubectl scale deployment nginx-deployment --replicas=2 -n nginx
    ```

    ```output
    deployment.apps/nginx-deployment scaled
    ```

6. You can even Rollback if you made any mistake.

    ```bash
    kubectl rollout undo deployment/nginx-deployment
    ```


&nbsp;

---

### Services 

It is method used to allow outside world to access application instance running in pods deployment, some sort of proxy.

In our example, nginx is running but not accessible because we haven't applied any service yet.

Example:

{{<code language="yaml" title="service.yml" >}}
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - protocol: TCP
      port: 80 # containers port
      targetPort: 9376  # service's port to map with.
{{</code>}}


##### Services are of 3 types: 

1. **NodePort**:

    It act as a node machine, this maps the deployment's port to serivce's port. 

    We have to provide 3 ports:
       
     * `port`: Port of application running in pods, (80 incase of nginx).
     * `targetPort`: Service port, to map pods port with Service port. (incoming)
     * `nodePort`: Outgoing port, which is actual accessible port. ( ranges [30000 - 32627])

  
     Example: 

     This service file will provide the access to users for our application which is nginx in this case.


    {{<code language="yaml" title="service.yml" >}}
apiVersion: v1                                                                                 
kind: Service                                                                                  
metadata:                                                                                      
  name: my-service                                                                             
  namespace: webserverss                                                                       
spec:                                                                                          
  selector:                                                                                    
    app: nginx                                                                                 
  type: NodePort                                                                               
  ports:                                                                                       
    - protocol: TCP                                                                            
      port: 80                                                                                 
      targetPort: 80                                                                           
      nodePort: 30004
    {{</code>}}

2. Cluster IP: 
    
    It Exposes the Service on a cluster-internal IP, Making the Service only reachable from within the cluster not outside, And this is used by default.

3. Load balancer:

    It Exposes the Service externally using an external load balancer. Kubernetes does not offer a load balancing component; you have provide one, or you can integrate your cluster with a cloud provider like AWS.


We, will use NodePort which will allow us to access out nginx outside the cluster.


- Apply the service
    ```bash
    kubectl apply -f serivce.yml
    ```

- List your Services.
    ```bash
    kubectl get services -n webserverss
    ```
    
    ```output
    NAME         TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE                       │
    my-service   NodePort   10.104.86.172   <none>        80:30004/TCP   15s
    ```


&nbsp;

--- 


### Auto healing.


 Now, our pods are running and our application is also accessible by the user. But, what if we delete one of the pod or container?


Well, let's do it.

1. First get list of your pods.

    ```bash
    kubectl get pods -n webserverss # replace with your namespace
    ```
    
    ```output
    NAME                                READY   STATUS    RESTARTS   AGE                           
    nginx                               1/1     Running   1          17m                         
    nginx-deployment-66b6c48dd5-2299p   1/1     Running   1          16m                         
    nginx-deployment-66b6c48dd5-vtqq8   1/1     Running   1          16m
    ```

2. And now delete one pod.    
    ```bash
    kubectl delete pod nginx-deployment-66b6c48dd5-2299p -n webserverss
    ```
    
    Now, we have deleted one pod, let's check the status of pods.
    
    ```output
    NAME                                READY   STATUS    RESTARTS   AGE                         
    nginx                               1/1     Running   1          17m                         
    nginx-deployment-66b6c48dd5-tlq9v   1/1     Running   0          8s                            
    nginx-deployment-66b6c48dd5-vtqq8   1/1     Running   1          16m
    ```

    You saw that right? The `Age` of second pod is `8s`. 

    Yes, that 2nd pod got created after we deleted one, And this is what we call **Auto Healing**.


3. Anyway, If you want to delete you particular depolyment or manfiest configuration use this syntax:

    ```bash
    kubectl delete -f pod.yml # your manifest.yml file
    ````

&nbsp;

---


<!-- ### Micro services -->

<!-- Small services, Every service is treated as new application. --> 



### Secrets & config map

 In k8s, we can't pass environment variables through kubectl at runtime. Therefore we use secret & config map file.

- **Config map**:

    It is a Special kind of manifest file, if you deployment needs particular variable then you can declare that in this manifest file. All variables are passed to all pods. In manifest set kind to `kind: ConfigMap` to create a config map. It pass data as plain texts.

- **Secrets**:

    It is a type of config which contains credentials (passwords), advantage is you can pass encoded password and it will be decrypted in pods. In manifest set kind to `kind: secrets` to create secrets. 


Example: 

1. Setup servers

2. Create deployment manifest.

    {{<code language="yaml" title="deployment.yml" >}}
apiVersion: apps/v1                                                                               
kind: Deployment                                                                                  
metadata:                                                                                         
  name: mysql-deplyment                                                                           
  namespace: mysql                                                                                
  labels:                                                                                         
    app: mysql                                                                                    
spec:                                                                                             
  replicas: 1                                                                                     
  selector:                                                                                       
    matchLabels:                                                                                  
      app: mysql                                                                                  
  selector:                                                                                       
    matchLabels:                                                                                  
      app: nginx-2                                                                                
  template:                                                                                       
    metadata:                                                                                     
      labels:                                                                                     
        app: nginx-2                                                                              
    spec:                                                                                         
      containers:                                                                                 
        - name: mysql                                                                             
          image: mysql                                                                          
          ports:                                                                                  
            - containerPort: 3306                                                                 
          env:                                                                                    
            - name: MYSQL_DATABASE                                                                
              valueFrom:                                                                          
                configMapKeyRef:                                                                  
                  name: mysql-config                                                              
                  key: MYSQL_DATABASE                                                             
              name: MYSQL_ROOT_PASSWORD                                                           
              valueFrom:                                                                          
                secretKeyRef:                                                                     
                  name: mysql-secret                                                              
                  key: MYSQL_PASSWORD 

    {{</code>}}

3. You can rectify errors using dry run, it doesn't apply the changes only show what will be happen if applied: 

    ```bash
    kubectl apply -f deployment.yml --dry-run
    ```

4. Create defined namespace:

    ```bash
    kuebctl create namespace mysql
    ```

<!-- 5. Apply the changes -->

<!--     ```bash -->
<!--     kubectl apply -f depolyment.yml -->
<!--     ``` -->

5. Create configMaps manifest file

    {{< code language="yaml" title="configMaps.yml" >}}
apiVersion: v1
kind: ConfigMap
metadata: 
    name: mysql-config
    namespace: mysql
    labels:
        app: mysql
data: 
    MYSQL_DATABASE: "cooldb"
    {{</code>}}

6. Apply config map.

    ```bash
    kubectl apply -f configMap.yml
    ```
    
7. Check your config map.

    ```bash
    kubectl get configmap -n mysql
    ```


8. Now create secrests manifest.

    But, before that encrypt your pass using below command.

    ```bash
    echo -n 'secret' | base64  # you can pass -d to decrypt
    ```
    
    copy output and pass in data field in secrets.yml

    {{<code language="yaml" title="secrets.yml" >}}
apiVersion: v1
kind: Secret
metadata:
    name: mysql-secret
    namespace: mysql
    labels:
        app: mysql
type: Opaque
data: 
    MYSQL_PASSWORD: dkoafusfmsdjk # base64 password.
    {{</code>}}


9. Apply secrets manifest to deployment.

    ```bash
    kubectl apply -f secret.yml
    ```

10. Now, check if secret is added successfully.

    ```bash
    kubectl get secret -n mysql
    ```

11. After that, finally apply your deployment.

    ```bash
    kubectl apply -f deployment.yml 
    ```

    ```output
    NAME              READY   UP-TO-DATE   AVAILABLE   AGE                                            │
    mysql-deplyment   1/1     1            1           40m
    ```

    After your deployment, you can cross verify by logging in mysql. Run commands in worker node.
    Make sure you are putting correct container id.
    
    ```bash
    docker ps | grep mysql 
    docker exec -it ef175a2293f2 /bin/mysql -u root -p    
    ```

12. You can delete your deployment if you want.
    
    ```bash
    kubectl delete -f deployment.yml
    ```

&nbsp;

---



### PVC & PV, Storage classes 

- **PV (Persistent Volume)**

    It creates application's stateful location is in your disk where data is stored as snapshot.


    {{<code language="yaml" title="persistenVolume.yml" >}}
apiVersion: v1
kind: PersistentVolume
metadata: 
    name: mysql-pv-volume
    namespace: mysql
    labels:
        app: mysql
spec: 
    storageClassName: manual
    capacity: 
        storage: 2Gi
    accessModes: 
        - ReadWriteOnce
    hostPath: 
        path: "/mnt/data"
    {{< /code >}}

    **Make sure hostPath.path directory exists in worker node.**


    Now apply your peristentVolume manifest
    
    ```bash
    kubectl apply -f persistenVolume.yml
    ```

    Check if persistentVolume is created.
    ```bash
    kubectl get pv -n mysql
    ```
    
    ```output
    NAME              CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM   STORAGECLASS   REASON   AGE                                                                                        
    mysql-pv-volume   2Gi        RWO            Retain           Available           manual                  16s
    ```


- **PVC (Persistent Volume Claim):** 

    After creating the volume you have to claim it to use, until now we have just created not used. You can claim how much you want from volume for your deployment.

    {{<code language="yaml" title="persistentVolumeClaim.yml" >}}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pv-claim
  namespace: mysql
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 2Gi
    {{</code>}}

    Then, apply it

    ```bash
    kubectl apply -f persistentVolumeClaim.yml
    ```

    After that check if was successfull.

    ```bash
    kubectl get pvc -n mysql
    ```


    Now, to use volumes add these into containers object in deployment.yml. 
    
    ```yaml
            volumeMounts:
            - name: mysql-persistent-storage
              mountPath: /var/lib/mysql
          volumes:
          - name: mysql-persistent-storage
            persistentVolumeClaim:
              claimName: mysql-pv-claim
    
    
    ```


&nbsp;




So, that's it.

