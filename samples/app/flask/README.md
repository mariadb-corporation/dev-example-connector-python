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

### 3. Install Python modules

Open a terminal window and install the MariaDB and Flask modules.

```bash
$ pip install mariadb flask
```

### 4. Start the API project

```bash
$ python api.py
```

That's it! You should now having a running Python/Flask API project. You can test HTTP requests targeting http://localhost:8080/api/tasks.

## More Resources

* [Getting Started with MariaDB using Docker, Python and MariaDB](https://dev.to/probablyrealrob/getting-started-with-mariadb-using-docker-python-and-flask-38a7) (blog)