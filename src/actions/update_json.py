import json


def update_json(data):
    with open('schedule.json', 'r') as file:
        existing_json = json.load(file)

    existing_json.update(data)

    with open('schedule.json', 'w') as file:
        json.dump(existing_json, file, indent=4)

    return 'Schedule.json file updated successfully.'
