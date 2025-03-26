# Assign first and last name to variables
first_name = "lord"
last_name = "griffin"

# Create a full name using an f-string
full_name = f"{first_name} {last_name}"

# Print the full name
print(full_name)  # Output: "lord griffin"

# Print a greeting message using title case
print(f"Hello, {full_name.title()}!")  # Output: "Hello, Lord Griffin!"

# Store the greeting message in a variable
message = f"Hello, {full_name.title()}!"

# Print the message
print(message)  # Output: "Hello, Lord Griffin!"

"""
Explanation:

1️⃣ We declare two variables: `first_name` and `last_name` to store a person's name.
2️⃣ We create `full_name` using an **f-string** (formatted string) to combine first and last names.
3️⃣ We print `full_name` to display the full name.
4️⃣ We use `full_name.title()` to format the name in title case before displaying a greeting.
5️⃣ We store the greeting message in a variable `message` and print it.

✅ Key concepts in this exercise:
   - **String concatenation using f-strings (`f"{var}"`)** for cleaner, more readable formatting.
   - **Using `.title()` to capitalize the first letter of each word** for better presentation.
   - **Storing formatted strings in variables** for reuse and better program organization.

📌 This is useful for dynamically generating and formatting user messages, such as in chat applications or automated responses.
"""
