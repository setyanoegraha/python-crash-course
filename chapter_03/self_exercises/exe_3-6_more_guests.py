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

print("There is a little problem.")

# Guest who can't make it
unable_to_attends = 'joana'
print(
    f"Unfotunately, {unable_to_attends.title()} can't make it to the dinner.\n")

# Removing the guest who can't attend in cafe
guests.remove(unable_to_attends)
print("These are the guests who could attend:")
print(guests)

# Replace the guest who can't attend with a new guest using index inserting
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

# The change of situation, Effect the guests
print("\n\tBecause I found a bigger table at the cafe, I'm deciding to invite four more guests to dinner.")

# Adding four more additional guest due to the bigger table
first_additional_guest = 'andera'
guests.insert(0, first_additional_guest)
print(
    f"I'm deciding to invite {first_additional_guest.title()} as a first additional guest.")

second_additional_guest = 'kana'
guests.insert(4, second_additional_guest)
print(
    f"My friend from japan. {second_additional_guest.title()} as a second additional guest.")

third_additional_guest = 'yulensky'
guests.insert(5, third_additional_guest)
print(
    f"My beautiful friend from Russia. {third_additional_guest.title()} as a third additional guest.")

last_additional_guest = 'anwar'
guests.append(last_additional_guest)
print(
    f"Who always have my back. {last_additional_guest.title()} as a last additional guest.")

# Printing out the new guests list after addition
print("\nHere are the new guests list:")
print(guests)

# Sending a new invitation message to each person on updated guests list
print(f"\nDear {guests[0].title()}, you're invited to dinner at Brooklyn Cafe, Avenue Street on March 28th at 7:00 PM. Your table number is 21. See you there!")
print(f"\nDear {guests[1].title()}, you're invited to dinner at Brooklyn Cafe, Avenue Street on March 28th at 7:00 PM. Your table number is 21. See you there!")
print(f"\nDear {guests[2].title()}, you're invited to dinner at Brooklyn Cafe, Avenue Street on March 28th at 7:00 PM. Your table number is 21. See you there!")
print(f"\nDear {guests[3].title()}, you're invited to dinner at Brooklyn Cafe, Avenue Street on March 28th at 7:00 PM. Your table number is 21. See you there!")
print(f"\nDear {guests[4].title()}, you're invited to dinner at Brooklyn Cafe, Avenue Street on March 28th at 7:00 PM. Your table number is 21. See you there!")
print(f"\nDear {guests[5].title()}, you're invited to dinner at Brooklyn Cafe, Avenue Street on March 28th at 7:00 PM. Your table number is 21. See you there!")
print(f"\nDear {guests[6].title()}, you're invited to dinner at Brooklyn Cafe, Avenue Street on March 28th at 7:00 PM. Your table number is 21. See you there!")
print(f"\nDear {guests[7].title()}, you're invited to dinner at Brooklyn Cafe, Avenue Street on March 28th at 7:00 PM. Your table number is 21. See you there!")
print(f"\nDear {guests[8].title()}, you're invited to dinner at Brooklyn Cafe, Avenue Street on March 28th at 7:00 PM. Your table number is 21. See you there!")
print(f"\nDear {guests[9].title()}, you're invited to dinner at Brooklyn Cafe, Avenue Street on March 28th at 7:00 PM. Your table number is 21. See you there!")
print(f"\nDear {guests[-3].title()}, you're invited to dinner at Brooklyn Cafe, Avenue Street on March 28th at 7:00 PM. Your table number is 21. See you there!")
print(f"\nDear {guests[-2].title()}, you're invited to dinner at Brooklyn Cafe, Avenue Street on March 28th at 7:00 PM. Your table number is 21. See you there!")
print(f"\nDear {guests[-1].title()}, you're invited to dinner at Brooklyn Cafe, Avenue Street on March 28th at 7:00 PM. Your table number is 21. See you there!")

"""
Explanation:

1️⃣ The program begins by printing a statement informing us that due to the discovery of a bigger table, four more guests are being invited to dinner.
2️⃣ We define the first additional guest as 'andera' and insert their name at the beginning of the 'guests' list using `.insert()`.
3️⃣ We print a message confirming that 'andera' has been added as the first additional guest.
4️⃣ The second additional guest 'kana' is defined and inserted at the 4th position in the list (index 4) using `.insert()`.
5️⃣ We print a message confirming 'kana' as the second additional guest.
6️⃣ The third additional guest 'yulensky' is defined and added to the 5th position of the list (index 5) using `.insert()`.
7️⃣ A message is printed confirming 'yulensky' as the third additional guest.
8️⃣ The last additional guest 'anwar' is added at the end of the list using `.append()`.
9️⃣ A message is printed confirming 'anwar' as the last additional guest.
🔟 The updated guest list is printed. A personalized dinner invitation is sent to each guest in the updated list using a loop and formatted strings, displaying the details of the event (date, location, and table number).

✅ Key concepts:
    - **List Manipulation:** `.insert()` adds elements at specific positions in the list, and `.append()` adds an element to the end of the list.
    - **String Formatting:** We use f-strings to format the names and print personalized messages.
    - **Looping:** The program generates invitation messages for each guest in the updated list.
    - **List Indexing:** Inserting guests at specific positions using indexes.

🚀 This method is useful for dynamically updating a guest list and sending personalized invitations based on new circumstances.
"""
