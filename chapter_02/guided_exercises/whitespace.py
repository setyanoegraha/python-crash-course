# Print "Python" followed by a newline
print("Python\n")  # Output: "Python" with an extra blank line after it

# Print "Python" with a tab space before it, followed by a newline
# Output: "    Python" (indented with a tab) with an extra blank line after it
print("\tPython\n")

# Print a list of programming languages, each on a new line
print("Languages:\nPython\nC\nJavaScript\nC++\nRust\n")

"""
Output:
Languages:
Python
C
JavaScript
C++
Rust
"""

# Print the same list but with each language indented using a tab
print("Languages:\n\tPython\n\tC\n\tJavaScript\n\tC++\n\tRust\n")

"""
Output:
Languages:
    Python
    C
    JavaScript
    C++
    Rust
"""

"""
Explanation:

1️⃣ `\n` (newline) moves text to the next line, making outputs more readable.
2️⃣ `\t` (tab) adds an indentation, useful for formatting lists.
3️⃣ The first print statement prints `"Python"` followed by a blank line.
4️⃣ The second print statement prints `"Python"` with an indentation.
5️⃣ The third print statement prints a list of languages, each on a new line.
6️⃣ The fourth print statement prints the same list, but with indentation for better presentation.

✅ Key concepts in this exercise:
   - **Escape sequences (`\n` and `\t`)** for formatting output.
   - **Newline (`\n`)** to print text on separate lines.
   - **Tab (`\t`)** to add indentation for structured output.

📌 These formatting techniques are useful for printing structured data like menus, tables, and reports.
"""
