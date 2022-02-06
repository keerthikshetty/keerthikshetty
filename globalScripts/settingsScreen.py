'''Objects of main window'''

mainWindow = {"type": "QQuickWindowQmlImpl", "visible": True}
monitorScreen_MainWindow = {"container": mainWindow, "id": "manualInput", "type": "ManualInputPopup",  "visible": True}
evaluationScreen_MainWindow = {"container": mainWindow, "id": "evaluationScreenId", "type": "EvalScreen", "visible": True}
menuScreen_MainWindow = {"container": mainWindow, "id": "menuScreenId", "type": "Rectangle", "visible": True}
patientCardScreen_MainWindow = {"container": mainWindow, "id": "patientScreenId", "type": "PatientCard",  "visible": True}
liveSettingsScreen_MainWindow = {"container": mainWindow,  "type": "Rectangle", "visible": True}
livePatientList_MainWindow = {"container": mainWindow, "id": "centreRectId", "type": "Rectangle", "visible": True}
settingsScreen_Mainindow = {"container": mainWindow, "id": "deviceSettingsScreenId", "type": "DeviceSettingsScreen", "unnamed": 1, "visible": True}


backButton = {"container": settingsScreen_Mainindow, "id": "headerItemId", "type": "Item", "unnamed": 1, "visible": True}
deviceSettingsBackButtonId = {"container": mainWindow, "id": "deviceSettingsBackButtonId", "type": "Button",  "visible": True}
menuSettingsButton = {"checkable": False, "container": mainWindow, "id": "menuSettingsButtonId", "type": "CircularButton", "visible": True}
networkButtonInsettingsScreen = {"checkable": True, "container": mainWindow, "id": "networkSettingsButtonId", "type": "RectangularRadioButton",  "visible": True}
systemSettingsButtonInsettingsScreen = {"checkable": True, "container": mainWindow, "id": "systemSettingsButtonId", "type": "RectangularRadioButton",  "visible": True}
profileSettingsButtonInsettingsScreen = {"checkable": True, "container": settingsScreen_Mainindow, "id": "profilesSettingsButtonId", "type": "RectangularRadioButton",  "visible": True}
printSettingsButtonInsettingsScreen = {"checkable": True, "container": mainWindow, "id": "printSettingsButtonId", "type": "RectangularRadioButton",  "visible": True}
patientCardSettingsButtonInsettingsScreen = {"checkable": True, "container": mainWindow, "id": "patientCardSettingsButtonId", "type": "RectangularRadioButton",  "visible": True}
deviceInfoButtonInSettingsScreen = {"checkable": True, "container": mainWindow, "id": "deviceInfoButtonId", "type": "RectangularRadioButton", "visible": True}
generalButtonInSettingScreen = {"checkable": True, "container": mainWindow, "id": "systemSettingsButtonId", "type": "RectangularRadioButton", "visible": True}
exportButtonInSettingScreen = {"checkable": True, "container": mainWindow, "id": "exportSettingsButtonId", "type": "RectangularRadioButton", "visible": True}
serviceButtonInSettingsScreen = {"checkable": True, "container": mainWindow, "id": "servicePageButtonId", "type": "RectangularRadioButton", "visible": True}
profilesSettingsButtonId = {"container": mainWindow, "id": "profilesSettingsButtonId", "type": "RectangularRadioButton",  "visible": True}
autoProfileInSettingsScreen = {"container": settingsScreen_Mainindow, "id": "autoProfilesId", "type": "ProfilePageAuto", "unnamed": 1, "visible": True}
manualProfileInSettingsScreen = {"container": settingsScreen_Mainindow, "text": "Manual", "type": "Label",  "visible": True}
rhythmProfileInSettingScreen = {"checkable": True, "container": settingsScreen_Mainindow, "text": "Rhythm", "type": "RectangularRadioButton", "visible": True}
adaptiveWorkflowSelection = {"container": settingsScreen_Mainindow, "id": "adaptiveWorklflowSelectionId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
durationSelection = {"container": settingsScreen_Mainindow, "id": "durationSelectionId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
durationSelectionId = {"container": mainWindow, "id": "durationSelectionId", "type": "CustomComboBoxWithLabel",  "visible": True}
startRecordingAt = {"container": mainWindow, "id": "historySelectionId", "type": "CustomComboBoxWithLabel",  "visible": True}
#startRecordingAtComboBox = {"container":settingsScreen_Mainindow , "id": "customComboBoxId", "type": "CustomComboBox","visible": True}
startRecordingAtComboBox = {"container": settingsScreen_Mainindow, "id": "customComboBoxId","occurrence": 6, "type": "CustomComboBox", "unnamed": 1, "visible": True}
saveProfileInSettingsScreen = {"checkable": False, "container": settingsScreen_Mainindow, "id": "savePatientCardSettingsButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
ECGSpeedProfileInSettingsScreen = {"container": settingsScreen_Mainindow, "id": "ecgSpeedSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
ecgSpeedSelectorId = {"container": mainWindow, "id": "ecgSpeedSelectorId", "type": "CustomComboBoxWithLabel",  "visible": True}
ecgSensitivitySelectorId = {"container": mainWindow, "id": "ecgSensitivitySelectorId", "type": "CustomComboBoxWithLabel",  "visible": True}
ECGSensitivityProfileInSettingsScreen = {"container": settingsScreen_Mainindow, "id": "ecgSensitivitySelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
patientCardInSettingsScreen = {"checkable": True, "container": settingsScreen_Mainindow, "id": "patientCardSettingsButtonId", "type": "RectangularRadioButton", "unnamed": 1, "visible": True}
nameOrderPatientCardInSettingsScreen = {"container": settingsScreen_Mainindow, "id": "nameOrderSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
primaryPatientCardInSettingsScreen = {"container": settingsScreen_Mainindow, "id": "primaryIdSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
pidMandatorySelectorId = {"container": settingsScreen_Mainindow, "id": "pidMandatorySelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
hidMandatorySelectorId =   {"container": settingsScreen_Mainindow, "id": "hidMandatorySelectorId", "type": "CustomSwitchWithLabel",  "visible": True}
warnBeforeDeleteSelectorID = {"container": settingsScreen_Mainindow, "id": "warnBeforeDeleteSelectorId", "type": "CustomSwitchWithLabel", "visible": True}
ScrollViewPatientCardInSettingsScreen = {"container": settingsScreen_Mainindow, "id": "scrollviewId", "type": "ScrollView", "unnamed": 1, "visible": True}
surnameMandatorySelectorId= {"container": settingsScreen_Mainindow, "id": "surnameMandatorySelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
firstnameMandatorySelectorId = {"container": settingsScreen_Mainindow, "id": "firstNameSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
aboutSettingScreen = {"checkable": True, "container": settingsScreen_Mainindow, "id": "deviceInfoButtonId", "type": "RectangularRadioButton", "visible": True}
scrollViewAboutProfile = {"container": settingsScreen_Mainindow, "id": "scrollviewId", "type": "ScrollView", "visible": True}
autoFilterInSettingsScreen = {"checkable": True, "container": settingsScreen_Mainindow,  "type": "CustomRadioButton", "label": "Auto", "visible": True}
noneFilterInSettingsScreen = {"checkable": True, "container": settingsScreen_Mainindow, "type": "CustomRadioButton", "label": "None", "visible": True}
strictFilterInSettingsScreen = {"checkable": True, "container": settingsScreen_Mainindow, "type": "CustomRadioButton", "label": "Strict", "visible": True}
UserFilterInSettingsScreen = {"checkable": True, "container": settingsScreen_Mainindow, "type": "CustomRadioButton", "label": "User", "visible": True}
saveAutoProfile = {"checkable": False, "container": settingsScreen_Mainindow, "id": "saveAutoProfileButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
saveManualProfile = {"checkable": False, "container": settingsScreen_Mainindow, "id": "saveManualProfileButtonId", "type": "RoundedRectangleButton", "visible": True}
FilterValuesList = {"container": settingsScreen_Mainindow, "id": "ecgSignalColumnId", "type": "Column", "unnamed": 1, "visible": True}
filterMainInSettingsScreen = {"container": settingsScreen_Mainindow, "id": "filterMainsSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
filterDriftInSettingsScreen = {"container": settingsScreen_Mainindow, "id": "filterDriftSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
filterMyoInSettingsScreen = {"container": settingsScreen_Mainindow, "id": "filterMyoSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
profileColumn = {"container": settingsScreen_Mainindow, "id": "profilesColumnId", "type": "Column", "unnamed": 1, "visible": True}
printedLeadsInPatientCardSettingsScreen = {"container": settingsScreen_Mainindow, "id": "noOfPrintedLeadSelectionId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}

'Localization testing-Settings'
'1) General settings'
optionsItemId={"container": mainWindow, "id": "optionsItemId", "type": "Rectangle", "unnamed": 1, "visible": True}
dateSettingControlId={"container": mainWindow, "id": "dateSettingControlId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
timeSettingControlId={"container":  mainWindow, "id": "timeSettingControlId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
languageSelectorId={"container":  mainWindow, "id": "languageSelectorId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
scrollviewId={"container": mainWindow, "id": "scrollviewId", "type": "ScrollView", "unnamed": 1, "visible": True}
Langauge_customComboBoxId={"container": mainWindow, "id": "languageSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
LeadMarking_customComboBoxId={"container": mainWindow, "id": "leadMarkingSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
pacemakerEnableSelectorId={"container": mainWindow, "id": "pacemakerEnableSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}

jPointSelectorId_customComboBoxId={"container": mainWindow, "id": "jPointSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
qtcMethodSelectorId_customComboBoxId={"container": mainWindow, "id": "qtcMethodSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
warningSoundSelectorId={"container": mainWindow, "id": "warningSoundSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
homeScreenSelectorId_customComboBoxId={"container": mainWindow, "id": "homeScreenSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
demoModeSelectorId={"container": mainWindow, "id": "demoModeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
autologinModeSelectorId={"container": mainWindow, "id": "autologinModeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
autologinModeSelectorId_ON= {"checkable": True, "container": mainWindow, "id": "onSwitchId", "occurrence": 4, "type": "CustomRadioButton", "unnamed": 1, "visible": True}    
confirmPopupItemId_Autologin={"container": mainWindow, "id": "confirmPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
cancelButtonId={"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
advancedGeneralSettingsColumnId={"container": mainWindow, "id": "advancedGeneralSettingsColumnId", "type": "Column", "unnamed": 1, "visible": True}
resetSettingsButtonId={"checkable": False, "container": mainWindow, "id": "resetSettingsButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
profilesSettingsButtonId1={"checkable": True, "container": mainWindow, "id": "profilesSettingsButtonId", "type": "RectangularRadioButton", "unnamed": 1, "visible": True}
settingstextID={"container": mainWindow, "id": "headerItemId", "type": "Item", "unnamed": 1, "visible": True}

'2)Profile settings'
scrollviewId_AutoProfile={"container": mainWindow, "id": "scrollviewId", "type": "ScrollView", "unnamed": 1, "visible": True}
adaptiveWorklflowSelectionId={"container": mainWindow, "id": "adaptiveWorklflowSelectionId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
durationSelectionId={"container": mainWindow, "id": "durationSelectionId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
leadFormatSelectionId={"container": mainWindow, "id": "leadFormatSelectionId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
rhythmLeadSelectionId={"container": mainWindow, "id": "rhythmLeadSelectionId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
historySelectionId={"container": mainWindow, "id": "historySelectionId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
printSecondPageSelectorId={"container": mainWindow, "id": "printSecondPageSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
leadLayoutSelectionId={"container": mainWindow, "id": "leadLayoutSelectionId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
noOfPrintedLeadSelectionId_manual={"container": mainWindow, "id": "noOfPrintedLeadSelectionId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}

'3)Patient card settings'

nameOrderSelectorId={"container": mainWindow, "id": "nameOrderSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
primaryIdSelectorId={"container": mainWindow, "id": "primaryIdSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
pidMandatorySelectorId={"container": mainWindow, "id": "pidMandatorySelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
surnameMandatorySelectorId={"container": mainWindow, "id": "hidMandatorySelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
firstNameSelectorId={"container": mainWindow, "id": "firstNameSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
defaultClassificationSelectorId={"container": mainWindow, "id": "defaultClassificationSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
#advancedPatientCardSettingsRectId={"container": mainWindow, "id": "advancedPatientCardSettingsRectId", "type": "Rectangle", "unnamed": 1, "visible": True}

Surname_onSwitchId={"checkable": True, "container": mainWindow, "id": "onSwitchId", "occurrence": 2, "type": "CustomRadioButton", "unnamed": 1, "visible": True}

Surname_offSwitchId={"checkable": True, "container": mainWindow, "id": "offSwitchId", "occurrence": 2, "type": "CustomRadioButton", "unnamed": 1, "visible": True}

okButtonId={"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
advancedPatientCardSettingsColumnId={"container": mainWindow, "id": "advancedPatientCardSettingsColumnId", "type": "Column", "unnamed": 1, "visible": True}
deleteAllRecordsButtonId={"checkable": False, "container": mainWindow, "id": "deleteAllRecordsButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
deleteAllPatientsButtonId={"checkable": False, "container": mainWindow, "id": "deleteAllPatientsButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
sytemSettingsPopupItemId_Surname={"container": mainWindow, "id": "sytemSettingsPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}

'4)Network tab screen'
hostNameOrIPAdressControlId={"container": mainWindow, "id": "hostNameOrIPAdressControlId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
portControlId={"container": mainWindow, "id": "portControlId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
saveNetworkSettingsButtonId={"checkable": False, "container": mainWindow, "id": "saveNetworkSettingsButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
cmsConnectionInfoId={"container": mainWindow, "id": "cmsConnectionInfoId", "type": "Item", "unnamed": 1, "visible": True}
wifiConnectionId={"container": mainWindow, "id": "wifiConnectionId", "type": "ConnectionSettings", "unnamed": 1, "visible": True} 
wifiSwitchId={"container": mainWindow, "id": "wifiSwitchId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True} 
wifiGroupBoxId={"container": mainWindow, "id": "wifiGroupBoxId", "type": "GroupBox", "unnamed": 1, "visible": True} 
networkSelect={"container": mainWindow, "id": "networkSelect", "title": "Select Connection", "type": "GroupBox", "unnamed": 1, "visible": True}
Wi_fi_ID={"container": mainWindow, "id": "content", "type": "ColumnLayout", "unnamed": 1, "visible": True}

'5)Export tab-Settings -Language validation'
autoExportEnableSelectorId={"container": mainWindow, "id": "autoExportEnableSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}

'Service tab-settings-Language validation'
servicescreenId={"container": mainWindow, "id": "servicescreenId", "type": "ServiceScreen", "unnamed": 1, "visible": True}
upgradeAModuleFwButtonId={"checkable": False, "container": mainWindow, "id": "upgradeAModuleFwButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
factoryResetButtonId={"checkable": False, "container": mainWindow, "id": "factoryResetButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
logExportButtonId={"checkable": False, "container": mainWindow, "id": "logExportButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
printerCheckButtonId={"checkable": False, "container": mainWindow, "id": "printerCheckButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
contentRectId={"container": mainWindow, "id": "contentRectId", "type": "Rectangle", "unnamed": 1, "visible": True}
appContrllerPopupItemId={"container": mainWindow, "id": "appContrllerPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}

scrollviewId={"container": mainWindow, "id": "scrollviewId", "type": "ScrollView", "unnamed": 1, "visible": True}
additionalInfoColumnId={"container": mainWindow, "id": "additionalInfoColumnId", "type": "Column", "unnamed": 1, "visible": True}
#{"container": deviceSettingsScreenId_scrollviewId_ScrollView, "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}

'Printing tab settings-Language validation'
printSettingsButtonId={"checkable": True, "container": mainWindow, "id": "printSettingsButtonId", "type": "RectangularRadioButton", "unnamed": 1, "visible": True}
deviceInfoButtonId={"checkable": True, "container": mainWindow, "id": "deviceInfoButtonId", "type": "RectangularRadioButton", "unnamed": 1, "visible": True}

# Language ID's
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









#Function to navigate to profile screen from menu screen
def navigateToProfileButtonInSettingsScreen():
    try:
        result = False
        if waitForObject(profileSettingsButtonInsettingsScreen):
            if object.exists(profileSettingsButtonInsettingsScreen):
                mouseClick(waitForObject(profileSettingsButtonInsettingsScreen))
                snooze(2)
            
        if object.exists(adaptiveWorkflowSelection):
            result = True
            test.log("Successfully Profiles list in Settings screen is displayed")
        else:
            result = False
            test.log("Profiles List in Setting Screen is not displayed")   
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to navigate to auto profile in settings screen
def navigateToAutoProfileInSettingsScreen():
    try:
        result = False
        if waitForObject(profileColumn):
            if object.exists(profileColumn):
                parent=findObject(profileColumn)
                child=object.children(parent)
                mouseClick(child[0])         
        if object.exists(adaptiveWorkflowSelection):
            result = True
            test.log("Successfully navigated to auto profile page")
        else:
            result = False
            test.log("auto profile page is not displayed")   
        return result #verifications to all the profiles 
    
    except Exception as e:
        test.fail("Exception" +str(e))

        
#Function to navigate to manual profile in settings screen
def navigateToManualProfileInSettingsScreen():
    try:
        result = False
        if waitForObject(profileColumn):
            if object.exists(profileColumn):
                parent=findObject(profileColumn)
                child=object.children(parent)
                mouseClick(child[1])
                snooze(1)          
        if object.exists(printedLeadsInPatientCardSettingsScreen):
            result = True
            test.log("Successfully navigated to manual profile page")
        else:
            result = False
            test.log("Manual profile page is not displayed")   
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
#Function to navigate to rhythm profile in settings screen
def navigateToRhythmProfileInSettingsScreen():
    try:
        result = False
        if waitForObject(profileColumn):
            if object.exists(profileColumn):
                parent=findObject(profileColumn)
                child=object.children(parent)
                mouseClick(child[2])
                result = True                
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
    
#Function to navigate to Printing tab in settings screen
def navigateToPrintingButtonInSettingsScreen():
    try:
        result = False
        if waitForObject(printSettingsButtonId):
            if object.exists(printSettingsButtonId):
                mouseClick(waitForObject(printSettingsButtonId))
                snooze(2)
                result = True
        else:
            result = False
            test.log("Profiles List in Setting Screen is not displayed")   
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
        
#Function to navigate to patient card in settings screen
def navigateToPatientCardInSettingsScreen():
    try:
        result = False
        snooze(1)
        if object.exists(patientCardInSettingsScreen):
            mouseClick(waitForObject(patientCardInSettingsScreen))
            snooze(1)
            
            if object.exists(nameOrderPatientCardInSettingsScreen):
                result = True
                test.log("Successfully navigated to patient card page")
            else:
                result = False
                test.log("Patient card page is not displayed")   
        else:
            result = False
            test.log("Patient card page is not displayed")          
        
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Function to navigate About profile in setting screen
def navigateToAboutProfileInSettingsScreen(): 
    try:
        result = False
        snooze(1)
        if waitForObject(aboutSettingScreen):
            if object.exists(aboutSettingScreen):
                mouseClick(waitForObject(aboutSettingScreen))
                snooze(2)
            
        if object.exists(scrollViewAboutProfile):
            result = True
            test.log("Successfully navigated to patient card page")
        else:
            result = False
            test.log("Patient card page is not displayed")   
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
# Function to navigate General profile in setting screen
def navigateToGeneralInSettingsScreen(): 
    try:
        result = False
        snooze(1)
        if waitForObject(generalButtonInSettingScreen):
            if object.exists(generalButtonInSettingScreen):
                mouseClick(waitForObject(generalButtonInSettingScreen))
                snooze(1)
                result = True         
        
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Function to navigate General profile in setting screen
def navigateToNetworkInSettingsScreen(): 
    try:
        result = False
        snooze(1)
        if waitForObject(networkButtonInsettingsScreen):
            if object.exists(networkButtonInsettingsScreen):
                mouseClick(waitForObject(networkButtonInsettingsScreen))
                snooze(1)
                result = True         
        
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Function to navigate General profile in setting screen
def navigateToServiceInSettingsScreen(): 
    try:
        result = False
        snooze(1)
        if waitForObject(serviceButtonInSettingsScreen):
            if object.exists(serviceButtonInSettingsScreen):
                mouseClick(waitForObject(serviceButtonInSettingsScreen))
                snooze(1)
                result = True         
        
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Function to navigate General profile in setting screen
def navigateToExportInSettingsScreen(): 
    try:
        result = False
        snooze(1)
        if waitForObject(exportButtonInSettingScreen):
            if object.exists(exportButtonInSettingScreen):
                mouseClick(waitForObject(exportButtonInSettingScreen))
                snooze(1)
                result = True         
        
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
def BTLAdaptiveWorkFlowInSettingsScreen():    
    try:
        result = False
        if object.exists(adaptiveWorkflowSelection):
            mouseClick(findObject(adaptiveWorkflowSelection))  
            result = True
            test.log("Successfully clicked on adaptive work flow")
        else:
            result = False
            test.log("Adaptive work flow is not clicked")          
        
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))


#Method to verify advance settings available or not under general and printing

def CheckadvancedoptionsGeneralandPrinting():
    try:
        result = False
        snooze(1)
        if waitForObject(aboutSettingScreen):
            if object.exists(aboutSettingScreen):
                mouseClick(waitForObject(aboutSettingScreen)) 
                snooze(1)
        if waitForObject(generalButtonInSettingScreen):
            if object.exists(generalButtonInSettingScreen):
                mouseClick(waitForObject(generalButtonInSettingScreen))
                scroll_to_end()
                if (object.exists(advancedGeneralSettingsColumnId)==False):
                    test.log('Adavance settings not found under general settings')
                    snooze(1)
        if waitForObject(printSettingsButtonId):
            if object.exists(printSettingsButtonId):
                mouseClick(waitForObject(printSettingsButtonId))
                scroll_to_end()
                if (object.exists(advancedPrintSettingsRectId)==False):
                    test.log('Adavance settings not found under printing settings')
                    snooze(1)
                    result = True         
        
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))


def saveInSettingsScreen():
    try:
        result = False   
        if object.exists(saveProfileInSettingsScreen):
            mouseClick(findObject(saveProfileInSettingsScreen))  
            result = True
            test.log("Successfully saved the details")
        else:
            result = False
            test.log("Details are not saved")          
        
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
                  
#Function to save Auto profile in setting screen                     
def saveAutoProfileInSettingsScreen():   
    try:
        result = False    
        if object.exists(saveAutoProfile):
            mouseClick(findObject(saveAutoProfile)) 
            result = True
            test.log("Successfully saved the details in auto profile")
        else:
            result = False
            test.fail("Details are not saved in auto profile")          
        
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to save manual Profile in setting screen
def saveManualProfileInSettingsScreen():    
    try:
        result = False    
        if object.exists(saveManualProfile):
            mouseClick(findObject(saveManualProfile)) 
            result = True
            test.log("Successfully saved the details in auto profile")
        else:
            result = False
            test.log("Details are not saved in auto profile")          
        
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
def backPressInSettingsScreen():
    try:
        result = False 
        snooze(1)        
        if waitForObject(backButton):
            if object.exists(backButton):   
                mouseClick(waitForObject(backButton), 5,5,Qt.NoModifier,Qt.LeftButton)     
                #mouseClick(backButton)
                result = True
                test.log("Successfully menu screen is displayed")
        else:
            result = False
            test.log("Menu screen is not displayed")          
        
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
    


def scroll():
    try:
          
        snooze(1)
        mouseWheel(waitForObject(autoProfileInSettingsScreen), 468, 601, 0, -110, Qt.NoModifier)
        
    except Exception as e:
        test.fail("Exception" +str(e))
        
def scrollManual():
    try:
          
        snooze(1)
        mouseWheel(waitForObject(manualProfileInSettingsScreen), 468, 201, 0, -110, Qt.NoModifier)
        
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Method to scroll in settings 'Auto profile speed/sensitivity' screen 
def scrollInProfilesSettingsToSpeedAndSensitivitySection():
    try:
        snooze(1)
        mouseWheel(waitForObject(profilesSettingsButtonId), 300, 201, 0, -80, Qt.NoModifier)
    
    except Exception as e:
        test.fail("Exception" +str(e))
    
def scrollInProfilesSettingsToFilterSection():
    try:
        snooze(1)
        mouseWheel(waitForObject(profilesSettingsButtonId), 300, 201, 0, -110, Qt.NoModifier)
    
    except Exception as e:
        test.fail("Exception" +str(e))   
        
def scrollInSettingsScreen():
    try:
        snooze(1)
        mouseWheel(waitForObject(autoProfileInSettingsScreen), 468, 201, 0, -80, Qt.NoModifier)
        
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to navigate to auto profile in settings screen
def selectComboBoxItem(obj, valueToSelect):
    try:
        child = object.children(obj)
        initIndex = child[1].currentIndex
        for i in range (child[1].count):
            child[1].currentIndex = i
            if child[1].currentText == str(valueToSelect):
                snooze(1)
                test.log(" Given value %s is selected  "%valueToSelect)            
                return True
        child[1].currentIndex = initIndex
        return False

    except Exception as e:
        test.fail("Exception" +str(e))
        


def ComboboxValueToselectWorkaround(obj1,obj2):
    try:
        if object.exists(obj1):
            mouseClick(obj1)
            snooze(3)
            if object.exists(obj2):
                mouseClick(obj2)
                test.log(" Given value is selected ")            
                return True
        else:
            return False

    except Exception as e:
        test.fail("Exception" +str(e))     
        
           
#Function to navigate to patient card in settings screen       
def toChangeToggle(obj, valueToSet):
    try:
        snooze(1)
        hidMandatory = findObject(obj)
        
        if valueToSet == "Off":
            hidMandatory.switchControl = False
        elif valueToSet == "On":
            hidMandatory.switchControl = True
        
        test.log("Successfully selected the toggle")
        
        return True
            
    except Exception as e:
        test.fail("Exception"+ str(e))
        
def checkPatientCardItems():
    try:
        mandatoryItemsList = [
                          "View patient name as:",
                          "Primarily used identification number",
                          "Mandatory items","Patient ID","Hospital ID","Surname","First name",
                          "Default patient classification"
                          ]
    
        parent=findObject(ScrollViewPatientCardInSettingsScreen)
        child1=object.children(parent)
        objFlick=object.children(child1[0])
        objItem=object.children(objFlick[0])
        objColumn=object.children(objItem[0])
        
        listItems = []
        
        for item in objColumn:
            childColumn = object.children(item)
            
            if len(childColumn) >= 1:
                listItems.append(str(childColumn[0].text).strip())
            elif len(childColumn) < 1:
                listItems.append(str(item.text).strip())
            else:
                pass            
            
        
        if len(listItems) >= len(mandatoryItemsList):
            for val in mandatoryItemsList:
                if val in listItems:
                    pass
                else:
                    test.fail("Patient card does not contain all items")
                    return False
                
        test.passes("Patient card contain all items")
        return True
    
    except Exception as e:
        test.fail("Exception"+ str(e))    

#Function to check the toggle items
def checkTheToggleItems():
    try:
    
        mandatoryItemsList = [
                          "Patient ID",
                          "Hospital ID",
                          "Surname",
                          "First name"
                          ]
    
        parent=findObject(ScrollViewPatientCardInSettingsScreen)
        child1=object.children(parent)
        objFlick=object.children(child1[0])
        objItem=object.children(objFlick[0])
        objColumn=object.children(objItem[0])
        
        listItems = []
          
        for item in objColumn:
            childColumn = object.children(item)
            
            if len(childColumn) == 4:
                listItems.append(str(childColumn[0].text).strip())            
            
        
        if len(listItems) >= len(mandatoryItemsList):
            for val in mandatoryItemsList:
                if val in listItems:
                    pass
                else:
                    test.log("Mandatory items not present in list")
                    return False
                
        test.log("Mandatory items are present")
        return True
    
    except Exception as e:
        test.fail("Exception"+ str(e))     

def adaptiveWorkflowOptions():
    try:
        adaptiveOptions = [
                            "Record - Evaluate - Store",
                            "Record - Evaluate - Print",
                            "Record - Store",
                            "Record - Print"]
        
        dropdownList = []
        
        BTLAdp = waitForObject(adaptiveWorkflowSelection)
        child = object.children(BTLAdp)
        initIndex = child[1].currentIndex
        for i in range (child[1].count):
            child[1].currentIndex = i
            dropdownList.append(str(child[1].currentText).strip())
              
        child[1].currentIndex = initIndex
        
        if len(adaptiveOptions) == len(dropdownList):
            for item in adaptiveOptions:
                if item in dropdownList:
                    pass
                else:
                    test.log("Drop-down value not matching")
                    return False
        else:
            test.log("Drop-down value not matching")
            return False
        
        test.log("Drop-down value matching")
        return True
        
    except Exception as e:
        test.fail("Exception"+ str(e))
 
#Function to navigate to auto profile in settings screen
def navigateToNoneFilterInSettingsScreen():
    try:
        mainsResult=False
        driftResult=False
        myoResult=False
        snooze(1)
        if object.exists(noneFilterInSettingsScreen):
            mouseClick(waitForObject(noneFilterInSettingsScreen))
            snooze(1)
            obj = waitForObject(noneFilterInSettingsScreen)
            if obj.checked:
                test.log("Successfully None button is clicked")   
                
                mainObj=findObject(filterMainInSettingsScreen)
                driftObj=findObject(filterDriftInSettingsScreen)
                myoObj=findObject(filterMyoInSettingsScreen)
                
                mainChild = object.children(mainObj)
                if mainChild[1].enabled:                
                    mainsResult=False
                    test.log("Mains value is enabled")   
                else:
                    mainsResult=True
                    if str(mainObj.currentOptionText).strip() == "None":
                        test.log("Mains value displayed")
                        mainsResult=True
                    else:
                        test.log("Mains value not displayed") 
                        mainsResult=False                   
                   
                driftChild = object.children(driftObj)
                if driftChild[1].enabled:
                    driftResult=False
                    test.log("Drift value enabled")                    
                else:
                    driftResult=True
                    if str(driftObj.currentOptionText).strip() == "0.049 Hz (None)":
                        test.log("Drift value displayed")
                        driftResult=True
                    else:
                        test.log("Drift value not displayed")
                        driftResult=False                    
                    
                myoChild = object.children(myoObj)
                if myoChild[1].enabled:
                    myoResult=False
                    test.log("Myo value is enabled")                    
                else:
                    myoResult=True
                    if str(myoObj.currentOptionText).strip() == "170 Hz (None)":
                        test.log("Myo value displayed")
                        myoResult=True
                    else:
                        test.log("Myo value not displayed")
                        myoResult=False                      
                    
            else:
                test.log("None button is not clicked")
                return False
                    
        if mainsResult & driftResult & myoResult:
            return True
        else:
            return False
    
    except Exception as e:
        test.fail("Exception" +str(e))
 
#Function to navigate to auto profile in settings screen
def navigateToAutoFilterInSettingsScreen():
    try:
        result=False
        snooze(1)
        if object.exists(autoFilterInSettingsScreen):
            mouseClick(waitForObject(autoFilterInSettingsScreen))
            snooze(1)
            
            obj = waitForObject(strictFilterInSettingsScreen)
            if obj.checked:
                test.log("Successfully Strict button is clicked")
            result = True 
        else:
            result= False
        return result 
    
    except Exception as e:
        test.fail("Exception" +str(e)) 
                   
#Function to verify auto profile in settings screen
def verifyAutoFilterInSettingsScreen():
    try:
        mainsResult=False
        driftResult=False
        myoResult=False
        snooze(1)
        if object.exists(autoFilterInSettingsScreen):
            mouseClick(waitForObject(autoFilterInSettingsScreen))
            snooze(1)
            
            obj = waitForObject(autoFilterInSettingsScreen)
            if obj.checked:
                test.log("Successfully Auto button is clicked")
                
                mainObj=findObject(filterMainInSettingsScreen)
                driftObj=findObject(filterDriftInSettingsScreen)
                myoObj=findObject(filterMyoInSettingsScreen)
                
                mainChild = (object.children(mainObj))[1]
                                
                mainsList = []
                initIndex = mainChild.currentIndex
                
                for item in range(mainChild.count):
                    mainChild.currentIndex = item 
                    mainsList.append(str(mainChild.currentText).strip())
                    
                mainChild.currentIndex = initIndex
                
                actualMainsList = ["50 Hz", "60 Hz"]
                
                if mainChild.enabled:
                    mainsResult=True
                    if mainsList == actualMainsList:
                        test.log("Mains value displayed")
                        mainsResult=True
                    else:
                        test.log("Mains value not displayed")
                        mainsResult=False 
                else:
                    test.log("Mains value not displayed")
                    mainsResult=False
                       
                    
                driftChild = (object.children(driftObj))
                if driftChild[1].enabled:
                    test.log("Drift value is enabled")
                    driftResult=False
                else:
                    if str(driftObj.currentOptionText).strip() == "0.07 Hz Cubic Spline":
                        test.log("Drift value displayed")
                        driftResult=True
                    else:
                        test.log("Drift value not displayed")
                        driftResult=False
                
                
                myoChild = (object.children(myoObj))
                if myoChild[1].enabled:
                    test.log("Myo value is enabled")
                    myoResult=False 
                else: 
                    if str(myoObj.currentOptionText).strip() == "90 Hz Adaptive":
                        test.log("Myo value displayed")
                        myoResult=True
                    else:
                        test.log("Myo value not displayed")
                        myoResult=False  
            
        else:
            test.log("Auto button is not clicked")
        
        if mainsResult & driftResult & myoResult:
            return True
        else:
            return False
    
    except Exception as e:
        test.fail("Exception" +str(e))
#Function to select Filter in setting screen
def selectFilterInSettingScreen(filterName):
    try:
        result = False
        filter = filterName.strip()
        filterName = filter.upper()
        if filterName == "AUTO" :
            if object.exists(autoFilterInSettingsScreen):
                mouseClick(waitForObject(autoFilterInSettingsScreen))
                snooze(1)
                result = True
        elif filterName == "STRICT":
            if object.exists(strictFilterInSettingsScreen):
                mouseClick(waitForObject(strictFilterInSettingsScreen))
                snooze(1)
                result = True
        elif filterName == "USER":
            if object.exists(UserFilterInSettingsScreen):
                mouseClick(waitForObject(UserFilterInSettingsScreen))
                snooze(1)
                result = True
        elif filterName == "NONE":
            if object.exists(noneFilterInSettingsScreen):
                mouseClick(waitForObject(noneFilterInSettingsScreen))
                snooze(1)
                result = True
        else:
            test.log("Failed to select any filter value in setting screen")
        return result
    except Exception as e:
        test.fail("Exception" +str(e))
            

#Function to navigate to auto profile in settings screen
def navigateToStrictFilterInSettingsScreen():
    try:
        result = False
        snooze(1)
        if object.exists(strictFilterInSettingsScreen):
            mouseClick(waitForObject(strictFilterInSettingsScreen))
            snooze(1)
            
            obj = waitForObject(strictFilterInSettingsScreen)
            if obj.checked:
                test.log("Successfully Strict button is clicked")
            result = True
        else:
            result = False
        return result
    except Exception as e:
        test.fail("Exception" +str(e))            
#Function to navigate to auto profile in settings screen
def verifyStrictFilterInSettingsScreen():
    try:
        mainsResult=False
        driftResult=False
        myoResult=False
        snooze(1)
        if object.exists(strictFilterInSettingsScreen):
            mouseClick(waitForObject(strictFilterInSettingsScreen))
            snooze(1)
            
            obj = waitForObject(strictFilterInSettingsScreen)
            if obj.checked:
                test.log("Successfully Strict button is clicked")
                
                mainObj=findObject(filterMainInSettingsScreen)
                driftObj=findObject(filterDriftInSettingsScreen)
                myoObj=findObject(filterMyoInSettingsScreen)
                
                mainChild = (object.children(mainObj))[1]
                
                mainsList = []
                initIndex = mainChild.currentIndex
                
                for item in range(mainChild.count):
                    mainChild.currentIndex = item 
                    mainsList.append(str(mainChild.currentText).strip())
                    
                mainChild.currentIndex = initIndex
                
                actualMainsList = ["50 Hz", "60 Hz"]
                
                if mainChild.enabled:
                    mainsResult=True
                    if mainsList == actualMainsList:
                        test.log("Mains value displayed")
                        mainsResult=True
                    else:
                        test.log("Mains value not displayed")   
                        mainsResult=False 
                else:
                    test.log("Mains value not displayed")   
                    mainsResult=False
                    
                driftChild = (object.children(driftObj))[1]
           
                if str(driftObj.currentOptionText).strip() == "0.6 Hz":
                    test.log("Drift value displayed")
                    driftResult=True
                else:
                    test.log("Drift value not displayed")
                    driftResult=False  
                    
                myoChild = (object.children(myoObj))[1]
                
                if str(myoObj.currentOptionText).strip() == "25 Hz":
                    test.log("Myo value displayed")
                    myoResult=True
                else:
                    test.log("Myo value not displayed")
                    myoResult=False
                    
            else:
                test.log("Strict button is not clicked")
                return False
                
        if mainsResult & driftResult & myoResult:
            return True
        else:
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to navigate to auto profile in settings screen
def navigateToUserFilterInSettingsScreen():
    try:
        result = False
        snooze(1)
        if object.exists(UserFilterInSettingsScreen):
            mouseClick(waitForObject(UserFilterInSettingsScreen))
            snooze(1)
            
            obj = waitForObject(strictFilterInSettingsScreen)
            if obj.checked:
                test.log("Successfully Strict button is clicked")
            result = True  
        else:
            result = False
             
        return result   
    
    except Exception as e:
        test.fail("Exception" +str(e)) 
             
#Function to navigate to auto profile in settings screen
def verifyUserFilterInSettingsScreen():
    try:
        mainsListResult=False
        driftListResult=False
        myoListResult=False
        
        
        snooze(1)
        if object.exists(UserFilterInSettingsScreen):
            mouseClick(waitForObject(UserFilterInSettingsScreen))
            snooze(1)
            
            obj = waitForObject(UserFilterInSettingsScreen)
            if obj.checked:
                test.log("Successfully User button is clicked")
                
                mainObj=findObject(filterMainInSettingsScreen)
                driftObj=findObject(filterDriftInSettingsScreen)
                myoObj=findObject(filterMyoInSettingsScreen)
                
                mainChild = (object.children(mainObj))[1]
                mainsList = []
                mainInitIndex = mainChild.currentIndex
                
                for item in range(mainChild.count):
                    mainChild.currentIndex = item 
                    mainsList.append(str(mainChild.currentText).strip())
                    
                mainChild.currentIndex = mainInitIndex
                  
                actualMainsList = ["None","50 Hz", "60 Hz"]
                
                if mainChild.enabled:
                    mainsListResult=True
                    if mainsList == actualMainsList:
                        test.log("Mains value displayed")
                        mainsListResult=True
                    else:
                        test.log("Mains value not displayed")
                        mainsListResult=False
                else:
                    test.log("Mains value not displayed")
                    mainsListResult=False
                    
                
                driftChild = (object.children(driftObj))[1]
                driftList = []
                driftInitIndex = driftChild.currentIndex
                
                for item in range(driftChild.count):
                    driftChild.currentIndex = item 
                    driftList.append(str(driftChild.currentText).strip())
                    
                driftChild.currentIndex = driftInitIndex
                  
                actualDriftList = ['0.049 Hz (None)', '0.05 Hz', '0.6 Hz', '0.07 Hz Cubic Spline']
                
                if driftChild.enabled:
                    driftListResult=True
                    if driftList == actualDriftList:
                        test.log("Drift value displayed")
                        driftListResult=True
                    else:
                        test.log("Drift value not displayed")
                        driftListResult=False    
                else:
                    test.log("Drift value not displayed")
                    driftListResult=False    
                                                
                                   
                myoChild = (object.children(myoObj))[1]
                myoList = []
                myoInitIndex = myoChild.currentIndex
                
                for item in range(myoChild.count):
                    myoChild.currentIndex = item 
                    myoList.append(str(myoChild.currentText).strip())
                    
                myoChild.currentIndex = myoInitIndex
                  
                actualMyoList = ['170 Hz (None)', '35 Hz', '20 Hz', '25 Hz', '90 Hz Adaptive']
                
                if myoChild.enabled:
                    myoListResult=True
                    if myoList == actualMyoList:
                        test.log("Myo value displayed")
                        myoListResult=True
                    else:
                        test.log("Myo value not displayed")
                        myoListResult=False
                else:
                    test.log("Myo value not displayed")
                    myoListResult=False
                    
                
            else:
                test.log("User button is not clicked")
                return False
        
        if mainsListResult & driftListResult & myoListResult:
            return True
        else:
            return False
    
    except Exception as e:
        test.fail("Exception" +str(e))
  
#Function to verify Auto profile filter values
def displayFilterValues():
    try:
        
        filterLists = [
                       "None",
                       "Auto",
                       "Strict",
                       "User"
                       ] 
        
        parent = findObject(FilterValuesList)
        child = object.children(parent)
        child1= object.children(child[5])
        child2 = object.children(child1[0])
 
        listItems = []
        
        for item in range(len(child2)-1):
            listItems.append(str(child2[item].label).strip())
            
        if listItems == filterLists:
            test.log("Successfully filter values are displayed")
            return True
        else:
            test.log("Filter values are not displayed")
            return False
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to verify manual profile filter values
def displayManualProfileFilterValues():   
    try:
        
        filterLists = [
                       "None",
                       "Auto",
                       "Strict",
                       "User"
                       ] 
        
        parent = findObject(FilterValuesList)
        child = object.children(parent)
        child1= object.children(child[3])
        child2 = object.children(child1[0])
 
        listItems = []
        
        for item in range(len(child2)-1):
            listItems.append(str(child2[item].label).strip())
            
        if listItems == filterLists:
            test.log("Successfully filter values are displayed")
            return True
        else:
            test.log("Filter values are not displayed")
            return False
    
    except Exception as e:
        test.fail("Exception" +str(e))

#Function to verify manual profile filter values
def displayAboutProfileValues():   
    try:
        
        deviceInformation = ['Device IP Address',
                             'Release version(UI)',
                             'Controller', 'Acquisition',
                             'ECG Diag version', 'Acquisition FW',
                             'Printer', 'Printer FW', 'Storage', 
                             'git version', 'commit id', 
                             'release date', 'build machine', 
                             'build user']                      
        
        parent = findObject(scrollViewAboutProfile)
        child = object.children(parent)
        child1= object.children(child[0])
        child2 = object.children(child1[0])
        child3 = object.children(child2[0])
        listItems = []
        
        for item in range(len(child3)-1):
            child4 = object.children(child3[item])
            if len(child4) > 0 :
                listItems.append(str(child3[item].title).strip())
            
        if listItems == deviceInformation:
            test.log("Successfully filter values are displayed")
            return True
        else:
            test.log("Filter values are not displayed")
            return False
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to verify device Information displayed in about profile
def deviceInformationAboutProfile(testData):
    try:
        
        deviceInformation = [testData['Step 1']['Device IP Address'],
                             testData['Step 2']['Release version(UI)'],
                             testData['Step 3']['Controller'],
                             testData['Step 4']['Acquisition'],
                             testData['Step 5']['ECG Diag version'],
                             testData['Step 6']['Acquisition FW'],
                             testData['Step 7']['Printer'],
                             testData['Step 8']['Printer FW'],
                             testData['Step 9']['Storage'],
                             testData['Step 10']['git version'],
                             testData['Step 11']['commit id'],
                             testData['Step 12']['release date'],
                             testData['Step 13']['build machine'],
                             testData['Step 14']['build user']]                      
        
        parent = findObject(scrollViewAboutProfile)
        flickable = object.children(parent)
        item= object.children(flickable[0])
        column = object.children(item[0])
        customTextField = object.children(column[0])
        listItems = []
        
        for item in range(len(customTextField)-1):
            child4 = object.children(customTextField[item])
            if len(child4) > 0 :
                listItems.append(str(child4[1].displayText).strip())
            
        if listItems == deviceInformation:
            test.log("Successfully filter values are displayed")
            return True
        else:
            test.log("Filter values are not displayed")
            return False
    
    except Exception as e:
        test.fail("Exception" +str(e)) 
 
def checkPrimarilyUsedIdentification():
    try:
    
        primarilyUsedIdentificationValues = [
                                         "Patient ID",
                                         "Hospital ID"
                                        ]
    
        listItems = []
        
        dropDownObj = waitForObject(primaryPatientCardInSettingsScreen)
        child = object.children(dropDownObj)
        initIndex = child[1].currentIndex
        for i in range (child[1].count):
            child[1].currentIndex = i
            listItems.append(str(child[1].currentText).strip())
              
        child[1].currentIndex = initIndex
        
        if primarilyUsedIdentificationValues == listItems:
            test.log("Successfully primarily values are displayed")
            return True
        else:
            test.log("Primarily values are not displayed")
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e))
 
def sensitivityList():
    try:
        sensitivityValues = [
                         "2.5",
                         "5",
                         "10",
                         "20"
                         ]
        listItems = []
        
        
        dropDownObj = waitForObject(ECGSensitivityProfileInSettingsScreen)
        child = object.children(dropDownObj)
        initIndex = child[1].currentIndex
        for i in range (child[1].count):
            child[1].currentIndex = i
            listItems.append(str(child[1].currentText).strip())
              
        child[1].currentIndex = initIndex
        
        if sensitivityValues == listItems:
            test.passes("Successfully sensitivity values are displayed")
            return True
        else:
            test.fail("Sensitivity values are not displayed")
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e))
        
def speedList():
    try:
    
        speedValues = [
                   "5",
                   "10",
                   "12.5",
                   "25",
                   "50"
                  ]
        listItems = []
        
        
        dropDownObj = waitForObject(ECGSpeedProfileInSettingsScreen)
        child = object.children(dropDownObj)
        initIndex = child[1].currentIndex
        for i in range (child[1].count):
            child[1].currentIndex = i
            listItems.append(str(child[1].currentText).strip())
              
        child[1].currentIndex = initIndex
        
        if speedValues == listItems:
            test.passes("Successfully sensitivity values are displayed")
            return True
        else:
            test.fail("Sensitivity values are not displayed")
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e)) 
        
def durationList():
    try:
    
        durationValues = [
                   "10",
                   "12",
                   "15",
                   "20"
                  ]
        listItems = []
        
        
        dropDownObj = waitForObject(durationSelection)
        child = object.children(dropDownObj)
        initIndex = child[1].currentIndex
        for i in range (child[1].count):
            child[1].currentIndex = i
            listItems.append(str(child[1].currentText).strip())
              
        child[1].currentIndex = initIndex
        
        if durationValues == listItems:
            test.passes("Successfully duration values are displayed")
            return True
        else:
            test.fail("duration values are not displayed")
            return False    
        
    except Exception as e:
        test.fail("Exception" +str(e))       
        
def checkProfileList():
    try:
    
        profileList = [
                   "Auto",
                   "Manual"
                   ]
    
        profileObj = waitForObject(profileColumn)
        child = object.children(profileObj)
    
        listItems = []
        
        for item in range(len(child)-2):
            listItems.append(str(child[item].text).strip())
            
        if profileList == listItems:
            test.log("Successfully profile list is displayed")
            return True
        else:
            test.log("Profile list is not displayed")
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e))      
        
def getECGList():
    
    try:
    
        ECGSignalList = [
                     "Speed",
                     "Rhythm lead speed",
                     "Sensitivity",
                     "Chest leads to half sensitivity",
                     "View",
                     "Filters"
                     ]
        
        filterValuesObj = waitForObject(FilterValuesList)
        filterChild = object.children(filterValuesObj)
        
        listItems = []
        
        for item in range(len(filterChild) - 1):
            childItem = object.children(filterChild[item])
            
            if len(childItem) > 1:
                listItems.append(str(childItem[0].text).strip())
            else:
                listItems.append(str(filterChild[item].text).strip())
                
        if ECGSignalList == listItems:
            test.passes("Successfully ECG signal list is displayed")
            return True
        else:
            test.fail("Ecg signal liSuccessfullyst is not displayed")
            return False
    
    except Exception as e:
        test.fail("Exception" +str(e))   
    
def checkProfiles():
    try:
        profileList = [
                     "defaultProfiles",
                     "customProfiles"
                     ]
    
        profileObj = waitForObject(profileColumn)
        child = object.children(profileObj)
    
        listItems=[]
    
        for item in range(len(child)):
            try:
                listItems.append(str(child[item].text).strip())
            
            except Exception:
                pass
  
    
        if profileList == listItems:
            test.log("Successfully profile list is displayed")
            return True
        else:
            test.log("Profile list is not displayed")
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e))      


#Language validation-Keerthik
#Navigatting to menu screen

leadmarkingcomboID={"container":settingsScreen_Mainindow, "id": "customComboBoxId", "occurrence": 2, "type": "CustomComboBox", "unnamed": 1, "visible": True}
SelectingIECasleadmarkingID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "type": "ItemDelegate", "unnamed": 1, "visible": True}
SelectingAHAasleadmarkingID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 2, "type": "ItemDelegate", "unnamed": 1, "visible": True}
BacktomenuscreenfromsettingsscreenID={"checkable": False, "container": mainWindow, "id": "deviceSettingsBackButtonId", "type": "Button", "unnamed": 1, "visible": True}

#Navigating to Printer tab settings







#selecting lead marking combo
def Selectingleadmarkingcombo():
    try:
        status='fail'
        if waitForObject(leadmarkingcomboID):
            if object.exists(leadmarkingcomboID):
                mouseClick(leadmarkingcomboID)
                status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))


"""Keerthik_language validation objects"""

#selecting IEC from combo
def SelectingIECasleadmarking():
    try:
        status='fail'
        if waitForObject(SelectingIECasleadmarkingID):
            if object.exists(SelectingIECasleadmarkingID):
                mouseClick(SelectingIECasleadmarkingID)
                status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))
        
def Backtomenuscreenfromsettingsscreen():
    try:
        status='fail'
        if waitForObject(BacktomenuscreenfromsettingsscreenID):
            if object.exists(BacktomenuscreenfromsettingsscreenID):
                mouseClick(BacktomenuscreenfromsettingsscreenID)
                status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))
        
def SelectingAHAasleadmarking():
    try:
        status='fail'
        if waitForObject(SelectingAHAasleadmarkingID):
            if object.exists(SelectingAHAasleadmarkingID):
                mouseClick(SelectingAHAasleadmarkingID)
                status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))

"Evaluation screen supporting steps"

SelectRecord_EvaluateID={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "type": "ItemDelegate", "unnamed": 1, "visible": True}

#Setting BTL work flow to Record-Evaluate in settings
def Selectrecord_Evaluate():
    try:
        status='fail'
        if waitForObject(SelectRecord_EvaluateID):
            if object.exists(SelectRecord_EvaluateID):
                mouseClick(SelectRecord_EvaluateID)
                status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))


def SetBTLadaptiveworkflowtorecordandevaluvateAuto():
    try:
        step1=Onlinesccreentomenuscreen()
        #Navigating to settings screen
        step2=navigateToSettingsScreenFromMenuScreen()
        #Navigating to profile screen
        step3=navigateToProfileButtonInSettingsScreen()
        #Navigating to auto profile
        step4=navigateToAutoProfileInSettingsScreen()
        #select BTL adaptive work flow
        step5=BTLAdaptiveWorkFlowInSettingsScreen()
        #Select Record Record-Evaluate
        step6=Selectrecord_Evaluate()
        #Navigate back to menu screen
        step7=Backtomenuscreenfromsettingsscreen()
        #Navigate to online screen
        step8=navigateToLiveScreenFromMenuScreen()
        if step1 and step2 and step3 and step4 and step5 and step6 and step7 and step8:
            test.log('sucessfully set Record-Evaluate as work flow navigated back to online screen')
            status='pass'
        else:
            test.log('Failed set Record-Evaluate as work flow navigated back to online screen')
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail('exception'+str(e))   
        
#Battery back up pre-req setup
birghtnessID={"container": mainWindow, "id": "brightnessAdjustComponentId", "type": "Slider", "unnamed": 1, "visible": True}
Brightnessadjustcomp={"container": mainWindow, "id": "brightnessAdjustComponentId", "type": "Slider", "unnamed": 1, "visible": True}
networkSettingsButtonId={"checkable": True, "container": mainWindow, "id": "networkSettingsButtonId", "text": "Network", "type": "RectangularRadioButton", "unnamed": 1, "visible": True}
Wif_off={"container": mainWindow, "id": "wifiConnectionId", "type": "ConnectionSettings", "unnamed": 1, "visible": True}
exportSettingsButtonId={"checkable": True, "container": mainWindow, "id": "exportSettingsButtonId", "text": "Export", "type": "RectangularRadioButton", "unnamed": 1, "visible": True}
Export_off={"container": mainWindow, "id": "autoExportEnableSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}

'''Scenario-3
Setting brightness to 50% in setting'''
def setbatterypercentage_50(): 
    try:
        status='fail'
        if waitForObject(Brightnessadjustcomp):
            if object.exists(Brightnessadjustcomp):
                setValue((Brightnessadjustcomp.value),5)
                test.verify(waitForObject(Brightnessadjustcomp).value==5)
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail('exception'+str(e)) 
        

#naviagte to n/w tab and turn off the wi-fi
def navigateto_networktab_andturnoffwifi():
    try:
        if waitForObject(networkSettingsButtonId):
            if object.exists(networkSettingsButtonId):
                tapObject(networkSettingsButtonId)
                if waitForObject(Wif_off):
                    if object.exists(Wif_off):
                        tapObject(Wif_off)
                        status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.fail('exception'+str(e)) 

#Navigate to export tab and turn off auto export
def navigateto_networktab_andturnoffwifi():
    try:
        if waitForObject(networkSettingsButtonId):
            if object.exists(networkSettingsButtonId):
                tapObject(networkSettingsButtonId)
                if waitForObject(Wif_off):
                    if object.exists(Wif_off):
                        tapObject(Wif_off)
                        status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.fail('exception'+str(e)) 


def navigateto_Exporttab_andturnoff_autoexport():
    try:
        if waitForObject(exportSettingsButtonId):
            if object.exists(exportSettingsButtonId):
                tapObject(exportSettingsButtonId)
                if waitForObject(Export_off):
                    if object.exists(Export_off):
                        tapObject(Export_off)
                        status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.fail('exception'+str(e)) 


'Localization testing-General settings'
autoShutdownSelectorId={"container": mainWindow, "id": "autoShutdownSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
standByModeSelectorId={"container": mainWindow, "id": "standByModeSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
autoShutdowncustomComboBoxId={"container": mainWindow, "id": "customComboBoxId", "occurrence": 6, "type": "CustomComboBox", "unnamed": 1, "visible": True}
standByModecustomComboBoxId={"container": mainWindow, "id": "customComboBoxId", "occurrence": 7, "type": "CustomComboBox", "unnamed": 1, "visible": True}

#collecting all the sub option text from settings screen (General,Profile,Printing....)
def Collectingsuboptionsfromgenralscreen():
    try:
        if object.exists(optionsItemId):
            parent=findObject(optionsItemId)
            child=object.children(parent)
            col_0=object.children(child[0])
            col_00=object.children(col_0[0])
            for x in range(9):
                if x==2:
                    continue    
                str1=col_00[x].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(1)
                status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
 
#collecting General screen text-date,time,Pacemaker signalization,J point,etc
def Collectingtextsfromgenralscreen_1stchild_text(*arguments):
    try:
        status='fail'
        for obj in arguments:
            if object.exists(obj):
                parent=findObject(obj)
                child=object.children(parent)
                str1=child[0].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(1)
                status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e)) 

#Collecting display brightness text,Local settings and Recording configuration
def collectingbrightneess_Local_recordingconfig_text():
    try:
        status='fail'   
        if object.exists(scrollviewId):
            parent=findObject(scrollviewId)
            child=object.children(parent)
            Flick=object.children(child[0])       
            item_0=object.children(Flick[0])
            col_0=object.children(item_0[0])
            Row_0=object.children(col_0[0])
            #collecting brightness text settings text
            str1=Row_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting local settings text
            str1=col_0[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting recording configuration text
            str1=col_0[4].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting Bar code text
            #str1=col_0[12].text
            #addtolist1(str1)
            #test.log('Collected string ='+str(str1))
            #snooze(1)
            status='pass'
            return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))

#Common method to collect drop down text            
def toReturnComboBoxList1(*arguments):
    try:
        snooze(1)
        for obj in arguments:
            parent=findObject(obj)
            child = object.children(parent)
            initIndex = child[1].currentIndex
            for i in range (child[1].count):
                child[1].currentIndex = i
                str1=child[1].currentText
                list1.append(child[1].currentText)         
                test.log('Collected string ='+str(str1))
                status='pass'
                snooze(1)
                child[1].currentIndex = initIndex
        return True if status=='pass' else False
    except Exception as e:
        test.log("Exception: " + str(e))   


#Genral_ettings scroll till end of page
def scroll_to_end():
    try:
        status='fail'
        snooze(1)
        mouseWheel(waitForObject(scrollviewId), 614, 51, -16, -322, Qt.NoModifier)
        status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e))
        

        
        
        

#Collecting text -Auto login warning
def Collectingautologin_warning():
    try:
        status='fail'
        if object.exists(autologinModeSelectorId_ON):
            mouseClick(autologinModeSelectorId_ON)
            snooze(1)
        if object.exists(confirmPopupItemId_Autologin):
            collectingwarning_text(confirmPopupItemId_Autologin)
            Acceptwarning_popup(cancelButtonId)
            status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))

barcodeColumnID={"container": mainWindow, "id": "barcodeColumnID", "type": "Column", "unnamed": 1, "visible": True}
saveRegexButtonID={"checkable": False, "container": mainWindow, "id": "saveRegexButtonID", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
resetRegexButtonID={"checkable": False, "container": mainWindow, "id": "resetRegexButtonID", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
barcodeIDTypeSelecterID={"container": mainWindow, "id": "barcodeIDTypeSelecterID", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
barcodeReaderEnableSelectorId={"container": mainWindow, "id": "barcodeReaderEnableSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
General_settingsadvancedtab={"container": mainWindow, "id": "advancedGeneralSettingsRectId", "type": "Rectangle", "unnamed": 1, "visible": True}
DateofbirthFormatID={"container": mainWindow, "id": "barcodeDOBFormatSelectorID", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}



def CollectingBarcode_text():
    try:
        status='fail'
        if object.exists(barcodeColumnID):
            parent=findObject(barcodeColumnID)
            child=object.children(parent)
            #Collecting Bar code reader regex  editor text
            str1=child[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #Collecting Enable Barcode reader text
        if object.exists(barcodeReaderEnableSelectorId):
            parent=findObject(barcodeReaderEnableSelectorId)
            child=object.children(parent)
            str1=child[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #Collecting save text
        if object.exists(saveRegexButtonID):
            parent=findObject(saveRegexButtonID)
            child=object.children(parent)
            str1=child[3].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #Collecting reset text
        if object.exists(resetRegexButtonID):
            parent=findObject(resetRegexButtonID)
            child=object.children(parent)
            str1=child[3].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #Collecting ID number type text
        if object.exists(barcodeIDTypeSelecterID):
            parent=findObject(barcodeIDTypeSelecterID)
            child=object.children(parent)
            str1=child[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #Collecting date of birth format text
        if object.exists(DateofbirthFormatID):
            parent=findObject(DateofbirthFormatID)
            child=object.children(parent)
            str1=child[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
        
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
        
#Collecting text under general settings-Advanced tab(bar code

def advancedGeneralSettingsColumnId_Text():
    try:
        status='fail'
        if object.exists(advancedGeneralSettingsColumnId):
            parent=findObject(advancedGeneralSettingsColumnId)
            child=object.children(parent)
            #Navigating to advanced tab
            mouseClick(General_settingsadvancedtab)
            snooze(1)
            #Collecting 'Bar code' text
            Row_1=object.children(child[1])
            str1=Row_1[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Calling function- Bar code related text
            CollectingBarcode_text()
        
        #Collecting factory settings  
        if object.exists(advancedGeneralSettingsColumnId):
            parent=findObject(advancedGeneralSettingsColumnId)
            child=object.children(parent)
            Column_2=object.children(child[2])
            Row_2=object.children(Column_2[2])
            str1=Row_2[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting 'resetting to factory settings will not delete patient text'
            Row_3=object.children(Column_2[3])
            str1=Row_3[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #Collecting reset text and click on that
        if object.exists(resetSettingsButtonId):
            parent=findObject(resetSettingsButtonId)
            child=object.children(parent)
            str1=child[3].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            mouseClick(resetSettingsButtonId)
            collectingwarning_text(confirmPopupItemId_Autologin)
            Acceptwarning_popup(cancelButtonId)
            status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))

# Settings>Profile>Auto profile
'Localization testing- Profile-Auto profile'
signalSettingBackgroundId={"container": mainWindow, "id": "signalSettingBackgroundId", "type": "Rectangle", "unnamed": 1, "visible": True}

#Functions to collect auto profile text
def CollectTextfromAutoprofilesettings():
    try:
        status='fail'
        if object.exists(scrollviewId_AutoProfile):
            parent=findObject(scrollviewId_AutoProfile)
            child=object.children(parent)
            Flick=object.children(child[0])
            item0=object.children(Flick[0])
            col0=object.children(item0[0])
            #collecting ECG profile text
            str1=col0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting Examination set up text
            str1=col0[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting ECG Signal text
            str1=col0[8].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting Report Setup text
            str1=col0[10].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        if object.exists(signalSettingBackgroundId):
            parent=findObject(signalSettingBackgroundId)
            child=object.children(parent)
            Flick=object.children(child[0])
            col0=object.children(Flick[4])
            #Collecting filters text
            str1=col0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting note: text
            str1=col0[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
            
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
    
#Settings>Profile>Manual profile text

#Function to collect text from Manual profile

def CollectTextfromManualprofilesettings():
    try:
        status='fail'
        if object.exists(scrollviewId_AutoProfile):
            parent=findObject(scrollviewId_AutoProfile)
            child=object.children(parent)
            Flick=object.children(child[0])
            item0=object.children(Flick[0])
            col0=object.children(item0[0])
            #collecting Manual profile text
            str1=col0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
            return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
        
#Function to collect text from Rhythm profile
def CollectTextfromRhythmprofilesettings():
    try:
        status='fail'
        if object.exists(scrollviewId_AutoProfile):
            parent=findObject(scrollviewId_AutoProfile)
            child=object.children(parent)
            Flick=object.children(child[0])
            item0=object.children(Flick[0])
            col0=object.children(item0[0])
            #collecting Rhythm profile text
            str1=col0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
            return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
        
'Localization- Collecting text from printing tab'
scrollviewId_printingtab={"container":mainWindow, "id": "scrollviewId", "type": "ScrollView", "unnamed": 1, "visible": True}
reportPrintSpeedSelectorId={"container": mainWindow, "id": "reportPrintSpeedSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
customComboBoxId_reportforspeed={"container": mainWindow, "id": "customComboBoxId", "type": "CustomComboBox", "unnamed": 1, "visible": True}
printLineWidthSelectionId={"container": mainWindow, "id": "printLineWidthSelectionId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
printFormatSelectionId={"container": mainWindow, "id": "printFormatSelectionId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
advancedPrintSettingsRectId={"container": mainWindow, "id": "advancedPrintSettingsRectId", "type": "Rectangle", "unnamed": 1, "visible": True}
Reportprint_combobox={"container": mainWindow, "id": "reportPrintSpeedSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
customComboBoxId_Printformat={"container": mainWindow, "id": "printFormatSelectionId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
customComboBoxId_linewidth={"container": mainWindow, "id": "printLineWidthSelectionId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}

#Collecting text from print tab -settings
def Collectingtextfromprintingtab_settingsscreen():
    try:
        status='fail'
        if object.exists(scrollviewId_printingtab):
            parent=findObject(scrollviewId_printingtab)
            child=object.children(parent)
            Flick=object.children(child[0])
            item0=object.children(Flick[0])
            col0=object.children(item0[0])
            #collecting header print setup
            str1=col0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #Collecting Report print speed text
        if object.exists(reportPrintSpeedSelectorId):
            parent=findObject(reportPrintSpeedSelectorId)
            child=object.children(parent)
            str1=child[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))


#Collecting Print format and printer line width        
def printtab_advancedsettings():
    try:
        status='fail'
        if object.exists(advancedPrintSettingsRectId):
            mouseClick(advancedPrintSettingsRectId)
            if object.exists(printLineWidthSelectionId):
                parent=findObject(printLineWidthSelectionId)
                child=object.children(parent)
                str1=child[0].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(1)
                status='pass'
        #Collecting print format settings
        if object.exists(printFormatSelectionId):
            parent=findObject(printFormatSelectionId)
            child=object.children(parent)
            str1=child[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
        status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
        

'Localization testing- Profile-Patient card screen'

#Collecting text from patient card settings screen
def CollectTextfromPatientcardesettings():
    try:
        status='fail'
        if object.exists(scrollviewId_AutoProfile):
            parent=findObject(scrollviewId_AutoProfile)
            child=object.children(parent)
            Flick=object.children(child[0])
            item0=object.children(Flick[0])
            col0=object.children(item0[0])
            #collecting Mandatory item text
            str1=col0[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
            return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
   
#Collecting warning message about PID or surname mandatory:
def Collectingwarningmessage_Surname():
    try:
        status='fail'
        if object.exists(Surname_offSwitchId):
            mouseClick(waitForObject(Surname_offSwitchId))
            snooze(1)
            #Click on back button-To get warning text
            mouseClick(BacktomenuscreenfromsettingsscreenID)
            if object.exists(sytemSettingsPopupItemId_Surname):
                collectingwarning_text(sytemSettingsPopupItemId_Surname)
                Acceptwarning_popup(okButtonId)
                snooze(1)
            #Switch on the the surname
        if object.exists(Surname_onSwitchId):
            mouseClick(waitForObject(Surname_onSwitchId))
            status='pass'
            return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
        
#Collecting advanced tab in patient card text
def Collectingadvancedtab_Patientcard_text():
    try:
        #Clicking on advanced tab in patient card
        if waitForObject(advancedPatientCardSettingsColumnId):
            if object.exists(advancedPatientCardSettingsColumnId):
                mouseClick(advancedPatientCardSettingsColumnId)
        #Collecting text from advanced tab        
        if object.exists(advancedPatientCardSettingsColumnId):
            parent=findObject(advancedPatientCardSettingsColumnId)
            child=object.children(parent)
            Col2=object.children(child[2])
            #collecting Delete all records text
            Row0=object.children(Col2[0])
            str1=Row0[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            #collecting Delete all records and patients
            Row1=object.children(Col2[1])
            str1=Row1[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            status='pass'
            return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))

#Collecting warning text when click on delete button-Patient card advanced
def collectingwarningmessage_Pateintcard_delete(*arguments):
    try:
        #Clicking on delete button in patient card(advanced)
        for obj in arguments:
            if waitForObject(obj):
                if object.exists(obj):
                    mouseClick(obj)
                    snooze(1)
                    if object.exists(confirmPopupItemId_Autologin):
                        collectingwarning_text(confirmPopupItemId_Autologin)
                        Acceptwarning_popup(cancelButtonId)
                        snooze(1)
                        status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
        
'Localization testing-Network tab'
 
Wifi_groupID={"container": mainWindow, "id": "wifiGroupBoxId", "type": "GroupBox", "unnamed": 1, "visible": True}

#Collecting Refresh, Reset and Forget all n/ws text

def collectingRefreshResetForgetnw():
    try:
        count=0
        if object.exists(Wifi_groupID):
            parent=findObject(Wifi_groupID)
            child=object.children(parent)
            item0=object.children(child[0])
            content0=object.children(item0[0])
            Row2=object.children(content0[2])
            coln1=object.children(Row2[1])
            #Collecting Refresh text
            for x in range(len(coln1)):
                Row0=object.children(coln1[x])
                str1=Row0[1].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(1)
                count=count+1
                
        return True if count==3 else False                   
    except Exception as e:
        test.log('exception'+str(e))
  
#Collecting text from network tab settings screen
def CollectTextfromNetworktabsettings():
    try:
        status='fail'
        if object.exists(scrollviewId_AutoProfile):
            parent=findObject(scrollviewId_AutoProfile)
            child=object.children(parent)
            Flick=object.children(child[0])
            item0=object.children(Flick[0])
            col0=object.children(item0[0])
            #collecting Network mode text
            str1=col0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting CONNECTin Server Details
            str1=col0[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #collecting save and connect text
        if object.exists(saveNetworkSettingsButtonId):
            parent=findObject(saveNetworkSettingsButtonId)
            child=object.children(parent)
            #label1=object.children(child[2])
            str1=child[3].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #collecting save Availiable networks text
        if object.exists(Wi_fi_ID):
            parent=findObject(Wi_fi_ID)
            child=object.children(parent)
            str1=child[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
         
#Collecting 1st child of parent and text in 2nd position of child 

#Disconnection text,Select Connection
def CollectingtextsfromNetworktab_2ndtextof_child(*arguemnts):  
    try:
        for obj in arguemnts:
            if object.exists(obj):
                parent=findObject(obj)
                child=object.children(parent)
                str1=child[0].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(1)
                status='pass'
            return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e)) 
        
def CollectingEthernet_wifi_text():
    try:
        if object.exists(networkSelect):
            parent=findObject(networkSelect)  
            child=object.children(parent)
            item0=object.children(child[0])
            collay=object.children(item0[0])
            btn0=object.children(collay[0])
            Rec0=object.children(btn0[0])
            col0=object.children(Rec0[0])
            #Collecting ethernet text
            str1=col0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #collecting connected/disconnected text
            str1=col0[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting Wi-fi text
            btn1=object.children(collay[1])
            Rec0=object.children(btn1[0])
            col0=object.children(Rec0[0])
            ##Collecting Wi-fi text
            str1=col0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #collecting connected/disconnected text
            str1=col0[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)

            status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
                    
                               
                

'Localization testing-Export screen and service screen'


scrollviewId_service={"container": mainWindow, "id": "scrollviewId", "type": "ScrollView", "unnamed": 1, "visible": True}

def CollectingTextfromServicescreenSettings():
    try:
        status='fail'
        if object.exists(scrollviewId_service):
            parent=findObject(scrollviewId_service)
            child=object.children(parent)
            Flick0=object.children(child[0])
            item0=object.children(Flick0[0])
            col00=object.children(item0[0])
            #collecting Upgrade firmware in A-module text
            Row0=object.children(col00[0])
            str1=Row0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting factory reset
            Row1=object.children(col00[1])
            str1=Row1[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting printer check text
            Row3=object.children(col00[3])
            str1=Row3[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting export to USB and warning msg
            col2=object.children(col00[2])
            str1=col2[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            col2=object.children(col00[2])
            row0=object.children(col2[0])
            str1=row0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass' 
        return True if status=='pass' else False     
                  
    except Exception as e:
        test.log('exception'+str(e))

#Collecting 3rd text from child
def Collectingtextsfrom_3rdchild_text(*arguments):
    try:
        status='fail'
        for obj in arguments:
            if object.exists(obj):
                parent=findObject(obj)
                child=object.children(parent)
                str1=child[3].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(2)
                status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
 
#Collecting warning message factory reset
def collectingwarningmessage_ServicescreenSettings(*arguments):
    try:
        #Clicking on Reset button button in service screen
        status='fail'
        for obj in arguments:
            if waitForObject(obj):
                if object.exists(obj):
                    mouseClick(obj)
                    snooze(1)
                    if object.exists(confirmPopupItemId_Autologin):
                        collectingwarning_text(confirmPopupItemId_Autologin)
                        Acceptwarning_popup(cancelButtonId)
                        snooze(3)
                        status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
        
 
confirmButtonId_factoryreset={"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
        
#Do factory reset and collecting text factory reset successful
def dofactoryreset(obj):
    try:
        #Clicking on Reset button button in service screen
        status='fail'
        if waitForObject(obj):
            if object.exists(obj):
                mouseClick(obj)
                snooze(1)
                if object.exists(confirmPopupItemId_Autologin):
                    snooze(1)
                    Acceptwarning_popup(confirmButtonId_factoryreset)
                    snooze(3)
                    status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))        
 
#Collecting factory reset msg succesful message
def collectfactoryresetmsg():
    try:
        status='fail'    
        if waitForObject(okButtonIdFactory):
            if object.exists(okButtonIdFactory):
                mouseClick(okButtonIdFactory)
                #snooze(1)
                #if object.exists(confirmPopupItemId_Autologin):
                    #snooze(1)
                    #Acceptwarning_popup(confirmButtonId_factoryreset)
                    #snooze(3)
                status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e)) 
        
        
 
#Collecting failed to export logs... 
def collectingwarningmessage_Servicescreen_Exportlogs(obj):
    try:
        status='fail'
        if waitForObject(obj):
            if object.exists(obj):
                mouseClick(obj)
                snooze(15)
                if object.exists(appContrllerPopupItemId):
                    collectingwarning_text(appContrllerPopupItemId)
                    Acceptwarning_popup(okButtonId)
                    snooze(1)
                    status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))

warningMessageId_Amodulefwfail={"container": mainWindow, "id": "genericPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
okButtonId_Amodulefwfail={"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}


#Click on upgrade button and collect text about FW upgrade
def collectingwarningmessage_Amodule_FWupmessage(obj):
    try:
        status='fail'
        if waitForObject(obj):
            if object.exists(obj):
                mouseClick(obj)
                snooze(1)
                if object.exists(contentRectId):
                    parent=findObject(contentRectId)
                    child=object.children(parent)
                    #Collecting Do not power off device or disconnect A-Module under any circumstances.Please wait...
                    str1=child[0].text
                    addtolist1(str1)
                    test.log('Collected string ='+str(str1))
                    snooze(3)
                    #Collecting Firmware upgrade in progress...
                    str1=child[2].text
                    addtolist1(str1)
                    test.log('Collected string ='+str(str1))
                    snooze(180)
                    status='pass'
                    if object.exists(warningMessageId_Amodulefwfail):
                        collectingwarning_text(warningMessageId_Amodulefwfail)
                        Acceptwarning_popup(okButtonId_Amodulefwfail)
                        snooze(1)
                    
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))

scrollviewId_Servicescreen={"container": mainWindow, "id": "scrollviewId", "type": "ScrollView", "unnamed": 1, "visible": True}
serviceAccessEntryTextId={"container": mainWindow, "id": "serviceAccessEntryTextId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
Acesskey_textip={"container": mainWindow, "echoMode": 0, "id": "textInputId", "type": "TextField", "unnamed": 1, "visible": True}
servicescreen_validatekeyID={"checkable": False, "container": mainWindow, "id": "serviceKeyCheckId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
appContrllerPopupItemId_servicescreen={"container": mainWindow, "id": "appContrllerPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
okButtonId_servicescreen={"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}


def servicescreen_serviceacess():
    try:
        status='fail'
        if object.exists(scrollviewId_Servicescreen):
            parent=findObject(scrollviewId_Servicescreen)
            child=object.children(parent)
            Flick=object.children(child[0])
            item0=object.children(Flick[0])
            col0=object.children(item0[0])
            col4=object.children(col0[4])
            #collecting service Access text
            str1=col4[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #Collecting access key text
        if object.exists(serviceAccessEntryTextId):
            parent=findObject(serviceAccessEntryTextId)
            child=object.children(parent)
            #collecting service Access text
            str1= child[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
 
#Function to get access text and collecting alert text
def Servicescreen_enertingthekeyandcollectingalerttext():
    try: 
        status='fail'
        if object.exists(servicescreen_validatekeyID):
            parent=findObject(servicescreen_validatekeyID)
            child=object.children(parent)
            str1= child[3].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
            mouseClick(servicescreen_validatekeyID)
            snooze(25)
            if object.exists(appContrllerPopupItemId_servicescreen):
                    collectingwarning_text(appContrllerPopupItemId_servicescreen)
                    Acceptwarning_popup(okButtonId_servicescreen)
                    snooze(1)
                    status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
        
        
        
        
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))        
        

'Localization testing-About screen'
#Collect Text from the About screen

def CollectingTextfromAboutcreenSettings():
    try:
        status='fail'
        if object.exists(scrollviewId):
            parent=findObject(scrollviewId)
            child=object.children(parent)
            Flick=object.children(child[0])
            item0=object.children(Flick[0])
            col0=object.children(item0[0])
            col00=object.children(col0[0])
            #Collecting device details text
            str1=col00[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Device software version text
            col1=object.children(col00[1])
            str1=col1[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Device model text
            col2=object.children(col00[2])
            str1=col2[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Device serial number text
            col3=object.children(col00[3])
            str1=col3[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collect Memory text
            col1=object.children(col0[1])
            str1=col1[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            col11=object.children(col1[1])
            #collecting Space left for text
            str1=col11[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting 20sec ECG record or 20 min rhythm 
            str1=col11[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
            return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
   

#Collecting text from more details in about screen

def additionalInfoColumnId_text_aboutscreen():
    try:
        status='fail'

        if object.exists(scrollviewId):
            parent=findObject(scrollviewId)
            child=object.children(parent)
            Flick=object.children(child[0])
            item0=object.children(Flick[0])
            col0=object.children(item0[0])
            adinfo=object.children(col0[2])
            adinfo1=object.children( adinfo[1])
            Row0=object.children(adinfo1[0])
            #Collecting 'More details'  text
            str1=Row0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            '''
            #collecting 'device IP address' text
            Row_1=object.children(adinfo1[1])
            C1=object.children(Row_1[0])
            str1=C1[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting 'device eth0 IP' address
            C1=object.children(Row_1[1])
            str1=C1[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting for developers only text
            str1=adinfo1[10].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            '''
            status='pass'
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))
        
#Collecting text from more details in about screen 
       
def additionalInfoColumnId_text_aboutscreen1():
    try:
        status='fail'
        if object.exists(scrollviewId):
            parent=findObject(scrollviewId)
            child=object.children(parent)
            Flick=object.children(child[0])
            item0=object.children(Flick[0])
            col0=object.children(item0[0])
            adinfo=object.children(col0[2])
            adinfo1=object.children( adinfo[1])
            for x in range(1,(len(adinfo1)-1)):
                a=object.children(adinfo1[x])
                str1=a[0].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))   
                snooze(1)
        return True if status=='pass' else False                   
    except Exception as e:
        test.log('exception'+str(e))  
                

# Set selected Language and verify selected Language is set or not (main method)

def selectLanguageinSettingsandVerify(Language,Settings,Recording,PrimaryusedID,BTLworkflow):
    try:
        status='fail'
        step1=Onlinesccreentomenuscreen()
        snooze(1)
        step2=navigateToSettingsScreenFromMenuScreen()
        snooze(1)
        step3=selectComboBoxItem(waitForObject(Langauge_customComboBoxId),Language)
        snooze(1)
        step4=navigateToProfileButtonInSettingsScreen()
        snooze(1)
        #Navigating to auto profile
        step5=navigateToAutoProfileInSettingsScreen()
        snooze(1)
        step6=selectComboBoxItem(waitForObject(adaptiveWorklflowSelectionId),BTLworkflow) 
        snooze(1)
        step7=navigateToPatientCardInSettingsScreen()
        snooze(2)
        #Set PID as primary used ID
        step8=selectComboBoxItem(waitForObject(primaryIdSelectorId),PrimaryusedID) 
        snooze(1)
        step9=CollectSettingsTexttext()
        snooze(1)
        step10=CollectMenuRecordingText()
        snooze(1)
        step11=navigateToLiveScreenFromMenuScreen()
        snooze(1)
        
        if (str(step9)==Settings) and (str(step10)==Recording):
            if step1 and step2 and step3 and step4 and step5 and step6 and step7 and step8 and step11:
                status='pass'
        
        return True if status=='pass' else False
    
    except Exception as e:
        test.log('exception'+str(e))
        
        
# Set selected Language and verify selected Language is set or not (Work around method method)

def selectLanguageinSettingsandVerifyWorkaroundmethod(LanguageID,Settings,Recording,PrimaryusedID,BTLworkflow):
    try:
        status='fail'
        step1=Onlinesccreentomenuscreen()
        snooze(1)
        step2=navigateToSettingsScreenFromMenuScreen()
        snooze(1)
        step3=ComboboxValueToselectWorkaround(Langauge_customComboBoxId,LanguageID)
        snooze(1)
        step4=navigateToProfileButtonInSettingsScreen()
        #Navigating to auto profile
        step5=navigateToAutoProfileInSettingsScreen()
        snooze(1)
        step6=ComboboxValueToselectWorkaround(adaptiveWorklflowSelectionId,BTLworkflow) 
        snooze(1)
        step7=navigateToPatientCardInSettingsScreen()
        snooze(2)
        #Set PID as primary used ID
        step8=ComboboxValueToselectWorkaround(primaryIdSelectorId,PrimaryusedID) 
        snooze(1)
        step9=CollectSettingsTexttext()
        snooze(1)
        step10=CollectMenuRecordingText()
        snooze(1)
        step11=navigateToLiveScreenFromMenuScreen()
        snooze(1)
        
        if (str(step9)==Settings) and (str(step10)==Recording):
            if step1 and step2 and step3 and step4 and step5 and step6 and step7 and step8 and step11:
                status='pass'
        
        return True if status=='pass' else False
    
    except Exception as e:
        test.log('exception'+str(e))




#Collecting settings text from settings screen
def CollectSettingsTexttext():
    try:
        status='fail'
        if findObject(settingstextID):
            parent=findObject(settingstextID) 
            column_0=object.children(parent) 
            child=object.children(column_0[0])
            str1=child[1].text
            return str1
            status='pass'
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e))
        
#Collecting settings text from settings and recording text from menu screen
        
def CollectMenuRecordingText(): 
    try:
        #status='fail'
        if Backtomenuscreenfromsettingsscreen():
            test.log('Navigated to menu screen')
            snooze(2)
        if object.exists(MenuScreenId):
            parent=findObject(MenuScreenId)
            child=object.children(parent)
            Row_3=object.children(child[3])
            column_0=object.children(Row_3[0])
            str2=column_0[1].text
            return str2
            status='pass'
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e))    
        
            
            
# Method to navigate to Settings -> Auto profiles settings screen from live waveform screen
def navigateToAutoProfileSettingsFromLive():
    try:
        count =0 
        snooze(5)
        if waitForObject(liveScreenMenuButton):
            mouseClick(waitForObject(liveScreenMenuButton))
            snooze(1)
            
            if waitForObject(menuSettingsButton):
                mouseClick(waitForObject(menuSettingsButton))
                snooze(1)
                
                if waitForObject(profilesSettingsButtonId):
                    mouseClick(waitForObject(profilesSettingsButtonId))                
                    snooze(1)
#                     profilesObj = waitForObject(profilesColumnId)
#                     childOfProfiles = object.children(profilesObj)
#                     manualProfileTab = object.children(childOfProfiles[1])
#                     mouseClick(manualProfileTab[0])
                                       
                    if (object.exists(adaptiveWorklflowSelectionId)):
                        test.log(" Successfully navigated to Auto profiles tab in settings ")
                        count = 1
                    else:
                        test.log(" Fail to navigate to Auto profiles tab in settings ")

                else:
                    test.log(" Profiles option is not displayed in settings ")
                
            else:
                test.log(" Settings button is not displayed in menu screen ")
        else:
            test.log(" Menu option is not displayed in live waveform screen ")
                          
        if count == 1:
            return True
        else:
            return False

    except Exception as e:
        test.fail("Exception" + str(e))
        
def navigateToLiveFromSettings():
    try:
        count =0
        snooze(1) 
        if waitForObject(deviceSettingsBackButtonId):
            mouseClick(waitForObject(deviceSettingsBackButtonId))
            snooze(1)
            
            if waitForObject(menuRecordingButton):
                mouseClick(waitForObject(menuRecordingButton))
                
                snooze(2)
                if (findObject(liveScreenMenuButton)):
                    test.log(" Successfully navigated to live from settings page ")
                    count = 1
                else:
                    test.log(" Fail to navigate to live page ")
            else:
                test.fail(" Menu record button is not displayed ")
        else:
            test.fail(" Settings back button is not displayed ")
                          
        if count == 1:
            return True
        else:
            return False

    except Exception as e:
        test.fail("Exception" + str(e))
                   
            
