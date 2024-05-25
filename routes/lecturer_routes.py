from flask import Blueprint, request, jsonify
from models.lecturer import Lecturer

lecturer_bp = Blueprint('lecturer_bp', __name__)

@lecturer_bp.route('/lecturer/add', methods=['POST'])
def add_lecturer():
    data = request.json
    Lecturer.add_lecturer(data)
    return jsonify({"message": "Lecturer added successfully"}), 201

@lecturer_bp.route('/lecturer/<lecturer_id>', methods=['GET'])
def get_lecturer(lecturer_id):
    lecturer = Lecturer.get_lecturer(lecturer_id)
    if lecturer:
        lecturer['_id'] = str(lecturer['_id'])
        return jsonify(lecturer), 200
    return jsonify({"message": "Lecturer not found"}), 404

@lecturer_bp.route('/lecturer/<lecturer_id>', methods=['PUT'])
def update_lecturer(lecturer_id):
    data = request.json
    result = Lecturer.update_lecturer(lecturer_id, data)
    if result.modified_count:
        return jsonify({"message": "Lecturer updated successfully"}), 200
    return jsonify({"message": "No lecturer found with the given ID or no changes made"}), 404

@lecturer_bp.route('/lecturer/<lecturer_id>', methods=['DELETE'])
def delete_lecturer(lecturer_id):
    result = Lecturer.delete_lecturer(lecturer_id)
    if result.deleted_count:
        return jsonify({"message": "Lecturer deleted successfully"}), 200
    return jsonify({"message": "No lecturer found with the given ID"}), 404

@lecturer_bp.route('/lecturer/getAll', methods=['GET'])
def get_all_lecturers():
    lecturers = list(Lecturer.get_all_lecturers())
    for lecturer in lecturers:
        lecturer['_id'] = str(lecturer['_id'])
    return jsonify(lecturers), 200