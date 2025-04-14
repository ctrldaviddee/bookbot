from collections import Counter

def display_word_count(text: str):
    return len(text.split(maxsplit=-1))


def count_characters(text):
    return dict(Counter(text.lower()))

def sorted_dict(dictionary: dict):

    return sorted(
                [{'char': char, 'count': count} for char, count in dictionary.items()],
                key=lambda x: x['count'],
                reverse=True
            )


# char_count = {}
# for char in text.lower():
#     char_count[char] = char_count.get(char, 0) + 1
# return char_count

# def count_characters(text: str):
#     text = text.lower()
#     chars_count = {}

#     for char in text:
#         if char in chars_count:
#             chars_count[char] += 1
#         else:
#             chars_count[char] = 1

#     return chars_count


    # result = []
    # for char, count in dictionary.items():
    #     result.append({'char':char, 'count':count})

    # result.sort(key=lambda x: x['count'], reverse=True)

    # return result
    #
