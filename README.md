# CoviDesk
A Web Application where people can help hospitals and government, by giving information about available beds. And many more features !

## Installation
1. Clone the repository on your system.
```
git clone https://github.com/abhishak3/CoviDesk
```

**Now, navigate into the downloaded repository and follow these steps.**

2. Setting up **Python Virtual Environment**
- Download `virtualenv` python package
  ```
  pip install virtualenv
  ```
- Creating **Virtual Environment**
  #### For Windows
  ```
  python -m venv venv
  ```
  #### For Linux or MacOs
  ```
  python3 -m venv venv
  ```  

3. Setting up Environment Variables
  #### For Windows
  ```
  set FLASK_APP=run.py
  set FLASK_ENV=development
  set FLASK_CONFIG=development
  set SECRET_KEY=yoursecretkey
  ```
  #### For Linux or MacOs
  ```
  export FLASK_APP=run.py
  export FLASK_ENV=development
  export FLASK_CONFIG=development
  export SECRET_KEY=yoursecretkey
  ```

4. Running the Application
  ```
  flask run
  ```
