"""Recursos HTTP relacionados con `Paciente`.

Define endpoints para listar, obtener, actualizar y eliminar pacientes.
Las respuestas usan `PacienteSchema` para serializar/deserializar y se
apoyan en `PacienteService` para la lógica de negocio.
"""

from app.models import Paciente
from app.services.paciente_service import PacienteService
from app.mapping import PacienteSchema

from flask import Blueprint, jsonify, request


paciente_bp = Blueprint('paciente', __name__)

paciente_schema = PacienteSchema()


@paciente_bp.route('/pacientes/', methods=['GET'])
def get_pacientes():
    pacientes = PacienteService.read_all()
    return paciente_schema.dump(pacientes, many=True), 200


@paciente_bp.route('/pacientes/<int:id>/', methods=['GET'])
def get_paciente(id):
    paciente = PacienteService.get_by_id(id)
    if not paciente:
        return jsonify({'message': 'Paciente no encontrado'}), 404
    return paciente_schema.dump(paciente), 200


@paciente_bp.route('/pacientes/<int:id>/', methods=['DELETE'])
def delete_paciente(id):
    deleted = PacienteService.delete(id)
    if deleted:
        return jsonify({"message": f"Paciente {id} eliminado"}), 200
    return jsonify({"message": f"Paciente {id} no encontrado"}), 404


@paciente_bp.route('/pacientes/<int:id>/', methods=['PUT'])
def update_paciente(id):
    paciente = paciente_schema.load(request.get_json(),many=False)
    setattr(paciente, 'id', id)
    updated = PacienteService.update(paciente)
    return paciente_schema.dump(updated), 200
from app.models import Paciente
from app.services import PacienteService
from app.mapping import PacienteSchema

from flask import Blueprint, jsonify, request


paciente_bp = Blueprint('paciente', __name__)

paciente_schema = PacienteSchema()
paciente_service = PacienteService()

@paciente_bp.route('/pacientes/', methods=['GET'])
def get_pacientes():
    pacientes = paciente_service.obtener_todos_los_pacientes()
    return paciente_schema.dump(pacientes, many=True), 200
    

@paciente_bp.route('/pacientes/<int:id>/', methods=['GET'])
def get_paciente(id):
    paciente = paciente_service.obtener_paciente(id)
    return paciente_schema.dump(paciente), 200
    

@paciente_bp.route('/pacientes/<int:id>/', methods=['DELETE'])
def delete_paciente(id):
    return jsonify({"message": f"Paciente {id} deleted"}), 200

@paciente_bp.route('/pacientes/<int:id>/', methods=['PUT'])
def update_paciente(id):
    paciente = paciente_schema.load(request.get_json(),many=False)
    return jsonify({"message": f"Paciente {id}, {paciente.nombre} updated"}), 200