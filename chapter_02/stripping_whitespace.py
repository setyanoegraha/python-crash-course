# Assign a value into a variable with leading and trailing spaces
favorite_language = " python "

# Print out the variable, showing the leading and trailing spaces clearly
print(f"'{favorite_language}'")  # Output: ' python '

# Print out the variable after removing the trailing space on the right side using rstrip()
print(f"'{favorite_language.rstrip()}'")  # Output: ' python'

# Print out the variable after removing the leading space on the left side using lstrip()
print(f"'{favorite_language.lstrip()}'")  # Output: 'python '

# Print out the variable after removing spaces on both sides using strip()
print(f"'{favorite_language.strip()}'")  # Output: 'python'

"""
Explanation:

1️⃣ We assign the string `" python "` to the variable `favorite_language`, which includes leading and trailing spaces.
2️⃣ The first `print(f"'{favorite_language}'")` statement displays the value with both spaces.
3️⃣ We use `.rstrip()` to remove the **trailing whitespace** (spaces, tabs, or newlines) from the right side.
4️⃣ We use `.lstrip()` to remove the **leading whitespace** from the left side.
5️⃣ We use `.strip()` to remove **both leading and trailing whitespaces**.

✅ Key concepts in this exercise:
   - **String assignment:** Storing a string with both leading and trailing spaces.
   - **Printing strings:** Using `print()` to show how different strip methods affect the string.
   - **String methods:**
     - `.rstrip()` removes only the right-side spaces.
     - `.lstrip()` removes only the left-side spaces.
     - `.strip()` removes spaces from both sides.

📌 This is useful when handling user input or processing text where extra spaces might cause formatting issues.
"""
