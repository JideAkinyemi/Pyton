addresses = []
while True:
    name = input("Enter a name (or 'q' to quit): ")
    if name.lower() == 'q':
        break
    address = input("Enter the address: ")
    addresses.append({'name': name, 'address': address})


max_name_length = max(len(d['name']) for d in addresses)
max_address_length = max(len(d['address']) for d in addresses)

print("Names and Addresses:")
print("-" * (max_name_length + max_address_length + 4))
for d in addresses:
    print(f"{d['name']:>{max_name_length}} | {d['address']:<{max_address_length}}")
print("-" * (max_name_length + max_address_length + 4))
