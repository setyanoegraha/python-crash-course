# ✅ Correct usage with double quotes
message = "One of Python's strengths is its diverse community."
print(message)

# ❌ Incorrect usage with single quotes (will cause a syntax error if uncommented)
# message = 'One of Python's strengths is its diverse community.'
# print(message)

# ✅ Correct usage with escaped apostrophe in single quotes
message = 'One of Python\'s strengths is its diverse community.'
print(message)

# ✅ Correct usage with triple quotes
message = """One of Python's strengths is its diverse community."""
print(message)

"""
📌 Explanation:

1️⃣ `"   "` (double quotes) allow an apostrophe inside without issues.
2️⃣ `'   '` (single quotes) with an apostrophe causes a **SyntaxError**.
3️⃣ `\'` (escaping the apostrophe) in single quotes prevents errors.
4️⃣ `"""   """` (triple quotes) also allow apostrophes without escaping.

✅ **Key concepts in this exercise:**
   - **Using different string delimiters (`"` and `'`)**.
   - **Escaping characters (`\'`) when necessary**.
   - **Avoiding syntax errors caused by improper string usage**.

🛠️ **Best Practice:**
Use double quotes (`"..."`) if your string contains an apostrophe to keep your code clean and readable.
"""
