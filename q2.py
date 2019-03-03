
# Show all papers* and allow one to be selected. Once a papers is selected, 
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
    end = 5
    while notselected:
        print(p_df[start:end]) # show 5 papers at most
        invalid=True
        while invalid:
            try:
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
                and not exists( select *
                                from reviews r
                                where r.reviewer = e.reviewer
                                and r.paper = :pid)''',{"parea":p_df.iloc[paperid-1,3],"pid":paperid})
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
    values = input("Please enter "+rows[reviewid][0]+"'s review marks for paper "+str(paperid)+": ").split(",")
    # insert the marks into the database for that review
    c = connection.cursor()
    c.execute('''insert into reviews values
                (:pid, :rname, :orig, :impor, :sound, :overall)
                ''',{"pid":paperid, "rname":rows[reviewid][0], "orig":int(values[0]),"impor":int(values[1]),"sound":int(values[2]),"overall":int(values[3])})
    
    return
