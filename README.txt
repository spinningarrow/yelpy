------------------------------------------------------------------------
GROUP ID: 32
------------------------------------------------------------------------

Bajaj Sahil 	(U1020595G)
Chia Yan An 	(U1020691K)
Kok Mun Kiat 	(U1020729J)
Sabharwal Shahbaaz Deep Singh (U1021230J)

------------------------------------------------------------------------
YouTube Video URL
------------------------------------------------------------------------

http://youtu.be/oveu0YvI1xA

------------------------------------------------------------------------
Instructions on how to reproduce results and run programs
------------------------------------------------------------------------

## Programming languages and technologies used:
1. Crawling: Python (yelpapi package)
2. Indexing and Ranking: Apache Solr
3. Querying: Python (Django), HTML, CSS (Bootstrap), JavaScript (jQuery)

## Demo
A working demo of this project is hosted on an Amazon EC2 instance.
The short URL* is http://tinyurl.com/irntu-group32.

## Installing locally
1. To run the project locally, clone it from the Git repository hosted
   on Bitbucket at
   https://bitbucket.org/spinningarrow/ntuirprojectgroup32.

2. This project uses SOLR to index data. The schema used is located at
   ./solr/schema.xml; this file must be copied to
   <solr_dir>/example/solr/collection1/conf/

3. Start SOLR by running the following command from the
   <solr_dir>/example/ dir:
	  java -jar start.jar

4. In the web directory, create a virtual environment using virtualenv:
	  virtualenv env

   Activate the environment by sourcing the activate script:
	  source env/bin/activate

   The above two steps are not mandatory, but they help keep things
   modularised.

5. Install the necessary python packages:
	pip install -r requirements.txt

6. Sync the database:
	python manage.py syncdb

7. Rebuild the database index (SOLR must be running):
	python manage.py rebuild_index

8. Finally, run the server:
	python manage.py runserver

## Using the Web UI
1. Log in to the website (creates a new user the first time) using
   Facebook credentials
2. Update preference details using the form on the Profile page
3. View personalised search results on the Search page
4. Filter personalised search results using the search box on the Search
   page

------------------------------------------------------------------------
* In case the short url doesn't work, the full url is:
http://ec2-54-186-213-97.us-west-2.compute.amazonaws.com:8000/