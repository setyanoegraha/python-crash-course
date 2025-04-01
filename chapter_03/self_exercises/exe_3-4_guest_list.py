# Create a list of guests to invite
# The list contains names of friends who will receive an invitation.
guests = ['joana', 'cynthia', 'kyle', 'kenny',
          'niche', 'wezler', 'brock', 'gargan']

# Print personalized dinner invitations for each guest
print(
    f"Hello, My Dearest Friend {guests[0].title()}! I would like to invite you to dinner. I look forward to an insightful conversation with you!\n")
print(
    f"Hello, My Dearest Friend {guests[1].title()}! I would like to invite you to dinner. I look forward to an insightful conversation with you!\n")
print(
    f"Hello, My Dearest Friend {guests[2].title()}! I would like to invite you to dinner. I look forward to an insightful conversation with you!\n")
print(
    f"Hello, My Dearest Friend {guests[3].title()}! I would like to invite you to dinner. I look forward to an insightful conversation with you!\n")
print(
    f"Hello, My Dearest Friend {guests[4].title()}! I would like to invite you to dinner. I look forward to an insightful conversation with you!\n")
print(
    f"Hello, My Dearest Friend {guests[5].title()}! I would like to invite you to dinner. I look forward to an insightful conversation with you!\n")
print(
    f"Hello, My Dearest Friend {guests[6].title()}! I would like to invite you to dinner. I look forward to an insightful conversation with you!\n")
print(
    f"Hello, My Dearest Friend {guests[-1].title()}! I would like to invite you to dinner. I look forward to an insightful conversation with you!\n")

"""
Explanation:

1️⃣ We define a list called `guests`, which contains eight names of friends.
2️⃣ Each `print()` statement generates a personalized dinner invitation.
3️⃣ `f-strings` are used to insert the guest's name dynamically into the invitation text.
4️⃣ `.title()` is applied to each guest's name to ensure proper capitalization.
5️⃣ Negative indexing (`guests[-1]`) is used to access the last element (`gargan`).
6️⃣ The invitations are formatted with `\n` to create line breaks for better readability.

✅ Key concepts demonstrated:
   - **Lists:** Storing multiple names in an ordered sequence.
   - **String Methods:** `.title()` capitalizes the first letter of each name.
   - **Formatted Strings (f-strings):** Dynamic string interpolation for better readability.
   - **Indexing:** Using both positive (`guests[0]`) and negative (`guests[-1]`) indexing.
   
📝 This snippet showcases list operations and string formatting to generate multiple personalized messages efficiently.
"""
