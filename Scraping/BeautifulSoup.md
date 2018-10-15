# BeautifulSoup

#### Import
````python
from bs4 import BeautifulSoup
````

#### Syntax
````python
soup = BeautifulSoup(html_string, "html.parser")
````

#### Find methods
````python
# By tagname
first_div = soup.body.div

# One matching tag (first one)
div = soup.find('div')

# A list of matching tags
div_list = soup.find_all('div')

````

#### Find params
````python
# Find by id
find_id = soup.find(id='id-name')

# Find by class
find_class = soup.find(class_='class-name')
find_list_class = soup.find_all(class_='class-name')

# Find by attribute
find_attr = soup.find_all(attrs={"atribute-name": "value"})
find_attr = soup.find_all(attrs="attribute-name")
````

#### Find using CSS Selectors
`````python
# IT ALWAYS RETURNS A LIST

# Select by id
select_id = soup.select('#id-name')

# select by class
select_class = soup.select('.class-name')

# Select by attribute
select_attr = soup.select('[attribute-name]')
`````

#### Accessing data of a tag
`````python
el = soup.select('.class-name')[0]
# Access inner text of a tag
title = el.get_text()

# Access tag name
tag_name = el.name

# Access attributes
attr = el["atribute-name"]
`````

#### Navigating elements
**Vía Tags:**
`````python
# Contents returns a list with '\n' after each element
# To access next element you need to skip 1 after
data = soup.body.contents[1]

# Parent / Parents
parent = data.parent

# next_sibling / next_siblings
# returns '\n' so you have to use it twice
next_el = data.next_sibling.next_sibling

# previous_sibling / previous_siblings
prev_sibling = data.previous_sibling
`````

**Vía Searching Methods:**
`````python
# Using seach mathods does not return '\n'
# Can add filter classes, id's or attributes inside methods
data = soup.find(id="id-name")

# find_parent / find_parents
parent = soup.find_parent()

# find_next_sibling / find_next_siblings
next_sibl = data.find_next_sibling()

# find_previous_sibling() 
prev_sibl = data.find_previous_sibling(class_='class-name')
`````