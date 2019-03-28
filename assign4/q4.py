
# Given a range of years and an integer N, 
# show (in a map) the Top-N neighborhoods with 
# the highest crimes to population ratio within the provided range. 
# Also, show the most frequent crime type in each of these neighborhoods.
def f4(conn,q4count):
    q4count += 1 # increment the number of times that q4 has ran
    # get user input
    start = input("Enter start year (YYYY): ")
    end = input("Enter end year (YYYY): ")
    num = input("Enter number of neighborhoods: ")
    # get the number of crimes and population for each neighborhood that has a population
    df = pd.read_sql_query('''select crime_incidents.Neighbourhood_Name, sum(Incidents_Count), (CANADIAN_CITIZEN + NON_CANADIAN_CITIZEN + NO_RESPONSE)
                            from population, crime_incidents
                            where crime_incidents.Neighbourhood_Name = population.Neighbourhood_Name
                            and CANADIAN_CITIZEN + NON_CANADIAN_CITIZEN + NO_RESPONSE !=0
                            and crime_incidents.Year between ? and ?
                            group by crime_incidents.Neighbourhood_Name''',conn, params=(start,end))
    # create a new dataframe for storing the ratios 
    ndf = pd.DataFrame(columns=["Neighborhood", "ratio"], index = range(0,len(df)), dtype = float)
    for i in range(0,len(df)):
        ndf.iloc[i, 0] = df.iloc[i,0]
        ndf.iloc[i, 1] =  float(df.iloc[i, 1]/ df.iloc[i, 2])
    pdf = ndf.nlargest(int(num), 'ratio', keep='all') # get the nlargest ratios 

    maxval = pdf.iloc[0,1] # get the largest crime to population ratio for scaling
    q4map = folium.Map(location=[53.5444, -113.4909], zoom_start=11)

    for i in range(int(num)):
        stri = str(pdf.iloc[i,0]) # neighborhood name
        locs = pd.read_sql_query("select * from coordinates where Neighbourhood_Name = '%s';"%(stri),conn) # coordinates of the neighborhood
        # get most common crime type (mostly remnant from when you wanted ratio of crimes commited)
        crimes = pd.read_sql_query('''select crime_type, sum(Incidents_Count) as s
                                    from crime_incidents
                                    where crime_incidents.Neighbourhood_Name = '%s'
                                    and year between ? and ?
                                    group by crime_type
                                    order by s DESC'''%(stri),conn, params=(start,end))
        # generate popup text
        top_pop = stri + ' <br> ' + crimes.iloc[0,0] #+ ' <br> ' + str(crimes.iloc[0,1]/crimes.sum().iloc[1])
        folium.Circle(
            location = [locs.iloc[0,1], locs.iloc[0,2]],
            popup = top_pop,
            radius = (1000 * pdf.iloc[i,1]) / maxval,
            color = 'crimson',
            fill = True,
            fill_color = 'crimson'
        ).add_to(q4map)
    # create the name to save the map as
    name = 'Q4-'+str(q4count)+'.html'
    q4map.save(name)
    # return q4count to allow main to update
    return q4count

