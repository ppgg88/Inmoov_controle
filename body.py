from tkinter import *
from arduino import *
import configparser

cfg = configparser.ConfigParser()
cfg.read('config/info.ini')


#controle des moteurs
def moteur_head_1(position):
    #rotation tete
    angle = int(cfg["moteurs"]["rotation_tete_max"])-int(cfg["moteurs"]["rotation_tete_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["rotation_tete_min"])
    print("head 1 : " + str(int(angle)))
    controle_moteur(int(cfg["moteurs"]["rotation_tete_pin"]), int(angle))

def moteur_head_2(position):
    #mouvement haut bas
    angle = int(cfg["moteurs"]["elevation_tete_max"])-int(cfg["moteurs"]["elevation_tete_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["elevation_tete_min"])
    print("head 1 : " + str(int(angle)))
    controle_moteur(int(cfg["moteurs"]["elevation_tete_pin"]), int(angle))

def moteur_head_3(position):
    #mouvement bouche
    angle = int(cfg["moteurs"]["bouche_tete_max"])-int(cfg["moteurs"]["bouche_tete_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["bouche_tete_min"])
    print("head 3 : " + str(int(angle)))
    controle_moteur(int(cfg["moteurs"]["bouche_tete_pin"]), int(angle))

def moteur_head_4(position):
    #mouvement yeux X
    angle = int(cfg["moteurs"]["yeux_x_tete_max"])-int(cfg["moteurs"]["yeux_x_tete_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["yeux_x_tete_min"])
    print("head 4 : " + str(int(angle)))
    controle_moteur(int(cfg["moteurs"]["yeux_x_tete_pin"]), int(angle))

def moteur_head_5(position):
    #mouvement yeux Y
    angle = int(cfg["moteurs"]["yeux_y_tete_max"])-int(cfg["moteurs"]["yeux_y_tete_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["yeux_y_tete_min"])
    print("head 5 : " + str(int(angle)))
    controle_moteur(int(cfg["moteurs"]["yeux_y_tete_pin"]), int(angle))

def moteur_left_arm_1(position):
    #mouvement epaule gauche x
    angle = int(cfg["moteurs"]["epaule_x_left_max"])-int(cfg["moteurs"]["epaule_x_left_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["epaule_x_left_min"])
    print("left arm 1 : " + str(int(angle)))
    controle_moteur(int(cfg["moteurs"]["epaule_x_left_pin"]), int(angle))

def moteur_left_arm_2(position):
    #mouvement epaule gauche y
    angle = int(cfg["moteurs"]["epaule_y_left_max"])-int(cfg["moteurs"]["epaule_y_left_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["epaule_y_left_min"])
    print("left arm 2 : " + str(int(angle)))
    controle_moteur(int(cfg["moteurs"]["epaule_y_left_pin"]), int(angle))

def moteur_left_arm_3(position):
    #mouvement epaule gauche z
    angle = int(cfg["moteurs"]["epaule_z_left_max"])-int(cfg["moteurs"]["epaule_z_left_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["epaule_z_left_min"])
    print("left arm 3 : " + str(int(angle)))
    controle_moteur(int(cfg["moteurs"]["epaule_z_left_pin"]), int(angle))

def moteur_left_arm_4(position):
    #mouvement yeux Y
    angle = int(cfg["moteurs"]["coude_left_max"])-int(cfg["moteurs"]["coude_left_min"])
    angle = ((float(position)/100) * angle) + float(cfg["moteurs"]["coude_left_min"])
    print("left arm 4 : " + str(int(angle)))
    controle_moteur(int(cfg["moteurs"]["coude_left_pin"]), int(angle))