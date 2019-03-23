
def f4(conn,q4count):
    q4count += 1
    start = input("Enter start year (YYYY): ")
    end = input("Enter end year (YYYY): ")
    num = input("Enter number of neighborhoods: ")
    df = pd.read_sql_query('''select crime_incidents.Neighbourhood_Name, sum(Incidents_Count) as incedents, (CANADIAN_CITIZEN + NON_CANADIAN_CITIZEN + NO_RESPONSE) as pop
                            from population, crime_incidents
                            where crime_incidents.Neighbourhood_Name = population.Neighbourhood_Name
                            and CANADIAN_CITIZEN + NON_CANADIAN_CITIZEN + NO_RESPONSE !=0
                            and crime_incidents.Year between ? and ?
                            group by crime_incidents.Neighbourhood_Name''',conn, params=(start,end))
    ndf = pd.DataFrame(columns=["Neighborhood", "ratio"], index = range(0,len(df)), dtype = float)
    for i in range(0,len(df)):
        ndf.iloc[i, 0] = df.iloc[i,0]
        ndf.iloc[i, 1] =  float(df.iloc[i, 1]/ df.iloc[i, 2])
    pdf = ndf.nlargest(int(num), 'ratio', keep='all')
    maxval = pdf.iloc[0,1]
    q4map = folium.Map(location=[53.5444, -113.4909], zoom_start=11)
    for i in range(int(num)):
        stri = str(pdf.iloc[i,0])
        locs = pd.read_sql_query("select * from coordinates where Neighbourhood_Name = '%s';"%(stri),conn)
        print(locs.iloc[0,1])
        top_pop = 'test'
        folium.Circle(
            location = [locs.iloc[0,1], locs.iloc[0,2]],
            popup = top_pop,
            radius = (1000 * pdf.iloc[i,1]) / maxval,
            color = 'crimson',
            fill = True,
            fill_color = 'crimson'
        ).add_to(q4map)

    name = 'Q4-'+str(q4count)+'.html'
    q4map.save(name)

    return q4count

