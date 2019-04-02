curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' \
-d 'fields name, developed, description, logo; limit 50; \
where developed != null & logo != null & description != null;' \
'https://api-v3.igdb.com/companies/' | jq '.[]'
