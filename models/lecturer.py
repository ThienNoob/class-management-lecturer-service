from bson.objectid import ObjectId
from flask import current_app

class Lecturer:
    @staticmethod
    def add_lecturer(data):
        db = current_app.config['DB']
        return db.lecturer.insert_one(data)
    
    @staticmethod
    def get_lecturer(lecturer_id):
        db = current_app.config['DB']
        return db.lecturer.find_one({'_id': ObjectId(lecturer_id)})
    
    @staticmethod
    def update_lecturer(lecturer_id, data):
        db = current_app.config['DB']
        return db.lecturer.update_one({"_id": ObjectId(lecturer_id)}, {"$set": data})
    
    @staticmethod
    def delete_lecturer(lecturer_id):
        db = current_app.config['DB']
        return db.lecturer.delete_one({"_id": ObjectId(lecturer_id)})
    
    @staticmethod
    def get_all_lecturers():
        db = current_app.config['DB']
        return db.lecturer.find()