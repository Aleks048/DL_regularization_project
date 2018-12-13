from generate_dataset import *

# script to generate a bunch of datasets

num_to_generate = 5000

variances = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1]

for v in variances:
	path = "D:/datasets/csi5138-imgs/var{}".format(v)
	train_path = path + "/train"
	test_path = path + "/test"
	generate_dataset(N=num_to_generate, sigma=v, mu=0, datapath=train_path)
	generate_dataset(N=num_to_generate, sigma=v, mu=0, datapath=test_path)
	
