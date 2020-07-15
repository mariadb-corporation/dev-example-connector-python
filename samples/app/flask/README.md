# MariaDB Connector/Python Samples

## Configuring and running the Python/Flask API 

### 1. Create the schema <a name="schema"></a>

[Connect to the database](https://mariadb.com/kb/en/connecting-to-mariadb/) and execute the following SQL scripts:

```sql
CREATE DATABASE todo;

CREATE TABLE todo.tasks (
  id INT(11) unsigned NOT NULL AUTO_INCREMENT,
  description VARCHAR(500) NOT NULL,
  completed BOOLEAN NOT NULL DEFAULT 0,
  PRIMARY KEY (id)
);
```

### 2. Configure the database connection

Update the configuration for your target database instance.

```python
config = {
    'host': 'host_address',
    'user': 'your_user',
    'password': 'your_pass',
    'database': 'todo'
}
```

Then save api.py.

### 3. Set up and activate a virtual environment <a name="activate"></a>

A virtual environment is a directory tree which contains Python executable files and other files which indicate that it is a virtual environment. Basically, it's the backbone for running your Python Flask app.

Creation of [virtual environments](https://docs.python.org/3/library/venv.html?ref=hackernoon.com#venv-def) is done by executing the following command:

```
$ python3 -m venv venv
```

**Tip**: Tip: pyvenv is only available in Python 3.4 or later. For older versions please use the [virtualenv](https://virtualenv.pypa.io/en/latest/) tool. 

Before you can start installing or using packages in your virtual environment, you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH.

Activate the virtual environment using the following command:

```bash
$ . venv/bin/activate activate
```

### 4. Install Python modules

Open a terminal window and install the MariaDB and Flask modules.

```bash
$ pip install mariadb flask
```

### 5. Start the API project

```bash
$ python api.py
```

That's it! You should now having a running Python/Flask API project. You can test HTTP requests targeting http://localhost:8080/api/tasks.

## More Resources

* [Getting Started with MariaDB using Docker, Python and MariaDB](https://dev.to/probablyrealrob/getting-started-with-mariadb-using-docker-python-and-flask-38a7) (blog)
