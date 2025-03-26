# 1-2. Hello World Typos

I tried making a few typos in the `hello_world.py` file:

# (a) A typo that causes an error:

```python
print("Hello World)  # Missing closing quote
```

**Error:**
```python
SyntaxError: EOL while scanning string literal
```

**Analysis:** Python detects an unclosed string.

---

## (b) A typo that causes an error but is not a syntax issue:

```python
pritn("Hello World")  # Typo in 'print'
```

**Error:**
```python
NameError: name 'pritn' is not defined
```

Python assumes `pritn` is an undefined variable, not the `print()` function.

---

## (c) A typo that does not cause an error but changes the output:

```python
print("Helo World")  # Typo in 'Hello'
```

**Output:**
```python
Helo World
```

**Analysis:** Python still executes the code because there is no syntax error, just a mistake in the text itself.
