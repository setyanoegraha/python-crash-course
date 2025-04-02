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

print()

# Guest who can't make it
unable_to_attends = 'joana'
print(
    f"Unfotunately, {unable_to_attends.title()} can't make it to the dinner.\n")

# Removing the guest who can't attend in a mosque
guests.remove(unable_to_attends)
print("These are the guests who could attend:")
print(guests)

# Replace the guest who can't attend  with a new guest
new_guest = 'einar'
guests.insert(0, new_guest)
print("\nThese are the new list guests who could attend:")
print(guests)

# Print personalized invitations message to the new guests list
print(
    f"\nGood Night, My Beloved Bestfriend {guests[0].title()}, Since we've been on friendly terms for a long time. I invite you all to dinner on March 28 at Avenue Street, Brooklyn Cafe.")
print(
    f"\nGood Night, My Beloved Bestfriend {guests[1].title()}, Since we've been on friendly terms for a long time. I invite you all to dinner on March 28 at Avenue Street, Brooklyn Cafe.")
print(
    f"\nGood Night, My Beloved Bestfriend {guests[2].title()}, Since we've been on friendly terms for a long time. I invite you all to dinner on March 28 at Avenue Street, Brooklyn Cafe.")
print(
    f"\nGood Night, My Beloved Bestfriend {guests[3].title()}, Since we've been on friendly terms for a long time. I invite you all to dinner on March 28 at Avenue Street, Brooklyn Cafe.")
print(
    f"\nGood Night, My Beloved Bestfriend {guests[4].title()}, Since we've been on friendly terms for a long time. I invite you all to dinner on March 28 at Avenue Street, Brooklyn Cafe.")
print(
    f"\nGood Night, My Beloved Bestfriend {guests[5].title()}, Since we've been on friendly terms for a long time. I invite you all to dinner on March 28 at Avenue Street, Brooklyn Cafe.")
print(
    f"\nGood Night, My Beloved Bestfriend {guests[6].title()}, Since we've been on friendly terms for a long time. I invite you all to dinner on March 28 at Avenue Street, Brooklyn Cafe.")
print(
    f"\nGood Night, My Beloved Bestfriend {guests[-1].title()}, Since we've been on friendly terms for a long time. I invite you all to dinner on March 28 at Avenue Street, Brooklyn Cafe.")

"""
Explanation:

1️⃣ **Creating a guest list:** I store names of friends in a list called `guests`.
2️⃣ **Printing invitations:** I use f-strings and `.title()` to format names properly while inviting each guests.
3️⃣ **Handling an unavailable guest:**
    - A variable `unable_to_attends` stores the name of a guest who can't attend.
    - I remove this guest from the list using `.remove()`.
    
"""
