class Anagram:

    def anagram(first, second):
        return sorted(first) == sorted(second)

    str1 = input("Enter First String")
    str2 = input("Enter Second String")
    st1 = str1.replace(" ", "")
    st2 = str2.replace(" ", "")
    if anagram(st1, st2):
        print("Anagram")
    else:
        print("Not An Anagram")



