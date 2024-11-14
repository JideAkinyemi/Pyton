# Initialize empty lists to store names and addresses
names = []
addresses = []

# Collect user input
while True:
    # Get the name from the user
    name = input("Enter a name (or type 'done' to finish): ")
    
    # Check if the user wants to finish input
    if name.lower() == 'done':
        break
    
    # Get the address from the user
    address = input("Enter the address: ")
    
    # Append the name and address to their respective lists
    names.append(name)
    addresses.append(address)

# Display the names and addresses in a tabular format
print("\nNames and Addresses:")
print(f"{'Name':<20} {'Address':<30}")
print("-" * 50)

# Loop through the lists and print each name and address
for name, address in zip(names, addresses):
    print(f"{name:<20} {address:<30}")