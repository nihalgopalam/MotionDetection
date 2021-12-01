# MotionDetection

This is a webapp that is currently only supported locally. Built using flask, bootstrap, sqlite3, openCV, pandas, and python3

### To Run:

1. Create and activate a virtual enviroment in the same MotionDetection directory where you have the code downloaded
2. Install/verify the following tools: 
    - [Python3](https://www.python.org/downloads/)
    - [Pandas](https://stackoverflow.com/questions/42907331/how-to-install-pandas-from-pip-on-windows-cmd)
    - [openCV](https://pypi.python.org/pypi/opencv-python)
    - [sqlite3](https://www.sqlite.org/download.html)
    - [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)
3. Start the flask server on local host with:

    Bash:
    ```
    $ export FLASK_APP=app
    $ flask run
    ```

    CMD:
    ```
    $ export FLASK_APP=app
    $ flask run
    ```

    Powershell:
    ```
    > $env:FLASK_APP = "app"
    > flask run
    ```

>Server defaults to running on port 5000

# TODO:
1. html to jquery to python
2. python and database access and checking/adding accounts
3. fix detection python program
4. add a welcome page with download of detection.py
5. send paths of the imgs to db and store imgs locally
6. display the img and time of movement on recordings page