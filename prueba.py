from flask import Blueprint, render_template, request, redirect, url_for, flash

prueba_bp=Blueprint('prueba_bp',__name__, template_folder='templates')

@prueba_bp.route('/prueba')
def prueba():
    return render_template('prueba.html')