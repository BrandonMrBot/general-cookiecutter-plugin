{{ cookiecutter.plugin_description }}
==============

Getting Started
---------------

- Activate the {{ cookiecutter.plugin_for }} environment.
```
$ . ./path/to/{{ cookiecutter.plugin_for }}/bin/activate
```

- Change directory into your newly created plugin.
```
$ cd {{ cookiecutter.plugin_name }}
```

- Build the plugin
```
$ python setup.py develop
```

- Alembic configuration for extra tables
```
$ mv alembic.example.ini alembic.ini
```
- Edit the alembic.ini an replace sqlalchemy.url with the one in the FormShare ini file
```    
$ alembic revision --autogenerate -m "Initial version"
$ alembic upgrade head
```

- Add the plugin to the {{ cookiecutter.plugin_for }} list of plugins by editing the following line in development.ini or production.ini
```
    #{{ cookiecutter.plugin_for }}.plugins = examplePlugin
    {{ cookiecutter.plugin_for }}.plugins = {{ cookiecutter.plugin_name }}
```

- Run {{ cookiecutter.plugin_for }} again
