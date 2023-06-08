
By LongDV
Updated 07/06/2023
# Overview

This details of 'Building a CI/CD Pipeline' project, that are all of step to deploy a application into Azure webapp service.

The project includes a Python application that predicts housing prices in Boston provided by Udacity. The repository provides the following capabilities:

1. Deployment in Azure CloudShell: You can deploy the application in Azure CloudShell.
2. Deployment as an Azure App Service: The application can be deployed as an Azure App Service.
4. Automated code testing using GitHub Actions: Any commits made to the GitHub repository trigger automated code testing using GitHub Actions.
5. Azure DevOps pipeline: A pipeline has been set up in Azure DevOps to automatically test and deploy the updated code to the Azure App Service.

The project focuses on establishing a continuous integration and continuous deployment (CI/CD) pipeline to streamline the development and deployment process for the application.


## Project Plan
A [Trello](https://trello.com/b/JXLO9PrB/udacity) board for the project has been created to keep track deadline for all of tasks.

A [spreadsheet](https://github.com/longdvgch/Udacitycicd/blob/main/Project_Plan/project-management-template.xlsx) that includes the original and final project plan.

## Instructions


* Architectural Diagram:
![Architectural Diagram](https://github.com/longdvgch/Udacitycicd/blob/main/Screenshot/cicd_diagram.png?raw=true)

Below is the guide with step-by-step instructions on how to run a Python project:
## Deploy the app in Azure Cloud Shell

1. Setup a Azure Cloud Shell and open, clone the repository by SSH:
``` bash
git clone git@github.com:longdvgch/udacitycicd.git
```
![clone the repository](https://github.com/longdvgch/Udacitycicd/blob/main/Screenshot/git-clone-success.png?raw=true)
2. Change directory to new repository cloned:
``` bash
cd udacitycicd
```
3. Create a Python virtual environment:
``` bash
python -m venv udacitycicd
}
```
4. Activate the virtual environment to start using it. The activation steps depend on your operating system:
``` bash
source udacitycicd/bin/activate
```
5. Install all dependencies in the virtual environment and run tests:
``` bash
make all
}
```
![make all](https://github.com/longdvgch/Udacitycicd/blob/main/Screenshot/make-all-result.png?raw=true)
6. Start the application:
``` bash
python app.py
```
7. Open Cloud Shell and check that the application is working:
``` bash
./make_prediction.sh
```
![make prediction](https://github.com/longdvgch/Udacitycicd/blob/main/Screenshot/make_prediction_local.png?raw=true)
8. Create CI by GitHub Actions
- Enable Ations for repository and set up a workfilow.
![GitHub Actions](https://github.com/longdvgch/Udacitycicd/blob/main/Screenshot/git-action-build.png?raw=true)
	
	
## Deploy the app to an Azure App Service

1. Create an App Service in Azure. In this project, my App Service is called udacitycicd2023 and the resource group is called Azuredevops:
``` bash
az webapp up --name udacitycicd2023 --resource-group Azuredevops --sku B1 --logs --runtime "PYTHON:3.9"
```
2. Create Azure Pipeline for app in  Azure  Devops. The steps to set up the pipeline flolowing :
*Access to https://dev.azure.com and sign in.
*Create a new public project.
*Select Project Settings and  create a new service connection to Azure Resource Manager and a Agent Pool.
*Next, back to Azure create a VM and config Agent (VM). Then add the self-hosted agent to the agent pool.
*Final, create a new pipeline linked to GitHub repo.
Pipeline jobs list:
![pipline](https://github.com/longdvgch/Udacitycicd/blob/main/Screenshot/piplines-jobs.png?raw=true)
Pipeline job success details:
![pipline](https://github.com/longdvgch/Udacitycicd/blob/main/Screenshot/pipline-job-details.png?raw=true)
App Service deatails in Azure:
![App Service](https://github.com/longdvgch/Udacitycicd/blob/main/Screenshot/webapp.png?raw=true)

3. Check app working:
*Access to webapp's domain via the browser
![webapp page](https://github.com/longdvgch/Udacitycicd/blob/main/Screenshot/access-domain.png?raw=true)
*Run prediction against Azure Application.
``` bash
./make_predict_azure_app.sh 
```
![prediction](https://github.com/longdvgch/Udacitycicd/blob/main/Screenshot/make-predictions.png?raw=true)
*Trace streamed log files from deployed application
``` bash
az webapp log tail -g Azuredevops --name udacitycicd2023
```
![webapp log tail](https://github.com/longdvgch/Udacitycicd/blob/main/Screenshot/webapp-log-tail.png?raw=true)
*Load test using locust
![webapp log tail](https://github.com/longdvgch/Udacitycicd/blob/main/Screenshot/locust-main.png?raw=true)
![webapp log tail](https://github.com/longdvgch/Udacitycicd/blob/main/Screenshot/locust-statistics.png?raw=true)


## Enhancements

Currently, the GitHub repository consists of a single branch. However, it is advisable to adopt a branching strategy that incorporates multiple branches.
This approach enables thorough testing and deployment of code changes in a staging environment. 
Once the changes have been validated in the staging environment, they can be merged into the production branch and subsequently deployed into the production environment.

## Demo 
Domain: http://udacitycicd2023.azurewebsites.net/

You can watch a short demo of project on Youtube in [here](https://www.youtube.com/watch?v=8mKU1_wK9RI)


