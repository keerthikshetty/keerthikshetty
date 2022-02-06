import object

'''Objects of main window'''
mainWindow = {"type": "QQuickWindowQmlImpl", "visible": True}
onlineScreen_MainWindow ={"container": mainWindow, "id": "onlineScreenId", "type": "OnlineWfScreen", "visible": True}
evaluationScreen_MainWindow = {"container": mainWindow, "id": "evaluationScreenId", "type": "EvalScreen", "visible": True}
menuScreen_MainWindow = {"container": mainWindow, "id": "menuScreenId", "type": "Rectangle", "visible": True}
patientCardScreen_MainWindow = {"container": mainWindow, "id": "patientScreenId", "type": "PatientCard",  "visible": True}
liveSettingsScreen_MainWindow = {"container": onlineScreen_MainWindow,  "type": "Rectangle", "visible": True}

'''Objects of create user / New user screen'''

userLoginNameInputId = { "container": mainWindow, "id": "userLoginNameInputId", "type": "CustomTextFieldWithLabel",  "visible": True}
userLastNameInputId = { "container": mainWindow, "id": "userLastNameInputId", "type": "CustomTextFieldWithLabel",  "visible": True}
userFirstNameInputId = { "container": mainWindow, "id": "userFirstNameInputId", "type": "CustomTextFieldWithLabel",  "visible": True}
roleInputId = { "container": mainWindow, "id": "roleInputId", "type": "CustomComboBoxWithLabel",  "visible": True}

passwordInputId = { "container": mainWindow, "id": "passwordInputId", "type": "CustomTextFieldWithLabel",  "visible": True}
confirmPasswordInputId = { "container": mainWindow, "id": "confirmPasswordInputId", "type": "CustomTextFieldWithLabel",  "visible": True}

changePasswordAfterFirstLoginSwitchId = { "container": mainWindow, "id": "changePasswordAfterFirstLoginSwitchId", "type": "CustomSwitchWithLabel",  "visible": True}
defaultProfileInputId={"container": mainWindow, "id": "defaultProfileInputId", "type": "CustomComboBoxWithLabel", "unnamed": 1, "visible": True} 
 
 
saveUserButtonId = {  "container": mainWindow, "id": "saveUserButtonId", "type": "CircularButton",  "visible": True}
cancelUserButtonId = {  "container": mainWindow, "id": "cancelUserButtonId", "type": "CircularButton",  "visible": True}

confirmButtonId = {  "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton",  "visible": True}
cancelButtonId = {  "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton",  "visible": True}

backButtonUserScreenId = { "container": mainWindow, "id": "backButtonUserScreenId", "type": "Button", "visible": True}
passwordMatchIconId = { "container": mainWindow, "id": "passwordMatchIconId", "type": "Image", "visible": True}
confirmpasswordMatchIconId = { "container": mainWindow, "id": "confirmpasswordMatchIconId", "type": "Image", "visible": True}

hideKeyBackground={"container": mainWindow, "id": "hideKeyBackground", "type": "Rectangle", "unnamed": 1, "visible": True}


'''Objects of user screen'''
addUserButtonId = { "container": mainWindow, "id": "addUserButtonId", "type": "CircularButton",  "visible": True}                        

userSearchInputId = { "container": mainWindow, "id": "userSearchInputId", "type": "SearchBar",  "visible": True}
userListViewId={"container": mainWindow, "id": "userListViewId", "type": "ListView", "unnamed": 1, "visible": True}

nameSortButtonId = {"container": mainWindow, "id": "nameSortButtonId", "type": "UserSortButton", "visible": True}
loginSortButtonId = {"container": mainWindow, "id": "loginSortButtonId", "type": "UserSortButton", "visible": True}
roleSortButtonId = {"container": mainWindow, "id": "roleSortButtonId", "type": "UserSortButton", "visible": True}
backButtonUserScreenId = {"container": mainWindow, "id": "backButtonUserScreenId", "type": "Button", "visible": True}
searchBarControlImageId = {"container": mainWindow, "id": "searchBarControlImageId", "type": "Image", "visible": True}
editUserButtonId = {"container": mainWindow, "id": "editUserButtonId", "type": "EditUserButton", "visible": True}
deleteUserButtonId = {"container": mainWindow, "id": "deleteUserButtonId", "type": "DeleteButton", "visible": True}
confirmPasswordTextInputId= { "container": mainWindow, "id": "confirmPasswordTextInputId", "type": "CustomTextFieldWithLabelAsRow", "visible": True}
rolesTabButtonId={"checkable": True, "container": mainWindow, "id": "rolesTabButtonId", "type": "TabButton", "unnamed": 1, "visible": True}
usersTabButtonId={"checkable": True, "container": mainWindow, "id": "usersTabButtonId", "type": "TabButton", "unnamed": 1, "visible": True}
autologinModeSelectorId={"container": mainWindow, "id": "autologinModeSelectorId", "type": "CustomSwitchWithLabelColumn", "unnamed": 1, "visible": True}
userSearchField= {"container": mainWindow, "id": "searchField", "type": "TextField", "unnamed": 1, "visible": True}
PassworderrorPopupItemId={"container": mainWindow, "text": "The password length shall be atleast 8 characters ", "type": "Label", "unnamed": 1, "visible": True} 
passwordMatchIconId={"container": mainWindow, "id": "passwordMatchIconId", "source": "qrc:/qml/images/1280x800/passwordmatch.png", "type": "Image", "unnamed": 1, "visible": True}
DiscardwarningMessageId={"container": mainWindow, "id": "discardWarningItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}


'''Objects of Edit user screen'''
changePasswordButtonId = {"container": mainWindow, "id": "changePasswordButtonId", "type": "RoundedRectangleButton", "visible": True}
oldPasswordInputId = { "container": mainWindow, "id": "oldPasswordInputId", "type": "CustomTextFieldWithLabel",  "visible": True}
showConfirmPasswordButton = { "container": mainWindow, "id": "showConfirmPasswordButton", "type": "CircularButton",  "visible": True}
showOldPasswordButton = { "container": mainWindow, "id": "showOldPasswordButton", "type": "CircularButton",  "visible": True}
showPasswordButton = { "container": mainWindow, "id": "showPasswordButton", "type": "CircularButton",  "visible": True}                                
cancelUserButtonId={"checkable": False, "container": mainWindow, "id": "cancelUserButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
RolecustomComboBoxId={"container": mainWindow, "id": "customComboBoxId", "type": "CustomComboBox", "unnamed": 1, "visible": True}
confirmButtonId={"checkable": False, "container": mainWindow, "id": "confirmButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
cancelButtonId={"checkable": False, "container": mainWindow, "id": "cancelButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
saveUserButtonId={"checkable": False, "container": mainWindow, "id": "saveUserButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}



#Object from menu screen
menuRecordingButton = {"checkable": False, "container": mainWindow, "id": "menuRecordingButtonId", "type": "CircularButton",  "visible": True}
menuPatientcardButton = {"checkable": False, "container": menuScreen_MainWindow, "id": "menuPatientcardButtonId", "type": "CircularButton",  "visible": True}
menuWorklistButton = {"checkable": False, "container": menuScreen_MainWindow, "id": "menuWorklistButtonId", "type": "CircularButton",  "visible": True}
menuUserButton = {"checkable": False, "container": menuScreen_MainWindow, "id": "menuUsersButtonId", "type": "CircularButton",  "visible": True}
menuSettingsButton ={"checkable": False, "container": menuScreen_MainWindow, "id": "menuSettingsButtonId", "type": "CircularButton",  "visible": True}
menuScreenLogButtonId={"checkable": False, "container": mainWindow, "id": "menuScreenLogButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}


#login screen objects
logButtonId= {"container": mainWindow, "id": "logButtonId", "type": "LogOutButton", "unnamed": 1, "visible": True}
loginNameEntryFieldId ={"container": mainWindow, "id": "loginNameEntryFieldId", "type": "PatientInfoField", "unnamed": 1, "visible": True}
loginPasswordInputId = {"container": mainWindow, "id": "loginPasswordInputId", "type": "CustomTextFieldWithLabelAsRow", "unnamed": 1, "visible": True}
loginButton ={"checkable": False, "container": mainWindow, "id": "loginButton", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
loginscreenpasswordID={"container": mainWindow, "id": "loginPasswordInputId", "type": "CustomTextFieldWithLabelAsRow", "unnamed": 1, "visible": True}
loginPopupItemId={"container": mainWindow, "id": "loginPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
skipLoginButtonID={"checkable": False, "container": mainWindow, "id": "skipLoginButton", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
loginscreenaccepterror={"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
OnlinescreenLogoutbutton={"container": mainWindow, "id": "logButtonId", "type": "LogOutButton", "unnamed": 1, "visible": True}


#Role tab object
rolesListviewId={"container": mainWindow, "id": "rolesListviewId", "type": "RolesListView", "unnamed": 1, "visible": True}
rolesTabButtonId={"checkable": True, "container": mainWindow, "id": "rolesTabButtonId", "type": "TabButton", "unnamed": 1, "visible": True}
rolesNewViewButtonId={"checkable": False, "container": mainWindow, "id": "rolesNewViewButtonId", "type": "RoundedRectangleButton", "unnamed": 1, "visible": True}
editRoleButtonId={"checkable": False, "container": mainWindow, "id": "editRoleButtonId", "type": "EditUserButton", "unnamed": 1, "visible": True}
deleteRoleButtonId={"checkable": False, "container": mainWindow, "id": "deleteRoleButtonId", "type": "DeleteButton", "unnamed": 1, "visible": True}
roleNameInputId={"container": mainWindow, "id": "roleNameInputId", "type": "CustomTextFieldWithLabel", "unnamed": 1, "visible": True}
newPatientPrevilegeSelectorId={"container": mainWindow, "id": "newPatientPrevilegeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
modifyPatientPrevilegeSelectorId={"container": mainWindow, "id": "modifyPatientPrevilegeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
approveExamPrevilegeSelectorId={"container": mainWindow, "id": "approveExamPrevilegeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
cancelApproveExamPrevilegeSelectorId={"container": mainWindow, "id": "cancelApproveExamPrevilegeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
accessToSettingsPrevilegeSelectorId={"container": mainWindow, "id": "accessToSettingsPrevilegeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
accessToUsersPrevilegeSelectorId={"container": mainWindow, "id": "accessToUsersPrevilegeSelectorId", "type": "CustomSwitchWithLabel", "unnamed": 1, "visible": True}
saveUserButtonIdRles={"checkable": False, "container": mainWindow, "id": "saveUserButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}
deleteWarningItemId={"container": mainWindow, "id": "deleteWarningItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
apcErrorPopupItemId={"container": mainWindow, "id": "apcErrorPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}
okButtonId={"checkable": False, "container": mainWindow, "id": "okButtonId", "type": "CircularButton", "unnamed": 1, "visible": True}


#Auto login related
AutologinONbutton={"checkable": True, "container": mainWindow, "id": "onSwitchId", "type": "CustomRadioButton", "unnamed": 1, "visible": True}
confirmPopupItemIdAutologin={"container": mainWindow, "id": "confirmPopupItemId", "type": "WarningPopUp", "unnamed": 1, "visible": True}





#Method to verify last selected sorting is applied and verify the sorted list(Ascending)
def verifyLastappliedSortMechanismAsc(obj,sorttype):
    try:
        status='fail'
        objct=findObject(obj)
        if object.exists(obj):
            if objct.state==sorttype:
                test.log('Last applied Ascending sorting method is saved')
                if testAscendingSortInUserListScreen(obj):
                    status='pass'
                else:
                    test.log('List is not sorted based on the ascending order')
                    status='fail'    
            else:
                test.log('ascending sort type is not highlighted')
        else:
            test.log('Name sorting object not found')
            
        return True if status=='pass'   else False
                
    except Exception as e:
        test.fail("Exception" +str(e))
        
#Method to verify last selected sorting is applied and verify the sorted list(descending)
def verifyLastappliedSortMechanismDec(obj,sorttype):
    try:
        status='fail'
        objct=findObject(obj)
        if object.exists(obj):
            if objct.state==sorttype:
                test.log('Last applied descending sorting method is saved')
                if testDescendingSortInUserListScreen(obj):
                    status='pass'
                else:
                    test.log('List is not sorted based on the ascending order')
                    status='fail'    
            else:
                test.log('ascending sort type is not highlighted')
        else:
            test.log('Name sorting object not found')
            
        return True if status=='pass'   else False
                
    except Exception as e:
        test.fail("Exception" +str(e))






#Method to check all sorting applied at a time
def methodToVerifAllSortingAppliedAtaTime(nameSortButtonId,loginSortButtonId,roleSortButtonId):
    try:
        count=0
        value1='ascendingSort'
        value2='descendingSort'
        Name=findObject(nameSortButtonId)
        Login=findObject(loginSortButtonId)
        Role=findObject(roleSortButtonId)
        
        if object.exists(nameSortButtonId):
            mouseClick(nameSortButtonId)
            snooze(2)
            if Name.state==(value1) or (value2):
                test.log('Name sorting is highlighted')
                if (Login.state=='') and (Role.state==''):
                    test.log('Login and Role not highlighted')
                    count=count+1
                else:
                    test.log('Login or Role is also highlighted along with Name sort')
            else:
                test.log('Name sorting is not highlighted')
        else:
            test.log('Name sorting object not found')
                
        if object.exists(loginSortButtonId):
            mouseClick(loginSortButtonId)
            snooze(2)
            if Login.state==(value1) or (value2):
                test.log('Login sorting is highlighted')
                if (Name.state=='') and (Role.state==''):
                    test.log('Name and Role not highlighted')
                    count=count+1
                else:
                    test.log('Name or Role is also highlighted along with Name sort')
            else:
                test.log('Login sorting is not highlighted')
        else:
            test.log('Login sorting object not found')
            
        if object.exists(roleSortButtonId):
            mouseClick(roleSortButtonId)
            snooze(2)
            if Role.state==(value1) or (value2):
                test.log('Role sorting is highlighted')
                if (Name.state=='') and (Login.state==''):
                    test.log('Name and Login not highlighted')
                    count=count+1
                else:
                    test.log('Name or Login is also highlighted along with Name sort')
            else:
                test.log('Role sorting is not highlighted')
        else:
            test.log('Name sorting object not found')
                
        return True if count==3 else False
                
    except Exception as e:
        test.fail("Exception" +str(e))


# Common method to verify the options
def CommonMethodToVerifyOptions(list,n):
    try:
        count=0  
        for x in list:
            if object.exists(x):
                #test.log('Object listed')
                count=count+1
            else:
                test.log('All objects are not listing')
        return True if count==n else False
        
    except Exception as e:
        test.fail("Exception" +str(e))
       
def CommonMethodToVerifyOptionsisfalse(list1,n1): 
    try:
        count=0  
        for x in list:
            if object.exists(x):
                obj=findObject(x)
                if obj.visible:
                    test.log('Object are visible for the user')
                    count=count+1
                else:
                    test.log('Object are not visible for the user')
                    count=count+1
                    
                test.log('All objects are listing')
            else:
                test.log('objects not listing')
        return True if count==n1 else False
        
    except Exception as e:
        test.fail("Exception" +str(e))

#Common method to verify options is enabled or disabled

def CommonMethodToVerifyOptionisEnabled(list1,n1):
    try:
        count=0
        for x in list1:
            if object.exists(x):
                obj=findObject(x)
                if not obj.enabled:
                    count=count+1
                else:
                    test.log('Object is editable')
                    
        return True if count==n1 else False
        
    except Exception as e:
        test.fail("Exception" +str(e))

 
#Navigate to add user screen from user list screen
def NavigateToaddUserScreen():
    try:
        status=False
        if object.exists(addUserButtonId):
            mouseClick(addUserButtonId)
            test.log('Add button is clicked')
            if object.exists(userLoginNameInputId):
                test.log('Successfully navigated to the new user screen')
                status=True
            else:
                test.log('Failed to navigate to add new user screen')
    
        return status
       
    except Exception as e:
        test.fail("Exception" + str(e))


# Functions to enter all the values in add user screen field
def EnterUserInformationInUserCretationScreen(Login,LastName,FirstName,NewPassword,ConfirmPassword,Role):
    try:
        totalarguments=6
        count =0 
        snooze(1)
        if waitForObject(userLoginNameInputId):
            setFocusTextBox(userLoginNameInputId)
            type(mainWindow, Login)
            count+=1
        if waitForObject(userLastNameInputId):
            setFocusTextBox(userLastNameInputId)
            type(mainWindow, LastName)
            count+=1
        if waitForObject(userFirstNameInputId):
            setFocusTextBox(userFirstNameInputId)
            type(mainWindow, FirstName)
            count+=1
        if waitForObject(passwordInputId):
            setFocusTextBox(passwordInputId)
            type(mainWindow, NewPassword)
            count+=1
        if waitForObject(confirmPasswordInputId):
            setFocusTextBox(confirmPasswordInputId)
            type(mainWindow, ConfirmPassword)
            snooze(1)
            count+=1
        if selectComboBoxItem(waitForObject(roleInputId),Role):
            count+=1
            test.log("Entered all the values in user creation screen")
        if object.exists(hideKeyBackground):
            mouseClick(hideKeyBackground)
            
        else:
            test.log('Not able verify all items')
            
        return True if count==totalarguments else False
      
    except Exception as e:
        test.fail("Exception" +str(e))                       
  
                               
#Function to click on cancel button in user creation screen
def CancelButtonInUserCreationScreenAndWarningPopUp():
    try:
        count =0 
        snooze(1)
        if waitForObject(cancelUserButtonId):
            mouseClick(waitForObject(cancelUserButtonId))
            snooze(2)
            if (object.exists(DiscardwarningMessageId)):
                parent=findObject(DiscardwarningMessageId)
                child=object.children(parent)
                coln_0=object.children(child[0])
                item2=object.children(coln_0[2])
                Row_0=object.children(item2[0])
                warningText = Row_0[2].text
                if ("Are you sure want to discard the changes?" in str(warningText)):
                    if object.exists(confirmButtonId) and object.exists(cancelButtonId):
                        count=1
                        test.log("successfully verified warning message and accept and reject button is available in warning message")
                else:
                    test.log('Are you sure want to discard the changes not displayed')            
            else:
                test.log("Warning message not displayed")
        else:
            test.log('Cancel button not found')
        
        return True if count==1 else False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
                               

#Cancel button or back button press and verify the behaviour.

def CancelButtonBackbuttonAcceptButton(obj,obj1):
    try:
        status='Fail'
        snooze(1)
        if object.exists(obj):
            mouseClick(waitForObject(obj))
            test.log('Clicked obj button')
            snooze(1)
        if object.exists(obj1):
            status='pass'
                
        return True if status=='pass' else False
                           
    except Exception as e:
        test.fail("Exception" +str(e))        
                
                              
# Method to verify  user details for all the fields in New user screen
def VerifyLastenteredUserValuesInNewUserScreen(Login,LastName,FirstName,NewPassword,ConfirmPassword,Role):
    try:
        totalarguments=5
        count =0 
        snooze(1) 
        snooze(1)
        if waitForObject(userLoginNameInputId):
            loginText= __getTextFromTextBox(userLoginNameInputId)
            if str(loginText) == Login:
                count+=1             
                test.log(" Given Login name is exists ")
                
        if object.exists(userLastNameInputId):
            lastNameText= __getTextFromTextBox(userLastNameInputId)
            if str(lastNameText) == LastName :
                count+=1
                test.log(" Given Last name is exists ")
                        
        if object.exists(userFirstNameInputId):
            firstNameText= __getTextFromTextBox(userFirstNameInputId)
            if str(firstNameText) == FirstName :
                count+=1
                test.log(" Given first name is exists ")
                                               
        if object.exists(passwordInputId):
            passwordText= __getTextFromTextBox(passwordInputId)
            if str(passwordText) == NewPassword :
                count+=1
                test.log(" Given password is exists ")
                                        
        if object.exists(confirmPasswordInputId):
            confPasswordText= __getTextFromTextBox(confirmPasswordInputId)
            if str(confPasswordText) == ConfirmPassword :
                count+=1
                test.log(" Given confirm password is exists ")  
                
        else:
            test.log('Not able to verify new user screen values')                              
            
        return True if count==totalarguments else False                       
                           
    except Exception as e:
        test.fail("Exception" +str(e))                               
                               
                               
#Login to the device with cred
def LoginToDeviceAndVerifyTheUserNameinOnlineScreen(Login,ConfirmPassword,FirstName,LastName,passwordlen):
    try:
        status=False
        if object.exists(loginNameEntryFieldId):
            setFocusTextBox(loginNameEntryFieldId)
            type(mainWindow,Login)
            #test.log('Succesfully entered login id')
            snooze(1)
            if object.exists(loginPasswordInputId):
                setFocusTextBox(loginPasswordInputId)
                type(mainWindow,ConfirmPassword)
                #test.log('Succesfully entered password')
                snooze(1)
                if VerifyPassWordisMaskedorNot(passwordlen):
                    test.log('Password is masked')
                if waitForObject(loginButton):
                    mouseClick(loginButton)
                    snooze(3)
                    if object.exists(OnlinescreenLogoutbutton):
                        parent=findObject(OnlinescreenLogoutbutton)
                        child=object.children(parent)
                        Rec0=object.children(child[1])
                        UserNameA=Rec0[0].text
                        #admin user has extra space in start and end, hence using this method
                        #UserName=(str(UserNameA).lstrip())
                        A= FirstName+ ' ' +LastName
                        #B=(str(A).rstrip())
                        if str(UserNameA)==str(A):
                            test.log('User name is displayed in the online screen is matching with logged in user')
                            status=True
                        else:
                            test.log('Logged in name is not matching')
                        
                            
        return True if status==True else False
                           
    except Exception as e:
        test.fail("Exception" +str(e))                           

PasswordTextinput={"backgroundcolor": "#ffffff", "container": mainWindow, "echoMode": 2, "id": "textInputId", "passwordCharacter": "*", "type": "TextField", "unnamed": 1, "visible": True}
                               
def VerifyPassWordisMaskedorNot(passwordlen):
    try:
        status=False
        if object.exists(loginPasswordInputId):
            if waitForObject(loginPasswordInputId):
                loginText= __getDisplaytextfromTextBox(PasswordTextinput)
                y='*'
                if str(loginText) == (passwordlen)*y:            
                    test.log("Password is masked and length also matching ")
                    status=True
                            
                        
        return True if status==True else False
                           
    except Exception as e:
        test.fail("Exception" +str(e))                        
                                                    
                               
                        
#Function to navigate from Menu screen to Users screen
def createAnUserWithMandatoryValuesFirstTime(userName, lastName, newPass, confirmPass):
    try:
        count =0 
        snooze(1)
        if waitForObject(userLoginNameInputId):
            setFocusTextBox(userLoginNameInputId)
            type(mainWindow, userName)
            if waitForObject(userLastNameInputId):
                setFocusTextBox(userLastNameInputId)
                type(mainWindow, lastName)
                if waitForObject(passwordInputId):
                    setFocusTextBox(passwordInputId)
                    type(mainWindow, newPass)
                    if waitForObject(confirmPasswordInputId):
                        setFocusTextBox(confirmPasswordInputId)
                        type(mainWindow, confirmPass)
                        
                        if waitForObject(saveUserButtonId):
                            mouseClick(waitForObject(saveUserButtonId))
                            snooze(1)  
                            if waitForObject(loginNameEntryFieldId):
                                test.log(" Successfully created and saved user ")
                                count =1
                            else:
                                test.fail(" Fail to create and save user ")
        else:
            test.fail("Create user screen is not displayed ")
        if count == 1:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))

# Method to save create users screen
def saveCreateUserScreen():
    try:
        count =0 
        snooze(1)
        if waitForObject(saveUserButtonId):
            mouseClick(waitForObject(saveUserButtonId))
            snooze(1)  
            if waitForObject(addUserButtonId):
                test.log(" Successfully saved user ")
                count =1
            else:
                test.fail(" Fail to save user ")
        if count == 1:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))


# Function to Search an user using Login name and verify it is exists or not 
def searchAnUserInUsersListAndVerifyRecordExistsOrNot(LoginIDSearch):
    try:
        status = False
        loginIDToSearch = LoginIDSearch
        snooze(1)
        if (waitForObject(userSearchInputId)):
            setFocusTextBox(userSearchInputId)
            type(mainWindow,loginIDToSearch)
            
            if (object.exists(userListViewId)):              
                
                userTable = waitForObject(userListViewId)
                userListItem = object.children(userTable)
                snooze(1)
                userSubItems = object.children(userListItem[0])
                userSubList = object.children(userSubItems[0])
                userSubListItem = object.children(userSubList[0])
                userRow = object.children(userSubListItem[1])
                userRowItem = object.children(userRow[0])
                rowValue = userRowItem[3].text

                if (rowValue == loginIDToSearch):
                    test.log(" Successfully searched '"+ loginIDToSearch +"' record from users list")
                    status = True
                    
                else:
                    test.log("No matching user record found in the user list " )
                                        
            else:
                    test.log(" User list is empty ")            
        else:
            test.log(" Search option is not displayed in users screen ")
        
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))
        
        
# Function to Search an user using user name and verify it is exists or not 
def SearchAnUserInUsersListAndVerifyRecordExistsOrNotUserName(LastName,FirstName):
    try:
        status = False
        UserNameToSearch = LastName+" , "+FirstName
        snooze(1)
        if (waitForObject(userSearchInputId)):
            setFocusTextBox(userSearchInputId)
            type(mainWindow,UserNameToSearch)
            snooze(1)
            if (object.exists(userListViewId)):              
                
                userTable = waitForObject(userListViewId)
                userListItem = object.children(userTable)
                snooze(1)
                userSubItems = object.children(userListItem[0])
                userSubList = object.children(userSubItems[0])
                userSubListItem = object.children(userSubList[0])
                userRow = object.children(userSubListItem[1])
                userRowItem = object.children(userRow[0])
                rowValue = userRowItem[1].text

                if (rowValue == UserNameToSearch):
                    test.log(" Successfully searched '"+ UserNameToSearch +"' record from users list")
                    status = True
                    
                else:
                    test.log("No matching user record found in the user list " )
                                        
            else:
                    test.log(" User list is empty ")            
        else:
            test.log(" Search option is not displayed in users screen ")
        
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))       
        
        
          
        
        
        
#Function to check user list is available.
def VerifyUserListisavalibleorNot():
    try:
        status = False
        snooze(1)
        if (object.exists(userListViewId)): 
            test.log('User list screen is available') 
            status = True           
                                        
        else:
            test.log(" User list is not available")            
        
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))   
        
        
        
 
# Function to Search an user using Name 
def searchAnUserInUsersListUsingName(userNameToSearch):
    try:
        status = False
        nameToSearch = userNameToSearch
        snooze(1)
        if (waitForObject(userSearchInputId)):
            type(waitForObject(userSearchInputId), nameToSearch)
            
            if (waitForObject(userListViewId)):               
                
                userTable = waitForObject(userListViewId)
                userListItem = object.children(userTable)
                snooze(1)
                userSubItems = object.children(userListItem[0])
                userSubList = object.children(userSubItems[0])
                userSubListItem = object.children(userSubList[0])
                userRow = object.children(userSubListItem[1])
                userRowItem = object.children(userRow[0])
                rowValue = userRowItem[1].text

                if (rowValue == nameToSearch):
                    test.log(" Successfully searched '"+ nameToSearch +"' record from users list")
                    status = True
                    
                else:
                    test.log("No matching user record found in the user list " )
                                        
            else:
                    test.log(" User list is empty ")            
        else:
            test.log(" Search option is not displayed in users screen ")
        
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))

# Method to Search an user using Login name and click on user 
def searchAnUserInUsersListAndClickOnIt(LoginIDSearch):
    try:
        status = False
        loginIDToSearch = LoginIDSearch
        snooze(1)
        if (waitForObject(userSearchInputId)):
            setFocusTextBox(userSearchInputId)
            type(mainWindow,LoginIDSearch)
            
            if (waitForObject(userListViewId)):               
                
                userTable = waitForObject(userListViewId)
                userListItem = object.children(userTable)
                snooze(1)
                userSubItems = object.children(userListItem[0])
                userSubList = object.children(userSubItems[0])
                userSubListItem = object.children(userSubList[0])
                userRow = object.children(userSubListItem[1])
                userRowItem = object.children(userRow[0])
                rowValue = userRowItem[3].text

                if (rowValue == loginIDToSearch):
                    mouseClick(userSubListItem[1])
                    snooze(.5)
                    if object.exists(editUserButtonId):
                        test.log(" Successfully clicked on user record ")
                        status = True
                    
                else:
                    test.log("No matching user record found in the user list " )
                                        
            else:
                    test.log(" User list is empty ")            
        else:
            test.log(" Search option is not displayed in users screen ")
        
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Method to navigate to Live page from users page  
def navigateToLiveFromUsersPage():
    try:
        status = False
        if (waitForObject(backButtonUserScreenId)):
            mouseClick(waitForObject(backButtonUserScreenId))
            mouseClick(waitForObject(menuRecordingButton))
            snooze(1)
            if (waitForObject(liveScreenECGRecordButton)):
                test.log("Successfully navigated to live screen")
                status = True
            else:                
                test.log("Unable to navigate to live screen")
            
        else:
            test.log(" Unable to click back button in examination screen ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))

# Method to verify no user exists warning pop up  
def verifyNoUserExistsWarning():
    try:
        status = False
        snooze(1)
        if (object.exists(evaluationScreenwarningMessageId)):
            warningObj = waitForObject(evaluationScreenwarningMessageId)
            warningText = warningObj.text
            
            if ("No user exists, Please create a user for security reasons" in str(warningText)):              
                if object.exists(okButtonId):
                    test.log(" Successfully verified 'No user exists' warning popup ")
                    status = True                    
                
                else:
                    test.fail(" Fail to verify 'No user exists' warning popup")
            
        else:
            test.log(" 'No user exists' warning message is not displayed  ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))      

# Method to verify confirmation before deleting the user 
def verifyDeleteUserConfirmWarning():
    try:
        status = False
        snooze(1)
        if (object.exists(evaluationScreenwarningMessageId)):
            warningObj = waitForObject(evaluationScreenwarningMessageId)
            warningText = warningObj.text
            
            if ("Enter your password before deleting the user" in str(warningText)):              
                if object.exists(confirmButtonId):
                    test.log(" Successfully verified 'Delete user confirmation' pop up ")
                    status = True                                 
                else:
                    test.fail(" Fail to verify 'Delete user confirmation' pop up")         
        else:
            test.log(" 'Delete user confirmation' message is not displayed  ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e)) 
        
# Method to click 'ok' on  No user exists warning pop up  
def clickOnNoUserExistsWarning():
    try:
        status = False
        snooze(.5)
        if (object.exists(okButtonId)):
            mouseClick(okButtonId)            
            if (object.exists(evaluationScreenwarningMessageId)):
                test.fail(" Fail to click on 'Tick' mark on 'No user exists' warning popup")
            
            else:
                test.log(" Successfully clicked on 'Tick' mark on warning popup ")
                status = True            
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
        
# Method to verify available fields in 'New user' creation screen  
def verifyFieldsInNewUserScreen():
    try:
        status = False
        snooze(.5)
        if (waitForObject(userLoginNameInputId)):
            if (object.exists(userLastNameInputId)):
                if (object.exists(userFirstNameInputId)):
                    if (object.exists(passwordInputId)):
                        if (object.exists(confirmPasswordInputId)):
                            if (object.exists(roleInputId)):
                                
                                if (object.exists(defaultProfileInputId)):
                                    if (object.exists(changePasswordAfterFirstLoginSwitchId)):
                                        status = True   
                                        test.log(" Successfully verified fields in 'New user' screen Login, Role (Disabled), Last name, First name, Default profile (Disabled), New password, Confirm Password and  Change password after first login (on/off toggle button)Disabled ")
        else: 
            test.fail(" Fail to verify fields in 'New user' screen ")          
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
        
# Method to enter user details for all the fields in New user screen
def EnterUserValuesInNewUserScreen(userName, lastName, firstName, newPass, confirmPass):
    try:
        status = False 
        snooze(1)
        if waitForObject(userLoginNameInputId):
            setFocusTextBox(userLoginNameInputId)
            type(mainWindow, userName)
            if waitForObject(userLastNameInputId):
                setFocusTextBox(userLastNameInputId)
                type(mainWindow, lastName)
                if waitForObject(userFirstNameInputId):
                    setFocusTextBox(userFirstNameInputId)
                    type(mainWindow, firstName)
                    if waitForObject(passwordInputId):
                        setFocusTextBox(passwordInputId)
                        type(mainWindow, newPass)
                        if waitForObject(confirmPasswordInputId):
                            setFocusTextBox(confirmPasswordInputId)
                            type(mainWindow, confirmPass)
                            status = True
        else:
            test.fail(" New user screen is not displayed ")
            
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))

# Method to click 'cancel' on  No user screen   
def clickOnCancelOnNewUserScreen():
    try:
        status = False
        snooze(.5)
        if (object.exists(cancelUserButtonId)):
            mouseClick(cancelUserButtonId)            
            status = True            
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))

# Method to verify discard changes warning pop up  
def verifyDiscardChangesWarning():
    try:
        status = False
        snooze(1)
        if (object.exists(evaluationScreenwarningMessageId)):
            warningObj = waitForObject(evaluationScreenwarningMessageId)
            warningText = warningObj.text
            
            if ("Are you sure want to discard the changes?" in str(warningText)):              
                if object.exists(confirmButtonId):
                    if object.exists(cancelButtonId):
                        test.log(" Successfully verified 'discard the changes' warning popup ")
                        status = True                    
                
                else:
                    test.fail(" Fail to verify 'discard the changes' warning popup")
            
        else:
            test.log(" 'Discard the changes' warning message is not displayed  ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e)) 
        
# Method to verify discard changes warning pop up and reject the changes 
def verifyDiscardChangesWarningAndReject():
    try:
        status = False
        if (object.exists(evaluationScreenwarningMessageId)):
            warningObj = waitForObject(evaluationScreenwarningMessageId)
            warningText = warningObj.text
            
            if ("Are you sure want to discard the changes?" in str(warningText)):              
                if object.exists(confirmButtonId):
                    if object.exists(cancelButtonId):
                        mouseClick(cancelButtonId)
                        if object.exists(cancelButtonId):
                            test.fail(" Fail to reject the warning popup")                    
                
                        else:
                            test.log(" Successfully 'Rejected' the warning popup ")
                            status = True
            
        else:
            test.log(" 'Discard the changes' warning message is not displayed  ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))      

# Method to verify discard changes warning pop up and confirm the changes 
def verifyDiscardChangesWarningAndConfirm():
    try:
        status = False
        if (object.exists(evaluationScreenwarningMessageId)):
            warningObj = waitForObject(evaluationScreenwarningMessageId)
            warningText = warningObj.text
            
            if ("Are you sure want to discard the changes?" in str(warningText)):              
                if object.exists(confirmButtonId):
                    if object.exists(cancelButtonId):
                        mouseClick(confirmButtonId)
                        snooze(2)
                        if object.exists( addUserButtonId):
                            test.log(" Successfully confirmed the warning popup ")
                            status = True                    
                
                else:
                    test.fail(" Fail to confirm the warning popup")
            
        else:
            test.log(" 'Discard the changes' warning message is not displayed  ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))      

# Method to verify  user details for all the fields in New user screen
def VerifyUserValuesInNewUserScreen(userName, lastName, firstName, newPass, confirmPass):
    try:
        status = False 
        snooze(1)
        if waitForObject(userLoginNameInputId):
            loginText= __getTextFromTextBox(userLoginNameInputId)
            if str(loginText) == userName :
                test.log(" Given Login name is exists ")
                
                if object.exists(userLastNameInputId):
                    lastNameText= __getTextFromTextBox(userLastNameInputId)
                    if str(lastNameText) == lastName :
                        test.log(" Given Last name is exists ")
                        
                        if object.exists(userFirstNameInputId):
                            firstNameText= __getTextFromTextBox(userFirstNameInputId)
                            if str(firstNameText) == firstName :
                                test.log(" Given first name is exists ")
                                               
                                if object.exists(passwordInputId):
                                    passwordText= __getTextFromTextBox(passwordInputId)
                                    if str(passwordText) == newPass :
                                        test.log(" Given password is exists ")
                                        
                                        if object.exists(confirmPasswordInputId):
                                            confPasswordText= __getTextFromTextBox(confirmPasswordInputId)
                                            if str(confPasswordText) == confirmPass :
                                                test.log(" Given confirm password is exists ")                                
                                                status = True
        else:
            test.fail(" Not able to verify new user screen values ")
            
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Method to get text from a textbox  
def __getTextFromTextBox(obj):
    try:
        snooze(1)
        if (object.exists(obj)):
            givenObj=waitForObject(obj)
            valueOfText=givenObj.input
            return valueOfText                    
        else:
            test.log(" Given object is not exists ")
            
    except Exception as e:
        test.fail("Exception"+ str(e)) 
        
        
        
# Method to get password tab text
def __getDisplaytextfromTextBox(obj):
    try:
        snooze(1)
        if (object.exists(obj)):
            givenObj=waitForObject(obj)
            valueOfText=givenObj.displayText
            return valueOfText                    
        else:
            test.log(" Given object is not exists ")
            
    except Exception as e:
        test.fail("Exception"+ str(e))         
        
        
        
# Method to set text box empty in Edit user screen  
def __setTextBoxEmptyInEditUser(obj):
    try:
        snooze(.5)
        status = False
        if (object.exists(obj)):
            givenObj = waitForObject(obj)
            childObj = object.children(givenObj)
            childObj[1].text = ""
            status = True                 
        else:
            test.log(" Given object is not exists ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e)) 
        
        
# Method to get value from a text box in Edit user screen  
def __getTextFromTextBoxEditUser(obj):
    try:
        snooze(.5)
        if (object.exists(obj)):
            givenObj = waitForObject(obj)
            childObj = object.children(givenObj)
            textValue = childObj[1].text
            return textValue                
        else:
            test.log(" Given object is not exists ")
            
    except Exception as e:
        test.fail("Exception"+ str(e))         

        
# Method to navigate to new user screen from users screen  
def navigateToNewuserScreenFromUsersScreen():
    try:
        status = False
        snooze(1)
        if (waitForObject(addUserButtonId)):
            mouseClick(waitForObject(addUserButtonId))
            snooze(1)
            if (waitForObject(userLoginNameInputId)):
                test.log("Successfully navigated to new user screen")
                status = True
            else:                
                test.log("Unable to navigate to new user screen")
            
        else:
            test.log(" Fail to navigate to new user screen ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
        
# Method to navigate to user screen from new user screen  
def navigateToUsersScreenFromNewusersScreen():
    try:
        status = False
        snooze(1)
        if (waitForObject(backButtonUserScreenId)):
            mouseClick(waitForObject(backButtonUserScreenId))
            snooze(1)
            if (waitForObject(addUserButtonId)):
                test.log("Successfully navigated to users screen")
                status = True
            else:                
                test.log("Unable to navigate to users screen")
            
        else:
            test.log(" Fail to navigate to users screen ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
        
# Method to save new user for the first time
def saveNewuserInNewuserScreenFirstTime():
    try:
        status = False
        snooze(1)
        if (waitForObject(saveUserButtonId)):
            mouseClick(waitForObject(saveUserButtonId))
            snooze(1)
            if (waitForObject(loginNameEntryFieldId)):
                test.log("Successfully saved new user ")
                status = True
            else:                
                test.log(" Unable to save new user ")
            
        else:
            test.log(" Fail to save new user in new users screen ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))

# Method to save new user in the new user screen
def saveNewuserInNewuserScreen():
    try:
        status = False
        snooze(1)
        if (waitForObject(saveUserButtonId)):
            mouseClick(waitForObject(saveUserButtonId))
            snooze(1)
            if (waitForObject(addUserButtonId)):
                test.log("Successfully saved new user ")
                status = True
            else:                
                test.log(" Unable to save new user ")
            
        else:
            test.log(" Fail to save new user in new users screen ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))

#Method to verify options in Users screen
def verifyOptionsInUsersScreen():
    try:
        status = False 
        snooze(1)
        if waitForObject(userSearchInputId):
            if object.exists(nameSortButtonId):
                if object.exists(userListViewId):
                    if object.exists(loginSortButtonId):
                        if object.exists(roleSortButtonId):
                            status = True
                            test.log(" Users screen is displayed with below information 'Search tab', 'Name', 'Login', 'Role (Disabled)' and 'User list' ")

        else:
            test.fail(" Fail to verify users options ")
            
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))  



# Function to clear Search field in users screen  
def clearSearchFieldInUsersScreen():
    try:
        status = False
        snooze(.5)
        UserserachField = waitForObject(userSearchField)
        UserserachField.text = ""
        #UserserachField.placeholderText = ""
        test.log(" Search option is not displayed in users screen ")
        status = True
        
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))

# Function to clear Search field using clear button in users screen  
def clearSearchFieldUsingClearButtonInUsersScreen():
    try:
        status = False
        snooze(.5)
        if (waitForObject(searchBarControlImageId)):
            mouseClick(searchBarControlImageId)
            searchBox = (waitForObject(userSearchInputId))
            value = searchBox.text
            if str(value)=="":
                status = True
        else:
            test.log(" Clear icon is not displayed in users screen ")
        
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))

# Method to verify user list is empty or not after entering invalid user name 
def verifyUsersListForInvalidUser(toSearch):
    try:
        status = False
        nameToSearch = toSearch
        snooze(1)
        if (waitForObject(userSearchInputId)):
            type(waitForObject(userSearchInputId), nameToSearch)
            
            if (object.exists(userListViewId)==False): 
                test.log(" User list is empty ")              
                status = True                       
            else:
                test.log(" Failed, user list is not empty ")            
        else:
            test.log(" Search option is not displayed in users screen ")
        
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))

# Method to get user list record count 
def getRecordCountFromUsersScreen():
    try:       
        listCount=0
        snooze(1)
        if (waitForObject(userListViewId)): 
            userList = waitForObject(userListViewId)
            listCount = userList.count
            return listCount                 
        else:
            test.log(" Failed, user list is not empty ")            
        
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Method to verify options in Users screen after clicking an user record
def verifyOptionsAfterClickingOnAnUser():
    try:
        status = False 
        snooze(1)
        if waitForObject(editUserButtonId):
            if object.exists(deleteUserButtonId):
                status = True
                test.log(" Edit and Delete options are displayed after selecting a record ")

        else:
            test.fail(" Fail to verify Delete and Edit buttons ")
            
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))  
        
# Method to click on Edit icon in users list screen 
def clickOnEditUserButton():
    try:
        status = False
        snooze(1)
        if (waitForObject(editUserButtonId)):
            mouseClick(editUserButtonId)
                       
            if (waitForObject(userLoginNameInputId)):
                test.log(" Successfully clicked on Edit button ")
                status = True
   
            else:
                test.log(" Fail to click on Edit user screen is not displayed ")
                
        else:
            test.log(" Fail to click on Edit button ")
        
        if status:
            return True
        else:
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e)) 

# Method to click on Delete icon in users list screen 
def clickOnDeleteUserButton():
    try:
        status = False
        snooze(1)
        if (waitForObject(deleteUserButtonId)):
            mouseClick(deleteUserButtonId)
                       
            if (waitForObject(confirmPasswordTextInputId)):
                test.log(" Successfully clicked on Delete button ")
                status = True 
            else:
                test.log(" Fail to click on Delete in user screen ")               
        else:
            test.log(" Fail to click on Delete button ")
        
        if status:
            return True
        else:
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e)) 
        
# Method to verify available fields in 'Edit user' screen  
def verifyFieldsInEditUserScreen():
    try:
        status = False
        snooze(.5)
        if (waitForObject(userLoginNameInputId)):
            if (object.exists(userLastNameInputId)):
                if (object.exists(userFirstNameInputId)):
                    if (object.exists(roleInputId)):                               
                        if (object.exists(defaultProfileInputId)):
                            if (object.exists(changePasswordButtonId)):
                                status = True   
                                test.log(" Successfully verified fields in 'Edit user' screen Login, Role (Disabled), Last name, First name, Default profile (Disabled) and  Change password ")
        else: 
            test.fail(" Fail to verify fields in 'Edit user' screen ")          
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
        

# Method to verify  user details for all the fields in Edit user screen
def VerifyUserValuesInEditUserScreen(userName, lastName, firstName):
    try:
        status = False 
        snooze(1)
        if waitForObject(userLoginNameInputId):
            loginText= __getTextFromTextBoxEditUser(userLoginNameInputId)
            snooze(.5)
            if str(loginText) == userName :
                test.log(" Given Login name is exists ")
                
                if object.exists(userLastNameInputId):
                    lastNameText= __getTextFromTextBoxEditUser(userLastNameInputId)
                    snooze(.5)
                    if str(lastNameText) == lastName :
                        test.log(" Given Last name is exists ")
                        
                        if object.exists(userFirstNameInputId):
                            firstNameText= __getTextFromTextBoxEditUser(userFirstNameInputId)
                            snooze(.5)
                            if str(firstNameText) == firstName :
                                test.log(" Given first name is exists ")
                                status = True
        else:
            test.fail(" Not able to verify Edit user screen values ")
            
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Method to edit user details for Login Last Name First Name in Edit user screen
def editUserValuesInEditUserScreen(userName, lastName, firstName,Role):
    try:
        count=0 
        snooze(1)
        if waitForObject(userLoginNameInputId):
            if( __setTextBoxEmptyInEditUser(userLoginNameInputId)):
                snooze(.5)
                setFocusTextBox(userLoginNameInputId)
                type(mainWindow, userName)
                count=count+1
                
        if object.exists(userLastNameInputId):
            if( __setTextBoxEmptyInEditUser(userLastNameInputId)):
                snooze(.5)
                setFocusTextBox(userLastNameInputId)
                type(mainWindow, lastName)
                count=count+1    
        if object.exists(userFirstNameInputId):
            if( __setTextBoxEmptyInEditUser(userFirstNameInputId)):
                snooze(.5)
                setFocusTextBox(userFirstNameInputId)
                type(mainWindow, firstName)
                count=count+1
        if selectComboBoxItem(waitForObject(roleInputId),Role):
                count+=1
        if object.exists(hideKeyBackground):
                mouseClick(hideKeyBackground)
                test.log(" Successfully edited user details in Edit user screen ")
        else:
            test.fail(" Fail to edit user details in Edit user screen  ")
            
        return True if count==4 else False
                           
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Method to verify discard changes warning pop up  
def verifyDiscardChangesWarningInEditUserScreen():
    try:
        status = False
        snooze(1)
        if (object.exists(evaluationScreenwarningMessageId)):
            warningObj = waitForObject(evaluationScreenwarningMessageId)
            warningText = warningObj.text
            
            if ("Are you sure want to discard the changes?" in str(warningText)):              
                if object.exists(confirmButtonId):
                    test.log(" Successfully verified 'Discard the changes' warning pop up ")
                    status = True                    
                
                else:
                    test.fail(" Fail to verify 'discard the changes' warning pop up")     
        else:
            test.log(" 'Discard the changes' warning message is not displayed  ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))  

# Method to click on Accept button on Discard changes warning pop up in Edit user screen  
def clickOnAcceptDiscardChangesInEditUserScreen():
    try:
        status = False
        snooze(1)
        if (waitForObject(confirmButtonId)):
            mouseClick(confirmButtonId)     
            snooze(1)                
            if ( object.exists(addUserButtonId)):
                test.log(" Successfully clicked on Accept button ")
                status = True
   
            else:
                test.log(" Fail to click on Accept button ")
                
        else:
            test.log(" Fail to click on Accept button ")
        
        if status:
            return True
        else:
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e)) 

# Method to click on cancel button on Discard changes warning pop up in Edit user screen  
def clickOnCancelDiscardChangesInEditUserScreen():
    try:
        status = False
        snooze(1)
        if (waitForObject(cancelButtonId)):
            mouseClick(cancelButtonId)     
            snooze(1)                
            if ( object.exists(cancelButtonId)==False):
                test.log(" Successfully clicked on cancel button ")
                status = True
   
            else:
                test.log(" Fail to click on cancel button ")
                
        else:
            test.log(" Fail to click on cancel button ")
        
        if status:
            return True
        else:
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Method to click on Change password icon in edit user screen  
def clickOnChangePasswordInEditUserScreen():
    try:
        status = False
        snooze(1)
        if (waitForObject(changePasswordButtonId)):
            mouseClick(changePasswordButtonId)
                       
            if (waitForObject(oldPasswordInputId)):
                test.log(" Successfully clicked on Change password button ")
                status = True
   
            else:
                test.log(" Fail to click on Change password button ")
                
        else:
            test.log(" Fail to click on Change password button ")
        
        if status:
            return True
        else:
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e)) 

# Method to verify 'show password' options in edit user screens   
def verifyShowPasswordButtonsInEditUserScreen():
    try:
        status = False
        snooze(.5)
        if (waitForObject(showOldPasswordButton)):
            if (object.exists(showPasswordButton)):
                if (object.exists(showConfirmPasswordButton)):
                    status = True   
                    test.log(" Successfully verified 'show password' options in 'Edit user' screen ")
        else: 
            test.fail(" Fail to verify 'show password' options in 'Edit user' screen ")          
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
        
# Method to enter values for 'change password' in edit user screen 
def changePasswordInEditUserScreen(currentPass, newPass, confirmPass):
    try:
        status = False 
        snooze(1)

        if waitForObject(oldPasswordInputId):
            setFocusTextBox(oldPasswordInputId)
            type(mainWindow, currentPass)
            if waitForObject(passwordInputId):
                setFocusTextBox(passwordInputId)
                type(mainWindow, newPass)
                if waitForObject(confirmPasswordInputId):
                    setFocusTextBox(confirmPasswordInputId)
                    type(mainWindow, confirmPass)
                    status = True
        if object.exists(hideKeyBackground):
                mouseClick(hideKeyBackground)
          
        else:
            test.fail(" Entered Change password values in edit user screen ")
            
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Method to enter password on delete user confirmation pop up 
def enterPasswordAndConfirmDeleteUserPopup(password):
    try:
        status = False 
        snooze(1)
        if waitForObject(confirmPasswordTextInputId):
            setFocusTextBox(confirmPasswordTextInputId)
            type(mainWindow, password)
                
            if object.exists(confirmButtonId):
                mouseClick(confirmButtonId)
                status = True
                test.log(" Successfully entered password and confirmed ")
        else:
            test.fail(" Fail to enter password details in delete confirm pop up  ")
            
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))

# Method to verify warning pop up 'incorrect password entered' on user deletion 
def verifyIncorrectPasswordWarningInDeleteUserPopup():
    try:
        status = False
        snooze(1)
        if (object.exists(evaluationScreenwarningMessageId)):
            warningObj = waitForObject(evaluationScreenwarningMessageId)
            warningText = warningObj.text
            
            if ("Please enter the correct password" in str(warningText)):              
                if object.exists(okButtonId):
                    test.log(" Successfully verified 'Please enter the correct password' warning ")
                    status = True                                   
                else:
                    test.fail(" Fail to verify 'Please enter the correct password' warning")            
        else:
            test.log(" 'Please enter the correct password' message is not displayed  ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e)) 


# Method to click on 'Ok' in 'Incorrect password entered' warning  
def acceptIncorrectPasswordEnteredInUserDeletionWarning():
    try:
        status = False
        snooze(1)
        if (waitForObject(okButtonId)):
            mouseClick(okButtonId)     
            snooze(1)                
            if ( object.exists(addUserButtonId)):
                test.log(" Successfully clicked on accept button ")
                status = True  
            else:
                test.log(" Fail to click on accept button ")                
        else:
            test.log(" Fail to click on accept button ")
        
        if status:
            return True
        else:
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Method to verify login screen is displayed or not 
def verifyLoginScreenDisplayedOrNot():
    try:
        status = False
        snooze(1)                     
        if (waitForObject(loginNameEntryFieldId)):
            test.log(" Login screen is displayed ")
            status = True  
        else:
            test.log(" Fail to verify Login screen ")               
        
        if status:
            return True
        else:
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e))

# Method to click on save user button 
def clickOnSaveNewuserInNewuserScreen():
    try:
        status = False
        snooze(1)
        if (waitForObject(saveUserButtonId)):
            mouseClick(waitForObject(saveUserButtonId))
            status = True           
        else:
            test.log(" Fail to save new user in new users screen ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
  
  
warningMessageId={"container": mainWindow, "text": "Confirmation password is not matching, Please enter again", "type": "Label", "unnamed": 1, "visible": True}
        
# Method to verify warning pop up 'password length 8 characters and password miss match
def verifyPasswordLengthWarningInNewUserScreen():
    try:
        status = False
        snooze(1)
        if (object.exists(PassworderrorPopupItemId)):
            warningObj = waitForObject(PassworderrorPopupItemId)
            warningText = warningObj.text
            
            if ("The password length shall be atleast 8 characters " in str(warningText)):              
                if object.exists(okButtonId):
                    test.log(" Successfully verified 'password length' warning ")
                    status = True                                   
                else:
                    test.fail(" Fail to verify 'password length' warning")            
        else:
            test.log(" 'password length' message is not displayed  ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e)) 
        
        
        
def verifyPasswordmisMatchWarningInNewUserScreen():
    try:
        status = False
        snooze(1)
        if (object.exists(warningMessageId)):
            warningObj = waitForObject(warningMessageId)
            warningText = warningObj.text
            
            if ("Confirmation password is not matching, Please enter again" in str(warningText)):              
                if object.exists(okButtonId):
                    test.log(" Successfully verified 'password length' warning ")
                    status = True                                   
                else:
                    test.fail(" Fail to verify 'password length' warning")            
        else:
            test.log(" 'password length' message is not displayed  ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))         
        
        
        
        
# Method to accept okButton in warning pop up   
def clickOnOkInWarningPopUp():
    try:
        status = False
        snooze(1)
        if (waitForObject(okButtonId)):
            mouseClick(okButtonId)     
            snooze(1)                
            if ( object.exists(okButtonId)==False):
                test.log(" Successfully clicked on cancel button ")
                status = True
   
            else:
                test.log(" Fail to click on cancel button ")
                
        else:
            test.log(" Fail to click on cancel button ")
        
        if status:
            return True
        else:
            return False
        
    except Exception as e:
        test.fail("Exception" +str(e))

# Method to enter password text
def enterPasswordText(obj, passText):
    try:
        status = False 
        snooze(1)
        if waitForObject(obj):
            setFocusTextBox(obj)
            type(mainWindow, passText)
            status = True
        else:
            test.fail(" New user screen is not displayed ")
            
        if status:
            return True
        else:
            return False
                           
    except Exception as e:
        test.fail("Exception" +str(e))

# Method to clear new password text in new user screen  
def clearNewPasswordFieldInNewUserScreen():
    try:
        status = False
        snooze(1)

        if waitForObject(passwordInputId):
            passObj = waitForObject(passwordInputId)
            setFocusTextBox(passwordInputId)
            passObj.input = ""
            status = True
        else:
            test.fail(" Fail to clear new password field ")
    
        if status:
            return True
        else:
            return False   
          
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Method to clear confirm password text in new user screen  
def clearConfirmPasswordFieldInNewUserScreen():
    try:
        status = False
        snooze(1)

        if waitForObject(confirmPasswordInputId):
            passObj = waitForObject(confirmPasswordInputId)
            setFocusTextBox(confirmPasswordInputId)
            passObj.input = ""
            status = True
        else:
            test.fail(" Fail to clear confirm password field ")
    
        if status:
            return True
        else:
            return False   
          
    except Exception as e:
        test.fail("Exception" +str(e))
        
# Method to verify warning pop up 'password length 8 characters 
def verifyWarningMessage(warningMessage):
    try:
        status = False
        snooze(1)
        if (object.exists(evaluationScreenwarningMessageId)):
            warningObj = waitForObject(evaluationScreenwarningMessageId)
            warningText = warningObj.text
            
            if (warningMessage in str(warningText)):              
                if object.exists(okButtonId):
                    test.log(" Successfully verified warning text ")
                    status = True                                   
                else:
                    test.fail(" Fail to verify warning text ")            
        else:
            test.log(" 'warning pop up' is not displayed  ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e)) 

# Method to verify tick marks displayed adjacent to password and confirm password text boxes
def verifyTickMarksInNewUserScreen():
    try:
        status = False
        snooze(.5)
        if (waitForObject(passwordMatchIconId)):
            if (object.exists(confirmpasswordMatchIconId)):
                status = True   
                test.log(" Successfully verified tick marks in new user screen ")
        else: 
            test.fail(" Fail to verify tick marks in new user screen ")          
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
        
        

#Method to navigate to roles tab from user list screen

def NavigateToAddRolestabfromUserList():
    try:
        status=False
        snooze(.5)
        if (waitForObject(rolesTabButtonId)):
            if (object.exists(rolesTabButtonId)):
                mouseClick(rolesTabButtonId)
                test.log('Clicked Add button in user list screen')
        if object.exists(rolesNewViewButtonId):
            test.log('Successfully navigated to the add roles tab')
            status=True
            
        return True if status else False
    
    except Exception as e:
        test.fail("Exception"+ str(e))  
            
# Common method to verify the default roles

def DefaultrolesInuserScreen():
    try:
        mandatoryItemsList = ['Administrative Nurse', 'Medical technician', 'Assistant Physician', 'Chief Physician', 'Admin', 'BTL support', 'Physician', 'Nurse']
    
        parent=findObject(rolesListviewId)
        child1=object.children(parent)
        objFlick=object.children(child1[1])
        objItem=object.children(objFlick[1])
        objrol=object.children(objItem[0])
        rollist=object.children(objrol[0])
        objColumn=object.children(rollist[0])
    
        listItems = []
        
        for item in objColumn:
            childColumn = object.children(item)
            if len(childColumn)>0:
                rolbutton=object.children(childColumn[0])
                Row1=object.children(rolbutton[1])
                if len(Row1) >= 1:
                    listItems.append(str(Row1[1].text).strip())
                elif len(Row1) < 1:
                        listItems.append(str(item.text).strip())        
            
        
        if len(listItems) >= len(mandatoryItemsList):
            for val in mandatoryItemsList:
                if val in listItems:
                    pass
                else:
                    test.fail("Roles tab not contains all the roles")
                    return False
                
        test.log("Roles tab contains all the default roles")
        return True
    
    except Exception as e:
        test.fail("Exception"+ str(e)) 
        
#Collecting default roles and adding into list -Lanaguage validation
def DefaultrolesInuserScreenandAddintolist():
    try:
        status='fail'
        parent=findObject(rolesListviewId)
        child1=object.children(parent)
        objFlick=object.children(child1[1])
        objItem=object.children(objFlick[1])
        objrol=object.children(objItem[0])
        rollist=object.children(objrol[0])
        objColumn=object.children(rollist[0])
        
        for item in objColumn:
            childColumn = object.children(item)
            if len(childColumn)>0:
                rolbutton=object.children(childColumn[0])
                Row1=object.children(rolbutton[1])
                if len(Row1) >= 1:
                    list1.append(str(Row1[1].text).strip())
                    status='pass'
                elif len(Row1) < 1:
                        list1.append(str(item.text).strip())
                        'pass'
                        
        return True if status==True else False
    
    except Exception as e:
        test.fail("Exception"+ str(e)) 
        
        
        
        
        
        
        
    
        
def SelectTheRoleinRolesscreen(SelectRole):
    try:
        status=False
        #mandatoryItemsList = ['Administrative Nurse', 'Medical technician', 'Assistant Physician', 'Chief Physician', 'Admin', 'BTL support', 'Physician', 'Nurse']
        parent=findObject(rolesListviewId)
        child1=object.children(parent)
        objFlick=object.children(child1[1])
        objItem=object.children(objFlick[1])
        objrol=object.children(objItem[0])
        rollist=object.children(objrol[0])
        objColumn=object.children(rollist[0])
        
        for item in objColumn:
            childColumn = object.children(item)
            if len(childColumn)>0:
                rolbutton=object.children(childColumn[0])
                Row1=object.children(rolbutton[1])
                if len(Row1) >= 1:
                    if str(Row1[1].text)==SelectRole:
                        mouseClick(childColumn[0])
                        test.log('Successfully selected role '+SelectRole)
                        status=True
                    else:
                        continue
        return True if status==True else False
    
    except Exception as e:
        test.fail("Exception"+ str(e)) 
        


        
        
#Method to click on edit button and verify the click on perticular role

def Clickonroleeditbutton():
    try:
        status='Fail'
        snooze(1)
        if object.exists(editRoleButtonId):
            mouseClick(waitForObject(editRoleButtonId))
            test.log('Clicked on edit button button')
            snooze(1)
        if object.exists(roleNameInputId):
            status='pass'
                
        return True if status=='pass' else False
                           
    except Exception as e:
        test.fail("Exception" +str(e)) 
        
#Verify the role text field to make sure that clicked right role
def verifyclickedRoleInRoleEditscreen(SelectRole):
    try:
        status='Fail'
        snooze(1)
        if object.exists(roleNameInputId):
            loginText= __getTextFromTextBoxEditUser(roleNameInputId)
            if str(loginText) == SelectRole:    
                status='pass'        
                test.log("Clicked the correct user : "+SelectRole)
                
        return True if status=='pass' else False
                           
    except Exception as e:
        test.fail("Exception" +str(e)) 
        
        
#Method to verify Default role- Privileges check---ON ID

def VerifythePrivillagesofRolesON(list,n):
    try:
        count=0
        for x in list:
            if object.exists(x):
                parent=findObject(x)
                child=object.children(parent)
                SwithID=object.children(child[1])
                row0=object.children(SwithID[0])
                if row0[0].checked:
                    test.log('Current object is ON')
                    count=count+1
                    
        return True if count==n else False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
        
#Method to verify Default role- Privileges check---OFF checked

def VerifythePrivillagesofRolesOFF(list1,n1):
    try:
        count=0
        for x in list1:
            if object.exists(x):
                parent=findObject(x)
                child=object.children(parent)
                SwithID=object.children(child[1])
                row0=object.children(SwithID[0])
                if row0[1].checked:
                    test.log('Current object is OFF')
                    count=count+1
                    
        return True if count==n1 else False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
        
        
#Method  to navigate to user list screen from roles tab/roles edit screen
def NavigateToUsersTabfromRolesTab():
    try:
        status='Fail'
        snooze(1)
        if object.exists(usersTabButtonId):
            mouseClick(waitForObject(usersTabButtonId))
            test.log('Clicked on users tab button')
            snooze(1)
        if object.exists(addUserButtonId):
            status='pass'
                
        return True if status=='pass' else False
                           
    except Exception as e:
        test.fail("Exception" +str(e)) 
        
#Functions to navigate to add new role screen

def NavigateToNewUseraddScreen():
    try:
        status='Fail'
        snooze(1)
        if object.exists(rolesNewViewButtonId):
            mouseClick(waitForObject(rolesNewViewButtonId))
            test.log('Clicked on new add role button')
            snooze(1)
        if object.exists(roleNameInputId):
            test.log('Sucessfully navigated to add new role screen')
            status='pass'
                
        return True if status=='pass' else False
                           
    except Exception as e:
        test.fail("Exception" +str(e)) 
        
#Function to create a new role in add new role screen
def CreateNewRoles(RoleName):
    try:
        status='Fail'
        snooze(1)
        if object.exists(roleNameInputId):
            setFocusTextBox(roleNameInputId)
            type(mainWindow, RoleName)
            snooze(1)
            if object.exists(hideKeyBackground):
                mouseClick(hideKeyBackground)
            if object.exists(saveUserButtonIdRles):
                mouseClick(saveUserButtonIdRles)
                snooze(3)
                test.log('Successfully navigated to add new role screen')
        if object.exists(rolesListviewId):
            test.log('Successfully navigated to roles list')
            status='pass'
                
        return True if status=='pass' else False
                           
    except Exception as e:
        test.fail("Exception" +str(e)) 
    
#Providing the all privilege to the user
def ProvidingTheuserRolesPrevillages(list,n):
    try:
        count=0
        for x in list:
            if object.exists(x):
                parent=findObject(x)
                child=object.children(parent)
                SwithID=object.children(child[1])
                row0=object.children(SwithID[0])
                mouseClick(row0[0])
                test.log('Current object turned ON')
                count=count+1
            else:
                test.log('Object Not found')
        if object.exists(saveUserButtonIdRles):
            mouseClick(saveUserButtonIdRles)
                    
        return True if count==n else False

    except Exception as e:
        test.fail("Exception" +str(e)) 


roleinfoId={"container": mainWindow, "id": "roleinfoId", "type": "RolesInfoView", "unnamed": 1, "visible": True}

# Common method to verify the default roles

def VerifytheOptioninRolesTab():
    try:
        mandatoryItemsList = ["Actions with patients","Actions with examinations","Actions with settings and user management"]
    
        parent=findObject(roleinfoId)
        child1=object.children(parent)
        objFlick=object.children(child1[1])
        objItem=object.children(objFlick[0])
        objrol=object.children(objItem[0])
        rollist=object.children(objrol[1])
    
        listItems = []
        
        for item in rollist:
            childColumn = object.children(item)
            if len(childColumn)>0:
                if len(childColumn) >= 1:
                    listItems.append(str(childColumn[0].text).strip())
                elif len(Row1) < 1:
                    continue
        
        if len(listItems) >= len(mandatoryItemsList):
            for val in mandatoryItemsList:
                if val in listItems:
                    pass
                else:
                    test.fail("Roles tab not contains all the roles")
                    return False
                
        test.log("Roles tab contains all the default roles")
        return True
    
    except Exception as e:
        test.fail("Exception"+ str(e))
        
        
#Function to create a new role in add new role screen
def CreateNewRolesandChaningthePrillagesofthatrole(RoleName):
    try:
        status='Fail'
        snooze(1)
        if object.exists(roleNameInputId):
            setFocusTextBox(roleNameInputId)
            type(mainWindow, RoleName)
            snooze(1)
            if object.exists(hideKeyBackground):
                mouseClick(hideKeyBackground)
            if object.exists(saveUserButtonIdRles):
                mouseClick(saveUserButtonIdRles)
                test.log('Successfully navigated to add new role screen')
                snooze(3)
        if object.exists(rolesListviewId):
            test.log('Successfully navigated to roles list')
            status='pass'
                
        return True if status=='pass' else False
                           
    except Exception as e:
        test.fail("Exception" +str(e)) 


#Functions to turn on all the privileges while creating role 
def TurningOnAllthePrivillagesofRoles(list,n):
    try:
        count=0
        for x in list:
            if object.exists(x):
                parent=findObject(x)
                child=object.children(parent)
                SwithID=object.children(child[1])
                row0=object.children(SwithID[0])
                if not row0[0].checked:
                    mouseClick(row0[0])
                    test.log('Current object is turned ON')
                    count=count+1
                else:
                    test.log('Current object is turned ON')
                    count=count+1
            test.log('All privileges are turned ON')  
        return True if count==n else False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
  
  
def getTotalExaminationCountForPatient():
    try:
        count = 0
          
        if (object.exists(examinationListView)):
            
            examListView = waitForObject(examinationListView)
            count = examListView.count
            test.log("Total number of examinations recorded for the patient is '" + str(count) + "'")
                        
        else:
            test.log("Total number of examinations recorded for the patient is '" + str(count) + "'")
        
        return count
  
    except Exception as e:
        test.fail("Exception"+ str(e))
        
Rolescountview={"container": mainWindow, "id": "roleListViewId", "type": "ListView", "unnamed": 1, "visible": True}

def VerifytheMaxTotalusersinrolesTab(InputRoleName):
    try:
        status='Fail'
        global Totalusers
        Totalusers=0
        if (object.exists(Rolescountview)):
            obj=waitForObject(Rolescountview)
            Totalusers=obj.count
        while Totalusers<50:
            CreatemaxrolesandVeriytheuser(Totalusers,InputRoleName)
            if (object.exists(Rolescountview)):
                obj=waitForObject(Rolescountview)
                Totalusers=obj.count
                test.log("Total number of roles created '" + str(Totalusers) + "'")
        else:
            if verifytheWarningMsgaboutlowWarning(Totalusers,InputRoleName):
                status='pass'
                   
        return True if status=='pass' else False
    
    except Exception as e:
        test.fail("Exception"+ str(e))  
            
def CreatemaxrolesandVeriytheuser(Totalusers,InputRoleName):
    try:
        status='fail'
        status1=NavigateToNewUseraddScreen()
        snooze(1)
        InputRoleName=InputRoleName+str(Totalusers)
        status2=CreateNewRolesandChaningthePrillagesofthatrole(InputRoleName)
        snooze(1)
        status3=SelectTheRoleinRolesscreen(InputRoleName)
        snooze(1)
        
        if status1 and status2 and status3:
            test.log('Created new role '+InputRoleName)
            status='pass'
        
        return True if status=='pass' else False 
            
    except Exception as e:
        test.fail("Exception"+ str(e)) 
        
        
def SetTextinroleedittab(SelectRole):
    try:
        status='Fail'
        snooze(1)
        if object.exists(roleNameInputId):
            setFocusTextBox(roleNameInputId)
            type(mainWindow, SelectRole)
            snooze(1)
            loginText= __getTextFromTextBoxEditUser(roleNameInputId)
            if str(loginText) == SelectRole:    
                status='pass'        
                test.log("Modified role name displayed in role input tab : "+SelectRole)
                
        return True if status=='pass' else False
                           
    except Exception as e:
        test.fail("Exception" +str(e)) 
            
            
            
def verifytheWarningMsgaboutlowWarning(Totalusers,InputRoleName):
    try:
        status='fail'
        status1=NavigateToNewUseraddScreen()
        snooze(1)
        InputRoleName=InputRoleName+str(Totalusers)
        status2=CreateNewRolesandChaningthePrillagesofthatrole(InputRoleName)
        snooze(1)
        status3=verifymaxroleswarningmessageinnRolesscreen()
        snooze(1)
        
        if status1 and status2 and status3:
            test.log('Verified the warning message when created 51th role'+InputRoleName)
            status='pass'
        
        return True if status=='pass' else False 
            
    except Exception as e:
        test.fail("Exception"+ str(e))          
            
RolemaxwarningMessageId={"container": mainWindow, "text": "Failed to add role, Max role limit reached, please delete a role to continue", "type": "Label", "unnamed": 1, "visible": True}          
#Function to verify max roles warning message
def verifymaxroleswarningmessageinnRolesscreen():
    try:
        status = False
        snooze(1)
        if (object.exists(RolemaxwarningMessageId)):
            warningObj = waitForObject(RolemaxwarningMessageId)
            warningText = warningObj.text
            
            if ("Failed to add role, Max role limit reached, please delete a role to continue" in str(warningText)):              
                if object.exists(okButtonId):
                    mouseClick(okButtonId)
                    test.log(" Successfully verified  max role warning ")
                    status = True                                   
                else:
                    test.fail(" Fail to verify max role warning")            
        else:
            test.log("max role message is not displayed  ")
        
        if status:
            return True
        else:
            return False
            
    except Exception as e:
        test.fail("Exception"+ str(e)) 
 

        
#Function to check the warning message (about delete role which is not associated with any user)
def RoledeletionWarningPopUp():
    try:
        count =0 
        snooze(1)
        if waitForObject(deleteRoleButtonId):
            mouseClick(waitForObject(deleteRoleButtonId))
            snooze(2)
            if (object.exists(deleteWarningItemId)):
                parent=findObject(deleteWarningItemId)
                child=object.children(parent)
                coln_0=object.children(child[0])
                item2=object.children(coln_0[2])
                Row_0=object.children(item2[0])
                warningText = Row_0[2].text
                if ("Delete role?" in str(warningText)):
                    if object.exists(confirmButtonId) and object.exists(cancelButtonId):
                        count=1
                        test.log("successfully verified warning message and accept and reject button is available in warning message")
                else:
                    test.log('Delete role is not displayed')            
            else:
                test.log("Warning message ID is not displayed")
        else:
            test.log('Delete button not found')
        
        return True if count==1 else False
            
    except Exception as e:
        test.fail("Exception"+ str(e))           

def AccepttheDeleteRolewarningMessage(obj):
    try:
        status='Fail'
        if (object.exists(obj)):
            mouseClick(waitForObject(obj))
            snooze(1)
            status='Pass'
            
        
        return True if status=='Pass' else False
    
    except Exception as e:
        test.fail("Exception"+ str(e))  
  
      
#Function to check the warning message (About role which is associated with any other role can't be deleted)/autologin
def RoledeletionWarningPopUpAssociatedRole(text):
    try:
        count =0 
        snooze(1)
        if waitForObject(confirmButtonId):
            mouseClick(waitForObject(confirmButtonId))
            snooze(2)
            if (object.exists(apcErrorPopupItemId)):
                parent=findObject(apcErrorPopupItemId)
                child=object.children(parent)
                coln_0=object.children(child[0])
                item2=object.children(coln_0[2])
                Row_0=object.children(item2[0])
                warningText = Row_0[2].text
                if (str(text) in str(warningText)):
                    if object.exists(okButtonId):
                        count=1
                        test.log("successfully verified warning message and accept button is available in warning message")
                else:
                    test.log('Waring text message is not displayed role is not displayed')            
            else:
                test.log("Warning message ID is not displayed")
        else:
            test.log('Delete button not found')
        
        return True if count==1 else False
            
    except Exception as e:
        test.fail("Exception"+ str(e))
        
        
def autoLoginEnablingwarningmessage(text):
    try:
        count =0 
        snooze(1)
        if waitForObject(AutologinONbutton):
            mouseClick(waitForObject(AutologinONbutton))
            snooze(2)
            if (object.exists(confirmPopupItemIdAutologin)):
                parent=findObject(confirmPopupItemIdAutologin)
                child=object.children(parent)
                coln_0=object.children(child[0])
                item2=object.children(coln_0[2])
                Row_0=object.children(item2[0])
                warningText = Row_0[2].text
                if (str(text) in str(warningText)):
                    if object.exists((confirmButtonId) and (cancelButtonId)):
                        count=1
                        test.log("successfully verified warning message and accept button is available in warning message")
                else:
                    test.log('Waring text message is not displayed role is not displayed')            
            else:
                test.log("Warning message ID is not displayed")
        else:
            test.log('Delete button not found')
        
        return True if count==1 else False
            
    except Exception as e:
        test.fail("Exception"+ str(e))        
        
        
                
#Function to save the modified roles
def savetherolechanges():
    try:
        if object.exists(saveUserButtonIdRles):
            mouseClick(saveUserButtonIdRles)
            test.log('Successfully navigated to add new role screen')
        if object.exists(rolesListviewId):
            test.log('Successfully navigated to roles list')
            status='pass'
                
        return True if status=='pass' else False
                           
    except Exception as e:
        test.fail("Exception" +str(e)) 
                
                
#Function to verify sort by user name in user management screen
def verifySortingUserListScreen(obj,sortType):
    try:  
        if object.exists(obj):
            
            sortButtonState =str(waitForObject(obj).state)
            
            if sortButtonState == "" and sortType == "ascending":
                mouseClick(waitForObject(obj)) 
                if testAscendingSortInUserListScreen(obj):
                    return True
                else:
                    return False

            elif sortType == "ascending" and sortButtonState == "ascendingSort":
                if testAscendingSortInUserListScreen(obj):
                    return True
                else:
                    return False
                
            elif sortType == "ascending" and sortButtonState == "descendingSort":
                mouseClick(waitForObject(obj))
                if testAscendingSortInUserListScreen(obj):
                    return True
                else:
                    return False   
         
            elif sortType == "descending" and sortButtonState == "":
                mouseClick(waitForObject(obj))
                snooze(2)
                mouseClick(waitForObject(obj))
                if testDescendingSortInUserListScreen(obj):
                    return True
                else:
                    return False   
                            
            elif sortType == "descending" and sortButtonState == "descendingSort":
                if testDescendingSortInUserListScreen(obj):
                    return True
                else:
                    return False
                
            elif sortType == "descending" and sortButtonState == "ascendingSort":
                mouseClick(waitForObject(obj))
                if testDescendingSortInUserListScreen(obj):
                    return True
                else:
                    return False 
     
    except Exception as e:
        test.fail("Exception"+ str(e))

#function to sort in ascending order by using patient name in patient list screen
def testAscendingSortInUserListScreen(obj):
    try:
        result=False
        
        patientList=scrollListInPatientListScreenP(obj)
        
        newList = []
        newList = patientList[:]
          
        newList.sort(key = lambda x: x[0])
        
        if newList == patientList:
            test.passes("Sorted in ascending order by using patient name in patient list screen")
            result=True
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
        test.fail("Exception" +str(e))

#function to sort in descending order by using patient name in patient list screen
def testDescendingSortInUserListScreen(obj):
    try:
        
        result=False
        
        patientList=scrollListInPatientListScreenP(obj)
        
        newList = []
        newList = patientList[:]
        newList.sort(key = lambda x: x[0],reverse=True)
    
        if newList == patientList:
            result=True
            test.passes("Sorted in descending order by using patient name in patient list screen")
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
        test.fail("Exception" +str(e))


        
#Function to scroll the list and get the patient details in patient list screen
def scrollListInPatientListScreenP(obj):
    
    patientList=[]
    y_list = []
    i = 0.0
    
    #for i in range(0, 130):
    while i <= 1.0  :         
        listChild=[]        
        
        listChild = waitForObject(userListViewId)
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
                    item1=object.children(row[1])  
                    Row0=object.children(item1[0])
                    if obj==nameSortButtonId:
                        name = (str(Row0[1].text).lower()).replace(",","").replace(" ", "")
                        patientData.append(name)
                    elif obj==loginSortButtonId:
                        login= str(Row0[3].text).lower()
                        patientData.append(login)
                    elif obj==roleSortButtonId:
                        role=str(Row0[5].text).lower()
                        patientData.append(role)                  
                    
                
                    patientList.append(patientData)
                    
                    y_list.append(j.y) 
  
        flick(waitForObject(userListViewId), 0, 415)
        i = item[1].position
        
    return patientList

