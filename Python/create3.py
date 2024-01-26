import pygame
import cv2


resposta = input("Coloque o nome do meme: ")
if(resposta == 'miau'):
    audio = 'audio/meme2.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    pygame.time.wait(3000)

elif(resposta == 'jooj'):
    audio = 'audio/meme.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    pygame.time.wait(1500)



elif(resposta == 'video'):
    video_path = 'video/grito.mp4'
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print('algo deu errado')
        exit()
    while True:
        ret, frame = cap.read()

        if not ret:
             break
        
        cv2.imshow('Video' , frame)
        if cv2.waitKey(25)  == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
     


else:
    audio = 'audio/meme3.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    pygame.time.wait(3000)

