import sqlite3 

# siquiero llamar la base de datos
#para utilizar las funciones solo 
#importo al blueprint que utilize la 
#base de datos 

# creacion de la base de datos en sqlite
def crear_db():
    conn = sqlite3.connect("bajas_siges.db")
    conn.commit()
    conn.close()
    
# funcion que crea la tabla alumno baja
def usuarios():
    conn = sqlite3.connect("bajas_siges.db")
    cursor = conn.cursor()
    cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS usuarios(            
                id INTEGER PRIMARY KEY  AUTOINCREMENT,
                nombre TEXT NOT NULL,
                contra TEXT NOT NULL
            )   
    """)
    conn.commit()
    conn.close()
    
def alumno_baja():
      conn = sqlite3.connect("bajas_siges.db")
      cursor = conn.cursor()
      cursor.execute("""
            CREATE TABLE IF NOT EXISTS alumno(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_alumno TEXT NOT NULL,
                matricula TEXT NOT NULL,
                grupo TEXT NOT NULL,
                turno TEXT NOT NULL,
                carrera TEXT NOT NULL,
                nivel TEXT NOT NULL,
                cuatrimestre TEXT NOT NULL
            )             
      """)
      conn.commit()
      conn.close()

#funcion que crea la tabla motivo, se puede llamar de cualquier parte solo importando
def motivo_baja():
    conn = sqlite3.connect("bajas_siges.db")
    cursor = conn.cursor()
    cursor.execute("""
             CREATE TABLE IF NOT EXISTS motivo(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   motivo_baja TEXT NOT NULL,
                   detalles_baja TEXT NOT NULL,
                   tipo_baja TEXT NOT NULL
            )
       """)
    conn.commit()
    conn.close()
    
#creacion del  tutor esta funcion tambien se puede llamar desde cualquier parte del codigo solo importandola 
def tutor():
    conn = sqlite3.connect("bajas_siges.db")
    cursor = conn.cursor()
    cursor.execute("""
             CREATE TABLE IF NOT EXISTS tutor(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre_tutor TEXT NOT NULL,
                   fecha_baja TEXT NOT NULL,
                   num_empleado TEXT NOT NULL,
                   baja_responsable TEXT NOT NULL
            )
    """)
    conn.commit()
    conn.close()
    
# funcion de la creacion de la tabla departamentos bajas.
def dep_bajas():
    conn = sqlite3.connect("bajas_siges.db")
    cursor = conn.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS departamento(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   resp_baja TEXT NOT NULL,
                   baja_fecha TEXT NOT NULL
            )
                   
    """)
    conn.commit()
    conn.close()
    
## funciones para insertar datos en la base de datos.
def insertar_alumno(nombre_alumno, matricula, grupo,turno, carrera, nivel, cuatrimestre):
    conn = sqlite3.connect('bajas_siges.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO alumno (nombre_alumno, grupo, matricula, turno, carrera, nivel, cuatrimestre)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (nombre_alumno, matricula, grupo, turno, carrera, nivel, cuatrimestre))
    conn.commit()
    conn.close()
    
#datos para insertar a la tabla de baja.

def insertar_usuarios(nombre, contra):
    conn = sqlite3.connect('bajas_siges.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO usuarios (nombre, contra)
                   VALUES (?,?)''', (nombre, contra))
    conn.commit()
    conn.close()

def insertar_baja(motivo_baja, detalles_baja, tipo_baja):
    conn = sqlite3.connect('bajas_siges.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO motivo (motivo_baja, detalles_baja, tipo_baja)
                      VALUES (?, ?, ?)''', (motivo_baja, detalles_baja, tipo_baja))
    conn.commit()
    conn.close()
    
def insertar_tutor(nombre_tutor, fecha_baja, num_empleado, baja_responsable):
    conn = sqlite3.connect('bajas_siges.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO tutor (nombre_tutor, fecha_baja, num_empleado, baja_responsable)
                      VALUES (?, ?, ?, ?)''', (nombre_tutor, fecha_baja, num_empleado, baja_responsable))
    conn.commit()
    conn.close()
    
def insertar_departamento(resp_baja, baja_fecha):
    conn = sqlite3.connect('bajas_siges.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO departamento (resp_baja, baja_fecha)
                      VALUES (?, ?)''', (resp_baja, baja_fecha))
    conn.commit()
    conn.close()
    

        
        


    
    
    
if __name__=="__main__":
    #crear_db()
    #usuarios()
    #alumno_baja()
    #motivo_baja()
    #tutor()
    #dep_bajas()
    pass