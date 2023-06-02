#Containerising python microservices using docker and kubernets.

Dependency:
    python3
    flask
    minikube
    kubectl
    docker
    docker-desktop
    git


Installing Python 3.X
Creating Python Virtual Environments
Installing Python VS Code Extension
Sample Flask Application
Jinja templating for Dynamic Web Pages
Using Pip to Freeze Python Dependencies
    CMD:- pip3 freeze > requirements.txt

Building the docker image using Dockerfile
    BUild CMD: docker build -t k8pythonwebapp:1.0 .
    run CMD: docker run -d -p 80:5000 --name k8pythonweb-app k8pythonwebapp:1.0
    push to dockerhub 
        CMD: docker login
        CMD: docker push rithinprabha/k8pythonwebapp:1.0


Writing Docker Compose file
    build using compose CMD: docker-compose build
    run using compose CMD: docker-compose up
    delete using compose CMD: docker-compose down

Writing Kubernetes Manifest files for the application
    CMD: minikube start
    #deploying the pods CMD: kubectl apply -f deployment.yaml 
    #deploying the service MD: kubectl apply -f service.yaml 

    #list pods and services CMD: kubectl get pods,svc 
    #lsit nodes and details CMD: kubectl get node -o wide 
    #list the services CMD: kubectl get service
    # running through tunnel .. Minikube ip plus port wont work on new versions. CMD: minikube service {{service name}} 

Creating Helm Chart
    #creating helm chart CMD: helm create k8webapp
    #modifify deployment and service od helm chart
    #create the helm template CMD: helm template k8webapp
    #for debugging CMD: helm template k8webapp --debug
    #installing helm chart CMD:  helm install  {{release name}} k8webapp/
    #get helm list CMD: helm list
    #uninstall the release CMD: helm uninstall {{release name}}