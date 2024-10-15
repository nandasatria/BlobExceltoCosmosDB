from io import BytesIO
import os
import uuid
import azure.functions as func
import logging
import pandas as pd

from azure.cosmos import CosmosClient, exceptions


app = func.FunctionApp()

@app.function_name(name="uploadexcel")
@app.blob_trigger(arg_name="myblob", path="excel/{name}", connection="devopsb902_STORAGE")
def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob\n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    data = myblob.read()
    excel_data = BytesIO(data)
    df = pd.read_excel(excel_data, engine='openpyxl')

    insert_cosmos(df=df)
        

def connect_cosmos():
    endpoint = os.getenv("cosmos_endpoint")
    key = os.getenv("cosmos_key")
    if endpoint is not None and key is not None:
        client = CosmosClient(endpoint, key)
        database_name = os.getenv("cosmos_database")
        container_name = os.getenv("cosmos_container") 
        if database_name and container_name:
            database = client.get_database_client(database_name)
            container = database.get_container_client(container_name)
            return container
        
    return None

def insert_cosmos(df):
    container = connect_cosmos()
    if container:
        df['id'] = [str(uuid.uuid4()) for _ in range(len(df))]

        for index, row in df.iterrows():
            # Convert the row to a dictionary
            item = row.to_dict()
            # Insert the item into the container
            try:
                container.create_item(body=item)
            except exceptions.CosmosResourceExistsError:
                print(f"Item already exists: {item['id']}")
    
    else:
        print("Failed to connect Container CosmosDB")
