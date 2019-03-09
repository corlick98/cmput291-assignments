
# Find the AVG of each column for each of reviewer
# Display the results on a bar chart
# A single grouped bar chart is shown with the reviewer as the x-axis label
def question6(connection):
    # Query and format a table showing the reviewer along with their AVG scores
    r_df = pd.read_sql_query("select reviewer, AVG(originality), AVG(importance), \
    AVG(soundness), AVG(overall) from reviews group by reviewer;",connection)

    # Chart formated table with data being all columns but the reviewer
    r_df2 = pd.DataFrame(r_df.iloc[:,1:], columns=r_df.columns[1:])
    r_df2.plot.bar().set_xticklabels(r_df.iloc[:,0]) # Label x-axis using reviewer
    plt.plot()
    plt.show()

    return
