def question5(connection):
    df = pd.read_sql_query("select area, count(*) as 'count' from papers group by area order by count(*) desc;", connection)
    pdf = df.nlargest(5, 'count',keep='all')
    plot=pdf.plot.pie(labels=pdf.area,y="count")
    plt.plot()
    plt.show()
    return
