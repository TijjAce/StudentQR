import xlsxwriter
from os import walk
import QrMake





listFichier=[]
x=0
for(repertoire,sousRepertoires, fichiers)in walk('dossierfichier/'):
    listFichier.extend(fichiers)
    
for i in listFichier:
    x=x+1
newFile=str(x+1)


nomInput=input('Ecrit le nom de l\'eleve\n')
PrenomInput=input('Ecrit le prenom de l\'eleve\n')
classInput=input('Ecrit la classe de l eleve comme l exemple: \'4b\'')



creator=(str(nomInput+PrenomInput+newFile+'.xlsx'))
path=(f'file:///sdcard/Documents/{classInput}/')
print(path)
QrMake.associationducode(creator, path)


workbook=xlsxwriter.Workbook(f'./dossierfichier/{creator}')
worksheet=workbook.add_worksheet()
worksheet.write('A1',nomInput)
worksheet.write('B1',PrenomInput)
worksheet.write('C1',classInput)


workbook.close()
