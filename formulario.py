from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file
from db import insertar_alumno, insertar_baja, insertar_tutor, insertar_departamento
from openpyxl import load_workbook
import os
formu_bp= Blueprint('formu_bp',__name__,template_folder='templates')

@formu_bp.route('/formulario')
def  formulario():
    return render_template('form.html')

@formu_bp.route('/submit', methods =['POST'])
def submit():
    if request.method=='POST':
        nombre_alumno = request.form.get('nombre_alumno', "").strip().title()
        matricula = request.form.get('matricula', "").strip().upper()
        grupo = request.form.get('grupo', "").strip().upper()
        turno = request.form.get('turno', "").strip().upper()
        carrera = request.form.get('carrera', "").strip().title()
        nivel = request.form.get('nivel', "").strip().lower()
        cuatrimestre = request.form.get('cuatrimestre', "") .strip().upper()
    #############################################################
        motivo_baja = request.form.get('motivo_baja', "").strip().upper()
        detalles_baja = request.form.get('detalles_baja', "").strip()
        tipo_baja = request.form.get('tipo_baja', "").strip().capitalize()
    ##################################################
        nombre_tutor = request.form.get('nombre_tutor', "").strip().title()
        fecha_baja = request.form.get('fecha_baja', "").strip()
        numero_empleado = request.form.get('numero_empleado', "").strip()
        baja_responsable = request.form.get('baja_responsable', "").strip().capitalize()
        #######################
        departamento_responsable = request.form.get('departamento_responsable', "").strip()
        baja_fecha = request.form.get('baja_fecha', "").strip()
        try:
            # Insertar en tabla de alumno
            insertar_alumno(nombre_alumno, grupo, matricula, turno, carrera, nivel, cuatrimestre)
            
            insertar_baja(motivo_baja, detalles_baja, tipo_baja)
            
            insertar_tutor(nombre_tutor, fecha_baja, numero_empleado, baja_responsable)
            
            insertar_departamento(departamento_responsable, baja_fecha )
            
            ruta_archivo = 'template.xlsx'
            ruta_guardado = 'solicitud.xlsx'
            
            workbook = load_workbook(ruta_archivo)
            hoja = workbook['solicitud']
           
           ## alumno
            hoja['D6'] = nombre_alumno
            hoja['K6'] = matricula
            hoja['O6'] = grupo
            hoja['D8'] = carrera
            
            if nivel == "licenciatura":
                hoja['Q8'] = "X"
            elif nivel == "tsu":
                hoja['T8'] = "X"
                
            cuatrimestre_map = {"E-A": "M10", "M-A": "O10", "S-D": "Q10"}
            if cuatrimestre in cuatrimestre_map:
                hoja[cuatrimestre_map[cuatrimestre]] = "X"
                
            if turno == "M":
                hoja['R6'] = "X"
            elif turno == "V":
                hoja['T6'] = "X"
                
            ## motivos 
                
            motivo_baja_map = {
                "CAUSA DESCONOCIDA": 'G17',
                "INCUMPLIMIENTO DE EXPECTATIVAS": 'G18',
                "REPROBACIÓN": 'G19',
                "PROBLEMAS ECONÓMICOS": 'G20',
                "MOTIVOS PERSONALES": 'G21',
                "DISTANCIA DE LA UNIVERSIDAD (PROBLEMAS DE TRANSPORTE)": 'G22',
                "PROBLEMAS DE TRABAJO": 'G23',
                "CAMBIO DE INSTITUCIÓN": 'G24',
                "CAMBIO DE CARRERA": 'G25',
                "CAMBIO DE RESIDENCIA": 'M17',
                "FALTAS AL REGLAMENTO ESCOLAR": 'M18',
                "BAJO RENDIMIENTO ACADÉMICO": 'M19',
                "SALUD": 'M20',
                "DEFUNCIÓN": 'M21',
                "INASISTENCIAS": 'M22',
                "EMBARAZO": 'M23',
                "MALA ELECCIÓN DE CARRERA": 'M24',
                "VIOLENCIA ESCOLAR": 'M25'
            }
            
            if motivo_baja in motivo_baja_map:
                hoja[motivo_baja_map[motivo_baja]] = "X"
                
            hoja['O17'] = detalles_baja
            
            if tipo_baja == "Temporal":
                hoja['T22'] = "X"
            if tipo_baja== "Definitiva":
                hoja['T23'] = "X"
                
            ## tutor
            hoja['B30'] = nombre_tutor
            hoja['J30'] = fecha_baja
            hoja['M30'] = numero_empleado
            if baja_responsable == "Tutor":
                hoja['K28'] = "X"
            elif tipo_baja == "Alumno":
                 hoja['Q28'] = "X"
            #departamento
            hoja['B33'] = departamento_responsable
            hoja['J33'] = baja_fecha
                
            
            workbook.save(ruta_guardado)
            
            
            #flash("Datos insertados correctamente", "success")
            flash("Datos insertados correctamente", "success")
            # Enviar el archivo generado al usuario para su descarga
            return send_file(ruta_guardado, as_attachment=True)
    
        except Exception as e:
            flash(f"Error al insertar datos: {str(e)}", "danger")           
            return redirect(url_for('formu_bp.formulario'))
        
        
        
##paso
#1 el usuario ingrese los datos en el formulario
#2 que los datos se envien a la base de datos 
#3 que el archivo excel se llene en la celda esoecifica con la info del formulario.
#4 que los datos se analizen con el inicio de sesion 
        
        
        
        
        
        
    
        
       

        