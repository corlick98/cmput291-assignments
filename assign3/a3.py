import sqlite3
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
	# This is the primary control area to the questions
	# connect to the database
	dbname = input("Enter database name: ")
	connection = sqlite3.connect(dbname)

	print('Welcome to the Paper Review Database')
	
	exit_program = False
	# loop till user says to stop
	while exit_program == False:
		printoptions()
		try: #test if the user enters an integer
			user_input = int(input('Select the option number you wish to see: '))
		except ValueError:
			print()
			print('Please enter a valid selection')
			print()
			time.sleep(0.5)
			continue
		# tests if the user enters a valid choice
		if user_input not in range(1,8):
			print()
			print('Please enter a valid selection')
			print()
			time.sleep(0.5)
			continue
		# call the corresponding function for each question/task
		if user_input == 1:
			question1(connection)
		elif user_input == 2:
			question2(connection)
		elif user_input == 3:
			question3(connection)
		elif user_input == 4:
			question4(connection)
		elif user_input == 5:
			question5(connection)
		elif user_input == 6:
			question6(connection)
		elif user_input == 7:
			exit_program = True

	return

# Show all papers and allow one to be selected. Once a paper is selected, 
# show the email of all reviewers that have reviewed the paper.
def question1(connection):
    # get Id, title and author for all papers
    p_df = pd.read_sql_query("select Id, title, author from papers;",connection)
    notselected = True
    start = 0
    end = min(5,len(p_df))
    while notselected:
        print(p_df[start:end]) # show 5 papers at most
        invalid=True
        while invalid:
            try:
                print("Press N to go to next page. Press P to go to previous")
                paperid = input("select a paper ID: ")
                # if N show next page
                if paperid == "N":
                    if start+5<len(p_df):
                        start+=5
                    if end+5<len(p_df):
                        end+=5
                    else:
                        end = len(p_df)
                    break
                # if P show previous page
                elif paperid == "P":
                    if end-5>0:
                        end-=5
                    if start-5>0:
                        start-=5
                    else:
                        start=0
                    if end-start<5:
                        end=start+5
                    break
                else:
                    paperid = int(paperid)
            # check if they entered a integer
            except ValueError:
                print("Please enter a valid paper ID")
                continue
            # check if they entered a valid integer
            if (paperid-1) in p_df["Id"]:
                invalid = False
                notselected = False
            else:
                print("Please enter a valid paper ID")
    # select all reviewers who have reviewed that paper
    c = connection.cursor()
    c.execute('select reviewer from reviews where paper=?;',(paperid,))
    revs = c.fetchall()
    # print reviewers who reviewed the paper
    if revs == []:
        print("Nobody reviewed paper "+str(paperid))
    else:
        print("The reviewers who have reviewed paper "+str(paperid)+" are:")
        for reviewer in revs:
            print(reviewer[0])
    print()
    return

# Show all papers and allow one to be selected. Once a papers is selected, 
# show all potential reviewers for that paper. 
# Potential reviewers shown must have the same area of expertise as the paper. 
# If reviewer has already reviewed the paper, they should not be able to review it again 
# (either don’t show them as a potential reviewer or 
# give proper error once they try to input a review)
def question2(connection):
    # get Id, title and author for all papers
    p_df = pd.read_sql_query("select Id, title, author, area from papers;",connection)
    notselected = True
    start = 0
    end = min(5,len(p_df))
    while notselected:
        print(p_df[start:end]) # show 5 papers at most
        invalid=True
        while invalid:
            try:
                print("Press N to go to next page. Press P to go to previous")
                paperid = input("select a paper ID: ")
                # if N show next page
                if paperid == "N":
                    if start+5<len(p_df):
                        start+=5
                    if end+5<len(p_df):
                        end+=5
                    else:
                        end = len(p_df)
                    break
                # if P show previous page
                elif paperid == "P":
                    if end-5>0:
                        end-=5
                    if start-5>0:
                        start-=5
                    else:
                        start=0
                    if end-start<5:
                        end=start+5
                    break
                else:
                    paperid = int(paperid)
            # check if they entered an integer
            except ValueError:
                print("Please enter a valid paper ID")
                continue
            # check if they entered a valid paper Id
            if (paperid-1) in p_df["Id"]:
                invalid = False
                notselected = False
            else:
                print("Please enter a valid paper ID")
    # select reviewers who have expertise in the area of the paper
    # and haven't reviewed it yet
    c = connection.cursor()
    c.execute('''select e.reviewer 
                from expertise e
                where e.area = :parea
                and e.reviewer != :pauthor
                and not exists( select *
                                from reviews r
                                where r.reviewer = e.reviewer
                                and r.paper = :pid)''',{"parea":p_df.iloc[paperid-1,3],"pid":paperid,"pauthor":p_df.iloc[paperid-1,2]})
    # print potential reviewers
    rows = c.fetchall()
    if rows == []:
        print("Nobody can review paper "+str(paperid))
        print()
        return
    else:
        i = 0
        print("The reviewers who can review paper "+str(paperid)+" are:")
        print("Id  Email")
        for reviewer in rows:
            print(i, reviewer[0])
            i+=1
    print()
    # Enter a review for the paper
    invalid=True
    while invalid:
        try:
            reviewid = int(input("select a reviewer ID: "))
        # check if they entered an integer
        except ValueError:
            print("Please enter a valid reviewer ID")
            continue
        # check if they entered a valid reviewid 
        if (reviewid) in range(0,i):
            invalid = False
        else:
            print("Please enter a valid reviewer ID")
    # get the marks for the paper
    values = [0,0,0,0]
    values[0] = input("Please enter "+rows[reviewid][0]+"'s originality mark for paper "+str(paperid)+": ")
    values[1] = input("Please enter "+rows[reviewid][0]+"'s importance mark for paper "+str(paperid)+": ")
    values[2] = input("Please enter "+rows[reviewid][0]+"'s soundness mark for paper "+str(paperid)+": ")
    values[3] = input("Please enter "+rows[reviewid][0]+"'s overall mark for paper "+str(paperid)+": ")
    # insert the marks into the database for that review
    c = connection.cursor()
    c.execute('''insert into reviews values
                (:pid, :rname, :orig, :impor, :sound, :overall)
                ''',{"pid":paperid, "rname":rows[reviewid][0], "orig":int(values[0]),"impor":int(values[1]),"sound":int(values[2]),"overall":int(values[3])})
    connection.commit()
    
    return

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

# Create a pie chart of the top 5 most popular areas, popularity comes from the number of papers under the area. 
# If there are less than 5 areas, show pie chart of however many areas that exist.
def question5(connection):
    df = pd.read_sql_query("select area, count(*) as 'count' from papers group by area order by count(*) desc;", connection)
    pdf = df.nlargest(5, 'count',keep='all')
    plot=pdf.plot.pie(labels=pdf.area,y="count")
    plt.plot()
    plt.show()
    return

# Find the AVG of each column for each of reviewer
# Display the results on a bar chart
# A single grouped bar chart is shown with the reviewer as the x-axis label
def question6(connection):
    # Query and format a table showing the reviewer along with their AVG scores
    r_df = pd.read_sql_query("select reviewer, AVG(originality), AVG(importance), \
    AVG(soundness), AVG(overall) from reviews group by reviewer;",connection)

    # Chart formated table with data being all columns but the reviewer
    r_df2 = pd.DataFrame(r_df.iloc[:,1:], columns=r_df.columns[1:])
    r_df2.plot.bar().set_xticklabels(r_df.iloc[:,0]) # Label x-axis using reviewer
    plt.plot()
    plt.show()

    return

def printoptions():
    print("1. Show a paper and its reviewer")
    print("2. Show a paper and its potential reviewers can enter a review")
    print("3. Find all reviewers who have reviewed a number of papers in a range")
    print("4. How many sessions does each author participate in")
    print("5. Pie chart of top 5 most popular areas")
    print("6. Bar chart of each reviewers average review scores")
    print("7. Exit program")
    return
main()