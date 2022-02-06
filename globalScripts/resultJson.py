import json

def resultToJson(testName,testSuiteName):
    testSteps={'line':1,'result':'log','type':'msg'}
    testCase={'name':testName,'type':'testcase','stop':''}
    testSuite={'name':testSuiteName,'type':'testSuite','stop':''}
    stepInfo=[]
    testCaseInfo=[]
    testSuiteInfo=[]
    
    
    stepInfo.append(testSteps)
    stepInfo.append(testSteps)
    resultDictionaryTests={'tests':stepInfo}
    
    
    resultDictionarySuite={}
    resultDictionarySuite.update(testCase)
    resultDictionarySuite.update(resultDictionaryTests)
    testCaseInfo.append(resultDictionarySuite)
    
    
    resD1={'test':testCaseInfo}
    
    
    resultDictionaryOverall={}
    resultDictionaryOverall.update(resD1)
    resultDictionaryOverall.update(testSuite)
    testSuiteInfo.append(resultDictionaryOverall)
    resultDictionaryOverall={'version':{'major':1,
            'minor':0},
            'tests':testSuiteInfo}
    
    
    
    with open('result.json','w') as outfile:
        json.dump(resultDictionaryOverall, outfile,sort_keys=True,indent=3)
        
        

    
    
    

    
    
    
    
    
    
    
    

    