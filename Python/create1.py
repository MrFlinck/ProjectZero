import pygame
import webbrowser
import re
import tkinter as tk 
from tkinter import messagebox

palavra_chave = "batata" 




pygame.init()
audio = "audio/meme.mp3"



nome = 'presunto'; 
print(nome[1])
print('p' in nome)
if ('p' in nome):
    print('shoosh')
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    pygame.time.wait(1500) #aguarda 5 segundos


    