from .api_config import fastapi_app
import httpx
import json
from typing import Dict, Any 
import os
from dotenv import load_dotenv


class railway_api:
    
    load_dotenv('.env.development')
    
    API_TOKEN = os.getenv("railway_API_TOKEN")
    
    PROJECT_ID = os.getenv("railway_PROJECT_ID")
    
    ENVIRONMENT_ID = os.getenv("railway_ENVIRONMENT_ID")
    
    SERVICE_ID = os.getenv("railway_SERVICE_ID")
    
    RAILWAY_GRAPHQL_ENDPOINT = "https://backboard.railway.com/graphql/v2"
    
    QUERY = f"""
    query GetLatestDeploymentInfo {{
      deployments(
        first: 1 
        input: {{
          projectId: "{PROJECT_ID}"
          environmentId: "{ENVIRONMENT_ID}"
          serviceId: "{SERVICE_ID}"
        }}
      ) {{
        edges {{
          node {{
            id         
            status     
            createdAt  
            updatedAt  
          }}
        }}
      }}
    }}
    """

    HEADERS = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    PAYLOAD = {"query": QUERY}
    
    

@fastapi_app.get("/railway/state")
async def fetch_latest_deployment()-> Dict[str, Any]:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                railway_api.RAILWAY_GRAPHQL_ENDPOINT, 
                headers=railway_api.HEADERS, 
                json=railway_api.PAYLOAD,
                timeout=10.0
            )
            
            response.raise_for_status() 
            
            data = response.json()

            if 'errors' in data:
                error_details = json.dumps(data['errors'], indent=2)
                raise ValueError(f"Error GraphQL en la respuesta: {error_details}")

            deployments_data = data.get('data', {}).get('deployments', {})
            
            latest_deployment = deployments_data['edges'][0]['node']
            
            return {
                "status": latest_deployment.get('status', 'N/A'),
                "updated_at": latest_deployment.get('updatedAt', 'N/A'),
            }
        
        except httpx.HTTPStatusError as e:
            raise ConnectionError(f"Error HTTP {e.response.status_code} al conectar: {e.response.text}") from e
        except Exception as e:
            raise ConnectionError(f"Error de conexión o inesperado: {e}") from e