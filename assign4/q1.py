

def f1(conn,q1count):
    q1count = q1count + 1
    start = input("Enter start year (YYYY): ")
    end = input("Enter end year (YYYY): ")
    ctype = input("Enter crime type: ")
    df = pd.read_sql_query('''select Month, sum(Incidents_Count) as count
                            from crime_incidents 
                            where crime_type = ?
                            and year between ? and ?
                            group by month
                            union 
                            select Month,0
                            from crime_incidents
                            where Month!='Month'
                            group by Month
                            except 
                            select Month, 0
                            from crime_incidents 
                            where crime_type = ?
                            and year between ? and ?
                            group by month;''',conn,params=(ctype, start,end,ctype, start,end))
    plot = df.plot.bar(x='Month')
    plt.plot()
    name = "Q1-"+str(q1count)+".png"
    plt.savefig(name)
    return q1count