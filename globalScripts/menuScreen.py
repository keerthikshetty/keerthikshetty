import object


'''Objects of main window'''
mainWindow = {"type": "QQuickWindowQmlImpl", "visible": True}
onlineScreen_MainWindow ={"container": mainWindow, "id": "onlineScreenId", "type": "OnlineWfScreen", "visible": True}
evaluationScreen_MainWindow = {"container": mainWindow, "id": "evaluationScreenId", "type": "EvalScreen", "visible": True}
menuScreen_MainWindow = {"container": mainWindow, "id": "menuScreenId", "type": "Rectangle", "visible": True}
patientCardScreen_MainWindow = {"container": mainWindow, "id": "patientScreenId", "type": "PatientCardLoader",  "visible": True}
liveSettingsScreen_MainWindow = {"container": onlineScreen_MainWindow,  "type": "Rectangle", "visible": True}

'''Objects of menu button'''
menuRecordingButton = {"checkable": False, "container": mainWindow, "id": "menuRecordingButtonId", "type": "CircularButton",  "visible": True}
menuPatientcardButton = {"checkable": False, "container": menuScreen_MainWindow, "id": "menuPatientcardButtonId", "type": "CircularButton",  "visible": True}
menuWorklistButton = {"checkable": False, "container": menuScreen_MainWindow, "id": "menuWorklistButtonId", "type": "CircularButton",  "visible": True}
menuUserButton = {"checkable": False, "container": menuScreen_MainWindow, "id": "menuUsersButtonId", "type": "CircularButton",  "visible": True}
menuSettingsButton ={"checkable": False, "container": menuScreen_MainWindow, "id": "menuSettingsButtonId", "type": "CircularButton",  "visible": True}
menuRhythmComboBox = {"container": menuScreen_MainWindow, "id": "rhythmComboBoxId", "type": "ComboBox",  "visible": True}
menuDefaultComboBox = {"container": menuScreen_MainWindow, "id": "comboBoxId", "type": "ComboBox",  "visible": True}
backButtonWorkList = {"checkable": False, "container": mainWindow, "id": "backPButtonWorklistId", "type": "Button", "visible": True}
backButtonUserScreen = {"checkable": False, "container": mainWindow, "id": "backButtonUserScreenId", "type": "Button", "visible": True}
addUserButtonId={"checkable": False, "container": mainWindow, "id": "addUserButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
backButtonUserScreenId={"checkable": False, "container": mainWindow, "id": "backButtonUserScreenId", "type": "Button", "unnamed": 1, "visible": True}

'Localization testing objects'
'1) Menu screen'
MenuScreenId={"container": mainWindow, "id": "menuScreenId", "type": "MenuScreen", "unnamed": 1, "visible": True}
MenutitleID={"container": mainWindow, "id": "titleSpaceId", "type": "Row", "unnamed": 1, "visible": True}
menuFormfeedButtonId={"checkable": False, "container": mainWindow, "id": "menuFormfeedButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}

'2)Work-list screen'
referenceLocationSelectorId={"container": mainWindow, "id": "referenceLocationSelectorId", "type": "ReferenceLocationList", "unnamed": 1, "visible": True}
deptNameId={"container": mainWindow, "id": "deptNameId", "type": "Rectangle", "unnamed": 1, "visible": True}
dateOfBirthSortButtonId={"checkable": False, "container": mainWindow, "id": "dateOfBirthSortButtonId", "type": "WorklistSortButton", "unnamed": 1, "visible": True}
durationSortButtonId={"checkable": False, "container": mainWindow, "id": "durationSortButtonId", "type": "WorklistSortButton", "unnamed": 1, "visible": True}
nameSortButtonId={"checkable": False, "container": mainWindow, "id": "nameSortButtonId", "type": "WorklistSortButton", "unnamed": 1, "visible": True}
orderDateTimeSortButtonId={"checkable": False, "container": mainWindow, "id": "orderDateTimeSortButtonId", "type": "WorklistSortButton", "unnamed": 1, "visible": True}
orderLocationSortButtonId={"checkable": False, "container": mainWindow, "id": "orderLocationSortButtonId", "type": "WorklistSortButton", "unnamed": 1, "visible": True}
syncWorkListItems={"container": mainWindow, "id": "syncWorkListItems", "type": "ColumnLayout", "unnamed": 1, "visible": True}

'3)User management screen'
titleSpace_ID={"container": mainWindow, "id": "titleSpace", "type": "Rectangle", "unnamed": 1, "visible": True}
#userLoginNameInputId={"container": mainWindow, "id": "userLoginNameInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
userFirstNameInputId={"container": mainWindow, "id": "userFirstNameInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
userLastNameInputId={"container": mainWindow, "id": "userLastNameInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
defaultProfileInputId={"container": mainWindow, "id": "defaultProfileInputId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
roleInputId={"container": mainWindow, "id": "roleInputId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
userLoginNameInputId={"container": mainWindow, "id": "userLoginNameInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
passwordInputId={"container": mainWindow, "id": "passwordInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
confirmPasswordInputId={"container": mainWindow, "id": "confirmPasswordInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
changePasswordAfterFirstLoginSwitchId={"container": mainWindow, "id": "changePasswordAfterFirstLoginSwitchId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
passWordRequirementsFor7Inch={"container": mainWindow, "id": "passWordRequirementsFor7Inch", "type": "PasswordValidityInfo", "unnamed": 1, "visible": False}
saveUserButtonId={"checkable": False, "container": mainWindow, "id": "saveUserButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
errorPopupItemId={"container": mainWindow, "id": "errorPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
okButtonId={"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
userButtonId={"container": mainWindow, "type": "Rectangle", "unnamed": 1, "visible": True}
cancelUserButtonId={"checkable": False, "container": mainWindow, "id": "cancelUserButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
discardWarningItemId={"container": mainWindow, "id": "discardWarningItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
cancelButtonId={"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
userSearchInputId={"backgroundcolor": "#ffffff", "container": mainWindow, "echoMode": 0, "id": "userSearchInputId", "type": "SearchBar", "unnamed": 1, "visible": True}
userListviewId={"container": mainWindow, "occurrence": 2, "type": "ListView", "unnamed": 1, "visible": True}
deleteID={"checkable": False, "container": mainWindow, "id": "deleteUserButtonId", "type": "DeleteButton", "unnamed": 1, "visible": False}
#userListViewId={"container": mainWindow, "occurrence": 2, "type": "ListView", "unnamed": 1, "visible": True}
#Searching created user and checking objects
deleteUserButtonId={"checkable": False, "container": mainWindow, "id": "deleteUserButtonId", "type": "DeleteButton", "unnamed": 1, "visible": True}
editUserButtonId={"checkable": False, "container": mainWindow, "id": "editUserButtonId", "type": "EditUserButton", "unnamed": 1, "visible": True}
userButtonId={"container": mainWindow, "type": "Rectangle", "unnamed": 1, "visible": True}
listId={"container": mainWindow, "id": "listId", "type": "UserList", "unnamed": 1, "visible": True}
TitleID_Edituser={"container": mainWindow, "id": "titleSpace", "type": "Rectangle", "unnamed": 1, "visible": True}
backButtonUserScreenId={"checkable": False, "container": mainWindow, "id": "backButtonUserScreenId", "type": "Button", "unnamed": 1, "visible": True}
changePasswordButtonId={"checkable": False, "container": mainWindow, "id": "changePasswordButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
oldPasswordInputId={"container": mainWindow, "id": "oldPasswordInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
oldPasswordInputId_textInputId={"container": mainWindow, "echoMode": 2, "id": "textInputId", "passwordCharacter": "*", "type": "TextField", "unnamed": 1, "visible": True}
NewPasswordInputID_textInputID={"container": mainWindow, "echoMode": 2, "id": "textInputId", "occurrence": 2, "passwordCharacter": "*", "type": "TextField", "unnamed": 1, "visible": True}
deleteconfirm_ID={"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
deleteWarningId={"container": mainWindow, "id": "deleteWarningId", "type": "UserDeleteWarningPopup", "unnamed": 1, "visible": True}
delete_confirmButtonId={"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
delete_confirmPasswordTextInputId={"container": mainWindow, "id": "confirmPasswordTextInputId", "type": "CustomTextFieldWithLabelAsRow", "unnamed": 1, "visible": True}
a={"backgroundcolor": "#ffffff", "container": mainWindow, "echoMode": 2, "id": "textInputId", "passwordCharacter": "*", "type": "TextField", "unnamed": 1, "visible": True}
userLoginLabelId={"container": mainWindow, "text": 1, "type": "Label", "unnamed": 1, "visible": True}
userButtonId_1={"container": mainWindow, "id": "userButtonId", "type": "Rectangle", "unnamed": 1, "visible": True}

#Function to navigate  to live screen from menu screen

def navigateToLiveScreenFromMenuScreen():
    try:
        status = False
        snooze(1)
        if waitForObject(menuRecordingButton):
            if object.exists(menuRecordingButton):
                mouseClick(menuRecordingButton)
                snooze(2)
        if object.exists(liveScreenPatientListButton):
            test.log("Successfully live screen is displayed")
            status = True
        else:
            test.log("Live screen is not displayed")
            status = False       
                
        return status 
        
    except Exception as e:
        test.fail("Exception" +str(e))
        
        
#Function to navigate  to patient card screen from menu screen
def navigateToPatientCardScreenFromMenuScreen():
    try:
        status = False
        if waitForObject(menuPatientcardButton):
            if object.exists(menuPatientcardButton):
                mouseClick(menuPatientcardButton)
        else:
            test.log("Menu patient card button is not active")
        if waitForObject(patientCardAddButton):
            #test.log("Successfully patient card screen is displayed")
            status = True
        else:
            test.fail("Patient card screen is not displayed")
            status = False   
        
        return status
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to navigate  to work list screen from menu screen
def navigateToWorkListScreenFromMenuScreen():
    try:
        status = False
        if waitForObject(menuWorklistButton):
            if object.exists(menuWorklistButton):
                mouseClick(menuWorklistButton)
                status = True
        else:
            test.log("Work list screen is not visible")
        
        return status
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to navigate  to user screen from menu screen
def navigateToUserScreenFromMenuScreen():
    try:
        status = False
        if waitForObject(menuUserButton):
            if object.exists(menuUserButton):
                mouseClick(menuUserButton)
            status = True
        else:
            test.log("User screen is not visible")
        
        return status
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to navigate  to user screen from menu screen
def navigateToMenuScreenFromUserScreen():
    try:
        status = False
        if waitForObject(backButtonUserScreen):
            if object.exists(backButtonUserScreen):
                mouseClick(backButtonUserScreen)
        if waitForObject(backButtonUserScreen):
            if object.exists(backButtonUserScreen):
                mouseClick(backButtonUserScreen)             
                status = True
        else:
            test.log("Menu screen is not visible")
        
        return status
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to navigate  to menu screen from work list screen
def navigateToMenuScreenFromWorkListScreen():
    try:
        status = False
        if waitForObject(backButtonWorkList):
            if object.exists(backButtonWorkList):
                mouseClick(backButtonWorkList)
                status = True
        else:
            test.log("Menu screen is not visible")
        
        return status
    
    except Exception as e:
        test.fail("Exception" +str(e))
                
#Function to navigate  to patient card screen from menu screen
def navigateToSettingsScreenFromMenuScreen():
    try:
        #from settingsScreen import profileSettingsButtonInsettingsScreen
        result=False
        if waitForObject(menuSettingsButton):
            if object.exists(menuSettingsButton):
                mouseClick(waitForObject(menuSettingsButton))
                snooze(2)
        if object.exists(profileSettingsButtonInsettingsScreen):
            result=True
            test.log("Successfully settings screen is displayed")
        else:
            result=False
            test.log("Settings screen is not displayed")    
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Function to navigate to create user screen
def navigateToUsercreationScreenFromMenuScreen():
    try:
        result=False
        if waitForObject(addUserButtonId):
            if object.exists(addUserButtonId):
                mouseClick(waitForObject(addUserButtonId))
                snooze(2)
                result=True
        else:
            result=False
            test.log("Settings screen is not displayed")    
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
    
#Function to navigate to edit user screen from user screen
def navigateToEditUserScreenFromMenuScreen():
    try:
        result=False
        if waitForObject(backButtonUserScreenId):
            if object.exists(backButtonUserScreenId):
                mouseClick(waitForObject(backButtonUserScreenId))
                snooze(2)
                result=True
        else:
            result=False
            test.log("Settings screen is not displayed")    
        return result
    
    except Exception as e:
        test.fail("Exception" +str(e))
 
backButtonUserScreenId={"checkable": False, "container": mainWindow, "id": "backButtonUserScreenId", "type": "Button", "unnamed": 1, "visible": True}
hideKeyBackground_keyboard={"container":mainWindow, "id": "hideKeyBackground", "type": "Rectangle", "unnamed": 1, "visible": True}
backButtonUserScreenId={"checkable": False, "container": mainWindow, "id": "backButtonUserScreenId", "type": "Button", "unnamed": 1, "visible": True}

#Function to Navigate to Menu screen from user list screen
def navigateToMenuScreenFromUserlistScreen():
    try:
        status = 'fail'
        if waitForObject(backButtonUserScreenId):
            if object.exists(backButtonUserScreenId):
                mouseClick(waitForObject(backButtonUserScreenId))
                snooze(2)
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e))

def navigateTouserlistscreenFromnewrolescreen():
    try:
        status = 'fail'
        if waitForObject(backButtonUserScreenId):
            if object.exists(backButtonUserScreenId):
                mouseClick(waitForObject(backButtonUserScreenId))
                snooze(2)
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e))

        
#Object and text from menu screen
'Localization testing -Menu screen'
autologinModeSelectorId={"container": mainWindow, "id": "autologinModeSelectorId", "type": "CustomSwitchWithLabelColumn", "unnamed": 1, "visible": True}
Autologin_onID={"checkable": True, "container": mainWindow, "id": "onSwitchId", "type": "CustomRadioButton", "unnamed": 1, "visible": True}
confirmPopupItemId_autologinon={"container": mainWindow, "id": "confirmPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
confirmButtonId={"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
Autologin_offID={"checkable": True, "container": mainWindow, "id": "offSwitchId", "type": "CustomRadioButton", "unnamed": 1, "visible": True}
confirmPopupItemId_autologinoff={"container": mainWindow, "id": "confirmPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
cancelButtonId_autologinoff={"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
confirmButtonId_autologinoff={"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}


#Collecting auto login,
def Collecttextfromuserlistscreen():
    try:
        status='fail'
        #Collecting 'Auto login text'
        if object.exists(autologinModeSelectorId):
            parent=findObject(autologinModeSelectorId)
            child=object.children(parent)
            str1=child[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(0.5)
        #Clicking on auto login on and selecting warning and accept the warning   
        if object.exists(Autologin_onID):
            mouseClick(Autologin_onID)
            snooze(1)
            collectingwarning_text(confirmPopupItemId_autologinon)
            Acceptwarning_popup(confirmButtonId)
            snooze(1)
        #Clicking on auto login off and selecting warning and accept the warning 
        if object.exists(Autologin_offID):
            mouseClick(Autologin_offID)
            snooze(1)
            collectingwarning_text(confirmPopupItemId_autologinoff)
            Acceptwarning_popup(confirmButtonId_autologinoff)
            snooze(1)
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.fail("Exception" +str(e))
    
    



#collecting text-Menu,patient card,work list,users and settings

def collectmenuscreenscreentext():
    try:
        status='fail'     
        #collecting Menu text   
        if object.exists(MenutitleID):
            parent=findObject(MenutitleID)
            child=object.children(parent)
            #Label1=object.children(child[1])
            str1=child[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(0.5)
        #collecting recording, patient card, worklist, users, settings text
        if object.exists(MenuScreenId):
            parent=findObject(MenuScreenId)
            child=object.children(parent)
            Row_3=object.children(child[3])
            for x in range(len(Row_3)):
                column_0=object.children(Row_3[x])
                str1=column_0[1].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(0.5)
        #ff text
        if object.exists(menuFormfeedButtonId):
            parent=findObject(menuFormfeedButtonId)
            child=object.children(parent)
            Row_5=object.children(child[5])
            str1=Row_5[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(0.5)
            status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))

        
#Object and text from work list screen
'Localization testing -Work list screen'
nameSortButtonId1={"checkable": False, "container": mainWindow, "id": "nameSortButtonId", "type": "WorklistSortButton", "unnamed": 1, "visible": True}

#Collecting text from the work list screen
def CollectingTextfromworklist():
    try:
        status='fail'
        #Collecting 'referred to' text
        if object.exists(referenceLocationSelectorId):
            parent=findObject(referenceLocationSelectorId)
            child=object.children(parent)
            str1=child[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        if collectingsoringID_text(orderDateTimeSortButtonId,nameSortButtonId,orderLocationSortButtonId,dateOfBirthSortButtonId,durationSortButtonId):
            test.log("collected all sorting text")
        if syncWorkListItems_text():
            status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))
        
#collecting sorting ID text  
def collectingsoringID_text(*arguments): 
    try:
        status='fail'
        for obj in arguments:
            if object.exists(obj):
                parent=findObject(obj)
                child=object.children(parent)
                str1=child[3].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(1)
                status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))

syncWorkListItems1= {"container": mainWindow, "id": "syncWorkListItems", "type": "Column", "unnamed": 1, "visible": True}      
 
            
#Collecting Network error and last sync text
def syncWorkListItems_text():
    try:
        #Network error text
        status='fail'
        if object.exists(syncWorkListItems1):
            parent=findObject(syncWorkListItems1)
            child=object.children(parent)
            str1=child[3].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Last sync text
            str1=child[4].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
        return True if status=='pass' else status=='fail'
    except Exception as e:
        test.fail('exception'+str(e))
        

'Localization testing -User creation/Management'

def Collectextfromcreateuserscreen():
    try:
        status='fail'
        #collecting New user text
        if object.exists(titleSpace_ID):
            parent=findObject(titleSpace_ID)
            child=object.children(parent)
            Row_0=object.children(child[0])
            str1=Row_0[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #collecting all the text    
        if Left_Side_usercreationtext(userLoginNameInputId,userFirstNameInputId,userLastNameInputId,defaultProfileInputId,roleInputId):
            status='pass'
        if Right_Side_usercreationtext(passwordInputId,confirmPasswordInputId,changePasswordAfterFirstLoginSwitchId):
            status='pass'
        if passwordrequirments_text():
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e))

def Left_Side_usercreationtext(*arguments):
    try:
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

def Right_Side_usercreationtext(*arguments):
    try:
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

def passwordrequirments_text():
    try:
        status='fail'
        if object.exists(passWordRequirementsFor7Inch):
            parent=findObject(passWordRequirementsFor7Inch)
            child=object.children(parent)
            col_0=object.children(child[0])
            item2=object.children(col_0[2])
            Row_0=object.children(item2[0])
            str1=Row_0[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            item4=object.children(col_0[4])
            Row_0=object.children(item4[0])
            str1=Row_0[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e))
        
#Collecting all the warning text from the user screen
#Please enter all the required field text

def Collectingallpopupmessagefromuserscreen1(Password='q'):
    try:
        #To get 'Please enter all the required fields! text'
        if object.exists(passwordInputId):           
            setFocusTextBox(passwordInputId)
            type(mainWindow, Password)
            snooze(1)
            if object.exists(hideKeyBackground_keyboard):
                mouseClick(waitForObject(hideKeyBackground_keyboard))
                snooze(2)
                if object.exists(saveUserButtonId):
                    mouseClick(waitForObject(saveUserButtonId))
                    snooze(2)
                #Collecting 'Please enter all required fields!' strings
                if object.exists(errorPopupItemId):
                    collectingwarning_text(errorPopupItemId)
                    Acceptwarning_popup(okButtonId)
                    status='pass' 
                return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e))
 
#Collecting password mismatch warning text 
def Collectingallpopupmessagefromuserscreen3(login='Q',Lastname='Q',Password='qwerty123'):
    try:
        #To get 'Please enter all the required fields! text'
        if object.exists(userLoginNameInputId):           
            setFocusTextBox(userLoginNameInputId)
            type(mainWindow, login)
            snooze(1)
        if object.exists(userLastNameInputId):           
            setFocusTextBox(userLastNameInputId)
            type(mainWindow, Lastname)
            snooze(1)
        if object.exists(roleInputId):
            mouseClick(roleInputId)
            snooze(1)
        if object.exists(Role_servicecreen):
            mouseClick(Role_servicecreen)
            snooze(1)
        if object.exists(passwordInputId):           
            setFocusTextBox(passwordInputId)
            type(mainWindow, Password)
            snooze(1)
            if object.exists(hideKeyBackground_keyboard):
                mouseClick(waitForObject(hideKeyBackground_keyboard))
                snooze(2)
            if object.exists(saveUserButtonId):
                mouseClick(waitForObject(saveUserButtonId))
                snooze(2)
                #Collecting 'Confirmation password is not matching' strings
                if object.exists(errorPopupItemId):
                    collectingwarning_text(errorPopupItemId)
                    Acceptwarning_popup(okButtonId)
                    status='pass' 
                return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e)) 

roleInputId={"container": mainWindow, "id": "roleInputId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True}
Role_servicecreen={"checkable": False, "container": mainWindow, "id": "comboBoxDelegateId", "type": "ItemDelegate", "unnamed": 1, "visible": True}




#collecting Login already exists text
 
def Collectingallpopupmessagefromuserscreen2(login='1',Lastname='Q',Password='qaqaqaqa'):
    try:
        #To get 'Please enter all the required fields! text'
        if object.exists(userLoginNameInputId):           
            setFocusTextBox(userLoginNameInputId)
            type(mainWindow, login)
            snooze(1)
        if object.exists(userLastNameInputId):           
            setFocusTextBox(userLastNameInputId)
            type(mainWindow, Lastname)
            snooze(1)  
        if object.exists(passwordInputId):           
            setFocusTextBox(passwordInputId)
            type(mainWindow, Password)
            snooze(1)
        if object.exists(roleInputId):
            mouseClick(roleInputId)
            snooze(1)
        if object.exists(Role_servicecreen):
            mouseClick(Role_servicecreen)
            snooze(1)
            if object.exists(saveUserButtonId):
                mouseClick(waitForObject(saveUserButtonId))
                snooze(2)
                #Collecting 'login name already exists!Please enter another name' strings
                if object.exists(errorPopupItemId):
                    collectingwarning_text(errorPopupItemId)
                    Acceptwarning_popup(okButtonId)
                    status='pass' 
        #Collecting 'Are you want to discard changes with save' text    
        if object.exists(cancelUserButtonId):
                mouseClick(waitForObject(cancelUserButtonId))
                snooze(2)
                if object.exists(discardWarningItemId):
                    collectingwarning_text(discardWarningItemId)
                    Acceptwarning_popup(cancelButtonId)
                    status='pass' 
                return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e)) 
    
    
#Common method to collect warning text message                 
def collectingwarning_text(obj):
    try:
        if object.exists(obj):
            parent=findObject(obj)
            child=object.children(parent)
            col_0=object.children(child[0])
            item2=object.children(col_0[2])
            Row_0=object.children(item2[0])
            str1=Row_0[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e))

            
#Function to accept warning pop up 
def Acceptwarning_popup(obj):
    try:
        status='fail'
        if object.exists(obj):
                mouseClick(waitForObject(obj))
                snooze(2)
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e))

Confirmpassword_textID={"container": mainWindow, "echoMode": 2, "id": "textInputId", "occurrence": 2, "passwordCharacter": "*", "type": "TextField", "unnamed": 1, "visible": True}

#Creating one user login '1' and lastname-'Q' and password-'qaqaqaqa'
def Creationofuser(login='1',Lastname='1',Password='qaqaqaqa',ConfirmPassword='qaqaqaqa'):
    try:
        #To get 'Please enter all the required fields! text'
        if object.exists(userLoginNameInputId):           
            setFocusTextBox(userLoginNameInputId)
            type(mainWindow,login)
            snooze(1)
        if object.exists(userLastNameInputId):           
            setFocusTextBox(userLastNameInputId)
            type(mainWindow, Lastname)
            snooze(1)  
        if object.exists(passwordInputId):           
            setFocusTextBox(passwordInputId)
            type(mainWindow, Password)
            snooze(1)
        if object.exists(Confirmpassword_textID):           
            setFocusTextBox(Confirmpassword_textID)
            type(mainWindow, ConfirmPassword)
            snooze(1) 
        if object.exists(roleInputId):
            mouseClick(roleInputId)
            snooze(1)
        if object.exists(Role_servicecreen):
            mouseClick(Role_servicecreen)
            snooze(1)
        if object.exists(saveUserButtonId):
            mouseClick(waitForObject(saveUserButtonId))
            snooze(2)
            status='pass' 
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e)) 




#Need to update Properly (Its'  not working)
def SearchuserandSlectuser(obj):
    try:
        status = False
        if object.exists(userSearchInputId):
            searchBox = (waitForObject(userSearchInputId))
            searchBox.text = ""
            type(waitForObject(userSearchInputId),obj)
            #userListviewIdView = waitForObject(listId)
            Parent=findObject(listId)
            child=object.children(Parent)
            #item = object.children(userListviewIdView) #2
            UserID=object.children(child[1])   #2
            Item_0=object.children(UserID[0]) #2
            item_00 = object.children(Item_0[0])  #4
            userbuttonID=object.children(item_00[1]) #2
            item1=object.children(userbuttonID[0]) #1
            row0 = object.children(item1[0]) #7
            value = row0[5].text 
                       
            for j in item_0:
                outline = object.children(j)
                if len(outline) > 0:
                    item1=object.children(outline[0])
                    Row0=object.children(item1[0])
                    value = Row0[0].text                
                    if (value == str(obj)):
                        snooze(1)
                        longMouseClick(j)
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e))
              
#Method to select login='1' and 1
def selectlogin_1():
    try:
        snooze(2)
        status='pass'
        if object.exists(userButtonId_1):
            mouseClick(waitForObject(userButtonId_1))
            snooze(2)
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e))

#Function click on edit button in user management.
def Edituser_details(obj):
    try:
        status='fail'
        if object.exists(obj):
            mouseClick(obj)
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e))

#Function to collect text from edit text screen
def Collecttextfromedituserscreen(CurrentPassword='qwertyuio',NewPassword='qwertyuio',ConfirmPassword='qwertyuiop'):
    try:
        status='fail'
        #collecting Edit user text
        if object.exists(TitleID_Edituser):
            parent=findObject(TitleID_Edituser)
            child=object.children(parent)
            Row_0=object.children(child[0])
            str1=Row_0[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #collecting Change password text
        if object.exists(changePasswordButtonId):
            parent=findObject(changePasswordButtonId)
            child=object.children(parent)
            str1=child[3].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #click on change password text
        if object.exists(changePasswordButtonId):
            if waitForObject(changePasswordButtonId):
                mouseClick((changePasswordButtonId))
                snooze(1) 
                #Collecting current password text   
                if object.exists(oldPasswordInputId):
                    parent=findObject(oldPasswordInputId)
                    child=object.children(parent)
                    str1=child[0].text
                    addtolist1(str1)
                    test.log('Collected string ='+str(str1))
                    snooze(1)
                    status='pass' 
                '''    
                if object.exists(oldPasswordInputId_textInputId):           
                    setFocusTextBox(oldPasswordInputId_textInputId)
                    type(mainWindow, Password)
                    snooze(1)
                if object.exists(oldPasswordInputId_textInputId):           
                    setFocusTextBox(oldPasswordInputId_textInputId)
                    type(mainWindow, Password)
                    snooze(1)
                
                    if object.exists(hideKeyBackground_keyboard):
                        mouseClick(waitForObject(hideKeyBackground_keyboard))
                        snooze(2)
                    if object.exists(saveUserButtonId):
                        mouseClick(waitForObject(saveUserButtonId))
                        snooze(2)
                        #Collecting 'confirmation
                        if object.exists(errorPopupItemId):
                            collectingwarning_text(errorPopupItemId)
                            Acceptwarning_popup(okButtonId)'''
                        
                return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e))
                    
#searchBox.text = ""

#Collecting warning message-Old and new password is same
def collectingoldandnewpasswordtextissame(oldpassword='qwertyuio',Newpassword='qwertyuio'):
    try:
        status='fail'
        #Entering password to old password 
        if object.exists(oldPasswordInputId_textInputId):
            searchBox = (waitForObject(oldPasswordInputId_textInputId))
            searchBox.text = ""          
            setFocusTextBox(oldPasswordInputId_textInputId)
            type(mainWindow, oldpassword)
            snooze(1)
            #Entering password to new password
            if object.exists(NewPasswordInputID_textInputID):          
                setFocusTextBox(NewPasswordInputID_textInputID)
                setFocusTextBox.text=''
                type(mainWindow,Newpassword)
                snooze(1)
                if object.exists(hideKeyBackground_keyboard):
                    mouseClick(waitForObject(hideKeyBackground_keyboard))
                    snooze(2)
                if object.exists(saveUserButtonId):
                    mouseClick(waitForObject(saveUserButtonId))
                    snooze(2)
                #Collecting 'Old and new password should not be same'                       if object.exists(errorPopupItemId):
                if object.exists(errorPopupItemId):
                    collectingwarning_text(errorPopupItemId)
                    Acceptwarning_popup(okButtonId)
                status='pass' 
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e))

#Function to collect text from delete user screen
def Clickon_delete_userbutton():
    try:
        status='fail'
        if waitForObject(deleteUserButtonId):
            if object.exists(deleteUserButtonId):
                mouseClick(deleteUserButtonId)
                snooze(2)
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e))

ErorpopIDuserscreen={"container": mainWindow, "id": "apcErrorPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
okButtonIdUserscreen={"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}

#collect text from delete user screen
def Collecttextfromdeleteuserscreen(confirmpassword='q'):
    try:
        status='fail'
        if object.exists(deleteWarningId):
            parent=findObject(deleteWarningId)
            child=object.children(parent)  
            col_0=object.children(child[0]) 
            #collecting  'confirmation' text
            Row_0=object.children(col_0[0]) 
            str1=Row_0[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Do you really want delete the selected user?
            str1=col_0[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #collecting Enter your password before deleting the user 
            Col_3=object.children(col_0[3]) 
            Row_0=object.children(Col_3[0]) 
            str1=Row_0[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #Collecting 'password' text and entering password        
        if object.exists(delete_confirmPasswordTextInputId):
            parent=findObject(delete_confirmPasswordTextInputId)
            child=object.children(parent)
            str1=child[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #entering wrong password to collect warning message
        if object.exists(delete_confirmPasswordTextInputId):
            setFocusTextBox(delete_confirmPasswordTextInputId)
            type(mainWindow,'')
            type(mainWindow,confirmpassword)
            snooze(1)
            #Click on save button
            if object.exists(deleteconfirm_ID):
                mouseClick(deleteconfirm_ID)
                snooze(2)
                #collecting Incorrect password entered
                collectingwarning_text(ErorpopIDuserscreen)
                Acceptwarning_popup(okButtonIdUserscreen)
                status='pass' 
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e))
            

rolesTabButtonId={"checkable": True, "container": mainWindow, "id": "rolesTabButtonId", "type": "TabButton", "unnamed": 1, "visible": True}
rolesNewaddButtonId={"checkable": False, "container": mainWindow, "id": "rolesNewViewButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
#rolesListIduserscreen={"container": mainWindow, "id": "rolesListId", "type": "RolesList", "unnamed": 1, "visible": True}

roleListViewIduserscreen={"container": mainWindow, "id": "roleListViewId", "type": "ListView", "unnamed": 1, "visible": True}

#Function to collect roles text and navigate to roles tab



def Navigatetotolestab():
    try:
        status='fail'
        if waitForObject(rolesTabButtonId):
            if object.exists(rolesTabButtonId):
                parent=findObject(rolesTabButtonId)
                child=object.children(parent)
                str1=child[1].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(1)
                mouseClick(rolesTabButtonId)
                snooze(2)
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e)) 
        

'''
#FUnction to collect all the default roles in user screen-Roles tab
def collectingalldefaulttoles():
    try:
        status='fail'
        if object.exists(roleListViewIduserscreen):
            parent=findObject(roleListViewIduserscreen)
            child=object.children(roleListViewIduserscreen)
            item_0=object.children(child[0])
            
            str1=child[1].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            mouseClick(rolesTabButtonId)
            snooze(2)
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e)) 

'''




#Collecting text from roles tab user management-Add text and navigate to add role screen
def Collecttextfromrolestab():
    try:
        status='fail'
        if object.exists(rolesNewaddButtonId):
                parent=findObject(rolesNewaddButtonId)
                child=object.children(parent)
                str1=child[3].text
                addtolist1(str1)
                test.log('Collected string ='+str(str1))
                snooze(1)
                mouseClick(rolesNewaddButtonId)
                snooze(2)
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e)) 
        

userInfoId={"container": mainWindow, "id": "userInfoId", "type": "RolesTable", "unnamed": 1, "visible": True}       
RoleNameID={"container": mainWindow, "id": "roleNameInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}                              
newPatientPrevilegeSelectorId={"container": mainWindow, "id": "newPatientPrevilegeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}            
modifyPatientPrevilegeSelectorId={"container": mainWindow, "id": "modifyPatientPrevilegeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
approveExamPrevilegeSelectorId={"container": mainWindow, "id": "approveExamPrevilegeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
cancelApproveExamPrevilegeSelectorId={"container": mainWindow, "id": "cancelApproveExamPrevilegeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
deleteExamPrevilegeSelectorId={"container": mainWindow, "id": "deleteExamPrevilegeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
exportExamToPendrivePrevilegeSelectorId={"container": mainWindow, "id": "exportExamToPendrivePrevilegeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": False}
accessToSettingsPrevilegeSelectorId={"container": mainWindow, "id": "accessToSettingsPrevilegeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
accessToUsersPrevilegeSelectorId={"container": mainWindow, "id": "accessToUsersPrevilegeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}

#Collecting title text
NewroletitleID={"container": mainWindow, "id": "titleSpace", "type": "Rectangle", "unnamed": 1, "visible": True}

def Collecttextfrom_Newroletab():
    try:
        status='fail'
        if object.exists(NewroletitleID):
            parent=findObject(NewroletitleID)
            child=object.children(parent)
            Row0=object.children(child[0])
            str1=Row0[2].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
        if Collecttextfromrolestab_Rolename():
            status='pass'    
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e)) 


#Collecting text 'Role name'
def Collecttextfromrolestab_Rolename():
    try:
        status='fail'
        if object.exists(RoleNameID):
            parent=findObject(RoleNameID)
            child=object.children(parent)
            str1=child[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
        #Collecting all the role privilege action  heading
        if collectroleprevillage_actionheading():
            if collectroleprevillage_actions(newPatientPrevilegeSelectorId,modifyPatientPrevilegeSelectorId,
                                             approveExamPrevilegeSelectorId,cancelApproveExamPrevilegeSelectorId,
                                             deleteExamPrevilegeSelectorId,exportExamToPendrivePrevilegeSelectorId,
                                             accessToSettingsPrevilegeSelectorId,accessToUsersPrevilegeSelectorId):
                status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e))         

def collectroleprevillage_actionheading():
    try:
        status='fail'
        if object.exists(userInfoId):
            parent=findObject(userInfoId)
            child=object.children(parent)
            col0=object.children(child[0])
            Row1=object.children(col0[1])
            col00=object.children(Row1[0])
            #Collecting Actions with patients text
            str1=col00[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting Actions with examinations text
            col2=object.children(Row1[2])
            str1=col2[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            #Collecting Actions with settings and user management text
            col4=object.children(Row1[4])
            str1=col4[0].text
            addtolist1(str1)
            test.log('Collected string ='+str(str1))
            snooze(1)
            status='pass'
        return True if status=='pass' else False
    except Exception as e:
        test.log('exception'+str(e)) 
        
        
#Collecting action text

def collectroleprevillage_actions(*arguments):
    try:
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
    
