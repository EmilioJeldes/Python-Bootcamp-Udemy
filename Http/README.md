# HTTP
Using ``requests`` module to make http requests.

### Syntax
`````python
import requests
`````

### Get response
`````python
res = requests.get(url_string)
`````


### Pass headers
`````python
res = requests.get(url_string, headers = {"Accept": "application/json"})
`````

### Pass params
`````python
res = requests.get(url, params = {"param-name": param_value})
`````

### Get text representation of html (string)
`````python
text_html = res.text
`````

### Get dictionary representation (json)
`````python
text_json = res.json()
`````