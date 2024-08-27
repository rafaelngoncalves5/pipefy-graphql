import requests
import pandas as pd
import json

API_KEY = "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJQaXBlZnkiLCJpYXQiOjE3MjE2NTg0OTMsImp0aSI6IjMwMGE1ZjY0LTZlNTUtNGMyMS1iNDBkLWY0MjUwOWQ4MTRlNyIsInN1YiI6MzAxMDQwMjQ2LCJ1c2VyIjp7ImlkIjozMDEwNDAyNDYsImVtYWlsIjoiYnAuZm9uc2VjYThAZ21haWwuY29tIn19.f68A2-ln_SmSKaWBwBNVeolYsTPkoiNIbK79VBFeTZ618q665_bJ7gcTyR-rxeGZV9XEeOLPS02sAnfv2mOpYA"

url = "https://api.pipefy.com/graphql"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# ROTINAS

def get_all_organizations():
    query = """
    {
        organizations{
        id
        name
    }
    }
"""
    response = requests.post(url, json={'query': query}, headers=headers)
    data = response.json()
    return data

def get_organization_basics():
    query = """
    {
        organization(id:300780691) {
            id
            name
            planName
            createdAt
        }
    }
    """
    response = requests.post(url, json={'query': query}, headers=headers)
    data = response.json()
    return data

def get_organization_tables():
    query = """
        {
            organization(id:300780691) {
            id
            tables {
                edges {
                    node {
                        id
                        name
                        internal_id
                    }
                }
            }
        }
    }
    """
    response = requests.post(url, json={'query': query}, headers=headers)
    data = response.json()
    return data

def get_organization_pipes():
    query = """
        {
            organization(id:300780691) {
            id
            name
            pipes {
                id
                name
            }
        }
    }
    """
    response = requests.post(url, json={'query': query}, headers=headers)
    data = response.json()
    return data

def get_vendas_pipe_info():
    query = """
    {
        pipe(id: 303486089) {
            id
            name
            color
            users_count
            cards_count
            opened_cards_count
            emailAddress
        }
    }
    """
    response = requests.post(url, json={'query': query}, headers=headers)
    data = response.json()
    return data

def get_vendas_pipe_cards():
    query = """
    {
        pipe(id: 303486089) {
            id
            name
            color
            users_count
            cards_count
            opened_cards_count
            emailAddress
        }
    }
    """
    response = requests.post(url, json={'query': query}, headers=headers)
    data = response.json()
    return data

def get_all_tables():
    query = """
    {
  pipe(id: "303486089") {
    id
    name
    phases {
      name
      cards {
        edges {
          node {
            id
            title
            fields {
              name
              value
            }
          }
        }
      }
    }
  }
}
    """
    response = requests.post(url, json={'query': query}, headers=headers)
    data = response.json()
    return data

# PROCESSOS
ORGANIZATION_ID = get_all_organizations()['data']['organizations'][0]['id']
VENDAS_PIPE_ID = get_organization_pipes()['data']['organization']['pipes'][0]['id']

data = get_all_tables()
df = pd.DataFrame(data)

print(data)