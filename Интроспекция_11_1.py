import requests
# help(requests)
# help(requests.get)

some_string = "im a string"
some_number = 42
some_list = [some_string, some_number]


def some_function(param, param_2="n/a"):
    print("my params is", param, param_2)


class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)


some_object = SomeClass()


# print(some_function.__name__)
# print(SomeClass.__name__)
# print(requests.__name__)
# # print(some_string.__name__)
# # print(some_number.__name__)
#
# print(type(some_number) is int)


from pprint import pprint


# pprint(dir(some_list))
# pprint(dir(some_number))
# pprint(dir(some_string))
# pprint(dir(some_function))
# pprint(dir(some_object))
# pprint(dir(SomeClass))
pprint(dir(requests))

