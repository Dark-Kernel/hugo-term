---
title: "Implementing Blue-Green Deployments in Kubernetes: Achieving Zero-Downtime Updates"
date: 2024-07-15
draft: false
author: "Sumit Patel"
tags: ["Kubernetes", "containers", "deployment", "blue-green"] 
description: "We are going to implement Blue-Green Deployments with Kubernetes for Zero-Downtime Updates"
cover: "/blue-green.png"
---



Things we are going to learn

1. Kubernetes Deployments
2. Services and Ingress
3. Database migrations // just as part of the process, not much ;) 
4. Automate with CICD
5. Monitoring and health checks

&nbsp;


Let's get started.

## Blue-Green Deployment Technique

You might or might not know that Blue-green deployment is a technique for releasing applications with zero downtime and easy rollback. Yes, that's the gist of it, at least conceptually.

This guide will walk you through implementing blue-green deployments in a Kubernetes environment. Yep, we're diving into Kubernetes.

## Implementation Steps

### 1. Prepare Kubernetes Manifests

Since it is a blue-green deployment, we will need two manifests one for the green version and one for the blue version.

Create separate deployments for blue and green versions:

{{< code language="yaml" title="blue-deployment.yml" id="1">}}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-blue
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: blue
  template:
    metadata:
      labels:
        app: myapp
        version: blue
    spec:
      containers:
      - name: myapp
        image: myapp:1.0
        ports:
        - containerPort: 8080
{{< /code >}}

green-deployment.yaml (similar, but with version: green and newer image) 

{{< code language="yaml" title="green-deployment.yml" id="2">}}
# green-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-green
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: green
  template:
    metadata:
      labels:
        app: myapp
        version: green
    spec:
      containers:
      - name: myapp
        image: myapp:1.1
        ports:
        - containerPort: 8080
{{< /code >}}


### 2. Set Up Service and Ingress

What ingress does is it maps the service to the load balancer, exposing the service externally. The load balancer then distributes traffic between the two deployments.

Create a service that can be switch between blue and green versions:

{{< code language="yaml" title="service.yaml" id="3">}}
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp
    # Note: We don't specify the version (blue/green) here.
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
{{< /code >}}

In the Ingress, we will add the service to the ingress rules.
{{< code language="yaml" title="ingress.yaml" id="4">}}
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-weight: "0"
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: myapp-service
                port: 
                  number: 80

{{< /code >}}


### 3. Implement Deployment Script

**Automation is the key**. Here's a overview of the bash script to manage the deployment:

```bash
#!/bin/bash

# Deploy new (green) version
kubectl apply -f green-deployment.yaml

# Wait for green deployment to be ready
kubectl rollout status deployment/myapp-green

# Run smoke tests on green deployment
# (implement your tests here)

# Switch the traffic to green. Here the game changes
kubectl patch service myapp-service -p '{"spec":{"selector":{"version":"green"}}}'

# Wait and monitor for any issues
sleep 60

# If everything is fine, delete the old (blue) deployment
kubectl delete -f blue-deployment.yaml

# If not, you can quickly rollback by switching the service back to blue
kubectl patch service myapp-service -p '{"spec":{"selector":{"version":"blue"}}}'
```

These are the steps we need to implement in our deployment script.

### 4. Database Migrations

Database migrations in a blue-green deployment scenario are challenging because you need to maintain compatibility between the two versions of your application (blue and green) and the database schema. What we want is to perform these migrations without downtime and ensure both versions can operate correctly during the transition.
which is damn easy :) (maybe)

You can use any of your strategies.
For database changes, you can use a migration tool that supports reversible migrations. *Run migrations before deploying the green version:

```bash
# I will be something like this:
./migrate up

# If migration fails, you can roll back
./migrate down
```
It's not only this much, but it's enough for now.

### 5. Monitoring and Health Checks

Implement readiness and liveness probes in your deployments:

```yaml
spec:
  containers:
  - name: myapp
    image: myapp:1.0
    readinessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 10
      periodSeconds: 5
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 15
      periodSeconds: 10
```

Once the application is up and running, possibly if you're lucky or an expert, you can monitor it with Prometheus and Grafana.

### 6. Automate with CI/CD Pipeline

Integrate the deployment process into your CI/CD pipeline. Personally, I use GitLab (you'd never guess). Here's an example GitLab CI configuration:
```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - docker build -t myapp:$CI_COMMIT_SHA .
    - docker push myapp:$CI_COMMIT_SHA

test:
  stage: test
  script:
    - run_unit_tests.sh
    - run_integration_tests.sh

deploy:
  stage: deploy
  script:
    - update_kubernetes_manifests.sh $CI_COMMIT_SHA
    - ./blue_green_deploy.sh
  only:
    - main
```

And if you are wondering what those scripts contain, Then check [this out](https://gist.github.com/Dark-Kernel/7a1289d56f1e1a38e9551911d5b5fa68)


## Best Practices

1. **Automate everything**: From builds to deployments to rollbacks.
2. **Implement robust monitoring**: Quickly detect any issues post-deployment.
3. **Gradual rollout**: Consider canary releases before full blue-green switch.

## Conclusion

In the conlcusion, Kubernetes's blue-green deployments aren't just a fancy color scheme—they're your ticket to stress-free updates. It provide a powerful way to achieve zero-downtime updates. By combining infrastructure management, automation, and *careful testing, we can significantly reduce some of the risks of deployment and improve availability.

&nbsp;

And, that's it.

