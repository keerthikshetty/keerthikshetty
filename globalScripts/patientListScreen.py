import __builtin__

#source(findFile('scripts', '../../globalScripts/liveScreen.py'))
#source(findFile('scripts', '../../../globalScripts/utils.py'))
#productCode=getProduct()

mainWindow = {"type": "QQuickWindowQmlImpl", "visible": True}
# mainWindow ={"container": mainWindow, "id": "onlineScreenId", "type": "OnlineWfScreen",  "visible": True}
# mainWindow = {"container": mainWindow, "id": "evaluationScreenId", "type": "EvalScreen",  "visible": True}
patientCardScreen_MainWindow = {"container": mainWindow, "id": "patientScreenId", "type": "PatientCard", "visible": True}
livePatientList_MainWindow = {"container": mainWindow, "id": "centreRectId", "type": "Rectangle", "visible": True}
liveAddPatient_MainWindow = {"container": mainWindow, "id": "centreRectId", "type": "Rectangle", "visible": True}

liveScreenPatientListButton = { "container": mainWindow, "id": "patientButtonId", "type": "CircularButton", "visible": True}
liveScreenPatientSearchInput = {"container": mainWindow, "id": "patientSearchInputId", "type": "SearchBar", "visible": True}
liveScreenPatientListView = {"container": mainWindow, "id": "patientListViewId", "type": "ListView", "visible": True}
liveScreenPatientCloseButton = {"container": mainWindow, "id": "closePatientDialogButtonId", "type": "CloseDialogButton", "visible": True}
evaluationScreenSaveRecordButton = { "container": mainWindow, "id": "saveRecordButtonId", "type": "CircularButton", "visible": True}

'''Objects of add patient button in live patient list screen'''
liveScreenPatientAddButton = { "container": mainWindow, "id": "addPatientButtonId", "type": "AddNewPatientButton", "visible": True}
liveScreenAddPatientSurnameInput = {  "container": mainWindow, "id": "surnameInputId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientFirstNameInput = {  "container": mainWindow, "id": "firstnameInputId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientTitleInput = {  "container": mainWindow, "id": "titleInputId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientDOBInput = {"container": mainWindow, "id": "dobInputId", "type": "DateOfBirthEntry", "visible": True}

liveScreenAddPatientAgeInput = {  "container": mainWindow, "id": "ageInputId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientIdInput = {  "container": mainWindow, "id": "patientIdInputId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientHospitalIdInput = {  "container": mainWindow, "id": "hospitalIdInputId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientMaleRadioButton = { "container": mainWindow, "id": "genderMaleRadioButtonId", "type": "CustomRadioButton", "visible": True}
liveScreenAddPatientFemaleRadioButton = { "container": mainWindow, "id": "genderFemaleRadioButtonId", "type": "CustomRadioButton", "visible": True}
liveScreenAddPatientOthersRadioButton = { "container": mainWindow, "id": "genderOtherRadioButtonId", "type": "CustomRadioButton", "visible": True}
liveScreenAddPatientClassificationComboBox = {"container": mainWindow, "id": "classificationComboBoxId", "type": "ComboBox", "visible": True}
liveScreenAddPatientWeightInput = {  "container": mainWindow, "id": "weightInputId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientWeightUnit = {"container": mainWindow, "text": "kg", "type": "Label", "visible": True}
liveScreenAddPatientHeightInput = {  "container": mainWindow, "id": "heightInputId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientHeightUnit = {"container": mainWindow, "text": "cm", "type": "Label", "visible": True}
liveScreenAddPatientPaceMakeYesButton = { "container": mainWindow, "id": "pacemakeYesButtonId", "type": "CustomRadioButton", "visible": True}
liveScreenAddPatientPaceMakeNoButton = { "container": mainWindow, "id": "pacemakeNoButtonId", "type": "CustomRadioButton", "visible": True}
liveScreenAddPatientDigoxinYesButton = { "container": mainWindow, "id": "digoxinYesButtonId", "type": "CustomRadioButton", "visible": True}
liveScreenAddPatientDigoxinNoButton = { "container": mainWindow, "id": "digoxinNoButtonId", "type": "CustomRadioButton", "visible": True}
liveScreenAddPatientSaveButton = { "container": mainWindow, "id": "savePatientButtonId", "type": "CircularButton", "visible": True}
liveScreenAddPatientCancelButton = { "container": mainWindow, "id": "cancelPatientButtonId", "type": "CircularButton", "visible": True}
liveScreenAddPatientCloseButton = {"container": mainWindow, "id": "closePatientDialogButtonId", "type": "CloseDialogButton", "visible": True}
liveScreenAddPatientCancelPopUpMessage = {"container": mainWindow, "id": "warningMessageId", "type": "Label", "visible": True}
liveScreenAddPatientPopUpConfirmButton = { "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "visible": True}
liveScreenAddPatientPopUpCancelButton = { "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton", "visible": True}


livePatientDialogErrorPopUp = {"container": mainWindow, "id": "patientDialogError", "type": "ErrorPopup", "visible": True}
livePatientDialogErrorMessage = {"container": mainWindow, "text": "Patient ID already exists!!", "type": "Text", "visible": True}
livePatientDialogErrorOkButton = { "container": mainWindow, "id": "okButtonId", "type": "Button", "visible": True}
liveScreenPatientRecord = {"container": liveScreenPatientListView, "id": "outlineId", "type": "Rectangle", "visible": True}
liveScreenInfoButton = {"container": mainWindow, "type": "PatientInfoButton", "visible": True}

nameSortButton = { "container": mainWindow, "id": "nameSortButtonId", "type": "SortingButton", "unnamed": 1, "visible": True}
idSortButton = { "container": mainWindow, "id": "patientidSortButtonId", "type": "SortingButton", "unnamed": 1, "visible": True}
lastExamSortButton = { "container": mainWindow, "id": "lastrecordDateTimeSortButtonId", "type": "SortingButton", "unnamed": 1, "visible": True}

liveScreenAddPatientSurnameInput7Inch = {  "container": mainWindow, "id": "surnameFieldId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientFirstNameInput7Inch = {  "container": mainWindow, "id": "firstnameFieldId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientTitleInput7Inch = {  "container": mainWindow, "id": "titleFieldId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientDOBInput7Inch = {"container": mainWindow, "id": "dobFieldId", "type": "DateOfBirthEntry", "visible": True}
liveScreenAddPatientAgeInput7Inch = {  "container": mainWindow, "id": "ageFieldId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientIdInput7Inch = {  "container": mainWindow, "id": "patientIdFieldId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientHospitalIdInput7Inch = {  "container": mainWindow, "id": "hospitalIdFieldId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientWeightInput7Inch = {  "container": mainWindow, "id": "weightFieldId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientHeightInput7Inch = {  "container": mainWindow, "id": "heightFieldId", "type": "PatientInfoField", "visible": True}
liveScreenAddPatientSaveButton7Inch = { "container": mainWindow, "id": "saveButtonId", "type": "CircularButton", "visible": True}
textId7Inch = {  "container": mainWindow, "id": "textId", "type": "TextField", "visible": True}


# Function to navigate to live add patient screen from patient List screen
def closeThePatientListScreen():
    try:
        if waitForObject(liveScreenPatientCloseButton):
            mouseClick(waitForObject(liveScreenPatientCloseButton))
            snooze(1)
            if waitForObject(mainWindow):
                test.log("Successfully live screen is displayed")
            else:
                test.fail("Live screen is not displayed")
               
        return True  
       
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to navigate to patients screen from Live screen
def navigateToPatientListScreenFromLive():
    try:
        snooze(2)
        if waitForObject(liveScreenPatientListButton):
            mouseClick(waitForObject(liveScreenPatientListButton))
            snooze(1)
            if waitForObject(liveScreenPatientAddButton):
                test.log("Patients screen is displayed successfully")
                return True
            else:
                test.fail("Patients screen is not displayed ")
                return False
                         
    except Exception as e:
        test.fail(str(e))

# Function to add a new patient in patient list screen
def addNewPatientInPatientListScreen(Surname="", Firstname="", Title="", PatientDOB="", PatientAge="", PatientId="", HospitalId="", Weight="", Height="", Gender="", PaceMaker="", Digoxin=""):
    try:
        snooze(2)
        if waitForObject(liveScreenPatientAddButton):
            mouseClick(waitForObject(liveScreenPatientAddButton))                                      
            if waitForObject(liveScreenAddPatientSurnameInput):
                    setFocusTextBox(liveScreenAddPatientSurnameInput)
                    type(mainWindow, Surname)
                    # type(waitForObject(liveScreenAddPatientSurnameInput), Surname)
                    snooze(1)
            if waitForObject(liveScreenAddPatientFirstNameInput):
                    setFocusTextBox(liveScreenAddPatientFirstNameInput)
                    type(mainWindow, Firstname)
                    # type(waitForObject(liveScreenAddPatientFirstNameInput), Firstname)
                    snooze(1)            

            if waitForObject(liveScreenAddPatientTitleInput):
                    setFocusTextBox(liveScreenAddPatientTitleInput)
                    type(mainWindow, Title)
                    # type(waitForObject(liveScreenAddPatientTitleInput), Title)
                    snooze(1)
               
            if waitForObject(liveScreenAddPatientDOBInput):
                    setFocusTextBox(liveScreenAddPatientDOBInput)
                    type(mainWindow, PatientDOB)
                    # type(waitForObject(liveScreenAddPatientDOBInput), PatientDOB)
                    snooze(1)
                # Handling 'system can not handle date of birth / out of range' scenario
                    type(mainWindow, "<Tab>")       
                    if (object.exists(livePatientDialogErrorOkButton)):
                        mouseClick(waitForObject(livePatientDialogErrorOkButton))
                        snooze(1)
       
            if (object.exists(livePatientDialogErrorOkButton)):
                    mouseClick(waitForObject(livePatientDialogErrorOkButton))
                    snooze(1)                
            else: 
                if waitForObject(liveScreenAddPatientIdInput):
                    setFocusTextBox(liveScreenAddPatientIdInput)
                    type(mainWindow, PatientId)
                    
                # Handling Patient Id already exists dialog
                type(mainWindow, "<Tab>")       
                if (object.exists(livePatientDialogErrorOkButton)):
                    mouseClick(waitForObject(livePatientDialogErrorOkButton))
                snooze(1)
#             if(productCode=='lx'): 
#                 if waitForObject(liveScreenAddPatientHospitalIdInput7Inch):
#                     setFocusTextBox(liveScreenAddPatientHospitalIdInput7Inch)
#                     type(mainWindow, HospitalId)
#                     snooze(.5)  
#                     mouseClick(waitForObject(liveScreenAddPatientSaveButton7Inch))
#                     snooze(.5)
#                 if (object.exists(livePatientDialogErrorOkButton)):
#                     mouseClick(waitForObject(livePatientDialogErrorOkButton))
#                     snooze(1)                
#             else: 
#                 if waitForObject(liveScreenAddPatientHospitalIdInput):
#                     setFocusTextBox(liveScreenAddPatientHospitalIdInput)
#                     type(mainWindow, HospitalId)
#                     
#                 # Handling Hospital Id already exists dialog
#                 type(mainWindow, "<Tab>")       
#                 if (object.exists(livePatientDialogErrorOkButton)):
#                     mouseClick(waitForObject(livePatientDialogErrorOkButton))
#                 snooze(1)

            
            if Gender:
                value = Gender.strip()
                upper = value.upper()
                
                if upper == "MALE":
                    mouseClick(waitForObject(liveScreenAddPatientMaleRadioButton))
                
                elif upper == "FEMALE":
                    mouseClick(waitForObject(liveScreenAddPatientFemaleRadioButton))
                
                elif upper == "OTHER":
                    mouseClick(waitForObject(liveScreenAddPatientOthersRadioButton))
                                        
    
                if waitForObject(liveScreenAddPatientWeightInput):
                    setFocusTextBox(liveScreenAddPatientWeightInput)
                    type(mainWindow, Weight)
                                    
                    # type(waitForObject(liveScreenAddPatientWeightInput), Weight)
                    snooze(1)
                if waitForObject(liveScreenAddPatientHeightInput):
                    setFocusTextBox(liveScreenAddPatientHeightInput)
                    type(mainWindow, Height)                
                    # type(waitForObject(liveScreenAddPatientHeightInput), Height)
                    snooze(1)
 
                if PaceMaker:
                    value = PaceMaker.strip()
                    upper = value.upper()
                    
                    if upper == "YES":
                        mouseClick(waitForObject(liveScreenAddPatientPaceMakeYesButton))
                    
                    elif upper == "NO":
                        mouseClick(waitForObject(liveScreenAddPatientPaceMakeNoButton))
                    
                    else:
                        pass

                if Digoxin:
                    value = Digoxin.strip()
                    upper = value.upper()
                    
                    if upper == "YES":
                        mouseClick(waitForObject(liveScreenAddPatientDigoxinYesButton))
                    
                    elif upper == "NO":
                        mouseClick(waitForObject(liveScreenAddPatientDigoxinNoButton))
                    
                    else:
                        pass            
        
        mouseClick(waitForObject(liveScreenAddPatientSaveButton))
        return True
                
    except Exception as e:
        test.fail("Exception" + str(e)) 
   
#Function to save edited details in patient card
def savePatiententineditPatientScreen():
    try:
        status=False
        if object.exists(liveScreenAddPatientSaveButton):
            mouseClick(waitForObject(liveScreenAddPatientSaveButton))
            status=True
            
        return True if status==True else False
                
    except Exception as e:
        test.fail("Exception" + str(e))   
   
   
   
   
   
        
def SearchPatientinPatientCard(pid):
    try:
        if object.exists(liveScreenPatientSearchInput):
            searchBox = (waitForObject(liveScreenPatientSearchInput))
            snooze(1)
            
            type(waitForObject(liveScreenPatientSearchInput), pid)
            snooze(2)
            parent = waitForObject(liveScreenPatientListView)
            child = object.children(parent)
            child_1 = object.children(child[0])
            
            for i in child_1:
                child_2 = object.children(i)
                if len(child_2) > 0:
                    child_3 = object.children(child_2[0])
                    value = child_3[1].text
                    
                    if str(value) == pid:
                        mouseClick(child_2[0])
                        test.log("Successfully saved the patient details in the live patient list screen")
                        return True
                    else:
                        test.fail("The patient details are not saved in the live patient list screen")
                        return False
        
    except Exception as e:
        test.fail("Exception" + str(e))
            
        
              
        
# Function to save the patient details after adding the patient details in patient list screen and clicking on respective item for examination
def savePatientAndVerifyInPatientListScreen(pid):
    try:
        if waitForObject(liveScreenAddPatientSaveButton):
            mouseClick(waitForObject(liveScreenAddPatientSaveButton))
            
            mouseClick(waitForObject(liveScreenPatientListButton))
            searchBox = (waitForObject(liveScreenPatientSearchInput))
            snooze(1)
            searchBox.text = ""
            snooze(1)
            type(waitForObject(liveScreenPatientSearchInput), pid)
            snooze(2)
            parent = waitForObject(liveScreenPatientListView)
            child = object.children(parent)
            child_1 = object.children(child[0])
            
            for i in child_1:
                child_2 = object.children(i)
                if len(child_2) > 0:
                    child_3 = object.children(child_2[0])
                    value = child_3[1].text
                    
                    if str(value) == pid:
                        mouseClick(child_2[0])
                        test.log("Successfully saved the patient details in the live patient list screen")
                        return True
                    else:
                        test.fail("The patient details are not saved in the live patient list screen")
                        return False
        
    except Exception as e:
        test.fail("Exception" + str(e))

# Function to verify patient details in patient list screen and clicking on respective item for examination
def verifyPatientRecordInPatientListScreenAndSelect(pid):
    try:
        snooze(2)
        if waitForObject(liveScreenPatientListButton):
            mouseClick(waitForObject(liveScreenPatientListButton))
            searchBox = (waitForObject(liveScreenPatientSearchInput))
            snooze(1)
            searchBox.text = ""
            snooze(1)
            type(waitForObject(liveScreenPatientSearchInput), pid)
            snooze(2)
            parent = waitForObject(liveScreenPatientListView)
            child = object.children(parent)
            child_1 = object.children(child[0])
            
            for i in child_1:
                child_2 = object.children(i)
                if len(child_2) > 0:
                    child_3 = object.children(child_2[0])
                    value = child_3[1].text
                    
                    if str(value) == pid:
                        mousePress(child_2[0])
                        snooze(0.10)
                        mouseRelease(child_2[0])
                        snooze(0.10)
                        test.log("Successfully saved the patient details in the patient list screen and select the same patient")
                        return True
                    else:
                        test.fail("The patient details are not saved in the live patient list screen")
                        return False
        
    except Exception as e:
        test.fail("Exception" + str(e))
                
        
# Function to cancel the patient details in live add patient list screen
def cancelForAddingAPatientInPatientListScreen(pid):
    try:
        if waitForObject(liveScreenAddPatientCancelButton):
            mouseClick(waitForObject(liveScreenAddPatientCancelButton))
            snooze(0.5)
            cancelWarningMessage = str(waitForObject(liveScreenAddPatientCancelPopUpMessage).text)
            textMessage = "Do you want to close the window without saving the changes?"
            if cancelWarningMessage == textMessage:
                mouseClick(waitForObject(liveScreenAddPatientPopUpConfirmButton))
                searchBox = (waitForObject(liveScreenPatientSearchInput))
                searchBox.text = ""
                type(waitForObject(liveScreenPatientSearchInput), pid)
                snooze(0.5)
                if waitForObject(liveScreenPatientRecord):
                    test.fail("Patient details in the  patient list screen is not cancelled and it is saved")
                else:
                    test.log("The patient details is cancelled in the  patient list screen")
            else:
                mouseClick(waitForObject(liveScreenAddPatientPopUpCancelButton))
                test.fail("Warning message in pop up : " + cancelWarningMessage)


        return True
         
    except Exception as e:
        test.fail("Exception : " + str(e)) 
        
        
# Function to close the live add new patient list screen
def closeTheLiveAddPatientScreenInPatientListScreen(pid):
    try:
        if waitForObject(liveScreenAddPatientCloseButton):
            mouseClick(waitForObject(liveScreenAddPatientCloseButton))
            snooze(0.5)
            cancelWarningMessage = str(waitForObject(liveScreenAddPatientCancelPopUpMessage).text)
            textMessage = "Do you want to close the window without saving the changes?"
            if cancelWarningMessage == textMessage:
                mouseClick(waitForObject(liveScreenAddPatientPopUpConfirmButton))
                searchBox = (waitForObject(liveScreenPatientSearchInput))
                searchBox.text = ""
                type(waitForObject(liveScreenPatientSearchInput), pid)
                snooze(0.5)
                if waitForObject(liveScreenPatientRecord):
                    test.fail("The live add patient list screen is not closed")
                else:
                    test.log("The live add patient list screen is closed")
            else:
                mouseClick(waitForObject(liveScreenAddPatientPopUpCancelButton))
                test.fail("Warning message in pop up : " + cancelWarningMessage)

        return True
        
    except Exception as e:
        test.fail("Exception" + str(e))        
    
# Function to Search  and select the patient details
def searchAndSelectPatientInLivePatientListScreen(pid):
    try:
        if waitForObject(liveScreenPatientSearchInput):
            searchBox = (waitForObject(liveScreenPatientSearchInput))
            searchBox.text = ""
            snooze(1)
            type(waitForObject(liveScreenPatientSearchInput), pid)
            snooze(2)
            parent = waitForObject(liveScreenPatientListView)
            child = object.children(parent)
            child_1 = object.children(child[0])
            
            for i in child_1:
                child_2 = object.children(i)
                if len(child_2) > 0:
                    child_3 = object.children(child_2[0])
                    value = child_3[1].text
                    test.log("value=%s" % value)
                    if str(value) == pid:
                        mouseClick(child_3[1])
                        test.log("Successfully searched and selected the given patient")
            
        return True
    
    except Exception as e:
        test.fail("Exception" + str(e))    
        
# Function to Search the patient details
def searchPatientInLivePatientListScreen(pid):
    try:
        if waitForObject(liveScreenPatientSearchInput):
            searchBox = (waitForObject(liveScreenPatientSearchInput))
            snooze(1)
            searchBox.text = ""
            snooze(1)
            type(waitForObject(liveScreenPatientSearchInput), pid)
            snooze(2)
            test.log("Successfully searched the given patient")
            
        return True
    
    except Exception as e:
        test.fail("Exception" + str(e))   
        
# Function to select the patient details
def selectPatientInLivePatientListScreen(pid):
    try:
        if waitForObject(liveScreenPatientSearchInput):
            parent = waitForObject(liveScreenPatientListView)
            child = object.children(parent)
            child_1 = object.children(child[0])
            
            for i in child_1:
                child_2 = object.children(i)
                if len(child_2) > 0:
                    child_3 = object.children(child_2[0])
                    value = child_3[1].text
                    test.log("value=%s" % value)
                    if str(value) == pid:
                        mouseClick(child_3[1])
                        test.log("Successfully searched and selected the given patient")
            
        return True
    
    except Exception as e:
        test.fail("Exception" + str(e))    
         
# Function to search the patient to edit the patient details in the patient list screen
def searchThePatientToEditThePatientDetailsInPatientListScreen(pid):
    try:
        if waitForObject(liveScreenPatientSearchInput):
            searchBox = (waitForObject(liveScreenPatientSearchInput))
            searchBox.text = ""
            type(waitForObject(liveScreenPatientSearchInput), pid)
            parent = waitForObject(liveScreenPatientListView)
            child = object.children(parent)
            child_1 = object.children(child[0])
            
            for i in child_1:
                child_2 = object.children(i)
                if len(child_2) > 0:
                    child_3 = object.children(child_2[0])
                    value = child_3[1].text
                    test.log("value=%s" % value)
                    
                    if (value == pid):
                        test.log("The given pid is matching with the patient's pid in the list")
                        mouseClick(waitForObject(liveScreenInfoButton))
                        test.log("Successfully clicked on info button")
                        PatientIdInput = (waitForObject(liveScreenAddPatientIdInput))
                                
                        if PatientIdInput.text == pid :
                            test.log("Successfully navigated to the patient details screen with patient id " + pid + " in the live patient list screen")
                        else:
                            test.fail("Does not navigated to the patient details screen with patient id " + pid + " in the live patient list screen")
                    else:
                        test.fail("Edit patient details screen is not displayed")
                        
        return True
    
    except Exception as e:
        test.fail("Exception: " + str(e))
        
# Function to edit the patient details in patient list screen
def editPatientDetailsInPatientListScreen(Surname="", Firstname="", Title="", PatientDOB="", PatientAge="", PatientId="", HospitalId="", Weight="", Height="", Gender="", PaceMaker="", Digoxin=""):
    try:
        if Surname:
            if waitForObject(liveScreenAddPatientSurnameInput):
                surnameInput = (waitForObject(liveScreenAddPatientSurnameInput))
                snooze(1)
                surnameInput.text = ""
                type(waitForObject(liveScreenAddPatientSurnameInput), Surname)
                snooze(1)
                changedSurname = waitForObject(liveScreenAddPatientSurnameInput)
                
                if changedSurname.text == Surname :
                    test.log("Successfully changed the surname")
                
                else:
                    test.fail("Surname is not changed")
                           
        if Firstname:
            if waitForObject(liveScreenAddPatientFirstNameInput):
                firstNameInput = (waitForObject(liveScreenAddPatientFirstNameInput))
                snooze(1)
                firstNameInput.text = ""
                type(waitForObject(liveScreenAddPatientFirstNameInput), Firstname)
                snooze(1)
                changedFirstname = waitForObject(liveScreenAddPatientFirstNameInput)
                
                if changedFirstname.text == Firstname :
                    test.log("Successfully changed the firstname")
                
                else:
                    test.fail("Firstname is not changed")                
        
        if Title:
            if waitForObject(liveScreenAddPatientTitleInput):
                TitleInput = (waitForObject(liveScreenAddPatientTitleInput))
                snooze(1)
                TitleInput.text = ""
                type(waitForObject(liveScreenAddPatientTitleInput), Title)
                snooze(1)
                changedTitle = waitForObject(liveScreenAddPatientTitleInput)
                
                if changedTitle.text == Title :
                    test.log("Successfully changed the title")
                
                else:
                    test.fail("Title is not changed")
                            
        '''if PatientDOB:
            if waitForObject(liveScreenAddPatientDOBInput):
                DOBInput =(waitForObject(liveScreenAddPatientDOBInput))
                snooze(1)
                DOBInput.text=""
                dateOfBirth = findObject(liveScreenAddPatientDOBInput)
                parent=object.parent(dateOfBirth)
                mouseClick(parent)
                type(waitForObject(liveScreenAddPatientDOBInput),PatientDOB)
                snooze(1)
                test.log("Successfully changed the patient's date of birth")'''
        
        if PatientAge:
            if waitForObject(liveScreenAddPatientAgeInput):
                AgeInput = (waitForObject(liveScreenAddPatientAgeInput))
                snooze(1)
                AgeInput.text = ""
                type(waitForObject(liveScreenAddPatientAgeInput), PatientAge)
                snooze(1)
                changedPatientAge = waitForObject(liveScreenAddPatientAgeInput)
                
                if changedPatientAge.text == PatientAge :
                    test.log("Successfully changed the patient's age")
                
                else:
                    test.fail("Patient's age is not changed")
                            
        if PatientId:
            if waitForObject(liveScreenAddPatientIdInput):
                PatientIdInput = (waitForObject(liveScreenAddPatientIdInput))
                snooze(1)
                PatientIdInput.text = ""
                type(waitForObject(liveScreenAddPatientIdInput), PatientId)
                snooze(1)
                changedPatientId = waitForObject(liveScreenAddPatientIdInput)
                
                if changedPatientId.text == PatientId :
                    test.log("Successfully changed the patient's id")
                
                else:
                    test.fail("Patient's id is not changed")
                    
        if HospitalId:
            if waitForObject(liveScreenAddPatientHospitalIdInput):
                HospitalIdInput = (waitForObject(liveScreenAddPatientHospitalIdInput))
                snooze(1)
                HospitalIdInput.text = ""
                type(waitForObject(liveScreenAddPatientHospitalIdInput), HospitalId)
                snooze(1)
                changedHospitalId = waitForObject(liveScreenAddPatientHospitalIdInput)
                
                if changedHospitalId.text == HospitalId :
                    test.log("Successfully changed the hospital id")
                
                else:
                    test.fail("Hospital id is not changed")
                            
        if Gender:
            value = Gender.strip()
            upper = value.upper()
            
            if upper == "MALE":
                mouseClick(waitForObject(liveScreenAddPatientMaleRadioButton))
                test.log("Successfully changed the gender to male")
            
            elif upper == "FEMALE":
                mouseClick(waitForObject(liveScreenAddPatientFemaleRadioButton))
                test.log("Successfully changed the gender to female")
            
            elif upper == "OTHER":
                mouseClick(waitForObject(liveScreenAddPatientOthersRadioButton))
                test.log("Successfully changed the gender to other")
                
            else:
                test.fail("Gender is not changed")
                               
        if Weight:
            if waitForObject(liveScreenAddPatientWeightInput):
                WeightInput = (waitForObject(liveScreenAddPatientWeightInput))
                snooze(1)
                WeightInput.text = ""
                type(waitForObject(liveScreenAddPatientWeightInput), Weight)
                snooze(1)
                changedWeight = waitForObject(liveScreenAddPatientWeightInput)
                
                if changedWeight.text == Weight :
                    test.log("Successfully changed the patient's weight")
                
                else:
                    test.fail("Patient's weight is not changed")
                    
        if Height:
            if waitForObject(liveScreenAddPatientHeightInput):
                HeightInput = (waitForObject(liveScreenAddPatientHeightInput))
                snooze(1)
                HeightInput.text = ""
                type(waitForObject(liveScreenAddPatientHeightInput), Height)
                snooze(1)
                changedHeight = waitForObject(liveScreenAddPatientHeightInput)
                
                if changedHeight.text == Height :
                    test.log("Successfully changed the patient's height")
                
                else:
                    test.fail("Patient's height is not changed")
                        
        if PaceMaker:
            value = PaceMaker.strip()
            upper = value.upper()
            
            if upper == "YES":
                mouseClick(waitForObject(liveScreenAddPatientPaceMakeYesButton))
                test.log("Successfully changed the pacemaker to yes")
            
            elif upper == "NO":
                mouseClick(waitForObject(liveScreenAddPatientPaceMakeNoButton))
                test.log("Successfully changed the pacemaker to no")
            
            else:
                test.fail("Pacemaker is not changed")
                        
        if Digoxin:
            value = Digoxin.strip()
            upper = value.upper()
            
            if upper == "YES":
                mouseClick(waitForObject(liveScreenAddPatientDigoxinYesButton))
                test.log("Successfully changed the digoxin to yes")
            
            elif upper == "NO":
                mouseClick(waitForObject(liveScreenAddPatientDigoxinNoButton))
                test.log("Successfully changed the digoxin to no")
            
            else:
                test.fail("Digoxin is not changed")
                
        return True
    
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to save the patient details after editing the patient details in live add patient list screen
def saveForEditingThePatientInPatientListScreen(Surname="", Firstname="", Title="", PatientAge="", PatientId="", HospitalId="", Weight="", Height=""):
    try:
        if waitForObject(liveScreenAddPatientSaveButton):
            mouseClick(waitForObject(liveScreenAddPatientSaveButton))
            
            mouseClick(waitForObject(liveScreenPatientListButton))
            searchBox = (waitForObject(liveScreenPatientSearchInput))
            snooze(1)
            searchBox.text = ""
            snooze(1)
            type(waitForObject(liveScreenPatientSearchInput), PatientId)
            snooze(2)
            parent = waitForObject(liveScreenPatientListView)
            child = object.children(parent)
            child_1 = object.children(child[0])
            
            for i in child_1:
                child_2 = object.children(i)
                if len(child_2) > 0:
                    child_3 = object.children(child_2[0])
                    value = child_3[1].text
                    test.log("value=%s" % value)
                    
                    if str(value) == PatientId:
                        mouseClick(waitForObject(liveScreenInfoButton))
                        test.log("Successfully clicked on info button")
                        
                        if Surname:
                            if waitForObject(liveScreenAddPatientSurnameInput):
                                surnameInput = (waitForObject(liveScreenAddPatientSurnameInput))
                                
                                if surnameInput.text == Surname :
                                    test.log("Successfully edited and saved the surname in the live patient list screen")
                                
                                else:
                                    test.fail("Surname is not edited and it is not saved in the live patient list screen")
                                    
                        if Firstname:
                            if waitForObject(liveScreenAddPatientFirstNameInput):
                                firstNameInput = (waitForObject(liveScreenAddPatientFirstNameInput))
                                
                                if firstNameInput.text == Firstname :
                                    test.log("Successfully edited and saved the firstname in the live patient list screen")
                                
                                else:
                                    test.fail("Firstname is not edited and it is not saved in the live patient list screen")                
                        
                        if Title:
                            if waitForObject(liveScreenAddPatientTitleInput):
                                TitleInput = (waitForObject(liveScreenAddPatientTitleInput))
                                
                                if TitleInput.text == Title :
                                    test.log("Successfully edited and saved the title in the live patient list screen")
                                
                                else:
                                    test.fail("Title is not edited and it is not saved in the live patient list screen")
                                            
                        if PatientAge:
                            if waitForObject(liveScreenAddPatientAgeInput):
                                AgeInput = (waitForObject(liveScreenAddPatientAgeInput))
                                
                                if  AgeInput.text == PatientAge :
                                    test.log("Successfully edited and saved the title in the live patient list screen")
                                
                                else:
                                    test.fail("Patient's age is not edited and it is not saved in the live patient list screen")
                                            
                        if PatientId:
                            if waitForObject(liveScreenAddPatientIdInput):
                                PatientIdInput = (waitForObject(liveScreenAddPatientIdInput))
                                
                                if PatientIdInput.text == PatientId :
                                    test.log("Successfully edited and saved the patient's id in the live patient list screen")
                                
                                else:
                                    test.fail("Patient's id is not edited and it is not saved in the live patient list screen")
                                    
                        if HospitalId:
                            if waitForObject(liveScreenAddPatientHospitalIdInput):
                                HospitalIdInput = (waitForObject(liveScreenAddPatientHospitalIdInput))
                                
                                if HospitalIdInput.text == HospitalId :
                                    test.log("Successfully edited and saved the hospital id in the live patient list screen")
                                
                                else:
                                    test.fail("Hospital id is not edited and it is not saved in the live patient list screen")
                                               
                        if Weight:
                            if waitForObject(liveScreenAddPatientWeightInput):
                                WeightInput = (waitForObject(liveScreenAddPatientWeightInput))
                                
                                if WeightInput.text == Weight :
                                    test.log("Successfully edited and saved the patient's weight in the live patient list screen")
                                
                                else:
                                    test.fail("Patient's weight is not edited and it is not saved in the live patient list screen")
                                    
                        if Height:
                            if waitForObject(liveScreenAddPatientHeightInput):
                                HeightInput = (waitForObject(liveScreenAddPatientHeightInput))
                                
                                if HeightInput.text == Height :
                                    test.log("Successfully edited and saved the patient's height in the live patient list screen")
                                
                                else:
                                    test.fail("Patient's height is not edited and it is not saved in the live patient list screen")
                                
            return True 
    
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to get the values of patient details in patient list screen
def gettingTheDetailsOfPatientsInPatientListScreen():
    try:
        if waitForObject(liveScreenAddPatientSurnameInput):
            global surnameInput
            surnameInput = str(waitForObject(liveScreenAddPatientSurnameInput).text)
            test.log("surnameInput=%s" % surnameInput)
            
        if waitForObject(liveScreenAddPatientFirstNameInput):
            global firstNameInput
            firstNameInput = str(waitForObject(liveScreenAddPatientFirstNameInput).text)
            test.log("firstNameInput=%s" % firstNameInput)
            
        if waitForObject(liveScreenAddPatientTitleInput):
            global TitleInput
            TitleInput = (waitForObject(liveScreenAddPatientTitleInput).text)
            test.log("TitleInput=%s" % TitleInput)
            
        if waitForObject(liveScreenAddPatientAgeInput):
            global AgeInput
            AgeInput = (waitForObject(liveScreenAddPatientAgeInput).text)
            test.log("AgeInput=%s" % AgeInput)
            
        if waitForObject(liveScreenAddPatientIdInput):
            global PatientIdInput
            PatientIdInput = (waitForObject(liveScreenAddPatientIdInput).text)
            test.log("PatientIdInput=%s" % PatientIdInput)
            
        if waitForObject(liveScreenAddPatientHospitalIdInput):
            global HospitalIdInput
            HospitalIdInput = (waitForObject(liveScreenAddPatientHospitalIdInput).text)
            test.log("HospitalIdInput=%s" % HospitalIdInput)
            
        if waitForObject(liveScreenAddPatientWeightInput):
            global WeightInput
            WeightInput = (waitForObject(liveScreenAddPatientWeightInput).text)
            test.log("WeightInput=%s" % WeightInput)
            
        if waitForObject(liveScreenAddPatientHeightInput):
            global HeightInput
            HeightInput = (waitForObject(liveScreenAddPatientHeightInput).text)
            test.log("HeightInput=%s" % HeightInput)
            
        return surnameInput, firstNameInput, TitleInput, AgeInput, PatientIdInput, HospitalIdInput, WeightInput, HeightInput
    
    
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to cancel the changes after editing the patient's record in patient list screen
def cancelForEditingThePatientInPatientListScreen(Surname="", Firstname="", Title="", PatientAge="", PatientId="", HospitalId="", Weight="", Height=""):
    try:
        if waitForObject(liveScreenAddPatientCancelButton):
            mouseClick(findObject(liveScreenAddPatientCancelButton))
            
            cancelWarningMessage = str(waitForObject(liveScreenAddPatientCancelPopUpMessage).text)
            textMessage = "Do you want to close the window without saving the changes?"
            if cancelWarningMessage == textMessage:
                mouseClick(waitForObject(liveScreenAddPatientPopUpConfirmButton))
                searchBox = (waitForObject(liveScreenPatientSearchInput))
                searchBox.text = ""
                type(waitForObject(liveScreenPatientSearchInput), PatientId)
                snooze(0.5)
                parent = waitForObject(liveScreenPatientListView)
                child = object.children(parent)
                child_1 = object.children(child[0])
                
                for i in child_1:
                    child_2 = object.children(i)
                    if len(child_2) > 0:
                        child_3 = object.children(child_2[0])
                        value = child_3[1].text
                        test.log("value=%s" % value)
                        
                        if (value == PatientId):
                            test.log("The given pid is matching with the patient's pid in the list")
                            mouseClick(waitForObject(liveScreenInfoButton))
                            test.log("Successfully clicked on info button")
                            
                            if waitForObject(liveScreenAddPatientSurnameInput):
                                newSurnameInput = str(waitForObject(liveScreenAddPatientSurnameInput).text)
                                test.log("newSurnameInput=%s" % newSurnameInput)
                                
                            if waitForObject(liveScreenAddPatientFirstNameInput):
                                newFirstNameInput = str(waitForObject(liveScreenAddPatientFirstNameInput).text)
                                test.log("newFirstNameInput=%s" % newFirstNameInput)
                                
                            if waitForObject(liveScreenAddPatientTitleInput):
                                newTitleInput = (waitForObject(liveScreenAddPatientTitleInput).text)
                                test.log("newTitleInput=%s" % newTitleInput)
                                
                            if waitForObject(liveScreenAddPatientAgeInput):
                                newAgeInput = (waitForObject(liveScreenAddPatientAgeInput).text)
                                test.log("newAgeInput=%s" % newAgeInput)
                                
                            if waitForObject(liveScreenAddPatientIdInput):
                                newPatientIdInput = (waitForObject(liveScreenAddPatientIdInput).text)
                                test.log("newPatientIdInput=%s" % newPatientIdInput)
                                
                            if waitForObject(liveScreenAddPatientHospitalIdInput):
                                newHospitalIdInput = (waitForObject(liveScreenAddPatientHospitalIdInput).text)
                                test.log("newHospitalIdInput=%s" % newHospitalIdInput)
                                
                            if waitForObject(liveScreenAddPatientWeightInput):
                                newWeightInput = (waitForObject(liveScreenAddPatientWeightInput).text)
                                test.log("newWeightInput=%s" % newWeightInput)
                                
                            if waitForObject(liveScreenAddPatientHeightInput):
                                newHeightInput = (waitForObject(liveScreenAddPatientHeightInput).text)
                                test.log("newHeightInput=%s" % newHeightInput)
                                
                            if Surname == newSurnameInput and Firstname == newFirstNameInput and Title == newTitleInput and PatientAge == newAgeInput and PatientId == newPatientIdInput and HospitalId == newHospitalIdInput and Weight == newWeightInput and Height == newHeightInput:
                                    test.log("Successfully cancelled the values after editing the patient details in patient list screen")
                            else:
                                test.fail("Values are not cancelled after editing the patient details in patient list screen")
            
    except Exception as e:
        test.fail("Exception" + str(e))
                
# Function to edit and save the patient details in patient list screen
def editAndSaveThePatientDetailsInPatientListScreen(Surname="", Firstname="", Title="", PatientDOB="", PatientAge="", PatientId="", HospitalId="", Weight="", Height="", Gender="", PaceMaker="", Digoxin=""):
    try:
        if Surname:
            if waitForObject(liveScreenAddPatientSurnameInput):
                surnameInput = (waitForObject(liveScreenAddPatientSurnameInput))
                snooze(1)
                surnameInput.text = ""
                type(waitForObject(liveScreenAddPatientSurnameInput), Surname)
                snooze(1)
                changedSurname = waitForObject(liveScreenAddPatientSurnameInput)
                
                if changedSurname.text == Surname :
                    test.log("Successfully changed the surname")
                
                else:
                    test.fail("Surname is not changed")
       
        if Firstname:
            if waitForObject(liveScreenAddPatientFirstNameInput):
                firstNameInput = (waitForObject(liveScreenAddPatientFirstNameInput))
                snooze(1)
                firstNameInput.text = ""
                type(waitForObject(liveScreenAddPatientFirstNameInput), Firstname)
                snooze(1)
                changedFirstname = waitForObject(liveScreenAddPatientFirstNameInput)
                
                if changedFirstname.text == Firstname :
                    test.log("Successfully changed the firstname")
                
                else:
                    test.fail("Firstname is not changed")
                    
        if Title:
            if waitForObject(liveScreenAddPatientTitleInput):
                TitleInput = (waitForObject(liveScreenAddPatientTitleInput))
                snooze(1)
                TitleInput.text = ""
                type(waitForObject(liveScreenAddPatientTitleInput), Title)
                snooze(1)
                changedTitle = waitForObject(liveScreenAddPatientTitleInput)
                
                if changedTitle.text == Title :
                    test.log("Successfully changed the title")
                
                else:
                    test.fail("Title is not changed")
        
        '''if PatientDOB:
            if waitForObject(liveScreenAddPatientDOBInput):
                DOBInput =(waitForObject(liveScreenAddPatientDOBInput))
                snooze(1)
                DOBInput.text=""
                dateOfBirth = findObject(liveScreenAddPatientDOBInput)
                parent=object.parent(dateOfBirth)
                mouseClick(parent)
                type(waitForObject(liveScreenAddPatientDOBInput),PatientDOB)
                snooze(1)
                test.log("Successfully changed the patient's date of birth")
                
                return True'''
        
        if PatientAge:
            if waitForObject(liveScreenAddPatientAgeInput):
                AgeInput = (waitForObject(liveScreenAddPatientAgeInput))
                snooze(1)
                AgeInput.text = ""
                type(waitForObject(liveScreenAddPatientAgeInput), PatientAge)
                snooze(1)
                changedPatientAge = waitForObject(liveScreenAddPatientAgeInput)
                
                if changedPatientAge.text == PatientAge :
                    test.log("Successfully changed the patient's age")
                
                else:
                    test.fail("Patient's age is not changed")
        
        if PatientId:
            if waitForObject(liveScreenAddPatientIdInput):
                PatientIdInput = (waitForObject(liveScreenAddPatientIdInput))
                snooze(1)
                PatientIdInput.text = ""
                type(waitForObject(liveScreenAddPatientIdInput), PatientId)
                snooze(1)
                changedPatientId = waitForObject(liveScreenAddPatientIdInput)
                
                if changedPatientId.text == PatientId :
                    test.log("Successfully changed the patient's id")
                
                else:
                    test.fail("Patient's id is not changed")

        if HospitalId:
            if waitForObject(liveScreenAddPatientHospitalIdInput):
                HospitalIdInput = (waitForObject(liveScreenAddPatientHospitalIdInput))
                snooze(1)
                HospitalIdInput.text = ""
                type(waitForObject(liveScreenAddPatientHospitalIdInput), HospitalId)
                snooze(1)
                changedHospitalId = waitForObject(liveScreenAddPatientHospitalIdInput)
                
                if changedHospitalId.text == HospitalId :
                    test.log("Successfully changed the hospital id")
                
                else:
                    test.fail("Hospital id is not changed")
        
        if Gender:
            value = Gender.strip()
            upper = value.upper()
            
            if upper == "MALE":
                mouseClick(waitForObject(liveScreenAddPatientMaleRadioButton))
                test.log("Successfully changed the gender to male")
            
            elif upper == "FEMALE":
                mouseClick(waitForObject(liveScreenAddPatientFemaleRadioButton))
                test.log("Successfully changed the gender to female")
            
            elif upper == "OTHER":
                mouseClick(waitForObject(liveScreenAddPatientOthersRadioButton))
                test.log("Successfully changed the gender to other")
                
            else:
                test.fail("Gender is not changed")
               
        if Weight:
            if waitForObject(liveScreenAddPatientWeightInput):
                WeightInput = (waitForObject(liveScreenAddPatientWeightInput))
                snooze(1)
                WeightInput.text = ""
                type(waitForObject(liveScreenAddPatientWeightInput), Weight)
                snooze(1)
                changedWeight = waitForObject(liveScreenAddPatientWeightInput)
                
                if changedWeight.text == Weight :
                    test.log("Successfully changed the patient's weight")
                
                else:
                    test.fail("Patient's weight is not changed")

        if Height:
            if waitForObject(liveScreenAddPatientHeightInput):
                HeightInput = (waitForObject(liveScreenAddPatientHeightInput))
                snooze(1)
                HeightInput.text = ""
                type(waitForObject(liveScreenAddPatientHeightInput), Height)
                snooze(1)
                changedHeight = waitForObject(liveScreenAddPatientHeightInput)
                
                if changedHeight.text == Height :
                    test.log("Successfully changed the patient's height")
                
                else:
                    test.fail("Patient's height is not changed")
        
        if PaceMaker:
            value = PaceMaker.strip()
            upper = value.upper()
            
            if upper == "YES":
                mouseClick(waitForObject(liveScreenAddPatientPaceMakeYesButton))
                test.log("Successfully changed the pacemaker to yes")
            
            elif upper == "NO":
                mouseClick(waitForObject(liveScreenAddPatientPaceMakeNoButton))
                test.log("Successfully changed the pacemaker to no")
            
            else:
                test.fail("Pacemaker is not changed")
                
        
        if Digoxin:
            value = Digoxin.strip()
            upper = value.upper()
            
            if upper == "YES":
                mouseClick(waitForObject(liveScreenAddPatientDigoxinYesButton))
                test.log("Successfully changed the Digoxin to yes")
            
            elif upper == "NO":
                mouseClick(waitForObject(liveScreenAddPatientDigoxinNoButton))
                test.log("Successfully changed the Digoxin to no")
            
            else:
                test.fail("Digoxin is not changed")
                
        
        if waitForObject(liveScreenAddPatientSaveButton):
            mouseClick(waitForObject(liveScreenAddPatientSaveButton))
            
            mouseClick(waitForObject(liveScreenPatientListButton))
            type(waitForObject(liveScreenPatientSearchInput), PatientId)
            snooze(2)
            parent = waitForObject(liveScreenPatientListView)
            child = object.children(parent)
            child_1 = object.children(child[0])
            
            for i in child_1:
                child_2 = object.children(i)
                if len(child_2) > 0:
                    child_3 = object.children(child_2[0])
                    value = child_3[1].text
                    test.log("value=%s" % value)
                    
                    if str(value) == PatientId:
                        mouseClick(waitForObject(liveScreenInfoButton))
                        test.log("Successfully clicked on info button")
                
                        if Surname:
                            if waitForObject(liveScreenAddPatientSurnameInput):
                                surnameInput = (waitForObject(liveScreenAddPatientSurnameInput))
                                
                                if surnameInput.text == Surname :
                                    test.log("Successfully edited and saved the surname in the live patient list screen")
                                
                                else:
                                    test.fail("Surname is not edited and it is not saved in the live patient list screen")
                                    
                        if Firstname:
                            if waitForObject(liveScreenAddPatientFirstNameInput):
                                firstNameInput = (waitForObject(liveScreenAddPatientFirstNameInput))
                                
                                if firstNameInput.text == Firstname :
                                    test.log("Successfully edited and saved the firstname in the live patient list screen")
                                
                                else:
                                    test.fail("Firstname is not edited and it is not saved in the live patient list screen")                
                        
                        if Title:
                            if waitForObject(liveScreenAddPatientTitleInput):
                                TitleInput = (waitForObject(liveScreenAddPatientTitleInput))
                                
                                if TitleInput.text == Title :
                                    test.log("Successfully edited and saved the title in the live patient list screen")
                                
                                else:
                                    test.fail("Title is not edited and it is not saved in the live patient list screen")
                                            
                        if PatientAge:
                            if waitForObject(liveScreenAddPatientAgeInput):
                                AgeInput = (waitForObject(liveScreenAddPatientAgeInput))
                                
                                if  AgeInput.text == PatientAge :
                                    test.log("Successfully edited and saved the title in the live patient list screen")
                                
                                else:
                                    test.fail("Patient's age is not edited and it is not saved in the live patient list screen")
                                            
                        if PatientId:
                            if waitForObject(liveScreenAddPatientIdInput):
                                PatientIdInput = (waitForObject(liveScreenAddPatientIdInput))
                                
                                if PatientIdInput.text == PatientId :
                                    test.log("Successfully edited and saved the patient's id in the live patient list screen")
                                
                                else:
                                    test.fail("Patient's id is not edited and it is not saved in the live patient list screen")
                                    
                        if HospitalId:
                            if waitForObject(liveScreenAddPatientHospitalIdInput):
                                HospitalIdInput = (waitForObject(liveScreenAddPatientHospitalIdInput))
                                
                                if HospitalIdInput.text == HospitalId :
                                    test.log("Successfully edited and saved the hospital id in the live patient list screen")
                                
                                else:
                                    test.fail("Hospital id is not edited and it is not saved in the live patient list screen")
                                            
                        if Gender:
                            value = Gender.strip() 
                            upper = value.upper()
                            
                            if upper == "MALE":
                                mouseClick(waitForObject(liveScreenAddPatientMaleRadioButton))
                                test.log("Successfully changed the gender to male")
                            
                            elif upper == "FEMALE":
                                mouseClick(waitForObject(liveScreenAddPatientFemaleRadioButton))
                                test.log("Successfully changed the gender to female")
                            
                            elif upper == "OTHER":
                                mouseClick(waitForObject(liveScreenAddPatientOthersRadioButton))
                                test.log("Successfully changed the gender to other")
                                
                            else:
                                test.fail("Gender is not changed")
                                               
                        if Weight:
                            if waitForObject(liveScreenAddPatientWeightInput):
                                WeightInput = (waitForObject(liveScreenAddPatientWeightInput))
                                
                                if WeightInput.text == Weight :
                                    test.log("Successfully edited and saved the patient's weight in the live patient list screen")
                                
                                else:
                                    test.fail("Patient's weight is not edited and it is not saved in the live patient list screen")
                                    
                        if Height:
                            if waitForObject(liveScreenAddPatientHeightInput):
                                HeightInput = (waitForObject(liveScreenAddPatientHeightInput))
                                
                                if HeightInput.text == Height :
                                    test.log("Successfully edited and saved the patient's height in the live patient list screen")
                                
                                else:
                                    test.fail("Patient's height is not edited and it is not saved in the live patient list screen")
                                        
                        if PaceMaker:
                            value = PaceMaker.strip()
                            upper = value.upper()
                            
                            if upper == "YES":
                                mouseClick(waitForObject(liveScreenAddPatientPaceMakeYesButton))
                                test.log("Successfully changed the pacemaker to yes")
                            
                            elif upper == "NO":
                                mouseClick(waitForObject(liveScreenAddPatientPaceMakeNoButton))
                                test.log("Successfully changed the pacemaker to no")
                            
                            else:
                                test.fail("Pacemaker is not changed")
                                        
                        if Digoxin:
                            value = Digoxin.strip()
                            upper = value.upper()
                            
                            if upper == "YES":
                                mouseClick(waitForObject(liveScreenAddPatientDigoxinYesButton))
                                test.log("Successfully changed the digoxin to yes")
                            
                            elif upper == "NO":
                                mouseClick(waitForObject(liveScreenAddPatientDigoxinNoButton))
                                test.log("Successfully changed the digoxin to no")
                            
                            else:
                                test.fail("Digoxin is not changed")   
                
        return True
    
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to scroll the list and get the patient details in patient list screen
def scrollListInPatientListScreen():
   
    patientList = []
    y_list = []
   
    listView = findObject(liveScreenPatientListView)
    totalIteration = listView.count / 9
       

    for i in range(totalIteration):
               
        listChild = []        
       
        listChild = waitForObject(liveScreenPatientListView)
        item = object.children(listChild)
        rowParent = object.children(item[0])
       
        for j in  rowParent:        
            rowchild = object.children(j)
           
            if len(rowchild) > 0:
                row = object.children(rowchild[0])
               
                if j.y in y_list:
                    pass
                else:
                    patientData = []
                   
                    name = str(row[0].text)
                    id = str(row[1].text)
                    lastExam = str(row[2].text)
                   
                    patientData.append(name)
                    patientData.append(id)
                    patientData.append(lastExam)
                   
                    patientList.append(patientData)
                   
                    y_list.append(j.y)
 
        flick(waitForObject(liveScreenPatientListView), 0, 415)
       
    return patientList    

# function to sort in ascending order by using patient name in patient list screen
def testAscendingByNameSortInPatientListScreen():

    patientList = scrollListInPatientListScreen()
        
    newList = []
    newList = patientList[:]
    
    newList.sort(key=lambda x: x[0])
    if newList == patientList:
        test.log("Sorted in ascending order by using patient name in patient list screen")
    else:
        test.fail("Not sorted in ascending order by using patient name in patient list screen") 
      
# function to sort in descending order by using patient name in patient list screen
def testDescendingByNameSortInPatientListScreen():

    patientList = scrollListInPatientListScreen()
        
    newList = []
    newList = patientList[:]
    
    newList.sort(key=lambda x: x[0], reverse=True)
    if newList == patientList:
        test.log("Sorted in descending order by using patient name in patient list screen")
    else:
        test.fail("Not sorted in descending order by using patient name in patient list screen")
        
# Function to verify sort by patient name in patient list screen
def verifySortForPnameInPatientListScreen(sortType):
    try:  
        if waitForObject(nameSortButton):
            
            sortButtonState = str(waitForObject(nameSortButton).state)
            
            if sortButtonState == "" and sortType == "ascending":
                mouseClick(waitForObject(nameSortButton)) 
                testAscendingByNameSortInPatientListScreen()

            elif sortType == "ascending" and sortButtonState == "ascendingSort":
                testAscendingByNameSortInPatientListScreen()
                
            elif sortType == "ascending" and sortButtonState == "descendingSort":
                mouseClick(waitForObject(nameSortButton))
                testAscendingByNameSortInPatientListScreen()   
         
            elif sortType == "descending" and sortButtonState == "":
                mouseClick(waitForObject(nameSortButton))
                snooze(2)
                mouseClick(waitForObject(nameSortButton))
                testDescendingByNameSortInPatientListScreen()   
                            
            elif sortType == "descending" and sortButtonState == "descendingSort":
                testDescendingByNameSortInPatientListScreen()
                
            elif sortType == "descending" and sortButtonState == "ascendingSort":
                mouseClick(waitForObject(nameSortButton))
                testDescendingByNameSortInPatientListScreen()
            return True  
     
    except Exception as e:
        test.fail("Exception" + str(e))

# function to sort in ascending order by using patient id in patient list screen
def testAscendingByPatientIdSortInPatientListScreen():

    patientList = scrollListInPatientListScreen()
        
    newList = []
    newList = patientList[:]
    
    newList.sort(key=lambda x: x[1])
    if newList == patientList:
        test.log("Sorted in ascending order by using patient id in patient list screen")
    else:
        test.fail("Not sorted in ascending order by using patient id in patient list screen") 
      
# function to sort in descending order by using patient id in patient list screen
def testDescendingBypatientIdSortInPatientListScreen():

    patientList = scrollListInPatientListScreen()
        
    newList = []
    newList = patientList[:]
    
    newList.sort(key=lambda x: x[1], reverse=True)
    if newList == patientList:
        test.log("Sorted in descending order by using patient id in patient list screen")
    else:
        test.fail("Not sorted in descending order by using patient id in patient list screen")
                     
# Function to verify sort by using patient id in patient list screen
def verifySortForPidInPatientListScreen(sortType):
    try:  
        if waitForObject(idSortButton):
           
            sortButtonState = str(waitForObject(idSortButton).state)
            
            if sortButtonState == "" and sortType == "ascending":
                mouseClick(waitForObject(idSortButton)) 
                testAscendingByPatientIdSortInPatientListScreen()

            elif sortType == "ascending" and sortButtonState == "ascendingSort":
                testAscendingByPatientIdSortInPatientListScreen()
                
            elif sortType == "ascending" and sortButtonState == "descendingSort":
                mouseClick(waitForObject(idSortButton))
                testAscendingByPatientIdSortInPatientListScreen()
         
            elif sortType == "descending" and sortButtonState == "":
                mouseClick(waitForObject(idSortButton))
                snooze(2)
                mouseClick(waitForObject(idSortButton))
                testDescendingBypatientIdSortInPatientListScreen()
                            
            elif sortType == "descending" and sortButtonState == "descendingSort":
                testDescendingBypatientIdSortInPatientListScreen()
                
            elif sortType == "descending" and sortButtonState == "ascendingSort":
                mouseClick(waitForObject(idSortButton))
                testDescendingBypatientIdSortInPatientListScreen()
            
            return True  
     
    except Exception as e:
        test.fail("Exception" + str(e))
        
# function to sort in ascending order by using last exam in patient list screen
def testAscendingByLastExamSortInPatientListScreen():

    patientList = scrollListInPatientListScreen()
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
    newList.sort(key=lambda x: x[2])
    
    if newList == updatedPatientList:
        test.log("Sorted in ascending order by using last exam in patient list screen")
    else:
        test.fail("Not sorted in ascending order by using last exam in patient list screen") 
      
# function to sort in descending order by using last exam  in patient list screen
def testDescendingByLastExamSortInPatientListScreen():

    patientList = scrollListInPatientListScreen()
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
    
    newList.sort(key=lambda x: x[2], reverse=True)
    if newList == updatedPatientList:
        test.log("Sorted in descending order by using last exam in patient list screen")
    else:
        test.fail("Not sorted in descending order by using last exam in patient list screen")
        
# Function to verify sort by using last exam in patient list screen
def verifySortForLastExamInPatientListScreen(sortType):
 
    try:  
        if waitForObject(lastExamSortButton):
        
            sortButtonState = str(waitForObject(lastExamSortButton).state)
            
            if sortButtonState == "" and sortType == "ascending":
                mouseClick(waitForObject(lastExamSortButton)) 
                testAscendingByLastExamSortInPatientListScreen()
                
            elif sortType == "ascending" and sortButtonState == "ascendingSort":
                testAscendingByLastExamSortInPatientListScreen()
                
            elif sortType == "ascending" and sortButtonState == "descendingSort":
                mouseClick(waitForObject(lastExamSortButton))
                testAscendingByLastExamSortInPatientListScreen() 
         
            elif sortType == "descending" and sortButtonState == "":
                mouseClick(waitForObject(lastExamSortButton))
                snooze(2)
                mouseClick(waitForObject(lastExamSortButton))
                testDescendingByLastExamSortInPatientListScreen()
                            
            elif sortType == "descending" and sortButtonState == "descendingSort":
                testDescendingByLastExamSortInPatientListScreen()
                
            elif sortType == "descending" and sortButtonState == "ascendingSort":
                mouseClick(waitForObject(lastExamSortButton))
                testDescendingByLastExamSortInPatientListScreen()
        
        return True  
     
    
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Method to select a patient from patients tab 
def selectPatientFromPatientsList(PatientIDSearch):
    try:
        
        Status = False
        PatientIDToSearch = PatientIDSearch
        snooze(2)
        if (waitForObject(liveScreenPatientListButton)):
            mouseClick(liveScreenPatientListButton)
            mouseClick(liveScreenPatientSearchInput)
            type(waitForObject(liveScreenPatientSearchInput), PatientIDToSearch)
            snooze(1)
            
            if (waitForObject(liveScreenPatientListView)):
                patientTable = waitForObject(liveScreenPatientListView)
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
                            
                            if (rowValue == PatientIDToSearch):
                                columnRecording = object.children(childRows[1])
                                mouseClick(columnRecording[1])
                                snooze(5)
                                if (waitForObject(liveScreenECGRecordButton)):
                                    Status = True
                                    break                           
                else:
                    test.log("No matching record found in Patient list with the given patient ID '" + PatientIDToSearch + "'")
                
            else:
                test.log("Patient list view is not available")    

        else:
            test.log("Failed to search '" + PatientIDToSearch + "' record from Patient List ")
        
        if Status:
            test.log("Successfully selected '" + PatientIDToSearch + "' record from Patient List ")
            return Status
        else:
            test.log("Failed to select '" + PatientIDToSearch + "' record from Patient List ")
            return Status
            
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to add a new patient in patient list screen _ Long run
def addNewPatientInPatientListScreenLongRun(PatientId=""):
    try:
        if waitForObject(liveScreenPatientAddButton):
            mouseClick(waitForObject(liveScreenPatientAddButton))              
            
            if waitForObject(liveScreenAddPatientIdInput):
                setFocusTextBox(liveScreenAddPatientIdInput)
                type(mainWindow, PatientId)           
        
        mouseClick(waitForObject(liveScreenAddPatientSaveButton))
        return True
                
    except Exception as e:
        test.fail("Exception" + str(e))  
        
# Function to add a new patient in patient list screen and select for recording_ diag test
def addNewPatientInPatientListScreenAndRecording(PatientId):
    try:
        if waitForObject(liveScreenPatientAddButton):
            mouseClick(waitForObject(liveScreenPatientAddButton))              
            
            if waitForObject(liveScreenAddPatientIdInput):
                setFocusTextBox(liveScreenAddPatientIdInput)
                type(mainWindow, PatientId)           
        
        mouseClick(waitForObject(patientCardAddPatientRecordButton))
        return True
                
    except Exception as e:
        test.fail("Exception" + str(e)) 