def question2(connection):
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
    c.execute('''select e.reviewer 
                from expertise e
                where e.area = :parea
                and not exists( select *
                from reviews r
                where r.reviewer = e.reviewer
                and r.paper = :pid)''',{"parea":p_df.iloc[paperid-1,3],"pid":paperid})


    rows = c.fetchall()
    if rows == []:
        print("Nobody can review paper "+str(paperid))
        print()
        return
    else:
        i = 0
        print("The reviewers who can review paper "+str(paperid)+" are:")
        for reviewer in rows:
            print(i, reviewer[0])
            i+=1
    print()
    invalid=True
    while invalid:
        try:
            reviewid = int(input("select a reviewer ID: "))
        except ValueError:
            print("Please enter a valid reviewer ID")
            continue
        if (paperid-1) in range(0,i+1):
            invalid = False
        else:
            print("Please enter a valid reviewer ID")

    values = input("Please enter "+rows[reviewid][0]+"'s review marks for paper "+str(paperid)+": ").split(",")
    
    c = connection.cursor()
    c.execute('''insert into reviews values
                (:pid, :rname, :orig, :impor, :sound, :overall)
                ''',{"pid":paperid, "rname":rows[reviewid][0], "orig":int(values[0]),"impor":int(values[1]),"sound":int(values[2]),"overall":int(values[3])})



    return
