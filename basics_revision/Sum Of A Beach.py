received_string = input()

received_string = received_string.lower()

total_count = 0

#print(received_string)

total_count += received_string.count('sand')

total_count += received_string.count('water')

total_count += received_string.count('fish')

total_count += received_string.count('sun')

print(total_count)