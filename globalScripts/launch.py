def launchApplication():
    appContext=attachToApplication("ui")
    if appContext.isRunning:
        test.log("Application launch", "ECG2.0 Launched successfully")
        return True
    else:
        test.log("Application not launched")
        return False
    
    
