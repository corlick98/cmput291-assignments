def question1(connection):
    p_df = pd.read_sql_query("select * from papers;",connection)
    notselected = True
    start = 0
    end = 5
    while notselected:
        print(p_df[start:end])
        invalid=True
        while invalid:
            try:
                paperid = input("select a paper ID: ")
                if paperid == "N":
                    if start+5<len(p_df):
                        start+=5
                    if end+5<len(p_df):
                        end+=5
                    else:
                        end = len(p_df)
                    break
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
            except ValueError:
                print("Please enter a valid paper ID")
                continue
            if (paperid-1) in p_df["Id"]:
                invalid = False
                notselected = False
            else:
                print("Please enter a valid paper ID")
    c = connection.cursor()
    c.execute('select reviewer from reviews where paper=?;',(paperid,))
    revs = c.fetchall()
    if revs == []:
        print("Nobody reviewed paper "+str(paperid))
    else:
        print("The reviewers who have reviewed paper "+str(paperid)+" are:")
        for reviewer in revs:
            print(reviewer[0])
    print()
    return
