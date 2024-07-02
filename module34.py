# def test_func(*params):
#     print('Tip:', type(params))
#     print('Arguments:', params)
# test_func(1,2,3,4)

# def summator(txt, *values, type='sum'):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt} {s} {type}'
#
# print(summator('Summa thisel:',1,2,3,4,5,6,7,8))

def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()

    for i in other_words:
        other_words = i.lower()

        if root_word in other_words or other_words in root_word:
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
