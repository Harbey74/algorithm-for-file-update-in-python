# Python Allow List Algorithm
# This script updates an IP allow list by removing specified IP addresses that are no longer allowed.

# Assign `import_file` to the name of the file containing the IP allow list
import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that should be removed from the allow list
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Step 1: Read the initial contents of the allow list file
with open(import_file, "r") as file:
    # Read the entire contents of the file into a string variable
    ip_addresses = file.read()

# Step 2: Convert the string of IP addresses into a list for easier processing
ip_addresses = ip_addresses.split()

# Step 3: Iterate through the list of IP addresses
# Use a copy of the list to safely remove elements while looping
for element in ip_addresses[:]:
    # If the current IP address is in the remove_list
    if element in remove_list:
        # Remove it from the ip_addresses list
        ip_addresses.remove(element)

# Step 4: Convert the list back into a string so it can be written into the file
# Each IP address is separated by a newline for readability
ip_addresses = "\n".join(ip_addresses)

# Step 5: Rewrite the original file with the updated IP addresses
with open(import_file, "w") as file:
    # Overwrite the file contents with the revised list
    file.write(ip_addresses)

# Step 6: Read and display the updated file to verify changes
with open(import_file, "r") as file:
    text = file.read()

print("Updated IP allow list:\n")
print(text)
