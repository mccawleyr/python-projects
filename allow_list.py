# Algorithm for file updates in Python
#
# Ryan McCawley 24 Apr 2024 #
#
# This project will read the contents of an ip address text file
# The update_file function will be given a list of IP addresses to be removed
# The text file will the be updated with those IPs removed.

# The function `update_file` uses two parameters: `import_file` and `remove_list`
def update_file(import_file, remove_list):

  # Read the initial contents of the file and store it in a variable
  with open(import_file, "r") as file:
    ip_addresses = file.read()

  # Convert from a string to a list
  ip_addresses = ip_addresses.split()

  # Iterative statement
  # Loop element through ip address list.
  # Remove the ip if it's in remove list
  for element in ip_addresses:
    if element in remove_list:
      ip_addresses.remove(element)

  # Convert back to a string so that it can be written into the text file     
  ip_addresses = " ".join(ip_addresses)

  # Rewrite the original file, replacing contents with ip_addresses
  with open(import_file, "w") as file:
    file.write(ip_addresses)

# Call function to introduce ip address text file and list of IPs to remove
update_file("allow_list.txt", ["192.168.25.60", "192.168.140.81", "192.168.203.198"])

# Read in the updated file and store the contents in `text`
with open("allow_list.txt", "r") as file:
  text = file.read()

# Display the contents of `text`
print(text)