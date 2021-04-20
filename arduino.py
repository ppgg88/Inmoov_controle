from tkinter import *
import serial
import serial.tools.list_ports
import configparser

cfg = configparser.ConfigParser()
cfg.read('config/info.ini')

conexion = False

def connection_robot():
    global conexion
    port_available = serial.tools.list_ports.comports(include_links=False)
    print(port_available)
    if cfg["robot"]["arduino_com"] in port_available :
        print("connection en cours :")
        try :
            arduino = serial.Serial(cfg["robot"]["arduino_com"], cfg["robot"]["arduino_speed"], timeout=1)
            print("conection OK")
            conexion = True
            return(conexion)
        except :
            print("erreur inconue sur le port : " + cfg["robot"]["arduino_com"])
            conexion = False
            return(conexion)
    else :
        print("erreur d'ouverture du port : " + cfg["robot"]["arduino_com"])
        conexion = False
        return(conexion)

def controle_moteur(pin, valeur):
    """prend en entrer le pin du moteur à controler et le positionement en angle de ce moteurs"""
    """la trame de controle du moteur en hexadecimal sera : 22 pin angle"""
    global conexion
    if conexion == False :
        print("l'arduino n'est pas conecter")
    else :
        arduino.write(0x22)
        arduino.write(pin)
        arduino.write(valeur)
