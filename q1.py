
# Show all papers and allow one to be selected. Once a paper is selected, 
# show the email of all reviewers that have reviewed the paper.
def question1(connection):
    # get Id, title and author for all papers
    p_df = pd.read_sql_query("select Id, title, author from papers;",connection)
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
