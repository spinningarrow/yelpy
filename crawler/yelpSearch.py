from yelpapi import YelpAPI
import json

yelp_api = YelpAPI('a5oBT4RnnHpt6rtHQWsGYg', '61UpHpxNDVJfpACumIIJNIR2nJ8', '-PlfjeTyjnMSGP67pQbopdxJ-lXE70Bn', 'ewGlo-jkCt0LpNYphzr2SxaEtCY')
search_results = yelp_api.search_query(location='singapore')

print json.dumps(search_results)
