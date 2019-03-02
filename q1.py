def question1(connection):
    p_df = pd.read_sql_query("select * from papers;",connection)
    print(df)
    invalid=True
    while invalid:
        try:
            paperid = int(input("select a paper ID: "))
        except ValueError:
            print("Please enter a valid paper ID")
            continue
        if paperid in df["ID"]:
            invalid = False
        else:
            print("Please enter a valid paper ID")
    c = conection.cursor()
    c.execute('select reviewer from reviews where paper=?;',paperid)
    revs = fetchall()
    print(revs)
    


    return
