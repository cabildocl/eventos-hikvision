#!/usr/bin/env python
# coding: utf-8

# In[112]:
# Este scrip recibe una notificacion de deteccion de rostro y la imagen
# de una camara hikvision. Y dividimos la informacion entre imagen y datos
#
#import xmltodict
from flask import Flask, flash, request, redirect, url_for
#from werkzeug.utils import secure_filename
import os
#import io
#from werkzeug.datastructures import ImmutableMultiDict
import json
app = Flask(__name__)


# In[ ]:


@app.route('/evento', methods = ['POST'])
def evento():
    data4 = request.stream.read()
    ### parametro limite entre informacion
    boundary="--boundary\r\n".encode()
    ### extracion de imagen
    imagen=data4.split(boundary)[2]
    imagen=imagen.split("\r\n\r\n".encode())[1]
    ### extracion json
    tipo=data4.split(boundary)[1]
    tipo=tipo.split("\r\n\r\n".encode())[1]
    listado=tipo.decode()
    ## usar uid para nombre
    nombre=json.loads(listado)['uid']
    ### guardar imagen e informacion
    f = open("informacion/"+str(nombre)+".jpg", "wb")
    f.write(imagen)
    f.close()
    g = open("informacion/"+str(nombre)+".txt", "wb")
    g.write(tipo)
    g.close()
    return 'JSON posted'
app.run(host='0.0.0.0', port= 8001)

