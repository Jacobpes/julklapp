# create a scipt to read a specific line from item_id_memory.txt according to user input

# scan user input for sender name and return the corresponding receiver name

# file is written like this:
#  with open('item_id_memory.txt', 'a') as file:
#             file.write(f"{giver} buys for {receiver}\n")
#         file.close()

# read the lines and split the lines by " buys for " and return the line that has giver in [0]
def get_receiver(sender):
    with open('item_id_memory.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        if sender == line.split(" buys for ")[0]:
            return line.split(" buys for ")[1]
    return None

print(get_receiver("Amanda"))