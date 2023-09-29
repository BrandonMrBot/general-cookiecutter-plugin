from jinja2.ext import babel_extract as extract_jinja2
import {{ cookiecutter.plugin_for }}.config.jinja_extensions as je

jinja_extensions = """
                    jinja2.ext.do, jinja2.ext.with_,
                    {{ cookiecutter.plugin_for }}.config.jinja_extensions.SnippetExtension,
                    {{ cookiecutter.plugin_for }}.config.jinja_extensions.ResourceExtension,
                    {{ cookiecutter.plugin_for }}.config.jinja_extensions:JSResourceExtension,
                    {{ cookiecutter.plugin_for }}.config.jinja_extensions:CSSResourceExtension,
                    {{ cookiecutter.plugin_for }}.config.jinja_extensions.extendThis,
                   """

# This function take badly formatted html with strings etc and make it beautiful
# generally remove surlus whitespace and kill \n this will break <code><pre>
# tags but they should not be being translated '''
def jinja2_cleaner(fileobj, *args, **kw):

    # Extract the messages from jinja2 files but taking into consideration custom extensions

    # This code is based on CKAN
    # :Copyright (C) 2007 Open Knowledge Foundation
    # :license: AGPL V3, see LICENSE for more details.

    kw["options"]["extensions"] = jinja_extensions

    raw_extract = extract_jinja2(fileobj, *args, **kw)

    for lineno, func, message, finder in raw_extract:

        if isinstance(message, str):
            message = je.regularise_html(message)
        elif message is not None:
            message = (je.regularise_html(message[0]), je.regularise_html(message[1]))

        yield lineno, func, message, finder


def extract_{{ cookiecutter.plugin_for }}(fileobj, *args, **kw):

    # This custom extractor is to support customs tags in the jinja2 extractions. Otherwise the normal extract fail

    # This code is based on CKAN
    # :Copyright (C) 2007 Open Knowledge Foundation
    # :license: AGPL V3, see LICENSE for more details.

    fileobj.read()
    output = jinja2_cleaner(fileobj, *args, **kw)
    fileobj.seek(0)
    return output
