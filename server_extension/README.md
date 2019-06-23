# snippets_catalog

```sh
cd server_extension/
pip install -e ./
cd ..
jupyter lab --NotebookApp.nbserver_extensions="{'snippets_catalog.snippets_catalog':True}"
```

```
http http://localhost:8888/snippets \
  url=="https://raw.githubusercontent.com/ipython/ipython/32cf29fb7962600d093b33eff7319cade67cc6ec/IPython/core/interactiveshell.py" \
  url=="server_extension/snippets_catalog/analyze_python_cod"
```

o

```
curl -X GET "http://localhost:8888/snippets?url=https://raw.githubusercontent.com/ipython/ipython/32cf29fb7962600d093b33eff7319cade67cc6ec/IPython/core/interactiveshell.py"
```
