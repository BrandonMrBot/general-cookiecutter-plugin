import {{ cookiecutter.plugin_for }}.plugins as plugins
import {{ cookiecutter.plugin_for }}.plugins.utilities as u
from {{ cookiecutter.plugin_name }}.views import MyPublicView, MyPrivateView
import sys
import os


class {{ cookiecutter.plugin_name }}(plugins.SingletonPlugin):
    plugins.implements(plugins.IRoutes)
    plugins.implements(plugins.IConfig)
    #plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IDatabase)

    def before_mapping(self, config):
        # We don't add any routes before the host application
        return []

    def after_mapping(self, config):
        # We add here a new route /json that returns a JSON
        custom_map = []
        custom_map = [
            u.add_route(
                "plugin_mypublicview", "/mypublicview", MyPublicView, "public.jinja2"
            ),
            u.add_route(
                "plugin_myprivateview",
                "/user/{userid}/myprivateview",
                MyPrivateView,
                "private.jinja2",
            ),
        ]

        return custom_map

    def update_config(self, config):
        # We add here the templates of the plugin to the config
        u.add_templates_directory(config, "templates")

    def get_translation_directory(self):
        module = sys.modules["{{ cookiecutter.plugin_name }}"]
        return os.path.join(os.path.dirname(module.__file__), "locale")

    def get_translation_domain(self):
        return "{{ cookiecutter.plugin_name }}"

    def update_orm(self, config):
        config.include("{{ cookiecutter.plugin_name }}.orm")

    def update_extendable_tables(self, tables_allowed):
        tables_allowed.append("{{ cookiecutter.plugin_name }}_example")
        return tables_allowed

    def update_extendable_modules(self, modules_allowed):
        modules_allowed.append("{{ cookiecutter.plugin_name }}.orm.{{ cookiecutter.plugin_name }}")
        return modules_allowed
