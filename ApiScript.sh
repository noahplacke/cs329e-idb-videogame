rm -f companies.json

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

#curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' \
#-d 'fields name; limit 5; \
#where developed != null & logo != null & description != null;' \
#'https://api-v3.igdb.com/companies/' | jq '.[]'

#curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' \
#-d 'fields name; offset 4; limit 5; \
#where developed != null & logo != null & description != null;' \
#'https://api-v3.igdb.com/companies/' | jq '.[]'
