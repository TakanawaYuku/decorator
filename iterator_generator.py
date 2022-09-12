from decorator import log_file_path


#Задание №1
class FlatIterator:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):

        if self.count == len(self.n):
            raise StopIteration
        if not isinstance(self.n[self.count], (list, tuple, set)):
            value = self.n[self.count]
            self.count += 1
            return value
        else:
            self.n = list(self.n[self.count]) + self.n[self.count + 1:]
            self.count = 0
            return self.__next__()


#Задание №2
@log_file_path('logs', 'logs_file.csv')
def flat_generator(t):
    k = 0
    while True:
        if k == len(t):
            break
        if not isinstance(t[k], (list, tuple, set)):
            yield t[k]
            k += 1
        else:
            t = list(t[k]) + t[k + 1:]
            k = 0


#Список
nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
test_list = [['a', 'b', 'c', 'd'], [1, 2, 3, 4, 5], ['Hello', 'World'],
             [10, 11, 12]]

#Вывод nested_list
# for item in FlatIterator(nested_list):
#     print(f'{item}')

# print(f'{[i for i in FlatIterator(nested_list)]}')

# for item in flat_generator(nested_list):
#     print(f'{item}')

#Вывод test_list
for item in FlatIterator(test_list):
    print(f'{item}')

print(f'{[i for i in FlatIterator(test_list)]}')

for item in flat_generator(test_list):
    print(f'{item}')
