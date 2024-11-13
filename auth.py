from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from db import insertar_usuarios

auth = Blueprint ('auth',__name__,template_folder='templates')

@auth.route('/', methods = ['GET'])
def login_form():
    return render_template('login.html')

@auth.route('/login', methods =['POST'])
def login_post():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        contra = request.form.get('contra')
        insertar_usuarios(nombre, contra)
        
        
@auth.route('/registro', methods = ['GET'])
def registro_form():
    return render_template('registro.html')

@auth.route('/registro', methods = ['POST'])
def registro_post():
    nombre = request.form.get('nombre')
    contra = request.form.get('contra')
    insertar_usuarios(nombre, contra)
        




