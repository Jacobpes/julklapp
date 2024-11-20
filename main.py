import random

# List of people
people = [["Dani", "Emmi"], ["Evert", "Maria"], ["Jacob", "Amanda"], ["Albert", "Jemina"], ["Juulia", "Junna"], ["Tony"]]

def assign_gifts(people):
    # Create a list of all people
    all_people = [person for pair in people for person in pair]
    # Create a dictionary to keep track of assigned gifts
    gift_assignments = {}

    # Function to check if an assignment is valid
    def is_valid_assignment(giver, receiver):
        # Check if the receiver is the partner of the giver
        for pair in people:
            if giver in pair and receiver in pair:
                return False
        # Check if the receiver has already been assigned a gift
        if receiver in gift_assignments.values():
            return False
        # Check if the receiver is already assigned to give a gift to the giver
        if gift_assignments.get(receiver) == giver:
            return False
        return True

    # Assign gifts
    for giver in all_people:
        possible_receivers = [person for person in all_people if person != giver and is_valid_assignment(giver, person)]
        if not possible_receivers:
            # If there are no valid receivers, restart the assignment process
            return assign_gifts(people)
        receiver = random.choice(possible_receivers)
        gift_assignments[giver] = receiver

    # Print assignments
    for giver, receiver in gift_assignments.items():
        print(f"{giver} buys a gift for {receiver}")

assign_gifts(people)
