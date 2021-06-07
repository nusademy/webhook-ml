# Nusademy Webhook ML

![](https://github.com/nusademy/Bangkit2021CapstoneProject/raw/main/logo/logo.png)

## Description
This repository contains the source code of the Machine Learning webhook application from nusademy. This application is used to provide the ML API for Dialogflow and then proceeds to the Nusademy mobile application. This application uses Python Flask and is added with Machine Learning support such as, Tensorflow, Keras, and others (for more details see the requireeement.txt file). More about Flask can be seen at the following link. <https://flask.palletsprojects.com>

## Features
- Testing API (/)
- Testing Webhook (/webhook)
- Predict MBTI (/predict)
- Personality Type Definition
- Personality Type Career Recommendations

## Notebook
We also provide the IPython Notebook file [mbti-personality-classifier.ipynb](https://github.com/nusademy/webhook-ml/raw/main/mbti-personality-classifier.ipynb) which can be run on the Jupyter Notebook application.


# Installation
The following are the installation steps both locally and in production.
## System Requireements
Based on our implementation, here are the minimum system requirements to run the Webhook ML from Nusademy
- Python3.7+
- Minimum required storage space recommended by your OS or 5 GB of free space

## Docker
The following are the steps to run this application with Docker:
1. Make sure that Docker are installed on your system.
2. Clone this repository with the following command.
```bash 
git clone https://github.com/nusademy/webhook-ml.git
```
3. Build container image with the following command.
```bash
docker build -t webhook-ml .
```
4. To run this program in your local just run following command.
```bash
docker run -p 8080:80 webhook-ml
```
5. Wait a few moments for the application to run successfully, open the address http://localhost:8080/ in the browser to access the Webhook ML API.


## Local
The following are the steps to run this application locally:
1. Make sure that Python3.7, python virtual environment and pip are installed on your system.
2. Clone this repository with the following command.
```bash 
git clone https://github.com/nusademy/webhook-ml.git
```
3. Create an isolated Python 3 environment named env with the following command.
```bash
virtualenv -p python3 env
```
4. Enter your newly created virtualenv named env with the following command.
```bash
source env/bin/activate
```
5. Use pip to install dependencies for your project from the requirements.txt file with the following command.
```bash
pip3 install -r requireements.txt
```
6. To run this program in your local just run following command.
```bash
python app.py
```
7. Wait a few moments for the application to run successfully, open the address http://localhost/ in the browser to access the Webhook ML API.



## Production 
The following are the steps for running this application in production:

1. Make sure you already have a Google Cloud Platform account.
2. Go to Console and open Google Cloud Shell.
3. Clone this repository with the following command.
```bash 
git clone https://github.com/nusademy/webhook-ml.git
```
4. Build container image with the following command.
```bash
docker build -t gcr.io/[PROJECT-ID]/webhook-ml .
```
5. Push the container image to Container Registry
```bash
docker push gcr.io/[PROJECT-ID]/webhook-ml
```
6. Deploy Webhook ML API container image to Cloud Run.
```bash
gcloud run deploy webhool-ml --image gcr.io/[PROJECT-ID]/webhook-ml --region us-central1 --platform managed --port 80
```

## CI/CD

1. Before setting up CI/CD, first connect Cloud Build with Repository. Cloud Build -> Trigger -> Connect Repository.
2. Create a Trigger for CI/CD, specify the repository (We have provided cloudbuild.yaml in the repository.):   
3. Click Save, then Run Trigger.

# END

