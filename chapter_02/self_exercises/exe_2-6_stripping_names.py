# Assign a value to the variable 'person_name' with leading and trailing whitespace
person_name = "\t\n Agatha Christie \t\n"

# Print the name with visible whitespace
print(f"Original: '{person_name}'")

# Print the name after removing leading whitespace using lstrip()
print(f"Lstrip: '{person_name.lstrip()}'")

# Print the name after removing trailing whitespace using rstrip()
print(f"Rstrip: '{person_name.rstrip()}'")

# Print the name after removing both leading and trailing whitespace using strip()
print(f"Strip: '{person_name.strip()}'")


"""
Explanation:

1️⃣ The variable `person_name` is assigned with a string containing leading and trailing whitespace.
   - `\t` (tab) and `\n` (new line) are used to create extra spacing.
2️⃣ The first `print()` statement displays the original value with whitespace.
3️⃣ The `.lstrip()` method removes leading spaces, tabs, and newlines.
4️⃣ The `.rstrip()` method removes trailing spaces, tabs, and newlines.
5️⃣ The `.strip()` method removes spaces from both ends.

✅ Key concepts:
   - **String manipulation**: Handling whitespace efficiently.
   - **String methods**: `.lstrip()`, `.rstrip()`, and `.strip()`.
   - **Text formatting**: Improving readability in output.

📌 This is useful when working with user inputs, file data, or database entries where extra whitespace might cause issues.
"""
