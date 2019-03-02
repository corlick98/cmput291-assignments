
def question4(connection):
    df = pd.read_sql_query("select author,count(csession) as count from papers group by author;", connection)


    usr_input = int(input("\nChoose your option.\n1. bar plot of all individual authors and how many sessions they participate in \n2. providing a number for a selected individual\n"))

    while usr_input not in range(1,3):
        print('\nPlease enter a valid selection\n')
        time.sleep(1)
        continue

    if usr_input == 1:
        plot = df.plot.bar(x="author")
        plt.plot()
        plt.show()

    elif usr_input == 2:
        print(df.iloc[ : , 0])
        author_name = (input("\nwrite the email of the author: "))
        print()
        print(df[df.author== author_name])
        print()
                       
        
                          


   
    return
