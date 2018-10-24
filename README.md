## InfluxDB with Grafana on Google Kubernetes Engine by [![N|Solid](https://think-big.solutions/img/logo.png)](https://think-big.solutions)
In this tutorial we explain how to get real time analytics of energy produced and consumed from two solar stations simulators using influxDB together with grafana hosted on the kubernetes engine of google

## Prerequisites
- Google Cloud Project linked to a billing account
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
- Run the following commands
```bash
git clone "https://github.com/ThinkBigEg/influxDB-grafana-gke"
cd influxDB-grafana-gke/configs/
```
### 4. Running the kubernetes config files
- Now we want to open the pods and services of influxDB and grafana
- Run the following commands
```bash
kubectl create -f pv-claim.yaml
kubectl create -f influxdb.yaml
kubectl create -f grafana.yaml
kubectl create -f influxdb-internal-service.yaml
kubectl create -f influxdb-external-service.yaml
kubectl create -f grafana-service.yaml
```
- Open Workloads in the side menu to check that the status of grafana and influxDB in OK
- Open Storage in the side menu to check that the phase of the persistent volume claim is Bound
- Open Services in the side menu refresh until all the services are OK

### 5. Create a database in influxDB
- SSH with influxDB container
```bash
# Get the name of the influxdb container
kubectl get pods
```
```bash
# Replace <NAME OF THE CONTAINER>
kubectl exec -it <NAME OF THE CONTAINER> influx
```
- Create solar_db database
```bash
create database solar_db
```
- Exit the container 
```bash
exit
```
### 6. Running the two sensor simulators
- Clone the repository on your local machine
```bash
git clone "https://github.com/ThinkBigEg/influxDB-grafana-gke"
cd python
```
- From the cloud shell run :
```bash
kubectl get services influxdb-external-service
```
- Copy the External ip and modify the two python files in repository on you local machine by **replacing <EXTERNAL IP>** by the External ip that you copied
  ```python
  INFLUXDB_HOST = '<EXTERNAL IP>'
  ```
- Executing the two python files open two terminals in python folder
  - In the 1st terminal run
  
  ```bash
  python producer_sensor.py
  ```
  - In the 2nd terminal run
  
  ```bash
  python consumer_sensor.py
  ```
Now the sensors are sending data to influxDB in the solar_db database
## NOTE: 
At this point you can modify the python code the get the data from **Real Sensors** and send it to influxDB instead of generating random values

### 7. Adding a dashboard on Grafana for real-time analytics
- In Kubernetes Engine side menu click on Services
- Click on the url in grafana-external-service row under the endpoint column
  - Username: admin
  - Password: admin
- Click Add Datasource
  - Enter the url http://<CLUSTER IP>:8086
    - To get cluster ip
      - From the cloud shell run :
  
    ```bash
    kubectl get services influxdb-external-service
    ```
  - Enter a name
  - Enter Database : solar_db
 - Click save and test
 - then click back
 - On the side menu Click Dashboards --> Manage
 - Click on import
 - Now on the repository on your local machine go to the dashboard folder and copy the content of the json file
 - Paste it on Or paste json field
 - Click load
 - Select solar and then click import 
## Congrats You should be finished

