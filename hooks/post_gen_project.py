from textwrap import dedent


def main():
    display_actions_message()


def display_actions_message():

    vars = dict(separator="=" * 79)
    msg = dedent(
        """
        %(separator)s
        This is a scaffolding of a {{ cookiecutter.plugin_for }} plugin. You can use it
        to create complex plugins.
        %(separator)s

        To make {{ cookiecutter.plugin_for }} to run this plugin do:
            
        Activate the {{ cookiecutter.plugin_for }} environment .
            . /path/to/{{ cookiecutter.plugin_for }}/bin/activate
            
        Change directory into your newly created plugin.
            cd {{ cookiecutter.plugin_name }}

        Build the plugin
            python setup.py develop
        
        Create an initial version of the DB for the plugin
            mv alembic.example.ini alembic.ini
            --Edit the alembic.ini an replace sqlalchemy.url with the one in the {{ cookiecutter.plugin_for }} ini file
            alembic revision --autogenerate -m "Initial version"
        
        Apply the initial version of the DB
            alembic upgrade head

        Add the plugin to the {{ cookiecutter.plugin_for }} list of plugins by editing the line
            #{{ cookiecutter.plugin_for }}.plugins = examplePlugin
            {{ cookiecutter.plugin_for }}.plugins = {{ cookiecutter.plugin_name }}
        

        Run {{ cookiecutter.plugin_for }} again
        """
        % vars
    )
    print(msg)


if __name__ == "__main__":
    main()
