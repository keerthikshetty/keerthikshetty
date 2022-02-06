
import os
import __builtin__
#Function to take the screenshot

#writing into text file


def writeintotextfile():
 try:
    outfile = os.path.join(os.getcwd(), os.path.basename('/home/testautomation/createpatientsaveanddelete')+ ".tmp")
    outfile = outfile.replace("/", os.sep)
    test.log("Writing %s" % outfile)
    file = open(outfile, "w")
 except Exception as fileerror:
     test.log('Exception'+str(fileerror))
    

def takeScreenShot():
    recordingTime = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
    fileLocation=squishinfo.testCase
    fileNameList=fileLocation.split('/')
    fileName=fileNameList[len(fileNameList)-1]
    saveDesktopScreenshot("/home/siddhi/Desktop/%s_%s_%s.png" )
    #saveDesktopScreenshot("/home/siddhi/Desktop/screenShotLongRuns/%s_%s_%s.png" %(fileName,stepNo,recordingTime))
    
#Function to take the screenshot for ecgDiag
def takeScreenShotEcgDiag(fileName):
    recordingTime = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
    saveDesktopScreenshot("/home/prashant/Desktop/ecgDiagScreenshots/%s.png" %fileName)
    
'''#Function to take the screenshot
def takeScreenShot():
    recordingTime = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
    fileLocation=squishinfo.testCase
    fileNameList=fileLocation.split('/')
    fileName=fileNameList[len(fileNameList)-1]
    saveDesktopScreenshot("/home/prashant/Desktop/screenShotLongRuns/%s %s.png" %(fileName,recordingTime))'''

#Method to find the configuration of device
def getConfigurationOfDevice():
    try:
        if object.exists(onlineScreenSettngsButtonLX): 
            return "LX"
        else:
            return "LXPlus"
    except Exception as e:
        test.fail("Exception" +str(e))
# Method to set focus on text field 
def setFocusTextBox(obj):
    try:
        targetTextBox=obj
        if (findObject(targetTextBox)):
            mouseClick(targetTextBox)

        else:
            test.log("Unable to set focus on text box ")            
    except Exception as e:
        test.fail("Exception" +str(e)) 
        
# Method to Create a patient and acquire ECG and save ECG
def createPatientAndSave():
    sName = "Hota"
    fName = "Debasish"
    pTitle = "Er"
    pDOB = "12 05 1988"
    pAge = ""
    pID = "pid@1012"
    hID = "hid@115"
    pWeight = "75"
    pHeight = "250"
    pGender = "Male"
    pPaceMaker = "Yes"
    pDigoxin = "No"
    try:
        state = "Fail"
        if navigateToPatientListScreenFromLiveScreen():
            if navigateToAddPatientScreenFromPatientListScreen():
                state = addNewPatientInLivePatientListScreen(Surname=sName,Firstname=fName,Title=pTitle,PatientDOB=pDOB,PatientAge=pAge,PatientId=pID,HospitalId=hID,Weight=pWeight,Height=pHeight,Gender=pGender,PaceMaker=pPaceMaker,Digoxin=pDigoxin)          
                if state:
                    status = saveAddPatientScreenInPatientListScreen()
                    if status:
                        test.log("Successfully navigate to Waveform screen with same patient")
                        state = "Pass"
                    else:
                        test.log(" Failed to navigate to waveform screen ")
                else:
                    test.log("Fail to add patient details for each field in addPatient screen") 
            else:
                test.log("Failed to navigate to add patient screen from patient list screen")
        else:
            test.log("Failed to navigate to patient list screen from live screen ")        
        if state == "Pass":
            return True
        else:
            return False
                    
    except Exception as e:
        test.fail("Exception" +str(e)) 
        
#Method to acquire and save ECG record
def acquireAndSave():
    try:
        status = "Fail"        
        if clickOnECGRecordButtonInLiveScreen():
            snooze(2)
            if saveECGRecordInEvaluationScreen():
                snooze(2)
                status = "Pass"               
            else:
                test.log("Failed to find save ECG record button")               
        else:
            test.log("Failed to find Record button")
        if status == "Pass":
            return True
        else:
            return False
                    
    except Exception as e:
        test.fail("Exception" +str(e)) 
        
#Method to delete patient record in patient card screen
def deletePatientPatientCard():
    patientList = ["pid@1012"]
    noOfPatientRecord = len(patientList)
    userInput = "Confirm"
    try:
        status = "Fail"
        if navigateToMenuScreenFromLiveScreen():
            if navigateToPatientCardScreenFromMenuScreen():
                test.log(" Device navigate to patient card from menu screen")
            else:
                test.log("Failed to navigate to patient card screen from Menu screen")
        else:
            test.log("Device fails to navigate menu screen from waveform screen")
        if searchAndSelectPatientToDeleteInPatientCardScreen(patientList):
            if deletePatientInPatientCard(userInput,noOfPatientRecord):                
                test.log("Device navigate back to Patient card screen")
            else:
                test.log("Failed to navigate to patient card screen")                
        else:
            test.log("Could not able to find patient details for patient ID : %s"%pID)
        '''Navigate to waveform screen'''
        if navigateToLiveScreenFromPatientCardScreen():
            test.log(" Successfully navigate to waveform screen")
            status = "Pass"
            test.log("Number of Iteration is : %s"%str(i))
        else:
            test.log(" Failed to navigate to waveform screen")  
            status = "Fail"
        if status == "Pass":
            return True
        else:
            return False
                    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Method to navigate to auto profile from live screen
def navigateBetweenLiveAndAutoProfileSettingScreen():
    try:
        status = False
        step1= navigateToMenuScreenFromLiveScreen()
        snooze(1)
        step2 = navigateToSettingsScreenFromMenuScreen()
        snooze(1)
        step3 = navigateToProfileButtonInSettingsScreen()
        snooze(1)
        step4 = navigateToAutoProfileInSettingsScreen()
        if step1 and step2 and step3 and step4 :
            test.log("Successfully navigate to Auto profile in setting screen")
            status = True
        else:
            test.log("Failed to navigate to Auto profile in setting screen")
        return status
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Method to navigate to live screen from setting screen
def navigateLiveScreenFromSettingScreen():
    try:
        status = False
        step1 = backPressInSettingsScreen()
        snooze(1)
        step2 = navigateToLiveScreenFromMenuScreen()
        if step1 and step2 :
            test.log("Successfully navigate to Live screen from Menu screen")
            status = True
        else:
            test.log("Failed to navigate to Live screen from Menu screen")
        return status
    except Exception as e:
        test.fail("Exception" +str(e)) 
        
#Method to navigate to examination screen for selected patient 
def navigateExaminationScreenFromLiveScreenForSelectedPatient(pID):
    try:
        status = False
        snooze(1)
        step1 = navigateToMenuScreenFromLiveScreen()
        snooze(1)
        step2 = navigateToPatientCardScreenFromMenuScreen()
        snooze(1)
        step3 = searchThePatientDetailsToNavigateToExaminationPageFromPatientCardScreen(pID)
        snooze(1)
        if step1 and step2 and step3 :
            test.log("Successfully navigate to examination screen from live screen")
            status = True
        else:
            test.log("Failed to navigate to examination screen from live screen")
            status = False        
        return status
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Method to navigate to live screen for examination screen 
def navigateLiveScreenFromExaminationScreen():
    try:
        status = False
        snooze(1)
        if object.exists(patientCardAddPatientBackButton):
            mouseClick(waitForObject(patientCardAddPatientBackButton))
            snooze(1)            
        else:
            test.log("Failed to find patient card Add patient back button")
        if navigateToLiveScreenFromPatientCardScreen():
            test.log(" Successfully navigate to waveform screen")
            status = True
        else:
            test.log(" Failed to navigate to waveform screen")
            status = False
        return status
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Method to navigate to add patient screen from live screen
def navigateaddPatientScreenFromLiveScreen():
    try:
        status = False
        snooze(2)
        status1 = navigateToPatientListScreenFromLiveScreen()
        snooze(1)
        status2 = navigateToAddPatientScreenFromPatientListScreen()
        if status1 and status2 :
            test.log("Successfully navigate to add patient screen from patient list screen")
            status = True
        else:
            test.log("Failed to navigate to add patient screen from live screen")
        return status
    except Exception as e:
        test.fail("Exception" +str(e))    
#Method to navigate between live screen and patient card screen
def navigateBetweenLiveAndPatientList():
    try:
        status = "Fail" 
        snooze(1)       
        status1 = navigateToPatientListScreenFromLiveScreen()
        snooze(1)
        status2 = navigateToAddPatientScreenFromPatientListScreen()
        snooze(1)
        status3 = navigateToPatientListScreenFromAddPatientScreenBackButton()
        snooze(1)
        status4 = navigateToLiveScreenFromPatientListScreenBackButton()
        snooze(1)
        if status1 and status2 and status3 and status4 :                        
            status = "Pass"                       
        if status == "Pass":
            return True
        else:
            return False
    except Exception as e:
        test.fail("Exception" +str(e)) 

#Method to navigate between live screen and patient card screen
def navigateBetweenLiveAndPatientCard():
    try:
        status = "Fail"
        status1 = navigateToMenuScreenFromLiveScreen()
        snooze(1)
        status2 = navigateToPatientCardScreenFromMenuScreen()
        snooze(1)
        status3 = navigateToAddPatientFromPatientCardScreen()
        snooze(1)
        status4 = navigateToPatientCardScreenFromAddPatientScreen()
        snooze(1)
        status5 = navigateToLiveScreenFromPatientCardScreen()
        if status1 and status2 and status3 and status4 and status5 :                       
            status = "Pass"                             
        else:
            test.log("Failed to navigate to waveform screen from patient card screen")
        if status == "Pass":
            return True
        else:
            return False   
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Method to navigate between live screen and work list screen
def navigateBetweenLiveAndWorkListScreen():
    try:
        status = "Fail"
        status1 = navigateToMenuScreenFromLiveScreen()
        snooze(1)
        status2 = navigateToWorkListScreenFromMenuScreen()
        snooze(1)
        status3 = navigateToMenuScreenFromWorkListScreen()
        snooze(1)
        status4 = navigateToLiveScreenFromMenuScreen()
        if status1 and status2 and status3 and status4 :                       
            status = "Pass"                             
        else:
            test.log("Failed to navigate to waveform screen from patient card screen")
        if status == "Pass":
            return True
        else:
            return False   
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Method to navigate between live screen and user screen
def navigateBetweenLiveAndUserScreen():
    try:
        status = "Fail"
        status1 = navigateToMenuScreenFromLiveScreen()
        snooze(1)
        status2 = navigateToUserScreenFromMenuScreen()
        snooze(1)
        status3 = navigateToMenuScreenFromUserScreen()
        snooze(1)
        status4 = navigateToLiveScreenFromMenuScreen()
        if status1 and status2 and status3 and status4 :                       
            status = "Pass"                             
        else:
            test.log("Failed to navigate to waveform screen from patient card screen")
        if status == "Pass":
            return True
        else:
            return False   
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Method to navigate between live screen and evaluation screen
def navigateBetweenLiveAndEvaluationscreen():
    try:
        status = "Fail"
        status1 = clickOnECGRecordButtonInLiveScreen()
        snooze(2)
        status2 = navigateToEvaluationSummaryScreenFromEvaluationScreen()
        snooze(2)
        status3 = navigateToEvaluationSummaryScreenAmplitudeTab()
        snooze(1)
        status4 = navigateToEvaluationSummaryScreenAverageComplexTab()
        snooze(1)
        status5 = navigateToEvaluationSummaryFromSummaryScreen()
        snooze(2)
        status6 = navigateToEvaluationSettingsScreenFromEvaluationScreen()
        snooze(2)
        status7 = closeTheEvaluationSettingsScreen()
        snooze(2)
        status8 = deleteECGRecordInEvaluationScreen()
        if status1 and status2 and status3 and status4 and status5 and status6 and status7 and status8 :                       
            status = "Pass"                             
        else:
            test.log("Failed to navigate to waveform screen from patient card screen")
        if status == "Pass":
            return True
        else:
            return False   
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Method to navigate between live screen and settings screen
def navigateBetweenLiveAndSettings():
    try:
        status = "Fail"
        status1 = navigateToMenuScreenFromLiveScreen()
        snooze(1)
        status2 = navigateToSettingsScreenFromMenuScreen()
        snooze(1)
        status3 = navigateToGeneralInSettingsScreen()
        snooze(1)
        status4 = navigateToNetworkInSettingsScreen()
        snooze(1)
        status5 = navigateToServiceInSettingsScreen()
        snooze(1)
        status6 = navigateToAboutProfileInSettingsScreen()
        snooze(1)
        status7 = navigateToExportInSettingsScreen()
        snooze(1)
        status8 = navigateToProfileButtonInSettingsScreen()
        snooze(1)
        status9 = navigateToAutoProfileInSettingsScreen()
        snooze(1)
        status10 = navigateToManualProfileInSettingsScreen()
        snooze(1)
        status11 = navigateToRhythmProfileInSettingsScreen()
        snooze(1)
        status12 = backPressInSettingsScreen()
        snooze(1)
        status13 = navigateToLiveScreenFromMenuScreen()
        if status1 and status2 and status3 and status4 and status5 and status6 and status7 and status8 and status9 and status10 and status11 and status12 and status13 :                       
            status = "Pass"                             
        else:
            test.log("Failed to navigate to settings screen from live screen and coming back to live screen screen")
        if status == "Pass":
            return True
        else:
            return False   
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Method to create patient in patient List screen
def createPatientPatientListScreen():
    try:
        sName = "Hota"
        fName = "Debasish"
        pTitle = "Er"
        pDOB = "12 05 1988"
        pAge = ""
        pID = "pid@1012"
        hID = "hid@115"
        pWeight = "75"
        pHeight = "250"
        pGender = "Male"
        pPaceMaker = "Yes"
        pDigoxin = "No"
        ''' Navigate to patient List screen from waveform screen'''
        
        step1=navigateToMenuScreenFromLiveScreen()
        snooze(1)
        step2=navigateToPatientCardScreenFromMenuScreen()
        snooze(2)
        step3=addNewPatientInPatientListScreen(Surname=sName,Firstname=fName,Title=pTitle,PatientDOB=pDOB,PatientAge=pAge,PatientId=pID,Weight=pWeight,Height=pHeight,Gender=pGender,PaceMaker=pPaceMaker,Digoxin=pDigoxin)
        snooze(2)
        if step1 and step2 and step3 :
            test.log("Patient details are added for each field in addPatient screen")
            status='pass'
        else:
            #takeScreenShot()
            test.log("Fail to add patient details for each field in addPatient screen")
            status='fail'
        '''Click save button in add patient screen and observe device behavior'''
        #status = setPatientForRecordingInPatientListScreen()
        if status == "pass":
            return True
        else:
            return False
                 
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Delete Patient information in Patient card screen
def deletePatientPatientcardScreen():
    try:
        patientList = ["pid@1012"]
        n = len(patientList)
        userInput = "Confirm"
        step1 = navigateToMenuScreenFromLiveScreen()
        snooze(1)
        step2 = navigateToPatientCardScreenFromMenuScreen()
        if step1 and step2 :
            test.log(" Device navigate to patient card from menu screen")
        else:
            #takeScreenShot()
            test.log("Failed to navigate to patient card screen from Menu screen")
        step3 = searchAndSelectPatientToDeleteInPatientCardScreen(patientList)
        snooze(2)
        step4 = deletePatientInPatientCard(userInput,n)
        snooze(1)
        step5 = navigateToLiveScreenFromPatientCardScreen()
        if step3 and step4 and step5 :
            snooze(1)
            return True
        else:
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to scroll the list and get the patient details in patient list screen
def scrollListInPatientListScreen():
    
    patientList=[]
    y_list = []
    
    listView = findObject(liveScreenPatientListView)
    totalIteration = listView.count/9
        

    for i in range(totalIteration):
                
        listChild=[]        
        
        listChild = waitForObject(liveScreenPatientListView)
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
  
        flick(waitForObject(liveScreenPatientListView), 0, 415)
        
    return patientList    


#Function to scroll the list and get the patient details in patient card screen
def scrollListInPatientCardScreenCommon():
    
    patientList=[]
    y_list = []
    
    listView = findObject(patientCardPatientListView)
    totalIteration = listView.count/9
    
    for i in range(totalIteration):
                
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
    
    return patientList 

# Function to search and select patient by patient ID to delete in patient card screen
def searchAndSelectPatientToDeleteInPatientCardScreenCommonMethod(patientList):
    try:
        status = False
        #global count
        patientListToDelete = patientList
        for i in range(len(patientListToDelete)):
            if object.exists(patientCardSearchInput):
                searchBox = (waitForObject(patientCardSearchInput))
                searchBox.text = ""
                type(waitForObject(patientCardSearchInput), patientListToDelete[i][1])
                patientListView = waitForObject(patientCardPatientListView)
                item = object.children(patientListView)
                row = object.children(item[0])                
                for j in row:
                    outline = object.children(j)
                    if len(outline) > 0:
                        label = object.children(outline[0])
                        value = label[1].text                
                        if (value == str(patientListToDelete[i][1])):
                            snooze(1)
                            longMouseClick(j)
                            #count = count + 1
                            test.log("The given patient is present in the patient card Screen")
                            status = True
                        else:
                            test.log("Given patient is not present in the patient list screen")
                            status = True
                            continue 
                    else:
                        status = True 
                        continue                    
            else:
                test.fail("Patient card search input object not found")
                status = True       
        return status
    
    except Exception as e:
        test.fail("Exception: " + str(e))

# Function to get Test data from Flat file

def getTestDataFromFile():
    testData={}
    try:
        if(os.path.exists("TestData.txt")):      
            strin_val=open('TestData.txt','r')
            for line in strin_val:
                print line                
                lineData= line.strip().split("-",1)
                if(len(lineData)>1):
                    for data in lineData:
                        itemData=data.split(",")
                        if(len(itemData)>1):
                            for eachitem in itemData:
                                fieldValue=eachitem.split(":")
                                if(len(fieldValue)>1):                                    
                                    testData.setdefault(lineData[0],{})[fieldValue[0]]=fieldValue[1]
                                else:
                                    test.fail("Field value not found")   
                                         
                        elif(len(itemData)==1):
                            fieldValue1=itemData[0].split(":")
                            if(len(fieldValue1)>1):                                    
                                    testData.setdefault(lineData[0],{})[fieldValue1[0]]=fieldValue1[1]                                                                    
        else:
            test.fail("file not found")
    except:
        e=sys.exc_info()
        test.log(str(e))
    return testData

#Function to select profile in live settings screen
def selectManualProfileInLive(obj, valueToSelect):
    try:
        child = waitForObject(obj)
        #valueToSelect = profileValue
        initIndex = child.currentIndex
        for i in range (child.count):
            child.currentIndex = i
            if child.currentText == str(valueToSelect):
                if str(valueToSelect) == "Manual":
                    child.altCurrentIndex = 1
                    test.log(" Given value %s is selected  "%valueToSelect)            
                    return True
                elif str(valueToSelect) == "Auto":
                    child.altCurrentIndex = 0
                    test.log(" Given value %s is selected  "%valueToSelect)            
                    return True
        child.currentIndex = initIndex
        return False

    except Exception as e:
        test.fail("Exception" +str(e)) 
        
#Function to select start recording at in settings screen
def selectStartRecordingAtProfileInSettings(obj, valueToSelect):
    try:
        child = waitForObject(obj)
        #valueToSelect = profileValue
        child1 = waitForObject(startRecordingAtComboBox)
        initIndex = child.currentOptionIndex
        for i in range (child1.count):
            child.currentOptionIndex = i
            if child.currentOptionText == str(valueToSelect):
                    child.altCurrentIndex = __builtin__.int(valueToSelect)
                    test.log(" Given value %s is selected  "%valueToSelect)            
                    return True
        child.currentOptionIndex = initIndex
        return False

    except Exception as e:
        test.fail("Exception" +str(e))

# Method to do diag testing on Demo mode
def ecgDiagProcess2(hostip,fileNameOfBebi):
    try:
        count = 0
        
        
        hostnameip = hostip
        port = 22
        username = 'root' 
        password = ''
        bebiFileName = fileNameOfBebi
              

        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostnameip,port,username,password)

        
    except Exception as e:
        test.fail("Exception" + str(e))     
      

#Method to add collected strings to list
def addtolist1(obj):
    try:
        status='fail'
        
        #string=(str(obj).strip('<font color="#ff0000"> *'))
        list1.append(str(obj))
        status='pass'
        return True if status=='pass' else False
    except Exception as a:
        test.log('exception'+str(a))
        
'--------------------------------------------------------------------'       
#Language Validation All script moved to common method
'''Prashant and Keethik-Discussion-23 jun 2021'''

#Collecting text from all the screen
def allScreenTextCollectionMethod():
    try:
        status='fail'
        step1=Manualinputscreen()
        snooze(5)
        step2=livewaveformsettingscreen()
        snooze(5)
        step3=Electrodestatuscsreenlive()   #Updated with loops
        snooze(5)
        step4= EvalutionscreenAutoprofile() #Different IDs
        snooze(5)
        step5=Menuscreentext()   #Updated with loops
        snooze(5)
        step6=Menu_Pateintcardscreen()
        snooze(5)
        step7=Menu_Worklist_screen()
        snooze(5)
        step8=loginandlogout()
        snooze(5)
        step9=Menu_User_screen()
        snooze(5)
        step10=Settings_Genralsettings_screen()
        snooze(5)
        step11=Settings_Profile_screen()
        snooze(5)
        step12=Settings_printing_screen()
        snooze(5)
        step13=Settings_Patientcard_screen()
        snooze(5)
        step14=settings_Exporttab_Screen()
        snooze(5)
        step15=Settings_Networktab_screen()
        snooze(5)
        step16=Settings_ServiceTab_screen()
        snooze(5)
        step17=Settings_AboutTab_screen()
        snooze(5)
        step18=Wavefromscreen()
        snooze(5)
        
        if step1 and step2 and step3 and step4 and step5 and step6 and step7 and step8 and step9 and step10 and step11 and step12 and step13 and step14 and step15 and step15 and step16 and step17 and step18:
            status='pass'
        else:
            status='fail'
        return True if status=='pass' else False
    
    except Exception as e:
        test.log('exception'+str(e))



'----------------------------------------------------------------------'

#Screen 1:-Live screen Manual input 
'Total number of strings in manual input screen=8'

def Manualinputscreen():
    try:
        #Navigating to manual input screen
        step1=NavigatetoManualinputscreen()
        snooze(1)
        #Collecting all the text from manual input screen
        step2=CollectManualinputscreentext()
        snooze(1)
        #Closing the manual input and moving to online screen
        step3=closeManualInputButton()
        snooze(1)
        if step1 and step2 and step3:
            status='pass'
        else:
            status='fail'
        return True if status=='pass' else False
    
    except Exception as e:
        test.log('exception'+str(e)) 
        
'-------------------------------------------------------------------------------'
#Screen 2:Live waveform settings screen

#Total Text=80

def livewaveformsettingscreen():
    try:
        #Navigating to waveform settings screen
        step1=Navigatetolivewaveformsettings()
        snooze(1)
        #Collecting the heading and profile text text from waveform settings screen
        step2=Collectlivewaveformsettingstext_title()
        snooze(1)
        #Collecting auto profile related text
        step3=Autoprofilesettings()
        snooze(2)
        #Collecting Manual profile related text
        step4=Manualprofilesettings()
        snooze(1)
        #Collecting Rhythm profile related text
        step5=Rhythmprofilesettings()
        snooze(1)
        #Closing the waveform settings screen and collecting warning message and moving to online screen
        step6=Waveformsettingstowaveformscreen()
        snooze(1)
        
        if step1 and step2 and step3 and step4 and step5 and step6:
            status='pass'
        else:
            status='fail'
        return True if status=='pass' else False
    
    except Exception as e:
        test.log('exception'+str(e)) 

'-------------------------------------------------------------------------------'

#Screen 3:Electrode status screen

def Electrodestatuscsreenlive():
    try:
        if livewaveelectordestatusscreenIEC():
            test.log('Succefully collected all the text from IEC leadmarking')
        if livewaveelectordestatusscreenAHA():
            test.log("Successfully collected all the text from electrode and navigated to waveform screen")
            test.log('Total number of strings in electrode status screen='+str(len(list1)))
                #for a in range(len(list1)):
                    #test.log(str(list1[a]))
        else:
            test.log("Failed to collect all the text from electrode  status screen")   
             
    except Exception as e:
        test.log('exception'+str(e))  

'Number of string in electrode status screen=50'
#collecting text from IEC lead marking
def livewaveelectordestatusscreenIEC():
    try:
        snooze(1)
        step1=SetIECasleadmarking()
        snooze(5)
        step2=Navigateelectrodestatusscreen()
        test.log('successfully navigated to electrode status screen')
        #Collecting text -title  
        step3=CollectelectrodestatusscreenIECAHA()
        #collecting label(N,R,L,F,C1-C6/V1-V6) and lead placement info
        step4=CollectelectrodestatusscreenIECAHA1(Label_N_RL,Label_R_RA,Label_L_LA,Label_F_LL,Label_C1_V1,Label_C2_V2,Label_C3_V3,Label_C4_V4,Label_C5_V5,Label_C6_V6)
        #closing electrode status screen and navigating to waveform screen
        step5=electrodestatustowaveformscreen()
        test.log('Navigated to the waveform screen from electrode status screen')
        if step1 and step2 and step3 and step4 and step5:
            status='pass'
        else:
            status='fail'
        
        return True if status=='pass' else False
    
    except Exception as e:
        test.log('exception'+str(e)) 
 
#Lead marking AHA and taking text of that
def livewaveelectordestatusscreenAHA():
    try:
        
        #Navigating to waveform electrode status screen
        snooze(1)
        step1=SetAHAasleadmarking()
        snooze(6)
        step2=Navigateelectrodestatusscreen()
        test.log('successfully navigated to electrode status screen')
        #Collecting text from electrode status screen-title
        step3=CollectelectrodestatusscreenIECAHA()
        snooze(1)
        #collecting label(N,R,L,F,C1-C6/V1-V6) and lead placement info
        step4=CollectelectrodestatusscreenIECAHA1(Label_N_RL,Label_R_RA,Label_L_LA,Label_F_LL,Label_C1_V1,Label_C2_V2,Label_C3_V3,Label_C4_V4,Label_C5_V5,Label_C6_V6)
        #closing electrode status screen and navigating to waveform screen
        step5=electrodestatustowaveformscreen()
        test.log('Navigated to the waveform screen from electrode status screen')
        if step1 and step2 and step3 and step4 and step5:
            status='pass'
        else:
            status='fail'
        
        return True if status=='pass' else False
    
    except Exception as e:
        test.log('exception'+str(e)) 
 
     
def SetIECasleadmarking():
    try:
        status='fail'
        #Navigate to menu screen
        step1=Onlinesccreentomenuscreen()
        snooze(0.5)
        #Navigating to settings screen
        step2=navigateToSettingsScreenFromMenuScreen()
        snooze(0.5)
        step3=Selectingleadmarkingcombo()
        snooze(0.5)
        step4=SelectingIECasleadmarking()
        snooze(0.5)
        step5=Backtomenuscreenfromsettingsscreen()
        snooze(0.5)
        step6=navigateToLiveScreenFromMenuScreen()
        snooze(0.5)
        if step1 and step2 and step3 and step4 and step5 and step6:
            test.log('sucessfully set IEC as lead marking and navigated back to online screen')
            status='pass'
        else:
            test.log('Failed set IEC as lead marking and navigated back to online screen')
            status='fail'
        return True if status=='pass' else False
    
    except Exception as e:
        test.log('exception'+str(e))
        
def SetAHAasleadmarking():
    try:
        #Navigate to menu screen
        step1=Onlinesccreentomenuscreen()
        snooze(0.5)
        #Navigating to settings screen
        step2=navigateToSettingsScreenFromMenuScreen()
        snooze(0.5)
        step3=Selectingleadmarkingcombo()
        snooze(0.5)
        step4=SelectingAHAasleadmarking()
        snooze(0.5)
        step5=Backtomenuscreenfromsettingsscreen()
        snooze(0.5)
        step6=navigateToLiveScreenFromMenuScreen()
        snooze(0.5)
        if step1 and step2 and step3 and step4 and step5 and step6:
            test.log('sucesfully set AHA as lead marking and navigated back to online screen')
            status='pass'
        else:
            test.log('Failed set AHA as lead marking and navigated back to online screen')
            status='fail'
        return True if status=='pass' else False
    
    except Exception as e:
        test.log('exception'+str(e))
        
'------------------------------------------------------------------------------------'
#Screen 4- Login screen

'Total strings=5'

def loginandlogout():
    try:
        status='fail'
        snooze(2)
        #Click Enable security and login
        step1 = navigateToMenuScreenFromLiveScreen()
        snooze(1)
        step2 = navigateToUserScreenFromMenuScreen()
        snooze(1)
        step3=acceptloginpopandnavigatetoonlinescreen()
        snooze(1)
        step4=autoLoginpopup(enableSecurityButtonId)
        snooze(1)
        #Logout from the current user
        step5=collectloginscreentext()
        snooze(1)
        step6=Navigatetoadminpasswordrecoveryscreen()
        snooze(2)
        #Login with correct credentials and navigate to online screen
        '''Make sure user ID and Password is correct'''
        step7=loginandnavigatetoonelinescreen()
        snooze(1)
        
        if step1 and step2 and step3 and step4 and step5 and step6 and step7:
            test.log('successfully collected all the items from login screen')
            status='pass'
        else:
            test.log('Failed to collect all the items from the login screen')
        
        return True if status=='pass' else False
    
    except Exception as e:
        test.log('exception'+str(e)) 
        
'-------------------------------------------------------------------------'
#Screen 5- Menu screen screen
'Total strings in menu screen=7'
def Menuscreentext():
    try:
        snooze(2)
        #Navigate to Menu screen
        snooze(6)
        step1=Onlinesccreentomenuscreen()
        snooze(2)
        step2=collectmenuscreenscreentext()
        snooze(1)
        step3=navigateToLiveScreenFromMenuScreen()
        test.log('Total number of strings in Menu screen='+str(len(list1)))
        if step1 and step2 and step3:
            status='pass'
        else:
            status='fail'
        
        return True if status=='pass' else False
    
    except Exception as e:
        test.log('exception'+str(e)) 

'--------------------------------------------------------------------------'
#Screen 6- Evaluation screen

'''Navigate to settings and set BTL adaptive work flow as record-evaluate'''
#Settings of record evaluation is not working as ID contains text-Rework on that
'Rhythm profile-Evaluation screen need to check'
#Total number of strings in Evaluation screen=49

def EvalutionscreenAutoprofile():
    try:
        status='fail'
        snooze(2)
        #Set work flow as Record and evaluate for auto profile
        #step1=SetBTLadaptiveworkflowtorecordandevaluvateAuto()
        #Record and navigate to evaluation screen
        step2=clickOnECGRecordButtonInLiveScreen()
        #collect primary strip text
        step3=collectingprimarystripword()
        #Navigate to summary screen
        step4=navigateToEvaluationSummaryScreenFromEvaluationScreen()
        #Navigating to results tab and taking results text
        step5=collectingtextfromSummaryScreenResultsTab()
        #Navigating to Amplitudes tab and collecting text
        step6=collectingtextfromSummaryScreenAmplitudesTab()
        #Navigating to avg complex tab and collecting text
        step7=collectingtextfromSummaryScreenavgcomplexTab()  
        #Navigating to Evaluation screen from summary screen  
        step8=NavigatetoEvaluationscreenfromsummaryscreen()    
        #Navigating to online screen from summary screen
        step9=NavigatetoonlinescreenfromEvaluationscreen()
        
        if step2 and step3 and step4 and step5 and step6 and step7 and step8 and step9:
            status='pass'
        else:
            status='fail'
        return True if status=='pass' else False
    except Exception as e:
        test.fail('exception'+str(e)) 
'---------------------------------------------------------------------------'
#Screen 7- Menu-Patient card screen
'''
a) Need to do rstrip in surname text
b) Need to do lstrip for mandatory field text
'''

#Total number of strings in Menu pateint card screen=28

def Menu_Pateintcardscreen():
    try:
        status='fail'
        #Create a patient in patient list and navigate to patient card screen
        step1=tst_createPatientPatientListDeletePatientPatientCard1()
        #Collecting Select all,Deslect all,Print,Export and delete,warning and delete 1 patients
        step2=Collectingalltextfrompatientcard1()
        #Collecting sorting text (Name,last exam and PID)
        step3=patientcardsortingtext(nameSortButtonId,patientidSortButtonId,lastrecordDateTimeSortButtonId)
        #Collecting 'search' text
        step4=Patientserachtext()
        #Navigating to patient add screen
        step5=navigateToAddPatientFromPatientCardScreen()
        #COllecting all the text from the patient add screen (left side)
        step6=Collectingalltextfromaddpatientcardscreen()
        #COllecting all the text from the patient add screen (Right side)
        step7=Collectingalltextfromaddpatientcardscreen1()
        #collecting male,female and other text
        step8=genderoptionsandyesorno(genderMaleRadioButtonId,genderFemaleRadioButtonId,
                                      genderOtherRadioButtonId,pacemakeYesButtonId,pacemakeNoButtonId)
        #Navigating back to waveform screen
        step9=navigateToLiveScreenFromAddPatientScreen()
        snooze(1)
        
        if step1 and step2 and step3 and step4 and step5 and step6 and step7 and step8 and step9:
            status='pass'
        else:
            status='fail'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e)) 
        
   
   
def SetPIDasPrimaryUsedID(PrimaryusedID):
    try:
        status='fail'
        step1=Onlinesccreentomenuscreen()
        snooze(1)
        #Navigating to settings screen
        step2=navigateToSettingsScreenFromMenuScreen()
        snooze(1)
        step3=navigateToPatientCardInSettingsScreen()
        snooze(2)
        #collecting combo box title
        step4=selectComboBoxItem(waitForObject(primaryIdSelectorId),PrimaryusedID) 
        snooze(1)
        step5=Backtomenuscreenfromsettingsscreen()
        snooze(1)
        step6=navigateToLiveScreenFromMenuScreen()
        snooze(3)
   
        if step1 and step2 and step3 and step4 and step5 and step6:
            status='pass'
        else:
            status='fail'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e)) 
   
   
        
#To create a patient with name
        
def tst_createPatientPatientListDeletePatientPatientCard1():
    try:
        step1 = createPatientPatientListScreen()
        snooze(1)
        step2 = deletePatientPatientcardScreen1()
        snooze(1)
        if step1 and step2 :
            status = "Pass"        
        else:
            status = "Fail"             
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e)) 
    
    
def deletePatientPatientcardScreen1():
    try:
        patientList = ["pid@1012"]
        n = len(patientList)
        userInput = "Confirm"
        step1 = searchAndSelectPatientToDeleteInPatientCardScreen(patientList)
        snooze(2)
        if step1:
            status='pass'
        else:
            status='fail'
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e)) 


'--------------------------------------------------------------------------'
#Screen 8- Menu work list screen
'Last sync text need to do r strip'
#Total number of strings in work list screen=8
def Menu_Worklist_screen():
    try:
        snooze(2)
        #Navigate to Menu screen
        step1 = navigateToMenuScreenFromLiveScreen()
        snooze(1)
        step2 = navigateToWorkListScreenFromMenuScreen()
        snooze(1)
        step3=CollectingTextfromworklist()
        snooze(1)
        step4=navigateToMenuScreenFromWorkListScreen()
        snooze(1)
        step5=navigateToLiveScreenFromMenuScreen()
        snooze(1)
        if step1 and step2 and step3 and step4 and step5:
            status='pass'
        else:
            status='fail'
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e))


'--------------------------------------------------------------------------'

#Screen 9- Menu- User management screen
'Login text,Last name,New password and confirm password need to do r strip'
#Total number of strings in user creation screen=45

def Menu_User_screen():
    try:
        status='fail'
        snooze(2)
        #Navigate to Menu screen
        step1 = navigateToMenuScreenFromLiveScreen()
        snooze(1)
        step2 = navigateToUserScreenFromMenuScreen()
        snooze(1)
        #Collecting auto login text+ 2 other warning msg (when turned auto on/off)
        step3=Collecttextfromuserlistscreen()
        snooze(1)
        #Login to the system
        step4=LoginToDeviceAndVerifyTheUserNameinOnlineScreen(Login='admin',ConfirmPassword='qaqaqaqa',FirstName='',LastName='admin',passwordlen=8)
        snooze(1)
        step5= navigateToMenuScreenFromLiveScreen()
        snooze(1)
        step6 = navigateToUserScreenFromMenuScreen()
        snooze(1)
        #Navigate to add user screen 
        step7=navigateToUsercreationScreenFromMenuScreen()
        snooze(1)
        #and one user login '1' and password-'qaqaqaqa'
        step8=Creationofuser()
        snooze(1)
        step9=navigateToUsercreationScreenFromMenuScreen()
        snooze(1)
        step10=Collectextfromcreateuserscreen()
        snooze(1)
        step11=Collectingallpopupmessagefromuserscreen1()
        snooze(1)
        step12=Collectingallpopupmessagefromuserscreen2()
        snooze(1)
        step13=Collectingallpopupmessagefromuserscreen3()
        snooze(1)
        #Collecting all the default profile
        step14=toReturnComboBoxList1(roleInputId)
        snooze(2)
        step15=navigateToEditUserScreenFromMenuScreen()
        snooze(5)
        #This method work only if login ID ='1'
        Login='1'  
        step16=searchAnUserInUsersListAndClickOnIt(Login)
        snooze(1)
        #step9=SearchuserandSlectuser('1')
        step17=Edituser_details(editUserButtonId)
        snooze(1)
        step18=Collecttextfromedituserscreen()
        snooze(1)
        step19=navigateToMenuScreenFromUserlistScreen()
        snooze(1)
        step20=searchAnUserInUsersListAndClickOnIt(Login)
        snooze(1)
        step21=Clickon_delete_userbutton()
        snooze(1)
        step22=Collecttextfromdeleteuserscreen()
        snooze(1)
        step23=Navigatetotolestab()
        snooze(1)
        step24=DefaultrolesInuserScreenandAddintolist()
        #Function to navigate to add new role screen
        step25=Collecttextfromrolestab()
        snooze(1)
        step26=Collecttextfrom_Newroletab()
        snooze(1)
        step27=navigateTouserlistscreenFromnewrolescreen()
        snooze(2)
        step28=navigateToMenuScreenFromUserlistScreen()
        snooze(1)
        step29= navigateToMenuScreenFromUserlistScreen()
        snooze(1)
        step30=navigateToLiveScreenFromMenuScreen()
        snooze(2)
        if step1 and step2 and step3 and step4 and step5 and step6 and step7 and step8 and step9 and step10 and step11 and step12 and step13 and step14 and step15 and step16 and step17 and step18 and step19 and step20 and step21 and step22 and step23 and step24 and step25 and step26 and step27 and step28 and step29 and step30:
            status='pass'
        else:
            status='fail'
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e))


'--------------------------------------------------------------------------'
#Screen 10- Menu General settings screen
interpretationSelectorId={"container": mainWindow, "id": "interpretationSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
filterMainsSelectorId={"container": mainWindow, "id": "filterMainsSelectorId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}

'Login text,Last name,New password and confirm password need to do r strip'
#Total number of strings in General settings screen=100
def Settings_Genralsettings_screen():
    try:
        status='fail'
        snooze(2)
        #Navigate to Menu screen
        step1=Onlinesccreentomenuscreen()
        snooze(1)
        #Navigating to settings screen
        step2=navigateToSettingsScreenFromMenuScreen()
        snooze(1)
        step3=Collectingsuboptionsfromgenralscreen()
        snooze(1)
        step4=Collectingtextsfromgenralscreen_1stchild_text(dateSettingControlId,timeSettingControlId,filterMainsSelectorId,
        pacemakerEnableSelectorId,interpretationSelectorId)
        snooze(1)
        step5=collectingbrightneess_Local_recordingconfig_text()
        snooze(1)
        step6=toReturnComboBoxList1(Langauge_customComboBoxId,filterMainsSelectorId)
        snooze(1)
        step7=toReturnComboBoxList1(LeadMarking_customComboBoxId)
        snooze(1)
        step8=scroll_to_end()
        snooze(2)
        step9=Collectingtextsfromgenralscreen_1stchild_text(interpretationSelectorId,jPointSelectorId_customComboBoxId,
                                                             qtcMethodSelectorId_customComboBoxId,homeScreenSelectorId_customComboBoxId,autoShutdownSelectorId,standByModeSelectorId)
        snooze(1)
        step10=toReturnComboBoxList1(interpretationSelectorId,jPointSelectorId_customComboBoxId,qtcMethodSelectorId_customComboBoxId,homeScreenSelectorId_customComboBoxId
                                     ,autoShutdownSelectorId,standByModeSelectorId)
        snooze(1)

        #Collecting sound of warning,demo and auto login
        step11=Collectingtextsfromgenralscreen_1stchild_text(warningSoundSelectorId,demoModeSelectorId)
        snooze(1)
        step12=Collectingautologin_warning()
        snooze(2)
        #Collecting barcode related text
        #step13=CollectingBarcode_text()
        snooze(2)
        step14=advancedGeneralSettingsColumnId_Text()
        snooze(2)
        step15=Backtomenuscreenfromsettingsscreen()
        snooze(1)
        step16=navigateToLiveScreenFromMenuScreen()
        snooze(1)
        if step1 and step2 and step3 and step4 and step5 and step6 and step7 and step8 and step9 and step10 and step11 and step12 and step14 and step15 and step16:
            status='pass'
        else:
            status='fail'
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e))

'--------------------------------------------------------------------------'
#Screen 11- Setting-Profile settings screen
'Login text,Last name,New password and confirm password need to do r strip'
#Total number of strings in Profile settings screen=54

def Settings_Profile_screen():
    try:
        status='fail'
        snooze(2)
        #Navigate to Menu screen
        step1=Onlinesccreentomenuscreen()
        snooze(1)
        #Navigating to settings screen
        step2=navigateToSettingsScreenFromMenuScreen()
        snooze(1)
        step3=navigateToProfileButtonInSettingsScreen()
        snooze(1)
        navigateToAutoProfileInSettingsScreen()
        snooze(2)
        step5=CollectTextfromAutoprofilesettings()
        snooze(1)
        step6=Collectingtextsfromgenralscreen_1stchild_text(adaptiveWorklflowSelectionId,durationSelectionId,leadFormatSelectionId,rhythmLeadSelectionId, historySelectionId,printSecondPageSelectorId,leadLayoutSelectionId)
        snooze(1)
        step7=toReturnComboBoxList1(adaptiveWorklflowSelectionId,durationSelectionId,
                                    leadFormatSelectionId,leadLayoutSelectionId,rhythmLeadSelectionId,historySelectionId)
        step8=scroll_to_end()
        snooze(2)
        step8a=autoProfilefiltertab()
        snooze(1)
        step9=navigateToManualProfileInSettingsScreen()
        snooze(2)
        step10=CollectTextfromManualprofilesettings()
        snooze(2)
        step11=toReturnComboBoxList1(noOfPrintedLeadSelectionId_manual)
        snooze(1)
        step12=navigateToRhythmProfileInSettingsScreen()
        snooze(2)
        step10=CollectTextfromRhythmprofilesettings()
        snooze(1)
        step11=Backtomenuscreenfromsettingsscreen()
        snooze(1)
        step12=navigateToLiveScreenFromMenuScreen()
        snooze(1)
        if step1 and step2 and step3  and step5 and step6 and step7 and step8 and step8a and step9 and step10 and step11 and step12:
            status='pass'
        else:
            status='fail'
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e))


'--------------------------------------------------------------------------'
#Screen 12- Setting-Printer settings screen
'Login text,Last name,New password and confirm password need to do r strip'
#Total number of strings in Print settings screen=11

def Settings_printing_screen():
    try:
        status='fail'
        snooze(2)
        #Navigate to Menu screen

        step1=Onlinesccreentomenuscreen()
        snooze(1)
        #Navigating to settings screen
        step2=navigateToSettingsScreenFromMenuScreen()
        snooze(1)
        step3=navigateToPrintingButtonInSettingsScreen()
        snooze(1)
        step4=Collectingtextfromprintingtab_settingsscreen()
        snooze(2)
        step5=scroll_to_end()
        snooze(2)
        step6=toReturnComboBoxList1(Reportprint_combobox)
        snooze(2)
        step7=printtab_advancedsettings()
        snooze(2)
        step8=toReturnComboBoxList1(customComboBoxId_Printformat,customComboBoxId_linewidth)
        snooze(1)
        step9=Backtomenuscreenfromsettingsscreen()
        snooze(1)
        step10=navigateToLiveScreenFromMenuScreen()
        snooze(1)
        if step1 and step2 and step3 and step4 and step5 and step6 and step7 and step8 and step9 and step10:
            status='pass'
        else:
            status='fail'
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e))


'--------------------------------------------------------------------------'
#Screen 13- Setting-Patient settings screen
'Login text,Last name,New password and confirm password need to do r strip'
#Total number of strings in Patient card settings screen=29

def Settings_Patientcard_screen():
    try:
        status='fail'
        snooze(2)
        #Navigate to Menu screen

        step1=Onlinesccreentomenuscreen()
        snooze(1)
        #Navigating to settings screen
        step2=navigateToSettingsScreenFromMenuScreen()
        snooze(1)
        snooze(1)
        step3=navigateToPatientCardInSettingsScreen()
        snooze(2)
        step4=CollectTextfromPatientcardesettings()
        snooze(1)
        #collecting combo box title
        step5=Collectingtextsfromgenralscreen_1stchild_text(nameOrderSelectorId,primaryIdSelectorId,
                                                            pidMandatorySelectorId,surnameMandatorySelectorId,
                                                            firstNameSelectorId,defaultClassificationSelectorId)
        #Collecting combo box text
        step6=toReturnComboBoxList1(nameOrderSelectorId,primaryIdSelectorId,defaultClassificationSelectorId)
        
        snooze(1)
        step7=Collectingwarningmessage_Surname()
        snooze(1)
        step8=scroll_to_end()
        snooze(2)
        step9=Collectingadvancedtab_Patientcard_text()
        snooze(2)
        step10=collectingwarningmessage_Pateintcard_delete(deleteAllRecordsButtonId,deleteAllPatientsButtonId)
        snooze(2)
        step11=Backtomenuscreenfromsettingsscreen()
        snooze(2)
        step12=navigateToLiveScreenFromMenuScreen()
        snooze(2)
        if step1 and step2 and step3 and step4 and step5 and step6 and step7 and step8 and step9 and step10 and step11 and step12:
            status='pass'
        else:
            status='fail'
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e))

'--------------------------------------------------------------------------'
#Screen 14- Setting-Export tab settings screen
#
'Total number of strings in Export tab settings screen=1'

def settings_Exporttab_Screen():
    try:
        status='fail'
        snooze(2)
        #Navigate to Menu screen

        step1=Onlinesccreentomenuscreen()
        snooze(1)
        #Navigating to settings screen
        step2=navigateToSettingsScreenFromMenuScreen()
        snooze(1)
        step3=navigateToExportInSettingsScreen()
        snooze(1)
        #collecting Auto export to BTL cardioPoint/CMS text
        step4=Collectingtextsfromgenralscreen_1stchild_text(autoExportEnableSelectorId)                                             
        snooze(1)
        step5=Backtomenuscreenfromsettingsscreen()
        snooze(2)
        step6=navigateToLiveScreenFromMenuScreen()
        snooze(2)
        if step1 and step2 and step3 and step4 and step5 and step6:
            status='pass'
        else:
            status='fail'
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e))

'--------------------------------------------------------------------------'
#Screen 15- Setting-Network settings screen
'Total number of strings in Network tab settings screen=11'

def Settings_Networktab_screen():
    try:
        status='fail'
        snooze(2)
        #Navigate to Menu screen
        step1=Onlinesccreentomenuscreen()
        snooze(1)
        #Navigating to settings screen
        step2=navigateToSettingsScreenFromMenuScreen()
        snooze(1)
        step3=navigateToNetworkInSettingsScreen()
        snooze(2)
        step4=CollectTextfromNetworktabsettings()
        snooze(1)
        step5=Collectingtextsfromgenralscreen_1stchild_text(hostNameOrIPAdressControlId,portControlId,wifiSwitchId)                                             
        snooze(1)
        step6=CollectingEthernet_wifi_text()
        snooze(1)
        step7=collectingRefreshResetForgetnw()
        snooze(1)
        step8=Backtomenuscreenfromsettingsscreen()
        snooze(2)
        step9=navigateToLiveScreenFromMenuScreen()
        snooze(2)
        if step1 and step2 and step3 and step4 and step5 and step6 and step7 and step8 and step9:
            status='pass'
        else:
            status='fail'
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e))
'--------------------------------------------------------------------------'
#Screen 16- Setting-Service settings screen
'#Total number of strings in service tab settings screen=13'
def Settings_ServiceTab_screen():
    try:
        status='fail'
        snooze(2)
        #Navigate to Menu screen
        step1=Onlinesccreentomenuscreen()
        snooze(1)
        #Navigating to settings screen
        step2=navigateToSettingsScreenFromMenuScreen()
        snooze(1)
        step3=navigateToServiceInSettingsScreen()
        snooze(1)
        #collecting text from Service screen settings
        step4=CollectingTextfromServicescreenSettings()
        #Collecting 3rd text of child
        step5=Collectingtextsfrom_3rdchild_text(upgradeAModuleFwButtonId,factoryResetButtonId,
                                                     logExportButtonId,printerCheckButtonId)                                             
        snooze(1)
        step6=collectingwarningmessage_ServicescreenSettings(factoryResetButtonId)
        snooze(1)
        step7=collectingwarningmessage_Servicescreen_Exportlogs(logExportButtonId)
        snooze(1)
        step8=collectingwarningmessage_Amodule_FWupmessage(upgradeAModuleFwButtonId)
        snooze(2)
        #Collecting service access text
        step9=servicescreen_serviceacess()
        snooze(1)
        step10=Servicescreen_enertingthekeyandcollectingalerttext()
        snooze(5)        
        step11=Backtomenuscreenfromsettingsscreen()
        snooze(2)
        step12=navigateToLiveScreenFromMenuScreen()
        snooze(2)
        if step1 and step2 and step3 and step4 and step5 and step6 and step7 and step8 and step9 and step10 and step11 and step12:
            status='pass'
        else:
            status='fail'
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e))


'--------------------------------------------------------------------------'
#Screen 17- Setting-About settings screen
'Total number of strings in About tab settings screen=19'

def Settings_AboutTab_screen():
    try:
        status='fail'
        snooze(2)
        #Navigate to Menu screen
        step1=Onlinesccreentomenuscreen()
        snooze(1)
        #Navigating to settings screen
        step2=navigateToSettingsScreenFromMenuScreen()
        snooze(1)
        step3=navigateToAboutProfileInSettingsScreen()
        snooze(1)
        #collecting text from About profile screen settings
        step4=CollectingTextfromAboutcreenSettings()
        snooze(1)
        step5=additionalInfoColumnId_text_aboutscreen()                                             
        snooze(1)
        step6=additionalInfoColumnId_text_aboutscreen1()
        snooze(2)
        step7=Backtomenuscreenfromsettingsscreen()
        snooze(2)
        step8=navigateToLiveScreenFromMenuScreen()
        snooze(2)
        if step1 and step2 and step3 and step4 and step5 and step6 and step7 and step8:
            status='pass'
        else:
            status='fail'
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e))

'--------------------------------------------------------------------------'
#Screen 18- waveform screen

'Total number of strings in waveform screen=8'
def Wavefromscreen():
    try:
        step1=CollectWavefromscreentext()
        snooze(1)
        if step1:
            status='pass'
        else:
            status='fail'
        return True if status=='pass' else False
    
    except Exception as e:
        test.log('exception'+str(e)) 


'----------------------------------------------------------------------------'
loginTypePopupId={"container": mainWindow, "id": "loginTypePopupId", "type": "Rectangle", "unnamed": 1, "visible": True}
Newpasswordadmin={"container": mainWindow, "id": "passwordInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
Confirmpasswordadmin={"container": mainWindow, "id": "confirmPasswordInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
hideKeyBackgroundpassword={"container": mainWindow, "id": "hideKeyBackground", "type": "Rectangle", "unnamed": 1, "visible": True}
Savepassword={"checkable": False, "container": mainWindow, "id": "saveUserButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
genericSecurityPopupId={"container": mainWindow, "id": "genericSecurityPopupId", "type": "SecurityPopup", "unnamed": 1, "visible": True}
autoLoginButtonId={"checkable": False, "container": mainWindow, "id": "autoLoginButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
enableSecurityButtonId={"checkable": False, "container": mainWindow, "id": "enableSecurityButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
okButtonIdFactory={"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}


#Prerequistes to create a default user and user '1'

#Creating the default user creation

#Do factory reset after each language verification and create a default admin user

def factoryRestCreateDefaultUser():
    try:
        status='fail'
        snooze(2)
        #Navigate to Menu screen
        step1=Onlinesccreentomenuscreen()
        snooze(1)
        #Navigating to settings screen
        step2=navigateToSettingsScreenFromMenuScreen()
        snooze(1)
        step3=navigateToServiceInSettingsScreen()
        snooze(1)
        step4=dofactoryreset(factoryResetButtonId)
        snooze(3)
        #Enable once factory reset issue pop auto accept issue solved
        step5=collectfactoryresetmsg()
        snooze(3)
        #Creating default admin user
        step6=Createdefaultusercredinusermanagement()
        snooze(1)
            
        if step1 and step2 and step3 and step4 and step5 and step6: 
            status='pass'
        else:
            status='fail'
        return True if status=='Pass' else False
    except Exception as e:
        test.log('exception'+str(e))
        

#Method to create default admin
def Createdefaultusercred():
    try:
        status='fail'
        #You must create new password for default admin user to continue.
        if object.exists(loginTypePopupId):
            parent=findObject(loginTypePopupId)
            child=object.children(parent)
            changePass=object.children(child[1])
            col0=object.children(changePass[0])
            str1=col0[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        if object.exists(Newpasswordadmin):
            setFocusTextBox(Newpasswordadmin)
            type(mainWindow,'qaqaqaqa')
            snooze(1)
        if object.exists(Confirmpasswordadmin):
            setFocusTextBox(Confirmpasswordadmin)
            type(mainWindow,'qaqaqaqa')
            snooze(1)
        if object.exists(hideKeyBackgroundpassword):
            mouseClick(hideKeyBackgroundpassword)
            snooze(1)
        if waitForObject(Savepassword):
            object.exists(Savepassword)
            mouseClick(Savepassword)
            status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))
        
def Createdefaultusercredinusermanagement():
    try:
        step1=Createdefaultusercred()   
        snooze(1)
        step2=autoLoginpopup(autoLoginButtonId)
        snooze(1)
        step3= navigateToMenuScreenFromUserlistScreen()
        snooze(1)
        step4=navigateToLiveScreenFromMenuScreen()
        snooze(5)
        status='pass'
        
        if step1 and step2 and step3 and step4:
            status='Pass'
        else:
            
            status='fail'
        
        return True if status=='Pass' else status=='fail'
    
    except Exception as e:
        test.fail('exception'+str(e))      
        
        
        
        
#Accept the pop up and navigate back to online screen
def acceptloginpopandnavigatetoonlinescreen():
    try:
        status='fail'
        #Auto login (No security) text
        if object.exists(genericSecurityPopupId):
            parent=findObject(genericSecurityPopupId)
            child=object.children(parent)
            col0=object.children(child[0])
            Row0=object.children(col0[0])
            str1=Row0[0].text
            test.log('Collected string ='+str(str1))
            addtolist1(str1)
            snooze(1)
            #Enable security and login text
            Row1=object.children(col0[1])
            str1=Row1[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Do not show this message again text
            Row3=object.children(col0[3])
            str1=Row3[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))
 
        
#Accepting auto login(No security)
def autoLoginpopup(obj):
    try:
        status='fail'
        if object.exists(obj):
            mouseClick(obj)
            status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))
        