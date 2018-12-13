import os
from myImage import *
from dataFeeder import *

#returns the datGenerators for the model
def getDataGenerators(imgDim,batch,numClasses,numOfChannels,shuffleInBatch,DataSetPath):
	#iterate over dataset and get all the paths and labels
	airplaneNum = 0
	dogNum = 1
	frogNum = 2
	personNum =3
	truckNum = 4
	
	myImages = []
	for subdir, dirs, files in os.walk("../DataSet"):
		for file in files:
			#print os.path.join(subdir, file)
			filepath = subdir + os.sep + file

			if filepath.endswith(".png"):
				if "airplane" in str(filepath):
					myImages.append(MyImage(filepath,airplaneNum))
				if "dog" in str(filepath):
					myImages.append(MyImage(filepath,dogNum))
				if "frog" in str(filepath):
					myImages.append(MyImage(filepath,frogNum))
				if "person" in str(filepath):
					myImages.append(MyImage(filepath,personNum))
				if "truck" in str(filepath):
					myImages.append(MyImage(filepath,truckNum))



	partition ={"train" : [],"test":[]}

	partition["train"] = [myImages[i].path for i in range(int(len(myImages)*0.8))]

	trainLabels = {myImages[i].path:myImages[i].classNum for i in range(int(len(myImages)*0.8))}

	partition["test"] = [myImages[i].path for i in range(int(len(myImages)*0.8),len(myImages))]
	testLabels = {myImages[i].path:myImages[i].classNum for i in range(int(len(myImages)*0.8),len(myImages))}

	params = {'dim': (imgDim[0],imgDim[1]),
				'batch_size': batch,
				'n_classes': numClasses,
				'n_channels': numOfChannels,
				'shuffle': shuffleInBatch}

	training_generator = DataGenerator(partition['train'], trainLabels, **params)         
	test_generator = DataGenerator(partition['test'], testLabels, **params)	
	return training_generator,test_generator