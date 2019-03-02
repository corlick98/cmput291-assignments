def question3(connection):
   
    invalid = True
    while invalid:
        try:
            num_range = input("Enter a number range (x,y): ").split(",")
            for i in num_range:
                i = int(i)
            invalid = False
        except ValueError:
            print("Please enter a valid range")
            continue
    
    c = connection.cursor()
    c.execute('select reviewer from reviews group by reviewer \
    having count(*) between :num1 and :num2;',\
    {"num1":int(num_range[0]), "num2":int(num_range[1])})

    revs = c.fetchall()
    for each in revs:
        print(each[0])

    return
