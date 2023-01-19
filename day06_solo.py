# manual decorator

def func_info(f):
    def info(*args, **kwargs):
        print('func name : ', f.__name__)
        print('positional param: ', args)
        print('keyword param:', kwargs)
        result = f(*args, **kwargs)
        print('result : ', result)
        return result
    return info


def list_into_dict(list1, list2):
    dict1 = {w1 : w2 for w1, w2 in zip(list1, list2)}
    return dict1


res1 = func_info(list_into_dict)
res1(['a', 'b', 'c', 'd'],[1, 2, 3, 4])