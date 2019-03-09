
# Show in how many sessions do authors participate in?  You must Implement two options: 
# (1) a bar plot of all individual authors and how many sessions they participate in
# (2) just providing a number for a selected individual
def question4(connection):
    df = pd.read_sql_query("select author,count(csession) as count from papers where decision = 'A' AND author is not NULL group by author;", connection)
    valid_input = False
    
    while valid_input == False:
        try:
            usr_input = int(input("\nChoose your option.\n1. bar plot of all individual authors and how many sessions they participate in \n2. providing a number for a selected individual\n"))
        except ValueError:
            print("\nPlease enter a valid selection\n")
            time.sleep(0.5)
            continue
        
        if usr_input not in range(1,3):
            print("\nPlease enter a valid selection\n")
            time.sleep(1)
            continue

        if usr_input == 1:
            plot = df.plot.bar(x="author")
            plt.plot()
            plt.show()
            valid_input =  True
            
        elif usr_input == 2:
            x=df["author"]
            print(x)
            valid_input = True
            valid_name = False
            while valid_name == False:
                print()
                author_name = (input("\nwrite the email of the author: "))
                if (df["author"].isin([author_name]).any()):
                    print(df[df.author == author_name])
                    valid_name = True
                    print()

        
                          


   
    return
