

print("Day 1")
the_file = open("um-deliveries-day-1.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[-2]
    amount = words[-1]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("Day 2")
the_file = open("um-deliveries-day-2.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[-2]
    amount = words[-1]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("Day 3")
the_file = open("um-deliveries-day-3.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[-2]
    amount = words[-1]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()
