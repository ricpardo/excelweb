from flask import Flask
from db import crear_db, usuarios, alumno_baja, motivo_baja, tutor, dep_bajas
from auth import auth
from formulario import formu_bp
from prueba import prueba_bp
app = Flask(__name__)
app.secret_key = 'mi_clave_secreta_unica'
app.register_blueprint(auth)
app.register_blueprint(formu_bp)
app.register_blueprint(prueba_bp)

def init_db():
    crear_db()
    usuarios()
    alumno_baja()
    motivo_baja()
    tutor()
    dep_bajas()
if __name__=="__main__":
    init_db()
    
    app.run(debug=True)