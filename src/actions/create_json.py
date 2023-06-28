import json


def create_json(data):
    with open('schedule.json', 'w') as file:
        json.dump(data, file, indent=4)

    return 'schedule.json file generated successfully.'
