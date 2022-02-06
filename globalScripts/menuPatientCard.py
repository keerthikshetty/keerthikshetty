'''Objects of main window'''
mainWindow = {"type": "QQuickWindowQmlImpl", "visible": True}
onlineScreen_MainWindow = {"container": mainWindow, "id": "onlineScreenId", "type": "OnlineWfScreen", "visible": True}
evaluationScreen_MainWindow = {"container": mainWindow, "id": "evaluationScreenId", "type": "EvalScreen", "visible": True}
menuScreen_MainWindow = {"container": mainWindow, "id": "menuScreenId", "type": "Rectangle", "visible": True}
patientCardScreen_MainWindow = {"container": mainWindow, "id": "patientScreenId", "type": "PatientCardLoader", "visible": True}
liveSettingsScreen_MainWindow = {"container": onlineScreen_MainWindow, "type": "Rectangle", "visible": True}
#patientCardAddPatient_MainWindow = {"container": patientCardScreen_MainWindow, "id": "patientCardColumn", "type": "Column", "visible": True}
patientCardAddPatient_MainWindow = {"container": patientCardScreen_MainWindow, "id": "patientCardAddviewId", "type": "PatientCardAddview", "visible": True}

'''Objects of menu button'''
#menuRecordingButton = {"checkable": False, "container": menuScreen_MainWindow, "id": "menuRecordingButtonId", "type": "CircularButton", "visible": True}
menuPatientcardButton = {"checkable": False, "container": menuScreen_MainWindow, "id": "menuPatientcardButtonId", "type": "CircularButton", "visible": True}
menuWorklistButton = {"checkable": False, "container": menuScreen_MainWindow, "id": "menuWorklistButtonId", "type": "CircularButton", "visible": True}
menuUserButton = {"checkable": False, "container": menuScreen_MainWindow, "id": "menuUsersButtonId", "type": "CircularButton", "visible": True}
menuSettingsButton = {"checkable": False, "container": menuScreen_MainWindow, "id": "menuSettingsButtonId", "type": "CircularButton", "visible": True}
menuRhythmComboBox = {"container": menuScreen_MainWindow, "id": "rhythmComboBoxId", "type": "ComboBox", "visible": True}
menuDefaultComboBox = {"container": menuScreen_MainWindow, "id": "comboBoxId", "type": "ComboBox", "visible": True}
'''Objects of add patient button in live patient screen LX'''
addPatientCardSurnameFieldLX = {"container": patientCardScreen_MainWindow, "id": "surnameFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardSurnameInputLX = {"container": patientCardScreen_MainWindow, "id": "surnameInputId", "type": "PatientInfoField", "visible": True}
saveButtonAddPatientCardInputLX = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "saveButtonId", "type": "CircularButton", "visible": True}
cancelButtonAddPatientCardInputLX = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "cancelButtonId", "type": "CircularButton","visible": True}
closeButtonAddPatientCardInpuLX = {"container":patientCardScreen_MainWindow, "id": "closePatientDialogButtonId", "type": "CloseDialogButton", "visible": True}
addPatientCardFirstNameFieldLX = {"container": patientCardScreen_MainWindow, "id": "firstnameFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardFirstNameInputLX = {"container": patientCardScreen_MainWindow, "id": "firstnameInputFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardTitleFieldLX = {"container": patientCardScreen_MainWindow, "id": "titleFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardTitleInputLX = {"container": patientCardScreen_MainWindow, "id": "titleInputFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardDOBFieldLX = {"container": patientCardScreen_MainWindow, "id": "dobFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardDOBInputLX = {"container": patientCardScreen_MainWindow, "id": "dobInputFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardAgeFieldLX = {"container": patientCardScreen_MainWindow, "id": "ageFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardAgeInputLX = {"container": patientCardScreen_MainWindow, "id": "ageInputFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardWeightFieldLX = {"container": patientCardScreen_MainWindow, "id": "weightFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardWeightInputLX = {"container": patientCardScreen_MainWindow, "id": "weightInputFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardHeightFieldLX = {"container": patientCardScreen_MainWindow, "id": "heightFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardHeightInputLX = {"container": patientCardScreen_MainWindow, "id": "heightInputFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardPacemakerSelectorLX = {"container": patientCardScreen_MainWindow, "id": "pacemakerSelectorId", "type": "CustomSwitchWithLabelColumn", "visible": True}
addPatientCardDigoxinSelectorLX = {"container": patientCardScreen_MainWindow, "id": "digoxinSelectorId", "type": "CustomSwitchWithLabelColumn", "visible": True}
addPatientCardPatientIDFieldLX = {"container": patientCardScreen_MainWindow, "id": "patientIdFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardPatientIDInputLX = {"container": patientCardScreen_MainWindow, "id": "patientIdInputFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardHospitalIDFieldLX = {"container": patientCardScreen_MainWindow, "id": "hospitalIdFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardHospitalIDInputLX = {"container": patientCardScreen_MainWindow, "id": "hospitalIdInputFieldId", "type": "PatientInfoField", "visible": True}
addPatientCardClassificationComboBoxLX = {"container": patientCardScreen_MainWindow, "id": "classificationComboBoxId", "type": "CustomComboBox", "visible": True}
addPatientCardGenderMaleRadioButtonLX = {"checkable": True, "container": patientCardScreen_MainWindow, "id": "genderMaleRadioButtonId", "type": "CustomRadioButton", "visible": True}
addPatientCardGenderFemaleRadioButtonLX = {"checkable": True, "container": patientCardScreen_MainWindow, "id": "genderFemaleRadioButtonId", "type": "CustomRadioButton", "visible": True}
addPatientCardGenderOtherRadioButtonLX = {"checkable": True, "container": patientCardScreen_MainWindow, "id": "genderOtherRadioButtonId", "type": "CustomRadioButton", "visible": True}
'''Objects of add patient button in patient card screen'''
patientCardAddPatientSurnameInput = {"container": patientCardScreen_MainWindow, "id": "surnameInputId", "type": "PatientInfoField", "visible": True}
patientCardAddPatientFirstNameInput = {"container": patientCardScreen_MainWindow, "id": "firstnameInputId", "type": "PatientInfoField", "visible": True}
patientCardAddPatientTitleInput = {"container": patientCardScreen_MainWindow, "id": "titleInputId", "type": "PatientInfoField", "visible": True}
patientCardAddPatientDOBInput = {"container": patientCardScreen_MainWindow, "id": "dobInputId", "type": "PatientInfoField", "visible": True}
patientCardAddPatientAgeInput = {"container": patientCardScreen_MainWindow, "id": "ageInputId", "type": "PatientInfoField", "visible": True}
patientCardAddPatientIdInput = {"container": patientCardScreen_MainWindow, "id": "patientIdInputId", "type": "PatientInfoField", "visible": True}
patientCardAddPatientHospitalIdInput = {"container": patientCardScreen_MainWindow, "id": "hospitalIdInputId", "type": "PatientInfoField", "visible": True}
patientCardAddPatientMaleRadioButton = {"checkable": True, "container": patientCardScreen_MainWindow, "id": "genderMaleRadioButtonId", "type": "CustomRadioButton", "visible": True}
patientCardAddPatientFemaleRadioButton = {"checkable": True, "container": patientCardScreen_MainWindow, "id": "genderFemaleRadioButtonId", "type": "CustomRadioButton", "visible": True}
patientCardAddPatientOthersRadioButton = {"checkable": True, "container": patientCardScreen_MainWindow, "id": "genderOtherRadioButtonId", "type": "CustomRadioButton", "visible": True}
patientCardAddPatientClassificationComboBox = {"container": patientCardScreen_MainWindow, "id": "classificationComboBoxId", "type": "ComboBox", "visible": True}
patientCardAddPatientWeightInput = {"container": patientCardScreen_MainWindow, "id": "weightInputId", "type": "PatientInfoField", "visible": True}
patientCardAddPatientWeightUnit = {"container": patientCardScreen_MainWindow, "text": "kg", "type": "Label", "visible": True}
patientCardAddPatientHeightInput = {"container": patientCardScreen_MainWindow, "id": "heightInputId", "type": "PatientInfoField", "visible": True}
patientCardAddPatientHeightUnit = {"container": patientCardScreen_MainWindow, "text": "cm", "type": "Label", "visible": True}
patientCardAddPatientPaceMakeYesButton = {"checkable": True, "container": patientCardScreen_MainWindow, "id": "pacemakeYesButtonId", "type": "CustomRadioButton", "visible": True}
patientCardAddPatientPaceMakeNoButton = {"checkable": True, "container": patientCardScreen_MainWindow, "id": "pacemakeNoButtonId", "type": "CustomRadioButton", "visible": True}
patientCardAddPatientDigoxinYesButton = {"checkable": True, "container": patientCardScreen_MainWindow, "id": "digoxinYesButtonId", "type": "CustomRadioButton", "visible": True}
patientCardAddPatientDigoxinNoButton = {"checkable": True, "container": patientCardScreen_MainWindow, "id": "digoxinNoButtonId", "type": "CustomRadioButton", "visible": True}
patientCardAddPatientSaveButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "savePatientButtonId", "type": "CircularButton", "visible": True}
patientCardAddPatientCancelButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "cancelPatientButtonId", "type": "CircularButton", "visible": True}
patientCardSetPatientForRecordButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "setPatientForRecordButtonId", "type": "CircularButton", "visible": True}
patientCardAddPatientBackButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "backPatientCardButtonId", "type": "Button", "visible": True}
patientCardDialogErrorMessage = {"container": patientCardScreen_MainWindow, "text": "Patient ID already exists!!", "type": "Text",  "visible": True}
patientCardAddPatientDialogOkButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "okButtonId", "type": "Button",  "visible": True}
patientcardSaveErrorPopUp = {"container": patientCardScreen_MainWindow, "id": "errorPopupItemId", "type": "WarningPopUp", "visible": True}
patientcardSaveErrorOkButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "okButtonId", "type": "CircularButton", "visible": True}
patientcardHospitalIDExistErrorOKButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "okButtonId", "type": "CircularButton", "visible": True}
patientcardPatientIdErrorPopUp = {"container": mainWindow, "id": "errorPopupItemId", "type": "WarningPopUp", "visible": True}
patientcardPatientIdErrorOkButton = {"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "CircularButton", "visible": True}
patientcardDobErrorPopUp = {"container": mainWindow, "id": "errorPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
patientcardDobErrorOkButton = {"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "CircularButton", "visible": True}
backPatientCardButtonId={"checkable": False, "container": mainWindow, "id": "backPatientCardButtonId", "type": "Button", "unnamed": 1, "visible": True}
examButtonId = {"container": patientCardScreen_MainWindow, "id": "examButtonId", "type": "Item", "visible": True}
#patientCardAddPatientCancelPopUpMessage = {"container": patientCardScreen_MainWindow, "id": "discardWarningItemId", "type": "WarningPopUp", "visible": True}
#patientCardAddPatientPopUpConfirmButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "confirmButtonId", "type": "CircularButton", "visible": True}
#patientCardAddPatientPopUpCancelButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "cancelButtonId", "type": "CircularButton",  "visible": True}
patientCardSelectAllPatientButtonId = {  "container": mainWindow, "id": "selectAllPatientButtonId", "type": "CircularButton", "visible": True}

'''Objects of menu patient card button'''
patientCardAddButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "addPatientButtonId", "type": "AddNewPatientButton", "visible": True}
#patientCardSearchInput = {"backgroundcolor": "#ffffff", "container": patientCardScreen_MainWindow, "echoMode": 0, "id": "patientSearchInputId", "type": "SearchBar", "unnamed": 1, "visible": True}
patientCardSearchInput = {"backgroundcolor": "#f6f6f6", "container": mainWindow, "echoMode": 0, "id": "searchField", "type": "TextField", "unnamed": 1, "visible": True}
# patientCardSearchInput = {"container": patientCardScreen_MainWindow, "text": "Type here..", "type": "PlaceholderText", "id": "placeholder", "visible": True}
patientCardNameSortButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "nameSortButtonId", "type": "SortingButton", "visible": True}
patientCardPatientSortButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "patientidSortButtonId", "type": "SortingButton", "visible": True}
patientCardLastExamSortButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "lastrecordDateTimeSortButtonId", "type": "SortingButton", "visible": True}
patientCardInfoButton = {"container": patientCardScreen_MainWindow, "source": "qrc:/qml/images/1280x800/infoicon.png", "type": "Image", "visible": True}
patientCardPatientListFirstRow = {"container": patientCardScreen_MainWindow, "id": "outlineId", "type": "Rectangle", "visible": True}
patientCardPatientListView = {"container": patientCardScreen_MainWindow, "id": "patientListViewId", "type": "ListView", "visible": True}
patientCardPrintPatientButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "printPatientButtonId", "type": "CircularButton", "visible": True}
patientCardExportPatientButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "exportPatientButtonId", "type": "CircularButton", "visible": True}
patientCardOtherOptionsPatientButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "otherOptionsPatientButtonId", "type": "CircularButton", "visible": True}
patientCardDeletePatientButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "deletePatientFromListButtonId", "type": "DeleteButton", "visible": True}
patientCardDeletePatientYesButton = {"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton",  "visible": True}
patientCardDeletePatientNoButton = {"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton",  "visible": True}
patientCardDeletePatientCancelPopUpMessage = {"container": mainWindow, "type": "Label", "visible": True, "id":"warningMessageId"}
#{"container": mainWindow, "text": "Delete 1 patient?", "type": "Label", "visible": True}

'''Objects of menu patient card info button'''
patientCardInfoLoadExamButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "loadExamButtonId", "type": "LoadExamButton", "visible": True}
patientCardInfoPrintExamButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "printExamButtonId", "type": "CircularButton", "visible": True}
patientCardInfoExportExamButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "exportExamButtonId", "type": "CircularButton", "visible": True}
patientCardInfoOtherOptionsExamButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "otherOptionsExamButtonId", "type": "CircularButton", "visible": True}
patientCardInfoChangePatientButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "changePatientButtonId", "type": "ChangePatientButton", "visible": True}
patientCardInfoDeleteExamButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "deleteExamButtonId", "type": "DeleteButton", "visible": True}
otherOptionExamButtonExaminationList = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "otherOptionsExamButtonId", "type": "CircularButton", "visible": True}
deleteExamWarningPopUp = {"container": mainWindow, "id": "deleteRecordItemId", "type": "WarningPopUp", "visible": True}
confirmDeleteExamWarningPopUp = {"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "visible": True}
discardDeleteExamWarningPopUp = {"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton", "visible": True}
patientCardInfoDeleteExamYesButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "yesButn", "text": "yes", "type": "Button", "visible": True}
patientCardInfoDeleteExamNoButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "noButn", "text": "no", "type": "Button", "visible": True}
#patientCardInfoEditPatientButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "editPatientButtonId", "type": "EditPatientInfo", "unnamed": 1, "visible": True}
patientCardInfoEditPatientButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "editPatientButtonId", "type": "Button", "visible": True}
patientCardInfoExamSummaryTextArea = {"container": patientCardScreen_MainWindow, "id": "examSummaryTextAreaId", "type": "TextArea", "visible": True}
patientCardInfoDeletePatientButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "deletePatientButtonId", "type": "DeleteButton", "visible": True}
patientCardInfoDeletePatientYesButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "yesButn", "text": "yes", "type": "Button", "visible": True}
patientCardInfoDeletePatientNoButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "noButn", "text": "no", "type": "Button", "visible": True}
#patientCardInfoSavePatientButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "savePatientButtonId", "type": "CircularButton", "visible": True}
patientCardInfoSavePatientButton = {"checkable": False, "container": mainWindow, "id": "savePatientButtonId", "type": "CircularButton", "visible": True}


patientCardInfoCancelPatientButton = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "cancelPatientButtonId", "type": "CircularButton", "visible": True}

patientCardAddPatientCancelPopUpMessage = {"container": mainWindow, "id": "warningMessageId", "type": "Label", "visible": True}
patientCardAddPatientPopUpConfirmButton = {"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
patientCardAddPatientPopUpCancelButton = {"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
patientCradEditPatientPopUpCancelButton = {"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
patientCardEditPatientSavePopUpConfirmButton = {"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "Button", "visible": True}
patientCardEditPatientSavePopUpMessage = {"container": mainWindow, "id": "errorPopupId", "type": "ErrorPopup", "visible": True}
patientCardEditScreenSetPatientForRecordingButton = {"checkable": False, "container": mainWindow, "id": "setPatientForRecordButtonId", "type": "CircularButton", "visible": True}
patientCardEditScreenDeletePatientButton = {"checkable": False, "container": mainWindow, "id": "deletePatientButtonId", "type": "DeleteButton", "visible": True}
patientCardEditDeletePopUpMessage = {"container": mainWindow, "id": "deleteWarningItemId", "type": "WarningPopUp", "visible": True}
patientCardEditDeletePopUpConfirmButton = {"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "visible": True}
patientCardEditDeletePopUpCancelButton = {"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton", "visible": True}
examinationListView = {"container": patientCardScreen_MainWindow, "id": "examListViewId", "type": "ListView", "visible": True}
patientCardScrollBar = {"container": patientCardScreen_MainWindow, "index": 0,  "type": "Rectangle", "unnamed": 1, "visible": True}
patientRecord = {"container": patientCardScreen_MainWindow, "id": "outlineId", "type": "Rectangle", "visible": True}
muliExamDeleteButtonPatientCard = {"checkable": False, "container": patientCardScreen_MainWindow, "id": "multiExamDeleteButtonId", "type": "DeleteButton", "visible": True}
multiExamDeletePopUp = {"container": mainWindow, "id": "deleteRecordItemId", "type": "WarningPopUp", "visible": True}
multiExamDeleteCancelButton = {"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton", "visible": True}
multiExamDeleteConfirmButton = {"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "visible": True}


'Localization testing-Objects'

'1) Patient card screen'
patientOpButtnColumnId={"container":mainWindow, "id": "patientOpButtnColumnId", "type": "Column", "unnamed": 1, "visible": True}         
patientDelete={"container": mainWindow, "id": "patientDelete", "type": "Column", "unnamed": 1, "visible": True}
deleteWarningItemId={"container": mainWindow, "id": "deleteWarningItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
WarningconfirmButtonId={"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
sortingButtonsId={"container": mainWindow, "id": "sortingButtonsId", "type": "Item", "unnamed": 1, "visible": True}
nameSortButtonId={"checkable": False, "container": mainWindow, "id": "nameSortButtonId", "type": "SortingButton", "unnamed": 1, "visible": True}
patientidSortButtonId={"checkable": False, "container": mainWindow, "id": "patientidSortButtonId", "type": "SortingButton", "unnamed": 1, "visible": True}
lastrecordDateTimeSortButtonId={"checkable": False, "container": mainWindow, "id": "lastrecordDateTimeSortButtonId", "type": "SortingButton", "unnamed": 1, "visible": True}
SearchtextID={"backgroundcolor": "#f6f6f6", "container": mainWindow, "echoMode": 0, "id": "patientSearchInputId", "type": "SearchBar", "unnamed": 1, "visible": True}
patientInfoId={"container": mainWindow, "id": "patientInfoId", "type": "PatientInfoTable", "unnamed": 1, "visible": True}
genderMaleRadioButtonId={"checkable": True, "container": mainWindow, "id": "genderMaleRadioButtonId", "type": "CustomRadioButton", "unnamed": 1, "visible": True}
genderFemaleRadioButtonId={"checkable": True, "container": mainWindow, "id": "genderFemaleRadioButtonId", "type": "CustomRadioButton", "unnamed": 1, "visible": True}
genderOtherRadioButtonId={"checkable": True, "container": mainWindow, "id": "genderOtherRadioButtonId", "type": "CustomRadioButton", "unnamed": 1, "visible": True}
classificationComboBoxId={"container": mainWindow, "id": "classificationComboBoxId", "type": "CustomComboBox", "unnamed": 1, "visible": True}
pacemakeYesButtonId={"checkable": True, "container": mainWindow, "id": "pacemakeYesButtonId", "type": "CustomRadioButton", "unnamed": 1, "visible": True}
pacemakeNoButtonId={"checkable": True, "container": mainWindow, "id": "pacemakeNoButtonId", "type": "CustomRadioButton", "unnamed": 1, "visible": True}
textId={"backgroundcolor": "#ffffff", "container": mainWindow, "echoMode": 0, "id": "textId", "type": "TextField", "unnamed": 1, "visible": True}
classificationComboBoxId={"container": mainWindow, "id": "classificationComboBoxId", "type": "CustomComboBox", "unnamed": 1, "visible": True} 
European_Text={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 2, "type": "ItemDelegate", "unnamed": 1, "visible": True}
Northeast_Asian={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 3, "type": "ItemDelegate", "unnamed": 1, "visible": True}
Japan_text={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 4, "type": "ItemDelegate", "unnamed": 1, "visible": True}
African_text={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 5, "type": "ItemDelegate", "unnamed": 1, "visible": True}
Southeast_Asian={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 6, "type": "ItemDelegate", "unnamed": 1, "visible": True}
North_Indians={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 7, "type": "ItemDelegate", "unnamed": 1, "visible": True}
South_Indians={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 8, "type": "ItemDelegate", "unnamed": 1, "visible": True}
African_American={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 9, "type": "ItemDelegate", "unnamed": 1, "visible": True}
Mexican_text={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 10, "type": "ItemDelegate", "unnamed": 1, "visible": True}
Latio_American={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 11, "type": "ItemDelegate", "unnamed": 1, "visible": True}
Iberian_text={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 12, "type": "ItemDelegate", "unnamed": 1, "visible": True}
Pakistanis_text={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 13, "type": "ItemDelegate", "unnamed": 1, "visible": True}
Polynesian={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "occurrence": 14, "type": "ItemDelegate", "unnamed": 1, "visible": True}
patientCardAddviewId={"container": mainWindow, "id": "patientCardAddviewId", "type": "PatientCardAddview", "unnamed": 1, "visible": True}


counter = 0
# Function to navigate  to add patient  from patient card screen
def navigateToAddPatientFromPatientCardScreen():
    try:
        status = False
        if waitForObject(patientCardAddButton):
            if object.exists(patientCardAddButton):
                mouseClick(patientCardAddButton)
        else:
            #takeScreenShot()
            test.log("Patient card add patient button is not active")
        if waitForObject(patientCardAddPatientSaveButton):
            #test.log("Successfully add patient screen in patient card screen is displayed")
            status = True
        else:
            #takeScreenShot()
            test.log("Add patient screen in patient card screen is not displayed")   
            status = False
        return status
    
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to navigate to patient card screen from add patient screen
def navigateToPatientCardScreenFromAddPatientScreen():
    try:
        status = False
        if waitForObject(patientCardAddPatientBackButton):
            if object.exists(patientCardAddPatientBackButton):
                mouseClick(patientCardAddPatientBackButton)
                snooze(1)
        else:
            #takeScreenShot()
            test.log("Patient card add patient back button is not active")            
        if waitForObject(patientCardAddButton):
            #test.log("Successfully navigated to patient card screen from add patient screen")
            status = True
        else:
            #takeScreenShot()
            test.fail("Patient card screen is not displayed")
            status = False
                
        return status
       
    except Exception as e:
        test.fail("Exception" + str(e))
    
# Function to navigate to menu screen from add patient screen
def navigateToMenuScreenFromAddPatientScreen():
    try:
        status = False
        if object.exists(patientCardAddPatientBackButton):
            mouseClick(waitForObject(patientCardAddPatientBackButton))
            snooze(2)
            mouseClick(waitForObject(patientCardAddPatientBackButton))
            snooze(2)

            if object.exists(menuScreen_MainWindow):
                test.log("Successfully navigated to menu screen from add patient screen")
                status = True
            else:
                test.log("Menu screen is not displayed")
                status = False
                
        return status
       
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to navigate to live screen from add patient screen
def navigateToLiveScreenFromAddPatientScreen():
    try:
        status = False
        if object.exists(patientCardAddPatientBackButton):
            mouseClick(waitForObject(patientCardAddPatientBackButton))
            snooze(2)
            mouseClick(waitForObject(patientCardAddPatientBackButton))
            snooze(2)
            mouseClick(waitForObject(menuRecordingButton))
            snooze(2)


            if object.exists(liveScreenPatientListButton):
                test.log("Successfully navigated to live screen from add patient screen")
                status = True
            else:
                test.log("Live screen is not displayed")
                status = False
        return status
       
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to navigate to live screen from  patient card screen
def navigateToLiveScreenFromPatientCardScreen():
    try:
        status = False
        snooze(1)
        if waitForObject(patientCardAddPatientBackButton):
            if object.exists(patientCardAddPatientBackButton):
                mouseClick(patientCardAddPatientBackButton)
        if waitForObject(menuRecordingButton):
            if object.exists(menuRecordingButton):
                mouseClick(menuRecordingButton)
        snooze(2)
        if waitForObject(liveScreenPatientListButton):
            status = True
        else:
            status = False                
        return status
       
    except Exception as e:
        test.fail("Exception" + str(e))
        
#Function to verify age based on input date of birth
def ageFromInputDOBInPatientCard(PatientDOB=""):
    try:
        if navigateToMenuScreenFromLiveScreen():
            if navigateToPatientCardScreenFromMenuScreen():
                test.log(" Device navigate to patient card from menu screen")
            else:
                test.log("Failed to navigate to patient card screen from Menu screen")
        else:
            test.log("Device fails to navigate menu screen from waveform screen")
        ''' Navigate to add patient screen '''
        if navigateToAddPatientFromPatientCardScreen():
            test.log("Device navigate to add Patient screen")
        else:
            test.log("Failed to navigate add Patient screen")
        if object.exists(patientCardAddPatientDOBInput):
            setFocusTextBox(patientCardAddPatientDOBInput)
            type(mainWindow, PatientDOB)
            snooze(1)
            # Handling 'system can not handle date of birth / out of range' scenario
            type(mainWindow, "<Tab>")       
            if (object.exists(patientcardDobErrorPopUp)):
                mouseClick(waitForObject(patientcardDobErrorOkButton))
            snooze(1) 
        else:
            test.log("Failed to write DOB in DOB input field in add Patient screen patient List ")
        if object.exists(patientCardAddPatientAgeInput):
                AgeInput =(waitForObject(patientCardAddPatientAgeInput))
                age =  AgeInput.text
        else:
            test.log("Age is not calculated as per input DOB")
        return age
    except Exception as e:
        test.fail("Exception" +str(e))

#Function to verify DOB based on input age
def dOBFromInputAgeInPatientCard(PatientAge=""):
    try:
        if navigateToMenuScreenFromLiveScreen():
            if navigateToPatientCardScreenFromMenuScreen():
                test.log(" Device navigate to patient card from menu screen")
            else:
                test.log("Failed to navigate to patient card screen from Menu screen")
        else:
            test.log("Device fails to navigate menu screen from waveform screen")
        ''' Navigate to add patient screen '''
        if navigateToAddPatientFromPatientCardScreen():
            test.log("Device navigate to add Patient screen")
        else:
            test.log("Failed to navigate add Patient screen")
        if object.exists(patientCardAddPatientAgeInput):
            setFocusTextBox(patientCardAddPatientAgeInput)
            type(mainWindow, PatientAge)
            snooze(1)
            # Handling 'system can not handle date of birth / out of range' scenario
            type(mainWindow, "<Tab>")  
        else:
            test.log("Failed to write age in age input field in add Patient screen patient List ")
        if object.exists(patientCardAddPatientDOBInput):
            dateOfBirth = findObject(patientCardAddPatientDOBInput)
            dob =  dateOfBirth.text
            #return True
        else:
            test.log("Age is not calculated as per input DOB")
            #return False

        return dob
    except Exception as e:
        test.fail("Exception" +str(e)) 

#Function to add a new patient in live patient list screen LX
def addNewPatientInLivePatientCardScreenLX(Surname="",Firstname="",Title="",PatientDOB="",PatientAge="",PatientId="",HospitalId="",Weight="",Height="",Gender="",PaceMaker="",Digoxin="",action=""):
    try:
        
        count = 0
        if Surname:
            if object.exists(addPatientCardSurnameFieldLX):
                setFocusTextBox(addPatientCardSurnameFieldLX)
                snooze(1)
                type(mainWindow, Surname)
                if action == "save":                    
                    mouseClick(waitForObject(saveButtonAddPatientCardInputLX))
                    snooze(1)
                    count = count + 1
                elif action == "cancel":
                    mouseClick(waitForObject(cancelButtonAddPatientCardInputLX))
                    snooze(1)
                elif action == "close":
                    mouseClick(waitForObject(closeButtonAddPatientCardInputLX))
                    snooze(1)
        if Firstname:
            if object.exists(addPatientCardFirstNameFieldLX):
                setFocusTextBox(addPatientCardFirstNameFieldLX)
                snooze(1)
                type(mainWindow, Firstname)
                if action == "save":                    
                    mouseClick(waitForObject(saveButtonAddPatientCardInputLX))
                    count = count + 1
                    snooze(1)
                elif action == "cancel":
                    mouseClick(waitForObject(cancelButtonAddPatientCardInputLX))
                    snooze(1)
                elif action == "close":
                    mouseClick(waitForObject(closeButtonAddPatientCardInputLX))
                    snooze(1)
        if Title:
            if object.exists(addPatientCardTitleFieldLX):
                setFocusTextBox(addPatientCardTitleFieldLX)
                snooze(1)
                type(mainWindow, Title)
                if action == "save":                    
                    mouseClick(waitForObject(saveButtonAddPatientCardInputLX))
                    count = count + 1
                    snooze(1)
                elif action == "cancel":
                    mouseClick(waitForObject(cancelButtonAddPatientCardInputLX))
                    snooze(1)
                elif action == "close":
                    mouseClick(waitForObject(closeButtonAddPatientCardInputLX))
                    snooze(1) 
        if  PatientDOB:
            if object.exists(addPatientCardDOBFieldLX):
                setFocusTextBox(addPatientCardDOBFieldLX)
                snooze(1)
                type(mainWindow, PatientDOB)                
                if action == "save":                    
                    mouseClick(waitForObject(saveButtonAddPatientCardInputLX))
                    count = count + 1
                    snooze(1)
                elif action == "cancel":
                    mouseClick(waitForObject(cancelButtonAddPatientCardInputLX))
                    snooze(1)
                elif action == "close":
                    mouseClick(waitForObject(closeButtonAddPatientCardInputLX))
                    snooze(1)
                # Handling 'system can not handle date of birth / out of range' scenario
                '''type(mainWindow, "<Tab>")       
                if (object.exists(livePatientDialogErrorOkButton)):
                    mouseClick(waitForObject(livePatientDialogErrorOkButton))
                    snooze(1) ''' 
        if PatientId:
            if object.exists(addPatientPatientIDFieldLX):
                setFocusTextBox(addPatientPatientIDFieldLX)
                snooze(1)
                type(mainWindow, PatientId)                
                if action == "save":                    
                    mouseClick(waitForObject(saveButtonAddPatientCardInputLX))
                    count = count + 1
                    snooze(1)
                elif action == "cancel":
                    mouseClick(waitForObject(cancelButtonAddPatientCardInputLX))
                    snooze(1)
                elif action == "close":
                    mouseClick(waitForObject(closeButtonAddPatientCardInputLX))
                    snooze(1)
                '''# Handling 'system can not handle date of birth / out of range' scenario
                type(mainWindow, "<Tab>")       
                if (object.exists(livePatientDialogErrorOkButton)):
                    mouseClick(waitForObject(livePatientDialogErrorOkButton))
                    snooze(1)'''
        if HospitalId:
            if object.exists(addPatientHospitalIDFieldLX):
                setFocusTextBox(addPatientHospitalIDFieldLX)
                snooze(1)
                type(mainWindow, HospitalId)                
                if action == "save":                    
                    mouseClick(waitForObject(saveButtonAddPatientCardInputLX))
                    count = count + 1
                    snooze(1)
                elif action == "cancel":
                    mouseClick(waitForObject(cancelButtonAddPatientCardInputLX))
                    snooze(1)
                elif action == "close":
                    mouseClick(waitForObject(closeButtonAddPatientCardInputLX))
                    snooze(1)
                # Handling Hospital Id already exists dialog
                '''type(mainWindow, "<Tab>")
                if (object.exists(livePatientDialogErrorOkButton)):
                    mouseClick(waitForObject(livePatientDialogErrorOkButton))
                    snooze(1)'''                                            
        if Gender:
            value = Gender.strip()
            upper = value.upper()                
            if upper == "MALE":
                mouseClick(waitForObject(addPatientCardGenderMaleRadioButtonLX))                
            elif upper == "FEMALE":
                mouseClick(waitForObject(addPatientCardGenderfemaleRadioButtonLX))                
            elif upper == "OTHER":
                mouseClick(waitForObject(addPatientCardGenderOtherRadioButtonLX))                                        
            else:
                pass
            snooze(1)
        if Weight:
            if object.exists(addPatientCardWeightFieldLX):
                setFocusTextBox(addPatientCardWeightFieldLX)
                snooze(1)
                type(mainWindow, Weight)               
                if action == "save":                    
                    mouseClick(waitForObject(saveButtonAddPatientCardInputLX))
                    count = count + 1
                    snooze(1)
                elif action == "cancel":
                    mouseClick(waitForObject(cancelButtonAddPatientCardInputLX))
                    snooze(1)
                elif action == "close":
                    mouseClick(waitForObject(closeButtonAddPatientCardInputLX))
                    snooze(1)
        if Height :
            if object.exists(addPatientCardHeightFieldLX):
                setFocusTextBox(addPatientCardHeightFieldLX)
                snooze(1)
                type(mainWindow, Height)               
                if action == "save":                    
                    mouseClick(waitForObject(saveButtonAddPatientCardInputLX))
                    count = count + 1
                    snooze(1)
                elif action == "cancel":
                    mouseClick(waitForObject(cancelButtonAddPatientCardInputLX))
                    snooze(1)
                elif action == "close":
                    mouseClick(waitForObject(closeButtonAddPatientCardInputLX))
                    snooze(1)               
        if PaceMaker:
            value = PaceMaker.strip()
            upper = value.upper()                
            if upper == "YES":
                mouseClick(waitForObject(addPatientCardPacemakerSelectorLX))                
            elif upper == "NO":
                mouseClick(waitForObject(addPatientCardPacemakerSelectorLX))                
            else:
                pass            
        if Digoxin:
            value = Digoxin.strip()
            upper = value.upper()                
            if upper == "YES":
                mouseClick(waitForObject(addPatientCardDigoxinSelectorLX))                
            elif upper == "NO":
                mouseClick(waitForObject(addPatientCardDigoxinSelectorLX))                
            else:
                pass
        if count > 0:
            return True
        else:
            return False  

                
    except Exception as e:
        test.fail("Exception" +str(e))       
# Function to add a new patient in  patient card screen
def addNewPatientInPatientCardScreen(Surname="", Firstname="", Title="", PatientDOB="", PatientAge="", PatientId="", HospitalId="", Weight="", Height="", Gender="", PaceMaker="", Digoxin=""):
    try:
        count = 0
        if object.exists(patientCardAddPatientSurnameInput):
            setFocusTextBox(patientCardAddPatientSurnameInput)
            type(mainWindow, Surname)
            count = count + 1
            snooze(1)            
        if object.exists(patientCardAddPatientFirstNameInput):
            setFocusTextBox(patientCardAddPatientFirstNameInput)
            type(mainWindow, Firstname)
            count = count +1
            snooze(1)            
        if object.exists(patientCardAddPatientTitleInput):
            setFocusTextBox(liveScreenAddPatientTitleInput)
            type(mainWindow, Title)
            snooze(1)                
        if object.exists(patientCardAddPatientDOBInput):
            setFocusTextBox(patientCardAddPatientDOBInput)
            type(mainWindow, PatientDOB)
            snooze(1)
            # Handling 'system can not handle date of birth / out of range' scenario
            type(mainWindow, "<Tab>")       
            if (object.exists(patientcardDobErrorPopUp)):
                mouseClick(waitForObject(patientcardDobErrorOkButton))
            snooze(1) 
        if object.exists(patientCardAddPatientIdInput):
            setFocusTextBox(patientCardAddPatientIdInput)
            type(mainWindow, PatientId)
            count = count + 1
            # Handling Patient Id already exists dialog
            type(mainWindow, "<Tab>")       
            if (object.exists(patientcardPatientIdErrorPopUp)):
                mouseClick(waitForObject(patientcardPatientIdErrorOkButton))
            snooze(1)           
        if object.exists(patientCardAddPatientHospitalIdInput):
            setFocusTextBox(patientCardAddPatientHospitalIdInput)
            type(mainWindow, HospitalId)
            count = count + 1
            # Handling Hospital Id already exists dialog
            type(mainWindow, "<Tab>")
            if (object.exists(patientCardAddPatientDialogOkButton)):
                mouseClick(waitForObject(patientCardAddPatientDialogOkButton))
            snooze(1)            
        if Gender:
            value = Gender.strip()
            upper = value.upper()                
            if upper == "MALE":
                mouseClick(waitForObject(patientCardAddPatientMaleRadioButton))
            elif upper == "FEMALE":
                mouseClick(waitForObject(patientCardAddPatientFemaleRadioButton))
            elif upper == "OTHER":
                mouseClick(waitForObject(patientCardAddPatientOthersRadioButton))
            else:
                pass            
        if object.exists(patientCardAddPatientWeightInput):
            setFocusTextBox(patientCardAddPatientWeightInput)
            type(mainWindow, Weight)            
            snooze(1)             
        if object.exists(patientCardAddPatientHeightInput):
            setFocusTextBox(liveScreenAddPatientHeightInput)
            type(mainWindow, Height) 
            snooze(1)                
        if PaceMaker:
            value = PaceMaker.strip()
            upper = value.upper()                
            if upper == "YES":
                mouseClick(waitForObject(patientCardAddPatientPaceMakeYesButton))
            elif upper == "NO":
                mouseClick(waitForObject(patientCardAddPatientPaceMakeNoButton))
            else:
                pass            
        if Digoxin:
            value = Digoxin.strip()
            upper = value.upper()                
            if upper == "YES":
                mouseClick(waitForObject(patientCardAddPatientDigoxinYesButton))
            elif upper == "NO":
                mouseClick(waitForObject(patientCardAddPatientDigoxinNoButton))
            else:
                pass  
        
        if count > 0:
            return True
        else:
            return False  
            
    except Exception as e:
        test.fail("Exception" + str(e))      
        
# Function to save the patient details after adding the patient details in add patient card screen
def saveForAddingAPatientInPatientCardScreen(pid):
    try:
        status = False
        if object.exists(patientCardAddPatientSaveButton):
            mouseClick(waitForObject(patientCardAddPatientSaveButton))
            #if object.exists(patientcardSaveErrorPopUp):
                #textMessage = str(waitForObject(patientcardSaveErrorPopUp).warning)
                #if "required" in textMessage:
            if object.exists(patientcardSaveErrorOkButton):
                samePatientIDPopUpHandler()
                counter = counter + 1
                status = "Pass"
            else:
                test.log("Pop up message is different")
            #else:
                #test.log("patient card save error pop up is missing")                
        else:
            test.log("Could not find Patient card add patient save button ")
        if object.exists(patientCardScreen_MainWindow):   
            searchBox = (waitForObject(patientCardSearchInput))
            snooze(1)
            searchBox.text = ""
            snooze(1)
            type(waitForObject(patientCardSearchInput), pid)
            snooze(2)
            parent = waitForObject(patientCardPatientListView)
            child = object.children(parent)
            child_1 = object.children(child[0])            
            for i in child_1:
                child_2 = object.children(i)
                if len(child_2) > 0:
                    child_3 = object.children(child_2[0])
                    value = child_3[1].text
                    #test.log("value=%s" % value)                    
                    if str(value) == pid:
                        test.log("Successfully saved the patient details in the patient card screen")
                        status = True
                    else:
                        test.log("The patient details are not saved in the patient card screen")
        else:
            test.log("Could not find patient card screen")            
        return status
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to save the patient details after adding the patient details in add patient card screen
def saveForAddPatientInPatientCardScreen():
    try:
        global counter
        status = False
        if object.exists(patientCardAddPatientSaveButton):
            mouseClick(waitForObject(patientCardAddPatientSaveButton))
            #if object.exists(patientcardSaveErrorPopUp):
                #textMessage = str(waitForObject(patientcardSaveErrorPopUp).warning)
                #if "required" in textMessage:
            if object.exists(patientCardDialogErrorOkButton):
                samePatientIDPopUpHandlerPatientCard()
                counter = counter + 1
                status = True
            else:
                if object.exists(patientCardAddButton):
                    test.log("error pop up message is not present")
                    status = True
                else:
                    status = False
            #else:
                #test.log("patient card save error pop up is missing")                
        else:
            test.log("Could not find Patient card add patient save button ")
        return status
    except Exception as e:
        test.fail("Exception" + str(e)) 
            
#Function to search patient in patient card by PID
def searchPatientInPatientCardScreen(pid):
    try:
        status = False
        if object.exists(patientCardScreen_MainWindow):   
            searchBox = (waitForObject(patientCardSearchInput))
            snooze(1)
            searchBox.text = ""
            snooze(1)
            type(waitForObject(patientCardSearchInput), pid)
            snooze(2)
            parent = waitForObject(patientCardPatientListView)
            child = object.children(parent)
            child_1 = object.children(child[0])            
            for i in child_1:
                child_2 = object.children(i)
                if len(child_2) > 0:
                    child_3 = object.children(child_2[0])
                    value = child_3[1].text
                    #test.log("value=%s" % value)                    
                    if str(value) == pid:
                        test.log("Successfully saved the patient details in the patient card screen")
                        status = True
                    else:
                        test.log("The patient details are not saved in the patient card screen")
        else:
            test.log("Could not find patient card screen")            
        return status
    except Exception as e:
        test.fail("Exception" + str(e))     
# Function to set patient for Recording in patient card screen
def setPatientForRecordingInPatientCard():
    try:
        status = False
        if object.exists(patientCardSetPatientForRecordButton):
            mouseClick(waitForObject(patientCardSetPatientForRecordButton))
            if object.exists(patientcardSaveErrorOkButton):
                samePatientIDPopUpHandler()
                counter = counter + 1
                status = True
            elif object.exists(patientcardHospitalIDExistErrorOKButton):
                samePatientIDPopUpHandler()                
            else:
                snooze(1)
                if object.exists(liveScreenPatientListButton):
                    test.log("Navigate to waveform screen from add patient screen patient card")
                    status = True
                else:
                    test.log("Failed to navigate to live screen from add patient screen patient card")
                    status = False
        return status      
            
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to back to patient card without saving patient information 
def backFromAddingAPatientInPatientCardScreen(pid):
    try:
        status = False
        if object.exists(patientCardAddPatientBackButton):
            mouseClick(waitForObject(patientCardAddPatientBackButton))            
        else:
            test.log("Could not find Patient card add patient back button ")
        if object.exists(patientCardScreen_MainWindow):                
            searchBox = (waitForObject(patientCardSearchInput))
            searchBox.text = ""
            type(waitForObject(patientCardSearchInput), pid)
            snooze(2)
            if object.exists(patientRecord):
                parent = waitForObject(patientCardPatientListView)
                child = object.children(parent)
                child_1 = object.children(child[0])            
                for i in child_1:
                    child_2 = object.children(i)
                    if len(child_2) > 0:
                        child_3 = object.children(child_2[0])
                        value = child_3[1].text
                        #test.log("value=%s" % value)                    
                        if str(value) == pid:
                            test.log("Successfully saved the patient details in the patient card screen")
                            status = False
                        else:
                            test.log("The patient details are not saved in the patient card screen")
                            status = True                    
            else:
                test.log("The patient details is cancelled in the  patient card screen")
                status = True
        else:
            test.log("Could not find patient card main window")            

        return status   
    
    except Exception as e:
        test.fail("Exception" + str(e))       
# Function to cancel the patient details in patient card add patient screen
def cancelForAddingAPatientInPatientCardScreen(pid):
    try:
        status = False
        if object.exists(patientCardAddPatientCancelButton):
            mouseClick(waitForObject(patientCardAddPatientCancelButton))
            snooze(1)
            if object.exists(patientCardAddPatientCancelPopUpMessage):
                cancelWarningMessage = str(waitForObject(patientCardAddPatientCancelPopUpMessage).text)
                textMessage = "discard the changes"
                if textMessage in cancelWarningMessage:
                    mouseClick(waitForObject(patientCardAddPatientPopUpConfirmButton))
                else:
                    test.log("Warning message in pop up : "+cancelWarningMessage)
                    mouseClick(waitForObject(patientCardDeletePatientNoButton))
            else:
                test.log("Could not find cancel warning pop up message")
        else:
            test.log("Could not find Patient card add patient cancel button ")
        if object.exists(patientCardScreen_MainWindow):                
            searchBox = (waitForObject(patientCardSearchInput))
            searchBox.text = ""
            type(waitForObject(patientCardSearchInput), pid)
            snooze(2)
            if object.exists(patientRecord):
                parent = waitForObject(patientCardPatientListView)
                child = object.children(parent)
                child_1 = object.children(child[0])            
                for i in child_1:
                    child_2 = object.children(i)
                    if len(child_2) > 0:
                        child_3 = object.children(child_2[0])
                        value = child_3[1].text
                        #test.log("value=%s" % value)                    
                        if str(value) == pid:
                            test.log("Successfully saved the patient details in the patient card screen")
                            status = False
                        else:
                            test.log("The patient details are not saved in the patient card screen")
                            status = True                    
            else:
                test.log("The patient details is cancelled in the  patient card screen")
                status = True
        else:
            test.log("Could not find patient card main window")            

        return status   
    
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to search the patient by patient ID in patient card screen
def searchThePatientInPatientCardScreen(pid):
    try:
        status = False
        if object.exists(patientCardSearchInput):
            searchBox = (waitForObject(patientCardSearchInput))
            searchBox.text = ""
            type(waitForObject(patientCardSearchInput), pid)
            patientListView = waitForObject(patientCardPatientListView)
            item = object.children(patientListView)
            row = object.children(item[0])
                
            for i in row:
                outline = object.children(i)
                if len(outline) > 0:
                    label = object.children(outline[0])
                    value = label[1].text
                
                    if (value == pid):
                        snooze(1)
                        longMouseClick(row[0])
                        test.log("The given patient is present in the patient card Screen")
                        status = True
                    else:
                        test.log("Given patient is not present in the patient list screen")
                        status = False                       
                       
        else:
            test.fail("Patient's record with patient id "+pid+" is not found")
        
        return status
    
    except Exception as e:
        test.fail("Exception: " + str(e)) 
        
# Function to search and select patient by patient ID to delete in patient card screen
def searchAndSelectPatientToDeleteInPatientCardScreen(patientList):
    try:
        status = False
        #global count
        patientListToDelete = patientList
        for i in range(len(patientListToDelete)):
            if object.exists(patientCardSearchInput):
                searchBox = (waitForObject(patientCardSearchInput))
                searchBox.text = ""
                type(waitForObject(patientCardSearchInput), patientListToDelete[i])
                patientListView = waitForObject(patientCardPatientListView)
                item = object.children(patientListView)
                row = object.children(item[0])                
                for j in row:
                    outline = object.children(j)
                    if len(outline) > 0:
                        row0 = object.children(outline[0])
                        label = object.children(row0[0])
                        value = label[3].text                
                        if (value == str(patientListToDelete[i])):
                            snooze(1)
                            longMouseClick(j)
                            #count = count + 1
                            test.log("The given patient is present in the patient card Screen")
                            status = True
                        else:
                            test.log("Given patient is not present in the patient list screen")
                            status = False                     
            else:
                test.fail("Patient card search input object not found")        
        return status
    
    except Exception as e:
        test.fail("Exception: " + str(e))       
# Function to search the patient to edit the patient details in the patient card screen
# Function to Search  and select the patient in patient card screen for examination
def searchAndSelectPatientInPatientCardScreenForExamination(patientIDSearch):
    try:
        Status = False
        patientIDToSearch = patientIDSearch
        snooze(1)
        if (waitForObject(patientCardSearchInput)):
            type(waitForObject(patientCardSearchInput), patientIDToSearch)
            
            if (waitForObject(patientCardPatientListView)):               
                
                patientTable = waitForObject(patientCardPatientListView)
                patientListItem = object.children(patientTable)
                snooze(1)
                patientItemRows = object.children(patientListItem[0])
                
                if len(patientItemRows):
                    for i in range(len(patientItemRows)):
                                   
                        childRows = object.children(patientItemRows[i])
                        if len(childRows):
                            subRows = object.children(childRows[0])
                            innerRows = object.children(subRows[0])
                            
                            rowValue = innerRows[3].text
                            if (rowValue == patientIDToSearch):
                                test.log(" Successfully searched '"+ patientIDToSearch +"' record from Patient Card")
                                columnRecording = object.children(childRows[1])
                                mouseClick(columnRecording[1])
                                
                                if (waitForObject(liveScreenECGRecordButton)):
                                    Status = True
                                    test.log(" Patient record %s is selected for examination "% patientIDToSearch)
                                    break
                else:
                    test.log("No matching record found in Patient Card with the given patient ID %s "  %patientIDToSearch)
                                        
            else:
                    test.log("Failed to search '"+ patientIDToSearch +"' record from Patient Card")            
        else:
            test.log("Failed to search '"+ patientIDToSearch +"' record from Patient Card")
        
        if Status:
            test.log(" Successfully navigated to Live waveform screen ")
            return True
        else:
            test.log(" Failed to navigate to Live waveform screen")           
            return False                

    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to edit the patient details in patient card screen
def editPatientDetailsInPatientCardScreen(Surname="", Firstname="", Title="", PatientDOB="", PatientAge="", PatientId="", HospitalId="", Weight="", Height="", Gender="", PaceMaker="", Digoxin=""):
    try:
        count = 0
        snooze(2)
        if object.exists(patientCardInfoEditPatientButton):
            mouseClick(waitForObject(patientCardInfoEditPatientButton))
            snooze(2)
            
            if Surname:
                if object.exists(patientCardAddPatientSurnameInput):
                    surnameInput = (waitForObject(patientCardAddPatientSurnameInput))
                    surnameInput.text = ""
                    setFocusTextBox(patientCardAddPatientSurnameInput)
                    type(mainWindow, Surname)                    
                    #surnameInput.text = str(Surname)                    
                    snooze(0.5)
                    changedSurname = waitForObject(patientCardAddPatientSurnameInput)                    
                    if changedSurname.text == Surname :
                        test.log("Successfully changed the surname")
                    
                    else:
                        test.log("Surname is not changed")
                               
            if Firstname:
                if object.exists(patientCardAddPatientFirstNameInput):
                    firstNameInput = (waitForObject(patientCardAddPatientFirstNameInput))
                    firstNameInput.text = "" 
                    setFocusTextBox(patientCardAddPatientFirstNameInput)
                    type(mainWindow, Firstname)                   
                    snooze(1)
                    changedFirstname = waitForObject(patientCardAddPatientFirstNameInput)                    
                    if changedFirstname.text == Firstname :
                        test.log("Successfully changed the firstname")
                    
                    else:
                        test.log("Firstname is not changed")                    
            
            if Title:
                if object.exists(patientCardAddPatientTitleInput):
                    TitleInput = (waitForObject(patientCardAddPatientTitleInput))
                    TitleInput.text = ""
                    setFocusTextBox(patientCardAddPatientTitleInput)
                    type(mainWindow, Title)                     
                    snooze(1)
                    changedTitle = waitForObject(patientCardAddPatientTitleInput)                    
                    if changedTitle.text == Title :
                        test.log("Successfully changed the title")
                    
                    else:
                        test.log("Title is not changed")
                                    
            '''if PatientDOB:
                if object.exists(patientCardAddPatientDOBInput):
                    DOBInput =(waitForObject(patientCardAddPatientDOBInput))
                    snooze(1)
                    DOBInput.text=""
                    dateOfBirth = findObject(patientCardAddPatientDOBInput)
                    parent=object.parent(dateOfBirth)
                    mouseClick(parent)
                    type(waitForObject(patientCardAddPatientDOBInput),PatientDOB)
                    snooze(1)
                    test.passes("Successfully changed the patient's date of birth")
                    
                    return True'''
            
            if PatientAge:
                if object.exists(patientCardAddPatientAgeInput):
                    AgeInput = (waitForObject(patientCardAddPatientAgeInput))
                    AgeInput.text = ""
                    setFocusTextBox(patientCardAddPatientAgeInput)
                    type(mainWindow, PatientAge)                     
                    snooze(1)
                    changedPatientAge = waitForObject(patientCardAddPatientAgeInput)                    
                    if changedPatientAge.text == PatientAge :
                        test.log("Successfully changed the patient's age")
                    
                    else:
                        test.log("Patient's age is not changed")
                                
            if PatientId:
                if object.exists(patientCardAddPatientIdInput):
                    PatientIdInput = (waitForObject(patientCardAddPatientIdInput))
                    PatientIdInput.text = ""
                    setFocusTextBox(patientCardAddPatientIdInput)
                    type(mainWindow, PatientId)                    
                    snooze(1)
                    # Handling Patient Id already exists dialog
                    type(mainWindow, "<Tab>")      
                    if (object.exists(patientcardPatientIdErrorPopUp)):                
                        mouseClick(waitForObject(patientcardPatientIdErrorOkButton))
                        snooze(1) 
                    changedPatientId = waitForObject(patientCardAddPatientIdInput)                
                    if changedPatientId.text == PatientId :
                        test.log("Successfully changed the patient's id")
                        count = count + 1
                    else:
                        test.log("Patient's id is not changed")                    
                        
            if HospitalId:
                if object.exists(patientCardAddPatientHospitalIdInput):
                    HospitalIdInput = (waitForObject(patientCardAddPatientHospitalIdInput))
                    HospitalIdInput.text = ""
                    setFocusTextBox(patientCardAddPatientHospitalIdInput)
                    type(mainWindow, HospitalId)                              
                    # Handling Hospital Id already exists dialog
                    type(mainWindow, "<Tab>")
                    if (object.exists(patientcardPatientIdErrorPopUp)):
                        mouseClick(waitForObject(patientcardPatientIdErrorOkButton))
                        snooze(1)
                    changedHospitalId = waitForObject(patientCardAddPatientHospitalIdInput)                
                    if changedHospitalId.text == HospitalId :
                        test.log("Successfully changed the hospital id")
                        count = count + 1
                    else:
                        test.log("Hospital id is not changed")                    
                                    
            if Gender:
                value = Gender.strip()
                upper = value.upper()
                
                if upper == "MALE":
                    mouseClick(waitForObject(patientCardAddPatientMaleRadioButton))
                    test.log("Successfully changed the gender to male")
                
                elif upper == "FEMALE":
                    mouseClick(waitForObject(patientCardAddPatientFemaleRadioButton))
                    test.log("Successfully changed the gender to female")
                
                elif upper == "OTHER":
                    mouseClick(waitForObject(patientCardAddPatientOthersRadioButton))
                    test.log("Successfully changed the gender to other")
                    
                else:
                    test.log("Gender is not changed")
                                   
            if Weight:
                if object.exists(patientCardAddPatientWeightInput):
                    WeightInput = (waitForObject(patientCardAddPatientWeightInput))
                    WeightInput.text = ""
                    setFocusTextBox(patientCardAddPatientWeightInput)
                    type(mainWindow, Weight)                     
                    snooze(1)
                    changedWeight = waitForObject(patientCardAddPatientWeightInput)                    
                    if changedWeight.text == Weight :
                        test.log("Successfully changed the patient's weight")
                    
                    else:
                        test.log("Patient's weight is not changed")
                        
            if Height:
                if object.exists(patientCardAddPatientHeightInput):
                    HeightInput = (waitForObject(patientCardAddPatientHeightInput))
                    HeightInput.text = ""
                    setFocusTextBox(patientCardAddPatientHeightInput)
                    type(mainWindow, Height)                    
                    snooze(1)
                    changedHeight = waitForObject(patientCardAddPatientHeightInput)                    
                    if changedHeight.text == Height :
                        test.log("Successfully changed the patient's height")
                    
                    else:
                        test.log("Patient's height is not changed")
                            
            if PaceMaker:
                value = PaceMaker.strip()
                upper = value.upper()
                
                if upper == "YES":
                    mouseClick(waitForObject(patientCardAddPatientPaceMakeYesButton))
                    test.log("Successfully changed the pacemaker to yes")
                
                elif upper == "NO":
                    mouseClick(waitForObject(patientCardAddPatientPaceMakeNoButton))
                    test.log("Successfully changed the pacemaker to no")
                
                else:
                    test.log("Pacemaker is not changed")
                                
            if Digoxin:
                value = Digoxin.strip()
                upper = value.upper()
                
                if upper == "YES":
                    mouseClick(waitForObject(patientCardAddPatientDigoxinYesButton))
                    test.log("Successfully changed the Digoxin to yes")
                
                elif upper == "NO":
                    mouseClick(waitForObject(patientCardAddPatientDigoxinNoButton))
                    test.log("Successfully changed the Digoxin to no")
                
                else:
                    test.log("Digoxin is not changed")
                    
        return True 
    
    except Exception as e:
        test.fail("Exception" + str(e))
        
#Function to verify patient details in edit patient screen
def verifyEdittedPatientDetailsInPatientCardScreen(PatientId=""):
    try:
        patientInformation = []
        if object.exists(patientCardSearchInput):
            searchBox =(waitForObject(patientCardSearchInput))
            snooze(1)
            searchBox.text = ""
            type(waitForObject(patientCardSearchInput), PatientId)
            snooze(2)
            patientListView = waitForObject(patientCardPatientListView)
            item = object.children(patientListView)
            row = object.children(item[0])
                
            for i in row:
                outline = object.children(i)
                if len(outline) > 0:
                    label = object.children(outline[0])
                    value = label[1].text
                
                    if (value == PatientId):
                        test.log("The given pid is matching with the patient's pid in the list")
                        if object.exists(patientCardInfoButton):
                            mouseClick(waitForObject(patientCardInfoButton))
                            snooze(3)
                            if object.exists(patientCardInfoEditPatientButton):
                                mouseClick(waitForObject(patientCardInfoEditPatientButton))
                                snooze(2)
                                if object.exists(patientCardAddPatientSurnameInput):
                                    surnameInput =(waitForObject(patientCardAddPatientSurnameInput))
                                    surNameA = surnameInput.text
                                    patientInformation.append(str(surNameA))                               
                                    
                                if object.exists(patientCardAddPatientFirstNameInput):
                                    firstNameInput =(waitForObject(patientCardAddPatientFirstNameInput))
                                    firstNameA = firstNameInput.text                               
                                    patientInformation.append(str(firstNameA))
                                if object.exists(patientCardAddPatientTitleInput):
                                    TitleInput =(waitForObject(patientCardAddPatientTitleInput))
                                    titleA = TitleInput.text 
                                    patientInformation.append(str(titleA))                         
                                            
                                if object.exists(patientCardAddPatientAgeInput):
                                    AgeInput =(waitForObject(patientCardAddPatientAgeInput))
                                    ageA = AgeInput.text 
                                    patientInformation.append(str(ageA))                               
                                            
                                if object.exists(patientCardAddPatientIdInput):
                                    PatientIdInput =(waitForObject(patientCardAddPatientIdInput))
                                    patientIdA = PatientIdInput.text
                                    patientInformation.append(str(patientIdA))                                
                                    
                                if object.exists(patientCardAddPatientHospitalIdInput):
                                    HospitalIdInput =(waitForObject(patientCardAddPatientHospitalIdInput))
                                    hospitalIdA = HospitalIdInput.text
                                    patientInformation.append(str(hospitalIdA))                               
                                               
                                if object.exists(patientCardAddPatientWeightInput):
                                    WeightInput =(waitForObject(patientCardAddPatientWeightInput))
                                    weightA = WeightInput.text
                                    patientInformation.append(str(weightA))                                
                                    
                                if object.exists(patientCardAddPatientHeightInput):
                                    HeightInput =(waitForObject(patientCardAddPatientHeightInput))
                                    heightA = HeightInput.text
                                    patientInformation.append(str(heightA))

                            
                                
            return patientInformation            
               
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to set patient for recording after editing the patient details in patient card screen        
def setEditedPatientForRecordingInPatientCardScreen():
    try:
        status = False
        if object.exists(patientCardEditScreenSetPatientForRecordingButton):
            mouseClick(findObject(patientCardEditScreenSetPatientForRecordingButton))
            snooze(1)
            if object.exists(patientCardDialogErrorOkButton):
                samePatientIDPopUpHandlerPatientCard()
                counter = counter + 1
                status = True
            else:
                if object.exists(patientCardInfoEditPatientButton):
                    test.log("error pop up message is not present")
                    status = True
                else:
                    status = False
        else:
            test.log("Failed to find set patient for recording button in edit patient screen")            
        if object.exists(liveScreenPatientListButton):
            test.log("Successfully navigated to live screen from add patient screen")
            status = True
        else:
            test.log("Live screen is not displayed")
            status = False  
        return status   
    except Exception as e:
        test.fail("Exception" + str(e))        
#Function to save the patient details after editing the patient details in add patient Card screen
def saveForEditingPatientInPatientCardScreen():
    try:
        status = False
        if object.exists(patientCardInfoSavePatientButton):
            mouseClick(waitForObject(patientCardInfoSavePatientButton))
            if object.exists(patientCardEditPatientSavePopUpMessage):
                saveWarningMessage = str(waitForObject(patientCardEditPatientSavePopUpMessage).errorMessage)
                textMessage = "Please entered all required fields"
                if saveWarningMessage == textMessage:
                    mouseClick(waitForObject(livePatientDialogErrorOkButton))
                else:
                    test.log("Save Warning message %s and text message %s are not same" %(saveWarningMessage,textMessage))
            elif object.exists(patientCardDialogErrorOkButton):
                samePatientIDPopUpHandlerPatientCard()
                counter = counter + 1
                status = True
            else:
                if object.exists(patientCardInfoEditPatientButton):
                    test.log("error pop up message is not present")
                    status = True
                else:
                    status = False
        else:
            test.log("Error message pop up is not there")
        if object.exists(patientCardInfoEditPatientButton) :
            status = True          
        return status       
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to cancel the changes after editing the patient's record in patient list screen
def cancelForEditingPatientInPatientCardScreen(userInput):
    try:
        status = False
        value = userInput.strip()
        upper = value.upper()
        if object.exists(patientCardInfoCancelPatientButton):
            mouseClick(findObject(patientCardInfoCancelPatientButton))
            if object.exists(patientCardAddPatientCancelPopUpMessage):            
                cancelWarningMessage = str(waitForObject(patientCardAddPatientCancelPopUpMessage).text)
                #textMessage = "Do you want to discard the changes?"
                if "discard" in cancelWarningMessage:
                    if upper == "CONFIRM":
                        mouseClick(waitForObject(patientCardAddPatientPopUpConfirmButton))
                        snooze(1)
                        if object.exists(patientCardAddPatientSurnameInput):
                            test.log("Successfully navigate to Edit patient screen")
                            status = True
                        else:
                            test.log("Failed to navigate to Edit patient screen")
                            status = False  
                    elif upper == "DISCARD":
                        mouseClick(waitForObject(patientCradEditPatientPopUpCancelButton))
                        snooze(1)
                        if object.exists(patientCardAddPatientSurnameInput):
                            test.log("Successfully navigate to Edit patient screen")
                            status = True
                        else:
                            test.log("Failed to navigate to Edit patient screen")
                            status = False   
                else:
                    test.log("Discard substring is not present in cancel warning message : %s" % cancelWarningMessage)
            else:
                test.log("Could not find cancel pop up message in edit patient screen")
        return status              
    except Exception as e:
        test.fail("Exception" + str(e)) 
        
# Function to delete patient details after editing the patient details in add patient card screen
def deleteEdittedPatientInformationInPatientCard(userinput):
    try:
        status = False
        value = userinput.strip()
        upper = value.upper()
        if object.exists(patientCardEditScreenDeletePatientButton):
            mouseClick(waitForObject(patientCardEditScreenDeletePatientButton))
            if object.exists(patientCardEditDeletePopUpMessage):
                deleteWarningMessage = str(waitForObject(patientCardEditDeletePopUpMessage).warning)
                if "Delete" in deleteWarningMessage:
                    if upper == "CONFIRM":
                        mouseClick(waitForObject(patientCardEditDeletePopUpConfirmButton))
                        snooze(1)
                        if object.exists(patientCardAddButton):
                            test.log("Successfully navigated to patient card screen from add patient screen")
                            status = True
                        else:
                            test.fail("Patient card screen is not displayed")
                            status = False
                    elif upper == "DISCARD":
                        mouseClick(waitForObject(patientCardEditDeletePopUpCancelButton))
                        snooze(1)
                        if object.exists(patientCardAddPatientSurnameInput):
                            test.log("Successfully navigate to Edit patient screen")
                            status = True
                        else:
                            test.log("Failed to navigate to Edit patient screen")
                            status = False                       
                        
                else:
                    test.log("Delete substring is not present in delete Warning message :%s"%deleteWarningMessage)
            else:
                test.log("Failed to find patient card delete pop up message ")
        return status       
            
    except Exception as e:
        test.fail("Exception" + str(e))
            
        
# Function to save the patient details after editing the patient details in add patient card screen
def saveForEditingThePatientInPatientCardScreen(Surname="", Firstname="", Title="", PatientAge="", PatientId="", HospitalId="", Weight="", Height=""):
    try:
        snooze(2)
        if object.exists(patientCardInfoSavePatientButton):
            mouseClick(waitForObject(patientCardInfoSavePatientButton))
            snooze(2)
            mouseClick(waitForObject(patientCardAddPatientBackButton))
            searchBox = (waitForObject(patientCardSearchInput))
            searchBox.text = ""
            type(waitForObject(patientCardSearchInput), PatientId)
            snooze(2)
            patientListView = waitForObject(patientCardPatientListView)
            item = object.children(patientListView)
            row = object.children(item[0])
                
            for i in row:
                outline = object.children(i)
                if len(outline) > 0:
                    label = object.children(outline[0])
                    value = label[1].text
                
                    if (value == PatientId):
                        test.log("The given pid is matching with the patient's pid in the list")
                        if object.exists(patientCardInfoButton):
                            mouseClick(waitForObject(patientCardInfoButton))
                            snooze(3)
                            if object.exists(patientCardInfoEditPatientButton):
                                mouseClick(waitForObject(patientCardInfoEditPatientButton))
                                snooze(2)
                                if Surname:
                                    if object.exists(patientCardAddPatientSurnameInput):
                                        surnameInput = (waitForObject(patientCardAddPatientSurnameInput))
                                         
                                        if surnameInput.text == Surname :
                                            test.passes("Successfully edited and saved the surname in the  patient card screen")
                                        
                                        else:
                                            test.fail("Surname is not edited and it is not saved in the  patient card screen")
                                                   
                                if Firstname:
                                    if object.exists(patientCardAddPatientFirstNameInput):
                                        firstNameInput = (waitForObject(patientCardAddPatientFirstNameInput))
                                        
                                        if firstNameInput.text == Firstname :
                                            test.passes("Successfully edited and saved the firstname in the  patient card screen")
                                        
                                        else:
                                            test.fail("Firstname is not edited and it is not saved in the  patient card screen")                    
                                
                                if Title:
                                    if object.exists(patientCardAddPatientTitleInput):
                                        TitleInput = (waitForObject(patientCardAddPatientTitleInput))
                                        
                                        if TitleInput.text == Title :
                                            test.passes("Successfully edited and saved the title in the  patient card screen")
                                        
                                        else:
                                            test.fail("Title is not edited and it is not saved in the  patient card screen")
                                 
                                if PatientAge:
                                    if object.exists(patientCardAddPatientAgeInput):
                                        AgeInput = (waitForObject(patientCardAddPatientAgeInput))
                                       
                                        if AgeInput.text == PatientAge :
                                            test.passes("Successfully edited and saved the title in the  patient card screen")
                                        
                                        else:
                                            test.fail("Patient's age is not edited and it is not saved in the  patient card screen")
                                                    
                                if PatientId:
                                    if object.exists(patientCardAddPatientIdInput):
                                        PatientIdInput = (waitForObject(patientCardAddPatientIdInput))
                                        
                                        if PatientIdInput.text == PatientId :
                                            test.passes("Successfully edited and saved the patient's id in the patient card screen")
                                        
                                        else:
                                            test.fail("Patient's id is not edited and it is not saved in the patient card screen")
                                            
                                if HospitalId:
                                    if object.exists(patientCardAddPatientHospitalIdInput):
                                        HospitalIdInput = (waitForObject(patientCardAddPatientHospitalIdInput))
                                        
                                        if HospitalIdInput.text == HospitalId :
                                            test.passes("Successfully edited and saved the hospital id in the patient card screen")
                                        
                                        else:
                                            test.fail("Hospital id is not edited and it is not saved in the patient card screen")
                                                        
                                if Weight:
                                    if object.exists(patientCardAddPatientWeightInput):
                                        WeightInput = (waitForObject(patientCardAddPatientWeightInput))
                                        
                                        if WeightInput.text == Weight :
                                            test.passes("Successfully edited and saved the patient's weight in the  patient card screen")
                                        
                                        else:
                                            test.fail("Patient's weight is not edited and it is not saved in the  patient card screen")
                                            
                                if Height:
                                    if object.exists(patientCardAddPatientHeightInput):
                                        HeightInput = (waitForObject(patientCardAddPatientHeightInput))
                                       
                                        if HeightInput.text == Height :
                                            test.passes("Successfully edited and saved the patient's height in the  patient card screen")
                                        
                                        else:
                                            test.fail("Patient's height is not edited and it is not saved in the  patient card screen")
                                                                      
                    else:
                        test.fail("Patient record is not saved")                        
                                
    except Exception as e:
        test.fail("Exception" + str(e))
        
#Function to get the values of patient details in patient card screen
def gettingTheDetailsOfPatientsInPatientCardEditScreen():
    try:
        patientInformationA = []
        snooze(2)
        if object.exists(patientCardInfoEditPatientButton):
            #mouseClick(waitForObject(patientCardInfoEditPatientButton))
            #snooze(2)
            
            if object.exists(patientCardAddPatientSurnameInput):
                global surnameInput
                surnameInput =str(waitForObject(patientCardAddPatientSurnameInput).text)
                patientInformationA.append(str(surnameInput))
                
            if object.exists(patientCardAddPatientFirstNameInput):
                global firstNameInput
                firstNameInput = str(waitForObject(patientCardAddPatientFirstNameInput).text)
                patientInformationA.append(str(firstNameInput))                
                
            if object.exists(patientCardAddPatientTitleInput):
                global TitleInput
                TitleInput = (waitForObject(patientCardAddPatientTitleInput).text)
                patientInformationA.append(str(TitleInput)) 
                
            if object.exists(patientCardAddPatientAgeInput):
                global AgeInput
                AgeInput = (waitForObject(patientCardAddPatientAgeInput).text)
                patientInformationA.append(str(AgeInput))
                
            if object.exists(patientCardAddPatientIdInput):
                global PatientIdInput
                PatientIdInput = (waitForObject(patientCardAddPatientIdInput).text)
                patientInformationA.append(str(PatientIdInput))
                
            if object.exists(patientCardAddPatientHospitalIdInput):
                global HospitalIdInput
                HospitalIdInput = (waitForObject(patientCardAddPatientHospitalIdInput).text)
                patientInformationA.append(str(HospitalIdInput))
                
            if object.exists(patientCardAddPatientWeightInput):
                global WeightInput
                WeightInput = (waitForObject(patientCardAddPatientWeightInput).text)
                patientInformationA.append(str(WeightInput))
                
            if object.exists(patientCardAddPatientHeightInput):
                global HeightInput
                HeightInput = (waitForObject(patientCardAddPatientHeightInput).text)
                patientInformationA.append(str(HeightInput))                
        # mouseClick(waitForObject(patientCardAddPatientBackButton))            
        return patientInformationA    
    
    except Exception as e:
        test.fail("Exception" + str(e))
        
#Function to cancel the changes after editing the patient's record in patient card screen
def cancelForEditingThePatientInPatientCardScreen(Surname="", Firstname="", Title="", PatientAge="", PatientId="", HospitalId="", Weight="", Height=""):
    try:
        if object.exists(patientCardInfoCancelPatientButton):
            mouseClick(findObject(patientCardInfoCancelPatientButton))
            snooze(1)
            # mouseClick(waitForObject(patientCardInfoEditPatientButton))
            cancelWarningMessage = str(waitForObject(patientCardAddPatientCancelPopUpMessage).text)
            textMessage = "Do you want to discard the changes?"
            if cancelWarningMessage == textMessage:
                mouseClick(waitForObject(patientCardAddPatientPopUpConfirmButton))
            else:
                test.log("Warning message in pop up : "+cancelWarningMessage)
                mouseClick(waitForObject(patientCardDeletePatientNoButton))
            mouseClick(waitForObject(patientCardAddPatientBackButton))
            snooze(0.5)
            searchBox = (waitForObject(patientCardSearchInput))
            searchBox.text = ""
            type(waitForObject(patientCardSearchInput), PatientId)
            patientListView = waitForObject(patientCardPatientListView)
            item = object.children(patientListView)
            row = object.children(item[0])
                
            for i in row:
                outline = object.children(i)
                if len(outline) > 0:
                    label = object.children(outline[0])
                    value = label[1].text
                
                    if (value == PatientId):
                        test.log("The given pid is matching with the patient's pid in the list")
                        if object.exists(patientCardInfoButton):
                            mouseClick(waitForObject(patientCardInfoButton))
                            snooze(3)
                            if object.exists(patientCardInfoEditPatientButton):
                                mouseClick(waitForObject(patientCardInfoEditPatientButton))
                                snooze(2)
                                if object.exists(patientCardAddPatientSurnameInput):
                                    newSurnameInput =str(waitForObject(patientCardAddPatientSurnameInput).text)
                                    test.log("newSurnameInput=%s" %newSurnameInput)
                                    
                                if object.exists(patientCardAddPatientFirstNameInput):
                                    newFirstNameInput = str(waitForObject(patientCardAddPatientFirstNameInput).text)
                                    test.log("newFirstNameInput=%s" %newFirstNameInput)
                                    
                                if object.exists(patientCardAddPatientTitleInput):
                                    newTitleInput = (waitForObject(patientCardAddPatientTitleInput).text)
                                    test.log("newTitleInput=%s" %newTitleInput)
                                    
                                if object.exists(patientCardAddPatientAgeInput):
                                    newAgeInput = (waitForObject(patientCardAddPatientAgeInput).text)
                                    test.log("newAgeInput=%s" %newAgeInput)
                                    
                                if object.exists(patientCardAddPatientIdInput):
                                    newPatientIdInput = (waitForObject(patientCardAddPatientIdInput).text)
                                    test.log("newPatientIdInput=%s" %newPatientIdInput)
                                    
                                if object.exists(patientCardAddPatientHospitalIdInput):
                                    newHospitalIdInput = (waitForObject(patientCardAddPatientHospitalIdInput).text)
                                    test.log("newHospitalIdInput=%s" %newHospitalIdInput)
                                    
                                if object.exists(patientCardAddPatientWeightInput):
                                    newWeightInput = (waitForObject(patientCardAddPatientWeightInput).text)
                                    test.log("newWeightInput=%s" %newWeightInput)
                                    
                                if object.exists(patientCardAddPatientHeightInput):
                                    newHeightInput = (waitForObject(patientCardAddPatientHeightInput).text)
                                    test.log("newHeightInput=%s" %newHeightInput)
                                    
                                if Surname ==newSurnameInput and Firstname==newFirstNameInput and Title==newTitleInput and PatientAge==newAgeInput and PatientId==newPatientIdInput and HospitalId==newHospitalIdInput and Weight==newWeightInput and Height==newHeightInput:
                                    test.passes("Successfully cancelled the values after editing the patient details in patient card screen")
                                else:
                                    test.fail("Values are not cancelled after editing the patient details in patient card screen")
    
    except Exception as e:
        test.fail("Exception :" + str(e))
        
      

        
#Function to get the values of patient details in patient list screen
def gettingTheDetailsOfPatientsInPatientListScreen():
    try:
        if object.exists(liveScreenAddPatientSurnameInput):
            global surnameInput
            surnameInput =str(waitForObject(liveScreenAddPatientSurnameInput).text)
            test.log("surnameInput=%s" %surnameInput)
            
        if object.exists(liveScreenAddPatientFirstNameInput):
            global firstNameInput
            firstNameInput = str(waitForObject(liveScreenAddPatientFirstNameInput).text)
            test.log("firstNameInput=%s" %firstNameInput)
            
        if object.exists(liveScreenAddPatientTitleInput):
            global TitleInput
            TitleInput = (waitForObject(liveScreenAddPatientTitleInput).text)
            test.log("TitleInput=%s" %TitleInput)
            
        if object.exists(liveScreenAddPatientAgeInput):
            global AgeInput
            AgeInput = (waitForObject(liveScreenAddPatientAgeInput).text)
            test.log("AgeInput=%s" %AgeInput)
            
        if object.exists(liveScreenAddPatientIdInput):
            global PatientIdInput
            PatientIdInput = (waitForObject(liveScreenAddPatientIdInput).text)
            test.log("PatientIdInput=%s" %PatientIdInput)
            
        if object.exists(liveScreenAddPatientHospitalIdInput):
            global HospitalIdInput
            HospitalIdInput = (waitForObject(liveScreenAddPatientHospitalIdInput).text)
            test.log("HospitalIdInput=%s" %HospitalIdInput)
            
        if object.exists(liveScreenAddPatientWeightInput):
            global WeightInput
            WeightInput = (waitForObject(liveScreenAddPatientWeightInput).text)
            test.log("WeightInput=%s" %WeightInput)
            
        if object.exists(liveScreenAddPatientHeightInput):
            global HeightInput
            HeightInput = (waitForObject(liveScreenAddPatientHeightInput).text)
            test.log("HeightInput=%s" %HeightInput)
            
        return surnameInput,firstNameInput,TitleInput,AgeInput,PatientIdInput,HospitalIdInput,WeightInput,HeightInput
    
    
    except Exception as e:
        test.fail("Exception" + str(e))
                            
        
# Function to edit and save the patient details in patient card screen
def editAndSaveThePatientDetailsInPatientCardScreen(Surname="", Firstname="", Title="", PatientDOB="", PatientAge="", PatientId="", HospitalId="", Weight="", Height="", Gender="", PaceMaker="", Digoxin=""):
    try:
        snooze(2)
        if object.exists(patientCardInfoEditPatientButton):
            snooze(2)
            mouseClick(waitForObject(patientCardInfoEditPatientButton))
            snooze(2)
            
            if Surname:
                if object.exists(patientCardAddPatientSurnameInput):
                    surnameInput = (waitForObject(patientCardAddPatientSurnameInput))
                    surnameInput.text = ""
                    type(waitForObject(patientCardAddPatientSurnameInput), Surname)
                    snooze(1)
                    changedSurname = waitForObject(patientCardAddPatientSurnameInput)
                    
                    if changedSurname.text == Surname :
                        test.passes("Successfully changed the surname")
                    
                    else:
                        test.fail("Surname is not changed")
                               
            if Firstname:
                if object.exists(patientCardAddPatientFirstNameInput):
                    firstNameInput = (waitForObject(patientCardAddPatientFirstNameInput))
                    firstNameInput.text = ""
                    type(waitForObject(patientCardAddPatientFirstNameInput), Firstname)
                    snooze(1)
                    changedFirstname = waitForObject(patientCardAddPatientFirstNameInput)
                    
                    if changedFirstname.text == Firstname :
                        test.passes("Successfully changed the firstname")
                    
                    else:
                        test.fail("Firstname is not changed")                    
            
            if Title:
                if object.exists(patientCardAddPatientTitleInput):
                    TitleInput = (waitForObject(patientCardAddPatientTitleInput))
                    TitleInput.text = ""
                    type(waitForObject(patientCardAddPatientTitleInput), Title)
                    snooze(1)
                    changedTitle = waitForObject(patientCardAddPatientTitleInput)
                    
                    if changedTitle.text == Title :
                        test.passes("Successfully changed the title")
                    
                    else:
                        test.fail("Title is not changed")
                                    
            '''if PatientDOB:
                if object.exists(patientCardAddPatientDOBInput):
                    DOBInput =(waitForObject(patientCardAddPatientDOBInput))
                    snooze(1)
                    DOBInput.text=""
                    dateOfBirth = findObject(patientCardAddPatientDOBInput)
                    parent=object.parent(dateOfBirth)
                    mouseClick(parent)
                    type(waitForObject(patientCardAddPatientDOBInput),PatientDOB)
                    snooze(1)
                    test.passes("Successfully changed the patient's date of birth")
                    
                    return True'''
            
            if PatientAge:
                if object.exists(patientCardAddPatientAgeInput):
                    AgeInput = (waitForObject(patientCardAddPatientAgeInput))
                    AgeInput.text = ""
                    type(waitForObject(patientCardAddPatientAgeInput), PatientAge)
                    snooze(1)
                    changedPatientAge = waitForObject(patientCardAddPatientAgeInput)
                    
                    if changedPatientAge.text == PatientAge :
                        test.passes("Successfully changed the patient's age")
                    
                    else:
                        test.fail("Patient's age is not changed")
                                
            if PatientId:
                if object.exists(patientCardAddPatientIdInput):
                    PatientIdInput = (waitForObject(patientCardAddPatientIdInput))
                    PatientIdInput.text = ""
                    type(waitForObject(patientCardAddPatientIdInput), PatientId)
                    snooze(1)
                    changedPatientId = waitForObject(patientCardAddPatientIdInput)
                    
                    if changedPatientId.text == PatientId :
                        test.passes("Successfully changed the patient's id")
                    
                    else:
                        test.fail("Patient's id is not changed")
                        
            if HospitalId:
                if object.exists(patientCardAddPatientHospitalIdInput):
                    HospitalIdInput = (waitForObject(patientCardAddPatientHospitalIdInput))
                    HospitalIdInput.text = ""
                    type(waitForObject(patientCardAddPatientHospitalIdInput), HospitalId)
                    snooze(1)
                    changedHospitalId = waitForObject(patientCardAddPatientHospitalIdInput)
                    
                    if changedHospitalId.text == HospitalId :
                        test.passes("Successfully changed the hospital id")
                    
                    else:
                        test.fail("Hospital id is not changed")
                                    
            if Gender:
                value = Gender.strip()
                upper = value.upper()
                
                if upper == "MALE":
                    mouseClick(waitForObject(patientCardAddPatientMaleRadioButton))
                    test.passes("Successfully changed the gender to male")
                
                elif upper == "FEMALE":
                    mouseClick(waitForObject(patientCardAddPatientFemaleRadioButton))
                    test.passes("Successfully changed the gender to female")
                
                elif upper == "OTHER":
                    mouseClick(waitForObject(patientCardAddPatientOthersRadioButton))
                    test.passes("Successfully changed the gender to other")
                    
                else:
                    test.fail("Gender is not changed")
                                   
            if Weight:
                if object.exists(patientCardAddPatientWeightInput):
                    WeightInput = (waitForObject(patientCardAddPatientWeightInput))
                    WeightInput.text = ""
                    type(waitForObject(patientCardAddPatientWeightInput), Weight)
                    snooze(1)
                    changedWeight = waitForObject(patientCardAddPatientWeightInput)
                    
                    if changedWeight.text == Weight :
                        test.passes("Successfully changed the patient's weight")
                    
                    else:
                        test.fail("Patient's weight is not changed")
                        
            if Height:
                if object.exists(patientCardAddPatientHeightInput):
                    HeightInput = (waitForObject(patientCardAddPatientHeightInput))
                    HeightInput.text = ""
                    type(waitForObject(patientCardAddPatientHeightInput), Height)
                    snooze(1)
                    changedHeight = waitForObject(patientCardAddPatientHeightInput)
                    
                    if changedHeight.text == Height :
                        test.passes("Successfully changed the patient's height")
                    
                    else:
                        test.fail("Patient's height is not changed")
                            
            if PaceMaker:
                value = PaceMaker.strip()
                upper = value.upper()
                
                if upper == "YES":
                    mouseClick(waitForObject(patientCardAddPatientPaceMakeYesButton))
                    test.passes("Successfully changed the pacemaker to yes")
                
                elif upper == "NO":
                    mouseClick(waitForObject(patientCardAddPatientPaceMakeNoButton))
                    test.passes("Successfully changed the pacemaker to no")
                
                else:
                    test.fail("Pacemaker is not changed")
                                
            if Digoxin:
                value = Digoxin.strip()
                upper = value.upper()
                
                if upper == "YES":
                    mouseClick(waitForObject(patientCardAddPatientDigoxinYesButton))
                    test.passes("Successfully changed the Digoxin to yes")
                
                elif upper == "NO":
                    mouseClick(waitForObject(patientCardAddPatientDigoxinNoButton))
                    test.passes("Successfully changed the Digoxin to no")
                
                else:
                    test.fail("Digoxin is not changed")
                    
            if object.exists(patientCardAddPatientSaveButton):
                mouseClick(waitForObject(patientCardAddPatientSaveButton))
                
                mouseClick(waitForObject(patientCardInfoEditPatientButton))
                snooze(1)
                if Surname:
                    if object.exists(patientCardAddPatientSurnameInput):
                        surnameInput = (waitForObject(patientCardAddPatientSurnameInput))
                         
                        if surnameInput.text == Surname :
                            test.passes("Successfully edited and saved the surname in the  patient card screen")
                        
                        else:
                            test.fail("Surname is not edited and it is not saved in the  patient card screen")
                                   
                if Firstname:
                    if object.exists(patientCardAddPatientFirstNameInput):
                        firstNameInput = (waitForObject(patientCardAddPatientFirstNameInput))
                        
                        if firstNameInput.text == Firstname :
                            test.passes("Successfully edited and saved the firstname in the  patient card screen")
                        
                        else:
                            test.fail("Firstname is not edited and it is not saved in the  patient card screen")                    
                
                if Title:
                    if object.exists(patientCardAddPatientTitleInput):
                        TitleInput = (waitForObject(patientCardAddPatientTitleInput))
                        
                        if TitleInput.text == Title :
                            test.passes("Successfully edited and saved the title in the  patient card screen")
                        
                        else:
                            test.fail("Title is not edited and it is not saved in the  patient card screen")
                 
                if PatientAge:
                    if object.exists(patientCardAddPatientAgeInput):
                        AgeInput = (waitForObject(patientCardAddPatientAgeInput))
                       
                        if AgeInput.text == PatientAge :
                            test.passes("Successfully edited and saved the title in the  patient card screen")
                        
                        else:
                            test.fail("Patient's age is not edited and it is not saved in the  patient card screen")
                                    
                if PatientId:
                    if object.exists(patientCardAddPatientIdInput):
                        PatientIdInput = (waitForObject(patientCardAddPatientIdInput))
                        
                        if PatientIdInput.text == PatientId :
                            test.passes("Successfully edited and saved the patient's id in the patient card screen")
                        
                        else:
                            test.fail("Patient's id is not edited and it is not saved in the patient card screen")
                            
                if HospitalId:
                    if object.exists(patientCardAddPatientHospitalIdInput):
                        HospitalIdInput = (waitForObject(patientCardAddPatientHospitalIdInput))
                        
                        if HospitalIdInput.text == HospitalId :
                            test.passes("Successfully edited and saved the hospital id in the patient card screen")
                        
                        else:
                            test.fail("Hospital id is not edited and it is not saved in the patient card screen")
                                        
                if Weight:
                    if object.exists(patientCardAddPatientWeightInput):
                        WeightInput = (waitForObject(patientCardAddPatientWeightInput))
                        
                        if WeightInput.text == Weight :
                            test.passes("Successfully edited and saved the patient's weight in the  patient card screen")
                        
                        else:
                            test.fail("Patient's weight is not edited and it is not saved in the  patient card screen")
                            
                if Height:
                    if object.exists(patientCardAddPatientHeightInput):
                        HeightInput = (waitForObject(patientCardAddPatientHeightInput))
                       
                        if HeightInput.text == Height :
                            test.passes("Successfully edited and saved the patient's height in the  patient card screen")
                        
                        else:
                            test.fail("Patient's height is not edited and it is not saved in the  patient card screen")
        return True
    
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to Search  and select the patient details in patient card screen
def searchAndSelectPatientInPatientCardScreen(pid="", name=""):
    try:
        if object.exists(patientCardSearchInput):
            searchBox = (waitForObject(patientCardSearchInput))
            snooze(1)
            searchBox.text = ""
            type(waitForObject(patientCardSearchInput), pid)
            snooze(2)
            patientListView = waitForObject(patientCardPatientListView)
            item = object.children(patientListView)
            row = object.children(item[0])
            for i in row:
                outline = object.children(i)
                if len(outline) > 0:
                    label = object.children(outline[0])
                    value = label[1].text                    
                    if (value == pid):
                        test.log("The given pid is matching with the patient's pid in the list")
                        mouseClick(waitForObject(label[1]))
                        snooze(1)                            
                        if outline[0].highlighted :
                            test.log("Successfully searched and selected the given patient in patient card screen")
                            return True
                        else:
                            test.fail("Given patient's record is not selected")
                            return False
                    position = 1
                    if (value == pid):
                        test.log("position = %d" % position)
                    else:
                        position += 1
                            
        else:
            test.fail("Patient's record with patient id "+pid+" is not found")                                
        
        
        '''if name:
            if object.exists(patientCardSearchInput):
                searchBox =(waitForObject(patientCardSearchInput))
                snooze(1)
                searchBox.text=""
                type(waitForObject(patientCardSearchInput),name)
                snooze(2)
                parent = waitForObject(patientCardPatientListView)
                child = object.children(parent)
                child_1 = object.children(child[0])
                
                for i in child_1:
                    child_2 = object.children(i)
                    if len(child_2)>0:
                        child_3 = object.children(child_2[0])
                        value = child_3[1].text
                        test.log("value=%s" %value)
                
                firstName = "harry"
                lastName = "potter"
                concat =  firstName+","+" "+lastName

                
                position = 1
                if (value == concat):
                    test.log("position = %d" %position)
                else:
                    position+=1
                test.log("position = %d" %position)
                
                if (value == concat):
                    test.log("The given pid is matching with the patient's pid in the list")
                    mouseClick(waitForObject(label[0]))
                    test.log("Successfully selected the given patient's record")
                else:
                    test.fail("Given patient's record is not selected")
                test.passes("Successfully searched and selected the given patient in patient card screen")
                
            return True'''

    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to delete single patient in patient card screen 
def deletePatientInPatientCard(userinput,patientRecord):
    try:
        status = False
        value = userinput.strip()
        upper = value.upper()
        numberOfPatient = str(patientRecord)
        #if str(count) > numberOfPatient:
#             numberOfPatient = str(count)            
        if object.exists(patientCardOtherOptionsPatientButton):  
                mouseClick(waitForObject(patientCardOtherOptionsPatientButton))
                mouseClick(waitForObject(patientCardDeletePatientButton))
                cancelWarningMessage = str(findObject(patientCardDeletePatientCancelPopUpMessage).text)
                #textMessage = "Delete 1"                
                if "Delete" in cancelWarningMessage:
                    if upper == "CONFIRM":
                        mouseClick(waitForObject(patientCardDeletePatientYesButton))
                        snooze(1)
                        if object.exists(patientCardAddButton):
                            test.log("Successfully navigated to patient card screen from add patient screen")
                            status = True
                        else:
                            test.fail("Patient card screen is not displayed")
                            status = False
                    elif upper == "DISCARD":
                        mouseClick(waitForObject(patientCardDeletePatientNoButton))
                        snooze(1)
                        if object.exists(patientCardAddButton):
                            test.log("Successfully navigate to Edit patient screen")
                            status = True
                        else:
                            test.log("Failed to navigate to Edit patient screen")
                            status = False
                    else:
                        test.log("User input is wrong %s"%userinput)
                else:
                    test.log("Cancel warning message : it is not same as text message : %s"%(cancelWarningMessage))
        elif object.exists(patientCardDeletePatientButton):
                mouseClick(waitForObject(patientCardDeletePatientButton))
                cancelWarningMessage = str(findObject(patientCardDeletePatientCancelPopUpMessage).text)
                #textMessage = "Delete 1"                
                if "Delete" in cancelWarningMessage:
                    if upper == "CONFIRM":
                        mouseClick(waitForObject(patientCardDeletePatientYesButton))
                        snooze(1)
                        if object.exists(patientCardAddButton):
                            test.log("Successfully navigated to patient card screen from add patient screen")
                            status = True
                        else:
                            test.fail("Patient card screen is not displayed")
                            status = False
                    elif upper == "DISCARD":
                        mouseClick(waitForObject(patientCardDeletePatientNoButton))
                        snooze(1)
                        if object.exists(patientCardAddButton):
                            test.log("Successfully navigate to Edit patient screen")
                            status = True
                        else:
                            test.log("Failed to navigate to Edit patient screen")
                            status = False
                    else:
                        test.log("User input is wrong %s"%userinput)
                else:
                    test.log("Cancel warning message : it is not same as text message : %s"%(cancelWarningMessage))
        else:
            test.log("Could not able to delete any record") 
        return status                
                    
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to delete single patient in patient card screen
def deleteOnePatientInPatientCard(pid="", name=""):
    try:
        if pid:
            if object.exists(patientCardOtherOptionsPatientButton):  
                mouseClick(waitForObject(patientCardOtherOptionsPatientButton))
                mouseClick(waitForObject(patientCardDeletePatientButton))
                cancelWarningMessage = str(findObject(patientCardDeletePatientCancelPopUpMessage).text)
                textMessage = "Delete 1 patient?"
                
                if cancelWarningMessage == textMessage:
                    mouseClick(waitForObject(patientCardDeletePatientYesButton))
                    snooze(2)
                    
                    if object.exists(patientCardSearchInput):
                        searchBox = (waitForObject(patientCardSearchInput))
                        searchBox.text = ""
                        type(waitForObject(patientCardSearchInput), pid)
                        
                        if object.exists(patientCardPatientListView):
                            if object.exists(patientRecord):
                                patientListView = waitForObject(patientCardPatientListView)
                                item = object.children(patientListView)
                                row = object.children(item[0])
                                
                                for i in row:
                                    outline = object.children(i)
                                    if len(outline) > 0:
                                        label = object.children(outline[0])
                                        value = label[1].text
                                    
                                        if (value == pid):
                                            test.fail("Patient's record with patient id "+pid+" is not deleted")
                                            return False
                                        else:
                                            test.passes("Successfully deleted the "+ pid +" patient's record")
                                            return True
                            else:
                                test.passes("Successfully deleted the "+ pid +" patient's record")               
                else:
                    test.log("Warning message in pop up : "+cancelWarningMessage)
                    mouseClick(waitForObject(patientCardDeletePatientNoButton))
                    test.log("Patient's record with patient id "+pid+" is not deleted")
            else:
                test.log("Patient's record with patient id "+pid+" is not found")
                        
        if name:
            if object.exists(patientCardOtherOptionsPatientButton):  
                mouseClick(waitForObject(patientCardOtherOptionsPatientButton))
                mouseClick(waitForObject(patientCardDeletePatientButton))
                cancelWarningMessage = str(waitForObject(patientCardDeletePatientCancelPopUpMessage).text)
                textMessage = "Delete 1 patient?"
                if cancelWarningMessage == textMessage:
                    mouseClick(waitForObject(patientCardDeletePatientYesButton))
                    snooze(2)
                    if object.exists(patientCardSearchInput):
                        searchBox = (waitForObject(patientCardSearchInput))
                        snooze(1)
                        searchBox.text = ""
                        type(waitForObject(patientCardSearchInput), name)
                        snooze(2)
                        if object.exists(patientRecord):
                            test.log("Patient's record with patient name "+name+" is not deleted")
                            return False
                        else:
                            test.log("Successfully deleted the "+ name +"'s record")
                            return True
                else:
                    test.log("Warning message in pop up : "+cancelWarningMessage)
                    mouseClick(waitForObject(patientCardDeletePatientNoButton))
                    test.log("Patient's record with patient name "+name+" is not deleted")
            else:
                test.log("Patient's record with patient name "+name+" is not found")       
                    
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to delete multiple patients in patient card screen
def deleteMultiplePatientsInPatientCard(noOfRecordsToBeDeleted):
    try:
        parentListView = waitForObject(patientCardPatientListView)
        item = object.children(parentListView)   
        row = object.children(item[0])   
        recordsBeforeDeleting = parentListView.count
        test.log("Records before deleting = %d" %recordsBeforeDeleting)
        if recordsBeforeDeleting >= noOfRecordsToBeDeleted:
            number = 0
            for i in row:
                outline = object.children(i)
                if len(outline) > 0:
                    label = object.children(outline[0])
                    if number < noOfRecordsToBeDeleted:
                        mouseClick(waitForObject(label[1]))
                        if outline[0].highlighted :
                            number += 1
                        else:
                            test.fail("Given patient's record is not selected")
            
            test.log("Successfully selected the %d patient's record in patient card screen" %number)
            mouseClick(waitForObject(patientCardOtherOptionsPatientButton))
            mouseClick(waitForObject(patientCardDeletePatientButton))
            snooze(1)
            cancelWarningMessage = str(findObject(patientCardDeletePatientCancelPopUpMessage).text)
            textMessage = ("Delete %d patients?" %number)
            
            if cancelWarningMessage == textMessage:
                mouseClick(waitForObject(patientCardDeletePatientYesButton))
                snooze(1)
                newParent = waitForObject(patientCardPatientListView)
                recordsAfterDeleting = newParent.count
                test.log("Records after deleting= %d" %recordsAfterDeleting)
                records = recordsBeforeDeleting - noOfRecordsToBeDeleted
                
                if records == recordsAfterDeleting:
                    test.passes("Successfully deleted the first %d patient records" %noOfRecordsToBeDeleted)
                else:
                    test.fail("The first %d patient record's are not deleted instead deleted the first %d records" %noOfRecordsToBeDeleted %number)
            else:
                test.log("Warning message in pop up : "+cancelWarningMessage)
                mouseClick(waitForObject(patientCardDeletePatientNoButton))
                test.fail("Patient's record is not deleted")
           
        else:
            test.fail("The number of records to be deleted is %d but only %d are existing" %noOfRecordsToBeDeleted %recordsBeforeDeleting)    
        
        return True
    
    except Exception as e:
        test.fail("Exception : " + str(e))
    
# Function to count the number of patients in patient card screen
def numberOfPatientsInPatientCardScreen():
    try:
        if object.exists(patientCardPatientListView):
            parentListView = waitForObject(patientCardPatientListView)
            totalRecords = parentListView.count
            test.log("Total number of patients record in patient card screen is %d" % totalRecords)
            
        return True
    
    except Exception as e:
        test.fail("Exception" + str(e))
        
#Function to count the number of examinations       
def getExaminationCount():
    try:
        if object.exists(examinationListView):
            examCount = waitForObject(examinationListView)
            count = examCount.count            
        else:
            test.log("Could not find examination List View")
            
        return count 
    
    except Exception as e:
        test.fail("Exception"+str(e))
        
#Function to get exam time of examination record
def getExamTimeExaminationRecord():
    try:
        if object.exists(examinationListView):
            examListView = waitForObject(examinationListView)
            childItem=object.children(examListView)
            childItems=object.children(childItem[0])    
        for child in childItems:        
            childrens=object.children(child)            
            if len(childrens)>0:
                examButton=object.children(childrens[0])
                row=object.children(examButton[1])
                dateValue=row[3].text
        return dateValue
    except Exception as e:
        test.fail("Exception"+str(e))
        
#Function to load preview screen for selected examination
def loadPreviewScreenFromPatientCardScreen(examTime=""):
    try:
        status = False      
        if object.exists(examinationListView):
            examListView = waitForObject(examinationListView)
            childItem=object.children(examListView)
            childItems=object.children(childItem[0])    
        for child in childItems:        
            childrens=object.children(child)            
            if len(childrens)>0:
                examButton=object.children(childrens[0])
                row=object.children(examButton[1])
                dateValue=row[3].text                
                if(dateValue==examTime):
                    snooze(2)
                    mouseClick(waitForObject(child))
                    if childrens[0].highlighted:
                        test.log("Successfully selected the examination record")
                    else:
                        test.log("Examination record is not selected") 
                        snooze(2)
        if object.exists(patientCardInfoLoadExamButton):
            mouseClick(waitForObject(patientCardInfoLoadExamButton))
            snooze(1)
            if object.exists(evaluationScreenSaveRecordButton):
                test.log("Successfully Navigate to preview screen")
                status = True
            else:
                test.log("Failed to load preview screen")
                status = False
        else:
            test.log("Failed to click patient card info load button")
        return status 
    except Exception as e:
        test.fail("Exception"+str(e))  
      
        
#Function to delete one examination record          
def deleteOneExaminationRecord(examTime="",userinput=""):
    try:
        value = userinput.strip()
        upper = value.upper()        
        if object.exists(examinationListView):
            examListView = waitForObject(examinationListView)
            childItem=object.children(examListView)
            childItems=object.children(childItem[0])    
        for child in childItems:        
            childrens=object.children(child)            
            if len(childrens)>0:
                examButton=object.children(childrens[0])
                row=object.children(examButton[1])
                dateValue=row[3].text                
            if(dateValue==examTime):
                snooze(2)
                mouseClick(waitForObject(child))
                if childrens[0].highlighted:
                    test.log("Successfully selected the examination record")
                else:
                    test.log("Examination record is not selected") 
                snooze(2)
            if object.exists(otherOptionExamButtonExaminationList):
                mouseClick(waitForObject(otherOptionExamButtonExaminationList))
                if waitForObject(patientCardInfoDeleteExamButton):
                    mouseClick(waitForObject(patientCardInfoDeleteExamButton))
                    snooze(2)
                    cancelWarningMessage = str(waitForObject(deleteExamWarningPopUp).warning)
                    #textMessage = "Delete 2 exams?"
                    if "Delete" in cancelWarningMessage:
                        if upper == "CONFIRM":
                            if waitForObject(confirmDeleteExamWarningPopUp):
                                mouseClick(waitForObject(confirmDeleteExamWarningPopUp))
                                snooze(2)
                                test.log("Successfully deleted the examination record")
                                return True
                            else:
                                test.log("Failed to delete Examination record")
                                return False
                        elif upper == "DISCARD":
                            if waitForObject(discardDeleteExamWarningPopUp):
                                mouseClick(waitForObject(discardDeleteExamWarningPopUp))
                                snooze(2)
                                test.log("Successfully discarded the pop up message")
                                return True
                            else:
                                test.log("Pop up message is still there ")
                                return False                           
                    else:
                        test.log("Delete substring is not there in cancelWarningMessage ")
                        return False                
            elif object.exists(patientCardInfoDeleteExamButton):
                mouseClick(waitForObject(patientCardInfoDeleteExamButton))
                snooze(2)
                cancelWarningMessage = str(waitForObject(deleteExamWarningPopUp).warning)
                #cancelWarningMessage = str(waitForObject(patientCardDeletePopUpMessage).text)
                #textMessage = "Delete 2 exams?"
                if "Delete" in cancelWarningMessage:
                    if confirm:
                        if waitForObject(confirmDeleteExamWarningPopUp):
                            mouseClick(waitForObject(confirmDeleteExamWarningPopUp))
                            snooze(2)
                            test.log("Successfully deleted the examination record")
                            return True
                        else:
                            test.log("Failed to delete Examination record")
                            return False
                    if discard:
                        if waitForObject(discardDeleteExamWarningPopUp):
                            mouseClick(waitForObject(discardDeleteExamWarningPopUp))
                            snooze(2)
                            test.log("Successfully discarded the pop up message")
                            return True
                        else:
                            test.log("Pop up message is still there ")
                            return False                           
                else:
                        test.log("Delete substring is not there in cancelWarningMessage ")
                        return False
            else:
                test.log("Not able find other and delete button")                   
       
    except Exception as e:
        test.fail("Exception"+str(e))  
        
#Function to delete multiple examination records
def deleteMultipleExaminationRecord(noOfRecordsToBeDeleted,userinput):
    try:
        value = userinput.strip()
        upper = value.upper()        
        if object.exists(examinationListView):
            examListView = waitForObject(examinationListView)
            childItem=object.children(examListView)
            childItems=object.children(childItem[0])
            recordsBeforeDeleting= examListView.count
            test.log("Records before deleting = %d" %recordsBeforeDeleting)
            if recordsBeforeDeleting >= noOfRecordsToBeDeleted:
                number = 0
            for child in childItems:
                childrens=object.children(child)
                if len(childrens)>0:
                    examButton=object.children(childrens[0])
                    if number < noOfRecordsToBeDeleted:
                        mouseClick(waitForObject(examButton[0]))
                        if childrens[0].highlighted :
                            number += 1
                        else:
                            test.fail("Given patient's record is not selected")
            test.log("Successfully selected the %d patient's record in patient card screen" %number)                
            if object.exists(muliExamDeleteButtonPatientCard):
                mouseClick(waitForObject(muliExamDeleteButtonPatientCard))
                snooze(2)
                cancelWarningMessage = str(waitForObject(multiExamDeletePopUp).warning)
                selectedExaminationNumber = str(number)            
                if selectedExaminationNumber in cancelWarningMessage :
                    if upper == "DISCARD":
                        if object.exists(multiExamDeleteCancelButton):
                            mouseClick(waitForObject(multiExamDeleteCancelButton))
                            test.log("Successfully discard the delete pop up message")
                            return True
                        else:
                            return False
                    elif upper == "CONFIRM":
                        if object.exists(multiExamDeleteConfirmButton):
                            mouseClick(waitForObject(multiExamDeleteConfirmButton))
                            test.log("Successfully confirmed the delete pop up message and navigate to examination page")
                            return True
                        else:
                            return False
                test.log("selected examination number is not present in cancel warning pop up")
            else:
                test.log("Failed to find multiexam delete button in exam list screen ")
    
    except Exception as e:
        test.fail("Exception"+str(e)) 
        
#Function to search the patient examination record                                            
def getExaminationInPatientCardScreen(pid,date):
    try:
        
        if object.exists(examinationListView):
            examListView = waitForObject(examinationListView)
            childItem=object.children(examListView)
            childItems=object.children(childItem[0])
            
            noOfRecords = 0
                      
            for child in childItems:        
                childrens=object.children(child)
                
                if len(childrens)>0:
                    examButton=object.children(childrens[0])
                    row=object.children(examButton[1])
                    dateValue=row[3].text
                    date1 = str(dateValue).strip()
                    
                    if(date1==date):
                        noOfRecords = noOfRecords + 1
                    else:
                        pass
                           
            if noOfRecords >= 1:
                test.passes("Successfully patient examination record found ")
            else:
                test.fail("Patient examination record not found")
                
            
    except Exception as e:
        test.fail("Exception"+ str(e))  
        
# Function to search the patient to navigate to the examination page from patient card screen
def searchThePatientDetailsToNavigateToExaminationPageFromPatientCardScreen(pid):
    try:
        if object.exists(patientCardSearchInput):
            searchBox = (waitForObject(patientCardSearchInput))
            searchBox.text = ""
            type(waitForObject(patientCardSearchInput), pid)
            patientListView = waitForObject(patientCardPatientListView)
            item = object.children(patientListView)
            row = object.children(item[0])
                
            for i in row:
                outline = object.children(i)
                if len(outline) > 0:
                    label = object.children(outline[0])
                    value = label[1].text
                    valuePid = str(value).strip()
                    test.log("valuePid=%s" %valuePid)
                    if valuePid == pid:
                        test.log("The given pid is matching with the patient's pid in the list")
                        if object.exists(patientCardInfoButton):
                            mouseClick(waitForObject(patientCardInfoButton))
                            snooze(2)
                            if object.exists(patientCardInfoEditPatientButton):
                                mouseClick(waitForObject(patientCardInfoEditPatientButton))
                                patientId = waitForObject(patientCardAddPatientIdInput)
                                child = patientId.text
                                if child == pid:
                                    mouseClick(waitForObject(patientCardAddPatientBackButton))
                                    test.log("Successfully navigated to the %s patients examination page" %pid)
                                    
                                else:
                                    test.log("Examination page is not displayed for patient with patient id "+pid)
                            
        return True
    
    except Exception as e:
        test.fail("Exception: " + str(e))
        
#Function to preview the examination in examination page
def previewExaminationInExaminationPage(date):
    try:
        if object.exists(examinationListView):
            parent = waitForObject(examinationListView)
            child = object.children(parent)
            child_1 = object.children(child[0])
           
            for i in child_1:
                child_2 = object.children(i)
                if len(child_2) > 0:
                    child_3 = object.children(child_2[0])
                    child_4 = object.children(child_3[1])
                    label = child_4[3].text
                    
                    timeBeforeRecordingTrim = str(date).strip()
                    value = str(label).strip()
                    test.log("timeBeforeRecordingTrim =%s" %timeBeforeRecordingTrim)
                    test.log("value =%s" %value)
                    dateObject = datetime.datetime.strptime(timeBeforeRecordingTrim,"%H:%M:%S %d-%m-%Y")
                    minusTime = dateObject - datetime.timedelta(seconds=1)
                    plusTime = dateObject + datetime.timedelta(seconds=1)
                    dateObjectFormat = dateObject.strftime("%H:%M:%S %d-%m-%Y")
                    minusTimeFormat = minusTime.strftime("%H:%M:%S %d-%m-%Y")
                    plusTimeFormat = plusTime.strftime("%H:%M:%S %d-%m-%Y")
                    test.log("dateObjectFormat =%s" %dateObjectFormat)
                    test.log("minusTimeFormat =%s" %minusTimeFormat)
                    test.log("plusTimeFormat =%s" %plusTimeFormat)
                    if value or minusTimeFormat or plusTimeFormat:
                        test.log("Exam time in the record and the given exam time are matching")
                        mouseClick(waitForObject(i))
                        mouseClick(waitForObject(patientCardInfoLoadExamButton))
                        snooze(2)
                    else:
                        test.fail("Not Found")
                       
        return True
                       
    except Exception as e:
        test.fail("Exception: " + str(e)) 
        
#Function to scroll the list and get the patient details in patient card screen
def scrollListInPatientCardScreen():
    
    patientList=[]
    y_list = []
    i = 0.0
    
    #for i in range(0, 124):
    while i <= 1.0  :             
        listChild=[]        
        
        listChild = waitForObject(patientCardPatientListView)
        item = object.children(listChild)
        rowParent = object.children(item[0])
        
        for j in  rowParent:        
            rowchild = object.children(j)
            
            if len(rowchild)>0:
                row = object.children(rowchild[0])
                
                if j.y in y_list:
                    pass
                else:
                    patientData = []
                    name = (str(row[0].text).lower()).replace(",","").replace(" ", "")
                    id= str(row[1].text).lower()
                    lastExam=str(row[2].text).lower()                   
                    patientData.append(name)
                    patientData.append(id)
                    patientData.append(lastExam)
                    
                    patientList.append(patientData)
                    
                    y_list.append(j.y) 
  
        flick(waitForObject(patientCardPatientListView), 0, 415)
        i = item[1].position
    
    return patientList     

#Function to scroll the list and get the patient details in patient card screen
def scrollListInPatientCardScreenForDelete():
    
    patientList=[]
    y_list = []
    i = 0.0
    
    #for i in range(0, 124):
    while i <= 1.0  :             
        listChild=[]        
        
        listChild = waitForObject(patientCardPatientListView)
        item = object.children(listChild)
        rowParent = object.children(item[0])
        
        for j in  rowParent:        
            rowchild = object.children(j)
            
            if len(rowchild)>0:
                row = object.children(rowchild[0])
                
                if j.y in y_list:
                    pass
                else:
                    patientData = []
                    name = (str(row[0].text).lower()).replace(",","").replace(" ", "")
                    id= str(row[1].text)
                    lastExam=str(row[2].text).lower()                   
                    patientData.append(name)
                    patientData.append(id)
                    patientData.append(lastExam)
                    
                    patientList.append(patientData)
                    
                    y_list.append(j.y) 
  
        flick(waitForObject(patientCardPatientListView), 0, 415)
        i = item[1].position
    
    return patientList     

#function to sort in ascending order by using patient name in patient card screen
def testAscendingByNameSortInPatientCardScreen():
    try:
        result=False
        patientList=scrollListInPatientCardScreen()
            
        newList = []
        newList = patientList[:]
        
        newList.sort(key = lambda x: x[0].lower())
        if newList == patientList:
            result=True
            test.passes("Sorted in ascending order by using patient name in patient card screen")
        else:
            result=False
            totalRecords=len(newList)
            
            iteration=0
            
            while iteration < totalRecords:
                 
                if newList[iteration] == patientList[iteration]:
                    pass
                else:
                    test.fail("Sort error at ",str(newList[iteration]))
                iteration = iteration+1 
        return result
                       
    except Exception as e:
        test.fail("Exception: " + str(e)) 
    
#function to sort in descending order by using patient name in patient list screen
def testDescendingByNameSortInPatientCardScreen():
    try:
        result=False
        patientList=scrollListInPatientCardScreen()
            
        newList = []
        newList = patientList[:]
        
        
        newList.sort(key = lambda x: x[0].lower(),reverse=True)
    
        if newList == patientList:
            result=True
            test.passes("Sorted in descending order by using patient name in patient card screen")
        else:
            result=False
            totalRecords=len(newList)
            
            iteration=0
            
            while iteration < totalRecords:
                 
                if newList[iteration] == patientList[iteration]:
                    pass
                else:
                    test.fail("Sort error at ",str(newList[iteration]))
                iteration = iteration+1
                
        return result
                       
    except Exception as e:
        test.fail("Exception: " + str(e))
    
#Function to verify sort by using patient name in patient card screen
def verifySortForPnameInPatientCardScreen(sortType):
    try:  
        if object.exists(nameSortButton):
            
            sortButtonState =str(waitForObject(nameSortButton).state)
            
            if sortButtonState == "" and sortType == "ascending":
                mouseClick(waitForObject(nameSortButton)) 
                if testAscendingByNameSortInPatientCardScreen():
                    return True
                else:
                    return False
            elif sortType == "ascending" and sortButtonState == "ascendingSort":
                if testAscendingByNameSortInPatientCardScreen():
                    return True
                else:
                    return False
                
            elif sortType == "ascending" and sortButtonState == "descendingSort":
                mouseClick(waitForObject(nameSortButton))
                if testAscendingByNameSortInPatientCardScreen():
                    return True
                else:
                    return False        
            elif sortType == "descending" and sortButtonState == "":
                mouseClick(waitForObject(nameSortButton))
                snooze(2)
                mouseClick(waitForObject(nameSortButton))
                if testDescendingByNameSortInPatientCardScreen():
                    return True
                else:
                    return False                            
            elif sortType == "descending" and sortButtonState == "descendingSort":
                if testDescendingByNameSortInPatientCardScreen():
                    return True
                else:
                    return False                
            elif sortType == "descending" and sortButtonState == "ascendingSort":
                mouseClick(waitForObject(nameSortButton))
                if testDescendingByNameSortInPatientCardScreen():
                    return True
                else:
                    return False 
     
    except Exception as e:
        test.fail("Exception"+ str(e))
        
#function to sort in ascending order by using patient id in patient card screen
def testAscendingByPatientIdSortInPatientCardScreen():
    try:
        result=False
        patientList=scrollListInPatientCardScreen()
            
        newList = []
        newList = patientList[:]
        
        
        newList.sort(key = lambda x: x[1].lower())
    
        if newList == patientList:
            result=True
            test.passes("Sorted in ascending order by using patient id in patient card screen")
        else:
            result=False
            totalRecords=len(newList)
            
            iteration=0
            
            while iteration < totalRecords:
                 
                if newList[iteration] == patientList[iteration]:
                    pass
                else:
                    test.fail("Sort error at ",str(newList[iteration]))
                iteration = iteration+1
      
        return result  
     
    except Exception as e:
        test.fail("Exception"+ str(e))
    
#function to sort in descending order by using patient id in patient card screen
def testDescendingBypatientIdSortInPatientCardScreen():
    try:
        result=False
        patientList=scrollListInPatientCardScreen()
            
        newList = []
        newList = patientList[:]
        
        
        newList.sort(key = lambda x: x[1].lower(), reverse=True)
    
        if newList == patientList:
            result=True
            test.passes("Sorted in descending order by using patient id in patient card screen")
        else:
            result=False
            totalRecords=len(newList)
                
            iteration=0
            
            while iteration < totalRecords:
                 
                if newList[iteration] == patientList[iteration]:
                    pass
                else:
                    test.fail("Sort error at ",str(newList[iteration]))
                iteration = iteration+1
            
        return result
                       
    except Exception as e:
        test.fail("Exception: " + str(e)) 
    
#Function to verify sort by using patient id in patient card screen
def verifySortForPidInPatientCardScreen(sortType):
    try:  
        if object.exists(idSortButton):
            
            sortButtonState =str(waitForObject(idSortButton).state)
            
            if sortButtonState == "" and sortType == "ascending":
                mouseClick(waitForObject(idSortButton)) 
                if testAscendingByPatientIdSortInPatientCardScreen():
                    return True
                else:
                    return False
            elif sortType == "ascending" and sortButtonState == "ascendingSort":
                if testAscendingByPatientIdSortInPatientCardScreen():
                    return True
                else:
                    return False                
            elif sortType == "ascending" and sortButtonState == "descendingSort":
                mouseClick(waitForObject(idSortButton))
                if testAscendingByPatientIdSortInPatientCardScreen():
                    return True
                else:
                    return False         
            elif sortType == "descending" and sortButtonState == "":
                mouseClick(waitForObject(idSortButton))
                snooze(2)
                mouseClick(waitForObject(idSortButton))
                if testDescendingBypatientIdSortInPatientCardScreen():
                    return True
                else:
                    return False                            
            elif sortType == "descending" and sortButtonState == "descendingSort":
                if testDescendingBypatientIdSortInPatientCardScreen():
                    return True
                else:
                    return False                
            elif sortType == "descending" and sortButtonState == "ascendingSort":
                mouseClick(waitForObject(idSortButton))
                if testDescendingBypatientIdSortInPatientCardScreen():
                    return True
                else:
                    return False     
    except Exception as e:
        test.fail("Exception"+ str(e))
        
 
#function to sort in ascending order by using last exam in patient card screen
def testAscendingByLastExamSortInPatientCardScreen():
    try:
        result=False
        patientList=scrollListInPatientCardScreen()
        updatedPatientList = []
        
        for i in patientList:
            
            if len(i[2]) > 4:
                i[2] = datetime.datetime.strptime(i[2].strip(), "%H:%M:%S %d-%m-%Y")
                patData = []
                patData.append(i[0])
                patData.append(i[1])
                patData.append(i[2])
                updatedPatientList.append(patData)
            else:
                patientList.remove(i)
                
        for data in updatedPatientList:
            print str(data[2])
            
        newList = []
        newList = updatedPatientList[:]
        newList.sort(key = lambda x: x[2])
        
        if newList == updatedPatientList:
            result=True
            test.passes("Sorted in ascending order by using last exam in patient card screen")
        else:
            result=False
            totalRecords=len(newList)
            
            iteration=0
            
            while iteration < totalRecords:
                 
                if newList[iteration] == patientList[iteration]:
                    pass
                else:
                    test.fail("Sort error at ",str(newList[iteration]))
                iteration = iteration+1
                
        return result
     
    except Exception as e:
        test.fail("Exception"+ str(e))
    
#function to sort in descending order by using last exam  in patient card screen
def testDescendingByLastExamSortInPatientCardScreen():
    try:
        result=False
        patientList=scrollListInPatientCardScreen()
        updatedPatientList = []
        
        for i in patientList:
            
            if len(i[2]) > 4:
                i[2] = datetime.datetime.strptime(i[2].strip(), "%H:%M:%S %d-%m-%Y")
                patData = []
                patData.append(i[0])
                patData.append(i[1])
                patData.append(i[2])
                updatedPatientList.append(patData)
            else:
                patientList.remove(i)
                
        for data in updatedPatientList:
            print str(data[2])
            
        newList = []
        newList = updatedPatientList[:]
        
        newList.sort(key = lambda x: x[2], reverse=True)
        if newList == updatedPatientList:
            result=True
            test.passes("Sorted in descending order by using last exam in patient card screen")
        else:
            result=False
            totalRecords=len(newList)
            
            iteration=0
            
            while iteration < totalRecords:
                 
                if newList[iteration] == patientList[iteration]:
                    pass
                else:
                    test.fail("Sort error at ",str(newList[iteration]))
                iteration = iteration+1
        return result 
     
    except Exception as e:
        test.fail("Exception"+ str(e))
    
#Function to verify sort by using last exam in patient card screen
def verifySortForLastExamInPatientCardScreen(sortType):
 
    try:  
        if object.exists(lastExamSortButton):
        
            sortButtonState =str(waitForObject(lastExamSortButton).state)
            
            if sortButtonState == "" and sortType == "ascending":
                mouseClick(waitForObject(lastExamSortButton)) 
                if testAscendingByLastExamSortInPatientCardScreen():
                    return True
                else:
                    return False                
            elif sortType == "ascending" and sortButtonState == "ascendingSort":
                if testAscendingByLastExamSortInPatientCardScreen():
                    return True
                else:
                    return False                
            elif sortType == "ascending" and sortButtonState == "descendingSort":
                mouseClick(waitForObject(lastExamSortButton))
                if testAscendingByLastExamSortInPatientCardScreen():
                    return True
                else:
                    return False                
            elif sortType == "descending" and sortButtonState == "":
                mouseClick(waitForObject(lastExamSortButton))
                snooze(2)
                mouseClick(waitForObject(lastExamSortButton))
                if testDescendingByLastExamSortInPatientCardScreen():
                    return True
                else:
                    return False                        
            elif sortType == "descending" and sortButtonState == "descendingSort":
                if testDescendingByLastExamSortInPatientCardScreen():
                    return True
                else:
                    return False                
            elif sortType == "descending" and sortButtonState == "ascendingSort":
                mouseClick(waitForObject(lastExamSortButton))
                if testDescendingByLastExamSortInPatientCardScreen():
                    return True
                else:
                    return False     
    except Exception as e:
        test.fail("Exception"+ str(e))
        
# Function to search the patient to navigate to the examination page from patient card screen
def searchThePatientDateInPatientCardScreen(Pdate):
    try:
        result=False
        if object.exists(patientCardSearchInput):
            searchBox = (waitForObject(patientCardSearchInput))
            searchBox.text = ""
            type(waitForObject(patientCardSearchInput), Pdate)
            patientListView = waitForObject(patientCardPatientListView)
            item = object.children(patientListView)
            row = object.children(item[0])
                
            for i in row:
                outline = object.children(i)
                if len(outline) > 0:
                    label = object.children(outline[0])
                    value = label[2].text
                    valuePdate = str(value).strip()
                    test.log("valuePdate=%s" %valuePdate)
                    if valuePdate == Pdate:
                        test.log("The given Pdate is matching with the patient's Pdate in the list")
                        if object.exists(patientCardInfoButton):
                            mouseClick(waitForObject(patientCardInfoButton))
                            snooze(2)
                            result=True
                        else:
                            result=False
                            test.fail("Examination page is not displayed for patient with patient date "+Pdate)
                            
        return result
    
    except Exception as e:
        test.fail("Exception: " + str(e))

'''Localization testing-patient card'''
        

def Collectingalltextfrompatientcard1():
    try:
        #collecting select all text
        status='fail'
        if object.exists(patientOpButtnColumnId):
            parent=findObject(patientOpButtnColumnId)
            child=object.children(parent)
            for x in range(len(child)):
                column_0=object.children(child[x])
                str1=column_0[1].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(0.5)
            #collecting warning text
        if object.exists(patientDelete):
            mouseClick(patientDelete)
            parent=findObject(deleteWarningItemId)
            child=object.children(parent)
            column_0=object.children(child[0])
            Row_0=object.children(column_0[0])
            str1=Row_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            #collecting delete message
            item_2=object.children(column_0[2])
            Row_0=object.children(item_2[0])
            str1=Row_0[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
        if object.exists(WarningconfirmButtonId):
            tapObject(WarningconfirmButtonId)
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log("Exception: " + str(e))
 

def patientcardsortingtext(*arguments):
    try:
        status='fail'
        for obj in arguments:
            if object.exists(obj):
                parent=findObject(obj) 
                child=object.children(parent)
                str1=child[3].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log("Exception: " + str(e))
        
def Patientserachtext():
    try:
        status='fail'
        if object.exists(SearchtextID):
            parent=findObject(SearchtextID) 
            child=object.children(parent)
            str1=child[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception: " + str(e))
        
#Collecting all text from add patient card screen
def Collectingalltextfromaddpatientcardscreen():
    try:
        status='fail'
        #Collecting Surname text
        if object.exists(patientInfoId):
            parent=findObject(patientInfoId)
            child=object.children(parent)
            col_0=object.children(child[0])
            col_00=object.children(col_0[0])
            str1=col_00[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #collecting First name text
            Grid1=object.children(col_0[1])
            col_0=object.children(Grid1[0])
            str1=col_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting Title text
            col_0=object.children(Grid1[1])
            str1=col_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #collecting date of birth
            col_0=object.children(Grid1[2])
            str1=col_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #collecting Age
            col_0=object.children(Grid1[3])
            str1=col_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting PID
            col_0=object.children(Grid1[4])
            str1=col_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #collecting HID
            col_0=object.children(Grid1[5])
            str1=col_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #date format=DD/MM/YYYY
            parent=findObject(textId)
            child=object.children(parent)
            #child1=object.children(child[0])
            str1=child[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log("Exception: " + str(e))

#collecting text from right side of add patient screen  
def Collectingalltextfromaddpatientcardscreen1():
    try:
        #Collecting Gender text
        status='fail'
        if object.exists(patientInfoId):
            parent=findObject(patientInfoId)
            child=object.children(parent)
            col_0=object.children(child[2])
            Row0=object.children(col_0[0])
            str1=Row0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting classification text
            column_0=object.children(col_0[1])
            str1=column_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #collecting Pace maker text
            Grid=object.children(col_0[2])
            Row_1=object.children(Grid[1])
            str1=Row_1[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting Digoxin user
            Row_1=object.children(Grid[3])
            str1=Row_1[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
            #collecting mandatory_field_text 
        if mandatory_field_text():
            status='pass'      
        return True if status=='pass' else False
    except Exception as e:
        test.log("Exception: " + str(e))

#collecting male,female and other text
def genderoptionsandyesorno(*arguments):
    try:
        status='fail'
        for obj in arguments:
            if object.exists(obj):
                parent=findObject(obj)
                child=object.children(parent)
                str1=child[1].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(1)
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log("Exception: " + str(e))

#collecting mandatory field text
def mandatory_field_text():
    try:
        status='fail'
        if object.exists(patientCardAddviewId):
                parent=findObject(patientCardAddviewId)
                child=object.children(parent)
                col_1=object.children(child[1])
                item2=object.children(col_1[2])
                str1=item2[0].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(1)
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log("Exception: " + str(e))
        

#Clicking on classification combo box and collecting text
def Collectingclassificationbasedoncountry():
    try:
        status='fail'
        if waitForObject(classificationComboBoxId):
            if object.exists(classificationComboBoxId):
                tapObject(classificationComboBoxId)
                snooze(3)
                Collectingclassificationbasedoncountry_text(European_Text,Northeast_Asian,Japan_text,African_text,
                                                            Southeast_Asian,North_Indians,South_Indians,African_American,
                                                            Mexican_text,Latio_American,Iberian_text,Pakistanis_text,Polynesian)
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log("Exception: " + str(e))

#collecting all the country text        
def Collectingclassificationbasedoncountry_text(*arguments):                
    try:
        status='fail'      
        for obj in arguments:
            parent=findObject(obj)
            child=object.children(parent)
            str1=child[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log("Exception: " + str(e))
                    
                    
                
# Method to Search a record from Patient card and Navigate to Examination page using patient ID
def searchAndNavigateToExaminationPage(patientIDSearch):
    try:
        Status = False
        patientIDToSearch = patientIDSearch
        snooze(2)
        if (waitForObject(patientCardSearchInput)):
            type(waitForObject(patientCardSearchInput), patientIDToSearch)
            
            if (waitForObject(patientCardPatientListView)):
                patientTable = waitForObject(patientCardPatientListView)
                patientListItem = object.children(patientTable)
                snooze(1)
                patientItemRows = object.children(patientListItem[0])
                
                if len(patientItemRows):
                    for i in range(len(patientItemRows)):
                                   
                        childRows = object.children(patientItemRows[i])
                        if len(childRows):
                            subRows = object.children(childRows[0])
                            innerRows = object.children(subRows[0])
                            
                            rowValue = innerRows[3].text
                            if (rowValue == patientIDToSearch):
                                test.log("Successfully searched '"+ patientIDToSearch +"' record from Patient Card")
                                mousePress(innerRows[3])
                                snooze(0.15)
                                mouseRelease(innerRows[3])
                                snooze(0.10)

                                if (waitForObject(patientCardInfoEditPatientButton)):
                                    Status = True
                                    break
                else:
                    test.log("No matching record found in Patient Card with the given patient ID '"+ patientIDToSearch +"'")
                                        
            else:
                    test.log("Failed to search '"+ patientIDToSearch +"' record from Patient Card")            
        else:
            test.log("Failed to search '"+ patientIDToSearch +"' record from Patient Card")
        
        if Status:
            test.log("Successfully navigated to Examination screen")
            return True
        else:
            test.log("Failed to navigate to Examination screen")           
            return False                

    except Exception as e:
        test.fail("Exception"+ str(e))
                   
                   
# Function to delete single patient record in patient card screen
def deleteOnePatientRecordInPatientCard():
    try:
        count = 0
        snooze(1)
        if(productCode=='lx'): 
            mouseClick(showOtherButtonsButtonId7Inch)
            
        if waitForObject(patientCardDeletePatientButton): 
            #setFocus(patientCardDeletePatientButton) 
            mouseClick(waitForObject(patientCardDeletePatientButton))
            cancelWarningMessage = str(findObject(patientCardDeletePatientCancelPopUpMessage).text)
            textMessage = "Delete 1 patient(s)?"
            
            if cancelWarningMessage == textMessage:
                mouseClick(waitForObject(patientCardDeletePatientYesButton))
                snooze(1)
                
                if object.exists(patientCardDeletePatientButton):
                    test.log(" Fail to delete patient record ")
                    
                else:
                    count = 1             
                            
        if count == 1:
            return True
        else:
            return False
                    
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to verify given patient record is exists or not it return True if record not exists
def verifyGivenPatientIsNotExistsInPatientCard(patientID):
    try:
        count = 0
        if waitForObject(patientCardSearchInput):
            searchBox = (waitForObject(patientCardSearchInput))
            searchBox.text = ""
            type(waitForObject(patientCardSearchInput), patientID)
            
            if waitForObject(patientCardPatientListView):
                if object.exists(patientRecord):
                    test.log(" Still given record is displayed in patient card ")
                else:
                    test.log(" Record deleted successfully ")
                    count = 1
            else:
                test.log(" Patient list view is not displayed ")
        else:
            test.log(" Search box is not displayed ")
            
        if count == 1:
            return True
        else:
            return False
                    
    except Exception as e:
        test.fail("Exception" + str(e))

# Method to navigate to Live page from patient card page  
def navigateToLiveFromPatientCardPage():
    try:
        count = 0
        if (waitForObject(patientCardAddPatientBackButton)):
            mouseClick(waitForObject(patientCardAddPatientBackButton))
            mouseClick(waitForObject(menuRecordingButton))
            snooze(1)
            if (waitForObject(liveScreenPatientListButton)):
                test.log(" Successfully navigated to live screen ")
                count = 1
            else:                
                test.log(" Unable to navigate to live screen ")
            
        else:
            test.log(" Unable to click back button in patient card screen ")
        
        if count == 1:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
        

# Method to delete latest examination from patient card page  
def deleteExaminationFromPatientCardPage():
    try:
        count = 0
        if (waitForObject(examinationListView)):
            mouseClick(waitForObject(examButtonId))
            snooze(.5)
            if (waitForObject(patientCardInfoOtherOptionsExamButton)):
                mouseClick(waitForObject(patientCardInfoOtherOptionsExamButton))
                snooze(.5)
                if (waitForObject(patientCardInfoDeleteExamButton)):
                    mouseClick(waitForObject(patientCardInfoDeleteExamButton))
                    mouseClick(waitForObject(patientCardDeletePatientYesButton))
                    snooze(1)
                    if (object.exists(examinationListView)):
                        test.log(" Fail to delete examination in patient card ")
                    else:
                        test.log(" Successfully deleted the examination from patient card ")
                        count = 1                    
    
                else:                
                    test.log(" Delete option is not displayed ")
            else:                
                test.log(" Other option is not displayed ")        
        else:
            test.log(" Examination list view is not displayed in patient card screen ")
        
        if count == 1:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
        
        
    
        
        
        
# Function to add a new patient in patient card screen with PID and surname
def addNewPatientInPatientCardUsingPId(PatientId,Surname):
    try:
        snooze(.25)
        if(productCode=='lx'): 
            if waitForObject(liveScreenAddPatientSurnameInput7Inch):
                setFocusTextBox(liveScreenAddPatientSurnameInput7Inch)
                type(mainWindow, Surname)
                # type(waitForObject(liveScreenAddPatientSurnameInput), Surname)
                snooze(.25)  
                mouseClick(waitForObject(liveScreenAddPatientSaveButton7Inch))
                snooze(.25) 
                
                setFocusTextBox(patientCardAddPatientIdInput7Inch)
                type(mainWindow, PatientId) 
                snooze(.25)  
                mouseClick(waitForObject(liveScreenAddPatientSaveButton7Inch))
                snooze(.25) 
        else: 
            if waitForObject(patientCardAddPatientIdInput):
                setFocusTextBox(patientCardAddPatientSurnameInput)
                type(mainWindow, Surname)
                snooze(.25)
                
                setFocusTextBox(patientCardAddPatientIdInput)
                type(mainWindow, PatientId)           
        
        mouseClick(waitForObject(patientCardAddPatientSaveButton))
        return True
                
    except Exception as e:
        test.fail("Exception" + str(e))  
        
# Function to verify patient already exists warning
def verifyingPatientAlreadyExistsWarning(PatientId,Surname):
    try:
        count = 0
        if(productCode=='lx'): 
            if waitForObject(liveScreenAddPatientSurnameInput7Inch):
                setFocusTextBox(liveScreenAddPatientSurnameInput7Inch)
                type(mainWindow, Surname)
                snooze(.5)  
                mouseClick(waitForObject(liveScreenAddPatientSaveButton7Inch))
                snooze(.5)
                
                setFocusTextBox(patientCardAddPatientIdInput7Inch)
                type(mainWindow, PatientId) 
                snooze(.25)  
                mouseClick(waitForObject(liveScreenAddPatientSaveButton7Inch))
                snooze(.25)
                
                mouseClick(waitForObject(patientCardAddPatientSaveButton))    
                if (object.exists(livePatientDialogErrorOkButton)):
                    alreadyExistsWarningMessage = str(findObject(patientCardAddPatientCancelPopUpMessage).text)
                    textMessage = "Patient ID already exists"
                    
                    if textMessage in alreadyExistsWarningMessage:
                        mouseClick(waitForObject(livePatientDialogErrorOkButton))
                        count =1
                        test.log(" Patient ID already exists message is displayed ")
                    else:
                        test.log(" Patient ID already exists message is not displayed ") 
        else :
            if waitForObject(patientCardAddPatientIdInput):
                setFocusTextBox(patientCardAddPatientSurnameInput)
                type(mainWindow, Surname)
                snooze(1)
                
                setFocusTextBox(patientCardAddPatientIdInput)
                type(mainWindow, PatientId)
            # Handling Patient Id already exists dialog
            type(mainWindow, "<Tab>")   
            mouseClick(waitForObject(patientCardAddPatientSaveButton))    
            if (object.exists(livePatientDialogErrorOkButton)):
                alreadyExistsWarningMessage = str(findObject(patientCardAddPatientCancelPopUpMessage).text)
                textMessage = "Patient ID already exists"
                
                if textMessage in alreadyExistsWarningMessage:
                    mouseClick(waitForObject(livePatientDialogErrorOkButton))
                    count =1
                    test.log(" Patient ID already exists message is displayed ")
                else:
                    test.log(" Patient ID already exists message is not displayed ")
                
        if count == 1:
            return True
        else:
            return False
                
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to add a new patient with pid and set for recording
def addNewPatientInPatientCardUsingPIdSetForRecording(PatientId,Surname,Firstname):
    try:
        count = 0
        if(productCode=='lx'): 
            if waitForObject(liveScreenAddPatientSurnameInput7Inch):
                sNameInput =(waitForObject(liveScreenAddPatientSurnameInput7Inch))
                setFocusTextBox(liveScreenAddPatientSurnameInput7Inch)
                sNameInput.text=""
                type(mainWindow, Surname)
                snooze(.5)  
                mouseClick(waitForObject(liveScreenAddPatientSaveButton7Inch))
                snooze(.5) 
                
                pidInput =(waitForObject(patientCardAddPatientIdInput7Inch))
                setFocusTextBox(patientCardAddPatientIdInput7Inch)
                pidInput.text=""
                type(mainWindow, PatientId)
                snooze(.5)  
                mouseClick(waitForObject(liveScreenAddPatientSaveButton7Inch))
                snooze(.5)
                
                setFocusTextBox(patientCardAddPatientFirstNameInput7Inch)
                type(mainWindow, Firstname)
                snooze(.5) 
                mouseClick(waitForObject(liveScreenAddPatientSaveButton7Inch))
                snooze(.5)
                
                mouseClick(waitForObject(patientCardAddPatientRecordButton))
        else:
            if waitForObject(patientCardAddPatientIdInput):
                pidInput =(waitForObject(patientCardAddPatientIdInput))
                setFocusTextBox(patientCardAddPatientIdInput)
                pidInput.text=""
                type(mainWindow, PatientId)
                
                sNameInput =(waitForObject(patientCardAddPatientSurnameInput))
                setFocusTextBox(patientCardAddPatientSurnameInput)
                sNameInput.text=""
                type(mainWindow, Surname)
                snooze(1)
                
                setFocusTextBox(patientCardAddPatientFirstNameInput)
                type(mainWindow, Firstname)
                snooze(1)      
            
                mouseClick(waitForObject(patientCardAddPatientRecordButton))
        if (waitForObject(liveScreenECGRecordButton)):
            test.log(" Successfully navigated to Live waveform screen ")
            count =1
        else:
            test.log(" Fail to navigate to Live waveform screen ")
            
        if count == 1:
            return True
        else:
            return False
        
    except Exception as e:
        test.fail("Exception" + str(e)) 


# Method to Delete all records in patient card
def deleteAllPatientsInPatientCard():
    try:
        status = False
        snooze(1)
            
        if (waitForObject(patientCardPatientListView)):
            patientTable = waitForObject(patientCardPatientListView)
            totalRecords = patientTable.count
            patientListItem = object.children(patientTable)
            snooze(1)
            patientItemRows = object.children(patientListItem[0])
            

            for i in range(len(patientItemRows)):
                           
                childRows = object.children(patientItemRows[i])
                if len(childRows):
                    childRowsLabel = object.children(childRows[0])
                    longMouseClick(childRowsLabel[1])
                    snooze(1)
                    
                    if (waitForObject(patientCardSelectAllPatientButtonId)):
                        mouseClick(patientCardSelectAllPatientButtonId)
                        
                        if waitForObject(patientCardDeletePatientButton): 
                            mouseClick(waitForObject(patientCardDeletePatientButton))
                            cancelWarningMessage = str(findObject(patientCardDeletePatientCancelPopUpMessage).text)
                            textMessage = "Delete %s patient(s)?"%totalRecords
                            
                            if cancelWarningMessage == textMessage:
                                mouseClick(waitForObject(patientCardDeletePatientYesButton))
                                snooze(20)
                                
                                if object.exists(patientCardPatientListView):
                                    patientTableAfterDelete = waitForObject(patientCardPatientListView)
                                    totalRecordsAfterDelete = patientTableAfterDelete.count
                                    
                                    if totalRecordsAfterDelete == 0:
                                        status = True
                                        test.log(" Successfully deleted all patient records in patient card ")
                                        break
                                    
                                    else:
                                        test.log(" Fail to deleted all patient records in patient card ")
                        else:
                            test.log(" Delete button is not displayed ")
                    else:
                        test.log(" Select all button is not displayed ")
                                    
        else:
                test.log(" Patient card record list is not displayed ")            

        if status:
            test.log(" Successfully deleted all patient records ")
            return True
        else:
            test.log(" Failed to delete all patient records ")           
            return False
    
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Method to verify patient card is empty or not   
def verifyPatientCardIsEmptyOrNot():
    try:
        status = False
        snooze(2)
        if object.exists(patientCardPatientListView):
            patientTableAfterDelete = waitForObject(patientCardPatientListView)
            totalRecordsAfterDelete = patientTableAfterDelete.count
            
            if totalRecordsAfterDelete == 0:
                status = True
                test.log(" Patient card is empty ")
                           
            else:
                test.log(" Patient card is not empty  ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))        
        
# Method to create 1000 patient records in patient card   
def create1000PatientsInPatientCard():
    try:
        status = False
        snooze(.25)
        for i in range(1000):           
            snooze(.50)
            mouseClick(waitForObject(patientCardAddButton))
            addNewPatientInPatientCardUsingPId(str(i),str(i))
        snooze(6)        
        if object.exists(patientCardPatientListView):
            patientTableAfterCreate = waitForObject(patientCardPatientListView)
            totalRecordsAfterCreate = patientTableAfterCreate.count
            
            if totalRecordsAfterCreate == 1000:
                status = True
                test.log(" Successfully created 1000 patient records ")
                           
            else:
                test.log(" Fail to create 1000 Patient records  ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e)) 
        
# Method to verify 'Reached max patient limit' message    
def verifyMaxPatientLimitMessageInPatientCard():
    try:
        status = False           
        snooze(1)
        mouseClick(waitForObject(patientCardAddButton))
        addNewPatientInPatientCardUsingPId(str(1001),str(1001))
        
        snooze(5)        
        if object.exists(patientCardAddPatientCancelPopUpMessage):
            warMessageActual=str(waitForObject(patientCardAddPatientCancelPopUpMessage).text)
            warMessageExpected="Failed to add patient, Reached max patient limit, Delete a patient to continue"
            if warMessageExpected == warMessageActual:
                test.log(" Message displayed 'Failed to add patient, Reached max patient limit, Delete a patient to continue' ")
                snooze(5)
                mouseClick(waitForObject(patientCardMaxLimitOkButtonId))
                status = True
            else:
                test.log(" Warning message for maximum patient records is not matching " )

        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e)) 
        
# Method to get 'record' count in patient card    
def getRecordCountFromPatientCard():
    try:
        snooze(1)          
        if object.exists(patientCardPatientListView):
            patientTableAfterCreate = waitForObject(patientCardPatientListView)
            totalRecordsAfterCreate = patientTableAfterCreate.count
        else:
            test.log(" Fail to get the record count from patient card " )
        
        return totalRecordsAfterCreate

    except Exception as e:
        test.fail("Exception"+ str(e))     
                
# Method to navigate to waveform screen from patient list (waveform) page
def navigateToWaveformFromPatientList():
    try:
        count = 0
        snooze(1)
        if (waitForObject(patientCardAddPatientBackButton)):
            mouseClick(waitForObject(patientCardAddPatientBackButton))
            snooze(1)
            if (waitForObject(liveScreenECGRecordButton)):
                test.log(" Successfully navigated to waveform screen")
                count = 1
            else:                
                test.log(" Fail to navigate to waveform screen")
            
        else:
            test.log(" Unable to click back button in examination screen ")
        
        if count == 1:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e)) 
        
# Method to search a patient record and do long press   
def searchOnePatientAndDoLongPressInPatientCard(patientID):
    try:
        Status = False
        patientIDToSearch = patientID
        snooze(1)
        if (waitForObject(patientCardSearchInput)):
            type(waitForObject(patientCardSearchInput), patientIDToSearch)
            
            if (waitForObject(patientCardPatientListView)):
                patientTable = waitForObject(patientCardPatientListView)
                patientListItem = object.children(patientTable)
                snooze(1)
                patientItemRows = object.children(patientListItem[0])
                
                if len(patientItemRows):
                    for i in range(len(patientItemRows)):
                                   
                        childRows = object.children(patientItemRows[i])
                        if len(childRows):
                            subRows = object.children(childRows[0])
                            innerRows = object.children(subRows[0])
                            
                            rowValue = innerRows[3].text
                            if (rowValue == patientIDToSearch):
                                test.log(" Successfully searched '"+ patientIDToSearch +"' record from Patient Card")
                                longMouseClick(innerRows[3])
                                snooze(1)
                                    
                                if (waitForObject(patientCardSelectAllPatientButtonId)):
                                    Status = True
                                    test.log(" Patient record %s is selected and options pane is displayed "% patientIDToSearch)
                                    break
                else:
                    test.log("No matching record found in Patient Card with the given patient ID %s "  %patientIDToSearch)
                                        
            else:
                    test.log("Failed to search '"+ patientIDToSearch +"' record from Patient Card")            
        else:
            test.log("Failed to search '"+ patientIDToSearch +"' record from Patient Card")
        
        if Status:
            test.log(" Successfully selected patient record ")
            return True
        else:
            test.log(" Failed to select patient record ")           
            return False                

    except Exception as e:
        test.fail("Exception" + str(e))
        
        
# Function to delete single patient record in patient card screen
def deleteOnePatientRecordInPatientCard():
    try:
        count = 0
        snooze(1)
            
        if waitForObject(patientCardDeletePatientButton): 
            #setFocus(patientCardDeletePatientButton) 
            mouseClick(waitForObject(patientCardDeletePatientButton))
            cancelWarningMessage = str(findObject(patientCardDeletePatientCancelPopUpMessage).text)
            textMessage = "Delete 1 patient(s)?"
            
            if cancelWarningMessage == textMessage:
                mouseClick(waitForObject(patientCardDeletePatientYesButton))
                snooze(1)
                
                if object.exists(patientCardDeletePatientButton):
                    test.log(" Fail to delete patient record ")
                    
                else:
                    count = 1             
                            
        if count == 1:
            return True
        else:
            return False
                    
    except Exception as e:
        test.fail("Exception" + str(e))
        
        
# Method to select the latest examination for the particular patient record
def toSelectLatestExamination():
    myList = []
    count = 0
    i = 0
    try:
        snooze(2) 
        if (object.exists(examinationListView)):
             
            examListView = waitForObject(examinationListView)
            count = examListView.count
            examItems = object.children(examListView)
            examSubItem = object.children(examItems[0])
             
            examButton = object.children(examSubItem[count-1])
            if len(examButton) :
                examRows = object.children(examButton[0])
                examLabel = object.children(examRows[1])
                examinationTime = examLabel[3].text
                sExaminationTime = str(examinationTime)
                examDate = datetime.datetime.strptime(sExaminationTime.strip(), '%H:%M:%S %d-%m-%Y')
            else:
                examButton = object.children(examSubItem[count])
                examRows = object.children(examButton[0])
                examLabel = object.children(examRows[1])
                examinationTime = examLabel[3].text
                sExaminationTime = str(examinationTime)
                examDate = datetime.datetime.strptime(sExaminationTime.strip(), '%H:%M:%S %d-%m-%Y')
                 
            while i < count:
                lButton = object.children(examSubItem[i])
                if len(lButton):
                    lRows = object.children(lButton[0])
                    lLabel = object.children(lRows[1])
                    lTime = lLabel[3].text
                    sTime=str(lTime)
                    date = datetime.datetime.strptime(sTime.strip(), '%H:%M:%S %d-%m-%Y')
                    myList.append(date)
                    i += 1
                else:
                    count += 1
                    i += 1
            latestTime = max(myList)
             
            if (latestTime == examDate):
                mouseClick(examRows[1])
                test.log("Successfully selected latest Examination")
                return True
            
            else:
                test.log("Unable to select latest Examination") 
                return False         
        else:
            test.log("No examinations available to select")
            return False
         
    except Exception as e:
        test.fail("Exception"+ str(e))
        
# Method to navigate to preview page from examination. 
def navigateToPreviewFromExamination():
    
    try:
        count = 0
        snooze(1)
        if (waitForObject(patientCardInfoLoadExamButton)):
            mouseClick(waitForObject(patientCardInfoLoadExamButton))
            snooze(5)
            if (waitForObject(previewScreenRecordIndexDetail)): 
                test.log("Successfully navigated to Preview page")
                count = 1
                
            else:
                test.log("Failed to navigate to preview page")
                
        else:
            test.log("Unable to find examination button ")
            
        if count == 1:
            return True
        else:
            return False
        
    except Exception as e:
        test.fail("Exception"+ str(e))
        
# Method to navigate to Live page from Examination page  
def navigateToLiveFromExaminationPage():
    try:
        count = 0
        if (waitForObject(patientCardAddPatientBackButton)):
            mouseClick(waitForObject(patientCardAddPatientBackButton))
            mouseClick(waitForObject(patientCardAddPatientBackButton))
            mouseClick(waitForObject(menuRecordingButton))
            snooze(2)
            if (waitForObject(liveScreenECGRecordButton)):
                test.log("Successfully navigated to live screen")
                count = 1
            else:                
                test.log("Unable to navigate to live screen")
            
        else:
            test.log(" Unable to click back button in examination screen ")
        
        if count == 1:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))

