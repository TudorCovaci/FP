class IterableDataType:

    def __init__(self):
        self._data = []
        self._index = 0

    def __setitem__(self, key, value):
        if key > len(self._data):
            raise IndexError("Error: Invalid index!")
        if key < 0:
            key = len(self._data) - key
        self._data[key] = value
        return True

    def __getitem__(self,key):
        if key<0:
            key = len(self._data) - key
        return self._data[key]

    def __str__(self):
        """
        String format of the repository
        """

        string = ""
        for obj in self:
            string = string + str(obj) + '\n'
        return string

    def __len__(self):
        return len(self._data)

    def __delitem__(self, key):
        if key > len(self._data):
            raise IndexError("Error: Invalid index!")
        del self._data[key]
        return True

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self):
            obj = self._data[self._index]
            self._index += 1
            return obj
        raise StopIteration

    def append(self, obj):
        self._data.append(obj)
        return True


    def removeObj(self, obj):
        self._data.remove(obj)
        return True

    def clearData(self):
        self._data.clear()
        return True

    def getAll(self):
        return self._data


def switch(list, index1, index2):
    res = []
    for i in range(0,len(list)):
        if i == index1:
            res.append(list[index2])
        elif i ==index2:
            res.append(list[index1])
        else:
            res.append(list[i])
    return res


def sorted(listToSort, cmpFunction):
    # Start with a big gap, then reduce the gap
    n = len(listToSort)
    gap = n // 2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(gap, n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = listToSort[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and cmpFunction(listToSort[j - gap], temp):
                listToSort[j] = listToSort[j - gap]
                j -= gap
            # put temp (the original a[i]) in its correct location
            listToSort[j] = temp
        gap //= 2

def filter(list, contFunction, structure = lambda x: x):
    res = []
    for i in list:
        if contFunction(i) != 0:
            val = contFunction(i)
            res.append(val)
    return res


