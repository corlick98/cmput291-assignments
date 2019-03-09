# Given range from user
# Find all reviewers whose number of reviewers are within user range
# Range includes bounds 
def question3(connection):
   # Create loop until valid range is given
    invalid = True
    while invalid:
        try:
            num_range = input("Enter a number range \"x,y\": ").split(",")  # Separate range ints
            for i in num_range:  # Check for valid int inputs
                i = int(i)
            invalid = False
        except ValueError:
            print("Please enter a valid range")  # Inform of invalid input
            continue
    
    # Query to find desired reviewers having count(*) in desired range
    c = connection.cursor()
    c.execute('select reviewer from reviews group by reviewer \
    having count(*) between :num1 and :num2;',\
    {"num1":int(num_range[0]), "num2":int(num_range[1])})

    # Print out each reviewer on separate line from query table
    revs = c.fetchall()
    for each in revs:
        print(each[0])

    return
