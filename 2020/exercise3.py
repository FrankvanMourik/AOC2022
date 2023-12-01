correct_passwords = 0
with open('exercise2a.txt') as my_file:
    for line in my_file:
        character_count=0
        parts = line.split()
        count_parts = parts[0].split('-')
        character = parts[1][0]
        password = parts[2]
        for i in password:
            if i == character:
                character_count += 1
        if int(count_parts[0]) <= character_count <= int(count_parts[1]):
            correct_passwords += 1
print(correct_passwords)