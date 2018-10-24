## InfluxDB with Grafana on Google Kubernetes Engine by [![N|Solid](https://think-big.solutions/img/logo.png)](https://think-big.solutions)
In this tutorial we explain how to get real time analytics of energy produced and consumed from two solar stations simulators using influxDB together with grafana hosted on the kubernetes engine of google

## Prerequisites
- Google Cloud Project linked with billing account
- Python

### 1. Create a kubernetes cluster on GCP
- From the side menu choose Kubernetes Engine --> clusters
- Click on Create Cluster button
- Choose your first cluster option
- Modify the number of nodes to 2 and the machine type to 1 vCPU
- Click create
- Wait few minutes until your cluster is up and running 

### 2. Connect to the cluster using Cloud Shell
- Click on the connect button
- Choose Run in Cloud shell
- Wait until the cloud shell is connected and execute the already written command

### 3. Cloning the repository on the cloud shell
