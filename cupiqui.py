class MyObject:
    def __init__(self, writable):
        self._writable = writable

    def writable(self):
        return self._writable

obj = MyObject(False)

if not obj.writable():
    break
