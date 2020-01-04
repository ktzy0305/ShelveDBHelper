def test(data, **kwargs):
    data_count = len(list(map(lambda x: x, data)))
    if data_count > 0:
        keys = list(map(lambda x : x, kwargs))
        data_keys = list(map(lambda x : x, data[0]))
        if set(keys).issubset(set(data_keys)):
            match_result = []
            for data_row in data:
                match_count = 0
                for key in keys:
                    if data_row[key] == kwargs[key]:
                        match_count += 1
                if match_count == len(keys):
                    match_result.append(data_row)
            return match_result
        else:
            print("Some keys in kwargs do not exist in the data")
    else:
        print("There is no data in the following table")


data = [
    {
        "key1" : 12,
        "key2" : "string",
        "key3" : True,
    },
    {
        "key1" : 22,
        "key2" : "a sentence",
        "key3" : False,
    },
    {
        "key1" : 12,
        "key2" : "abc",
        "key3" : True,
    },
]

data2 = []

print(test(data=data, key1=12, key2="abc"))
print(test(data=data, key1=12, key3=True))
print(test(data=data2, key1=12))