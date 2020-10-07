import sys
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from NewConverter import Ui_Dialog
from threading import Timer

import requests
from bs4 import BeautifulSoup as BS 
# Create app
app = QtWidgets.QApplication(sys.argv)

# init
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

# Hook logic
def cours():
    p = requests.get('https://www.profinance.ru/')
    proFinance = BS(p.content, 'html.parser')
    u = requests.get('https://kurs.com.ua/')
    kurs = BS(u.content, 'html.parser')
    a = requests.get('https://www.agroprombank.com/')
    agroprombank = BS(a.content, 'html.parser')
    s = requests.get('https://www.sravni.ru/bank/sberbank-rossii/valjuty/')
    sberbank = BS(s.content, 'html.parser')


    # proFinance
    proCours = proFinance.select('.curs')
    # Ukr. kurs
    ukrCours = kurs.select('.course')
    # agroprombank
    agroCours = agroprombank.select('.pane')
    # sberbank
    sberCours = sberbank.select('.table-light__cell ')
    usd0 = list(sberCours[1].text[0:5])
    usd1 = list(sberCours[2].text[0:5])
    eur0 = list(sberCours[5].text[0:5])
    eur1 = list(sberCours[6].text[0:5])
    usd0[2] = '.'
    usd1[2] = '.'
    eur0[2] = '.'
    eur1[2] = '.'
    usbB = ''.join(usd0)
    usbS = ''.join(usd1)
    eurB = ''.join(eur0)
    eurS = ''.join(eur1)
    # adding cours to labels
    ui.label_65.setText(proCours[7].select('td')[1].text)
    ui.label_67.setText(proCours[7].select('td')[2].text)
    ui.label_66.setText(proCours[8].select('td')[1].text)
    ui.label_68.setText(proCours[8].select('td')[2].text)

    ui.label_69.setText(proCours[10].select('table > tr')[4].select('td')[1].text)
    ui.label_73.setText(proCours[10].select('table > tr')[4].select('td')[2].text)
    ui.label_70.setText(proCours[10].select('table > tr')[4].select('td')[5].text)
    ui.label_74.setText(proCours[10].select('table > tr')[4].select('td')[6].text)
    ui.label_71.setText(proCours[10].select('table > tr')[4].select('td')[9].text)
    ui.label_75.setText(proCours[10].select('table > tr')[4].select('td')[10].text)
    ui.label_72.setText(proCours[10].select('table > tr')[4].select('td')[13].text)
    ui.label_76.setText(proCours[10].select('table > tr')[4].select('td')[14].text)
    # Ukr. kurs
    ui.label_43.setText(ukrCours[0].text[0:6])
    ui.label_44.setText(ukrCours[1].text[0:6])
    # agroprombank
    ui.label_55.setText(agroCours[0].select('td')[10].text)
    ui.label_56.setText(agroCours[0].select('td')[11].text)
    ui.label_57.setText(agroCours[0].select('td')[19].text)
    ui.label_61.setText(agroCours[0].select('td')[20].text)
    ui.label_58.setText(agroCours[0].select('td')[22].text)
    ui.label_62.setText(agroCours[0].select('td')[23].text)
    ui.label_59.setText(agroCours[0].select('td')[25].text)
    ui.label_63.setText(agroCours[0].select('td')[26].text)
    ui.label_60.setText(agroCours[0].select('td')[28].text)
    ui.label_64.setText(agroCours[0].select('td')[29].text)

    ui.label_17.setText(agroCours[0].select('td')[4].text)
    ui.label_18.setText(agroCours[0].select('td')[5].text)
    ui.label_19.setText(agroCours[0].select('td')[7].text)
    ui.label_20.setText(agroCours[0].select('td')[8].text)
    ui.label_21.setText(agroCours[0].select('td')[13].text)
    ui.label_22.setText(agroCours[0].select('td')[14].text)
    ui.label_23.setText(agroCours[0].select('td')[16].text)
    ui.label_24.setText(agroCours[0].select('td')[16].text)
    # sberbank
    ui.label_51.setText(usbB)
    ui.label_53.setText(usbS)
    ui.label_52.setText(eurB)
    ui.label_54.setText(eurS)
    Timer(3.0, cours).start()

Timer(3.0, cours).start()
cours()

sds = re.compile('^\d+(\,\d+)$')
msd = re.compile('^\d+$')
lsd = re.compile('^\d+\,$')
# proCoursConverter
def pro():
    if(ui.lineEdit_19.text() != '' and sds.match(ui.lineEdit_19.text()) != None or msd.match(ui.lineEdit_19.text()) != None or lsd.match(ui.lineEdit_19.text()) != None):
        if re.search(',', ui.lineEdit_19.text()):
            a = ui.lineEdit_19.text()
            rep = a.replace(',', '.')
            value = rep
        else:
            value = ui.lineEdit_19.text()
    else:
        value = 0
    if(ui.comboBox_10.currentText() == 'USD' and ui.comboBox_9.currentText() == 'RUB'):
        result = float(value) * float(ui.label_65.text()) 
    elif(ui.comboBox_10.currentText() == 'USD' and ui.comboBox_9.currentText() == 'EUR'):
        result = float(value) / float(ui.label_73.text()) 
    elif(ui.comboBox_10.currentText() == 'USD' and ui.comboBox_9.currentText() == 'GBP'):
        result = float(value) / float(ui.label_74.text()) 
    elif(ui.comboBox_10.currentText() == 'USD' and ui.comboBox_9.currentText() == 'USD'):
        result = float(value) 
    elif(ui.comboBox_10.currentText() == 'EUR' and ui.comboBox_9.currentText() == 'RUB'):
        result = float(value) * float(ui.label_66.text())
    elif(ui.comboBox_10.currentText() == 'EUR' and ui.comboBox_9.currentText() == 'USD'):
        result = float(value) * float(ui.label_69.text())
    elif(ui.comboBox_10.currentText() == 'EUR' and ui.comboBox_9.currentText() == 'EUR'):
        result = float(value)
    elif(ui.comboBox_10.currentText() == 'EUR' and ui.comboBox_9.currentText() == 'GBP'):
        result = 'Не конвертируемо'
    elif(ui.comboBox_10.currentText() == 'RUB' and ui.comboBox_9.currentText() == 'USD'):
        result = float(value) / float(ui.label_67.text())
    elif(ui.comboBox_10.currentText() == 'RUB' and ui.comboBox_9.currentText() == 'EUR'):
        result = float(value) / float(ui.label_68.text())
    elif(ui.comboBox_10.currentText() == 'RUB' and ui.comboBox_9.currentText() == 'RUB'):
        result = float(value) 
    elif(ui.comboBox_10.currentText() == 'RUB'):
        result = 'Не конвертируемо'
    elif(ui.comboBox_10.currentText() == 'GBP' and ui.comboBox_9.currentText() == 'USD'):
        result = float(value) * float(ui.label_70.text())
    elif(ui.comboBox_10.currentText() == 'GBP'):
        result = 'Не конвертируемо'
    output = (result)      
    if(ui.lineEdit_19.text() != '' and sds.match(ui.lineEdit_19.text()) != None and  result != '' and result != 'Не конвертируемо'):
        if re.search(',', ui.lineEdit_19.text()):
            b = ui.lineEdit_19.text()
            rap = b.replace(',', '.')
            value1 = rap
        else:
            value1 = ui.lineEdit_19.text()
        if(float(value1) < 100):
            output = (result)
        else:    
            output = ("%.2f" % result)
    output = str(output)
    ui.lineEdit_20.setText(output)
    Timer(3.0, pro).start()
ui.lineEdit_19.textChanged.connect( pro )
ui.comboBox_9.currentTextChanged.connect( pro )
ui.comboBox_10.currentTextChanged.connect( pro )
Timer(3.0, pro).start()
# Ukr kurs
def ukr():
    if(ui.lineEdit_17.text() != '' and sds.match(ui.lineEdit_17.text()) != None or msd.match(ui.lineEdit_17.text()) != None or lsd.match(ui.lineEdit_17.text()) != None):
        if re.search(',', ui.lineEdit_17.text()):
            a = ui.lineEdit_17.text()
            rep = a.replace(',', '.')
            value = rep
        else:
            value = ui.lineEdit_17.text()
    else:
        value = 0        
    if(ui.comboBox_8.currentText() == 'USD' and ui.comboBox_7.currentText() == 'UAH'):
        result = float(value) * float(ui.label_43.text())    
    elif(ui.comboBox_8.currentText() == 'USD' and ui.comboBox_7.currentText() == 'USD'):
        result = float(value)   
    elif(ui.comboBox_8.currentText() == 'UAH' and ui.comboBox_7.currentText() == 'USD'):
        result = float(value) / float(ui.label_44.text())
    elif(ui.comboBox_8.currentText() == 'UAH' and ui.comboBox_7.currentText() == 'UAH'):
        result = float(value) / float(ui.label_44.text())
    output = (result)        
    if(ui.lineEdit_17.text() != '' and sds.match(ui.lineEdit_17.text()) != None and  result != '' and result != 'Не конвертируемо'):
        if re.search(',', ui.lineEdit_17.text()):
            b = ui.lineEdit_17.text()
            rap = b.replace(',', '.')
            value1 = rap
        else:
            value1 = ui.lineEdit_17.text()        
        if(float(value1) < 100):
            output = (result)
        else:    
            output = ("%.2f" % result)
    output = str(output)
    ui.lineEdit_18.setText(output)
    Timer(3.0, ukr).start()
ui.lineEdit_17.textChanged.connect( ukr )
ui.comboBox_8.currentTextChanged.connect( ukr )
ui.comboBox_7.currentTextChanged.connect( ukr )
Timer(3.0, ukr).start()
# agroprombunk
def agro():
    if(ui.lineEdit_15.text() != '' and sds.match(ui.lineEdit_15.text()) != None or msd.match(ui.lineEdit_15.text()) != None or lsd.match(ui.lineEdit_15.text()) != None):
        if re.search(',', ui.lineEdit_15.text()):
            a = ui.lineEdit_15.text()
            rep = a.replace(',', '.')
            value = rep
        else:
            value = ui.lineEdit_15.text()
    else:
        value = 0
    if(ui.comboBox_6.currentText() == 'USD' and ui.comboBox_5.currentText() == 'MDL'):
        result = float(value) * float(ui.label_17.text())                   
    elif(ui.comboBox_6.currentText() == 'USD' and ui.comboBox_5.currentText() == 'RUB'):
        result = float(value) * float(ui.label_19.text())                   
    elif(ui.comboBox_6.currentText() == 'USD' and ui.comboBox_5.currentText() == 'RUP'):
        result = float(value) * float(ui.label_55.text())                   
    elif(ui.comboBox_6.currentText() == 'USD' and ui.comboBox_5.currentText() == 'EUR'):
        result = float(value) * float(ui.label_22.text())                   
    elif(ui.comboBox_6.currentText() == 'USD' and ui.comboBox_5.currentText() == 'USD'):
        result = float(value)                   
    elif(ui.comboBox_6.currentText() == 'USD'):
        result = 'Не конвертируемо'                  
    elif(ui.comboBox_6.currentText() == 'EUR' and ui.comboBox_5.currentText() == 'USD'):
        result = float(value) / float(ui.label_21.text())              
    elif(ui.comboBox_6.currentText() == 'EUR' and ui.comboBox_5.currentText() == 'RUB'):
        result = float(value) * float(ui.label_23.text())              
    elif(ui.comboBox_6.currentText() == 'EUR' and ui.comboBox_5.currentText() == 'RUP'):
        result = float(value) * float(ui.label_57.text())              
    elif(ui.comboBox_6.currentText() == 'EUR' and ui.comboBox_5.currentText() == 'EUR'):
        result = float(value)               
    elif(ui.comboBox_6.currentText() == 'EUR'):
        result = 'Не конвертируемо'              
    elif(ui.comboBox_6.currentText() == 'MDL' and ui.comboBox_5.currentText() == 'RUP'):
        result = float(value) * float(ui.label_58.text())              
    elif(ui.comboBox_6.currentText() == 'MDL' and ui.comboBox_5.currentText() == 'USD'):
        result = float(value) / float(ui.label_18.text())              
    elif(ui.comboBox_6.currentText() == 'MDL' and ui.comboBox_5.currentText() == 'MDL'):
        result = float(value)               
    elif(ui.comboBox_6.currentText() == 'MDL'):
        result = 'Не конвертируемо'                 
    elif(ui.comboBox_6.currentText() == 'UAH' and ui.comboBox_5.currentText() == 'RUP'):
        result = float(value) * float(ui.label_59.text())              
    elif(ui.comboBox_6.currentText() == 'UAH' and ui.comboBox_5.currentText() == 'UAH'):
        result = float(value)           
    elif(ui.comboBox_6.currentText() == 'UAH'):
        result = 'Не конвертируемо'      
    elif(ui.comboBox_6.currentText() == 'RUB' and ui.comboBox_5.currentText() == 'USD'):
        result = float(value) / float(ui.label_20.text())              
    elif(ui.comboBox_6.currentText() == 'RUB' and ui.comboBox_5.currentText() == 'EUR'):
        result = float(value) / float(ui.label_24.text())              
    elif(ui.comboBox_6.currentText() == 'RUB' and ui.comboBox_5.currentText() == 'RUP'):
        result = float(value) * float(ui.label_60.text())              
    elif(ui.comboBox_6.currentText() == 'RUB' and ui.comboBox_5.currentText() == 'RUB'):
        result = float(value)         
    elif(ui.comboBox_6.currentText() == 'RUB'):
        result = 'Не конвертируемо'        
    elif(ui.comboBox_6.currentText() == 'RUP' and ui.comboBox_5.currentText() == 'USD'):
        result = float(value) / float(ui.label_56.text())              
    elif(ui.comboBox_6.currentText() == 'RUP' and ui.comboBox_5.currentText() == 'EUR'):
        result = float(value) / float(ui.label_61.text())              
    elif(ui.comboBox_6.currentText() == 'RUP' and ui.comboBox_5.currentText() == 'MDL'):
        result = float(value) / float(ui.label_62.text())              
    elif(ui.comboBox_6.currentText() == 'RUP' and ui.comboBox_5.currentText() == 'UAH'):
        result = float(value) / float(ui.label_63.text())              
    elif(ui.comboBox_6.currentText() == 'RUP' and ui.comboBox_5.currentText() == 'RUB'):
        result = float(value) / float(ui.label_64.text())              
    elif(ui.comboBox_6.currentText() == 'RUP' and ui.comboBox_5.currentText() == 'RUP'):
        result = float(value)
    output = (result)        
    if(ui.lineEdit_15.text() != '' and sds.match(ui.lineEdit_15.text()) != None and result != '' and result != 'Не конвертируемо'):
        if re.search(',', ui.lineEdit_15.text()):
            b = ui.lineEdit_15.text()
            rap = b.replace(',', '.')
            value1 = rap
        else:
            value1 = ui.lineEdit_15.text()            
        if(float(value1) < 100):
            output = (result)
        else:    
            output = ("%.2f" % result)
    output = str(output)        
    ui.lineEdit_16.setText(output)
    Timer(3.0, agro).start()
ui.lineEdit_15.textChanged.connect( agro )
ui.comboBox_6.currentTextChanged.connect( agro )
ui.comboBox_5.currentTextChanged.connect( agro )
Timer(3.0, agro).start()
# sberbunk
def sber():
    if(ui.lineEdit_13.text() != '' and sds.match(ui.lineEdit_13.text()) != None or msd.match(ui.lineEdit_13.text()) != None or lsd.match(ui.lineEdit_13.text()) != None):
        if re.search(',', ui.lineEdit_13.text()):
            a = ui.lineEdit_13.text()
            rep = a.replace(',', '.')
            value = rep
        else:
            value = ui.lineEdit_13.text()
    else:
        value = 0
    if(ui.comboBox_4.currentText() == 'USD' and ui.comboBox_3.currentText() == 'RUB'):
        result = float(value) * float(ui.label_51.text())    
    elif(ui.comboBox_4.currentText() == 'USD' and ui.comboBox_3.currentText() == 'EUR'):
        result = 'Не конвертируемо'                   
    elif(ui.comboBox_4.currentText() == 'USD' and ui.comboBox_3.currentText() == 'USD'):
        result = float(value)    
    elif(ui.comboBox_4.currentText() == 'EUR' and ui.comboBox_3.currentText() == 'RUB'):
        result = float(value) * float(ui.label_52.text())   
    elif(ui.comboBox_4.currentText() == 'EUR' and ui.comboBox_3.currentText() == 'USD'):
        result = 'Не конвертируемо'                       
    elif(ui.comboBox_4.currentText() == 'EUR' and ui.comboBox_3.currentText() == 'EUR'):
        result = float(value)    
    elif(ui.comboBox_4.currentText() == 'RUB' and ui.comboBox_3.currentText() == 'USD'):
        result = float(value) / float(ui.label_53.text())                   
    elif(ui.comboBox_4.currentText() == 'RUB' and ui.comboBox_3.currentText() == 'EUR'):
        result = float(value) * float(ui.label_54.text())                   
    elif(ui.comboBox_4.currentText() == 'RUB' and ui.comboBox_3.currentText() == 'RUB'):
        result = float(value)
    output = (result)        
    if(ui.lineEdit_13.text() != '' and sds.match(ui.lineEdit_13.text()) != None and result != '' and result != 'Не конвертируемо'):
        if re.search(',', ui.lineEdit_13.text()):
            b = ui.lineEdit_13.text()
            rap = b.replace(',', '.')
            value1 = rap
        else:
            value1 = ui.lineEdit_13.text()            
        if(float(value1) < 100):
            output = (result)
        else:    
            output = ("%.2f" % result)
    output = str(output)        
    ui.lineEdit_14.setText(output)
    Timer(3.0, sber).start()
ui.lineEdit_13.textChanged.connect( sber )
ui.comboBox_4.currentTextChanged.connect( sber )
ui.comboBox_3.currentTextChanged.connect( sber )
Timer(3.0, sber).start()
# my own course
def own():
    if(ui.lineEdit_11.text() != '' and sds.match(ui.lineEdit_11.text()) != None or msd.match(ui.lineEdit_11.text()) != None or lsd.match(ui.lineEdit_11.text()) != None):
        if re.search(',', ui.lineEdit_11.text()):
            a = ui.lineEdit_11.text()
            rep = a.replace(',', '.')
            value = rep
        else:
            value = ui.lineEdit_11.text()
    else:
        value = 0
    if(ui.comboBox.currentText() == 'USD' and ui.comboBox_2.currentText() == 'RUP'):
        if(ui.lineEdit.text() != '' and sds.match(ui.lineEdit.text()) != None or msd.match(ui.lineEdit.text()) != None or lsd.match(ui.lineEdit.text()) != None):
            if re.search(',', ui.lineEdit.text()):
                a = ui.lineEdit.text()
                rep = a.replace(',', '.')
                value1 = rep
                result = float(value) * float(value1)
            else:
                value = ui.lineEdit.text()            
        else:
            result = 0     
    elif(ui.comboBox.currentText() == 'USD' and ui.comboBox_2.currentText() == 'EUR'):
        if(ui.lineEdit.text() != '' and sds.match(ui.lineEdit.text()) != None or msd.match(ui.lineEdit.text()) != None or lsd.match(ui.lineEdit.text()) != None 
        and
           ui.lineEdit_4.text() != '' and sds.match(ui.lineEdit_4.text()) != None or msd.match(ui.lineEdit_4.text()) != None or lsd.match(ui.lineEdit_4.text()) != None
        ):
            if (re.search(',', ui.lineEdit.text()) or re.search(',', ui.lineEdit_4.text())):
                a = ui.lineEdit.text()
                b = ui.lineEdit_4.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(rep1)
            else:
                value = (ui.lineEdit.text()/ui.lineEdit_4.text())            
        else:
            result = 0
    elif(ui.comboBox.currentText() == 'USD' and ui.comboBox_2.currentText() == 'MDL'):
        if(ui.lineEdit.text() != '' and sds.match(ui.lineEdit.text()) != None or msd.match(ui.lineEdit.text()) != None or lsd.match(ui.lineEdit.text()) != None 
        and
           ui.lineEdit_6.text() != '' and sds.match(ui.lineEdit_6.text()) != None or msd.match(ui.lineEdit_6.text()) != None or lsd.match(ui.lineEdit_6.text()) != None
        ):
            if (re.search(',', ui.lineEdit.text()) or re.search(',', ui.lineEdit_6.text())):
                a = ui.lineEdit.text()
                b = ui.lineEdit_6.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) * float(rep1)
            else:
                value = (ui.lineEdit.text()*ui.lineEdit_6.text())            
        else:
            result = 0     
    elif(ui.comboBox.currentText() == 'USD' and ui.comboBox_2.currentText() == 'RUB'):
        if(ui.lineEdit.text() != '' and sds.match(ui.lineEdit.text()) != None or msd.match(ui.lineEdit.text()) != None or lsd.match(ui.lineEdit.text()) != None 
        and
           ui.lineEdit_8.text() != '' and sds.match(ui.lineEdit_8.text()) != None or msd.match(ui.lineEdit_8.text()) != None or lsd.match(ui.lineEdit_8.text()) != None
        ):
            if (re.search(',', ui.lineEdit.text()) or re.search(',', ui.lineEdit_8.text())):
                a = ui.lineEdit.text()
                b = ui.lineEdit_8.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(rep1)
            else:
                value = (ui.lineEdit.text()/ui.lineEdit_8.text())            
        else:
            result = 0    
    elif(ui.comboBox.currentText() == 'USD' and ui.comboBox_2.currentText() == 'UAH'):
        if(ui.lineEdit.text() != '' and sds.match(ui.lineEdit.text()) != None or msd.match(ui.lineEdit.text()) != None or lsd.match(ui.lineEdit.text()) != None 
        and
           ui.lineEdit_10.text() != '' and sds.match(ui.lineEdit_10.text()) != None or msd.match(ui.lineEdit_10.text()) != None or lsd.match(ui.lineEdit_10.text()) != None
        ):
            if (re.search(',', ui.lineEdit.text()) or re.search(',', ui.lineEdit_10.text())):
                a = ui.lineEdit.text()
                b = ui.lineEdit_10.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(rep1)
            else:
                value = (ui.lineEdit.text()/ui.lineEdit_10.text())            
        else:
            result = 0                                                                                      
    elif(ui.comboBox.currentText() == 'USD' and ui.comboBox_2.currentText() == 'USD'):
        result = float(value)        
    elif(ui.comboBox.currentText() == 'USD'):
        result = 'Не конвертируемо'        
    elif(ui.comboBox.currentText() == 'EUR' and ui.comboBox_2.currentText() == 'RUP'):
        if(ui.lineEdit_3.text() != '' and sds.match(ui.lineEdit_3.text()) != None or msd.match(ui.lineEdit_3.text()) != None or lsd.match(ui.lineEdit_3.text()) != None):
            if re.search(',', ui.lineEdit_3.text()):
                a = ui.lineEdit_3.text()
                rep = a.replace(',', '.')
                value1 = rep
                result = float(value) * float(value1)           
            else:
                value = ui.lineEdit_3.text()                 
        else:
            result = 0  
    elif(ui.comboBox.currentText() == 'EUR' and ui.comboBox_2.currentText() == 'USD'):
        if(ui.lineEdit_3.text() != '' and sds.match(ui.lineEdit_3.text()) != None or msd.match(ui.lineEdit_3.text()) != None or lsd.match(ui.lineEdit_3.text()) != None 
        and
           ui.lineEdit_2.text() != '' and sds.match(ui.lineEdit_2.text()) != None or msd.match(ui.lineEdit_2.text()) != None or lsd.match(ui.lineEdit_2.text()) != None
        ):
            if (re.search(',', ui.lineEdit_3.text()) or re.search(',', ui.lineEdit_2.text())):
                a = ui.lineEdit_3.text()
                b = ui.lineEdit_2.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(rep1)
            else:
                value = (float(ui.lineEdit_3.text())/float(ui.lineEdit_2.text()))            
        else:
            result = 0      
    elif(ui.comboBox.currentText() == 'EUR' and ui.comboBox_2.currentText() == 'MDL'):
        if(ui.lineEdit_3.text() != '' and sds.match(ui.lineEdit_3.text()) != None or msd.match(ui.lineEdit_3.text()) != None or lsd.match(ui.lineEdit_3.text()) != None 
        and
           ui.lineEdit_6.text() != '' and sds.match(ui.lineEdit_6.text()) != None or msd.match(ui.lineEdit_6.text()) != None or lsd.match(ui.lineEdit_6.text()) != None
        ):
            if (re.search(',', ui.lineEdit_3.text()) or re.search(',', ui.lineEdit_6.text())):
                a = ui.lineEdit_3.text()
                b = ui.lineEdit_6.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) * float(rep1)
            else:
                value = (ui.lineEdit_3.text()*ui.lineEdit_6.text())            
        else:
            result = 0      
    elif(ui.comboBox.currentText() == 'EUR' and ui.comboBox_2.currentText() == 'RUB'):
        if(ui.lineEdit_3.text() != '' and sds.match(ui.lineEdit_3.text()) != None or msd.match(ui.lineEdit_3.text()) != None or lsd.match(ui.lineEdit_3.text()) != None 
        and
           ui.lineEdit_8.text() != '' and sds.match(ui.lineEdit_8.text()) != None or msd.match(ui.lineEdit_8.text()) != None or lsd.match(ui.lineEdit_8.text()) != None
        ):
            if (re.search(',', ui.lineEdit_3.text()) or re.search(',', ui.lineEdit_8.text())):
                a = ui.lineEdit_3.text()
                b = ui.lineEdit_8.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(rep1)
            else:
                value = (ui.lineEdit_3.text()/ui.lineEdit_8.text())            
        else:
            result = 0      
    elif(ui.comboBox.currentText() == 'EUR' and ui.comboBox_2.currentText() == 'UAH'):
        if(ui.lineEdit_3.text() != '' and sds.match(ui.lineEdit_3.text()) != None or msd.match(ui.lineEdit_3.text()) != None or lsd.match(ui.lineEdit_3.text()) != None 
        and
           ui.lineEdit_10.text() != '' and sds.match(ui.lineEdit_10.text()) != None or msd.match(ui.lineEdit_10.text()) != None or lsd.match(ui.lineEdit_10.text()) != None
        ):
            if (re.search(',', ui.lineEdit_3.text()) or re.search(',', ui.lineEdit_10.text())):
                a = ui.lineEdit_3.text()
                b = ui.lineEdit_10.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(rep1)
            else:
                value = (ui.lineEdit_3.text()/ui.lineEdit_10.text())            
        else:
            result = 0                                                                    
    elif(ui.comboBox.currentText() == 'EUR' and ui.comboBox_2.currentText() == 'EUR'):
        result = float(value)                  
    elif(ui.comboBox.currentText() == 'EUR'):
        result = 'Не конвертируемо'                        
    elif(ui.comboBox.currentText() == 'MDL' and ui.comboBox_2.currentText() == 'RUP'):
        if(ui.lineEdit_5.text() != '' and sds.match(ui.lineEdit_5.text()) != None or msd.match(ui.lineEdit_5.text()) != None or lsd.match(ui.lineEdit_5.text()) != None):
            if re.search(',', ui.lineEdit_5.text()):
                a = ui.lineEdit_5.text()
                rep = a.replace(',', '.')
                value1 = rep
                result = float(value) * float(value1)           
            else:
                value = ui.lineEdit_5.text()                 
        else:
            result = 0 
    elif(ui.comboBox.currentText() == 'MDL' and ui.comboBox_2.currentText() == 'USD'):
        if(ui.lineEdit_5.text() != '' and sds.match(ui.lineEdit_5.text()) != None or msd.match(ui.lineEdit_5.text()) != None or lsd.match(ui.lineEdit_5.text()) != None 
        and
           ui.lineEdit_2.text() != '' and sds.match(ui.lineEdit_2.text()) != None or msd.match(ui.lineEdit_2.text()) != None or lsd.match(ui.lineEdit_2.text()) != None
        ):
            if (re.search(',', ui.lineEdit_5.text()) or re.search(',', ui.lineEdit_2.text())):
                a = ui.lineEdit_5.text()
                b = ui.lineEdit_2.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(rep1)
            else:
                value = (ui.lineEdit_5.text()/ui.lineEdit_2.text())            
        else:
            result = 0     
    elif(ui.comboBox.currentText() == 'MDL' and ui.comboBox_2.currentText() == 'EUR'):
        if(ui.lineEdit_5.text() != '' and sds.match(ui.lineEdit_5.text()) != None or msd.match(ui.lineEdit_5.text()) != None or lsd.match(ui.lineEdit_5.text()) != None 
        and
           ui.lineEdit_4.text() != '' and sds.match(ui.lineEdit_4.text()) != None or msd.match(ui.lineEdit_4.text()) != None or lsd.match(ui.lineEdit_4.text()) != None
        ):
            if (re.search(',', ui.lineEdit_5.text()) or re.search(',', ui.lineEdit_4.text())):
                a = ui.lineEdit_5.text()
                b = ui.lineEdit_4.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(rep1)
            else:
                value = (ui.lineEdit_5.text()/ui.lineEdit_4.text())            
        else:
            result = 0      
    elif(ui.comboBox.currentText() == 'MDL' and ui.comboBox_2.currentText() == 'RUB'):
        if(ui.lineEdit_5.text() != '' and sds.match(ui.lineEdit_5.text()) != None or msd.match(ui.lineEdit_5.text()) != None or lsd.match(ui.lineEdit_5.text()) != None 
        and
           ui.lineEdit_8.text() != '' and sds.match(ui.lineEdit_8.text()) != None or msd.match(ui.lineEdit_8.text()) != None or lsd.match(ui.lineEdit_8.text()) != None
        ):
            if (re.search(',', ui.lineEdit_5.text()) or re.search(',', ui.lineEdit_8.text())):
                a = ui.lineEdit_5.text()
                b = ui.lineEdit_8.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(rep1)
            else:
                value = (ui.lineEdit_5.text()/ui.lineEdit_8.text())            
        else:
            result = 0    
    elif(ui.comboBox.currentText() == 'MDL' and ui.comboBox_2.currentText() == 'UAH'):
        if(ui.lineEdit_5.text() != '' and sds.match(ui.lineEdit_5.text()) != None or msd.match(ui.lineEdit_5.text()) != None or lsd.match(ui.lineEdit_5.text()) != None 
        and
           ui.lineEdit_10.text() != '' and sds.match(ui.lineEdit_10.text()) != None or msd.match(ui.lineEdit_10.text()) != None or lsd.match(ui.lineEdit_10.text()) != None
        ):
            if (re.search(',', ui.lineEdit_5.text()) or re.search(',', ui.lineEdit_10.text())):
                a = ui.lineEdit_5.text()
                b = ui.lineEdit_10.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(rep1)
            else:
                value = (ui.lineEdit_5.text()/ui.lineEdit_10.text())            
        else:
            result = 0                                               
    elif(ui.comboBox.currentText() == 'MDL' and ui.comboBox_2.currentText() == 'MDL'):
        result = float(value)                             
    elif(ui.comboBox.currentText() == 'MDL'):
        result = 'Не конвертируемо'             
    elif(ui.comboBox.currentText() == 'RUB' and ui.comboBox_2.currentText() == 'RUP'):
        if(ui.lineEdit_7.text() != '' and sds.match(ui.lineEdit_7.text()) != None or msd.match(ui.lineEdit_7.text()) != None or lsd.match(ui.lineEdit_7.text()) != None):
            if re.search(',', ui.lineEdit_7.text()):
                a = ui.lineEdit_7.text()
                rep = a.replace(',', '.')
                value1 = rep
                result = float(value) * float(value1)                                  
            else:
                value = ui.lineEdit_7.text()     
        else:
            result = 0
    elif(ui.comboBox.currentText() == 'RUB' and ui.comboBox_2.currentText() == 'USD'):
        if(ui.lineEdit_7.text() != '' and sds.match(ui.lineEdit_7.text()) != None or msd.match(ui.lineEdit_7.text()) != None or lsd.match(ui.lineEdit_7.text()) != None 
        and
           ui.lineEdit_2.text() != '' and sds.match(ui.lineEdit_2.text()) != None or msd.match(ui.lineEdit_2.text()) != None or lsd.match(ui.lineEdit_2.text()) != None
        ):
            if (re.search(',', ui.lineEdit_7.text()) or re.search(',', ui.lineEdit_2.text())):
                a = ui.lineEdit_7.text()
                b = ui.lineEdit_2.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(value2)
            else:
                value = (ui.lineEdit_7.text()/ui.lineEdit_2.text())            
        else:
            result = 0          
    elif(ui.comboBox.currentText() == 'RUB' and ui.comboBox_2.currentText() == 'EUR'):
        if(ui.lineEdit_7.text() != '' and sds.match(ui.lineEdit_7.text()) != None or msd.match(ui.lineEdit_7.text()) != None or lsd.match(ui.lineEdit_7.text()) != None 
        and
           ui.lineEdit_4.text() != '' and sds.match(ui.lineEdit_4.text()) != None or msd.match(ui.lineEdit_4.text()) != None or lsd.match(ui.lineEdit_4.text()) != None
        ):
            if (re.search(',', ui.lineEdit_7.text()) or re.search(',', ui.lineEdit_4.text())):
                a = ui.lineEdit_7.text()
                b = ui.lineEdit_4.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(value2)
            else:
                value = (ui.lineEdit_7.text()/ui.lineEdit_4.text())            
        else:
            result = 0     
    elif(ui.comboBox.currentText() == 'RUB' and ui.comboBox_2.currentText() == 'MDL'):
        if(ui.lineEdit_7.text() != '' and sds.match(ui.lineEdit_7.text()) != None or msd.match(ui.lineEdit_7.text()) != None or lsd.match(ui.lineEdit_7.text()) != None 
        and
           ui.lineEdit_6.text() != '' and sds.match(ui.lineEdit_6.text()) != None or msd.match(ui.lineEdit_6.text()) != None or lsd.match(ui.lineEdit_6.text()) != None
        ):
            if (re.search(',', ui.lineEdit_7.text()) or re.search(',', ui.lineEdit_6.text())):
                a = ui.lineEdit_7.text()
                b = ui.lineEdit_6.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) * float(rep1)
            else:
                value = (ui.lineEdit_7.text()*ui.lineEdit_6.text())            
        else:
            result = 0      
    elif(ui.comboBox.currentText() == 'RUB' and ui.comboBox_2.currentText() == 'UAH'):
        if(ui.lineEdit_7.text() != '' and sds.match(ui.lineEdit_7.text()) != None or msd.match(ui.lineEdit_7.text()) != None or lsd.match(ui.lineEdit_7.text()) != None 
        and
           ui.lineEdit_10.text() != '' and sds.match(ui.lineEdit_10.text()) != None or msd.match(ui.lineEdit_10.text()) != None or lsd.match(ui.lineEdit_10.text()) != None
        ):
            if (re.search(',', ui.lineEdit_7.text()) or re.search(',', ui.lineEdit_10.text())):
                a = ui.lineEdit_7.text()
                b = ui.lineEdit_10.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(rep1)
            else:
                value = (ui.lineEdit_7.text()/ui.lineEdit_10.text())            
        else:
            result = 0                                                                                
    elif(ui.comboBox.currentText() == 'RUB' and ui.comboBox_2.currentText() == 'RUB'):
        result = float(value)                                                 
    elif(ui.comboBox.currentText() == 'RUB'):
        result = 'Не конвертируемо'                
    elif(ui.comboBox.currentText() == 'UAH' and ui.comboBox_2.currentText() == 'RUP'):
        if(ui.lineEdit_9.text() != '' and sds.match(ui.lineEdit_9.text()) != None or msd.match(ui.lineEdit_9.text()) != None or lsd.match(ui.lineEdit_9.text()) != None):
            if re.search(',', ui.lineEdit_9.text()):
                a = ui.lineEdit_9.text()
                rep = a.replace(',', '.')
                value1 = rep
                result = float(value) * float(value1)                                                              
            else:
                value = ui.lineEdit_9.text()     
        else:
            result = 0  
    elif(ui.comboBox.currentText() == 'UAH' and ui.comboBox_2.currentText() == 'USD'):
        if(ui.lineEdit_9.text() != '' and sds.match(ui.lineEdit_9.text()) != None or msd.match(ui.lineEdit_9.text()) != None or lsd.match(ui.lineEdit_9.text()) != None 
        and
           ui.lineEdit_2.text() != '' and sds.match(ui.lineEdit_2.text()) != None or msd.match(ui.lineEdit_2.text()) != None or lsd.match(ui.lineEdit_2.text()) != None
        ):
            if (re.search(',', ui.lineEdit_9.text()) or re.search(',', ui.lineEdit_2.text())):
                a = ui.lineEdit_9.text()
                b = ui.lineEdit_2.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(rep1)
            else:
                value = (ui.lineEdit_9.text()/ui.lineEdit_2.text())            
        else:
            result = 0       
    elif(ui.comboBox.currentText() == 'UAH' and ui.comboBox_2.currentText() == 'EUR'):
        if(ui.lineEdit_9.text() != '' and sds.match(ui.lineEdit_9.text()) != None or msd.match(ui.lineEdit_9.text()) != None or lsd.match(ui.lineEdit_9.text()) != None 
        and
           ui.lineEdit_4.text() != '' and sds.match(ui.lineEdit_4.text()) != None or msd.match(ui.lineEdit_4.text()) != None or lsd.match(ui.lineEdit_4.text()) != None
        ):
            if (re.search(',', ui.lineEdit_9.text()) or re.search(',', ui.lineEdit_4.text())):
                a = ui.lineEdit_9.text()
                b = ui.lineEdit_4.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(rep1)
            else:
                value = (ui.lineEdit_9.text()/ui.lineEdit_4.text())            
        else:
            result = 0        
    elif(ui.comboBox.currentText() == 'UAH' and ui.comboBox_2.currentText() == 'MDL'):
        if(ui.lineEdit_9.text() != '' and sds.match(ui.lineEdit_9.text()) != None or msd.match(ui.lineEdit_9.text()) != None or lsd.match(ui.lineEdit_9.text()) != None 
        and
           ui.lineEdit_6.text() != '' and sds.match(ui.lineEdit_6.text()) != None or msd.match(ui.lineEdit_6.text()) != None or lsd.match(ui.lineEdit_6.text()) != None
        ):
            if (re.search(',', ui.lineEdit_9.text()) or re.search(',', ui.lineEdit_6.text())):
                a = ui.lineEdit_9.text()
                b = ui.lineEdit_6.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) * float(rep1)
            else:
                value = (ui.lineEdit_9.text()*ui.lineEdit_6.text())            
        else:
            result = 0    
    elif(ui.comboBox.currentText() == 'UAH' and ui.comboBox_2.currentText() == 'RUB'):
        if(ui.lineEdit_9.text() != '' and sds.match(ui.lineEdit_9.text()) != None or msd.match(ui.lineEdit_9.text()) != None or lsd.match(ui.lineEdit_9.text()) != None 
        and
           ui.lineEdit_8.text() != '' and sds.match(ui.lineEdit_8.text()) != None or msd.match(ui.lineEdit_8.text()) != None or lsd.match(ui.lineEdit_8.text()) != None
        ):
            if (re.search(',', ui.lineEdit_9.text()) or re.search(',', ui.lineEdit_8.text())):
                a = ui.lineEdit_9.text()
                b = ui.lineEdit_8.text()
                rep = a.replace(',', '.')
                rep1 = b.replace(',', '.')
                value1 = rep
                value2 = rep1
                result = float(value) * float(value1) / float(rep1)
            else:
                value = (ui.lineEdit_9.text()/ui.lineEdit_8.text())            
        else:
            result = 0                                                                
    elif(ui.comboBox.currentText() == 'UAH' and ui.comboBox_2.currentText() == 'UAH'):
        result = float(value)                                                            
    elif(ui.comboBox.currentText() == 'UAH'):
        result = 'Не конвертируемо'              
    elif(ui.comboBox.currentText() == 'RUP' and ui.comboBox_2.currentText() == 'USD'):
        if(ui.lineEdit_2.text() != '' and sds.match(ui.lineEdit_2.text()) != None or msd.match(ui.lineEdit_2.text()) != None or lsd.match(ui.lineEdit_2.text()) != None):
            if re.search(',', ui.lineEdit_2.text()):
                a = ui.lineEdit_2.text()
                rep = a.replace(',', '.')
                value1 = rep
                result = float(value) / float(value1)                                                             
            else:
                value = ui.lineEdit_2.text()     
        else:
            result = 0  
    elif(ui.comboBox.currentText() == 'RUP' and ui.comboBox_2.currentText() == 'EUR'):
        if(ui.lineEdit_4.text() != '' and sds.match(ui.lineEdit_4.text()) != None or msd.match(ui.lineEdit_4.text()) != None or lsd.match(ui.lineEdit_4.text()) != None):
            if re.search(',', ui.lineEdit_4.text()):
                a = ui.lineEdit_4.text()
                rep = a.replace(',', '.')
                value1 = rep
                result = float(value) / float(value1)                                                                      
            else:
                value = ui.lineEdit_4.text()     
        else:
            result = 0  
    elif(ui.comboBox.currentText() == 'RUP' and ui.comboBox_2.currentText() == 'MDL'):
        if(ui.lineEdit_6.text() != '' and sds.match(ui.lineEdit_6.text()) != None or msd.match(ui.lineEdit_6.text()) != None or lsd.match(ui.lineEdit_6.text()) != None):
            if re.search(',', ui.lineEdit_6.text()):
                a = ui.lineEdit_6.text()
                rep = a.replace(',', '.')
                value1 = rep
                result = float(value) * float(value1)                                                                      
            else:
                value = ui.lineEdit_6.text()     
        else:
            result = 0  
    elif(ui.comboBox.currentText() == 'RUP' and ui.comboBox_2.currentText() == 'RUB'):
        if(ui.lineEdit_8.text() != '' and sds.match(ui.lineEdit_8.text()) != None or msd.match(ui.lineEdit_8.text()) != None or lsd.match(ui.lineEdit_8.text()) != None):
            if re.search(',', ui.lineEdit_8.text()):
                a = ui.lineEdit_8.text()
                rep = a.replace(',', '.')
                value1 = rep
                result = float(value) * float(value1)                                                                               
            else:
                value = ui.lineEdit_8.text()     
        else:
            result = 0  
    elif(ui.comboBox.currentText() == 'RUP' and ui.comboBox_2.currentText() == 'UAH'):
        if(ui.lineEdit_10.text() != '' and sds.match(ui.lineEdit_10.text()) != None or msd.match(ui.lineEdit_10.text()) != None or lsd.match(ui.lineEdit_10.text()) != None):
            if re.search(',', ui.lineEdit_10.text()):
                a = ui.lineEdit_10.text()
                rep = a.replace(',', '.')
                value1 = rep
                result = float(value) * float(value1)                                                                       
            else:
                value = ui.lineEdit_10.text()     
        else:
            result = 0  
    elif(ui.comboBox.currentText() == 'RUP' and ui.comboBox_2.currentText() == 'RUP'):
        result = float(value)                                                                                    
    output = (result)        
    if(ui.lineEdit_11.text() != '' and sds.match(ui.lineEdit_11.text()) != None and result != '' and result != 'Не конвертируемо'):
        if re.search(',', ui.lineEdit_11.text()):
            b = ui.lineEdit_11.text()
            rap = b.replace(',', '.')
            value1 = rap
        else:
            value1 = ui.lineEdit_11.text()            
        if(float(value1) < 100):
            output = (result)
        else:    
            output = ("%.2f" % result)
    output = str(output)               
    ui.lineEdit_12.setText(output)
ui.lineEdit_11.textChanged.connect( own )
ui.comboBox.currentTextChanged.connect( own )
ui.comboBox_2.currentTextChanged.connect( own )

ui.lineEdit.textChanged.connect( own )
ui.lineEdit_2.textChanged.connect( own )
ui.lineEdit_3.textChanged.connect( own )
ui.lineEdit_4.textChanged.connect( own )
ui.lineEdit_5.textChanged.connect( own )
ui.lineEdit_6.textChanged.connect( own )
ui.lineEdit_7.textChanged.connect( own )
ui.lineEdit_8.textChanged.connect( own )
ui.lineEdit_9.textChanged.connect( own )
ui.lineEdit_10.textChanged.connect( own )
# Main loop
sys.exit(app.exec_())