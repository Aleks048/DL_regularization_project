import importlib.util
import os.path

#importing convNet
pathToConvNet = str(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))+"\\convNet\\convNet.py")
#this is a path to the DataSet folder that is ignored but you should create one))
pathToGenDataset =  str(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))+"\\img-generator\\generate_dataset.py"
pathToSaveDataset =  str(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))+"\\DataSet\\"


spec = importlib.util.spec_from_file_location("convNet",pathToConvNet)
convNet = importlib.util.module_from_spec(spec)
spec.loader.exec_module(convNet)

#spec = importlib.util.spec_from_file_location("generate_dataset",pathToGenDataset)
#dataGen = importlib.util.module_from_spec(spec)
#spec.loader.exec_module(dataGen)

#generate_dataset()
#convNet.LeNet()


print()