#!/usr/bin/env/python3

#imports
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

compiler = Tk()
compiler.title("IDE")
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path
