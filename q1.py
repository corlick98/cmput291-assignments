def question1(connection):
    p_df = pd.read_sql_query("select * from papers;",connection)
    print(p_df)
    invalid=True
    while invalid:
        try:
            paperid = int(input("select a paper ID: "))
        except ValueError:
            print("Please enter a valid paper ID")
            continue
        if (paperid-1) in p_df["Id"]:
            invalid = False
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
