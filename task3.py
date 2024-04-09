class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.flat_list = []
    
    def flatten_list(self):
        for i in self.list_of_list:
            if isinstance(i, list):
                self.flat_list.extend(FlatIterator(i).flatten_list())
            else:
                self.flat_list.append(i)
        return self.flat_list

    def __iter__(self):
        self.iter_list = self.flatten_list()
        self.start, self.end = 1, len(self.iter_list)
        self.current_value = self.start - 1
        return self
    
    def __next__(self):
        if self.current_value >= self.end:
            raise StopIteration
        else:
            item = self.iter_list[self.current_value]
            self.current_value += 1
            return item

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()