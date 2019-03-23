
def f3(connection,q3count):
    invalid = True
    q3count += 1
    while invalid:
        try:
            start = input("\nEnter start Year (YYYY):")
            end = input("\nEnter end Year (YYYY):")
            crime = input("\nEnter crime type:")
            N = int(input("\nEnter number of neighborhoods:"))
            invalid = False
        except ValueError:
            print("Please Enter valid information")
            continue

    df = pd.read_sql_query('''select crime_incidents.Neighbourhood_Name as Neighbourhood_Name, Count(*) as Count, Latitude, Longitude
                from crime_incidents, coordinates
                where crime_incidents.Year BETWEEN %s AND %s  
		        AND crime_incidents.Crime_Type = '%s' 
                AND crime_incidents.Neighbourhood_Name = coordinates.Neighbourhood_Name
                Group By  crime_incidents.Neighbourhood_Name
                order by Count(*) Desc;''' \
                %(start, end, crime),connection)
    pdf = df.nlargest(N, 'Count', keep='all')
    #print(pdf)

    m = folium.Map(location=[53.5444, -113.232], zoom_start=12)
    counter = 0
    #print(pdf.iloc[counter,1])
    #print(type(pdf.iloc[counter,1]))
    while (counter < N):
        pop_up = str(pdf.iloc[counter,0]) + ' <br> ' + str(pdf.iloc[counter,1])
        folium.Circle(
            location= [pdf.iloc[counter,2], pdf.iloc[counter,3]],
            popup = pop_up,
            radius= int(pdf.iloc[counter,1]) * 10,
            color= 'crimson',
            fill= True,
            fill_color='crimson'
        ).add_to(m)
        counter = 1 + counter
        #print(pdf.iloc[counter,1])
    name = 'Q3-'+str(q3count)+'.html'
    m.save(name)
    return q3count
