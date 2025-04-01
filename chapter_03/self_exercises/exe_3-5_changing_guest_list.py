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
print(guests)

# Replace the guest who can't attend  with a new guest
new_guest = 'einar'
guests.insert(0, new_guest)
print(guests)
