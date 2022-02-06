import object
#source(findFile('scripts', '../../globalScripts/monitorScreen.py'))

'''Objects of main window'''
mainWindow = {"type": "QQuickWindowQmlImpl", "visible": True}
monitorScreen_MainWindow = {"container": mainWindow, "id": "manualInput", "type": "ManualInputPopup", "unnamed": 1, "visible": True}
evaluationScreen_MainWindow = {"container": mainWindow, "id": "evaluationScreenId", "type": "EvalScreen", "visible": True}
menuScreen_MainWindow = {"container": mainWindow, "id": "menuScreenId", "type": "Rectangle", "visible": True}
patientCardScreen_MainWindow = {"container": mainWindow, "id": "patientScreenId", "type": "PatientCard", "unnamed": 1, "visible": True}
liveSettingsScreen_MainWindow = {"container": mainWindow,  "type": "Rectangle", "visible": True}
livePatientList_MainWindow = {"container": mainWindow, "id": "centreRectId", "type": "Rectangle", "visible": True}
'''Objects of live screen LX'''
onlineScreenSettngsButtonLX = {"checkable": False, "container": mainWindow, "id": "onlineScreenSettingsButtonId", "type": "CircularButton", "visible": True}
'''Objects of live screen LX++'''
liveScreenMenuButton = {"checkable": False, "container": mainWindow, "id": "menuButtonId", "type": "CircularButton","visible": True}
liveScreenECGRecordButton = {"checkable": False, "container": mainWindow, "id": "startButtonId", "type": "Button",  "visible": True}
liveScreenManualPrintButton = {"checkable": False, "container": mainWindow, "id": "manualPrintButtonId", "type": "CircularButton", "visible": True}
liveScreenSpeedAndGainButton = {"container": mainWindow, "id": "onlineScreenSettingsButtonId", "type": "SettingsButton",  "visible": True}
liveScreenSettingsButton = {"container": mainWindow, "source": "qrc:/qml/images/1280x800/settingsactive.png", "type": "Image",  "visible": True}
liveScreenAbortECG = {"checkable": True, "container": mainWindow, "id": "abortRecordingButtonId", "type": "AbortRecordingButton", "unnamed": 1, "visible": True}
lowBatteryRecordConfirmationButtonLiveScreen = {"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "visible": True}
liveScreenMonitor = {"container": mainWindow, "id": "onlineScreenMonitorContainerId", "type":"Item",  "visible": True}
liveScreenWeightText = {"container": mainWindow, "id":"weightValueId" , "type": "TextInfo", "visible": True}
liveScreenHeightText = {"container": mainWindow, "id": "heightValueId", "type": "TextInfo",  "visible": True}
liveScreenPatientNameDisplay = {"container": mainWindow, "id": "patientNameId", "type": "Label","visible": True}
liveScreenPatientIdDisplay = {"container": mainWindow, "id": "patientidId", "type": "Label","visible": True}
liveScreenPatientStatusBar = {"container": mainWindow, "id": "statusBarId", "type": "ECGStatusBar", "visible": True}
liveScreenPatientListButton = {"checkable": False, "container": mainWindow, "id": "patientButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
manualPrintButtonLiveScreen = {"checkable": False, "container": mainWindow, "id": "manualPrintButtonId", "type": "CircularButton", "visible": True}
resetPatientInLiveScreen = {"checkable": False, "container": mainWindow, "id": "resetPatientToAnonymousButtonId", "type": "DeselectPatientButton", "visible": True}

'''Objects of live settings screen'''
liveSettingsProfileComboBox = {"container": mainWindow, "id": "profileComboBoxId", "type": "ComboBox",  "visible": True}
liveSettingsRecordingTabButton = {"checkable": True, "container": mainWindow, "id": "recordingTabButtonId", "text": "Recording", "type": "TabButton", "visible": True}
liveSettingsDisplayAndPrintTabButton = {"checkable": True, "container": mainWindow, "id": "displayAndPrintTabButtonId", "text": "Display and Print", "type": "TabButton",  "visible": True}
#liveSettingsFilterTabButton = {"checkable": True, "container": mainWindow, "id": "filterTabButtonId", "text": "Filters", "type": "TabButton",  "visible": True}
liveSettingsFilterTabButton = {"checkable": True, "container": mainWindow, "text": "Filters", "type": "TabButton", "visible": True}
#liveSettingsSaveButton = {"checkable": False, "container": mainWindow, "id": "saveSettingsButtonId", "type": "CircularButton",  "visible": True}
liveSettingsSaveButton = {"checkable": False, "container": mainWindow, "id": "saveButtonId", "type": "CircularButton",  "visible": True}
#liveSettingsCancelButton = {"checkable": False, "container": mainWindow, "id": "cancelSettingsButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
liveSettingsCancelButton = {"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton",  "visible": True}
liveSettingsCloseButton = {"container": mainWindow, "id": "closeSettingsButtonId", "type": "CloseDialogButton",  "visible": True}
#profileSelectionLiveScreenSettings = {"container": mainWindow, "id": "profileSelectorItemId", "type": "Item", "visible": True}
profileSelectionLiveScreenSettings = {"container": mainWindow, "id": "profileSelectorId", "type": "CustomComboBoxProfile", "visible": True}

'''Objects of live settings display and print tab button'''
liveSpeed_5 = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CircularRadioButton", "visible": True,"_id":"speed_0"}
liveSpeed_10 = {"checkable": True, "container": mainWindow, "id": "_id",  "type": "CircularRadioButton",  "visible": True,"_id":"speed_1"}
liveSpeed_12_5 = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CircularRadioButton",  "visible": True,"_id":"speed_2"}
liveSpeed_25 = {"checkable": True, "container": mainWindow,"id": "_id", "type": "CircularRadioButton",  "visible": True,"_id":"speed_3"}
liveSpeed_50 = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CircularRadioButton",  "visible": True,"_id":"speed_4"}
liveSpeed_Unit = {"container": mainWindow, "text": "mm/s", "type": "Text", "visible": True}
liveSensitivity_2_5 = {"checkable": True, "container": mainWindow, "id": "_idsensitivity", "type": "CircularRadioButton",  "visible": True, "_idsensitivity":"sensitivity_0"}
liveSensitivity_5 = {"checkable": True, "container": mainWindow, "id": "_idsensitivity", "type": "CircularRadioButton",  "visible": True, "_idsensitivity":"sensitivity_1"}
liveSensitivity_10 = {"checkable": True, "container": mainWindow, "id": "_idsensitivity", "type": "CircularRadioButton",  "visible": True, "_idsensitivity":"sensitivity_2"}
liveSensitivity_20 = {"checkable": True, "container": mainWindow, "id": "_idsensitivity", "type": "CircularRadioButton",  "visible": True, "_idsensitivity":"sensitivity_3"}
liveSensitivity_Unit = {"container": mainWindow, "text": "mm/mV", "type": "Text", "visible": True}
liveSettingsSkipEvaluationYesButton = {"checkable": True, "container": mainWindow, "id": "skipEvaluationYesButtonId", "type": "CustomRadioButton", "visible": True}
liveSettingsSkipEvaluationNoButton = {"checkable": True, "container": mainWindow, "id": "skipEvaluationNoNoButtonId", "type": "CustomRadioButton",  "visible": True}

'''Objects of live screen settings display'''
liveScreenSpeedOfECG = {"container": mainWindow,"id":"speedValId","type": "TextInfo", "visible": True}
liveScreenSensitivityOfECG = {"container": mainWindow,"id":"sensValId","type": "TextInfo",  "visible": True}
liveScreenTypeOfECG = {"container": mainWindow,"id":"examTypeId",  "type": "TextInfo",  "visible": True}
liveScreenLengthOfECG = {"container": mainWindow, "id":"examLengthId","type": "TextInfo",  "visible": True}
liveScreenFilterName = {"container": mainWindow,"id":"filterNameId","type": "TextInfo",  "visible": True}
liveScreenViewName = {"container": mainWindow,"id":"viewNameId","type": "TextInfo", "visible": True}
#liveScreenPatientNameDisplay = {"container": mainWindow, "id": "patientNameId", "type": "Label",  "visible": True}

'''Objects of live settings filter tab button'''
liveSettingsFilterNoneButton = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CustomRadioButton", "_id": "filtergroup0", "visible": True}
liveSettingsFilterAutoButton = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CustomRadioButton", "_id": "filtergroup1", "visible": True}
liveSettingsFilterStrictButton = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CustomRadioButton", "_id": "filtergroup2", "visible": True}
liveSettingsFilterUserButton = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CustomRadioButton", "_id": "filtergroup3", "visible": True}
liveSettingsMainsFiltersComboBox = {"container": mainWindow, "id": "mainsFiltersComboboxId", "type": "ComboBox",  "visible": True}
liveSettingsMainFilterRowId = {"container": mainWindow, "id": "mainFilterRowId", "type": "Item", "visible": True}
liveSettingsDriftFiltersComboBox = {"container": mainWindow, "id": "driftFiltersComboboxId", "type": "ComboBox", "visible": True}
liveSettingsDriftFilterRowId = {"container": mainWindow, "id": "driftFilterRowId", "type": "Item", "visible": True}
liveSettingsMyoFiltersComboBox = {"container": mainWindow, "id": "myoFiltersComboboxId", "type": "ComboBox", "visible": True}
liveSettingsMyoFilterRowId = {"container": mainWindow, "id": "myoFilterRowId", "type": "Item", "visible": True}
liveSettingsFilterSuggestionLabel = {"container": mainWindow, "text": "0.05 Hz filter is recommended for ST observation. <br> 25 Hz filter significantly reduces QRS amplitudes", "type": "Text", "visible": True}
busyIndicatorPrintingLiveScreen = {"container": mainWindow, "id": "busyIndicatorId", "type": "CustomBusyIndicator", "visible": True}
printerTrayOpenPopUpLiveScreen = {"container": mainWindow, "id": "onlinePopupItemId", "type": "WarningPopUp", "visible": True}
printerTrayOpenPopUpConfirmButtonLiveScreen = {"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "CircularButton", "visible": True}
noPaperPopUpLiveScreen = {"container": mainWindow, "id": "onlinePopupItemId", "type": "WarningPopUp", "visible": True}
noPaperPopUpConfirmButtonLiveScreen = {"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "CircularButton", "visible": True}


#objectfromkeerthik
Recordkeerthik = {"checkable": False, "container": mainWindow, "id": "startButtonId", "type": "StartRecordingButton", "unnamed": 1, "visible": True}
Savekeerthik = {"checkable": False, "container": mainWindow, "id": "saveRecordButtonId", "type": "SaveRecordButton", "unnamed": 1, "visible": True}
Saveandonemorekeerthik = {"container": mainWindow, "id": "evalScreenId", "type": "EvalScreen", "unnamed": 1, "visible": True}
liveScreenManualPrintButton = {"checkable": False, "container": mainWindow, "id": "manualPrintButtonId", "type": "CircularButton", "visible": True}
manualPrintstopButtonId ={"checkable": False, "container": mainWindow, "id": "manualPrintButtonId", "type": "ManualPrintButton", "unnamed": 1, "visible": True}
#Localization testing
sidecolumnid ={"container":mainWindow, "id": "sideColumnId", "type": "Rectangle", "unnamed": 1, "visible": True}
bloodpressure= {"container": mainWindow, "id": "systolicInputId", "type": "PatientInfoField", "unnamed": 1, "visible": True}
Recordkeerthik = {"checkable": False, "container": mainWindow, "id": "startButtonId", "type": "StartRecordingButton", "unnamed": 1, "visible": True}
Savekeerthik = {"checkable": False, "container": mainWindow, "id": "saveRecordButtonId", "type": "SaveRecordButton", "unnamed": 1, "visible": True}
Waveformpatientcard ={"checkable": False, "container": mainWindow, "id": "patientButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
Addpatientfromwaveformscreen ={"checkable": False, "container": mainWindow, "id": "addPatientButtonId", "type": "AddNewPatientButton", "unnamed": 1, "visible": True}
Backbutton1fromaddpateinttopatientcard ={"checkable": False, "container": mainWindow, "id": "backPatientCardButtonId", "type": "Button", "unnamed": 1, "visible": True}
#Backbutton2frompatientcard_waveformscreen={"checkable": False, "container": mainWindow, "id": "backPatientCardButtonId", "type": "Button", "unnamed": 1, "visible": True}
#Note:-both back button has same id-try using same I
#object are from the waveform settings screen
Waveformsettingsscreen = {"container":mainWindow, "id": "onlineScreenSettingsButtonId", "type": "SettingsButton", "unnamed": 1, "visible": True}
Recordingtab ={"checkable": True, "container":mainWindow, "id": "recordingTabButtonId", "text": "Recording", "type": "TabButton", "unnamed": 1, "visible": True}
Filtertab = {"checkable": True, "container": mainWindow, "id": "filterTabButtonId", "text": "Filter", "type": "TabButton", "unnamed": 1, "visible": True}
closewindow ={"container": mainWindow, "text": "Current examination settings: settings change for the current examination only", "type": "Label", "unnamed": 1, "visible": True}
saveButtonId ={"checkable": False, "container":mainWindow, "id": "saveButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}

#object from Menu screen and patient card
Menubutton = {"checkable": False, "container":mainWindow, "id": "menuButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
MenuPatientcardbutton={"checkable": False, "container": mainWindow, "id": "menuPatientcardButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
MenuPateintaddbutton ={"checkable": False, "container": mainWindow, "id": "addPatientButtonId", "type": "AddNewPatientButton", "unnamed": 1, "visible": True}
PatientCancelbutton = {"checkable": False, "container": mainWindow, "id": "cancelPatientButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
PatientcardtomenuBackbutton ={"checkable": False, "container": mainWindow, "id": "backPatientCardButtonId", "type": "Button", "unnamed": 1, "visible": True}
MenuRecordingbutton ={"checkable": False, "container": mainWindow, "id": "menuRecordingButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}

#settings screen ID:-
menuSettingsButtonId = {"checkable": False, "container": mainWindow, "id": "menuSettingsButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
Genralsettings= {"container": mainWindow, "id": "deviceSettingsScreenId", "type": "DeviceSettingsScreen", "unnamed": 1, "visible": True}
Profilesettings ={"checkable": True, "container": mainWindow, "id": "profilesSettingsButtonId", "text": "Profiles", "type": "RectangularRadioButton", "unnamed": 1, "visible": True}
Autoprofile = {"container": mainWindow, "id": "profilesColumnId", "type": "Column", "unnamed": 1, "visible": True}
Manualprofile = {"container": mainWindow, "id": "profilesColumnId", "type": "Column", "unnamed": 1, "visible": True}
Rhythmprofile ={"container": mainWindow, "id": "profilesColumnId", "type": "Column", "unnamed": 1, "visible": True}
Printingsettings = {"checkable": True, "container": mainWindow, "id": "printSettingsButtonId", "text": "Printing", "type": "RectangularRadioButton", "unnamed": 1, "visible": True}
Patientcardsettings ={"checkable": True, "container": mainWindow, "id": "patientCardSettingsButtonId", "text": "Patient Card", "type": "RectangularRadioButton", "unnamed": 1, "visible": True}
Networksettings ={"checkable": True, "container": mainWindow, "id": "networkSettingsButtonId", "text": "Network", "type": "RectangularRadioButton", "unnamed": 1, "visible": True}
Exportsettings = {"checkable": True, "container": mainWindow, "id": "exportSettingsButtonId", "text": "Export", "type": "RectangularRadioButton", "unnamed": 1, "visible": True}
Servicesettings = {"checkable": True, "container": mainWindow, "id": "servicePageButtonId", "text": "Service", "type": "RectangularRadioButton", "unnamed": 1, "visible": True}
Aboutsettings = {"checkable": True, "container": mainWindow, "id": "deviceInfoButtonId", "text": "About", "type": "RectangularRadioButton", "unnamed": 1, "visible": True}
settingsbackbutton ={"checkable": False, "container": mainWindow, "id": "deviceSettingsBackButtonId", "type": "Button", "unnamed": 1, "visible": True}
MenuRecordingbutton1 ={"checkable": False, "container":mainWindow , "id": "menuRecordingButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
Deleterecord ={"checkable": False, "container": mainWindow, "id": "deleteRecordButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
confirmbutton = {"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
Evalutionsettingscreen={"container": mainWindow, "id": "evaluationScreenSettingsButtonId", "type": "SettingsButton", "unnamed": 1, "visible": True}
Evalutionsettingscreensavebutton ={"checkable": False, "container":mainWindow, "id": "saveButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
#Object from anaysis screen
Analysisbutton = {"checkable": False, "container": mainWindow, "id": "summarybuttonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
Amplituidebutton ={"checkable": True, "container": mainWindow, "id": "amplitudesTabButtonId", "text": "Amplitudes", "type": "TabButton", "unnamed": 1, "visible": True}
Avgcompbutton = {"checkable": True, "container": mainWindow, "id": "avgComplexesTabButtonId", "text": "Average Complexes", "type": "TabButton", "unnamed": 1, "visible": True}
AbnormalECGbutton ={"checkable": True, "container": mainWindow, "id": "abnormalECGButtonId", "type": "CustomRadioButton", "unnamed": 1, "visible": True}
NormalECGbutton= {"checkable": True, "container": mainWindow, "id": "normalECGButtonId", "type": "CustomRadioButton", "unnamed": 1, "visible": True}
Approvebutton ={"checkable": False, "container": mainWindow, "id": "lockExamButtonId", "type": "LockExamButton", "unnamed": 1, "visible": True}
Savebutton={"checkable": False, "container": mainWindow, "id": "saveButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}

#Worklistobject
worklistobject={"checkable": False, "container": mainWindow, "id": "menuWorklistButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
worklisttomenuscreen =  {"checkable": False, "container": mainWindow, "id": "backPButtonWorklistId", "type": "Button", "unnamed": 1, "visible": True}

#objects in user screen
menuUsersButtonId= {"checkable": False, "container": mainWindow, "id": "menuUsersButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
backButtonUserScreenId ={"checkable": False, "container": mainWindow, "id": "backButtonUserScreenId", "type": "Button", "unnamed": 1, "visible": True}
addUserButtonId ={"checkable": False, "container": mainWindow, "id": "addUserButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
userLoginNameInputId ={"container": mainWindow, "id": "userLoginNameInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
userLastNameInputId = {"container": mainWindow, "id": "userLastNameInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
passwordInputId ={"container": mainWindow, "id": "passwordInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
confirmPasswordInputId ={"container": mainWindow, "id": "confirmPasswordInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
saveUserButtonId ={"checkable": False, "container": mainWindow, "id": "saveUserButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
logButtonId= {"container": mainWindow, "id": "logButtonId", "type": "LogOutButton", "unnamed": 1, "visible": True}

#Object from login screen
loginNameEntryFieldId ={"container": mainWindow, "id": "loginNameEntryFieldId", "type": "PatientInfoField", "unnamed": 1, "visible": True}
loginPasswordInputId = {"container": mainWindow, "id": "loginPasswordInputId", "type": "CustomTextFieldWithLabelAsRow", "unnamed": 1, "visible": True}
loginButton ={"checkable": False, "container": mainWindow, "id": "loginButton", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
#low memeory pop up object
lowmemoryacceptbutton= {"checkable": False, "container":mainWindow, "id": "confirmButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}

'''Language Validation Objects'''

'1) Manual input screen'
onlineScreenMonitorContainerId={"container": mainWindow, "id": "onlineScreenMonitorContainerId", "type": "MonitoredParameterButton", "unnamed": 1, "visible": True}
manualInputId ={"container": mainWindow, "id": "manualInputId", "type": "ManualInputPopup", "unnamed": 1, "visible": True}
manualInputAreaWaveform={"container":mainWindow, "id": "manualInputArea", "type": "Rectangle", "unnamed": 1, "visible": True}
Manualinputtext={"container": mainWindow, "text": "Manual Input", "type": "Label", "unnamed": 1, "visible": True}
mainWindow = {"type": "QQuickWindowQmlImpl", "visible": True}
manualInputArea={"container": mainWindow, "id": "manualInputArea", "type": "Rectangle", "unnamed": 1, "visible": True}
saveManualInputButtonId={"checkable": False, "container":mainWindow, "id": "saveManualInputButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
closeManualInputButtonId={"container": mainWindow, "id": "closeManualInputButtonId", "type": "CloseDialogButton", "unnamed": 1, "visible": True}

'2) Waveform settings screen'
#Object from onlineSettings screen
Waveformsettingsscreen = {"container":mainWindow, "id": "onlineScreenSettingsButtonId", "type": "SettingsButton", "unnamed": 1, "visible": True}
Recordingtab ={"checkable": True, "container":mainWindow, "id": "recordingTabButtonId", "text": "Recording", "type": "TabButton", "unnamed": 1, "visible": True}
Filtertab = {"checkable": True, "container": mainWindow, "id": "filterTabButtonId", "text": "Filter", "type": "TabButton", "unnamed": 1, "visible": True}
closewindow ={"container": mainWindow, "text": "Current examination settings: settings change for the current examination only", "type": "Label", "unnamed": 1, "visible": True}
saveButtonId ={"checkable": False, "container":mainWindow, "id": "saveButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}

headerItemId={"container": mainWindow, "id": "headerItemId", "type": "HeaderItem", "unnamed": 1, "visible": True} 
profileSelectorId={"container": mainWindow, "id": "profileSelectorId", "type": "CustomComboBoxProfile", "unnamed": 1, "visible": True}
profileSelectorItemId={"container": mainWindow, "id": "profileSelectorItemId", "type": "Item", "unnamed": 1, "visible": True}
liveSettingsProfileComboBox = {"container": mainWindow, "id": "profileComboBoxId", "type": "ComboBox",  "visible": True}
liveSettingsRecordingTabButton = {"checkable": True, "container": mainWindow, "id": "recordingTabButtonId", "text": "Recording", "type": "TabButton", "visible": True}
liveSettingsDisplayAndPrintTabButton = {"checkable": True, "container": mainWindow, "id": "displayAndPrintTabButtonId", "text": "Display and Print", "type": "TabButton",  "visible": True}
#liveSettingsFilterTabButton = {"checkable": True, "container": mainWindow, "id": "filterTabButtonId", "text": "Filters", "type": "TabButton",  "visible": True}
liveSettingsFilterTabButton = {"checkable": True, "container": mainWindow, "text": "Filters", "type": "TabButton", "visible": True}
liveSettingsFilterTabID ={"checkable": True, "container": mainWindow, "id": "filterTabButtonId", "text": "Filter", "type": "TabButton", "unnamed": 1, "visible": True}
#liveSettingsSaveButton = {"checkable": False, "container": mainWindow, "id": "saveSettingsButtonId", "type": "CircularButton",  "visible": True}
liveSettingsSaveButton = {"checkable": False, "container": mainWindow, "id": "saveButtonId", "type": "CircularButton",  "visible": True}
#liveSettingsCancelButton = {"checkable": False, "container": mainWindow, "id": "cancelSettingsButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
liveSettingsCancelButton = {"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton",  "visible": True}
liveSettingsCloseButton = {"container": mainWindow, "id": "closeSettingsButtonId", "type": "CloseDialogButton",  "visible": True}
#profileSelectionLiveScreenSettings = {"container": mainWindow, "id": "profileSelectorItemId", "type": "Item", "visible": True}
profileSelectionLiveScreenSettings = {"container": mainWindow, "id": "profileSelectorId", "type": "CustomComboBoxProfile", "visible": True}

'''Objects of live settings display and print tab button'''
liveSpeed_5 = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CircularRadioButton", "visible": True,"_id":"speed_0"}
liveSpeed_10 = {"checkable": True, "container": mainWindow, "id": "_id",  "type": "CircularRadioButton",  "visible": True,"_id":"speed_1"}
liveSpeed_12_5 = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CircularRadioButton",  "visible": True,"_id":"speed_2"}
liveSpeed_25 = {"checkable": True, "container": mainWindow,"id": "_id", "type": "CircularRadioButton",  "visible": True,"_id":"speed_3"}
liveSpeed_50 = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CircularRadioButton",  "visible": True,"_id":"speed_4"}
liveSpeed_Unit = {"container": mainWindow, "text": "mm/s", "type": "Text", "visible": True}
liveSensitivity_2_5 = {"checkable": True, "container": mainWindow, "id": "_idsensitivity", "type": "CircularRadioButton",  "visible": True, "_idsensitivity":"sensitivity_0"}
liveSensitivity_5 = {"checkable": True, "container": mainWindow, "id": "_idsensitivity", "type": "CircularRadioButton",  "visible": True, "_idsensitivity":"sensitivity_1"}
liveSensitivity_10 = {"checkable": True, "container": mainWindow, "id": "_idsensitivity", "type": "CircularRadioButton",  "visible": True, "_idsensitivity":"sensitivity_2"}
liveSensitivity_20 = {"checkable": True, "container": mainWindow, "id": "_idsensitivity", "type": "CircularRadioButton",  "visible": True, "_idsensitivity":"sensitivity_3"}
liveSensitivity_Unit = {"container": mainWindow, "text": "mm/mV", "type": "Text", "visible": True}
livesettings0_5x={"checkable": True, "container": mainWindow, "type": "CustomRadioButton", "unnamed": 1, "visible": True}
livesettings1_x={"checkable": True, "container": mainWindow, "occurrence": 2, "type": "CustomRadioButton", "unnamed": 1, "visible": True}
livescreenhalfchestsensitvity={"container": mainWindow, "id": "chestLeadsHalfSensitivitySelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
livescreenhalfchestsensitvity_on={"checkable": True, "container":mainWindow, "occurrence": 3, "type": "CustomRadioButton", "unnamed": 1, "visible": True}
livescreenhalfchestsensitvity_off={"checkable": True, "container": mainWindow, "occurrence": 4, "type": "CustomRadioButton", "unnamed": 1, "visible": True}
TypewordId={"container": mainWindow, "text": "Type:", "type": "Label", "unnamed": 1, "visible": True}
ECGwordID={"container": mainWindow, "occurrence": 2, "text": "ECG", "type": "Label", "unnamed": 1, "visible": True}
LengthofRecordID={"container":mainWindow, "text": "Length of record", "type": "Label", "unnamed": 1, "visible": True}
Recordinglength_10={"checkable": True, "container": mainWindow, "type": "CustomRadioButton", "unnamed": 1, "visible": True}
Recordinglength_12={"checkable": True, "container": mainWindow, "occurrence": 2, "type": "CustomRadioButton", "unnamed": 1, "visible": True}
Recordinglength_15={"checkable": True, "container": mainWindow, "occurrence": 3, "type": "CustomRadioButton", "unnamed": 1, "visible": True}
Recordinglength_20={"checkable": True, "container": mainWindow, "occurrence": 4, "type": "CustomRadioButton", "unnamed": 1, "visible": True}
Mainfilterword={"container": mainWindow, "text": "Mains", "type": "Label", "unnamed": 1, "visible": True}
Driftfilterword={"container": mainWindow, "text": "Drift", "type": "Label", "unnamed": 1, "visible": True}
Myofilterword={"container": mainWindow, "text": "Myo", "type": "Label", "unnamed": 1, "visible": True}

NonefilterID={"checkable": True, "container": mainWindow , "occurrence": 3, "type": "CustomRadioButton", "unnamed": 1, "visible": True}


NonemainsfilterID={"container": mainWindow, "id": "mainsFiltersComboboxId", "type": "CustomComboBox", "unnamed": 1, "visible": True}
NonedriftfilterID={"container": mainWindow, "id": "driftFiltersComboboxId", "type": "CustomComboBox", "unnamed": 1, "visible": True}
NoneMyofilterID={"container": mainWindow, "id": "myoFiltersComboboxId", "type": "CustomComboBox", "unnamed": 1, "visible": True}
Driftfilterwarningmsg={"container": mainWindow, "text": "0.049 Hz filter can be used for ST observation.", "type": "Label", "unnamed": 1, "visible": True}
Myofilterwarningmsg={"container": mainWindow, "text": "170Hz filter preserves QRS amplitudes.", "type": "Label", "unnamed": 1, "visible": True}
livecomboboxprofileselectorID={"container": mainWindow, "id": "profileSelectorId", "type": "CustomComboBoxProfile", "unnamed": 1, "visible": True}
Autoprofileselection={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "type": "ItemDelegate", "unnamed": 1, "visible": True}

AutofilterbuttonID={"checkable": True, "container": mainWindow, "occurrence": 4, "type": "CustomRadioButton", "unnamed": 1, "visible": True}


Mains_50Hz={"container": mainWindow, "id": "mainsFiltersComboboxId", "type": "CustomComboBox", "unnamed": 1, "visible": True}
mainsFiltersComboboxId={"container": mainWindow, "id": "mainsFiltersComboboxId", "type": "CustomComboBox", "unnamed": 1, "visible": True}
mains_60Hz={"checkable": False, "container":mainWindow, "id": "comboBoxDelegateId", "occurrence": 2, "type": "ItemDelegate", "unnamed": 1, "visible": True}

myoFilterWarningId={"container": mainWindow, "text": "Adaptive filter preserves QRS amplitudes.", "type": "Label", "unnamed": 1, "visible": True}
StrictfilterID={"checkable": True, "container": mainWindow, "occurrence": 5, "type": "CustomRadioButton", "unnamed": 1, "visible": True}
UserfilterID={"checkable": True, "container": mainWindow, "occurrence": 6, "type": "CustomRadioButton", "unnamed": 1, "visible": True}

driftfilter_0_049Hz={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "type": "ItemDelegate", "unnamed": 1, "visible": True}
driftfilter_0_05Hz={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 2, "type": "ItemDelegate", "unnamed": 1, "visible": True}
driftfilter_0_25Hz={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 3, "type": "ItemDelegate", "unnamed": 1, "visible": True}
driftfilter_0_07Hz={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 4, "type": "ItemDelegate", "unnamed": 1, "visible": True}
driftfilter_90Hz={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 5, "type": "ItemDelegate", "unnamed": 1, "visible": True}

myofilter_170Hz={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "type": "ItemDelegate", "unnamed": 1, "visible": True}
myofilter_35Hz={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 2, "type": "ItemDelegate", "unnamed": 1, "visible": True}
myofilter_20Hz={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 3, "type": "ItemDelegate", "unnamed": 1, "visible": True}
myofilter_25Hz={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 4, "type": "ItemDelegate", "unnamed": 1, "visible": True}
myofilter_90Hz={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 5, "type": "ItemDelegate", "unnamed": 1, "visible": True}

driftFiltersComboboxId={"container": mainWindow, "id": "customComboBoxId", "occurrence": 10, "type": "CustomComboBox", "unnamed": 1, "visible": True}


myoFiltersComboboxId_0_07Hz={"container": mainWindow, "id": "myoFiltersComboboxId", "type": "CustomComboBox", "unnamed": 1, "visible": True}
myoFiltersComboboxId={"container": mainWindow, "id": "customComboBoxId", "occurrence": 11, "type": "CustomComboBox", "unnamed": 1, "visible": True}


#filter warning message

#Manual profile id
Manualprofileselection={"checkable": False, "container":mainWindow, "id": "comboBoxDelegateId", "occurrence": 2, "type": "ItemDelegate", "unnamed": 1, "visible": True}
#Manualprofileselection
Manualprofileselection={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 2, "type": "ItemDelegate", "unnamed": 1, "visible": True}
Rhythmprofileselection={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 3, "type": "ItemDelegate", "unnamed": 1, "visible": True}
Recordinglength_30sec={"checkable": True, "container": mainWindow, "type": "CustomRadioButton", "unnamed": 1, "visible": True}
Recordinglength_1min={"checkable": True, "container": mainWindow, "occurrence": 2, "type": "CustomRadioButton", "unnamed": 1, "visible": True}
Recordinglength_2min={"checkable": True, "container": mainWindow, "occurrence": 3, "type": "CustomRadioButton", "unnamed": 1, "visible": True}
Recordinglength_6min={"checkable": True, "container": mainWindow, "occurrence": 4, "type": "CustomRadioButton", "unnamed": 1, "visible": True}
Recordinglength_10min={"checkable": True, "container": mainWindow, "occurrence": 5, "type": "CustomRadioButton", "unnamed": 1, "visible": True}
Recordinglength_20min={"checkable": True, "container": mainWindow, "occurrence": 6, "type": "CustomRadioButton", "unnamed": 1, "visible": True}

Recoredleads_max2lead={"container": mainWindow, "text": "Recorded Leads (max. 2)", "type": "Label", "unnamed": 1, "visible": True}
Recoredleads_I={"checkable": True, "container": mainWindow, "type": "CircularCheckBox", "unnamed": 1, "visible": True}
Recoredleads_II={"checkable": True, "container": mainWindow, "occurrence": 2, "type": "CircularCheckBox", "unnamed": 1, "visible": True}
Recoredleads_III={"checkable": True, "container":mainWindow, "occurrence": 3, "type": "CircularCheckBox", "unnamed": 1, "visible": True}
Recoredleads_aVR={"checkable": True, "container": mainWindow, "occurrence": 4, "type": "CircularCheckBox", "unnamed": 1, "visible": True}
Recoredleads_aVL={"checkable": True, "container": mainWindow, "occurrence": 5, "type": "CircularCheckBox", "unnamed": 1, "visible": True}
Recoredleads_aVF={"checkable": True, "container": mainWindow, "occurrence": 6, "type": "CircularCheckBox", "unnamed": 1, "visible": True}
Recoredleads_V1={"checkable": True, "container": mainWindow, "occurrence": 7, "type": "CircularCheckBox", "unnamed": 1, "visible": True}
Recoredleads_V2={"checkable": True, "container": mainWindow, "occurrence": 8, "type": "CircularCheckBox", "unnamed": 1, "visible": True}
Recoredleads_V3={"checkable": True, "container": mainWindow, "occurrence": 9, "type": "CircularCheckBox", "unnamed": 1, "visible": True}
Recoredleads_V4={"checkable": True, "container": mainWindow, "occurrence": 10, "type": "CircularCheckBox", "unnamed": 1, "visible": True}
Recoredleads_V5={"checkable": True, "container": mainWindow, "occurrence": 11, "type": "CircularCheckBox", "unnamed": 1, "visible": True}
Recoredleads_V6={"checkable": True, "container": mainWindow, "occurrence": 12, "type": "CircularCheckBox", "unnamed": 1, "visible": True}
wavefromsettingsclosebutton={"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
warningtext={"container": mainWindow, "text": "Warning", "type": "Label", "unnamed": 1, "visible": True}
warningtextdiscription={"container": mainWindow, "text": "Do you want to close the window without saving the filter changes?", "type": "Label", "unnamed": 1, "visible": True}
PopupconfirmID={"checkable": False, "container":mainWindow, "id": "confirmButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
mainFilterRowId={"container":mainWindow, "id": "mainFilterRowId", "type": "Row", "unnamed": 1, "visible": True}
driftFilterRowId={"container": mainWindow, "id": "driftFilterRowId", "type": "Row", "unnamed": 1, "visible": True}
myoFilterRowId={"container": mainWindow, "id": "myoFilterRowId", "type": "Row", "unnamed": 1, "visible": True}
WarningconfirmItemId={"container": mainWindow, "id": "confirmItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
displayandprintsettingsID={"container": mainWindow, "id": "displayPrintSettingsId", "type": "DisplayPrintSettings", "unnamed": 1, "visible": True}
liveSettingsDisplayAndPrintTabButton1 = {"checkable": True, "container": mainWindow, "id": "displayAndPrintTabButtonId", "type": "TabButton",  "visible": True}
recordingSettingsId={"container": mainWindow, "id": "recordingSettingsId", "type": "RecordingSettings", "unnamed": 1, "visible": True}
Displayandprinttab1={"checkable": True, "container": mainWindow, "id": "displayAndPrintTabButtonId", "type": "TabButton", "unnamed": 1, "visible": True}
Recordingtab={"checkable": True, "container": mainWindow, "id": "recordingTabButtonId", "type": "TabButton", "unnamed": 1, "visible": True}
Filtertab={"checkable": True, "container": mainWindow, "id": "filterTabButtonId","type": "TabButton", "unnamed": 1, "visible": True}
Nonefilterword={"checkable": True, "container":mainWindow, "id": "_id", "type": "CustomRadioButton", "unnamed": 1, "visible": True}
recordingSettingsId={"container": mainWindow, "id": "recordingSettingsId", "type": "RecordingSettings", "unnamed": 1, "visible": True}
FilterdriftandmyomessageID={"container": mainWindow, "id": "filterWarningsId", "type": "Column", "unnamed": 1, "visible": True}

'3) Electrode status screen'
electrodeStatusButtonId={"checkable": False, "container": mainWindow, "id": "electrodeStatusButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
electrodestatusclosebutton={"checkable": False, "container":mainWindow, "id": "cancelButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
headerItemId_Electrodetext={"container": mainWindow, "id": "headerItemId", "type": "Item", "unnamed": 1, "visible": True}
previewItemID={"container": mainWindow, "id": "previewItemID", "type": "Item", "unnamed": 1, "visible": True}
contentItemId={"container": mainWindow, "id": "contentItemId", "type": "Item", "unnamed": 1, "visible": True}
Label_N_RL={"container": mainWindow, "id": "delegateItemId", "index": 0, "type": "Item", "unnamed": 1, "visible": True}
Label_R_RA={"container": mainWindow, "id": "delegateItemId", "index": 1, "type": "Item", "unnamed": 1, "visible": True}
Label_L_LA={"container": mainWindow, "id": "delegateItemId", "index": 2, "type": "Item", "unnamed": 1, "visible": True}
Label_F_LL={"container": mainWindow, "id": "delegateItemId", "index": 3, "type": "Item", "unnamed": 1, "visible": True}
Label_C1_V1={"container": mainWindow, "id": "delegateItemId", "index": 4, "type": "Item", "unnamed": 1, "visible": True}
Label_C2_V2={"container": mainWindow, "id": "delegateItemId", "index": 5, "type": "Item", "unnamed": 1, "visible": True}
Label_C3_V3={"container": mainWindow, "id": "delegateItemId", "index": 6, "type": "Item", "unnamed": 1, "visible": True}
Label_C4_V4={"container": mainWindow, "id": "delegateItemId", "index": 7, "type": "Item", "unnamed": 1, "visible": True}
Label_C5_V5={"container": mainWindow, "id": "delegateItemId", "index": 8, "type": "Item", "unnamed": 1, "visible": True}
Label_C6_V6={"container": mainWindow, "id": "delegateItemId", "index": 9, "type": "Item", "unnamed": 1, "visible": True}

'4)Login and logout screen'
logButtonId= {"container": mainWindow, "id": "logButtonId", "type": "LogOutButton", "unnamed": 1, "visible": True}
loginNameEntryFieldId ={"container": mainWindow, "id": "loginNameEntryFieldId", "type": "PatientInfoField", "unnamed": 1, "visible": True}
loginPasswordInputId = {"container": mainWindow, "id": "loginPasswordInputId", "type": "CustomTextFieldWithLabelAsRow", "unnamed": 1, "visible": True}
loginButton ={"checkable": False, "container": mainWindow, "id": "loginButton", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
loginscreenpasswordID={"container": mainWindow, "id": "loginPasswordInputId", "type": "CustomTextFieldWithLabelAsRow", "unnamed": 1, "visible": True}
loginPopupItemId={"container": mainWindow, "id": "loginPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
skipLoginButtonID={"checkable": False, "container": mainWindow, "id": "skipLoginButton", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
loginscreenaccepterror={"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}

'5) Waveform screen'
patientDetailsRowId={"container": mainWindow, "id": "patientDetailsRowId", "type": "RowLayout", "unnamed": 1, "visible": True}
onlineECGWfId={"container":mainWindow, "id": "onlineECGWfId", "type": "OnlineECGWf", "unnamed": 1, "visible": True}

Warningpopuplowmem={"container": mainWindow, "id": "genericPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
OkButtonID={"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}

#Function to click on ECG record button in live screen
def clickOnECGRecordButtonInLiveScreen():
    try:
        dateandtime=str(datetime.datetime.now())
        snooze(2)
        if waitForObject(liveScreenECGRecordButton):
            if object.exists(liveScreenECGRecordButton):
                mouseClick(liveScreenECGRecordButton)
                test.log("Successfully clicked on record ECG button")
                return True
                #file.write(dateandtime +"Successfully clicked on record ECG button\n")
                snooze(20)
        if object.exists(Warningpopuplowmem):
                mouseClick(OkButtonID)
                test.log('accepted confirm button-') 
                return True   
        if object.exists(lowBatteryRecordConfirmationButtonLiveScreen):
                mouseClick(lowBatteryRecordConfirmationButtonLiveScreen)
                return True
        else:
            test.log("LiveScreen ECG Record button not found")
            return False
    
    except Exception as e:
        test.fail("Exception" +str(e))
        #file.write(dateandtime+ "Exception"+str(e))

        
#Function to reset patient in Live screen
def resetPatientInformationInLiveScreen():
    try:
        status = False
        if waitForObject(resetPatientInLiveScreen):
            if object.exists(resetPatientInLiveScreen):
                mouseClick(waitForObject(resetPatientInLiveScreen))
                status = True
            else:
                test.log("Not Able to reset patient in live screen")
                status = False
        return status
    
    except Exception as e:
        test.fail("Exception" +str(e))

#Function to record the ECG
def recordECGInLiveScreen():
    try:
        snooze(1)
        if object.exists(liveScreenECGRecordButton):
            mouseClick(waitForObject(liveScreenECGRecordButton))
            global timeBeforeRecording
            timeBeforeRecording = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
            onlyTimeBefore = datetime.datetime.now().strftime("%H:%M:%S")
            format = "%H:%M:%S"
            test.log("timeBeforeRecording = %s" %timeBeforeRecording)
            test.log("onlyTimeBefore = %s" %onlyTimeBefore)
            snooze(5)
        
            if waitForObject(evaluationScreenSaveRecordButton):
                global timeAfterRecording
                timeAfterRecording = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
                onlyTimeAfter = datetime.datetime.now().strftime("%H:%M:%S")
                test.log("timeAfterRecording = %s" %timeAfterRecording)
                test.log("onlyTimeAfter = %s" %onlyTimeAfter)
                diff = datetime.datetime.strptime(onlyTimeAfter, format) - datetime.datetime.strptime(onlyTimeBefore, format)
                difference = str(diff)
                test.log("diff=%s" %diff)
                test.log("difference=%s" %difference)
                if "0:00:10"<=difference<="0:00:11":
                    test.log("Successfully ECG is recorded for 0:00:10 seconds")
                else:
                    test.log("ECG recorded %s seconds instead of 0:00:10 seconds" %difference)
                    
        return timeBeforeRecording

    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to click on manual print button in live screen
def clickOnManualPrintButtonInLiveScreen():
    try:
        if object.exists(liveScreenManualPrintButton):
            mouseClick(waitForObject(liveScreenManualPrintButton)) 
            test.log("Successfully clicked on ECG button") 
            
        return True
        
    except Exception as e:
        test.fail("Exception"+str(e))    

#Function to print ECG Report Manually
def manualPrintInLiveScreen():
    if object.exists(liveScreenManualPrintButton):
        mouseClick(waitForObject(liveScreenManualPrintButton)) 
        start = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        startTime = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(10) 
        if object.exists(liveScreenManualPrintButton):
            mouseClick(waitForObject(liveScreenManualPrintButton)) 
    stop = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
    stopTime = datetime.datetime.now().strftime("%H:%M:%S")
    printTime = datetime.datetime.strptime(stopTime, '%H:%M:%S') - datetime.datetime.strptime(startTime, '%H:%M:%S')
    printTime.total_seconds()
    Time =int(printTime.total_seconds())
    test.log("Time=%s"%Time)

#Function to stop the ECG Record  
def abortECGRecordInLiveScreen():
    try:
        snooze(2)
        if object.exists(liveScreenAbortECG):
            mousePress(waitForObject(liveScreenAbortECG))
            snooze(2)
            mouseRelease(waitForObject(liveScreenAbortECG))
            snooze(1)
            if object.exists(liveScreenECGRecordButton) :
                test.passes("Successfully stopped the ECG Recording by clicking on abort ECG Button")
            else:
                test.fail(" ECG recording is not stopped by clicking on abort ECG button")   
        
        return True
    
    except Exception as e:
        test.fail("Exception" +str(e))

#Function to navigate from live screen to menu screen
def navigateToMenuScreenFromLiveScreen():
    try:
        status = False
        snooze(2)
        if waitForObject(liveScreenMenuButton):
            if object.exists(liveScreenMenuButton):
                mouseClick(waitForObject(liveScreenMenuButton))
                snooze(1)
        else:
            #takeScreenShot()
            test.log("Live screen Menu button is not active")
        if waitForObject(menuRecordingButton):
            #test.log("Successfully menu screen is displayed")
            status = True
        
        else:
            #takeScreenShot()
            test.log("Menu screen is not displayed")
            status = False
                   
        return status
        
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to navigate from live screen to menu screen
def navigateToMonitorScreenFromLiveScreen():
    try:
        status = False
        if object.exists(liveScreenMonitor):
            mouseClick(waitForObject(liveScreenMonitor))
            snooze(1)
            if object.exists(monitorScreen_MainWindow):
                test.passes("Successfully monitor screen is displayed")
                status = True
            else:
                test.fail("Monitor screen is not displayed")
                status = False
                   
        return status
        
    except Exception as e:
        test.fail("Exception" +str(e))

#Function to navigate from live screen to  live settings screen
def navigateToLiveSettingsScreenFromLiveScreen():
    try:
        status = False
        if object.exists(liveScreenSettingsButton):
            mouseClick(waitForObject(liveScreenSettingsButton))
            snooze(1)
            if object.exists(mainWindow):
                test.log("Successfully live settings screen is displayed")
                status = True
            else:
                test.log("live settings screen is not displayed")
                status = False   
        
        return status
    
    except Exception as e:
        test.fail("Exception" +str(e))
    
#Function to navigate  to patient list from live screen
def navigateToPatientListScreenFromLiveScreen():
    try:
        status = False
        snooze(1)
        if waitForObject(liveScreenPatientListButton):
            if object.exists(liveScreenPatientListButton):
                mouseClick(liveScreenPatientListButton)
        else:
            #takeScreenShot()
            test.log("Live screen patient button is not active")
        if waitForObject(liveScreenPatientAddButton):
            #test.log("Successfully patient list screen is displayed")
            status = True
        else:
            #takeScreenShot()
            test.log("Patient list screen is not displayed")
            status = False   
        
        return status
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to get the speed and sensitivity values in live screen
def gettingTheSpeedAndSensitivityValuesInLiveScreen():
    try:
        if object.exists(liveScreenSpeedOfECG):
            global speedOfECGInLiveScreen
            speedOfECGInLiveScreen =str(waitForObject(liveScreenSpeedOfECG).text)
            test.log("speedOfECGInLiveScreen=%s" %speedOfECGInLiveScreen)
            
        if object.exists(liveScreenSensitivityOfECG):
            global sensitivityOfECGInLiveScreen
            sensitivityOfECGInLiveScreen =str(waitForObject(liveScreenSensitivityOfECG).text)
            test.log("sensitivityOfECGInLiveScreen=%s" %sensitivityOfECGInLiveScreen)
        
        return speedOfECGInLiveScreen,sensitivityOfECGInLiveScreen
    
    except Exception as e:
        test.fail("Exception" +str(e))  
    
#Function to get the weight and height values in live screen
def gettingWeightAndHeightValuesInLiveScreen():
    try:
        if object.exists(liveScreenMonitor):
            global weightInLiveScreen
            weightInLiveScreen =str(waitForObject(liveScreenWeightText).text)
            test.log("weightInLiveScreen=%s" %weightInLiveScreen)
            
        if object.exists(liveScreenMonitor):
            global heightInLiveScreen
    
            heightInLiveScreen =str(waitForObject(liveScreenHeightText).text)
            test.log("heightInLiveScreen=%s" %heightInLiveScreen)
        return weightInLiveScreen,heightInLiveScreen
    
    except Exception as e:
        test.fail("Exception" +str(e))
                

#Function to set the speed in live screen
def setSpeedInLiveScreen(speed):
    try:
        if object.exists(liveScreenSpeedAndGainButton):
            global newSpeed
            newSpeed = speed
            mouseClick(waitForObject(liveScreenSpeedAndGainButton))
            snooze(1)
            
            if object.exists(liveSettingsDisplayAndPrintTabButton):
                mouseClick(waitForObject(liveSettingsDisplayAndPrintTabButton))
                snooze(1)
                
                if speed==5:
                    mouseClick(waitForObject(liveSpeed_5))
                    test.log("Changed the Speed into %s" %speed)
                elif speed==10:
                    mouseClick(waitForObject(liveSpeed_10))
                    test.log("Changed the Speed into %s" %speed)
                elif speed==12.5:
                    mouseClick(waitForObject(liveSpeed_12_5))
                    test.log("Changed the Speed into %s" %speed)
                elif speed==25:
                    mouseClick(waitForObject(liveSpeed_25))
                    test.log("Changed the Speed into %s" %speed)
                elif speed==50:
                    mouseClick(waitForObject(liveSpeed_50))
                    test.log("Changed the Speed into %s" %speed)
                else:
                    test.log("changes are  not altered")
                    
        return newSpeed
    
    except Exception as e:
        test.fail("Exception" +str(e))

#Function to set the sensitivity in live screen
def setSensitivityInLiveScreen(sensitivity):
    try:
        if object.exists(liveScreenSpeedAndGainButton):
            global newSensitivity
            newSensitivity=sensitivity
            mouseClick(waitForObject(liveScreenSpeedAndGainButton))
            snooze(1)
            
            if object.exists(liveSettingsDisplayAndPrintTabButton):
                mouseClick(waitForObject(liveSettingsDisplayAndPrintTabButton))
                snooze(1)
                if sensitivity==2.5:
                    mouseClick(waitForObject(liveSensitivity_2_5))
                    test.log("Changed the sensitivity into %s" %sensitivity)
                elif sensitivity==5:
                    mouseClick(waitForObject(liveSensitivity_5))
                    test.log("Changed the sensitivity into %s" %sensitivity)
                elif sensitivity==10:
                    mouseClick(waitForObject(liveSensitivity_10))
                    test.log("Changed the sensitivity into %s" %sensitivity)
                elif sensitivity==20:
                    mouseClick(waitForObject(liveSensitivity_20))
                    test.log("Changed the sensitivity into %s" %sensitivity)
                else:
                    test.log("changes are  not altered")
                    
        return newSensitivity
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to set filter values in live screen
def setFilterValuesInLiveScreen(filter):
    try:
        if object.exists(liveScreenSpeedAndGainButton):
            global newFilter
            newFilter = filter
            mouseClick(waitForObject(liveScreenSpeedAndGainButton))
            snooze(1)
            
            if object.exists(liveSettingsFilterTabButton):
                mouseClick(waitForObject(liveSettingsFilterTabButton))
                snooze(1)
                
                if filter == "None":
                    mouseClick(waitForObject(liveSettingsFilterNoneButton))
                    test.log("Changed the filter into %s" %filter)
                elif filter == "Auto":
                    mouseClick(waitForObject(liveSettingsFilterAutoButton))
                    test.log("Changed the filter into %s" %filter)
                elif filter == "Strict":
                    mouseClick(waitForObject(liveSettingsFilterStrictButton))
                    test.log("Changed the filter into %s" %filter)
                elif filter == "User":
                    mouseClick(waitForObject(liveSettingsFilterUserButton))
                    test.log("Changed the filter into %s" %filter)
                else:
                    test.log("changes are  not altered")
                    
        return newFilter
    
    except Exception as e:
        test.fail("Exception" +str(e)) 
        
# Function to return Custom Filter Values of Mains, Drift and myoFilter
def getCustomFilterValueLiveScreen(customFilterName):  
    try:
            global newFilterName
            global customFilterValue
            newCustomFilterName=customFilterName
            if newCustomFilterName == "Main":
                if object.exists(liveSettingsMainsFiltersComboBox):
                    mainFilter = findObject(liveSettingsMainsFiltersComboBox)
                    customFilterValue=mainFilter.currentText
                else:
                    test.log("Could not able to find Mains Filter comboBox")                   
            elif newCustomFilterName == "Drift":
                if object.exists(liveSettingsDriftFiltersComboBox):
                    driftFilter = findObject(liveSettingsDriftFiltersComboBox)
                    customFilterValue=driftFilter.currentText                    
                else:
                    test.log("Could not able to find Drift Filter comboBox")                
            elif newCustomFilterName == "Myo":
                if object.exists(liveSettingsMyoFiltersComboBox):
                    myoFilter = findObject(liveSettingsMyoFiltersComboBox)
                    customFilterValue=myoFilter.currentText 
                else:
                    test.log("Could not able to find Myo Filter comboBox")                                       
            else:
                test.log("Could not get the custom Filter Values for User Filter")
            return customFilterValue
             
    except Exception as e:
        test.fail("Exception" + str(e)) 
# Function to return List values of custom Filter comboBox
def comboBoxListValuesLiveScreen(obj):
    try:
            listValues_A = []
            for i in range (obj.count):
                obj.currentIndex = i
                comboListItem = obj.currentText
                listValues_A.append(str(comboListItem))                       
            return listValues_A           
          
    except Exception as e:
        test.fail("Exception" + str(e)) 
        
# Function to select comboBox List item for custom Filter and verifying 
def selectingCustomFilterValuesLivescreen(obj,listValue):   
    try:
            status = "Fail"            
            listValue_E = listValue
            for i in range (obj.count):
                obj.currentIndex = i
                comboListItem = obj.currentText
                if comboListItem == listValue_E[i]:
                    status = "Pass"
                else:
                    status = "Fail"                    
            return status       
          
    except Exception as e:
        test.fail("Exception" + str(e))
#Function to verify whether object is enabled or disabled
def checkStateOfObjectLiveScreen(obj):
    try:
        status = False
        if obj.focus:
            status = "Enabled"
        else:
            status = "Disabled"
        return status
    except Exception as e:
        test.fail("Exception"+ str(e)) 
        
#Function to verify weight and height in the live screen
def verifyWeightAndHeightInTheLiveScreen(verifyWeight,verifyHeight):
    try:
        if object.exists(liveScreenMonitor):
            weightInLiveScreen =str(waitForObject(liveScreenWeightText).text)
            heightInLiveScreen =str(waitForObject(liveScreenHeightText).text)
        
            if weightInLiveScreen==str(verifyWeight):
                test.passes("Live Screen: Given weight %s and Displayed weight %s values are matched" %(verifyWeight,weightInLiveScreen))
            else:
                test.fail("Live Screen: Given weight %s and Displayed weight %s values are not matched" %(verifyWeight,weightInLiveScreen))
                    
            if heightInLiveScreen==str(verifyHeight):
                test.passes("Live Screen: Given height %s and Displayed height %s values are matched" %(verifyHeight,heightInLiveScreen))
            else:
                test.fail("Live Screen: Given height %s and Displayed height %s values are not matched" %(verifyHeight,heightInLiveScreen))
                
        return True
        
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to verify the  patient name in live screen
def verifyPatientNameInLiveScreen(verifyPatientNameDisplay=""):
    try:
        result=False
        if object.exists(liveScreenPatientNameDisplay):
            patientNameDisplayInLiveScreen = str(waitForObject(liveScreenPatientNameDisplay).text)
            
            
            if verifyPatientNameDisplay==patientNameDisplayInLiveScreen:
                result=True
                test.log("Live Screen: The given patient name %s and displayed patient name %s are matched" %(verifyPatientNameDisplay,patientNameDisplayInLiveScreen))
            else:
                result=False
                test.fail("Live Screen: The given patient name %s and displayed patient name %s are not matched" %(verifyPatientNameDisplay,patientNameDisplayInLiveScreen))
        else:
            result=False
            test.fail("live PatientName display not present")       
        return result
        
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to verify the patient ID and patient name in live screen
def verifyPatientInformationInLiveScreen(surName="",firstName="",patientID=""):
    try:
        status = "Fail"
        if object.exists(liveScreenPatientStatusBar):
            sNameLiveScreen = str(waitForObject(liveScreenPatientStatusBar).lname)
            fNameLiveScreen = str(waitForObject(liveScreenPatientStatusBar).pName)
            pIDLiveScreen = str(waitForObject(liveScreenPatientStatusBar).pId)
            if surName == sNameLiveScreen and firstName == fNameLiveScreen and patientID == pIDLiveScreen:
                test.log("Live Screen: The given patient information and displayed patient information are same")
                status = "Pass"
            else:
                test.log("Live Screen: The given patient information and displayed patient information are not same")
                status = "Fail"
        return status
        
    except Exception as e:
        test.fail("Exception" +str(e))        

#Function to verify the patient ID live screen
def verifyPatientIdInLiveScreen(verifyPatientIdDisplay=""):
    try:
        status = "Fail"
        if object.exists(liveScreenPatientIdDisplay):
            patientIdDisplayInLiveScreen = str(waitForObject(liveScreenPatientIdDisplay).text)
            
            if verifyPatientIdDisplay==patientIdDisplayInLiveScreen:
                test.log("Live Screen: The given patient name %s and displayed patient name %s are matched" %(verifyPatientIdDisplay,patientIdDisplayInLiveScreen))
                status = "Pass"
            else:
                test.log("Live Screen: The given patient name %s and displayed patient name %s are not matched" %(verifyPatientIdDisplay,patientIdDisplayInLiveScreen))
                status = "Fail"
        return status
        
    except Exception as e:
        test.fail("Exception" +str(e))
    
#Function to verify the speed value in live screen
def verifySpeedValuesInLiveScreenAfterChanging(verifySpeed):
    try:
        if object.exists(liveScreenSpeedOfECG):
            speedOfECGInLiveScreen =str(waitForObject(liveScreenSpeedOfECG).text)
            
            if speedOfECGInLiveScreen==str(verifySpeed):
                test.passes("Live Screen: Given speed %s and Displayed speed %s values are matched" %(verifySpeed,speedOfECGInLiveScreen))
            else:
                test.fail("Live Screen: Given speed %s and Displayed speed %s values are not matched" %(verifySpeed,speedOfECGInLiveScreen))
        
        return True
            
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to verify the sensitivity value in live screen
def verifySensitivityValuesInLiveScreenAfterChanging(verifySensitivity):
    try:
        if object.exists(liveScreenSensitivityOfECG):
            sensitivityOfECGInLiveScreen =str(waitForObject(liveScreenSensitivityOfECG).text)
            
            if sensitivityOfECGInLiveScreen==str(verifySensitivity):
                test.passes("Live Screen: Given sensitivity %s and Displayed sensitivity %s values match" %(verifySensitivity,sensitivityOfECGInLiveScreen))
            else:
                test.fail("Live Screen: Given sensitivity %s and Displayed sensitivity %s values does not match" %(verifySensitivity,sensitivityOfECGInLiveScreen))
         
        return True
            
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to verify manual profile in live screen
def verifyManualProfileInWaveformScreen():
    try:
        status = False
        snooze(1)
        if object.exists(manualPrintButtonLiveScreen):
            status = True
        else:
            status = False
        return status
    except Exception as e:
        test.fail("Exception" + str(e))
        
#Function to verify the filter value in live screen
def verifyFilterValuesInLiveScreenAfterChanging(verifyECGFilterName):
    try:
        status = False
        if object.exists(liveScreenFilterName):
            filterNameInLiveScreen =str(waitForObject(liveScreenFilterName).text)
            
            if filterNameInLiveScreen==str(verifyECGFilterName):
                test.log("Live Screen: Given filter name %s and Displayed filter name %s are matched" %(verifyECGFilterName,filterNameInLiveScreen))
                status = True
            else:
                test.log("Live Screen: Given filter name %s and Displayed filter name %s are not matched" %(verifyECGFilterName,filterNameInLiveScreen))
                status = True
        return status
    
    except Exception as e:
        test.fail("Exception" +str(e))

 
#Function to save the values in live settings screen
def saveTheValuesInTheLiveSettingsScreen():
    try:
        if object.exists(liveSettingsSaveButton):
            mouseClick(waitForObject(liveSettingsSaveButton))
            test.log("The values are saved")
            return True
        else:
            test.log("Values are not saved in setting screen")
            return False
       
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to cancel the values in live settings screen
def cancelTheValuesInTheLiveSettingsScreen(speed="",sensitivity=""):
    try:
        if waitForObject(liveSettingsCancelButton):
            mouseClick(waitForObject(liveSettingsCancelButton))
            test.log("The values are cancelled")
            
            if object.exists(liveScreenSpeedOfECG):
                newSpeedOfECGInLiveScreen =str(waitForObject(liveScreenSpeedOfECG).text)
                test.log("speedOfECGInLiveScreen=%s" %newSpeedOfECGInLiveScreen)
    
            if object.exists(liveScreenSensitivityOfECG):
                newSensitivityOfECGInLiveScreen =str(waitForObject(liveScreenSensitivityOfECG).text)
                test.log("sensitivityOfECGInLiveScreen=%s" %newSensitivityOfECGInLiveScreen)
                
            if speed ==newSpeedOfECGInLiveScreen and sensitivity==newSensitivityOfECGInLiveScreen:
                test.passes("Successfully cancelled the values in the live settings screen")
            else:
                test.fail("Values are not cancelled in the live settings screen")
                
        return True
       
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to cancel the values in Live setting screen
def cancelTheValuesInWaveformSettingsScreen():
    try:
        status = "Fail"
        if object.exists(liveSettingsCancelButton):
            mouseClick(waitForObject(liveSettingsCancelButton))
            test.log("The values are cancelled")
            
            if object.exists(mainWindow):
                test.log("Successfully cancelled the values in the waveform settings screen")
                status = "Pass"
            else:
                test.log("Values are not cancelled in the waveform settings screen")
                status = "Fail"
        if status == "Pass" :
            return True
        else:
            return False           
           
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to close the live settings screen without argument
def closeTheLiveSettingsScreenWithoutArgument():
    try:
        status = False
        if object.exists(liveSettingsCloseButton):
            mouseClick(waitForObject(liveSettingsCloseButton))
            snooze(2)
            if object.exists(liveScreenPatientListButton):
                test.log("Successfully navigate to waveform screen")
                status = True
            else:
                test.log("Failed to navigate to waveform screen")
                status = False
        else:
            test.log("Live settings close button is not active")
        return status
       
    except Exception as e:
        test.fail("Exception" +str(e))

#Function to close the live settings screen
def closeTheLiveSettingsScreen(speed="",sensitivity=""):
    try:
        if object.exists(liveSettingsCloseButton):
            mouseClick(waitForObject(liveSettingsCloseButton))
            test.log("The values are cancelled")
            
            if object.exists(liveScreenSpeedOfECG):
                SpeedOfECGInLiveScreen =str(waitForObject(liveScreenSpeedOfECG).text)
                test.log("speedOfECGInLiveScreen=%s" %SpeedOfECGInLiveScreen)
    
            if object.exists(liveScreenSensitivityOfECG):
                SensitivityOfECGInLiveScreen =str(waitForObject(liveScreenSensitivityOfECG).text)
                test.log("sensitivityOfECGInLiveScreen=%s" %SensitivityOfECGInLiveScreen)
                
            if speed ==SpeedOfECGInLiveScreen and sensitivity==SensitivityOfECGInLiveScreen:
                test.passes("Successfully closed the live settings screen")
            else:
                test.fail("Live settings screen is not closed")
            
        return True
       
    except Exception as e:
        test.fail("Exception" +str(e))

#Methods from keerthik

#Create and save and print for every 10th record
def create_andsave1():
 try:
    if waitForObject(liveScreenECGRecordButton):
            if object.exists(liveScreenECGRecordButton):
                mouseClick(liveScreenECGRecordButton)
                test.log("Successfully clicked on record ECG button")
                #file.write(dateandtime +"Successfully clicked on record ECG button\n")
                snooze(15)
            if object.exists(lowmemoryacceptbutton):
                mouseClick(lowmemoryacceptbutton)
                test.log('accepted confirm button-')    
            if object.exists(lowBatteryRecordConfirmationButtonLiveScreen):
                mouseClick(lowBatteryRecordConfirmationButtonLiveScreen)

 except Exception as b:
     test.log('Not able to find the record button'+str(b))
     takeScreenShot()              
   
def savepatient(): 
    try:          
         if waitForObject(Savekeerthik):
                if object.exists(Savekeerthik):
                    mouseClick(Savekeerthik)
                    test.log('Succesfully clicked  save button for the time')
                    snooze(5)
    except Exception as b:
        test.log('Not able to find the record button'+str(b))
        takeScreenShot()

#Navigating to patient card waveform screen
#Patient card from online screen>Add patient> back button>back button to recording screen
def Navigatetopatientcard_waveformscreen():
 try:
    if waitForObject(Waveformpatientcard):
        if object.exists(Waveformpatientcard):
            mouseClick(Waveformpatientcard)
            test.log('Able to find the waveform patient card')
            snooze(2)
            if waitForObject(Addpatientfromwaveformscreen):
                if object.exists(Addpatientfromwaveformscreen):
                    mouseClick(Addpatientfromwaveformscreen)
                    test.log('Able to find the add button in patient card')
                    snooze(2)
                    for i in range(2):
                         if waitForObject(Backbutton1fromaddpateinttopatientcard):
                             if object.exists(Backbutton1fromaddpateinttopatientcard):
                                  mouseClick(Backbutton1fromaddpateinttopatientcard)
                                  test.log('Able to find the back button1 in examintaion screen')
                                  snooze(2)
 except Exception as c:
     test.log('Exception occured'+str(c))
     
#Waveform settings screen from online screen>Recording tab>Filter tab>close window   
def waveformsettings():
 try:
    snooze(10)
    if waitForObject(Waveformsettingsscreen):
        if object.exists(Waveformsettingsscreen):
            mouseClick(Waveformsettingsscreen)
            test.log('Waveform settings button clicked')
            snooze(3)
            if waitForObject(Recordingtab):
                if object.exists(Recordingtab):
                    mouseClick(Recordingtab)
                    test.log('Recording tab clicked')
                    if waitForObject(Evalutionsettingscreensavebutton):
                                if object.exists(Evalutionsettingscreensavebutton):
                                    mouseClick(Evalutionsettingscreensavebutton)
                                    test.log('Closed window without modifying anything')
                                    snooze(5)
 except Exception as d:
     test.log('Exception occured'+str(d))
     takeScreenShot()
     
#Evalution screen settings button:
def Evalutionwaveformsettings():
 try:
    if waitForObject(Evalutionsettingscreen):
        if object.exists(Evalutionsettingscreen):
            mouseClick(Evalutionsettingscreen)
            test.log('Waveform settings button clicked')
            if waitForObject(Recordingtab):
                if object.exists(Recordingtab):
                    mouseClick(Recordingtab)
                    test.log('Recording tab clicked')
                    if waitForObject(Filtertab):
                        if object.exists(Filtertab):
                            mouseClick(Filtertab)
                            test.log('Filter tab clicked')
                            snooze(3)
                            if waitForObject(Evalutionsettingscreensavebutton):
                                if object.exists(Evalutionsettingscreensavebutton):
                                    mouseClick(Evalutionsettingscreensavebutton)
                                    test.log('Closed window without modifying anything')

 except Exception as d1:
     test.log('Exception occured'+str(d1))
     takeScreenShot()
 
 #Menu>Patient card    
def Menuscreen_Patientcardbutton():
 try:
    if waitForObject(Menubutton):
        if object.exists(Menubutton):
            mouseClick(Menubutton)
            test.log('Menu button clicked and navigated to the menu')
            if waitForObject(MenuPatientcardbutton):
                if object.exists(MenuPatientcardbutton):
                    mouseClick(MenuPatientcardbutton)
                    test.log('Patient card button clicked from menu screen')
                    if waitForObject(Addpatientfromwaveformscreen):
                        if object.exists(Addpatientfromwaveformscreen):
                            mouseClick(Addpatientfromwaveformscreen)
                            test.log('Able to find the add button in patient card')
                            snooze(2)
                            for i in range(2):
                                if waitForObject(Backbutton1fromaddpateinttopatientcard):
                                    if object.exists(Backbutton1fromaddpateinttopatientcard):
                                        mouseClick(Backbutton1fromaddpateinttopatientcard)
                                        test.log('Able to find the back button1 in examintaion screen')
                                        snooze(2)
 except Exception as e:
     test.log('Exception occured'+str(e))
     takeScreenShot()
     
#Navigating to genral settings screen

def Navigatetosettings():
 try:
    if waitForObject(menuSettingsButtonId):
        object.exists(menuSettingsButtonId)
        mouseClick(menuSettingsButtonId)
        test.log('Navigated to the settings screen')
    status1 = Genralsettings1()
    snooze(1)
    status2 = Profilesettings1()
    snooze(2)
    status3 =Printingsettings1()
    snooze(1)
    status4 =Patientcardsettings1()
    snooze(1)
    status5= Networksettings1()
    snooze(1)
    status6 =Exportsettings1()
    snooze(1)
    status7 =Servicesettings1()
    snooze(1)
    status8= Aboutsettings1()
    snooze(1)
    if status1 and status2  and status3 and status4 and status5 and status6 and status7 and status8:
        test.log('Succesfully switched between all the screen')
 except Exception as z:
     test.log('Exception occured'+str(z))
     takeScreenShot()
    
    
#Genral settings tab
def Genralsettings1():
 try:
    if waitForObject(Genralsettings):
     if object.exists(Genralsettings):
        mouseClick(Genralsettings)
        test.log('Clicked general settings screen')
 except Exception as c:
     test.log('Exception occured'+str(c))
     
def Profilesettings1():
    try:
        if waitForObject(Profilesettings):
         if object.exists(Profilesettings):
            mouseClick(Profilesettings)
            test.log('Clicked profile settings screen')
            if waitForObject(Autoprofile):
             if object.exists(Autoprofile):
                mouseClick(Autoprofile)
                test.log('Clicked auto profile settings screen')
                snooze(2)
                if waitForObject(Manualprofile):
                    if object.exists(Manualprofile):
                        mouseClick(Manualprofile)
                        test.log('Clicked manual profile settings screen')
                        if waitForObject(Rhythmprofile):
                            if object.exists(Rhythmprofile):
                                mouseClick(Rhythmprofile)
                                test.log('Clicked rhythm profile settings screen')
                                snooze(2)
    except Exception as d:
        test.log('Exception occured'+str(d))

def Printingsettings1():
    try:
        if waitForObject(Printingsettings):
         if object.exists(Printingsettings):
            mouseClick(Printingsettings)
            test.log('Clicked printing settings screen')
    except Exception as e:
        test.log('Exception occured'+str(e))     
            
           
def Patientcardsettings1():
     try:
        if waitForObject(Patientcardsettings):
         if object.exists(Patientcardsettings):
            mouseClick(Patientcardsettings)
            test.log('Clicked Patientcardsettings settings screen')
     except Exception as  f:
        test.log('Exception occured'+str(f)) 
    
def Networksettings1():
    try:
        if waitForObject(Networksettings):
         if object.exists(Networksettings):
            mouseClick(Networksettings)
            test.log('Clicked Networksettings settings screen')
    except Exception as g:
        test.log('Exception occured'+str(g)) 

def Exportsettings1():
    try:
        if waitForObject(Exportsettings):
         if object.exists(Exportsettings):
            mouseClick(Exportsettings)
            test.log('Clicked Exportsettings settings screen')
    except Exception as  h:
        test.log('Exception Exportsettings'+str(h)) 
        
def Servicesettings1():
    try:
        if waitForObject(Servicesettings):
         if object.exists(Servicesettings):
            mouseClick(Servicesettings)
            test.log('Clicked Servicesettings settings screen')
    except Exception as i:
        test.log('Exception occured'+str(i))
        
def Aboutsettings1():
    try:
        if waitForObject(Aboutsettings):
         if object.exists(Aboutsettings):
            mouseClick(Aboutsettings)
            test.log('Clicked Aboutsettings settings screen')
    except Exception as j:
        test.log('Exception occured'+str(j))
        
def Backtowaveformscreen():
 try:
      if waitForObject(settingsbackbutton):
          if object.exists(settingsbackbutton):
              mouseClick(settingsbackbutton)
              test.log('back to navigate menu screen')
              if waitForObject(MenuRecordingbutton1):
                  if object.exists(MenuRecordingbutton1):
                      mouseClick(MenuRecordingbutton1)
                      test.log('Back to navigate online screen and iteration is:')
                      snooze(2)
 except Exception as k:
        test.log('Exception occured'+str(k))
        takeScreenShot()
                      
def deleterecord():
    try:
        if waitForObject(Deleterecord):
          if object.exists(Deleterecord):
              mouseClick(Deleterecord)
              test.log('Able to find delete button')
              if waitForObject(confirmbutton):
                  if object.exists(confirmbutton):
                      mouseClick(confirmbutton)
                      test.log('succesfully deleted patient:')
                      snooze(3)
    except Exception as l:
        test.log('Exception occured'+str(l)) 
 

def Analysisscreen():
    try:
        if waitForObject(Analysisbutton):
            object.exists(Analysisbutton)
            mouseClick(Analysisbutton) 
            test.log('Succesfuly clicked analysis button')
            Analysisscreenswitchingalltab()
            if waitForObject(Savebutton):
                object.exists(Savebutton)
                mouseClick(Savebutton)
                test.log('Succesfuly clicked save buttona and navigated to evalution screen')
    except Exception as m:
        test.log('Not able to find object'+str(m))
        takeScreenShot()



def Analysisscreenswitchingalltab():
    try:
        if waitForObject(AbnormalECGbutton):
          object.exists(AbnormalECGbutton)
          mouseClick(AbnormalECGbutton) 
          test.log('Succesfuly abnormal ecg button in  analysis screen')
        if waitForObject(NormalECGbutton):
          object.exists(NormalECGbutton)
          mouseClick(NormalECGbutton) 
          test.log('Succesfuly normal ecg button in  analysis screen')
        if waitForObject(Approvebutton):
          object.exists(Approvebutton)
          mouseClick(Approvebutton) 
          test.log('Succesfuly approved the ecg button in  analysis screen')
        if waitForObject(Amplituidebutton):
            object.exists(Amplituidebutton)
            mouseClick(Amplituidebutton) 
            test.log('Succesfuly amp tab in analysis screen')
        if waitForObject(Avgcompbutton):
          object.exists(Avgcompbutton)
          mouseClick(Avgcompbutton) 
          test.log('Succesfuly avg comp tab in analysis screen')
    except Exception as n:
        test.log('Not able to find object'+str(n))
    

#Navigating to worklist:
def Worklistscreen():
 try:
     if waitForObject(worklistobject):
         object.exists(worklistobject)
         mouseClick(worklistobject)
         test.log('Succesfully clicked worklist button')
         if waitForObject(worklisttomenuscreen):
             object.exists(worklisttomenuscreen)
             mouseClick(worklisttomenuscreen)
             test.log('Succesfully clicked back button and navigated to the menu screen')
 except Exception as o:
        test.log('Not able to find object'+str(o))
        takeScreenShot()

#Navigating to userscreen
def Userscreen():
 try:
    snooze(3)
    if waitForObject(menuUsersButtonId):
         object.exists(menuUsersButtonId)
         mouseClick(menuUsersButtonId)
         test.log('Succesfully clicked users  button and navigated to the users screen')
         if waitForObject(addUserButtonId):
             object.exists(addUserButtonId)
             mouseClick(addUserButtonId)
             test.log('Succesfully clicked users  button and navigated to the users screen')
             '''if i<25:
                  login=i
                  lastname='Shetty'
                  newpassword='qwertyuio'
                  confirmpassowrd='qwertyuio'
                  Addusers(login,lastname,newpassword,confirmpassowrd)
                  snooze(6)
                  if waitForObject(backButtonUserScreenId):
                      object.exists(backButtonUserScreenId)
                      mouseClick(backButtonUserScreenId)
                      test.log('Navigated to user screens')'''
             for a in range(2):       
                 if waitForObject(backButtonUserScreenId):
                     object.exists(backButtonUserScreenId)
                     mouseClick(backButtonUserScreenId)
                     test.log('Navigated to menu screen')
                    
 except Exception as p:
     test.log('Issue in user screen:'+str(p))
     takeScreenShot()
                        
def Addusers(login,lastname,newpassword,confirmpassowrd):
 try:
   if object.exists(userLoginNameInputId):           
       setFocusTextBox(userLoginNameInputId)
       type(mainWindow,login+26)
       if object.exists(userLastNameInputId):
           setFocusTextBox(userLastNameInputId)
           type(mainWindow,lastname)
           if object.exists(passwordInputId):
               setFocusTextBox(passwordInputId)
               type(mainWindow,newpassword)
               snooze(5)
               if object.exists(confirmPasswordInputId):
                   setFocusTextBox(confirmPasswordInputId)
                   type(mainWindow,confirmpassowrd)
                   if waitForObject(saveUserButtonId):
                       object.exists(saveUserButtonId)
                       mouseClick(saveUserButtonId)
                       test.log('succesfuly created the user:-'+str(i))
                                 
 except Exception as o:
        test.log('Not able to find object'+str(o)) 
               
                        
def setFocusTextBox(obj):
    try:
        targetTextBox=obj
        if (findObject(targetTextBox)):
            mouseClick(targetTextBox)

        else:
            test.log("Unable to set focus on text box ")            
    except Exception as e:
        test.fail("Exception" +str(e))
  
  
def logoutandlogin():
    try:
        if waitForObject(logButtonId):
            object.exists(logButtonId)
            mouseClick(logButtonId)
            test.log('Succesfuly logged out from the user')
            snooze(2)
            if object.exists(loginNameEntryFieldId):
                setFocusTextBox(loginNameEntryFieldId)
                type(mainWindow,'admin')
                test.log('Succesfully entered login id')
                snooze(3)
                if object.exists(loginPasswordInputId):
                    setFocusTextBox(loginPasswordInputId)
                    type(mainWindow,'qaqaqaqa')
                    test.log('Succesfully entered password')
                    snooze(5)
                    if waitForObject(loginButton):
                        object.exists(loginButton)
                        mouseClick(loginButton)
                        test.log('Succesfully logged in')
                
    except Exception as q:
        test.fail("Exception" +str(q))
        takeScreenShot()
        

def waveformsettingsscreen():
    try:
        if waitForObject(Waveformsettingsscreen):
            object.exists(Waveformsettingsscreen)
            mouseClick(Waveformsettingsscreen)
            test.log('Succesfuly navigated to the waveform settings screen')
    except Exception as E1:
        test.log("Exception" +str(E1))
        
def selectmanualprofile():
    try:
        if waitForObject(liveSettingsProfileComboBox):
            object.exists(liveSettingsProfileComboBox)
            mouseClick(liveSettingsProfileComboBox)
            test.log('Succesfuly clicked profile tab')
            if waitForObject(liveSettingsProfileComboBox):
                object.exists(liveSettingsProfileComboBox)
                mouseClick(liveSettingsProfileComboBox)
                test.log('Succesfuly clicked profile tab')
    except Exception as E2:
        test.log("Exception" +str(E2))


#Choosint the speed and gain based on i value
def Changeparametersinwaveformsettings():
    try:
        if i%2==0:
            if object.exists(liveSpeed_5):
                mouseClick(liveSpeed_5)
            if object.exists(liveSensitivity_20):
                mouseClick(liveSensitivity_20)
        else:
            if object.exists(liveSpeed_25):
                mouseClick(liveSpeed_25)
            if object.exists(liveSensitivity_2_5):
                mouseClick(liveSensitivity_2_5)
        return True
    except Exception as E3:
        test.log("Exception" +str(E3))
        return False

#saving the waveform settings parameters
def Waveformsettingssave():
    try:
        if waitForObject(saveButtonId):
            object.exists(saveButtonId)
            mouseClick(saveButtonId)
            test.log('Succesfuly saved and naviagted to the waveform screen')
        return True
    except Exception as E4:
        test.fail("Exception" +str(E4)) 
    return False 
        

#click oon manual print button 

def ManualPrintButton():
    try:
        if waitForObject(liveScreenManualPrintButton):
            object.exists(liveScreenManualPrintButton)
            mouseClick(liveScreenManualPrintButton)
            test.log('Succesfuly clicked manual print button')
        return True
    except Exception as E5:
        test.fail("Exception" +str(E5))
    return False

def ManualPrintstopButton():
    try:
        if waitForObject(manualPrintstopButtonId):
            object.exists(manualPrintstopButtonId)
            mouseClick(manualPrintstopButtonId)
            test.log('Succesfuly stopped manual print')
        return True
    except Exception as E6:
        test.fail("Exception" +str(E6))
    return False
        
 
'Localization testing-Manual input screen'         
#Language validation-Manual input screen

def NavigatetoManualinputscreen():
    try: 
        snooze(1)    
        status='fail'
        if waitForObject(onlineScreenMonitorContainerId):
            if object.exists(onlineScreenMonitorContainerId):
                mouseClick(onlineScreenMonitorContainerId)
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e))
        
 
ManualINput={"container": mainWindow, "id": "manualInputArea", "type": "Rectangle", "unnamed": 1, "visible": True} 
        
def CollectManualinputscreentextCheck():
    try:
        snooze(1)
        status='fail'
        #collecting Manual input word
        if findObject(manualInputId):
            parent=findObject(manualInputId) 
            column_0=object.children(parent) 
            child=object.children(column_0[1]) 
            child1=object.children(child[0])  
            child2=object.children(child1[0])
            str1=child2[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)

        #collecting Blood pressure and Slash(/) symbol
        if findObject(ManualINput):
            parent=findObject(manualInputArea)
            child=object.children(parent)
            coln_0=object.children(child[0])
            if len(coln_0)>=1:
                for x in range(len(coln_0)):
                    a=object.children(coln_0[x])
                    for y in range(len(a)):
                        if a[0].text:
                            str1=a[0].text
                            addtolist1(str1)
                        else:
                            continue
            
            status='pass'
            
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e))  
    
        

def CollectManualinputscreentext():
    try:
        snooze(1)
        status='fail'
        #collecting Manual input word
        if findObject(manualInputId):
            parent=findObject(manualInputId) 
            column_0=object.children(parent) 
            child=object.children(column_0[1]) 
            child1=object.children(child[0])  
            child2=object.children(child1[0])
            str1=child2[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #collecting Blood pressure and Slash(/) symbol
        if findObject(manualInputArea):
            parent=findObject(manualInputArea)
            child=object.children(parent)
            child1= object.children(child[0])
            child2=object.children(child1[0])
            str1=child2[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting '/' and mmHg word
        if findObject(manualInputArea):
            parent=findObject(manualInputArea)
            child=object.children(parent)
            child1= object.children(child[0])
            child2=object.children(child1[0])
            child3=object.children(child2[1])
            str1=child3[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            str1=child3[3].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1) 
        #Collecting weight and kg text
        if findObject(manualInputArea):
            parent=findObject(manualInputArea)
            child=object.children(parent)
            child1= object.children(child[0])
            child2=object.children(child1[1])
            child3=object.children(child2[0])
            str1=child3[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #collecting kg text
            child3=object.children(child2[0])
            child4=object.children(child3[1])
            str1=child4[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #Collecting height text
        if findObject(manualInputArea):
            parent=findObject(manualInputArea)
            child=object.children(parent)
            child1= object.children(child[0])
            child2=object.children(child1[1])
            child3=object.children(child2[1])
            str1=child3[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #collecting cm text
            child4=object.children(child3[1])
            str1=child4[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
            
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e))

def closeManualInputButton():
    try:
        status='fail'
        if waitForObject(closeManualInputButtonId):
            if object.exists(closeManualInputButtonId):
                mouseClick(closeManualInputButtonId)
                snooze(3)
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail('exception'+str(e))
            

'Localization testing-Waveform settings'

def Waveformsettingstowaveformscreen():
    try:
        status='fail'
        if waitForObject(wavefromsettingsclosebutton):
            if object.exists(wavefromsettingsclosebutton):
                mouseClick(wavefromsettingsclosebutton)
                snooze(2)
                if waitForObject(Menubutton):
                    if object.exists(Menubutton):
                        status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail('exception'+str(e))
            
'''   
    
        #collecting 'do you want to close...filer changes ?'
        if waitForObject(WarningconfirmItemId):
            if object.exists(WarningconfirmItemId):
                parent=findObject(WarningconfirmItemId)
                child=object.children(parent)
                column_0=object.children(child[0])
                item_2=object.children(column_0[2])
                Row0=object.children(item_2[0])
                #msg1=object.children(Row0[2])
                str1=Row0[2].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
        ##collecting warning text
        if waitForObject(WarningconfirmItemId):
            if object.exists(WarningconfirmItemId):
                parent=findObject(WarningconfirmItemId)
                child=object.children(parent)
                column_0=object.children(child[0])
                Row0=object.children(column_0[0])
                #msg1=object.children(Row0[0])
                str1=Row0[0].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
        if waitForObject(PopupconfirmID):
            if object.exists(PopupconfirmID):
                mouseClick(PopupconfirmID)
                status='pass'
        return True if status=='pass' else 'fail'
    except Exception as e:
        test.fail('exception'+str(e))
''' 
def Navigatetolivewaveformsettings():
    try:
        status='fail'
        if waitForObject(Waveformsettingsscreen):
            if object.exists(Waveformsettingsscreen):
                tapObject(Waveformsettingsscreen)
                status='pass'
        return True if status=='pass' else 'fail'
    except Exception as e:
        test.fail('exception'+str(e))

       
def Collectlivewaveformsettingstext_title():
    try:
        status='fail'
        #collecting the title (Current examintaion.....)
        if waitForObject(headerItemId):
            if object.exists(headerItemId):
                tapObject(headerItemId)
                parent=findObject(headerItemId)
                child=object.children(parent)
                str1=child[0].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
        #collecting the profile word
        if findObject(profileSelectorItemId):
            parent=findObject(profileSelectorItemId)
            Label_0=object.children(parent)
            str1=Label_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            status='pass'
        return True if status=='pass' else False 
            
    except Exception as e:
        test.fail('exception'+str(e))


def Autoprofilesettings():
    try:
    #Clicking on profile combo box and selecting auto profile
        step1=profileselectioncombobox(livecomboboxprofileselectorID)
        snooze(2)
        step2=profileselection(Autoprofileselection)
    #Collecting text from display and print tab
        step2=Displayandprinttab()
    #Navigating to recording tab
        step3=liveSettingsRecordingtab()
        snooze(2)
    #collecting type word fro,ECG word and display and print tab
        step4=collecttextfromrecordingtab()
    #collecting all the recording length
        step5=Collect_1stchild_text(Recordinglength_10,Recordinglength_12,Recordinglength_15,Recordinglength_20)
    #Navigating filter tab and followed by collecting text
        #step6=livescreenfiltertab()
        snooze(1)
        if step1 and step2 and step3 and step4 and step5:
            test.log('Succesfully collected all the text from auto profile')
            status='pass'
        else:
            test.log('failed to collect all the text from auto profile')
            status='fail'
        
        return True if status=='pass' else False   
    
    except Exception as e:
        test.fail('exception'+str(e))
        
def Manualprofilesettings():
    try:
    #Clicking on profile combo box
        step1=profileselectioncombobox(livecomboboxprofileselectorID)
    #Slecting Manual profile
        step2=profileselection(Manualprofileselection)
        test.log('succesfully collected manual word')
        snooze(1)
        if step1 and step2:
            test.log('succesfully collected manual profile word') 
            status='pass' 
        else:
            test.log('Failed to collect manual profile word')
            status='fail' 
        return True if status=='pass' else False   
    
    except Exception as e:
        test.fail('exception'+str(e))
        
               
def Rhythmprofilesettings():
    try:
    #Clicking on profile combo box
        step1=profileselectioncombobox(livecomboboxprofileselectorID)
        snooze(1)
    #Slecting Manual profile
        step2=profileselection(Rhythmprofileselection)
        snooze(1)
        test.log('succesfully collected rhythm word')
        #collecting all the recording length of rhythm
        step3=Collect_1stchild_text(Recordinglength_30sec,Recordinglength_1min,Recordinglength_2min,Recordinglength_6min,Recordinglength_10min,Recordinglength_20min)
        test.log('collected all recoridng length from rhythm profile')
        #collecting recording leads of rhythm profile
        step4=Collect_1stchild_text(Recoredleads_I,Recoredleads_II,Recoredleads_III,Recoredleads_aVR,Recoredleads_aVL,Recoredleads_aVF,Recoredleads_V1,Recoredleads_V2,Recoredleads_V3,Recoredleads_V4,Recoredleads_V5,Recoredleads_V6)
        snooze(1)
        #collecting recorded leads (max 2) text
        step5=Recordedleads_max2word()
        snooze(1)
        #Navigatetofiltertab and None filter (This ll help to take the filter change warning messge when closing the tab)
        #step7=filtertabandclickNonefilter()
        if step1 and step2 and step3 and step4 and step5:
            test.log('succesfully collected rhythm profile word') 
            status='pass' 
        else:
            test.log('Failed to collect rhythm profile  word')
            status='fail' 
        return True if status=='pass' else False   
    
    except Exception as e:
        test.fail('exception'+str(e))
            
#collecting Type,ECG and lenth of  record word
def collecttextfromrecordingtab():
    try:
        status='fail'
        snooze(1)
        parent=findObject(recordingSettingsId)
        column_0=object.children(parent)
        column_00=object.children(column_0[0])
        Row_0=object.children(column_00[0])
        str1=Row_0[0].text
        test.log('Collected string ='+str(str1))
        addtolist1(str1)
        str1=Row_0[1].text
        Row_1=object.children(column_00[1])
        str1=Row_1[0].text
        test.log('Collected string ='+str(str1))
        addtolist1(str1)
        status='pass'
            
        return True if status=='pass' else False 
    
    except Exception as e:
        test.fail('exception'+str(e))


#collecting all the text from display and print
def Displayandprinttab():
    try:
        status='fail'
        #Display and print text
        if object.exists(Displayandprinttab1):
            parent=findObject(Displayandprinttab1)
            child=object.children(parent)
            str1=child[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))       
        #collecting speed,gain and RR values
        step1=Collect_1stchild_text(liveSpeed_5,liveSpeed_10,liveSpeed_12_5,liveSpeed_25,
                                    liveSpeed_50,liveSensitivity_2_5,liveSensitivity_5,
                                    liveSensitivity_10,liveSensitivity_20,livesettings0_5x,livesettings1_x)
        #collecting units (mm/sec and gain)
        step2=unitssppedandgain()
        snooze(1)
        step3=halfchestsensitivity()
        snooze(1)
         
        if step1 and step2 and step3:
            test.log('collected all the text from display and print tab')
            status='pass'
        else:
            test.log('Failed to collect the text from display and print tab')
            status='fail'
        return True if status=='pass' else False
      
    except Exception as e:
        test.fail('exception'+str(e))


#Moving to recording tab and collecting recording text
def liveSettingsRecordingtab():
    try:
        status='fail'
        if object.exists(Recordingtab):
            mouseClick(Recordingtab)
            parent=findObject(Recordingtab)
            child=object.children(parent)
            str1=child[1].text
            addtolist1(str1)
            snooze(2)
            test.log('Collected string ='+str(str1))
            status='pass'
        return True if status=='pass' else False   
    except Exception as e:
        test.fail('exception'+str(e))

#Clicking profile combo box
def profileselectioncombobox(obj):
    try:
        status='fail'
        if waitForObject(obj):
            if object.exists(obj):
                mouseClick(obj)
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail('exception'+str(e))
        


#Selecting auto,manual and rythm profile text       
def profileselection(obj):
    try:
        status='fail'
        if waitForObject(obj):
            if object.exists(obj):
                mouseClick(obj)
        if waitForObject(livecomboboxprofileselectorID):
            if object.exists(livecomboboxprofileselectorID):
                parent=findObject(livecomboboxprofileselectorID)
                str1=parent.currentText
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail('exception'+str(e))
    

def Profileselection(Obj):
    try:
        profile= waitForObject(Obj)
        child = object.children(profile)
        initIndex = child[1].currentIndex
        for i in range (child[1].count):
            child[1].currentIndex = i
            if child[1].currentText == valueToSelect:
                list2.append(child[1].currentText)
                test.log("Successfully selected  word and added into list")
                snooze(1)
                return True   
        child[1].currentIndex = initIndex
        test.log("Value is not present in the dropdown")  
    except Exception as e:
        test.fail('exception'+str(e))    
        
#collecting m/s and mm/mV text
def unitssppedandgain():
    try:
        status='fail'
        if waitForObject(displayandprintsettingsID):
            if object.exists(displayandprintsettingsID):
                parent=findObject(displayandprintsettingsID)
                child=object.children(parent)
                coloumn0=object.children(child[0])
                Row_0=object.children(coloumn0[0])
                #Label1=object.children(Row_0[3])
                str1=Row_0[3].text
                test.log('Collected string ='+str(str1))
                addtolist1(str1)
        if waitForObject(displayandprintsettingsID):
            if object.exists(displayandprintsettingsID):
                parent=findObject(displayandprintsettingsID)
                child=object.children(parent)
                coloumn0=object.children(child[0])
                Row_1=object.children(coloumn0[1])
                #Label1=object.children(Row_1[3])
                str1=Row_1[3].text
                test.log('Collected string ='+str(str1))
                addtolist1(str1)
                status='pass'
        return True if status=='pass' else False
    
    except Exception as e:
        test.fail('exception'+str(e))



def Recordedleads_max2word():
    try:
        status='fail'
        if waitForObject(recordingSettingsId):
            if object.exists(recordingSettingsId):
                parent=findObject(recordingSettingsId)
                child=object.children(parent)
                coloumn0=object.children(child[0])
                Row_2=object.children(coloumn0[2])
                #Label0=object.children(Row_2[0])
                str1=Row_2[0].text
                test.log('Collected string ='+str(str1))
                addtolist1(str1)
                status='pass'
        return True if status=='pass' else False
                
    except Exception as e:
        test.fail('exception'+str(e))

def autoProfilefiltertab():
    try:
        status='fail'
        #Click and collecting none filter words
        if Nonefilertabwords():
            test.log('sucesffuly collected None filter all text')
        #Click and collecting auto filter words
        if Autofilterwords():
            test.log('sucesffuly collected Auto filter text')
        if Strictfilterword():
            test.log('sucesffuly collected strict filter text')
        if Userfilterwords():
            test.log('sucesffuly collected user filter text')
            status='pass'
        return True if status=='pass' else False
    
    except Exception as e:
        test.fail('exception'+str(e))
        
#Rhythm profile>filter tab>None filter
def filtertabandclickNonefilter():
    try:
        #click on filter tab
        status='fail'
        if waitForObject(Filtertab):
            if object.exists(Filtertab):
                mouseClick(Filtertab)
                if waitForObject(NonefilterID):
                    if object.exists(NonefilterID):
                        mouseClick(NonefilterID)
                        status='pass'
        return True if status=='pass' else False
    
    except Exception as e:
        test.fail('exception'+str(e))



def Nonefilertabwords():
    try:
        #To collect Nonefiler word
        status='fail'
        if waitForObject(NonefilterID):
            if object.exists(NonefilterID):
                mouseClick(NonefilterID)
                #collect all the text from None filter tab (None,50Hz,0.07Hz cubic spline,90 Hz)
                Collect_1stchild_text(NonefilterID)     
                snooze(1)
        return True if status=='pass' else False
            
    except Exception as e:
        test.fail('exception'+str(e))
        
def Autofilterwords():
    try:
        status='fail'
        #To collect Auto word
        if waitForObject(AutofilterbuttonID):
            if object.exists(AutofilterbuttonID):
                mouseClick(AutofilterbuttonID)
                #collect all the text from Auto filter tab (Auto,50Hz,60Hz,0.07Hz cubic spline,90 Hz)
                Collect_1stchild_text(AutofilterbuttonID)     
                status='pass'
        
        return True if status=='pass' else False
    except Exception as e:
        test.fail('exception'+str(e))

        
#Clicking on strict filter and collecting all the text from that        
def Strictfilterword():
    try:
        status='fail'
        #To collect Stict word
        if waitForObject(StrictfilterID):
            if object.exists(StrictfilterID):
                mouseClick(StrictfilterID)
                #collect all the text from stict filter tab (Strict,0.25Hz adaptive,25 Hz)
                Collect_1stchild_text(StrictfilterID)  
                snooze(1)
                status='pass'
        return True if status=='pass' else False
            
    except Exception as e:
        test.fail('exception'+str(e))
     

#Clicking on user filter and collecting all the text from that 
def Userfilterwords():
    try:
        status='fail'
        #To collect user word
        if waitForObject(UserfilterID):
            if object.exists(UserfilterID):
                mouseClick(UserfilterID)
                #collect all the text from user filter-user
                Collect_1stchild_text(UserfilterID)     
        snooze(1)
        #collecting 0.049 Hz from drift filter
        if filtercombobox(driftFiltersComboboxId,driftfilter_0_049Hz):
            Collect_1stchild_text(driftFiltersComboboxId)
            snooze(1)
            if Driftwarningmessage(FilterdriftandmyomessageID):
                test.log("collected drift warning message of user 0.049 Hz drift filter")
        
        #collecting 0.05 Hz from drift filter
        if filtercombobox(driftFiltersComboboxId,driftfilter_0_05Hz):
            Collect_1stchild_text(driftFiltersComboboxId)
            snooze(1)
            #Collecting 0.05Hz drift warning message
            if Driftwarningmessage(FilterdriftandmyomessageID):
                test.log("collected drift warning message of user 0.05Hz drift filter")
            
        #collecting 0.25 Hz from drift filter
        if filtercombobox(driftFiltersComboboxId,driftfilter_0_25Hz):
            Collect_1stchild_text(driftFiltersComboboxId)
            snooze(1)
            #Collecting 0.25Hz drift warning message
            if Driftwarningmessage(FilterdriftandmyomessageID):
                test.log("collected drift warning message of user 0.25Hz drift filter")    
            
        #collecting 0.07 Hz from drift filter
        if filtercombobox(driftFiltersComboboxId,driftfilter_0_07Hz):
            Collect_1stchild_text(driftFiltersComboboxId)
            snooze(1)
            #Collecting 0.07 Hz drift warning message
            if Driftwarningmessage(FilterdriftandmyomessageID):
                test.log("collected drift warning message of user 0.07 Hz drift filter")    
                
        #collecting 0.07 Hz from drift filter
        if filtercombobox(driftFiltersComboboxId,driftfilter_90Hz):
            Collect_1stchild_text(driftFiltersComboboxId)
            snooze(1)
            #Collecting 0.07 Hz drift warning message
            if Driftwarningmessage(FilterdriftandmyomessageID):
                test.log("collected drift warning message of user 90 Hz drift filter")   
         
        #collecting 170 Hz from myo filter
        if filtercombobox(myoFiltersComboboxId,myofilter_170Hz):
            Collect_1stchild_text(myoFiltersComboboxId)
            #collecting myo filter waring msg
            if Myowarningmessage(FilterdriftandmyomessageID):
                test.log("collected myo warning message of 170 Hz myo filter")
                
        #collecting 35 Hz from myo filter
        if filtercombobox(myoFiltersComboboxId,myofilter_35Hz):
            Collect_1stchild_text(myoFiltersComboboxId)
            #collecting myo filter waring msg
            if Myowarningmessage(FilterdriftandmyomessageID):
                test.log("collected myo warning message of 35Hz myo filter")
         
        #collecting 20 Hz from myo filter
        if filtercombobox(myoFiltersComboboxId,myofilter_20Hz):
            Collect_1stchild_text(myoFiltersComboboxId)
            #collecting myo filter waring msg
            if Myowarningmessage(FilterdriftandmyomessageID):
                test.log("collected myo warning message of 35Hz myo filter")
         
        #collecting 25 Hz from myo filter
        if filtercombobox(myoFiltersComboboxId,myofilter_25Hz):
            Collect_1stchild_text(myoFiltersComboboxId)
            #collecting myo filter waring msg
            if Myowarningmessage(FilterdriftandmyomessageID):
                test.log("collected myo warning message of 325Hz myo filter")
         
        #collecting 90 Hz from myo filter
        if filtercombobox(myoFiltersComboboxId,myofilter_90Hz):
            Collect_1stchild_text(myoFiltersComboboxId)
            #collecting myo filter waring msg
            if Myowarningmessage(FilterdriftandmyomessageID):
                test.log("collected myo warning message of 325Hz myo filter")
                status='pass'
                
        return True if status=='pass' else False
        
    except Exception as e:
        test.fail('exception'+str(e))
        
        
def filtercombobox(obj,obj1):
    try:
        status='fail'
        if waitForObject(obj):
            if object.exists(obj):
                mouseClick(obj)
                snooze(1)
                if waitForObject(obj1):
                    if object.exists(obj1):
                        mouseClick(obj1)
                        status='pass'
        return True if status=='pass' else False    
    except Exception as e:
        test.fail('exception'+str(e))
 
#Function to collect drift warning message        
def Driftwarningmessage(obj):
    try:
        status='fail'
        if object.exists(obj):
            parent=findObject(obj)
            child1=object.children(parent)
            str1=child1[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail('exception'+str(e)) 
        
#Function to collect Myo warning message 
def Myowarningmessage(obj):
    try:
        status='fail'
        if object.exists(obj):
            parent=findObject(obj)
            child1=object.children(parent)
            str1=child1[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail('exception'+str(e))


#Collecting drift,myo and main filter words from filter tab
def MainDriftMyofilterword(*arguments):
    try:
        status='fail'
        for obj in arguments:
            if waitForObject(obj):
                if object.exists(obj):
                    parent=findObject(obj)
                    Label_0=object.children(parent)
                    str1=Label_0[0].text
                    addtolist1(str1)
                    test.log('Collected string ='+str(str1))
        status='pass'
        return True if status=='pass' else 'fail'
    except Exception as e:
        test.fail('exception'+str(e))


#common method to collect all the speed,gain,RR values,Recording length
def Collect_1stchild_text(*arguments):
    try:
        status='fail'
        for obj in arguments:
            if object.exists(obj):
                #mouseClick(obj)
                parent=findObject(obj)
                Label_1=object.children(parent)
                str1=Label_1[1].text
                test.log('Collected string ='+str(str1))
                addtolist1(str1)
                snooze(0.5)
        status='pass'
        return True if status=='pass' else False
    
    except Exception as e:
        test.fail('exception'+str(e))

                
def halfchestsensitivity():
    try:
        status='fail'
        if object.exists(livescreenhalfchestsensitvity):
            parent=findObject(livescreenhalfchestsensitvity)
            child=object.children(parent)
            str1=child[0].text
            test.log('Collected string ='+str(str1))
            addtolist1(str1)
        if object.exists(livescreenhalfchestsensitvity_on):
            parent=findObject(livescreenhalfchestsensitvity_on)
            Label_1=object.children(parent)
            str1=Label_1[1].text
            test.log('Collected string ='+str(str1))
            addtolist1(str1)
        if object.exists(livescreenhalfchestsensitvity_off):
            parent=findObject(livescreenhalfchestsensitvity_off)
            Label_1=object.children(parent)
            str1=Label_1[1].text
            test.log('Collected string ='+str(str1))
            addtolist1(str1)
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail('exception'+str(e))  
      
          
#objects from electrode status screen
'Localization testing-Electorde status screen'

def Navigateelectrodestatusscreen():
    status='fail'
    try:
        if waitForObject(electrodeStatusButtonId):
            if object.exists(electrodeStatusButtonId):
                mouseClick(electrodeStatusButtonId)
                status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))

#collecting text when IEC as lead marking
def CollectelectrodestatusscreenIECAHA():
    try:
        snooze(1)
        status='fail'
        #Getting elecrtodes words
        if object.exists(headerItemId_Electrodetext):
            parent=findObject(headerItemId_Electrodetext)
            Label_0=object.children(parent)
            str1=Label_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #Getting lead system word
        if object.exists(previewItemID):
            parent=findObject(previewItemID)
            Child=object.children(parent)        
            column_0=object.children(Child[0])  
            item_0=object.children(column_0[0])
            Flow0=object.children(item_0[0])        
            #Leadsys=object.children(Flow0[3])      
            str1=Flow0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #collecting 12L ECG standard text
            customcombobox=object.children(Flow0[3])
            str1=customcombobox[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #collecting label word
        if object.exists(contentItemId):
            parent=findObject(contentItemId)
            child=object.children(parent)
            Row_0=object.children(child[0])
            Rect_1=object.children(Row_0[1])
            Listview=object.children(Rect_1[0])
            item_0=object.children(Listview[0])
            Rect_0=object.children(item_0[0])
            Row_00=object.children(Rect_0[0])
            str1=Row_00[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #Collecting lead placement text
            str1=Row_00[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1) 
            status='pass'
        return True if status=='pass' else 'fail'
    except Exception as e:
        test.fail('exception'+str(e))
    
#Common method to get Label name and discription of same label
def CollectelectrodestatusscreenIECAHA1(*arguemnts):
    try:
        snooze(1)
        #Getting label name
        status='fail'
        for obj in arguemnts:
            if object.exists(obj):
                parent=findObject(obj)
                child=object.children(parent)
                column_0=object.children(child[0])
                Row_0= object.children(column_0[0])
                str1=Row_0[1].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(0.5)
                #Getting discription for the same label             
                str1=Row_0[3].text 
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(0.5)
        status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))
       
#Functions to navigate to waveform screen from  elecrode screen       
def electrodestatustowaveformscreen():
    try:
        status='fail'
        if waitForObject(electrodestatusclosebutton):
            if object.exists(electrodestatusclosebutton):
                mouseClick(electrodestatusclosebutton)
                status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))
        
#Navigating to menu screen from online screen
def Onlinesccreentomenuscreen():
    try:
        status='fail'
        snooze(6)
        if waitForObject(Menubutton):
            if object.exists(Menubutton):
                mouseClick(Menubutton)
                status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))
        

'Localization  testing-Login and logout screen'
        
 
#Logout button
def logoutfromcurrentuser():
    try:
        status='fail'      
        
        if waitForObject(logButtonId):
            object.exists(logButtonId)
            mouseClick(logButtonId)
            test.log('Succesfuly logged out from the user')
            status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))



















#collectloginscreentext-Collecting password,skip,login and error message
def collectloginscreentext():
    try:
        status='fail'
        #Password word
        if object.exists(loginscreenpasswordID):
            parent=findObject(loginscreenpasswordID)
            label_1=object.children(parent)
            str1=label_1[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(0.5)
        #Skip word
        if object.exists(skipLoginButtonID):
            parent=findObject(skipLoginButtonID)
            Label_1=object.children(parent)
            str1=Label_1[3].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(0.5) 
        #Login word
        if waitForObject(loginButton):
            object.exists(loginButton)
            mouseClick(loginButton)
            parent=findObject(loginButton)
            Label_1=object.children(parent)
            str1=Label_1[3].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(0.5)     
        #Collect Alert word
        if object.exists(loginPopupItemId):
            parent=findObject(loginPopupItemId)
            child=object.children(parent)    
            column_0=object.children(child[0])  
            Row_0=object.children(column_0[0])
            str1=Row_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(0.5)
        #login failed...warning msg
        if object.exists(loginPopupItemId):
            parent=findObject(loginPopupItemId) 
            child=object.children(parent)     
            Column_0=object.children(child[0])  
            item_2=object.children(Column_0[2])    
            Row_0=object.children(item_2[0])      
            #warningchild=object.children(Row_0[3]) 
            str1=Row_0[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(0.5)
            #Accept alert message pop up
            if object.exists(loginscreenaccepterror):
                mouseClick(loginscreenaccepterror)
                status='pass'
                snooze(0.5)
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))

pwdRecoveryScreenId={"container": mainWindow, "id": "pwdRecoveryScreenId", "type": "PasswordRecoveryPage", "unnamed": 1, "visible": True}
cancelRecoverynButtonId={"checkable": False, "container": mainWindow, "id": "cancelRecoverynButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
validateButtonId={"checkable": False, "container": mainWindow, "id": "validateButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
recoveryKeyEntryFieldId={"container": mainWindow, "id": "recoveryKeyEntryFieldId", "type": "PatientInfoField", "unnamed": 1, "visible": True}
loginPopupItemId={"container": mainWindow, "id": "loginPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}



#Navigate to password recorvery screen and collecting all text
def Navigatetoadminpasswordrecoveryscreen():
    try: 
        status='fail'
        if waitForObject(loginButton):
            mousePress(loginButton)
            snooze(6)
            mouseRelease(loginButton)
            snooze(2)
        #Collecting text from password recovery screen
        if object.exists(pwdRecoveryScreenId):
            parent=findObject(pwdRecoveryScreenId)
            child=object.children(parent)
            Column1=object.children(child[0])
            #Collecting Default admin password recovery
            str1=Column1[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting Device serial number text
            Row_3=object.children(Column1[3])
            str1=Row_3[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting Recovery key text
            Row_4=object.children(Column1[4])
            str1=Row_4[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Please contact BTL Support to get the password recovery key
            str1=Column1[8].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #Collecting Verify text and cancel text
        if object.exists(validateButtonId):
            parent=findObject(validateButtonId)
            child=object.children(parent)
            str1=child[3].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(2)
            setFocusTextBox(recoveryKeyEntryFieldId)
            snooze(1)
            type(mainWindow,'QA')
            snooze(2)
            mouseClick(validateButtonId)
            snooze(40)
        #Enterting wrong key and collecting warning text
        if object.exists(loginPopupItemId):
            collectingwarning_text(loginPopupItemId)
            snooze(1)
            Acceptwarning_popup(okButtonId)
        #Collecting cancel button text and navigate back to login page
        if object.exists(cancelRecoverynButtonId):
            parent=findObject(cancelRecoverynButtonId)
            child=object.children(parent)
            str1=child[3].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            mouseClick(cancelRecoverynButtonId)
            snooze(1)
            status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))

   
#Enter cred and login to online screen
def loginandnavigatetoonelinescreen():
    try: 
        status='fail'
        if object.exists(loginNameEntryFieldId):
            setFocusTextBox(loginNameEntryFieldId)
            type(mainWindow,'admin')
            snooze(3)
        if object.exists(loginPasswordInputId):
            setFocusTextBox(loginPasswordInputId)
            type(mainWindow,'qaqaqaqa')
        if waitForObject(loginButton):
            object.exists(loginButton)
            snooze(2)
            mouseClick(loginButton)
            status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))
 


'Localization  testing-Wavefrom screen'

         
#Collecting A-module disconnection message and Anonymous patient text
def CollectWavefromscreentext():
    try: 
        status='fail'
        if object.exists(patientDetailsRowId):
            parent=findObject(patientDetailsRowId)
            child=object.children(parent)
            str1=child[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #A-module disconnection message 
        if object.exists(onlineECGWfId):
            parent=findObject(onlineECGWfId)
            child=object.children(parent)
            str1=child[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))
        