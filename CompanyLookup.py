import json

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn


def find_existing_companies():
  companies = load_json('companies.json')
  company_ids = []

  for company in companies['Companies']:
    company_ids.append(company['id'])

  return company_ids


def find_missing_companies():
  games = load_json('games.json')
  existing_ids = find_existing_companies()
  missing_ids = []

  for game in games['Games']:
    companies = game['involved_companies']

    for company_id in companies:
      if (company_id not in existing_ids) and (company_id not in missing_ids):
        missing_ids.append(company_id)

  missing_ids_dedup = list(set(missing_ids))
  return missing_ids_dedup

def split_list(l):
  idx = 0
  groups = []
  while idx < len(l):
    group = []
    for i in range(10):
      if idx >= len(l):
        break
      group.append(l[idx])
      idx += 1
    groups.append(group)
  return groups

def format_groups(g):
  print("where", end = " ")
  for group in g:
    print("id = ", tuple(group), "|", end=" ")

def main():
  grouped_cos = split_list(find_missing_companies())
  print("EXISTING:", find_existing_companies())
  print("MISSING:", grouped_cos)
  format_groups(grouped_cos)

main() 
