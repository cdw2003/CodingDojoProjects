name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    new_dict = {}
    if len(arr1) == len(arr2):
        new_list = zip(arr1,arr2)
        new_dict.update(new_list)
    elif len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            new_list = zip(arr1, arr2)
            new_dict.update(new_list)
        elif len(arr2) > len(arr1):
            new_list = zip(arr2, arr1)
            new_dict.update(new_list)
    print new_dict
    return new_dict

make_dict(name, favorite_animal)
