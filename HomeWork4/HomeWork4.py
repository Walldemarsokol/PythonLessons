# import random
# some_dict = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
# k = int(input('Введите натуральную степень k: '))
# coef = [random.randint(0, 100) for _ in range(k + 1)]
# print(coef)
# with open('coef.txt', 'w', encoding='utf-8') as m:
#     for i in range(len(coef)):
#         if k - i != 1 and k - i != 0:
#             m.write(f'{coef[i]}x{some_dict[k - i]} + ')
#         elif k - i == 1:
#             m.write(f'{coef[i]}x + ')
#         elif k - i == 0:
#             m.write(f'{coef[i]} = 0')
