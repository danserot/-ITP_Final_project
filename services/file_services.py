import json
import csv 

class FileService:
    @staticmethod
    def save_json(filepath, data):
        with open(filepath, 'w') as file:
            json.dump(data, file, indent = 4)
