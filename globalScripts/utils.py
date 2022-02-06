
#################
#This is a Utility file where all external reources are been kept and used.


from ConfigParser import ConfigParser



def getProduct():
	productCode=__readConfigFile()
	return productCode
	



def __readConfigFile():

	con=ConfigParser()
	con.read("../../../configurations/config.ini")
	aut=con.get('product','aut')
	return aut
	
	





