# core.py
# This script interacts with the Pixela API

import requests
from getDate import get_current_date
import json
import os
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

def create_user(token: str, username: str) -> dict:
    """
    Creates a new user on Pixela with the specified username and token.
    
    Args:
        token (str): The token for the Pixela user.
        username (str): The username for the Pixela user.
    Returns:
        response (dict): The response from the Pixela API after creating the user.
    """
    
    userParams = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    
    response = requests.post(PIXELA_ENDPOINT, json=userParams)
    return response.json()

def create_graph(graph_id: str, name: str, unit: str, type: str, color: str, timezone: str, token: str, username: str) -> dict:
    """
    Creates a new graph on Pixela with the specified parameters.
    
    Args:
        graph_id (str): The ID of the graph to be created.
        name (str): The name of the graph.
        unit (str): The unit of measurement for the graph.
        type (str): The type of data the graph will hold (e.g., int, float).
        color (str): The color of the graph. Accepted values: "shibafu", "momiji", "sora", "ichou", "ajisai", or "kuro".
        timezone (str): The timezone for the graph.
        token (str): The user's token ID
        username (str): The username
    Returns:
        response (dict): The response from the Pixela API after creating the graph.
    """
    graphEndpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
    graph_params = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": type,
        "color": color,
        "timezone": timezone
    }

    headers = {
        "X-USER-TOKEN": token
    }

    response = requests.post(graphEndpoint, json=graph_params, headers=headers)
    return response.json()

# Adding a pixel
def add_pixel(graph_id: str, headers: dict, quantity: str, date: str, username: str) -> dict:
    """
    Adds a pixel to the specified graph on Pixela.
    Args:
        graph_id (str): User-generated graph id
        headers (dict): A dictionary that contains token
        quantity (str): The quantity to be added to the graph (must match graph type, e.g., "1" or "1.5")
    Returns:
        response (json): The response recieved from Pixela API
    """
    pixel_params = {
        "date": date,
        "quantity": quantity
    }
    add_pixel_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}"
    response = requests.post(add_pixel_endpoint, json=pixel_params, headers=headers)
    print(add_pixel_endpoint)
    print(response.text)
    return response.json()
CREDS_FILE = "creds.json"

def update_creds(username=None, tokenID=None, graphID=None, quantity=None, quantityType=None) -> None: 
    """
    Updates the creds.json file with new values for any provided fields.
    Existing values are preserved if not explicitly updated.
    Args:
        username (str): the username to update. Set to None
        tokenID (str): the user-generated token ID.  Set to None
        graphID (str): graph ID for the graph. Set to None
        quantity (str): The unit to use in the graph Set to None
        quantityType (str): The type of unit to use in the graph (accepted values: int or float). Set to None
    """
    # Load existing creds (or use defaults if file doesn't exist)
    if os.path.exists(CREDS_FILE):
        with open(CREDS_FILE, "r") as file:
            creds = json.load(file)
    else:
        creds = {
            "username": None,
            "tokenID": None,
            "graphID": None,
            "quantity": None,
            "quantityType": None
        }

    # Update only the provided fields
    if username is not None:
        creds["username"] = username
    if tokenID is not None:
        creds["tokenID"] = tokenID
    if graphID is not None:
        creds["graphID"] = graphID
    if quantity is not None:
        creds["quantity"] = quantity
    if quantityType is not None:
        creds["quantityType"] = quantityType

    # Save the updated creds
    with open(CREDS_FILE, "w") as file:
        json.dump(creds, file, indent=4)
# print(create_user(token="hellooooooo@12334", username="aknow")) <--- demo error message
