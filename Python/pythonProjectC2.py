import pandas as pd

class A:
	def __init__(self , Path):
		self.__path = Path 
		self.__extension = self.__path.rsplit(".",1)[-1].lower()


    def readData(self):
    	if self.__extension == "csv":
    		self.__df = pd.read_csv(self.__path)
    	elif self.__extension == "excel":
    		self.__df = pd.read_csv(self.__path)
    	elif self.__extension == "json":
    		self.__df = pd.read_csv(self.__path)
    	else:
    		print("Unknown Extension")
    		
    # For choosing an encoding way 
    def __chooseEncoding4Col(self , column):
    		while True:
    			choose = "\nEnter One for Catigorical Encoding \nEnter Tow for One Hot Encoding"
    			try:
    				
    				if (0< int(choose) <= 2):
    					choose = int(choose)
    					
    					if choose == 1:
    						self.__DoEncoding(column , "Catigorical Encoding")
    						
    					elif choose == 2:
    						self.__DoEncoding(column , "One Hot Encoding")
    						
    				
    			except:
    				print("Please Enter a Number")
    				
    def __DoEncoding(self , column , encodingWay):
    		if encodingWay == "Catigorical Encoding":
				dict = {k:i for i,k in enumerate(df[column].unique())}
    

    def __VeiwColDiscription(self , column : pd.Serise) -> None:
    		choose = input(""" Enter as Below To Veiw
    		1 - First 5 Rows and Last 5 Rows
    		2 - Value Counts
    		3 - Unique Values""")
    			try:
    				
    				if (0< int(choose) <= 3):
    					choose = int(choose)
    					
    					if choose == 1:
    						print(column.head())
    						
    					elif choose == 2:
							print(column.value_counts())

    					elif choose == 3:
							print(column.unique())
    					
    				
    			except:
    				print("Please Enter a Number")			
		
    		
    		    		