# CoviDesk
A Web Application made using [Flask](https://flask.palletsprojects.com) where different NGO's can collaborate and provide some useful information about availability of oxygen or empty beds at different hospitals.
All the useful information can be found at a place.

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

    - **For Windows**
      ```
      python -m venv venv
      ```

    - **For Linux or MacOs**
      ```
      python3 -m venv venv
      ```  
3. Installing Dependencies
    ```
    pip install -r requirements.txt
    ```
    
4. Setting up Environment Variables  

  - **For Windows**
    ```
    set FLASK_APP=run.py
    set FLASK_ENV=development
    set FLASK_CONFIG=development
    set SECRET_KEY=yoursecretkey
    ```
  
  - **For Linux or MacOs**
    ```
    export FLASK_APP=run.py
    export FLASK_ENV=development
    export FLASK_CONFIG=development
    export SECRET_KEY=yoursecretkey
    ```

5. Running the Application
  ```
  flask run
  ```
