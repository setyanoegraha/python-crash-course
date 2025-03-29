# Create a list of transportation vehicles
transportations = ['gtr', 'subaru', 'mustang', 'custom', 'nissan', 'maserati']

# Print statements expressing different thoughts about each vehicle
print(f"I would like to own a {transportations[0].upper()} as my first car.")
print(
    f"I have always dreamed of owning a {transportations[1].title()} for my off-road adventures.")
print(
    f"The roar of the {transportations[2].title()}'s engine echoed through the empty streets at midnight.")
print(
    f"Joan decided to build a {transportations[3].title()} race car to compete in local drifting competition.")
print(
    f"The {transportations[4].title()} Skyline is one of the most iconic sports car ever made.")
print(
    f"With the sleek design and powerful engine, The {transportations[-1].title()} is the definition of luxury.")

"""
Explanation:

1️⃣ We create a list called `transportations` containing six vehicle names.
2️⃣ Each `print()` statement constructs a sentence using one element from the list.
3️⃣ String formatting (`f-strings`) is used to insert vehicle names dynamically.
4️⃣ `.upper()` is applied to the first element (`transportations[0]`) to convert it to uppercase.
5️⃣ `.title()` is used on other elements to capitalize the first letter of each word.
6️⃣ Negative indexing (`transportations[-1]`) is used to access the last item (`maserati`).

✅ Key concepts in this exercise:
   - **Lists:** Store multiple vehicle names in an ordered sequence.
   - **String Methods:** `.upper()` capitalizes all letters, `.title()` capitalizes the first letter.
   - **Formatted Strings (f-strings):** Allow inserting variables dynamically into sentences.
   - **Indexing:** Both positive (`transportations[0]`) and negative (`transportations[-1]`) indexing are demonstrated.

📝 This snippet creatively applies list indexing and string manipulation to express preferences about different vehicles.
"""
