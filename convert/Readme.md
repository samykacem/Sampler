# Convert png to gif

## Convert PNG folder in Gif folder
```python convert.py```

## Virtual env
### Install
If virtual env is not installed on your machine: 
* Mac `python3 -m pip install --user virtualenv`
* Win `python -m pip install --user virtualenv`

### Setup for the project
Be sure to be in CAPT folder and then type : 
* Mac `python3 -m venv env`
* Win `python -m venv env`

### Activate env
Be sure to be in CAPT folder and then type : 
* Mac `source env/bin/activate`
* Win `env\Scripts\activate` (may have an issue to run script so type : `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`)

### Add dependencies
How to install dependencies
```
pip install -r requirements.txt
```

### Record dependencies
How to get the dependencies in venv and register them in requirements.txt 
```
pip freeze > requirements.txt
```