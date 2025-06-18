from flask import Blueprint, redirect, render_template, request, url_for

from app.decorators.auth_decorator import requiere_autenticacion

from app.services.auth_service import log_in, register
from app.services.checklist_service import post_items_service, get_items_service, put_items_service, delete_items_service


main_routes = Blueprint('main_routes', __name__)


#Frontend
@main_routes.route("/indexlogin", methods=["GET"])
def indexLogin_get():
    return render_template("indexLogin.html")

@main_routes.route("/indexchecklist", methods=["GET"])
@requiere_autenticacion
def indexChecklist_get():
    return render_template("indexChecklist.html")

@main_routes.route("/indexreporte", methods=["GET"])
@requiere_autenticacion
def reporte_view():
    return render_template("indexReporte.html")


#Backend
@main_routes.route("/login", methods=["POST"])
def login_post():
    data = request.get_json()
    response = log_in(data)
    return response

@main_routes.route("/register", methods=["POST"])
def register_post():
    data = request.get_json()
    response = register(data)
    return response





@main_routes.route("/item", methods=["POST"])
@requiere_autenticacion
def post_items():
    data = request.get_json()
    response = post_items_service(data)
    return response

@main_routes.route("/item", methods=["GET"]) 
@requiere_autenticacion
def get_items():
    response = get_items_service()
    return response

@main_routes.route("/item", methods=["PUT"]) 
@requiere_autenticacion
def put_items():
    data = request.get_json()
    response = put_items_service(data)
    return response

@main_routes.route("/item", methods=["DELETE"])  
@requiere_autenticacion
def delete_items():
    data = request.get_json()
    response = delete_items_service(data)
    return response

