# KAMI Airline App Backend Running Process

This KAMI Backend project is developed using Django which is Python Framework.

## Environment Setup

### 1. Install Python: 
Ensure that you have Python installed on your machine. You can download the latest version from the official [Python website](https://python.org/). Before setting up your virtual environment and Django, you need to ensure that you have Python installed and it should be a version above 3. You can run "py --version" in cmd.
### 2. Open the project directory in cmd: 
Open the File Explorer and navigate to the required directory. Then Click on the address bar and type "cmd", then hit Enter. (Don't open Powershell.)
### 3. Open the project directory in the command line and start airline_app server: 
Then follow these steps below.
- Run "py -m venv env" in cmd to create a new Virtual Environment. You can see the env folder created in the project directory.
- Then run ".\env\Scripts\activate" n cmd to activate the virtual environment. If you can see "(env)" at the first part of the command line, It explains that virtual environment activated.
- Then run "pip install django" and "pip install djangorestframework".
- Then, run "python manage.py migrate" to install database.
- Finally, run "python manage.py runserver" and the django server will run in localhost:8000.