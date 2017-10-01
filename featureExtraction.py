'''
feature 1 (avgTime):calculates average time between moves
feature 2 (avgSpeed):calculates a value similar to average speed of user moves
feature 3 (TimeSpent):calculates time duration user spends online
feature 4 (avgMoves):calculates avg number of by mouse movements per second  
'''
FileList=["session_0041905381","session_1060325796","session_3320405034",  "session_3826583375"  ,"session_6668463071","session_8961330453","session_9017095287"]

#FileList=["session_0041905381"]
import numpy as np

featureVector=[None] * 4


for fileName in FileList:

	data = np.genfromtxt("user7/"+fileName, dtype=None, delimiter=',')
	data=data[1:]
	rows=data.shape[0]
	avgSpeed=0


	for i in range (1,rows):
		timeT=data[i,0].astype(np.float)-data[i-1,0].astype(np.float)
		avgSpeed=avgSpeed+((np.linalg.norm([data[i,4].astype(np.float) - data[i-1,4].astype(np.float), data[i,5].astype(np.float) - data[i-1,5].astype(np.float)]))/(timeT*rows+1))
		#to avoid NaN, 1 is added in the denominator
               
	#For now only 4 features are used, more to be added.
 
	TimeSpent=data[rows-1,0].astype(np.float)-data[0,0].astype(np.float)
	avgMoves=(rows/TimeSpent)  
	avgTime= (TimeSpent/rows)
	features=np.array([avgTime,avgSpeed,TimeSpent,avgMoves])
	featureVector=np.column_stack((featureVector,features))
