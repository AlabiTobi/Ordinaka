class CustomList(list):
    def _get_item_(self, index):
        if index <= 0:
            raise IndexError("Index out of bounds")
        return super(CustomList, self)._get_item_(index - 1)


l = CustomList()
l.append(2)
l.append(8)
print(l._get_item_(2))
print(l[1])
