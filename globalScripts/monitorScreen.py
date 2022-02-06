
'''Objects of mainwindow's in every screen'''

mainWindow = {"type": "QQuickWindowQmlImpl", "visible": True}
onlineScreen_MainWindow ={"container": mainWindow, "id": "onlineScreenId", "type": "OnlineWfScreen", "visible": True}
patientCardScreen_MainWindow = {"container": mainWindow, "id": "patientScreenId", "type": "PatientCard",  "visible": True}
menuScreen_MainWindow = {"container": mainWindow, "id": "menuScreenId", "type": "Rectangle",  "visible": True}
evaluationScreen_MainWindow = {"container": mainWindow, "id": "evalScreenId", "type": "EvalScreen", "visible": True}
evaluationSettingsScreen_Mainwindow = {"container": mainWindow, "type": "Rectangle", "visible": True}
evaluationSummaryScreen_Mainwindow = {"container": mainWindow, "id": "diagSummary", "type": "DiagnosticSummary", "visible": True}
liveAddPatientScreen_Mainwindow = {"container": mainWindow, "id": "patientScreenRootId", "type": "Rectangle", "visible": True}
livePatientListScreen_Mainwindow = {"container": mainWindow, "id": "patientScreenRootId", "type": "Rectangle", "visible": True}

'''Objects of live screen '''

liveScreenWeightText = {"container": mainWindow, "id":"weightValueId" , "type": "TextInfo", "visible": True}
liveScreenHeightText = {"container": mainWindow, "id": "heightValueId", "type": "TextInfo",  "visible": True}
liveScreenMonitor = {"container": mainWindow, "id": "onlineScreenMonitorContainerId", "type":"Item",  "visible": True}

'''Objects of monitor screen'''

manualInputSystolicBox = {"backgroundcolor": "#f6f6f6", "container": mainWindow, "echoMode": 0, "id": "systolicInputId", "type": "TextField",  "visible": True}
manualInputDiastolicBox = {"backgroundcolor": "#f6f6f6", "container": mainWindow, "echoMode": 0, "id": "diastolicInputId", "type": "TextField", "visible": True}
manualInputBloodPressureUnit = {"container": mainWindow, "text": "mmHg", "type": "Label", "visible": True}
manualInputweightBox = {"backgroundcolor": "#f6f6f6", "container": mainWindow, "echoMode": 0, "id": "weightInputId", "type": "TextField", "unnamed": 1, "visible": True}
manualInputweightUnit = {"container": mainWindow, "text": "kg", "type": "Label", "unnamed": 1, "visible": True}
manualInputheightBox = {"backgroundcolor": "#f6f6f6", "container": mainWindow, "echoMode": 0, "id": "heightInputId", "type": "TextField", "visible": True}
manualInputheightUnit = {"container": mainWindow, "text": "cm", "type": "Label",  "visible": True}
manualInputSaveButton = { "container": mainWindow, "id": "saveManualInputButtonId", "type": "CircularButton"}
manualInputCancelButton = { "container": mainWindow, "id": "cancelManualInputButtonId", "type": "CircularButton", "visible": True}
manualInputCloseButton = {"container": mainWindow, "id": "closeManualInputButtonId", "type": "CloseDialogButton", "visible": True}


#Function to give input to weight and height
def setWeightAndHeightInMonitorScreen(weight,height):
    try:
        if object.exists(manualInputweightBox):
            wt=(waitForObject(manualInputweightBox))
            wt.text=""
            type(waitForObject(manualInputweightBox),weight)
        if object.exists(manualInputheightBox):
            ht = (waitForObject(manualInputheightBox))
            ht.text=""
            type(waitForObject(manualInputheightBox),height)
            type(waitForObject(manualInputheightBox),"<tab>")
            
        else:
            pass
    except Exception as e:
        test.fail("Exception"+str(e)) 

#Function to save the values in monitor screen
def saveTheValuesInMonitorScreen():
    try:
        if object.exists(manualInputweightBox):
            mouseClick(waitForObject(manualInputSaveButton))
            test.log("Successfully saved the values") 

    except Exception as e:
        test.fail("Exception"+str(e)) 

#Function to cancel the values in live settings screen
def cancelTheValuesInTheMonitorScreen(weight="",height=""):
    try:
        
        if waitForObject(manualInputCancelButton):
            mouseClick(waitForObject(manualInputCancelButton))
            test.log("The values are cancelled")
            
            if object.exists(liveScreenMonitor):
                weightInLiveScreen =str(waitForObject(liveScreenWeightText).text)
                test.log("sensitivityOfECGInLiveScreen=%s" %weightInLiveScreen)
    
            if object.exists(liveScreenMonitor):
                heightInLiveScreen =str(waitForObject(liveScreenHeightText).text)
                test.log("sensitivityOfECGInLiveScreen=%s" %heightInLiveScreen)
                
                
            if weight ==weightInLiveScreen and height==heightInLiveScreen:
                test.passes("Successfully cancelled the values in the live settings screen")
            else:
                test.fail("Values are not cancelled in the live settings screen")
                
        return True
       
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to close monitor screen and navigate back to live screen
def closeMonitorScreenAndNavigateToLiveScreen():
    try:
        status = False        
        if waitForObject(manualInputCloseButton):
            mouseClick(waitForObject(manualInputCloseButton))
            snooze(1)            
            if object.exists(liveScreenPatientListButton):
                test.log("Successfully navigate to waveform screen")
                status = True
            else:
                test.log("Failed to navigate to waveform screen")
                status = False
        else:
            test.log("Failed to find manual input close button")
                
        return status
       
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to close the values in live settings screen
def closeTheValuesInTheMonitorScreen(weight="",height=""):
    try:
        
        if waitForObject(manualInputCloseButton):
            mouseClick(waitForObject(manualInputCloseButton))
            
            if object.exists(liveScreenMonitor):
                weightInLiveScreen =str(waitForObject(liveScreenWeightText).text)
                test.log("sensitivityOfECGInLiveScreen=%s" %weightInLiveScreen)
    
            if object.exists(liveScreenMonitor):
                heightInLiveScreen =str(waitForObject(liveScreenHeightText).text)
                test.log("sensitivityOfECGInLiveScreen=%s" %heightInLiveScreen)
                
                
            if weight ==weightInLiveScreen and height==heightInLiveScreen:
                test.passes("Successfully cancelled the values in the live settings screen")
            else:
                test.fail("Values are not cancelled in the live settings screen")
                
        return True
       
    except Exception as e:
        test.fail("Exception" +str(e))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    











