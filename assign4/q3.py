
def f3(connection,q3count):
    invalid = True			# flag for checking the inputs
    q3count += 1                    #forgot to count++
    while invalid:
        try:
            start = input("\nEnter start Year (YYYY):")		# start year in range
            end = input("\nEnter end Year (YYYY):")		# end year in range
            crime = input("\nEnter crime type:")		# Crime type
            N = int(input("\nEnter number of neighborhoods:"))		#number of neighbourhoods
            invalid = False					# change flag
        except ValueError:
            print("Please Enter valid information")
            continue
	
	# This query groups by Neighbourhood name and takes the tuples which have 
	# specific crime type into account in the given range. It also sorts the 
	# output table in descending order of the count of that count of that
	# crime type 
    df = pd.read_sql_query('''select crime_incidents.Neighbourhood_Name as Neighbourhood_Name, Count(*) as Count, Latitude, Longitude
                from crime_incidents, coordinates
                where crime_incidents.Year BETWEEN %s AND %s  
		        AND crime_incidents.Crime_Type = '%s' 
                AND crime_incidents.Neighbourhood_Name = coordinates.Neighbourhood_Name
                Group By  crime_incidents.Neighbourhood_Name
                order by Count(*) Desc;''' \
                %(start, end, crime),connection)
    pdf = df.nlargest(N, 'Count', keep='all')			# the dataframe is created with the N largest tuples and ties are counted
    #print(pdf)

    m = folium.Map(location=[53.5444, -113.232], zoom_start=12)             # declaring a folium. map variable with the co-ordinates
    counter = 0								# a counter to add each tuple to the map
    #print(pdf.iloc[counter,1])
    #print(type(pdf.iloc[counter,1]))
    while (counter < N):
        pop_up = str(pdf.iloc[counter,0]) + ' <br> ' + str(pdf.iloc[counter,1])		# declaring the pop_up the to be the name of the 
											# neighborhood and its crime count 
        
	folium.Circle(						# making the circle and giving its arguments
            location= [pdf.iloc[counter,2], pdf.iloc[counter,3]],		# location from the tuple
            popup = pop_up,							# popup is initialized to be the string pop_up
            radius= int(pdf.iloc[counter,1]) * 10,                      #masking problem
            color= 'crimson',						# circle color
            fill= True,
            fill_color='crimson'					# fill color
        ).add_to(m)							# increment counter
        counter = 1 + counter
        #print(pdf.iloc[counter,1])
    name = 'Q3-'+str(q3count)+'.html'					# name the file to whateever the count of q3count is
    m.save(name)							# save the map
    return q3count							# return to main
