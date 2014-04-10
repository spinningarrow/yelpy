from yelpapi import YelpAPI
yelp_api =YelpAPI('a5oBT4RnnHpt6rtHQWsGYg','61UpHpxNDVJfpACumIIJNIR2nJ8','-PlfjeTyjnMSGP67pQbopdxJ-lXE70Bn','ewGlo-jkCt0LpNYphzr2SxaEtCY')
neighborhoods = ['Alexandra', 'Ang Mo Kio', 'Ann Siang Hill', 'Arab Street', 'Bayfront', 'Bedok North', 'Bedok Reservoir', 'Bedok South', 'Bencoolen', 'Bishan', 'Boat Quay', 'Boon Keng', 'Boon Lay','Bras Brasah','Buangkok','Bugis','Bukit Batok','Bukit Panjang','Bukit Timah','Changi','Chinatown','Choa Chu Kang','City Hall','Clarke Quay','Clementi','Dempsey Hill','Dhoby Ghaut','Dover','Duxton Hill','Eunos','Farrer Park','Geylang','Ghim Moh','Harbourfront','Holland Hill','Holland Village','Hougang','Joo Chiat','Jurong','Jurong Island','Kallang','Katong','Kembangan','Kent Ridge','Keppel','Labrador Park','Lavender','Lim Chu Kang','Little India','Macpherson','Mandai','Marine Parade','Mount Sophia','Mountbatten','Newton','Novena','Orchard','Outram','Pasir Panjang','Pasir Ris','Paya Lebar','Potong Pasir','Pulau Ubin','Punggol','Queenstown','Raffles Place','Redhill','River Valley','Robertson Quay','Seletar','Sembawang','Sengkang','Sentosa','SerangoonSerangoon Gardens','Siglap','Simei','Sixth Avenue','Somerset','Tampines','Tanglin','Tanglin Halt','Tanjong Pagar','Tanjong Rhu','Telok Blangah','Telok Kurau','Thomson','Tiong Bahru','Toa Payoh','Tuas','Ubi','Ulu Pandan','Upper Bukit Timah','Wessex Estate','West Coast','Woodlands','Yio Chu Kang','Yishun','one-north']

resultsDict = [] 
for location in neighborhoods:
	search_results = yelp_api.search_query(location=location, category_filter='food')
	totalResults = search_results['total']	
	for x in range (0, min(50, totalResults/20)):
		offsetValue = (str)(x*20)
		print "Query", x
		results = yelp_api.search_query(location=location, category_filter='food', offset=offsetValue)
		resultsDict.append(results)
