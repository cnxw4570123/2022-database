# def multiply(f, list1, list2):
#     for n1, n2 in zip(list1, list2):
#         print(f(n1, n2))


# num1_list = [1, 2, 3, 4, 5]
# num2_list = [6, 7, 8, 9, 10]

# multiply(lambda num1, num2 : (num1 * num2), num1_list, num2_list)

drinks = {
    "martini": {"vodka", "vermouth"},
    "black russian": {"vodka", "kahlua"},
    "white russian": {"cream", "kahlua", "vodka"},
    "manhattan": {"rye", "vermouth", "bitters"},
    "screwdriver": {"orange juice", "vodka"},
}

for key, contents in drinks.items():
    # if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
    #     print(key)
    if contents & {"vermouth", "orange juice"}:
        print(key)

bruss = drinks["black russian"]
wruss = drinks["white russian"]

a = {1, 2}
b = {2, 3}

print(a & b)
print(a.intersection(b))
print(bruss & wruss)
print(a | b)
print(a.union(b))
print(bruss.union(wruss))
print(bruss.symmetric_difference(wruss))
print(a <= b)
print(bruss < wruss)
