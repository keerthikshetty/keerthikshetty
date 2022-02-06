source(findFile('scripts', '../../globalScripts/liveScreen.py'))
source(findFile('scripts', '../../globalScripts/menuPatientCard.py'))

import datetime

'''Objects of main window'''
mainWindow = {"type": "QQuickWindowQmlImpl", "visible": True}
evaluationScreen_MainWindow = {"container": mainWindow, "id": "evalScreenId", "type": "EvalScreen", "unnamed": 1, "visible": True}

'''Objects of Evaluation screen'''
evaluationScreenSaveRecordButton = {"checkable": False, "container": evaluationScreen_MainWindow, "id": "saveRecordButtonId", "type": "CircularButton", "visible": True}
evaluationScreenPrintECGReportButton = {"checkable": False, "container": mainWindow, "id": "printRecordButtonId", "type": "CircularButton",  "visible": True}
evaluationScreenSettingsButton = {"container": mainWindow, "id": "evaluationScreenSettingsButtonId", "type": "SettingsButton", "unnamed": 1, "visible": True}
evaluationScreenDeleteRecordButton = {"checkable": False, "container": mainWindow, "id": "deleteRecordButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
evaluationScreenDeleteYesButton = {"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton",  "visible": True}
evaluationScreenDeleteNoButton = {"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton", "visible": True}

evaluationScreenRecordAgainButton = {"checkable": False, "container": mainWindow, "id": "recordOneMoreButtonId", "type": "RecordOneMoreButton", "unnamed": 1, "visible": True}

evaluationScreenDoOneMoreLabelIndex = {"container": mainWindow, "id": "indexLabel", "type": "Label",  "visible": True}
evaluationScreenSummaryButton = {"checkable": False, "container": mainWindow, "id": "summarybuttonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}

liveScreenECGRecordButton = {"checkable": False, "container": mainWindow, "id": "startButtonId", "type": "Button",  "visible": True}
liveScreenPatientListButton = {"checkable": False, "container": mainWindow, "id": "patientButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
warningMessageId = {"container": mainWindow, "id": "warningMessageId", "type": "Label", "visible": True}
'''Objects of evaluation settings screen'''
evaluationSettingsProfileComboBox = {"container": mainWindow, "id": "profileComboBoxId", "type": "ComboBox",  "visible": True}
evaluationSettingsRecordingTabButton = {"checkable": True, "container": mainWindow, "id": "recordingTabButtonId", "text": "Recording", "type": "TabButton",  "visible": True}
evaluationSettingsDisplayAndPrintTabButton = {"checkable": True, "container": mainWindow, "id": "displayAndPrintTabButtonId", "text": "Display and Print", "type": "TabButton", "visible": True}
#evaluationSettingsFilterTabButton = {"checkable": True, "container": mainWindow, "id": "filterTabButtonId", "text": "Filters", "type": "TabButton",  "visible": True}
evaluationSettingsFilterTabButton = {"checkable": True, "container": mainWindow, "id": "filterTabButtonId", "text": "Filter", "type": "TabButton", "visible": True}
#evaluationSettingsSaveButton = {"checkable": False, "container": mainWindow, "id": "saveSettingsButtonId", "type": "CircularButton",  "visible": True}
evaluationSettingsSaveButton = {"checkable": False, "container": mainWindow, "id": "saveButtonId", "type": "CircularButton",  "visible": True}
evaluationSettingsCancelButton = {"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton",  "visible": True}
evaluationSettingsCancelButtonPopUpAcceptButton = {"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "visible": True}
#evaluationSettingsCancelButton = {"checkable": False, "container": mainWindow, "id": "cancelSettingsButtonId", "type": "CircularButton",  "visible": True}
evaluationSettingsCloseButton = {"container": mainWindow, "id": "closeSummaryButtonId", "type": "CloseDialogButton", "visible": True}
'''Objects of evaluation settings display and print tab button'''
evaluationSpeed_5 = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CircularRadioButton", "_id": "speed_0", "visible": True}
evaluationSpeed_10 = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CircularRadioButton", "_id": "speed_1", "visible": True}
evaluationSpeed_12_5 = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CircularRadioButton", "_id": "speed_2", "visible": True}
evaluationSpeed_25 = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CircularRadioButton", "_id": "speed_3", "visible": True}
evaluationSpeed_50 = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CircularRadioButton", "_id": "speed_4", "visible": True}
evaluationSpeed_Unit = {"container": mainWindow, "text": "mm/s", "type": "Text",  "visible": True}
evaluationSensitivity_2_5 = {"checkable": True, "container": mainWindow, "id": "_idsensitivity", "type": "CircularRadioButton", "_idsensitivity": "sensitivity_0", "visible": True}
evaluationSensitivity_5 = {"checkable": True, "container": mainWindow, "id": "_idsensitivity", "type": "CircularRadioButton", "_idsensitivity": "sensitivity_1", "visible": True}
evaluationSensitivity_10 = {"checkable": True, "container": mainWindow, "id": "_idsensitivity", "type": "CircularRadioButton", "_idsensitivity": "sensitivity_2", "visible": True}
evaluationSensitivity_20 = {"checkable": True, "container": mainWindow, "id": "_idsensitivity",  "type": "CircularRadioButton", "_idsensitivity": "sensitivity_3", "visible": True}
evaluationSensitivity_Unit = {"container": mainWindow,  "text": "mm/mV", "type": "Text",  "visible": True}

'''Objects of evaluation settings filter tab button'''
evaluationSettingsFilterNoneButton = {"checkable": True, "container": mainWindow, "id": "_id", "type": "CustomRadioButton", "_id": "filtergroup0", "visible": True}
evaluationSettingsFilterAutoButton = {"checkable": True, "container": mainWindow, "id": "_id",  "type": "CustomRadioButton", "_id": "filtergroup1", "visible": True}
evaluationSettingsFilterStrictButton = {"checkable": True, "container": mainWindow, "id": "_id",  "type": "CustomRadioButton", "_id": "filtergroup2", "visible": True}
evaluationSettingsFilterUserButton = {"checkable": True, "container": mainWindow, "id": "_id",  "type": "CustomRadioButton", "_id": "filtergroup3", "visible": True}
#evaluationSettingsMainsFiltersComboBox = {"container": mainWindow, "id": "mainsFiltersComboboxId", "type": "ComboBox",  "visible": True}
evaluationSettingsMainsFiltersComboBox = {"container": mainWindow, "id": "mainsFiltersComboboxId", "type": "ComboBox",  "visible": True}
evaluationSettingsMainFilterRowId = {"container": mainWindow, "id": "mainFilterRowId", "type": "Item", "visible": True}
evaluationSettingsDriftFiltersComboBox = {"container": mainWindow, "id": "driftFiltersComboboxId", "type": "ComboBox",  "visible": True}
evaluationSettingsDriftFilterRowId = {"container": mainWindow, "id": "driftFilterRowId", "type": "Item", "visible": True}
evaluationSettingsMyoFiltersComboBox = {"container": mainWindow, "id": "myoFiltersComboboxId", "type": "ComboBox",  "visible": True}
evaluationSettingsMyoFilterRowId = {"container": mainWindow, "id": "myoFilterRowId", "type": "Item", "visible": True}
evaluationSettingsFilterSuggestionLabel = {"container": mainWindow, "text": "0.05 Hz filter is recommended for ST observation. <br> 25 Hz filter significantly reduces QRS amplitudes", "type": "Text", "visible": True}

'''Objects of evaluation screen settings display'''
evaluationScreenSpeedOfECG = {"container": mainWindow, "id": "speedValId", "type": "TextInfo", "visible": True}
evaluationScreenSensitivityOfECG = {"container": mainWindow, "id": "sensValId", "type": "TextInfo", "visible": True}
evaluationScreenFilterName = {"container": mainWindow, "id": "filterNameId", "type": "TextInfo","visible": True}
evaluationScreenViewName = {"container": mainWindow, "id": "viewNameId", "type": "TextInfo", "visible": True}
evaluationScreenPatientNameDisplay = {"container": mainWindow, "id": "patientNameId", "type": "Label", "visible": True}
evaluationScreenPatientIdDisplay = {"container": mainWindow, "id": "patientidId", "type": "Label","visible": True}
#evaluationScreenPatientStatusBar = {"container": mainWindow, "id": "statusBarId", "type": "ECGStatusBar", "visible": True}
evaluationScreenPatientStatusBar= {"container": mainWindow, "id": "statusBarId", "type": "ECGStatusBar", "visible": True}
evaluationScreenRecordIndexDetail = {"container": mainWindow,  "type": "Label", "id":"recordIndexDetail", "visible": True}
evaluationScreenPrintingPopUp = {"container": mainWindow, "id": "busyIndicatorId", "type": "CustomBusyIndicator", "visible": True}
'''Objects of summary screen display'''
closeSummaryScreenButton = {"container": mainWindow, "id": "closeSummaryButtonId", "type": "CloseDialogButton", "visible": True}
amplitudeSummaryScreenButton = {"checkable": True, "container": mainWindow, "id": "amplitudesTabButtonId", "text": "Amplitudes", "type": "TabButton", "visible": True}
averagecomlexSummaryScreenButton = {"checkable": True, "container": mainWindow, "id": "avgComplexesTabButtonId", "text": "Average Complexes", "type": "TabButton", "visible": True}


'Localization testing-Objects-'
'Evaluation screen-Auto profile record'
diagSummaryHeaderId={"container": mainWindow, "id": "diagSummaryHeaderId", "type": "Item", "unnamed": 1, "visible": True}
diagSummaryBPId={"container": mainWindow, "id": "diagSummaryBPId", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
diagSummaryRRId={"container": mainWindow, "id": "diagSummaryRRId", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
pIntervalId={"container": mainWindow, "id": "pIntervalId", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
pqIntervalId={"container": mainWindow, "id": "pqIntervalId", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
qrsId={"container": mainWindow, "id": "qrsId", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
qtId={"container": mainWindow, "id": "qtId", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
paxisid={"container": mainWindow, "id": "paxisid", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
qrsaxisid={"container": mainWindow, "id": "qrsaxisid", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
taxisid={"container": mainWindow, "id": "taxisid", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
qtcid={"container": mainWindow, "id": "qtcid", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
resultsID={"container": mainWindow, "id": "results", "type": "DiagnosticResults", "unnamed": 1, "visible": True}
footerItemId_warningmsg={"container": mainWindow, "id": "footerItemId", "type": "FooterItem", "unnamed": 1, "visible": True}
resultsTabButtonId={"checkable": True, "container": mainWindow, "id": "resultsTabButtonId","type": "TabButton", "unnamed": 1, "visible": True}
amplitudesTabButtonId={"checkable": True, "container": mainWindow, "id": "amplitudesTabButtonId","type": "TabButton", "unnamed": 1, "visible": True}
avgComplexesTabButtonId={"checkable": True, "container": mainWindow, "id": "avgComplexesTabButtonId", "type": "TabButton", "unnamed": 1, "visible": True}
parameterNamesAreaId={"container": mainWindow, "id": "parameterLabelListViewId", "type": "ListView", "unnamed": 1, "visible": True}
averageComplexestextID={"container":mainWindow, "id": "averageComplexes", "type": "AverageComplexes", "unnamed": 1, "visible": True}
summarysaveButtonId={"checkable": False, "container": mainWindow, "id": "saveButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
EvaluationsaveRecordButtonId={"checkable": False, "container": mainWindow, "id": "saveRecordButtonId", "type": "SaveRecordButton", "unnamed": 1, "visible": True}




#Function to save the ECG record in evaluation screen
def saveECGRecordInEvaluationScreen():
    try:
        snooze(2)
        status = "Fail"
        if waitForObject(evaluationScreenSaveRecordButton):
            if object.exists(evaluationScreenSaveRecordButton):
                mouseClick(evaluationScreenSaveRecordButton)
                test.log("Save button is clicked successfully")
                status = "Pass"
        else :
            test.log("Save button is not clicked successfully")
            status = "Fail" 
        if status == "Pass":
            return True  
        else :
            return False
        
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Function to delete ECG record in evaluation screen
def deleteECGRecordInEvaluationScreen():
    try:
        dateandtime=str(datetime.datetime.now())
        status = "Fail"
        if waitForObject(evaluationScreenDeleteRecordButton):
            if object.exists(evaluationScreenDeleteRecordButton):
                snooze(2)
                mouseClick(evaluationScreenDeleteRecordButton)
                snooze(2)
                warningpopup = waitForObject(warningMessageId)
                warningText = str(warningpopup.text)
                if ( "want to delete" in warningText):
                    mouseClick(evaluationScreenDeleteYesButton)
                    test.log("Discard ECG Record from Evaluation screen")
                    #file.write(dateandtime + 'Discard ECG record from the Evaluation screen\n')
                    status = "Pass"            
                else:
                    test.log("Unable to Discard the ECG")
                    #file.write(dateandtime + "Unable to Discard the ECG\n")
                    status = "Fail"            
        if status == "Pass" :
            return True  
        else :
            return False
    
    except Exception as e:
        test.fail("Exception" +str(e))
        #file.write(dateandtime + 'Exception:\n'+str(e))
        
# Function to save And Do one more in evaluation screen
def saveandDoOnemoreECGRecordInEvaluationScreen():
    try:
        status = "Fail"
        if waitForObject(evaluationScreenRecordAgainButton):
            snooze(2)
            mouseClick(waitForObject(evaluationScreenRecordAgainButton)) 
            test.log("Save and Do one more in Evaluation screen")
            status = "Pass"            
        else:
            test.log("Unable to do save and do one more in Evaluation screen") 
            status = "Fail"            
        if status == "Pass" :
            return True  
        else :
            return False
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to save the ECG record in evaluation screen
def saveECGRecordInEvaluationScreenWithVerification(pid,date):
    try:
        if object.exists(evaluationScreenSaveRecordButton):
            mouseClick(waitForObject(evaluationScreenSaveRecordButton))
            
            mouseClick(waitForObject(liveScreenMenuButton))
            mouseClick(waitForObject(menuPatientcardButton))
            searchBox =(waitForObject(patientCardSearchInput))
            searchBox.text=""
            type(waitForObject(patientCardSearchInput), pid)
            snooze(1)
            parent = waitForObject(patientCardPatientListView)
            child = object.children(parent)
            child_1 = object.children(child[0])
                
            for i in child_1:
                child_2 = object.children(i)
                if len(child_2) > 0:
                    child_3 = object.children(child_2[0])
                    value = child_3[1].text
                    test.log("value = %s" %value)
                    if (value == pid):
                        if object.exists(patientCardInfoButton):
                            mouseClick(waitForObject(patientCardInfoButton))
                            snooze(3)
                            if object.exists(examinationListView):
                                parentExam = waitForObject(examinationListView)
                                childExam = object.children(parentExam)
                                child_1Exam = object.children(childExam[0])
                                snooze(1)
                                for i in child_1Exam:
                                    child_2Exam = object.children(i)
                                    if len(child_2Exam)>0:
                                        snooze(1)
                                        child_3Exam = object.children(child_2Exam[0])
                                        child_4Exam = object.children(child_3Exam[1])
                                        label = child_4Exam[3].text
                                        valueExam = str(label).strip()
                                        test.log("value = %s" %valueExam)
                                        snooze(1)
                                        if date == valueExam:
                                            test.passes("Successfully saved the ECG record")
                                            break
                                    else:
                                        test.fail(" ECG record is not saved")
        return True  
    
    except Exception as e:
        test.fail("Exception" +str(e))

#Function to print the ECG record in evaluation screen
def reportPrintInEvaluationScreen():
    try:
        if object.exists(evaluationScreenPrintECGReportButton):
            mouseClick(waitForObject(evaluationScreenPrintECGReportButton))
            snooze(2)
            count = 0
            if object.exists(lowBatteryRecordConfirmationButtonLiveScreen):
                mouseClick(lowBatteryRecordConfirmationButtonLiveScreen)
            while object.exists(evaluationScreenPrintingPopUp) == True:
                snooze(1)
                count += 1
                test.passes("Successfully printed the ECG record for %d seconds" %count)
        if count > 0:    
            return True
        else:
            return False

    except Exception as e:
        test.fail("Exception" +str(e))

#Function to delete the ECG record from evaluation screen
def deleteECGFromEvaluationScreen(pid,date):
    try:
        if waitForObject(evaluationScreenDeleteRecordButton):
            mouseClick(waitForObject(evaluationScreenDeleteRecordButton))
            snooze(2)
            mouseClick(waitForObject(evaluationScreenDeleteYesButton))
            snooze(2)    
            
            mouseClick(waitForObject(liveScreenMenuButton))
            mouseClick(waitForObject(menuPatientcardButton))
            searchBox =(waitForObject(patientCardSearchInput))
            searchBox.text=""
            type(waitForObject(patientCardSearchInput), pid)
            snooze(1)
            parent = waitForObject(patientCardPatientListView)
            child = object.children(parent)
            child_1 = object.children(child[0])
                
            for i in child_1:
                child_2 = object.children(i)
                if len(child_2) > 0:
                    child_3 = object.children(child_2[0])
                    value = child_3[1].text
                    test.log("value = %s" %value)
                    if (value == pid):
                        if object.exists(patientCardInfoButton):
                            mouseClick(waitForObject(patientCardInfoButton))
                            snooze(3)
                            if object.exists(examinationListView):
                                parentExam = waitForObject(examinationListView)
                                childExam = object.children(parentExam)
                                child_1Exam = object.children(childExam[0])
                                snooze(1)
                                for i in child_1Exam:
                                    child_2Exam = object.children(i)
                                    if len(child_2Exam)>0:
                                        snooze(1)
                                        child_3Exam = object.children(child_2Exam[0])
                                        child_4Exam = object.children(child_3Exam[1])
                                        label = child_4Exam[3].text
                                        valueExam = str(label).strip()
                                        #test.log("value = %s" %valueExam)
                                        snooze(1)
                                        if date == valueExam:
                                            test.fail("ECG record is not deleted before saving in evaluation screen")
                                            break
                            else:
                                test.passes("ECG record is deleted before saving in evaluation screen ")       
                
        return True 
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to record the ECG one more time
def saveAndDoOneMoreECGRecordInEvaluationScreen(noOfTimesForDoOneMoreRecord):
    try:
        if noOfTimesForDoOneMoreRecord <= 10:
            
            for i in range(noOfTimesForDoOneMoreRecord-1):
                
                if i==0:
                    global timeBeforeRecordingForRecordOneMore
                    timeBeforeRecordingForRecordOneMore = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
                    test.log("timeBeforeRecordingForRecordOneMore =%s" %timeBeforeRecordingForRecordOneMore)
                
                mouseClick(waitForObject(liveScreenECGRecordButton))
                snooze(11)
                mouseClick(findObject(evaluationScreenRecordAgainButton))
                snooze(2)
     
            mouseClick(waitForObject(liveScreenECGRecordButton))
            mouseClick(waitForObject(evaluationScreenSaveRecordButton))
            test.passes("Recorded ECG for %d times" %noOfTimesForDoOneMoreRecord)   

        return timeBeforeRecordingForRecordOneMore
    
    except Exception as e:
        test.fail("Exception" + str(e))
        
#Function to navigate from evaluation screen to  evaluation settings screen
def navigateToEvaluationSettingsScreenFromEvaluationScreen():
    try:
        if waitForObject(evaluationScreenSettingsButton):
            if object.exists(evaluationScreenSettingsButton):
                mouseClick(evaluationScreenSettingsButton)
                snooze(2)
        if object.exists(mainWindow):
            test.passes("Successfully evaluation settings screen is displayed")
        else:
            test.fail("Evaluation settings screen is not displayed")
                
        return True
       
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to navigate  to  evaluation summary screen from evaluation screen
def navigateToEvaluationSummaryScreenFromEvaluationScreen():
    try:
        snooze(4)
        if waitForObject(evaluationScreenSummaryButton):
            if object.exists(evaluationScreenSummaryButton):
                mouseClick(waitForObject(evaluationScreenSummaryButton))
                snooze(2)
        if object.exists(mainWindow):
            test.passes("Successfully evaluation summary screen is displayed")
            return True
        else:
            test.fail("Evaluation summary screen is not displayed")
            return False
       
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to navigate  to  evaluation summary screen Amplitude tab
def navigateToEvaluationSummaryScreenAmplitudeTab():
    try:
        snooze(1)
        status = False
        if waitForObject(amplitudeSummaryScreenButton):
            if object.exists(amplitudeSummaryScreenButton):
                mouseClick(amplitudeSummaryScreenButton)
                snooze(1)
                status = True
        return status
       
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to navigate  to  evaluation summary screen Average complex tab
def navigateToEvaluationSummaryScreenAverageComplexTab():
    try:
        snooze(1)
        status = False
        if waitForObject(averagecomlexSummaryScreenButton):
            if object.exists(averagecomlexSummaryScreenButton):
                mouseClick(averagecomlexSummaryScreenButton)
                snooze(1)
                status = True
        return status
       
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to navigate  to  evaluation summary from summary screen
def navigateToEvaluationSummaryFromSummaryScreen():
    try:
        snooze(1)
        status = False
        if waitForObject(closeSummaryScreenButton):
            if object.exists(closeSummaryScreenButton):
                mouseClick(closeSummaryScreenButton)
                snooze(1)
                status = True
        return status
       
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to get the speed and sensitivity values in evaluation screen
def gettingTheSpeedAndSensitivityValuesInEvaluationScreen():
    try:
        if object.exists(evaluationScreenSpeedOfECG):
            global speedOfECGInEvaluationScreen
            speedOfECGInEvaluationScreen =str(waitForObject(evaluationScreenSpeedOfECG).text)
            test.log("speedOfECGInEvaluationScreen=%s" %speedOfECGInEvaluationScreen)
            
        if object.exists(evaluationScreenSensitivityOfECG):
            global sensitivityOfECGInEvaluationScreen
            sensitivityOfECGInEvaluationScreen =str(waitForObject(evaluationScreenSensitivityOfECG).text)
            test.log("sensitivityOfECGInEvaluationScreen=%s" %sensitivityOfECGInEvaluationScreen)
        
        return speedOfECGInEvaluationScreen,sensitivityOfECGInEvaluationScreen
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to get the weight and height values in evaluation screen
def gettingWeightAndHeightValuesInEvaluationScreen():
    try:
        if object.exists(evaluationScreenMonitor):
            global weightInEvaluationScreen
            weightInEvaluationScreen =str(waitForObject(evaluationScreenWeightText).text)
            test.log("weightInEvaluationScreen=%s" %weightInEvaluationScreen)
        
        if object.exists(evaluationScreenMonitor):
            global heightInEvaluationScreen
            heightInEvaluationScreen =str(waitForObject(evaluationScreenHeightText).text)
            test.log("heightInEvaluationScreen=%s" %heightInEvaluationScreen)
            
        return weightInEvaluationScreen,heightInEvaluationScreen
    
    except Exception as e:
        test.fail("Exception"+str(e)) 
        
# Function to set the speed in the evaluation screen
def setSpeedInEvaluationScreen(speed):
    try:
        if object.exists(evaluationScreenSettingsButton):
            global newspeed
            newspeed=speed
            mouseClick(waitForObject(evaluationScreenSettingsButton))
            test.log("Successfully clicked on SpeedAndGainButton")  
                      
            if object.exists(evaluationSettingsDisplayAndPrintTabButton):
                mouseClick(waitForObject(evaluationSettingsDisplayAndPrintTabButton))
                test.log("Successfully clicked on DisplayAndPrintTabButton")
                
                if speed == 5:
                    mouseClick(waitForObject(evaluationSpeed_5))
                    test.passes("Changed the Speed into %s" % speed)
                elif speed == 10:
                    mouseClick(waitForObject(evaluationSpeed_10))
                    test.passes("Changed the Speed into %s" % speed)
                elif speed == 12.5:
                    mouseClick(waitForObject(evaluationSpeed_12_5))
                    test.passes("Changed the Speed into %s" % speed)
                elif speed == 25:
                    mouseClick(waitForObject(evaluationSpeed_25))
                    test.passes("Changed the Speed into %s" % speed)
                elif speed == 50:
                    mouseClick(waitForObject(evaluationSpeed_50))
                    test.passes("Changed the Speed into %s" % speed)
                else:
                    test.fail("changes are  not altered")
                    
        return newspeed
           
    except Exception as e:
        test.fail("Exception" + str(e))  
        
# Function to set the sensitivity in the evaluation screen
def setSensitivityInEvaluationScreen(sensitivity):
    try:
        if object.exists(evaluationScreenSettingsButton):
            global newsensitivity
            newsensitivity=sensitivity
            mouseClick(waitForObject(evaluationScreenSettingsButton))
            test.log("Successfully clicked on SpeedAndGainButton")  
                      
            if object.exists(evaluationSettingsDisplayAndPrintTabButton):
                mouseClick(waitForObject(evaluationSettingsDisplayAndPrintTabButton))
                test.log("Successfully clicked on DisplayAndPrintTabButton")
                
                if sensitivity == 2.5:
                    mouseClick(waitForObject(evaluationSensitivity_2_5))
                    test.passes("Changed the sensitivity into %s" % sensitivity)
                elif sensitivity == 5:
                    mouseClick(waitForObject(evaluationSensitivity_5))
                    test.passes("Changed the sensitivity into %s" % sensitivity)
                elif sensitivity == 10:
                    mouseClick(waitForObject(evaluationSensitivity_10))
                    test.passes("Changed the sensitivity into %s" % sensitivity)
                elif sensitivity == 20:
                    mouseClick(waitForObject(evaluationSensitivity_20))
                    test.passes("Changed the sensitivity into %s" % sensitivity)
                else:
                    test.fail("changes are  not altered")
                    
        return newsensitivity
               
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to set the filter name in evaluation screen
def setFilterNameInEvaluationScreen(FilterName):  
    try:
        if object.exists(evaluationScreenSettingsButton):
            global newFilterName
            newFilterName=FilterName
            mouseClick(waitForObject(evaluationScreenSettingsButton))
            #test.log("Successfully clicked on SpeedAndGainButton")  
                      
            if object.exists(evaluationSettingsFilterTabButton):
                mouseClick(waitForObject(evaluationSettingsFilterTabButton))
                #test.log("Successfully clicked on FilterTabButton")
                
                if FilterName == "None":
                    mouseClick(waitForObject(evaluationSettingsFilterNoneButton))
                    #test.log("Changed the filter into %s" % filter)
                    
                elif FilterName == "Auto":
                    mouseClick(waitForObject(evaluationSettingsFilterAutoButton))
                    #test.log("Changed the filter into %s" % filter)
                    
                elif FilterName == "Strict":
                    mouseClick(waitForObject(evaluationSettingsFilterStrictButton))
                    #test.log("Changed the filter into %s" % filter)
                    
                elif FilterName == "User":
                    mouseClick(waitForObject(evaluationSettingsFilterUserButton))
                    #test.log("Changed the filter into %s" % filter)
                else:
                    test.log("changes are  not altered")
        return newFilterName
             
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to return Custom Filter Values of Mains, Drift and myoFilter
def getCustomFilterValueEvaluationScreen(customFilterName):  
    try:
            global newFilterName
            global customFilterValue
            newCustomFilterName=customFilterName
            if newCustomFilterName == "Main":
                if object.exists(evaluationSettingsMainsFiltersComboBox):
                    mainFilters = findObject(evaluationSettingsMainsFiltersComboBox)
                    customFilterValue = str(mainFilters.currentText)
                else:
                    test.log("Could not able to find Mains Filter comboBox")                   
            elif newCustomFilterName == "Drift":
                if object.exists(evaluationSettingsDriftFiltersComboBox):
                    mainFilters = findObject(evaluationSettingsDriftFiltersComboBox)
                    customFilterValue = str(mainFilters.currentText)
                else:
                    test.log("Could not able to find Drift Filter comboBox")                
            elif newCustomFilterName == "Myo":
                if object.exists(evaluationSettingsMyoFiltersComboBox):
                    mainFilters = findObject(evaluationSettingsMyoFiltersComboBox)
                    customFilterValue = str(mainFilters.currentText)
                else:
                    test.log("Could not able to find Myo Filter comboBox")                                       
            else:
                test.log("Could not get the custom Filter Values for User Filter")
            return customFilterValue
             
    except Exception as e:
        test.fail("Exception" + str(e))
        
def comboBoxListValuesEvaluationScreen(obj):
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
def selectingCustomFilterValuesEvaluationscreen(obj,listValue):   
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
def checkStateOfObjectEvaluationScreen(obj):
    try:
        status = False
        if obj.focus:
            status = "Enabled"
        else:
            status = "Disabled"
        return status
    except Exception as e:
        test.fail("Exception"+ str(e))      
 
# Function to verify the speed value in evaluation screen                     
def verifySpeedValueInEvaluationScreenAfterChanging(verifySpeed):
    try:
        if object.exists(evaluationScreenSpeedOfECG):
            speedOfECGInEvaluationScreen = str(waitForObject(evaluationScreenSpeedOfECG).text)
            
            if speedOfECGInEvaluationScreen == str(verifySpeed):
                test.log("Evaluation Screen: Given speed %s and Displayed speed %s values are matched " % (verifySpeed, speedOfECGInEvaluationScreen))
            else:
                test.log("Evaluation Screen: Given speed %s and Displayed speed %s values are not matched " % (verifySpeed, speedOfECGInLiveScreen))
                
        return True
            
    except Exception as e:
        test.fail("Exception" + str(e)) 
        
#Function to verify the sensitivity value in evaluation screen
def verifySensitivityValuesInEvaluationScreenAfterChanging(verifySensitivity):
    try:
        if object.exists(evaluationScreenSensitivityOfECG):
            sensitivityOfECGInEvaluationScreen =str(waitForObject(evaluationScreenSensitivityOfECG).text)
            
            if sensitivityOfECGInEvaluationScreen==str(verifySensitivity):
                test.passes("Evaluation Screen: Given sensitivity %s and Displayed sensitivity %s values match" %(verifySensitivity,sensitivityOfECGInEvaluationScreen))
            else:
                test.fail("Evaluation Screen: Given sensitivity %s and Displayed sensitivity %s values do not match" %(verifySensitivity,sensitivityOfECGInEvaluationScreen))
                
        return True
                
    except Exception as e:
        test.fail("Exception" +str(e))

# Function to verify the filter value in evaluation screen
def verifyfilterNameInEvaluationScreenAfterChanging(verifyECGFilterName): 
    try:
        if waitForObject(evaluationScreenFilterName):
            filterNameInEvaluationScreen = str(waitForObject(evaluationScreenFilterName).text)

            if filterNameInEvaluationScreen == str(verifyECGFilterName):
                test.log("Evaluation Screen: Given filter name %s and Displayed filter name %s are matched " % (verifyECGFilterName, filterNameInEvaluationScreen))
                status = "Pass"
            else:                
                test.log("Evaluation Screen: Given filter name %s and Displayed filter name %s are not matched" % (verifyECGFilterName, filterNameInEvaluationScreen))
                status = "Fail"
        if status == "Pass" :
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception" + str(e))
        
# Function to verify the patient ID and patient name in evaluation screen
def verifyPatientIdAndPatientNameInEvaluationScreen(verifyPatientNameDisplay=""):
    try:
        if object.exists(evaluationScreenPatientNameDisplay):
            patientNameDisplayInEvaluationScreen = str(waitForObject(evaluationScreenPatientNameDisplay).text)
        if object.exists(evaluationScreenPatientIdDisplay):
            patientIdDisplayInEvaluationScreen = str(waitForObject(evaluationScreenPatientIdDisplay).text)   
        patientInformationDisplayInEvaluationScreen =  patientNameDisplayInEvaluationScreen + " " + patientIdDisplayInEvaluationScreen      
        if verifyPatientNameDisplay == patientInformationDisplayInEvaluationScreen:
            test.passes("Evaluation Screen: The given patient name %s and displayed patient name %s are matching" % (verifyPatientNameDisplay, patientNameDisplayInEvaluationScreen))
        else:
            test.fail("Evaluation Screen: The given patient name %s and displayed patient name %s are not matched " % (verifyPatientNameDisplay, patientNameDisplayInEvaluationScreen))
                
        return True
         
    except Exception as e:
        test.fail("Exception" + str(e))
        
#Function to verify the patient ID and patient name in evaluation screen
def verifyPatientInformationInEvaluationScreen(surName="",firstName="",patientID=""):
    try:
        status = "False"
        if object.exists(evaluationScreenPatientStatusBar):
            sNameEvaluationScreen = str(waitForObject(evaluationScreenPatientStatusBar).lname)
            fNameEvaluationScreen = str(waitForObject(evaluationScreenPatientStatusBar).pName)
            pIDEvaluationScreen = str(waitForObject(evaluationScreenPatientStatusBar).pId)
            if surName == sNameEvaluationScreen and firstName == fNameEvaluationScreen and patientID == pIDEvaluationScreen:
                test.log("Evaluation Screen: The given patient information and displayed patient information are same")
                status = "True"
            else:
                test.log("Evaluation Screen: The given patient information and displayed patient information are not same")
                status = "False"
        return status
        
    except Exception as e:
        test.fail("Exception" +str(e))
  
        
# Function to verify weight and height in the evaluation monitor screen
def verifyWeightAndHeightInTheEvaluationScreen(verifyWeight, verifyHeight):
    try:
        if object.exists(evaluationScreenMonitor):
            weightInEvaluationScreen = str(findObject(evaluationScreenWeightText).text)
            heightInEvaluationScreen = str(findObject(evaluationScreenHeightText).text)
            
            if weightInEvaluationScreen == str(verifyWeight):
                test.passes("Evaluation Screen: Given weight %s and Displayed weight %s values are matched " % (verifyWeight, weightInEvaluationScreen))
            else:
                test.fail("Evaluation Screen: Given weight %s and Displayed weight %s values are not matched " % (verifyWeight, weightInEvaluationScreen))
            
            if heightInEvaluationScreen == str(verifyHeight):
                test.passes("Evaluation Screen: Given height %s and Displayed height %s values are matched " % (verifyHeight, heightInEvaluationScreen))
            else:
                test.fail("Evaluation Screen: Given height %s and Displayed height %s values are not matched" % (verifyHeight, heightInEvaluationScreen))
        
        return True
            
    except Exception as e:
        test.fail("Exception" + str(e)) 
        
#Function to save the values in evaluation settings screen
def saveTheValuesInTheEvaluationSettingsScreen():
    try:
        status = "Fail"
        if object.exists(evaluationSettingsSaveButton):
            mouseClick(waitForObject(evaluationSettingsSaveButton))
            test.log("The values are saved")
            
            if object.exists(mainWindow):
                test.log("Successfully saved the values in the evaluation settings screen")
                status = "Pass"
            else:
                test.log("Values are not saved in the evaluation settings screen")
                status = "Fail"
        if status == "Pass" :
            return True
        else :
            return False
       
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to cancel the values in evaluation settings screen
def cancelTheValuesInTheEvaluationSettingsScreen():
    try:
        status = False
        if object.exists(evaluationSettingsCancelButton):
            mouseClick(waitForObject(evaluationSettingsCancelButton))
            test.log("The values are cancelled")
            snooze(1)
            if object.exists(evaluationSettingsCancelButtonPopUpAcceptButton):
                mouseClick(waitForObject(evaluationSettingsCancelButtonPopUpAcceptButton))
            
        if object.exists(mainWindow):
            test.log("Successfully cancelled the values in the evaluation settings screen")
            status = True
        else:
            test.log("Values are not cancelled in the evaluation settings screen")
        return status           
           
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to close the evaluation settings screen
def closeTheEvaluationSettingsScreen():
    try:
        if waitForObject(evaluationSettingsCloseButton):
            if object.exists(evaluationSettingsCloseButton):
                mouseClick(evaluationSettingsCloseButton)
                test.log("The values are cancelled")
            
            if object.exists(mainWindow):
                test.passes("Successfully closed the evaluation settings screen")
            else:
                test.fail("Evaluation settings screen is not closed")
                
        return True
       
    except Exception as e:
        test.fail("Exception" +str(e))
        


#Evaluation screen language validation
'Localization testing-Evaluation screen'

PrimarystripID={"container": mainWindow, "id": "recordNavigationButtonId", "type": "RecordNavigationButton", "unnamed": 1, "visible": True}
SummarytextID={"container": mainWindow, "text": "Summary - ", "type": "Label", "unnamed": 1, "visible": True}
BP_textsummaryscreen={"container": mainWindow, "text": "BP", "type": "Label", "unnamed": 1, "visible": True}
RR_textsummaryscreen={"container": mainWindow, "text": "RR", "type": "Label", "unnamed": 1, "visible": True}
ms_textsummaryscreen={"container": mainWindow, "text": "ms", "type": "Label", "unnamed": 1, "visible": True}
P_textsummaryscreen={"container": mainWindow, "text": "P", "type": "Label", "unnamed": 1, "visible": True}
PQ_PR_textsummaryscreen={"container": mainWindow, "text": "PQ(PR)", "type": "Label", "unnamed": 1, "visible": True}
QT_textsummaryscreen={"container": mainWindow, "text": "QT", "type": "Label", "unnamed": 1, "visible": True}
P_axis_textsummaryscreen={"container": mainWindow, "text": "P axis", "type": "Label", "unnamed": 1, "visible": True}
QRS_axis_textsummaryscreen={"container": mainWindow, "text": "QRS axis", "type": "Label", "unnamed": 1, "visible": True}
T_axis_textsummaryscreen={"container": mainWindow, "text": "T axis", "type": "Label", "unnamed": 1, "visible": True}
QTc_B_textsummaryscreen={"container": mainWindow, "text": "QTc(B)", "type": "Label", "unnamed": 1, "visible": True}
diagnostic_suggestiontext={"container": mainWindow, "text": "Diagnostic suggestions", "type": "Label", "unnamed": 1, "visible": True}
Recordedby_textsummaryscreen={"container": mainWindow, "text": "Recorded by: ", "type": "Label", "unnamed": 1, "visible": True}
AbnormalECG_summaryscreen={"checkable": True, "container": mainWindow, "id": "abnormalECGButtonId", "type": "CustomRadioButton", "unnamed": 1, "visible": True}
NormalECG_summaryscreen={"checkable": True, "container": mainWindow, "id": "normalECGButtonId", "type": "CustomRadioButton", "unnamed": 1, "visible": True}
warningmessg_agegender_summaryscreen={"container": mainWindow, "text": "Patient is considered as 50 year old male for analysis", "type": "Label", "unnamed": 1, "visible": True}
Unapproved_summaryscreenID={"checkable": False, "container": mainWindow, "id": "lockExamButtonId", "type": "LockExamButton", "unnamed": 1, "visible": True}
Approved_summaryscreenID={"checkable": False, "container": mainWindow, "id": "lockExamButtonId", "type": "LockExamButton", "unnamed": 1, "visible": True}
Resulttab_summaryscreen={"checkable": True, "container": mainWindow, "id": "resultsTabButtonId", "text": "Results", "type": "TabButton", "unnamed": 1, "visible": True}
diagSummaryHeaderId={"container": mainWindow, "id": "diagSummaryHeaderId", "type": "Item", "unnamed": 1, "visible": True}
diagSummaryBPId={"container": mainWindow, "id": "diagSummaryBPId", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
diagSummaryRRId={"container": mainWindow, "id": "diagSummaryRRId", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
pIntervalId={"container": mainWindow, "id": "pIntervalId", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
pqIntervalId={"container": mainWindow, "id": "pqIntervalId", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
qrsId={"container": mainWindow, "id": "qrsId", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
qtId={"container": mainWindow, "id": "qtId", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
paxisid={"container": mainWindow, "id": "paxisid", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
qrsaxisid={"container": mainWindow, "id": "qrsaxisid", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
taxisid={"container": mainWindow, "id": "taxisid", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
qtcid={"container": mainWindow, "id": "qtcid", "type": "DiagMeasurements", "unnamed": 1, "visible": True}
resultsID={"container": mainWindow, "id": "results", "type": "DiagnosticResults", "unnamed": 1, "visible": True}
footerItemId_warningmsg={"container": mainWindow, "id": "footerItemId", "type": "FooterItem", "unnamed": 1, "visible": True}
resultsTabButtonId={"checkable": True, "container": mainWindow, "id": "resultsTabButtonId","type": "TabButton", "unnamed": 1, "visible": True}
amplitudesTabButtonId={"checkable": True, "container": mainWindow, "id": "amplitudesTabButtonId","type": "TabButton", "unnamed": 1, "visible": True}
avgComplexesTabButtonId={"checkable": True, "container": mainWindow, "id": "avgComplexesTabButtonId", "type": "TabButton", "unnamed": 1, "visible": True}
parameterNamesAreaId={"container": mainWindow, "id": "parameterLabelListViewId", "type": "ListView", "unnamed": 1, "visible": True}
averageComplexestextID={"container":mainWindow, "id": "averageComplexes", "type": "AverageComplexes", "unnamed": 1, "visible": True}
summarysaveButtonId={"checkable": False, "container": mainWindow, "id": "saveButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
EvaluationsaveRecordButtonId={"checkable": False, "container": mainWindow, "id": "saveRecordButtonId", "type": "SaveRecordButton", "unnamed": 1, "visible": True}









#collecting primary strip text
def collectingprimarystripword():
    try:
        status='fail'
        if waitForObject(PrimarystripID):
            if object.exists(PrimarystripID):
                mouseClick(PrimarystripID)
                parent=findObject(PrimarystripID)
                child=object.children(parent)
                Row_2=object.children(child[2])
                item_1=object.children(Row_2[1])
                str1=item_1[1].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                status='pass'  
        return True if status=='pass' else False       
    except Exception as e:
        test.fail("Exception" +str(e))
       
#Navigating to the summary screen and collecting analysis text
def navigateToEvaluationSummaryScreenFromEvaluationScreen():
    try:
        status='fail'
        snooze(4)
        if waitForObject(evaluationScreenSummaryButton):
            if object.exists(evaluationScreenSummaryButton):
                parent=findObject(evaluationScreenSummaryButton)
                child=object.children(parent)
                str1=child[3].text
                addtolist1(str1)
                mouseClick(waitForObject(evaluationScreenSummaryButton))
                test.log('Collected string ='+str(str1))
                test.log('Successfully navigated to the summary screen')
                status='pass'
        return True if status=='pass' else False       
    except Exception as e:
        test.fail("Exception" +str(e))


#collecting summary text
def summarytext(obj):
    try:
        status='fail'
        if object.exists(obj):
            parent=findObject(obj)
            child=object.children(parent)
            Row_0=object.children(child[0])
            str1=Row_0[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            status='pass'
        return True if status=='pass' else False       
    except Exception as e:
        test.fail("Exception" +str(e))

#Common method to collect all text the BP,RR,P QT etc 
def suammarysResulttabvaluecal(*arguments):
    try:
        status='fail'
        for obj in arguments:
            if object.exists(obj):
                parent=findObject(obj)
                child=object.children(parent)
                Row_1=object.children(child[1])
                str1=Row_1[0].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(0.5)
                str1=Row_1[2].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(0.5)
        status='pass'
        return True if status=='pass' else False       
    except Exception as e:
        test.fail("Exception" +str(e))

#collecting text-Diagnostic suggestion and Recorded by 
def diganosticssuggestionrecordedby(obj):
    try:
        if object.exists(obj):
            parent=findObject(obj)
            child=object.children(parent)
            Column_0=object.children(child[0])
            Row_1=object.children(Column_0[1])
            str1=Row_1[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(0.5)
            str1=Row_1[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(0.5)
            status='pass'
        return True if status=='pass' else False       
    except Exception as e:
        test.fail("Exception" +str(e))

#collecting warning message-age and gender
def Ageandgenderwarningmessage(obj):
    try:
        if object.exists(obj):
            parent=findObject(obj)
            child=object.children(parent)
            Row_2=object.children(child[2])
            str1=Row_2[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            status='pass'
        return True if status=='pass' else False       
    except Exception as e:
        test.fail("Exception" +str(e))
    
#Collecting summary screen tab results text,amplitudes text and avg complex text
def tabsresults_amptext_avgcomplex_text(obj):
    try:
        if object.exists(obj):
            parent=findObject(obj)
            child=object.children(parent)
            str1=child[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            status='pass'
        return True if status=='pass' else False       
    except Exception as e:
        test.fail("Exception" +str(e))
#collecting abnormal and normal text
def Abnoramalandnormalecg(*arguments):
    try:
        status='fail'
        for obj in arguments:
            if object.exists(obj):
                parent=findObject(obj)
                label_1=object.children(parent)
                str1=label_1[1].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(1)
            status='pass'
        return True if status=='pass' else False       
    except Exception as e:
        test.fail("Exception" +str(e))

#collecting approved and unapproved   
def Unapprovedecgtext(*arguments):
    try:
        status='fail'
        for obj in arguments:
            if object.exists(obj):
                parent=findObject(obj)
                Label_1=object.children(parent)
                str1=Label_1[3].text
                addtolist1(str1)
                mouseClick(obj)
                test.log('Collected string ='+str(str1))
                snooze(2)
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e))     
  
#collecting Max amplitude[mV] and J +80 ms text  
def Max_amplitude_text(obj):
    try:
        if object.exists(obj):
            parent=findObject(obj)
            child=object.children(parent)
            item_0=object.children(child[0])
            str1=item_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            str1=item_0[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e)) 
            
#common method to collect all the 12 text (P+,P- etc)
def PQRSTtext(obj):
    try:
        if object.exists(obj):
            parent=findObject(obj)
            child=object.children(parent)
            item_0=object.children(child[0])
            str1=item_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(0.5)
            str1=item_0[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            str1=item_0[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            str1=item_0[3].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            str1=item_0[4].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            str1=item_0[5].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            str1=item_0[6].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            str1=item_0[7].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            str1=item_0[8].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            str1=item_0[9].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            str1=item_0[10].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            str1=item_0[11].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e)) 
    
#collecting 10.00 mm/mV and 50.0 mm/Sec
def Avcomplex_mm_mV_mm_Sec(obj):
    try:
        status='fail'
        if object.exists(obj):
            parent=findObject(obj)
            child=object.children(parent)
            column_0=object.children(child[0])
            Row_1=object.children(column_0[1])
            str1=Row_1[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            str1=Row_1[4].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            status='pass'
            snooze(1)
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e))
         
def collectingtextfromSummaryScreenResultsTab():
    try:
        #collecting summary text
        step1=summarytext(diagSummaryHeaderId)
        #collecting all  the text(calculation) from results tab from summary screen
        step2=suammarysResulttabvaluecal(diagSummaryBPId,diagSummaryRRId,pIntervalId,pqIntervalId,qrsId,qtId,paxisid,qrsaxisid,taxisid,qtcid)
        #collecting text-Diagnostic suggestion and Recorded by
        step3=diganosticssuggestionrecordedby(resultsID)
        #collecting warning message
        step4=Ageandgenderwarningmessage(footerItemId_warningmsg)
        #collecting results tab text
        step5=tabsresults_amptext_avgcomplex_text(resultsTabButtonId)
        #collecting Abnormal text and normal text
        step6=Abnoramalandnormalecg(AbnormalECG_summaryscreen,NormalECG_summaryscreen)
        #collecting Unapproved and approved text
        step7=Unapprovedecgtext(Unapproved_summaryscreenID,Approved_summaryscreenID)

        if step1 and step2 and step3 and step4 and step5 and step6 and step7:
            test.log('Successfully collected text summary screen results tab screen')
            status='pass'
        else:
            test.log('Failed to collect summary screen results tab screen')
            status='fail'
        return True if status=='pass' else False       
    except Exception as e:
        test.fail("Exception" +str(e))
      
#Navigating to amplitude tab and collecting text
def collectingtextfromSummaryScreenAmplitudesTab():
    try:
        status='fail'
        if waitForObject(amplitudesTabButtonId):
            if object.exists(amplitudesTabButtonId):
                mouseClick(amplitudesTabButtonId)
                tabsresults_amptext_avgcomplex_text(amplitudesTabButtonId)
        #collecting max amplitude text        
        step1=Max_amplitude_text(parameterNamesAreaId)
        #Collecting (P+,P-, Q,R,R' etc)
        step2=PQRSTtext(parameterNamesAreaId)
        
        if step1 and step2:
            test.log('Collected all the text from amplitude tab')
            status='pass'
        else:
            test.log('failed to collect all text from amplitude tab')
            status='fail'
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e)) 

def collectingtextfromSummaryScreenavgcomplexTab():
    try:
        status='fail'
        if waitForObject(avgComplexesTabButtonId):
            if object.exists(avgComplexesTabButtonId):
                mouseClick(avgComplexesTabButtonId)
                tabsresults_amptext_avgcomplex_text(avgComplexesTabButtonId)
        #collecting 10.00 mm/mV and 50.0 mm/Sec text        
        step1=Avcomplex_mm_mV_mm_Sec(averageComplexestextID)
        
        if step1:
            test.log('Collected all the text from amplitude tab')
            status='pass'
        else:
            test.log('failed to collect all text from amplitude tab')
            status='fail'
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e)) 
        
def NavigatetoEvaluationscreenfromsummaryscreen():
    try:
        status='fail'
        if waitForObject(summarysaveButtonId):
            if object.exists(summarysaveButtonId):
                mouseClick(summarysaveButtonId)
                status='pass'
                snooze(2)
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e)) 

def NavigatetoonlinescreenfromEvaluationscreen():
    try:
        status='fail'
        if waitForObject(EvaluationsaveRecordButtonId):
            if object.exists(EvaluationsaveRecordButtonId):
                mouseClick(EvaluationsaveRecordButtonId)
                status='pass'
                snooze(2)
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e)) 
        
                
        
  
    