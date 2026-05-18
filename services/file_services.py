import json
import csv 

class FileService:
    @staticmethod
    def save_json(filepath, data):
        with open(filepath, 'w') as file:
            json.dump(data, file, indent = 4)

    @staticmethod
    def load_json(filepath):
        with open(filepath, 'r') as file:
            return json.load(file)
    
    @staticmethod
    def save_csv(filepath, data , fieldnames):
        with open(filepath, 'w') as file:
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writedata(data)
    