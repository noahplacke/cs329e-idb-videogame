rm -f companies.json
rm -f games.json
rm -f genres.json

printf "{\n\"Companies\": [\n" > companies.json

curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' \
-d 'fields name, developed, description, logo; limit 50; \
where developed != null & logo != null & description != null;' \
'https://api-v3.igdb.com/companies/' | jq '.[]' >> companies.json

curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' \
-d 'fields name, developed, description, logo; offset 50; limit 50; \
where developed != null & logo != null & description != null;' \
'https://api-v3.igdb.com/companies/' | jq '.[]' >> companies.json

printf "]\n}" >> companies.json


printf "{\n\"Games\": [\n" > games.json

curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' \
-d 'fields name, rating, genres, involved_companies, url, summary; limit 50; \
where developed != null & logo != null & description != null;' \
'https://api-v3.igdb.com/games/' | jq '.[]' >> games.json

curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' \
-d 'fields name, rating, genres, involved_companies, url, summary; offset 50; limit 50; \
where rating != null & genres != null & summary != null & involved_companies != null;' \
'https://api-v3.igdb.com/games/' | jq '.[]' >> games.json

printf "]\n}" >> games.json

printf "{\n\"Genres\": " > genres.json

curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' \
-d 'fields name, url; limit 50;' \
'https://api-v3.igdb.com/genres/' >> genres.json

printf "\n}" >> genres.json

