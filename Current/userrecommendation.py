import os
import subprocess

PATH = os.path.dirname(__file__)
filepath = os.path.join(PATH,'reccomendations.txt')
filename = filepath
    
def starter():
    os.startfile(filename)
