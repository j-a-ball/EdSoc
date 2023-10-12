#!/bin/bash
# sociology of education records
curl -X GET "https://api.ies.ed.gov/eric/?search=source%3A%22sociology%20of%20education%22%20AND%20NOT%20source%3A%22international%22%20AND%20NOT%20source%3A%22british%22%20AND%20NOT%20source%3A%22Leisure%22&format=json&rows=2000" -H "accept: */*" > se.json
# american journal of education records
curl -X GET "https://api.ies.ed.gov/eric/?search=source%3A%22american%20journal%20of%20education%22%20%20AND%20NOT%20source%3A%22health%22%20AND%20NOT%20source%3A%22business%22%20AND%20NOT%20source%3A%22pharmaceutical%22%20AND%20NOT%20source%3A%22distance%22%20AND%20NOT%20source%3A%22sexuality%22%20AND%20NOT%20source%3A%22engineering%22&format=json&rows=2000" -H "accept: */*" > aje.json
# american educational research journal records
curl -X GET "https://api.ies.ed.gov/eric/?search=source%3A%22american%20educational%20research%20journal%22&format=json&rows=2000" -H "accept: */*" > aerj.json
# british journal of sociology of education records
curl -X GET "https://api.ies.ed.gov/eric/?search=source%3A%22british%20journal%20of%20sociology%20of%20education%22&format=json&rows=2000" -H "accept: */*" > bjse.json
# international studies in sociology of education
curl -X GET "https://api.ies.ed.gov/eric/?search=source%3A%22international%20studies%20in%20sociology%20of%20education%22&format=json&rows=2000" -H "accept: */*" > isse.json
# american sociological review
curl -X GET "https://api.ies.ed.gov/eric/?search=source%3A%22American%20Sociological%20Review%22&format=json&rows=2000" -H "accept: */*" > asr.json
# american journal of sociology
curl -X GET "https://api.ies.ed.gov/eric/?search=source%3A%22american%20journal%20of%20sociology%22%20AND%20NOT%20source%3A%22economics%22&format=json&rows=2000" -H "accept: */*" > ajs.json
