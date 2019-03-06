def question6(connection):
    
    
    r_df = pd.read_sql_query("select reviewer, AVG(originality), AVG(importance), \
    AVG(soundness), AVG(overall) from reviews group by reviewer;",connection)

    
    # print(r_df)
    r_df2 = pd.DataFrame(r_df.iloc[:,1:], columns=r_df.columns[1:])
    r_df2.plot.bar().set_xticklabels(r_df.iloc[:,0])
    plt.plot()
    plt.show()

    return
