import cv2
import qrcode
import os
import shutil



def associationducode(chemin,path):
    leqrcode=qrcode.make(path)
    leqrcode.save(f'{chemin}.png')


    img=cv2.imread(f'{chemin}.png')
    cv2.imshow('Output',img)
    cv2.waitKey(1000)

    emplacementSrc=f'./{chemin}.png'
    emplacementDest='./qrcodeFichiers'

    shutil.move(emplacementSrc, emplacementDest)



    if os.path.exists('./qrcodeFichiers/'+f'{chemin}.png'):
        print('le fichier a été généré')
    else: 
        print('le fichier n a pas ete généré' )
    


