import os
import pandas as pd

class Data():
    def overrideData(self,folderName):
        newData = pd.DataFrame()
        for i in folderName:
            path = '/Users/muratdemiralay/Downloads/'#buraya klasorlerin oldugu yolu yazin   
            path = path+i  
            dataName = os.listdir(path)
            for j in dataName:
                data = pd.read_excel(path+'/'+j)
                col = data.columns
                for k in range(len(col)):
                    if k == 0:
                        newData['TARIH'] = data[col[k]]
                    else:
                        newData[col[k]] = data[col[k]]
                folderPath = str(os.getcwd())+"/"+i
                if os.path.exists(folderPath) == False:
                    os.mkdir(folderPath)
                newData.to_excel(folderPath+'/'+j, sheet_name='sheet_1', index = False)

folderName = ['xxxxx', 'xxxxx', 'xxxxx']
data = Data()
data.overrideData(folderName)
