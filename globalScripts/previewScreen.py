
'''Objects of mainwindow's in every screen'''

summaryScreen_Mainwindow = {"container": mainWindow, "type": "Rectangle", "visible": True}
mainWindow = {"type": "QQuickWindowQmlImpl", "visible": True}
patientCardScreen_MainWindow = {"container": mainWindow, "id": "patientScreenId", "type": "PatientCard", "visible": True}
menuScreen_MainWindow = {"container": mainWindow, "id": "menuScreenId", "type": "Rectangle", "visible": True}
evaluationScreen_MainWindow = {"container": mainWindow, "id": "evalScreenId", "type": "EvalScreen", "visible": True}
evaluationSettingsScreen_Mainwindow = {"container": mainWindow, "type": "Rectangle", "visible": True}
previewSummaryScreen_Mainwindow = {"container": mainWindow, "id": "diagSummary", "type": "DiagnosticSummary",  "visible": True}
liveAddPatientScreen_Mainwindow = {"container": mainWindow, "id": "patientScreenRootId", "type": "Rectangle", "visible": True}
livePatientListScreen_Mainwindow = {"container": mainWindow, "id": "patientScreenRootId", "type": "Rectangle", "visible": True}

previewScreenPatientNameDisplay = {"container": mainWindow, "id": "patientNameId" ,"type": "Label","visible": True}
previewScreenSummaryButton = {"checkable": False, "container": mainWindow, "id": "summarybuttonId", "type": "RoundedRectangleButton","visible": True}
previewScreenSaveRecordButton  = {"checkable": False, "container": mainWindow, "id": "saveRecordButtonId", "type": "CircularButton", "visible": True}
previewScreenRecordNavigation = {"container": mainWindow, "id": "recordNavigationButtonId", "type": "RecordNavigationButton", "visible": True}
previewScreenSpeedAndGainButton = {"container": mainWindow, "id": "evaluationScreenSettingsButtonId", "type": "SettingsButton",  "visible": True}
previewScreenPrintECGReportButton = {"checkable": False, "container": mainWindow, "id": "printRecordButtonId", "type": "CircularButton","visible": True}
previewScreenSpeedOfECG = {"container": mainWindow, "id":"speedValId", "type": "TextInfo", "visible": True}
previewScreenSensitivityOfECG = {"container": mainWindow, "id": "sensValId", "type": "TextInfo", "visible": True}
previewScreenFilterName = {"container": mainWindow, "id": "filterNameId", "type": "TextInfo","visible": True}
previewScreenViewName = {"container": mainWindow, "id": "viewNameId", "type": "TextInfo","visible": True}

previewScreenMonitor = {"container": mainWindow, "id": "evaluationScreenMonitorContainerId", "type": "MonitoredParameterButton", "visible": True}
previewScreenWeightText = {"container": mainWindow,  "type": "TextInfo", "visible": True,"id":"weightValueId"}
previewScreenHeightText = {"container": mainWindow,  "type": "TextInfo", "visible": True,"id":"heightValueId"}

previewScreenRecordIndexDetail = {"container": mainWindow, "type": "Label",  "visible": True,"id":"recordIndexDetail"}

lockExamButtonId={"checkable": False, "container": mainWindow, "id": "lockExamButtonId", "type": "LockExamButton", "unnamed": 1, "visible": True}
saveButtonId={"checkable": False, "container": mainWindow, "id": "saveButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}

PatientCardLoaderID={"container": mainWindow, "id": "patientScreenId", "type": "PatientCardLoader", "unnamed": 1, "visible": True}

#Function to verify the patient ID and patient preview screen
def verifyPatientIdAndPatientNameInPreviewScreen(patientNameDisplay=""):
    try:
        if object.exists(previewScreenPatientNameDisplay):
            patientNameDisplayInPreviewScreen = str(waitForObject(previewScreenPatientNameDisplay).text)
    
            if patientNameDisplay==patientNameDisplayInPreviewScreen:
                test.passes("The given patient name %s and displayed patient name %s are matching in the preview screen" %(patientNameDisplay,patientNameDisplayInPreviewScreen))
            else:
                test.fail("The given patient name %s and displayed patient name %s are not matched in the preview screen"%(patientNameDisplay,patientNameDisplayInPreviewScreen))
         
        return True         
                
    except Exception as e:
        test.fail(str(e)) 
                
#Function to navigate to preview summary screen from preview screen       
def navigateToPreviewSummaryScreenFromPreviewScreen():
    try:
        if object.exists(previewScreenSummaryButton):
            mouseClick(waitForObject(previewScreenSummaryButton))
            snooze(1)
            
            if object.exists(previewSummaryScreen_Mainwindow):
                test.passes("Successfully preview screen is displayed")
            else:
                test.fail("preview screen is not displayed")  
                 
        return True 
             
    except Exception as e:
        test.fail(str(e))   
           
#Function to save ECG record in preview screen
def saveECGRecordInPreviewScreen():
    try:
        if object.exists(previewScreenSaveRecordButton):
            mouseClick(waitForObject(previewScreenSaveRecordButton))
            snooze(5)
            
            if object.exists(patientCardScreen_MainWindow):
                test.passes("Successfully saved the ECG record in preview screen")
            else:
                test.passes(" ECG record is not saved in preview screen")
        
        return True        
                
    except Exception as e:
        test.fail(str(e))


def saveECGRecordInPreviewScreen_updated():
    try:
        if object.exists(previewScreenSaveRecordButton):
            mouseClick(waitForObject(previewScreenSaveRecordButton))
            snooze(5)
            
            if object.exists(PatientCardLoaderID):
                test.passes("Successfully saved the ECG record in preview screen")
            else:
                test.passes(" ECG record is not saved in preview screen")
        
        return True        
                
    except Exception as e:
        test.fail(str(e))      
        
        
        
        
        
            
#Function to report print in preview screen
def reportPrintInPreviewScreen():
    try:
        if object.exists(previewScreenPrintECGReportButton):
            mouseClick(waitForObject(previewScreenPrintECGReportButton))
            snooze(2) 
                
            count = 0
            while object.exists(evaluationScreenPrinting) == True:
                snooze(1)
                count += 1
            test.log("Successfully printed the ECG record for %d seconds" %count)
            
        return True    

    except Exception as e:
        test.fail(str(e))      
        
#Function to verify the speed value in preview screen                     
def verifySpeedValueInPreviewScreenAfterChanging(speed):
    try:
        if object.exists(previewScreenSpeedOfECG):
            speedOfECGInPreviewScreen =str(waitForObject(previewScreenSpeedOfECG).text)
            
            if speedOfECGInPreviewScreen==str(speed):
                test.passes("Given speed %s and Displayed speed %s values are matched in the preview screen"%(speed,speedOfECGInPreviewScreen))
            else:
                test.fail("Given speed %s and Displayed speed %s values are not matched in the preview screen"%(speed,speedOfECGInPreviewScreen))
                
        return True
            
    except Exception as e:
        test.fail("Exception"+str(e)) 
                                                                                
#Function to verify the sensitivity value in preview screen                     
def verifySensitivityValueInPreviewScreenAfterChanging(sensitivity):
    try:
        if object.exists(previewScreenSensitivityOfECG):
            sensitivityOfECGInPreviewScreen =str(waitForObject(previewScreenSensitivityOfECG).text)
            
            if sensitivityOfECGInPreviewScreen==str(sensitivity):
                test.passes("Given sensitivity %s and Displayed sensitivity %s values are matched in the preview screen"%(sensitivity,sensitivityOfECGInPreviewScreen))
            else:
                test.fail("Given sensitivity %s and Displayed sensitivity %s values are not matched in the preview screen"%(sensitivity,sensitivityOfECGInPreviewScreen))
                
        return  True
        
    except Exception as e:
        test.fail("Exception"+str(e))  
        
#Function to verify the filter value in preview screen
def verifyfilterNameInPreviewScreenAfterChanging(ECGFilterName): 
    try:
        if object.exists(previewScreenFilterName):
            filterNameInPreviewScreen =str(waitForObject(previewScreenFilterName).text)

            if filterNameInPreviewScreen==str(ECGFilterName):
                test.passes("Given filter name %s and Displayed filter name %s are matched in the preview screen "%(ECGFilterName,filterNameInPreviewScreen))
            else:
                test.fail("Given filter name %s and Displayed filter name %s are not matched in the preview screen"%(ECGFilterName,filterNameInPreviewScreen))
                
        return True
    
    except Exception as e:
        test.fail("Exception"+str(e))  
                

#Function to verify weight and height in the preview monitor screen
def verifyWeightAndHeightInThepreviewScreen(weight,height):
    try:
        if object.exists(previewScreenMonitor):
            weightInPreviewScreen =str(findObject(previewScreenWeightText).text)
            heightInPreviewScreen =str(findObject(previewScreenHeightText).text)
            
            if weightInPreviewScreen==str(weight):
                test.passes("Given weight %s and Displayed weight %s values are matched in the preview screen"%(weight,weightInPreviewScreen))
            else:
                test.fail("Given weight %s and Displayed weight %s values are not matched in the preview screen"%(weight,weightInPreviewScreen))
                
            if heightInPreviewScreen==str(height):
                test.passes("Given height %s and Displayed height %s values are matched in the preview screen"%(height,heightInPreviewScreen))
            else:
                test.fail("Given height %s and Displayed height %s values are not matched in the preview screen"%(height,heightInPreviewScreen))
        
        return True
            
    except Exception as e:
        test.fail("Exception"+str(e))     
        
        
#Function to the get the no of preview records
def getNumberOfPreviewRecords():
    try:
        if object.exists(previewScreenRecordIndexDetail):
            recordIndex = waitForObject(previewScreenRecordIndexDetail)
            recordIndexLabel = str(recordIndex.text)
            recordIndexSplit = recordIndexLabel.split('/ ')
            recordIndexCount = recordIndexSplit[1]
            test.passes("recordIndexCount=%s" %recordIndexCount)
            
        return True
            
    except Exception as e:
        test.fail("Exception"+str(e))
        
        
        
        
#Method to approve the examination
def ApprovetheExaminationInpreviewScreen():
    try:
        status=False
        if object.exists(lockExamButtonId):
            obj=findObject(lockExamButtonId)
            if obj.enabled:
                mouseClick(waitForObject(lockExamButtonId))
                snooze(2)
                status=True
            else:
                test.log('Approve button is not enabled')
        
        return True if status==True else False     
                
    except Exception as e:
        test.fail(str(e))
        
def UnapprovetheExaminationInpreviewScreen():
    try:
        status=False
        if object.exists(lockExamButtonId):
            obj=findObject(lockExamButtonId)
            if obj.enabled:
                mouseClick(waitForObject(lockExamButtonId))
                snooze(2)
                status=True
            else:
                test.log('Unapprove button is not enabled')
        
        return True if status==True else False     
                
    except Exception as e:
        test.fail(str(e))
        
#Function to save in summary screen in preview                  
def saveSummaryScreenPreview(): 
    try:
        count = 0
        if waitForObject(saveButtonId):
            mouseClick(waitForObject(saveButtonId)) 
            snooze(.5)
            if waitForObject(previewScreenSaveRecordButton):
                test.log("Successfully saved summary page and preview screen is displayed ")
                count = 1
            else:
                test.log(" preview screen is not displayed ")
        else:
            test.log(" Summary save button is not displayed ")
                
        if count == 1:
            return True
        else:
            return False      

    except Exception as e:
        test.fail("Exception"+str(e))  

#Function to navigate to preview summary screen from preview screen       
def navigateToPreviewSummaryScreenFromPreviewScreen():
    try:
        if object.exists(previewScreenSummaryButton):
            mouseClick(waitForObject(previewScreenSummaryButton))
            snooze(1)
            
            if object.exists(previewSummaryScreen_Mainwindow):
                test.passes("Successfully preview screen is displayed")
            else:
                test.fail("preview screen is not displayed")  
                 
        return True 
             
    except Exception as e:
        test.fail(str(e))   
    
 
            
            
            

        
        
