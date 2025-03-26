# Assign a URL string with a common prefix and a trailing slash
google_url = 'https://www.google.com/'

# Remove the "https://www." prefix using removeprefix()
google_without_prefix = google_url.removeprefix('https://www.')
print(google_without_prefix)  # Output: google.com/

# Remove the trailing slash using removesuffix()
google_cleaned = google_without_prefix.removesuffix('/')
print(google_cleaned)  # Output: google.com

"""
Explanation:

1️⃣ We assign the URL `'https://www.google.com/'` to the variable `google_url`.
2️⃣ We use `.removeprefix('https://www.')` to remove the **leading part** of the URL.
    - The result is stored in `google_without_prefix` and printed: `'google.com/'`
3️⃣ We then use `.removesuffix('/')` to remove the **trailing slash**.
    - The result is stored in `google_cleaned` and printed: `'google.com'`
4️⃣ Each step is printed separately to clearly show the effect of each method.

✅ Key concepts in this exercise:
   - **String assignment:** Storing a URL as a string.
   - **String manipulation:** Removing unwanted prefixes and suffixes.
   - **Printing modified strings:** Displaying step-by-step changes for clarity.

📌 This is useful for processing URLs where you need a clean domain name.
"""
