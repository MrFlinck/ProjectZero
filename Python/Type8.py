import pygame 


test = 0  or 'não' or True
resposta = input("Você quer o primeiro audio ou segundo? (1/2): ")

if (resposta == '1'):
        
        print('shoosh')
        audio = 'audio/meme.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(audio)
        pygame.mixer.music.play()
        pygame.time.wait(1500)
    

elif(resposta == '2'):
        print('não')
        audio = 'audio/meme3.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(audio)
        pygame.mixer.music.play()
        pygame.time.wait(3000)



    




