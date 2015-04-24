__author__ = 'Q'


def is_permutation(s1, s2):
    is_perm = True
    if len(s1) != len(s2):
        is_perm = False
    if is_perm:
        i = 0
        f1 = [0] * 128
        f2 = [0] * 128
        while i < len(s1):
            f1[ord(s1[i])] += 1
            f2[ord(s2[i])] += 1
            i += 1
        j = 0
        while is_perm and j<len(s1):
            is_perm = (f1[ord(s1[j])]==f2[ord(s2[j])])
            j += 1

    return is_perm


str1 = 'gfcbd3ea'
str2 = 'abc3defg'

print(is_permutation(str1,str2))


