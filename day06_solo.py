# recursive
def func_info(f):

    def info(args):
        print()
        print(f'함수 이름 : {f.__name__}, {f}')
        print(f'위치 인수 : {args}')
        result = f(args)
        print(f'결과 = {result}')
        return result

    return info


@func_info
def flatten(lol):  # flatten([3, 4, 5]), flatten([6, [7, 8, 9], []]) flatten([7, 8, 9]) flatten([])
    for item in lol:  # 1, 2, [3, 4, 5], [6, [7, 8, 9],[]]
        if isinstance(item, list):  # list의 원소가 list인지 확인
            for subitem in flatten(item):  # 3, 4, 5를 가진 generator 생성 # 6 yield
                yield subitem
        else:
            yield item


# generator : 시퀀스를 생성하는 객체


lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]

# flatten(lol)  # 1, 2, 3, 4, 5, 6, 7, 8, 9를 가진 generator 생성
for i in flatten(lol):
    print(i, end=" ")
