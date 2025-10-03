from flask import Blueprint, request, jsonify
from app.services.agenda_service import AgendaService

agenda_bp = Blueprint("agenda_bp", __name__)

@agenda_bp.route("/agendas", methods=["GET"])
def listar_agendas():
    agendas = AgendaService.listar_agendas()
    return jsonify([{"id": a.id, "fecha": str(a.fecha)} for a in agendas])

@agenda_bp.route("/agendas/<int:agenda_id>", methods=["GET"])
def obtener_agenda(agenda_id):
    agenda = AgendaService.obtener_agenda(agenda_id)
    if agenda:
        return jsonify({"id": agenda.id, "fecha": str(agenda.fecha)})
    return jsonify({"error": "Agenda no encontrada"}), 404

@agenda_bp.route("/agendas", methods=["POST"])
def crear_agenda():
    data = request.get_json()
    nueva_agenda = AgendaService.crear_agenda(data["fecha"])
    return jsonify({"id": nueva_agenda.id, "fecha": str(nueva_agenda.fecha)}), 201

@agenda_bp.route("/agendas/<int:agenda_id>", methods=["DELETE"])
def eliminar_agenda(agenda_id):
    eliminado = AgendaService.eliminar_agenda(agenda_id)
    if eliminado:
        return jsonify({"mensaje": "Agenda eliminada"})
    return jsonify({"error": "Agenda no encontrada"}), 404
