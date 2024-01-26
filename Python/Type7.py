import pygame
audio = 'audio/meme.mp3'
nome = 'presunto'; 
print(nome[1])
print('p' in nome)

if'p' in nome: 
    print('meme')

if ('k' not in nome):
    print('shoosh')
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    pygame.time.wait(1500)

if ('meme' in nome): 
    audio = 'audio/meme2.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    pygame.time.wait(3000)






