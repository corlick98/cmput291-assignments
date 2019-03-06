def question5(connection):
    df = pd.read_sql_query("select area, count(*) as 'count' from papers group by area order by count(*) desc;", connection)
    df.iloc[0:5,:]
    plot=df.plot.pie(labels=df.area,y="count")
    plt.plot()
    plt.show()
    return
