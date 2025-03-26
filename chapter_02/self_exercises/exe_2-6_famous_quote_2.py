# Assign a value to the variable 'famous_person'
famous_person = 'marcus aurelius'

# Assign a quote to the variable 'message'
message = "once said, \"You have power over your mind - not outside events. Realize this, and you will find strength.\""

# Prit the formatted output
print(f"\n\t{famous_person.title()} {message}")

"""
Explanation:

1️⃣ We assign the string `'marcus aurelius'` to the variable `famous_person`, storing the name of the philosopher.
2️⃣ The variable `message` holds the quote, using an **escaped double quote** (`\"`) to include quotation marks within the string.
3️⃣ The `print()` function formats and prints the output:
   - `\n` adds a **new line** before the quote for better readability.
   - `\t` adds a **tab space** for indentation.
   - `{famous_person.title()}` capitalizes the first letters of each word using `.title()`, making the name properly formatted.
4️⃣ The final output appears as:

Marcus Aurelius once said, "You have power over your mind - not outside events. Realize this, and you will find strength."

✅ **Key concepts in this exercise:**
- **Variable assignment:** Storing strings in `famous_person` and `message`.
- **String formatting:** Using `f"{variable}"` for cleaner output.
- **Escape sequences:** `\"` allows us to include double quotes inside the string.
- **Whitespace characters:** `\n` (new line) and `\t` (tab) improve readability.

📌 This technique is useful for printing well-structured quotes, formatted messages, or styled text output in Python.
"""
