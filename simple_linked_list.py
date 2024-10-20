
class SimpleLinkedList:

    #~~~~INITIALIZATION~~~~#

    def __init__(self):
        self.head = None
        self.size = 0

    #~~~~REPRESNETATIONS~~~~#

    def to_list(self):
        list_ = []

        if self.head is None:
            return list_

        current = self.head

        while current is not None:
            list_.append(current.datum)
            current = current.ref

        return list_

    #~~~~GETTER METHODS~~~~#

    @property
    def head(self):
        return self._head

    @property
    def size(self):
        return self._size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            return None

        return self.head.tail

    #~~~~SETTER METHODS~~~~#

    @head.setter
    def head(self, head):
        self._head = head

    @size.setter
    def size(self, size):
        self._size = size

    def push(self, datum):
        if self.head:
            old = self.head
        else:
            old = None

        self.head = Element(datum, old)
        self.size += 1

    def pop(self):
        if not self.head:
            return None

        value = self.head.datum
        self.head = self.head.ref
        self.size -= 1

        return value

    @classmethod
    def from_list(cls, list_):
        instance = cls()

        if not isinstance(list_, list):
            pass
        else:
            for element in list_[::-1]:
                instance.push(element)

        return instance

    def reverse(self):
        return self.__class__.from_list(self.to_list()[::-1])

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#//////////////////////////////////////////////////////////////////////////////

class Element:

    #~~~~INITIALIZATION~~~~#

    def __init__(self, datum, ref=None):
        self.datum = datum
        self.ref = ref

    #~~~~GETTER METHODS~~~~#

    @property
    def datum(self):
        return self._datum

    @property
    def ref(self):
        return self._ref

    def is_tail(self):
        return self.ref is None

    @property
    def tail(self):
        if self.is_tail:
            return self.datum

        return self.ref.tail

    #~~~~SETTER METHODS~~~~#

    @datum.setter
    def datum(self, datum):
        self._datum = datum

    @ref.setter
    def ref(self, ref):
        self._ref = ref
