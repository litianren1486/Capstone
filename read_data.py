import numpy as np

'''
Given path to .npz file returns dataset and labels as numpy arrays
'''
def read_data(path):
	npzfile = np.load(path, allow_pickle=True)
	data = npzfile["data"]
	labels = npzfile["labels"]
	npzfile.close()

	return data, labels

path= r"C:\Users\LiTianren\Desktop\COMP5703\Capstone_dataset\capstone_data\AWF.npz"
AWF=read_data(path)
AWF






