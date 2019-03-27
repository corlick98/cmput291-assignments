
# Given a range of years and crime type, show (in a bar plot) 
# the month-wise total count of the given crime type.
def f1(conn,q1count):
    q1count = q1count + 1 # increment the number of times that q1 has run
    # get the user input
    start = input("Enter start year (YYYY): ")
    end = input("Enter end year (YYYY): ")
    ctype = input("Enter crime type: ")
    # get a table where each month is with the number of crimes committed in that month
    # and if no crimes has a 0
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
    # create the name to save the graph as
    name = "Q1-"+str(q1count)+".png"
    plt.savefig(name)
    return q1count

