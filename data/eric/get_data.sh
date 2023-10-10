#!/bin/bash
# sociology of education records
curl -X GET "https://api.ies.ed.gov/eric/?search=issn%3A%22ISSN-0038-0407%22&format=xml&rows=2000" -H "accept: */*" > se.xml
# american journal of education records
curl -X GET "https://api.ies.ed.gov/eric/?search=issn%3A%22ISSN-0195-6744%22&format=xml&rows=2000" -H "accept: */*" > aje.xml
# american educational research journal records
curl -X GET "https://api.ies.ed.gov/eric/?search=issn%3A%22ISSN-0002-8312%22&format=xml&rows=2000" -H "accept: */*" > aerj.xml
# british journal of sociology of education records
curl -X GET "https://api.ies.ed.gov/eric/?search=issn%3A%22ISSN-0142-5692%22&format=xml&rows=2000" -H "accept: */*" > bjse.xml
# international studies in sociology of education
curl -X GET "https://api.ies.ed.gov/eric/?search=issn%3A%22ISSN-0962-0214%22&format=xml&rows=2000" -H "accept: */*" > isse.xml
