import ast
from pprint import pprint

from IPython.core.interactiveshell import InteractiveShell
from IPython.core.getipython import get_ipython

def catalog_file(path_or_url):
    """Helper function to extract functions and classes data from the given code file."""
    return analyze_source_code(retrieve_source_code(path_or_url))

def retrieve_source_code(path_or_url):
    """Retrieve a source code string from a file, url or string."""

    ipython_shell = get_ipython() or InteractiveShell()
    source = ipython_shell.find_user_code(path_or_url, raw=False, py_only=True, skip_encoding_cookie=True, search_ns=False)

    return source

def analyze_source_code(source):
    """
    Analyze the given source code (str), extracting functions and classes.

    Returns:
    --------
      dict: with "classes" and "functions" keys. Each value is another dict with (name, docstring)
            values.
    """
    tree = ast.parse(source)
    print()
    analyzer = PythonCodeAnalyzer()
    analyzer.visit(tree)
    return analyzer.report()


class PythonCodeAnalyzer(ast.NodeVisitor):
    """Analyze the AST, extracting functions and classes definitions."""

    def __init__(self):
        self.classes = {}
        self.functions = {}

    def visit_ClassDef(self, node):
        self.classes[node.name] = ast.get_docstring(node)
        # Don't call self.generic_visit(node) because we don't want to extract class methods

    def visit_FunctionDef(self, node):
        self.functions[node.name] = ast.get_docstring(node)
        self.generic_visit(node)

    def report(self):
        return {"classes": self.classes, "functions": self.functions}


if __name__ == "__main__":
    import sys
    pprint(
        catalog_file(sys.argv[1])
    )
