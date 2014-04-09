information-retrieval
=====================
3 Main categories have been indexed from yelp: food, shopping and arts. 

There are 12k crawled entries spanning these 3 categories. 
There might be duplicates due to certain businesses falling into many categories. 
e.g. Starbucks is located in 'shopping' and 'food', hence twice.

Based on the retrieved json, the following fields have been indexed:

{{ object.is_claimed }}
{{ object.rating }}
{{ object.mobile_url }}
{{ object.rating_image_url }}
{{ object.review_count }}
{{ object.name }}
{{ object.rating_image_url_small }}
{{ object.url }}
{{ object.is_closed }}
{{ object.phone }}
{{ object.snippet_text }}
{{ object.image_url }}
{{ object.categories }}
{{ object.display_phone }}
{{ object.rating_image_url_large }}
{{ object.identifier }}
{{ object.snippet_image_url }}
{{ object.location }}
{{ object.deals }}

To test it out:
1) in console, type "java -jar start.jar" where solr's "start.jar" is located
2) go to localhost:8000/search/
3) search