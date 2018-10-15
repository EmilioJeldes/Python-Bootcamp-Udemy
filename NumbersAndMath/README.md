# Numbers, Math & Casting

Numbers and math syntax

## Numbers
### 1. ``int()``
```python
num = 1
```

### 2. ``float()``
`````python
num = 2.3
`````

## Math
### 1. Sum, ``sum(iterable)``
float + int returns a float
`````python
num_sum = sum((1, 2, 3, 4, 5))  # 15
num_sum = 1 + 2 + 3 + 4
num_sum = (1 + 4) + 5 + (2 + 5)
`````

### 2. Multiplication
float * int returns a float
`````python
mult_nums = 2 * 4
`````

### 3. Division
Division always returns a float, 
unless is an integer division // in which case returns an int
* #### a. Float division
`````python
division_float = 4 / 2  #  2.0
division_float = 3 / 5  #  0.6
`````

* #### b. Integer division
`````python
int_division = 4 // 2  # 2
`````

## Casting
###1. Cast to int
`````python
num = int('2')  # 2
num = int(2.5)  # 2
`````

### 2. Cast to float 
````python
num = float('2')  # 2.0
num = float(2)    # 2.0
````