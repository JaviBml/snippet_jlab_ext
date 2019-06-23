from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler
from snippets_catalog.analyze_python_code import catalog_file

import json
import tornado.web


class SnippetsCatalogHandler(IPythonHandler):
    """Request handler where requests and responses speak JSON."""

    def get(self):
        catalog = {}
        target_urls = self.get_query_arguments("url")
        for url in target_urls:
            catalog[url] = catalog_file(url)

        self.response = catalog
        self.write_json()

    def prepare(self):
        # Incorporate request JSON into arguments dictionary.
        if self.request.body:
            try:
                json_data = json.loads(self.request.body)
                self.request.arguments.update(json_data)
            except ValueError:
                message = 'Unable to parse JSON.'
                self.send_error(400, message=message) # Bad Request

        # Set up response dictionary.
        self.response = dict()

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def write_error(self, status_code, **kwargs):
        if 'message' not in kwargs:
            if status_code == 405:
                kwargs['message'] = 'Invalid HTTP method.'
            else:
                kwargs['message'] = 'Unknown error.'

        self.response = kwargs
        self.write_json()

    def write_json(self):
        output = json.dumps(self.response)
        self.write(output)



def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    print('its a trap')
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], '/snippets')
    web_app.add_handlers(host_pattern, [(route_pattern, SnippetsCatalogHandler)])
