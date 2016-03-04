# Abelson Mechanical

## Setup

To provision your environment, execute the following commands from the project
root:

```
$ npm install
$ pip install -r requirements.txt
```

You'll need to add a view environment variables for Flask. Add the following lines to your .bash_profile:

```
export ABELSON_SETTINGS=/path/to/config.py
export ABELSON_DB=/path/to/abelson.sqlite
```
