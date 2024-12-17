# Product Deployment Pipeline with Logging
- This project is designed to simulate a product deployment pipeline, where the deployment process is logged at every step. The pipeline includes   actions such as build, deploy, and notify. Each action is logged using a decorator, and the logs are saved in a separate file.


# Overview
- This program simulates a product deployment pipeline with three primary actions:

- Build: Compiles and prepares the product for deployment.
- Deploy: Deploys the product to specified repositories.
- Notify: Sends notifications about the deployment process to specified channels (e.g., Mail, Slack).
- The program uses an Object-Oriented Design with Python's dataclass to model the Product class, which has attributes such as:

Product name
Scheduled deployment time
Target repositories (Artifactory, Nexus, S3)
Notification channels (Mail, Slack)
The program also uses a decorator to log method calls for actions like building, deploying, and notifying.

* I've also added a logging decorator for better debugging and reusabilty process.
* The product class compose the Notification and Deployment abstract classes for better code decoupling and usage of deployment to various repos more easily.


**********************************
Thank you for this oppotunity ! **
**********************************