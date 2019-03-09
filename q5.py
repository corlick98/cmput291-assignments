
# Create a pie chart of the top 5 most popular areas, popularity comes from the number of papers under the area. 
# If there are less than 5 areas, show pie chart of however many areas that exist.
def question5(connection):
    df = pd.read_sql_query("select area, count(*) as 'count' from papers group by area order by count(*) desc;", connection)
    pdf = df.nlargest(5, 'count',keep='all')
    plot=pdf.plot.pie(labels=pdf.area,y="count")
    plt.plot()
    plt.show()
    return
