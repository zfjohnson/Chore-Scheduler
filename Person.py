import csv
import os


class Person:
    def __init__(self, name='None', id=0, email='None', floor=0, br_count=0, lr_count=0, kitchen_count=0, yard_count=0):
        self.name = name
        self.id = id
        self.email = email
        self.floor_no = floor
        self.br_count = br_count
        self.lr_count = lr_count
        self.kitchen_count = kitchen_count
        self.yard_count = yard_count

    def save_to_csv(self):
        # Define the path to the CSV file
        csv_path = 'data.csv'
        
        with open(csv_path, 'w', newline='') as csvfile:
            header = ['name','id','email','floor_no','br_count','lr_count','kitchen_count','yard_count']
            writer = csv.DictWriter(csvfile, fieldnames=header)
            
            # Write headers only if the file is newly created
            if not file_exists:
                writer.writeheader()
            
            # Write the person's data
            writer.writerow({
                'name': self.name,
                'id': self.id,
                'email': self.email,
                'floor_no': self.floor_no,
                'br_count': self.br_count,
                'lr_count': self.lr_count,
                'kitchen_count': self.kitchen_count,
                'yard_count': self.yard_count
            })

    def update_chore_count(self, chore_type):
        if chore_type == 'bathroom':
            self.br_count +=1
        elif chore_type == 'living_room':
            self.lr_count +=1
        elif chore_type == 'kitchen':
            self.kitchen_count +=1
        elif chore_type == 'yard':
            self.yard_count +=1
