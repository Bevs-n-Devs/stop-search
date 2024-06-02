# Stop Search 
The **Stop Search UK** is an concept created by my neice Daniella Rose who wanted an app to report police misconduct within Black & Asian communities.
The concept of the app is to allow the public to report instances of police misconduct when the police are interacting with the public.
Users are able to select if they are witness or a victim, and the contents of the report are uploaded to a map for all to see.

**Stop Search UK** is a concept made in an attempt to bridge the gap between all communities and the UK police; *while the **Stop Search** app is developed for the UK, it also has the ability for develeopers to easily make changes to set the map, by setting it to their own country.*

## Installation and Setup
### Virtual Environemnt
After cloning the repo you will need to create your virtual environment **inside the newly cloned directory.**
```
python -m venv venv
```

To activate the virtual environment:
```
# Windows
.\venv\Scripts\activate

# MacOS / Linux
source venv/bin/activate
```

To turn off your virtual environment simply enter the following:
```
deactivate
```

### Install Libraries and Packages
The easiest weay to correctly install the packages & libraries that you need, you can use the `requirements.txt` file to install everything you need:
```
pip install -r requirements.txt
```

Because this is intended to be a community/open source project, **if you install new packages you will need to update the `requirements.txt` file.**
```
pip freeze > requirements.txt
```

### Setup `.env` File
You will need to setup the app's host and port for development and in test.
```
API_PORT=8000
API_HOST="127.0.0.1"
Test_API_BASE="http://127.0.0.1:8000"
STOPSEARCH_DB="mysql://<username>:<password>@127.0.0.1:3306/stop_search_dev_db"
```
To get the `username` and `password` email me at [yawakoto.python\@gmail.com](mailto:yawakoto.python@gmail.com).

### Create Application As Module
You will also need to create the application as a Python module by doing the following in the terminal:
```
pip install -e .
```

### Running Application
To get the application running you can enter the following in the terminal:
```
flask --app stopSearch run --port 8000 
```

To run the application via the **VScode Debugger** you will need to create a `.vcode` file with the following configurations:
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Flask",
            "type": "debugpy",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "stopSearch",
                "FLASK_DEBUG": "1",
            },
            "args": [
                "run",
                "--port",
                "8000"
            ],
            "jinja": true,
            "autoStartBrowser": true
        }
    ]
}
```


## Testing: Behaviour Driven Development
Behavior Driven Development (BDD) is a development approach where developers collaborate with stakeholders to define the desired behavior of an application using plain language descriptions. In Behave, this is done through .feature files, which contain scenarios written in Gherkin syntax detailing how a particular part of the app should work, such as how a page displays data and the contents of that data.

Developers use these .feature files to guide the implementation of the new feature, ensuring that the development aligns with the specified behavior. Once the feature is developed, it is tested to verify that it meets the expected requirements.

These tests are defined in .steps files, where each step corresponds to a part of the scenario described in the .feature file. The steps are implemented in Python code, and they validate that the application behaves as expected according to the requirements set out in the feature file. The steps must accurately match the steps in the feature file for the tests to be effective and to ensure the behavior is correctly validated.

For this Flask application we will use the [Behave](https://behave.readthedocs.io/en/latest/) framework

This should already bve installed in the `requirements.txt` file but if you find you need to install it eneter the following:
```
pip install behave
```

To run your test you can enter any of the following:
```
# all tests
behave

# run test via @tag
behave -t @tag_name

# run test with all @tags
behave -t @tag_name1 and @tag_name2

# run @tag1 or @tag2 (both if true)
behave -t @tag_name1 -t @tag_name2
```