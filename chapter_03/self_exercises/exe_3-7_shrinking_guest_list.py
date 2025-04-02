# Create a list of guests to invite
guests = ['joana', 'cynthia', 'kyle', 'kenny',
          'niche', 'wezler', 'brock', 'gargan']

# Print personalized dinner invitations for each guest
for guest in guests:
    print(
        f"Hello, My Dearest Friend {guest.title()}! I would like to invite you to dinner. I look forward to an insightful conversation with you!\n")

print("There is a little problem.")

# Guest who can't make it
unable_to_attend = 'joana'
print(
    f"Unfortunately, {unable_to_attend.title()} can't make it to the dinner.\n")

# Remove the guest who can't attend
guests.remove(unable_to_attend)
print("These are the guests who could attend:")
print(guests)

# Replace the guest who can't attend with a new guest
new_guest = 'einar'
guests.insert(0, new_guest)
print("\nThese are the new list of guests who could attend:")
print(guests)

# Print new invitations
for guest in guests:
    print(
        f"\nGood Night, My Beloved Bestfriend {guest.title()}, Since we've been on friendly terms for a long time. I invite you all to dinner on March 28 at Avenue Street, Brooklyn Cafe.")

# Due to finding a bigger table, more guests are invited
print("\n\tBecause I found a bigger table at the cafe, I'm deciding to invite four more guests to dinner.")

# Adding four additional guests
additional_guests = [('andera', 0), ('kana', 4),
                     ('yulensky', 5), ('anwar', len(guests))]
for name, position in additional_guests:
    guests.insert(position, name)
    print(f"I'm deciding to invite {name.title()} as an additional guest.")

# Print the updated guest list
print("\nHere are the new guests list:")
print(guests)

# Send updated invitations
for guest in guests:
    print(f"\nDear {guest.title()}, you're invited to dinner at Brooklyn Cafe, Avenue Street on March 28th at 7:00 PM. Your table number is 21. See you there!")

# Due to an issue, only two guests can be invited
print("\nIt turns out that the dinner table won't arrive in time, and now I'm ashamed about this.")
print("Due to this situation, I can only invite two people for dinner.")

# Remove guests until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"\nSorry, {removed_guest.title()}, I regret to inform you that I can't invite you to dinner due to limited space.")

# Notify the final two guests that they are still invited
for guest in guests:
    print(f"\n{guest.title()}, you are still invited to dinner.")

# Remove the last two guests and ensure the list is empty
del guests[:]
print("\nFinal guest list:", guests)
