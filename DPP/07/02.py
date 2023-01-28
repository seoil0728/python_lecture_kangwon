from threading import Lock


def locked_method(method):
    def newmethod(self, *args, **kwargs):
        with self._lock:
            return method(self, *args, **kwargs)
    return newmethod


class DecoratorLockedList(list):
    def __init__(self, *args, **kwargs):
        self._lock = Lock()
        super(DecoratorLockedList, self).__init__(*args, **kwargs)

    @locked_method
    def remove(self, elem):
        return super(DecoratorLockedList, self).remove(elem)

    @locked_method
    def insert(self, elem):
        return super(DecoratorLockedList, self).insert(elem)

    @locked_method
    def __contains__(self, elem):
        return super(DecoratorLockedList, self).__contains__(elem)
