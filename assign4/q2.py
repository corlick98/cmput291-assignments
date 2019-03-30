
# Given an integer N, show (in a map) the N-most populous 
# and N-least populous neighborhoods with their population count
def f2(connection, q2count):
    # Add to count number
    q2count += 1
    
    Total_pop = 'CANADIAN_CITIZEN + NON_CANADIAN_CITIZEN + NO_RESPONSE'

    # Create query to show neighbourhoods and its coordinates and sort by population
    # from the combination of the three population columns
    p_df = pd.read_sql_query('''select p.Neighbourhood_Name, Latitude, Longitude, Sum(%s)
                                from population p, coordinates c
                                where p.Neighbourhood_Name = c.Neighbourhood_Name
                                and (%s) > 0
                                group by p.Neighbourhood_Name
                                order by %s DESC;'''
                                % (Total_pop, Total_pop, Total_pop),
                                connection)

    # Enter number of locations 
    num_local = int(input("Enter number of locations: "))

    # Generate centralized map of Edmonton
    q2map = folium.Map(location=[53.5444, -113.4909], zoom_start=12)

    # Create max/min for relative sizes
    maxsize = p_df.iloc[0,3]
    minsize = p_df.iloc[-1,3]

    # For loop for N locations top and bottom
    for N in range(num_local):
        # Popup labels and format
        top_pop = str(p_df.iloc[N,0]) + ' <br> ' + str(p_df.iloc[N,3])
        bot_pop = str(p_df.iloc[-(N+1),0]) + ' <br> ' + str(p_df.iloc[-(N+1),3])
        # Create circle for top N
        folium.Circle(
            location = [p_df.iloc[N,1], p_df.iloc[N,2]],
            popup = top_pop,
            radius = (1000 * p_df.iloc[N,3]) / maxsize,
            color = 'crimson',
            fill = True,
            fill_color = 'crimson'
        ).add_to(q2map)
        # Create circle for bottom N
        folium.Circle(
            location = [p_df.iloc[-(N+1),1], p_df.iloc[-(N+1),2]],
            popup = bot_pop,
            radius = (100 * p_df.iloc[-(N+1),3]) / minsize,
            color = 'crimson',
            fill = True,
            fill_color = 'crimson'
        ).add_to(q2map)
    
    # Save as new map 
    name = 'Q2-'+str(q2count)+'.html'
    q2map.save(name)

    # Return count of maps
    return q2count
