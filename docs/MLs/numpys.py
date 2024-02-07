py_list = [[1,2]
           ,[3,4]
           ,[5,6]]  # list
import numpy as np
np_array = np.array([[7, 8]
                    ,[9,10]
                    ,[11,12]])  # 행렬 = array

np_array.sum(axis=0) # axis = 0 row 단위
# array([27, 30])
np_array.sum(axis=1) # axis = 1 column 단위
# array([15, 19, 23])

np.sum(np_array, axis=0)
# array([27, 30])
np.sum(np_array, axis=1)
# array([15, 19, 23])


# 구분 위한 타입확인
type(py_list)
# <class 'list'>
type(np_array)
# <class 'numpy.ndarray'>


# np에서는 리스트끼리 병합할 수 있음 - np.concatenate((data_1,data_2), axis=0 or 1)
np_array_second = np.array(py_list)
np.concatenate((np_array,np_array_second), axis=0)
# array([[ 7,  8],
#        [ 9, 10],
#        [11, 12],
#        [ 1,  2],
#        [ 3,  4],
#        [ 5,  6]])
np.concatenate((np_array,np_array_second), axis=1)
# array([[ 7,  8,  1,  2],
#        [ 9, 10,  3,  4],
#        [11, 12,  5,  6]])


pass