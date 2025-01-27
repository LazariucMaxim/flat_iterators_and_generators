class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list

    def __iter__(self):
        self.cursor = [0, -1]
        return self

    def __next__(self):
        self.cursor[1] += 1
        if self.cursor[1] >= len(self.list[self.cursor[0]]):
            self.cursor[0] += 1
            self.cursor[1] = 0
            if self.cursor[0] >= len(self.list):
                raise StopIteration
        return self.list[self.cursor[0]][self.cursor[1]]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
