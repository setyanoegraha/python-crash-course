# Assign a value into a variable with a trailing space at the end
favorite_language = "python "

# Print out the variable, showing the trailing space clearly
print(f"'{favorite_language}'")  # Output: 'python '

# Print out the variable after removing the trailing space using rstrip()
print(f"'{favorite_language.rstrip()}'")  # Output: 'python'

"""
Explanation:

1️⃣ We assign the string `"python "` to the variable `favorite_language`, including a trailing space.
2️⃣ The first `print(f"'{favorite_language}'")` statement displays the value with the trailing space.
3️⃣ We use `.rstrip()` to remove the **trailing whitespace** (spaces, tabs, or newlines) from the right side of the string.
4️⃣ The second `print(f"'{favorite_language.rstrip()}'")` outputs the modified string without the trailing space.

✅ Key concepts in this exercise:
   - **String assignment:** Storing a string with a trailing space.
   - **Printing strings:** Using `print()` to display the string with and without modifications.
   - **String methods:** `.rstrip()` removes only the trailing whitespace.

📌 This is useful when handling user input or processing text where trailing spaces might cause issues.
"""
