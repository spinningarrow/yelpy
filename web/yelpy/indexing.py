from yelpapi import YelpAPI
import pysolr
import json
import collections
import dictlitestore

yelp_api =YelpAPI('a5oBT4RnnHpt6rtHQWsGYg','61UpHpxNDVJfpACumIIJNIR2nJ8','-PlfjeTyjnMSGP67pQbopdxJ-lXE70Bn','ewGlo-jkCt0LpNYphzr2SxaEtCY')
neighborhoods = ['Ang Mo Kio','Arab Street','Bedok North', 'Bishan', 'Boat Quay', 'Boon Keng', 'Boon Lay','Bras Brasah','Bugis','Bukit Timah','Changi','Chinatown','Choa Chu Kang','City Hall','Clarke Quay','Clementi','Dhoby Ghaut','Eunos','Farrer Park','Geylang','Harbourfront','Holland Village','Hougang','Kallang','Katong','Lavender','Macpherson','Marine Parade','Newton','Novena','Orchard','Pasir Ris','Raffles Place','Serangoon','Somerset','Tampines','Thomson','Toa Payoh','Woodlands','Yio Chu Kang','Yishun']
#neighborhoods = ['Lavender','Macpherson','Marine Parade','Newton','Novena','Orchard','Pasir Ris','Raffles Place','Serangoon','Somerset','Tampines','Thomson','Toa Payoh','Woodlands','Yio Chu Kang','Yishun']

#solr = pysolr.Solr('http://localhost:8983/solr/', timeout=10)


row = 0
print len(neighborhoods)
#resultsDict = []
with dictlitestore.DictLiteStore('arts.db', 'shopslistings') as bucket:
    #results = yelp_api.search_query(location='singapore', category_filter='shopping')
    #print results['businesses'][0]
    #print len(results['businesses'])
    #bucket.store(results['businesses'][0])

    for location in neighborhoods:
        search_results = yelp_api.search_query(location=location, category_filter='arts', cc='SG')
        #print type(search_results)
        #print json.dumps(search_results['businesses'])
        print location
        print "-------------------------------------------------------"

        totalResults = search_results['total']
        for x in range (0, min(50, totalResults/20)):
            offsetValue = (str)(x*20)
            #print("Query", x)

            results = yelp_api.search_query(location=location, category_filter='arts', offset=offsetValue, cc='SG')
            row=0
            for r in results:
                results['businesses'][row]['identifier'] = results['businesses'][row]['id']
                del results['businesses'][row]['id']
                bucket.store(results['businesses'][row])
                print location, " - " , results['businesses'][row]['name']
                row+=1




