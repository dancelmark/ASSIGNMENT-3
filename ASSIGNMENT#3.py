#Saving and Writing Files

#Example 1
import numpy as np

def savetxt(filename, data):
    np.savetxt(filename, data)

Array1 = np.array([[8, 5, 7], [9, 3, 1], [7, 4, 1]])
savetxt('Array1', Array1)

#Example 2
import numpy as np

def savebinary(filename, data):
    np.save(filename, data)

Array2 = np.array([[5, 9, 8], [4, 3, 6], [8, 3, 5]])
savebinary('Array2', Array2)

#Example 3
import numpy as np

def savecompressed(filename, kombat):
    np.savecompressed(filename, kombat)

array1 = np.array([4, 2, 3])
array2 = np.array([7, 5, 9])
savecompressed('array.npz', array1=array1, array2=array2)

##LAODING DATA

#Example 1
import numpy as np

def loadtext(filename):
    return np.loadtxt(filename)

print("EXAMPLE 1")
loadtext = loadtext('data.txt')
print(loadtext)
print()
print()

#Example 2
import numpy as np

def loadbinary(filename):
    return np.load(filename)

print("EXAMPLE 2")
loadbinary = loadbinary('data.npy')
print(loadbinary)

print()
print()

#Example 3
import numpy as np

def loadcompressed(filename):
    npz_file = np.load(filename)
    return npz_file['data1'], npz_file['data2']

print("EXAMPLE 3")
loaddata1, loaded_data2 = load_from_compressed('data.npz')
print("Data 1:", loaddata1)
print("Data 2:", loaddata2)

print()
print()
