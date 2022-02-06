#source(findFile('scripts', '../../../globalScripts/utils.py'))
#productCode=getProduct()


'''Objects of mainwindow's in every screen'''

summaryScreen_Mainwindow = {"container": mainWindow, "type": "Rectangle", "visible": True}
mainWindow = {"type": "QQuickWindowQmlImpl", "visible": True}
onlineScreen_MainWindow ={"container": mainWindow, "id": "onlineScreenId", "type": "OnlineWfScreen", "visible": True}
patientCardScreen_MainWindow = {"container": mainWindow, "id": "patientScreenId", "type": "PatientCard", "unnamed": 1, "visible": True}
menuScreen_MainWindow = {"container": mainWindow, "id": "menuScreenId", "type": "Rectangle", "unnamed": 1, "visible": True}
evaluationScreen_MainWindow = {"container": mainWindow, "id": "evaluationScreenId", "type": "EvalScreen", "visible": True}
evaluationSettingsScreen_Mainwindow = {"container": mainWindow, "type": "Rectangle", "visible": True}
evaluationSummaryScreen_Mainwindow = {"container": mainWindow, "id": "diagSummary", "type": "DiagnosticSummary", "unnamed": 1, "visible": True}
liveAddPatientScreen_Mainwindow = {"container": mainWindow, "id": "patientScreenRootId", "type": "Rectangle", "unnamed": 1, "visible": True}
livePatientListScreen_Mainwindow = {"container": mainWindow, "id": "patientScreenRootId", "type": "Rectangle", "visible": True}

evaluationScreenSummaryButton = {"checkable": False, "container": mainWindow, "id": "summarybuttonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}

summaryDialogTitleId = {"container": mainWindow, "text": "Summary", "type": "Label", "unnamed": 1, "visible": True}
summaryResultsTabButton = {"checkable": True, "container": mainWindow, "id": "resultsTabButtonId", "text": "Results", "type": "TabButton", "unnamed": 1, "visible": True}
summaryAmplitudesTabButton = {"checkable": True, "container": mainWindow, "id": "amplitudesTabButtonId","type": "TabButton", "unnamed": 1, "visible": True}
summaryAvgComplexTabButton = {"checkable": True, "container": mainWindow, "id": "avgComplexesTabButtonId", "text": "Avg. Complex", "type": "TabButton", "unnamed": 1, "visible": True}
summaryPlaceHolder = {"container": mainWindow, "id": "placeholder", "type": "PlaceholderText", "unnamed": 1, "visible": True}
summaryConclusionInput = {"backgroundcolor": "#fcfcfc", "container": mainWindow, "echoMode": 0, "id": "conclusionInputId", "type": "TextField", "unnamed": 1, "visible": True}
summarySaveButton = {"checkable": False, "container": mainWindow, "id": "saveSummaryButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
summaryCloseButton = {"container": mainWindow, "id": "closeSummaryButtonId", "type": "CloseDialogButton", "unnamed": 1, "visible": True}
summaryAmplitudeTable = {"container": mainWindow, "id": "amplitudes", "type": "Amplitudes", "visible": True}
summaryConclusionTextArea = {"container": mainWindow, "id": "conclusionTextAreaId", "type": "TextArea", "visible": True}
summaryHiddenKey = {"container": mainWindow, "id": "hideKeyBackground", "type": "Rectangle", "visible": True}
summaryAvgComplexGraph = {"container": mainWindow, "id": "averageComplexes", "type": "AverageComplexes",  "visible": True}
summaryConclusionText = {"container": mainWindow, "id": "conclusionTextAreaId", "type": "TextArea",  "visible": True}



'''Objects of mainwindow's in every screen'''

summaryScreen_Mainwindow = {"container": mainWindow, "type": "Rectangle", "visible": True}
mainWindow = {"type": "QQuickWindowQmlImpl", "visible": True}
onlineScreen_MainWindow ={"container": mainWindow, "id": "onlineScreenId", "type": "OnlineWfScreen", "visible": True}
patientCardScreen_MainWindow = {"container": mainWindow, "id": "patientScreenId", "type": "PatientCard", "unnamed": 1, "visible": True}
menuScreen_MainWindow = {"container": mainWindow, "id": "menuScreenId", "type": "Rectangle", "unnamed": 1, "visible": True}
evaluationScreen_MainWindow = {"container": mainWindow, "id": "evaluationScreenId", "type": "EvalScreen", "visible": True}
evaluationSettingsScreen_Mainwindow = {"container": mainWindow, "type": "Rectangle", "visible": True}
evaluationSummaryScreen_Mainwindow = {"container": mainWindow, "id": "diagSummary", "type": "DiagnosticSummary", "unnamed": 1, "visible": True}
liveAddPatientScreen_Mainwindow = {"container": mainWindow, "id": "patientScreenRootId", "type": "Rectangle", "unnamed": 1, "visible": True}
livePatientListScreen_Mainwindow = {"container": mainWindow, "id": "patientScreenRootId", "type": "Rectangle", "visible": True}

evaluationScreenSummaryButton = { "container": mainWindow, "id": "summarybuttonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}

summaryDialogTitleId = {"container": mainWindow, "text": "Summary", "type": "Label", "unnamed": 1, "visible": True}
summaryResultsTabButton = {"container": mainWindow, "id": "resultsTabButtonId", "type": "TabButton", "visible": True}
summarySummaryTabButton = {"container": mainWindow, "id": "summaryTabButtonId", "type": "TabButton", "visible": True}

summaryAmplitudesTabButton = {"container": mainWindow, "id": "amplitudesTabButtonId", "type": "TabButton", "unnamed": 1, "visible": True}
summaryAvgComplexTabButton = { "container": mainWindow, "id": "avgComplexesTabButtonId", "type": "TabButton", "unnamed": 1, "visible": True}
summaryPlaceHolder = {"container": mainWindow, "id": "placeholder", "type": "PlaceholderText", "unnamed": 1, "visible": True}
summaryConclusionInput = {"container": mainWindow, "echoMode": 0, "id": "conclusionInputId", "type": "TextField", "unnamed": 1, "visible": True}
summarySaveButton = { "container": mainWindow, "id": "saveButtonId", "type": "CircularButton","visible": True}
summaryCloseButton = {"container": mainWindow, "id": "closeSummaryButtonId", "type": "CloseDialogButton", "visible": True}
summaryAmplitudeTable = {"container": mainWindow, "id": "amplitudes", "type": "Amplitudes", "visible": True}
summaryConclusionTextArea = {"container": mainWindow, "id": "conclusionTextAreaId", "type": "TextArea", "visible": True}
summaryHiddenKey = {"container": mainWindow, "id": "hideKeyBackground", "type": "Rectangle", "visible": True}
summaryAvgComplexGraph = {"container": mainWindow, "id": "averageComplexes", "type": "AverageComplexes",  "visible": True}
summaryConclusionText = {"container": mainWindow, "id": "conclusionTextAreaId", "type": "TextArea",  "visible": True}
summaryDiagSummaryHRId = {"container": mainWindow, "id": "diagSummaryHRId", "type": "Label", "visible": True}
summaryParameterNamesAreaId = {"container": mainWindow, "id": "parameterNamesAreaId", "type": "Item", "visible": True}
summaryEvalWfId1 = {"container": mainWindow, "id": "evalWfId1", "type": "Item", "visible": True}
summaryEvalWfId2 = {"container": mainWindow, "id": "evalWfId2", "type": "Item", "visible": True}
summaryEvalWfId3 = {"container": mainWindow, "id": "evalWfId3", "type": "Item", "visible": True}
summaryEvalWfId4 = {"container": mainWindow, "id": "evalWfId4", "type": "Item", "visible": True}

showMoreButtonId = {"container": mainWindow, "id": "showMoreButtonId", "type": "Item", "visible": True}
summaryDiagSummaryHRId7Inch = {"container": mainWindow, "id": "heartRateId", "type": "Label", "visible": True}

hideKeyIcon = {"container": mainWindow, "id": "hideKeyIcon", "type": "Image", "visible": True}

conclusionTextAreaId={"container": mainWindow, "id": "conclusionTextAreaId", "type": "TextArea", "unnamed": 1, "visible": True}
newconclusionInputId={"container": mainWindow, "id": "newconclusionInputId", "type": "PatientInfoField", "unnamed": 1, "visible": True}
statusButtonId={"container": mainWindow, "id": "statusButtonId", "type": "MedicalStatementStausButton", "unnamed": 1, "visible": True}


#Function to navigate summary results
def navigateToSummaryResults():
    try:
        if object.exists(summaryResultsTabButton):
            mouseClick(waitForObject(summaryResultsTabButton))
            snooze(1)
            if object.exists(summaryPlaceHolder):
                test.passes("Successfully summary results is displayed")
            else:
                test.fail("Summary results is not displayed")
                
        return True  
             
    except Exception as e:
        test.fail(str(e))     
         
#Function to navigate summary amplitudes
def navigateToSummaryAmplitudes():
    try:
        if object.exists(summaryAmplitudesTabButton):
            mouseClick(waitForObject(summaryAmplitudesTabButton))
            snooze(1)
            if object.exists(summaryAmplitudeTable):
                test.passes("Successfully summary amplitudes is displayed")
                return True
            else:
                test.fail("Summary amplitudes is not displayed")
                return False 
             
    except Exception as e:
        test.fail(str(e))     
         
#Function to navigate summary avg complex
def navigateToSummaryAvgComplex():
    try:
        if object.exists(summaryAvgComplexTabButton):
            mouseClick(waitForObject(summaryAvgComplexTabButton))
            snooze(1)
            
            if object.exists(summaryAvgComplexGraph):
                test.passes("Successfully summary avg complex is displayed")
            else:
                test.fail("Summary avg complex is not displayed")
                
        return True  
             
    except Exception as e:
        test.fail(str(e))     
        
#Function to navigate summary placeholder
def navigateToSummaryPlaceHolder():
    try:
        if object.exists(summaryConclusionTextArea):
            mouseClick(waitForObject(summaryConclusionTextArea))
            snooze(1)
            if object.exists(summaryConclusionTextArea):
                test.passes("Successfully summary conclusion screen is displayed")
            else:
                test.fail("Summary conclusion screen is not displayed")
                
        return True
             
    except Exception as e:
        test.fail(str(e))     

#Function to save in summary screen                   
def saveInSummaryScreen(): 
    try:
        if object.exists(summarySaveButton):
            mouseClick(waitForObject(summarySaveButton)) 
            snooze(2)
            if object.exists(evaluationScreen_MainWindow):
                test.log("Successfully saved and evaluation screen is displayed ")
            else:
                test.fail("Not saved and evaluation screen is not displayed")
                
        return True       

    except Exception as e:
        test.fail("Exception"+str(e))    
        
#Function to close in summary screen                   
def closeInSummaryScreen(): 
    try:
        if object.exists(summaryCloseButton):
            mouseClick(waitForObject(summaryCloseButton)) 
            snooze(5)
            
            if object.exists(evaluationScreenSaveRecordButton):
                test.log("Successfully closed and evaluation screen is displayed ")
                return True
            else:
                test.fail("Not closed and evaluation screen is not displayed")
                return False       

    except Exception as e:
        test.fail("Exception"+str(e))       
                
#Function to navigate summary placeholder
def summaryTextPlaceHolder(message):
    try:
        if object.exists(summaryConclusionTextArea):
            mouseClick(waitForObject(summaryConclusionTextArea))
            snooze(1)
            mouseClick(waitForObject(summaryHiddenKey))
            snooze(1)
            msg=(waitForObject(summaryConclusionTextArea))
            snooze(1)
            msg.text=""
            snooze(1)
            type(waitForObject(summaryConclusionTextArea),message)
            snooze(1)
            
            mouseClick(waitForObject(summarySaveButton)) 
            snooze(1)
            mouseClick(waitForObject(evaluationScreenSummaryButton)) 

        
        return True
             
    except Exception as e:
        test.fail(str(e))            
        
#Function to verify the placeholder text in the summary screen        
def verifyTheplaceHolderTextInTheSummaryScreen(message):
    try:
        if object.exists(summaryConclusionText):
            placeHolderTextInSummaryScreen =str(waitForObject(summaryConclusionText).text)
            
            if placeHolderTextInSummaryScreen==str(message):
                test.passes("Given message %s and Displayed message %s are matched in the summary screen"%(message,placeHolderTextInSummaryScreen))
            else:
                test.fail("Given message %s and Displayed message %s values are not matched in the summary screen"%(message,placeHolderTextInSummaryScreen))       
        
        return True
             
    except Exception as e:
        test.fail(str(e))  
        
        
#Function to configure conclusion in summary placeholder
def setConclusionInSummary(conclusionText):
    try:
        count = 0    
        if waitForObject(summaryConclusionTextArea):
            type(waitForObject(summaryConclusionTextArea), conclusionText)
            snooze(1)
            mouseClick(waitForObject(summaryAmplitudesTabButton))
            mouseClick(waitForObject(summaryResultsTabButton))
            test.log(" Successfully entered given text in conclusion section '%s' "%conclusionText)
            count = 1
        else:
            test.log(" Conclusion section is not available to enter ")
                
        if count == 1:
            return True
        else:
            return False
             
    except Exception as e:
        test.fail(str(e))     

conclusionTextAreaId={"container": mainWindow, "id": "conclusionTextAreaId", "type": "TextArea", "unnamed": 1, "visible": True}      
#Function to get conclusion text from summary placeholder
def getConclusionSummaryFromPreview_Screen():
    try:
        summaryText = ""
        if waitForObject(conclusionTextAreaId):
            summaryObject=waitForObject(conclusionTextAreaId)
            summaryText = summaryObject.text
            test.log(" Successfully get the text from conclusion section ")
    
        else:
            test.log("fail to get the text from Conclusion ")
            
        return  summaryText
             
    except Exception as e:
        test.fail(str(e)) 

#Function to edit conclusion text from summary place holder
def editConclusionSummaryFromPreview(conclusionEditText):
    try:
        count = 0
        if waitForObject(summaryConclusionTextArea):
            conclusionObject=waitForObject(summaryConclusionTextArea)
            conclusionObject.clear()
            type(conclusionObject,conclusionEditText)
            snooze(1)           
            test.log(" Successfully edit the text in conclusion section ")
            count = 1
        else:
            test.log(" Fail to edit the text in Conclusion section ")
            
        if count == 1:
            return True
        else:
            return False
             
    except Exception as e:
        test.fail(str(e)) 

#Function to save in summary screen in Evaluation                  
def saveSummaryScreenEvaluation(): 
    try:
        count = 0
        if waitForObject(summarySaveButton):
            mouseClick(waitForObject(summarySaveButton)) 
            snooze(1)
            if waitForObject(evaluationScreenSaveRecordButton):
                test.log("Successfully saved summary page and evaluation screen is displayed ")
                count = 1
            else:
                test.log(" Evaluation screen is not displayed ")
        else:
            test.log(" Summary save button is not displayed ")
                
        if count == 1:
            return True
        else:
            return False      

    except Exception as e:
        test.fail("Exception"+str(e))  
        
#Function to save in summary screen in preview                  
def saveSummaryScreenPreview(): 
    try:
        count = 0
        if waitForObject(summarySaveButton):
            mouseClick(waitForObject(summarySaveButton)) 
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
        
#Function to close in summary screen                   
def closeInSummaryScreen(): 
    try:
        count = 0
        if waitForObject(summaryCloseButton):
            mouseClick(waitForObject(summaryCloseButton)) 
            snooze(1)
            
            if waitForObject(evaluationScreenSaveRecordButton):
                test.log("Successfully closed summary page and evaluation screen is displayed ")
                count = 1
            else:
                test.log("Not closed summary page and evaluation screen is not displayed")
                
        if count == 1:
            return True
        else:
            return False   

    except Exception as e:
        test.fail("Exception"+str(e))       
                
#Function to navigate summary placeholder
def summaryTextPlaceHolder(message):
    try:
        if waitForObject(summaryConclusionTextArea):
            mouseClick(waitForObject(summaryConclusionTextArea))
            snooze(1)
            mouseClick(waitForObject(summaryHiddenKey))
            snooze(1)
            msg=(waitForObject(summaryConclusionTextArea))
            snooze(1)
            msg.text=""
            snooze(1)
            type(waitForObject(summaryConclusionTextArea),message)
            snooze(1)
            
            mouseClick(waitForObject(summarySaveButton)) 
            snooze(1)
            mouseClick(waitForObject(evaluationScreenSummaryButton)) 

        
        return True
             
    except Exception as e:
        test.fail(str(e))            
        
#Function to verify the placeholder text in the summary screen        
def verifyTheplaceHolderTextInTheSummaryScreen(message):
    try:
        if waitForObject(summaryConclusionText):
            placeHolderTextInSummaryScreen =str(waitForObject(summaryConclusionText).text)
            
            if placeHolderTextInSummaryScreen==str(message):
                test.log("Given message %s and Displayed message %s are matched in the summary screen"%(message,placeHolderTextInSummaryScreen))
            else:
                test.log("Given message %s and Displayed message %s values are not matched in the summary screen"%(message,placeHolderTextInSummaryScreen))       
        
        return True
             
    except Exception as e:
        test.fail(str(e))  
        
        
#Method to get Heart rate in summary screen                   
def getHeartRateFromSummary(): 
    try:
        count = 0
        if(productCode=='lx'): 
        
            if waitForObject(summaryDiagSummaryHRId7Inch):
                summaryHRObj =  str(waitForObject(summaryDiagSummaryHRId7Inch).text)
                count = 1
                test.log(" Successfully get the HR from summary ")               
            else:
                test.log(" Failed to get the HR from summary screen ")
        else:             
            if waitForObject(summaryDiagSummaryHRId):
                summaryHRObj =  str(waitForObject(summaryDiagSummaryHRId).text)
                count = 1
                test.log(" Successfully get the HR from summary ")                
            else:
                test.log(" Failed to get the HR from summary screen ")
                
        if count == 1:
            return summaryHRObj
        else:
            return False   

    except Exception as e:
        test.fail("Exception"+str(e))         
        
#Method to verify amplitudes parameter options
def verifyAmplitudesParameter():
    try:
        count =0
        if waitForObject(summaryAmplitudeTable):
            test.log(" Amplitudes parameters are displayed in amplitudes tab ")
            count =1
        else:
            test.log(" Amplitudes parameters are not displayed in amplitudes tab ")
                
        if count == 1:
            return True
        else:
            return False
             
    except Exception as e:
        test.fail(str(e))        
        
#Function to navigate summary summary tab
def navigateToSummarySummary():
    try:
        count = 0
        
        if waitForObject(summarySummaryTabButton):
            mouseClick(waitForObject(summarySummaryTabButton))
            snooze(.5)
            if(productCode=='lx'):
                count =1
                pass
            else:
                if waitForObject(summaryPlaceHolder):
                    test.log("Successfully summary results is displayed")
                    count =1
                else:
                    test.log("Summary results is not displayed")              
        if count == 1:
            return True
        else:
            return False
             
    except Exception as e:
        test.fail(str(e)) 
        

#Function to hide virtual keyboard
def hideVirtualKeyboard():
    try:
        count = 0
        
        if waitForObject(hideKeyIcon):
            mouseClick(waitForObject(hideKeyIcon))
            snooze(.5)
            count =1           
        if count == 1:
            return True
        else:
            return False
             
    except Exception as e:
        test.fail(str(e))         
        
newconclusionInputId={"container": mainWindow, "id": "newconclusionInputId", "type": "PatientInfoField", "unnamed": 1, "visible": True}
statusButtonId={"container": mainWindow, "id": "statusButtonId", "type": "MedicalStatementStausButton", "unnamed": 1, "visible": True}
      
def addingMedicalstatementinPreviewscreen(list1,n):
    try:
        count=0
        for x in list1:
            if object.exists(newconclusionInputId):
                setFocusTextBox(newconclusionInputId)
                type(mainWindow,x)
                if object.exists(statusButtonId):
                    mouseClick(statusButtonId)
                    snooze(3)
                    count=count+1
        return True if count==n else False
    
    except Exception as e:
        test.fail(str(e))         
        
conclusionListViewId={"container": mainWindow, "id": "conclusionListViewId", "type": "ListView", "unnamed": 1, "visible": True}
       
def getMedicalStatementFromPreviewScreen(list1):
    try:
        count=0
        medicalstatement=[]
        
        if waitForObject(conclusionListViewId):
            summaryObject=waitForObject(conclusionListViewId)
            item = object.children(summaryObject)
            rowParent = object.children(item[0])
            
            for j in  rowParent:        
                rowchild = object.children(j)     
                
                if len(rowchild)>0:
                    #row = object.children(rowchild[1]) 
                    medstatement=str(rowchild[1].text)
                    medicalstatement.append(medstatement)
            
            for x in list1:
                for y in medicalstatement:
                    if x==y:
                        count=count+1
    
        return True if count==5 else False
             
    except Exception as e:
        test.fail(str(e))    
        
        