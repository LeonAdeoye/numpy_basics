import numpy as np
# NumPy is a Python library used for working with arrays.


def slicing():
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    # Slicing includes the start index but exclude the end index.
    # Slice elements from index 2 to index 5 (not included).
    print(arr[2:5])
    # Slice elements from index 2 to the end.
    print(arr[2:])
    # Slice elements from beginning to index 5 (not included)
    print(arr[:5])
    # Creates a 2-D array containing two arrays with the values [1,2,3] and [4,5,6]
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr_2d)
    print(arr_2d.ndim)
    print(arr_2d[0])


def view_vs_copy():
    # The main difference between a copy and a view of an array is that the copy is a new array,
    # and the view is just a view of the original array.

    # The copy owns the data and any changes made to the copy will not affect original array,
    # and any changes made to the original array will not affect the copy.
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.copy()
    arr[0] = 42
    print(arr)
    print(x)
    # The view does not own the data and any changes made to the view will affect the original array,
    # and any changes made to the original array will affect the view.
    arr = np.array([1, 2])
    x = arr.view()
    arr[0] = 42
    x[1] = 43
    print(arr)
    for y in x:
        print(y)

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.concatenate((arr1, arr2))
    print(f'concatenated array: {arr}')
    # Find the indexes where the value is 4:
    print(f'Index when value = 4: {np.where(arr == 4)}')
    arr = np.array([3, 2, 0, 1])
    print(np.sort(arr))


if __name__ == '__main__':
    slicing()
    view_vs_copy();


