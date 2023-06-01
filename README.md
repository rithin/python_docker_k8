microservices-in-python

Installing Python 3.X
Creating Python Virtual Environments
Installing Python VS Code Extension
Sample Flask Application
Jinja templating for Dynamic Web Pages
Using Pip to Freeze Python Dependencies
    CMD:- pip3 freeze > requirements.txt

Building the docker image using Dockerfile
    BUild cmd: docker build -t k8pythonwebapp:1.0 .
    run cmd: docker run -d -p 80:5000 --name k8pythonweb-app k8pythonwebapp:1.0

Writing Docker Compose file
    build using compose cmd: docker-compose build
    run using compose cmd: docker-compose up
    delete using compose cmd: docker-compose down

Writing Kubernetes Manifest files for the application
    CMD: minikube start
    CMD: kubectl apply -f deployment.yaml ## deploying the pods
    CMD: kubectl apply -f service.yaml ## deploying the service

    CMD: kubectl get pods,svc # list pods and services
    CMD: kubectl get node -o wide #lsit nodes and details
    CMD: kubectl get service #list the services
    CMD: minikube service {{service name}} # running through tunnel .. Minikube ip plus port wont work on new versions.

Creating Helm Chart