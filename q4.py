
# Show in how many sessions do authors participate in?  You must Implement two options: 
# (1) a bar plot of all individual authors and how many sessions they participate in
# (2) just providing a number for a selected individual
def question4(connection):
    df = pd.read_sql_query("select author,count(csession) as count from papers group by author;", connection)
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
            print(df.iloc[ : , 0])
            author_name = (input("\nwrite the email of the author: "))
            print(df[df.author== author_name])
            valid_input = True           
        
                          


   
    return
