# Assign a filename with an extension to the variable 'filename'
filename = 'python_notes.txt'

# Remove the '.txt' suffix from the filename and print the result
print(filename.removesuffix('.txt'))

"""
Explanation
1️⃣ The variable filename stores the string 'python_notes.txt', which represents a filename with a .txt extension.
2️⃣ The .removesuffix('.txt') method is used to remove the .txt part from the end of the string if it exists.
3️⃣ The print() function then displays the modified filename without the extension, resulting in 'python_notes'.
4️⃣ If the string does not end with .txt, removesuffix() would return the original string unchanged.

✅ Key Concepts:

String manipulation: Removing a specific suffix from a string.

String method .removesuffix(): Introduced in Python 3.9, it ensures suffix removal without errors.

Practical use case: Useful when processing filenames, URLs, or text formatting.
"""
