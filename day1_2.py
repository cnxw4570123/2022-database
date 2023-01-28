def func_info(f):
    
    def info(*args):
        print(f'f_name : {f.__name__}, memory at {f}')
        print(f'positional param: {args}')
        result = f(*args)
        print(f'result = {result}')
        return result
    return info


@func_info
def factorial_recu(n):
    """
    재귀함수를 사용한 팩토리얼 함수
    :param n: n!
    :return: 자기 자신을 호출 또는 1
    """
    if n == 1:
        return 1
    return n * factorial_recu(n-1)


print(type(factorial_recu(5)))
