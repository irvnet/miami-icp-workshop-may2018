
## Getting familiar with Kubernetes

In this section get a little familiar with Kubernetes by looking around the environment.

We'll use [IBM Cloud Private](https://www.ibm.com/cloud/learn/what-is-private-cloud) (ICP) as our Kubernetes cluster for this session. ICP is a commercial implementation of a Kubernetes cluster and has a wide variety of extra functionality built on top of Kubernetes. In this session though, we'll focus on the kubernetes fundamentals using ICP. 

![](../images/cluster-diagram.jpg)



We can connect to our cluster with the browser and with the "kubectl" command line client. We'll spend most of our time with the command line client learning our kubernetes basics, but we'll use browser interface as well.

First make sure you've checked in with a proctor and have a username and password to log into the cluster.  We'll log into the system via our browser and get our kubectl command line client configured.  

Start by going to the login page, and entering your username and password.

![](../images/login.jpg)

In the upper right corner click on the icon of a user and select configure client.

![](../images/config.jpg)


Click the copy button to capture details for configuring the kubectl client and paste the results at the command line.

![](../images/config-box.jpg)


The kubectl command line client should be configured.. just to check type

```

$ kubectl get deploy --namespace=default

```

Now you're connected to the cluster!


---
