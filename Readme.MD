# Auto upload Excel in blob storage to CosmosDB

## Sample settings.json

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "DefaultEndpointsProtocol=https;AccountName=accountname;AccountKey=accountkey;EndpointSuffix=core.windows.net",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "devopsb902_STORAGE": "DefaultEndpointsProtocol=https;AccountName=accountname;AccountKey=accountkey;EndpointSuffix=core.windows.net",
    "cosmos_endpoint" :"https://cosmos.documents.azure.com:443/",
    "cosmos_key" : "kkey==",
    "cosmos_database" : "database_name",
    "cosmos_container" : "container_name"
  }
}
```

