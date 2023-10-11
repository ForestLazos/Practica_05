# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 19:05:43 2023

@author: danie
"""

import tkinter as tk

def limpiar_campos():
    entry_nombres.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_estatura.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    var_genero.set(0)

def borrar_campos():
    limpiar_campos()
    
def guardar_datos():
    nombre= entry_nombres.get()
    apellidos= entry_apellidos.get()
    eda= entry_edad.get()
    estatura= entry_estatura.get(0, tk.END)
    entry_telefono.delete(0, tk.END)
    
    genero= ""
    if var_genero.get()==1:
        genero= "Hombre"
    elif var_genero.get()==2:
        genero= "Mujer"
    
    with open("datos99.txt", "a") as archivo:
        archivo.write(datos+"/n/n")
    
    messagebox.showinfo("Información", "Datos guardados con éxito:/n/n"+datos)