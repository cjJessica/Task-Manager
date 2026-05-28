import json

#Save data to file
def save_data(data):
    with open('data/tasks.json', 'w') as json_file:
        json.dump(data, json_file)