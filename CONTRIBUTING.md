# "ambient-app--react" Contributing Guide

### Welcome

This project is a part of [Web Development learning class](https://hattifnatt4r.github.io/sd). It is designed to help learn ReactJS, Python APIs, Database basics and more.

See our Discord server for details (https://discord.gg/wAMEqRMbdm), or meet us in person at the Cambridge Public Library.

**Due to limited resources, contributions are currently open to class members only.**
Please contact organizers through Discord or email if you're an experienced developer and willing to help with feedback or the projects setup.

See [README.md](https://github.com/cambridge-devclass/ambient-app--react/blob/main/README.md) for the details about the app.

# Contribution workflow

### Environment setup

WIP: Front-end only setup

#### WIP: First-time back-end setup. Only do this once!

**Important** Please use Python 3.13 for working on this project. Having a standard version ensures we all have a reproducible environment that behaves the same.

We use a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/) with [`venv`](https://docs.python.org/3/library/venv.html). It isolates our project's dependencies from the globally installed Python and system packages. The links above go into much more detail about virtual environments and how they work.

Set up the `venv` folder

```bash
cd server
python -m venv venv
```

You **activate** the virtual environment by running one of the `activate` scripts in `venv/bin`. Doing so changes your local shell/CMD window so that calling `python` or `pip` will refer to the local files in `venv/bin`. Running `pip install some-package` will install the package locally in our `venv` directory instead of modifying our system.

To activate your environment run one of the following

**Windows with CMD**
```cmd
cd server
venv\Scripts\activate.bat
```
**Windows with PowerShell**
```powershell
cd server
venv\Scripts\Activate.ps1
```
**Mac/Linux**
```bash
cd server
source venv/bin/activate
# Or activate.fish or activate.csh depending on shell
```

Install the project's dependencies which are stored in `requirements.txt`

```bash
pip install -r requirements.txt
```

Now you've got a virtual environment with necessary Python packages installed locally!

##### SQLite setup (temporary)
The application can be run using SQLite for the database. This makes the setup process a little easier, because SQLite is built-in to Python.
 
To create a local SQLite database file, run the `_sqilite-setup.py` script in the server directory: 

```bash
cd server
python _sqlite-setup.py
```

This should create a "local.db" file in the server directory, which the server will use as long as it retrieves `DB_URL` from `config/sqlite.py`. 

A GUI database client is generally useful for backend development, it makes it easy to look up or change records/schema for debugging or prototyping.
HeidiSQL is pretty good but there are many alternatives. Here are some that support SQLite: \
https://heidisql.com \
https://dbeaver.io \
https://sqlitebrowser.org

#### WIP: Backend setup for every session

In every working session make sure you

1. Activate the virtual environment as shown above
2. From the `server` folder, launch the Flask dev server

    ```bash
    flask --app api run --debug

    * Serving Flask app 'api'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    ```
3. Navigate to the URL shown for basic info and a link to an interactive API doc+test page

The basic definition for the Flask app is in [`server/api/__init__.py`](server/api/__init__.py). Routes are in [`server/api/routes.py`](server/api/routes.py)

#### VSCode setup for backend

##### Install Python extension

Ensure you have the [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) `ms-python.python` installed. You'll get a popup for a few other recommended extensions.

##### Activate your virtual environment in VS Code

VSCode often detects that you have a `venv` and activates that when opening a Python file. In the VSCode footer on the right you'll see something like `3.13.13 (venv)`.

If that fails

1. Open the command pallette with `Cmd+Shift+P`
2. Search for `Python: Select Interpreter`
3. Choose `Enter interpreter path->Find...`
4. Select `server/venv/bin/python`

Now all of the Python intellisense and tooling in VSCode should work!

##### Debugging the Python API

The debug configuration for the Flask app is defined in [.vscode/launch.json](.vscode/launch.json). You can debug the Flask app in VS Code by opening the debug panel, choosing `Flask Api Server` in the dropdown, and clicking the green run button. `F5` will also start the debugger. You can then set breakpoints and step through the server code.

### Commit messages

WIP: Provide instructions on how to format commit messages.

* Include Issue ID in commit message (if this issue is listed in github repo). Example:<br>
`[10] Add icons, starter set `

### Pull requests

WIP: Example pull request.

### Deployment

WIP: Explain deployment process.

### Issue management

WIP: Provide instructions on how to create, tag, and assign issues.
