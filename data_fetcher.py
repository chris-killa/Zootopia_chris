import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')
URL = 'https://api.api-ninjas.com/v1/animals?name={}'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    """
    response = requests.get(URL.format(animal_name), headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        list_of_type = response.json()
    else:
        print("Error:", response.status_code, response.text)
        return "<h2>No animal found.</h2>"
    output_list = []
    for animal in list_of_type:
        if animal_name.lower() in animal['name'].lower():
            output_list.append(animal)
    return output_list


