from {{ cookiecutter.plugin_name }}.orm.{{ cookiecutter.plugin_name }} import ExampleTable

from sqlalchemy.orm import configure_mappers
from {{ cookiecutter.plugin_for }}.models.schema import initialize_schema

configure_mappers()


def includeme(config):
    initialize_schema()