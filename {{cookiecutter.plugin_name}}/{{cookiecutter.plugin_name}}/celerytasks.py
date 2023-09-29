{% if cookiecutter.plugin_hasCeleryTasks == 'Y' or cookiecutter.plugin_hasCeleryTasks == 'y' -%}
from {{ cookiecutter.plugin_for }}.config.celery_app import celeryApp
from {{ cookiecutter.plugin_for }}.plugins.utilities import {{ cookiecutter.plugin_for }}CeleryTask
import time


@celeryApp.task(
    bind=True, base={{ cookiecutter.plugin_for }}CeleryTask, soft_time_limit=7200, time_limit=7200
)
def plugin_task():
    time.sleep(
        30
    )  # Just to test that such sleep is handled by celery and does not hang {{ cookiecutter.plugin_for }}
    print("Plugin task finished")
{%- endif %}
