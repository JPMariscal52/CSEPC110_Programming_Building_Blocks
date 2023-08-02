#-courses_file = open("files.txt") 
#-This instrution let open the file until you indicate "closed", to avoit this you can use "with"
highest = 0
lowest = 101
lowest_drop = 100

with open("files.txt") as courses_files:
    
    diference = [0]
    
    for line in courses_files:
        
        line = line.strip()
        parts = line.split(",")

        name = parts[0]
        grade = float(parts[1])

        bonus = grade + 3

        first = diference[0]
        result = first - grade
        print(f"{result:.2f}")
         

        diference.pop(0)
        diference.append(grade)

        print(f"{name} - Grade: {grade}, after bonus {bonus}")



        if grade > highest:
            highest = grade

        if grade < lowest:
            lowest = grade


    print(lowest)
    print(highest)

