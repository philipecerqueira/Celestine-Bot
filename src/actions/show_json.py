import json


def show_json():
    try:
        with open('schedule.json', 'r') as file:
            json_data = json.load(file)
            print(json_data)
        return json_data
    except FileNotFoundError:
        return 'The JSON file does not exist.'
