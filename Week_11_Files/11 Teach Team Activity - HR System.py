with open("hr_system.txt") as employees:
    for person in employees:
        
        person = person.strip()
        employees_list = person.split(" ")

        name = employees_list[0]
        id_number = employees_list[1]
        title = employees_list[2]
        salary = float(employees_list[3])

        print(f"{name} (ID: {id_number}), {title} - ${salary:.2f}")