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
    print(f'np.array([[1, 2, 3], [4, 5, 6]]:\n{arr_2d}')
    print(arr_2d.ndim)
    print(arr_2d[0])


def create_array():
    # Creates a 2-D array containing two arrays with the values [1,2,3] and [4,5,6]
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f'np.array([[1, 2, 3], [4, 5, 6]]:\n{arr_2d}')
    print(arr_2d.ndim)
    print(arr_2d[0])
    zeroes = np.zeros((2, 2, 2))
    print(zeroes)
    sevens = np.full((2, 2, 2), 7)
    print(sevens)
    ones = np.ones((2, 2, 2))
    print(ones)
    np.delete(arr_2d, 1, axis=0)
    print(f'After delete: np.delete(arr_2d, 0, axis=1) => {arr_2d}')


def calculations_array():
    list1 = np.random.rand(10)
    list2 = np.random.rand(10)
    print(list1)
    add = np.add(list1, list2)
    print(add)
    sub = np.subtract(list1, list2)
    print(sub)
    div = np.divide(list1, list2)
    print(div)
    mult = np.multiply(list1, list2)
    print(mult)
    dot = np.dot(list1, list2)
    print(dot)
    add[0] = 100
    add = np.append(add, [0.999, 0.888])
    print(f'add: {add}')


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


def save_and_load():
    arr2 = np.array([1, 2, 3, 4, 5])
    np.save("saved_array", arr2)
    test = np.load("saved_array.npy")


if __name__ == '__main__':
    slicing()
    view_vs_copy()
    create_array()
    calculations_array()
    save_and_load()


