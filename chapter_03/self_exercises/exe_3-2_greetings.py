# Create a list of names
names = ['john', 'greg', 'sheila', 'alisha', 'megan']

# Print out a personalized message for each name with the first letter capitalized
print(
    f"Hey! {names[0].title()}, how do you feel after learning python? You look so fresh.\n")
print(
    f"Hey! {names[1].title()}, how do you feel after learning python? You look so fresh.\n")
print(
    f"Hey! {names[2].title()}, how do you feel after learning python? You look so fresh.\n")
print(
    f"Hey! {names[3].title()}, how do you feel after learning python? You look so fresh.\n")
print(
    f"Hey! {names[4].title()}, how do you feel after learning python? You look so fresh.\n")

"""
1️⃣ We create a list named `names` that contains five lowercase names.
2️⃣ Each `print()` statement displays a personalized message for one name.
3️⃣ We use `names[index].title()` to capitalize the first letter of each name.
4️⃣ The `f-string()` (formatted string) dynamically inserts the names into the message.
5️⃣ The same message is repeated for each name, but with proper capitalization.

✅ Key concepts in this exercise:
   - **Lists:** We store multiple names in an ordered collection.
   - **String Methods:** `.title()` capitalizes the first letter of each name.
   - **Formatted Strings (f-strings):** Allow dynamic insertion of variables into a string.
   - **Indexing:** Each name is accessed via its position in the list.

📝 While this code works correctly, it could be optimized using a loop to reduce redundancy. However, for learning purposes, this approach clearly shows how to access and format list elements individually.
"""
