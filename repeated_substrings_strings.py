from collections import Counter

"""Data Input & Hardcoding Substrings"""
str = str(input("Please your text here: "))
sub_s = "r434"
len_sub_s = len(sub_s)

"""Validating that the substrings is 4 characters"""
while True:
    if len_sub_s == 4:
        print("you can pass")
        break
    else:
        print("must be 4 characters")
        exit()


def repeated_subs(str):
    """Counting the substrings in the text string """
    total = Counter([str[i: i + len(sub_s)]
                     for i in range(len(str))])
    return (total[sub_s])


print('The 4-character substrings are', repeated_subs(str))
