#======================================================
# -*- coding: utf-8 -*-
#---> Created by : Keerthik Shetty
#---> Test Case ID : 
#---> Test Case Name : 
#---> Creation Date : 
#======================================================
source(findFile('scripts', '../../../globalScripts/liveScreen.py'))
source(findFile('scripts', '../../globalScripts/evaluationScreen.py'))
source(findFile('scripts', '../../globalScripts/patientListScreen.py'))
source(findFile('scripts', '../../../globalScripts/launch.py'))
source(findFile('scripts', '../../../globalScripts/menuScreen.py'))
source(findFile('scripts', '../../../globalScripts/menuPatientCard.py'))
source(findFile('scripts', '../../../globalScripts/commonMethods.py'))
source(findFile('scripts', '../../../globalScripts/settingsScreen.py'))
source(findFile('scripts', '../../../globalScripts/summaryScreen.py'))
source(findFile('scripts', '../../../globalScripts/users.py'))



resultsDictionary = {}
testData=getTestDataFromFile()

customComboBoxId={"container": mainWindow, "id": "customComboBoxId", "type": "CustomComboBox", "unnamed": 1, "visible": True}        
EnglishlangID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "type": "ItemDelegate", "unnamed": 1, "visible": True}
czechlanID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 2, "type": "ItemDelegate", "unnamed": 1, "visible": True}
PolishLangID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 3, "type": "ItemDelegate", "unnamed": 1, "visible": True}
RomaninaLangID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 4, "type": "ItemDelegate", "unnamed": 1, "visible": True}
ChineseTradlangID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 5, "type": "ItemDelegate", "unnamed": 1, "visible": True}
CrotianLangID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 6, "type": "ItemDelegate", "unnamed": 1, "visible": True}
FrenchLangID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 7, "type": "ItemDelegate", "unnamed": 1, "visible": True}
GermanLangID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 8, "type": "ItemDelegate", "unnamed": 1, "visible": True}
HurgerianID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 9, "type": "ItemDelegate", "unnamed": 1, "visible": True}
ItalainlnagID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 10, "type": "ItemDelegate", "unnamed": 1, "visible": True}
PortugueseLangID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 11, "type": "ItemDelegate", "unnamed": 1, "visible": True}
RussianlangID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 12, "type": "ItemDelegate", "unnamed": 1, "visible": True}
SpanishlanID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 13, "type": "ItemDelegate", "unnamed": 1, "visible": True}
TurkishLangID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 14, "type": "ItemDelegate", "unnamed": 1, "visible": True}
VietameselangID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 15, "type": "ItemDelegate", "unnamed": 1, "visible": True}

#BTLworkflowID's
BTLworkflowRecordandevaluavteID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "type": "ItemDelegate", "unnamed": 1, "visible": True}

#Primary ID
PrimaryusedIDPID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "type": "ItemDelegate", "unnamed": 1, "visible": True}


Language='Tiếng Việt'
Settings='Cài đặt'
Recording='Recording'
PrimaryusedID='ID beệnh nhân'
BTLworkflow='Ghi - Đánh giá'

def main():
    global list1
    list1=[]
    try:
        if Language_Validation():
            test.log("Successfully collected all the text from {} language".format(Language))
            test.log('Total strings collected in {} language = {} '.format(Language,len(list1)))
        else:
            test.log("Failed to collect all the text from {} language".format(Language))
            test.log('Total strings in {} language= {} '.format(Language,len(list1)))       
    except Exception as e:
        test.log('exception'+str(e)) 
        
def Language_Validation():
        status='fail'
        snooze(2)
        if launchApplication():
            test.log("Application Launched successfully")
        else:
            test.log('Application not launched successfully')  
        
# Step1 :Factory reset to collect strings
        step1=factoryRestCreateDefaultUser()
        snooze(2)
 
# Step2 : Set Language in settings and verify whether set language is applied in device        
        step2=selectLanguageinSettingsandVerifyWorkaroundmethod(VietameselangID,Settings,Recording,PrimaryusedIDPID,BTLworkflowRecordandevaluavteID)
        snooze(2)
        
        if step2:
            test.passes('{} language Successfully set'.format(Language))
#Step 3 :Common method to collect all the text
            step3=allScreenTextCollectionMethod()
            snooze(1)
        else:
            test.fail('{} language Not set Successfully'.format(Language))

        if step2 and step3:
            status='pass'
        else:
            status='fail'
            
        return True if status=='pass' else False
        