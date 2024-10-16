#1
def remove_exclamation_marks(s):
    return s.replace("!", "")

#2
def reverse(st):
    rev = []
    for word in st.split():
        rev.insert(0, word)
    return " ".join(rev)


#3
def distinct(seq):
    result = []
    for num in seq:
        if num not in result:
            result.append(num)
    return result

#4
def is_isogram(string):
    string = string.lower()
    for i in string:
        if string.count(i) > 1:
            return False
    return True

#5
def remove_duplicate_words(s):
    result = []
    for word in s.split():
        if word not in result:
            result.append(word)
    return " ".join(result)

#6
def vaporcode(s):
    return s.upper().replace(" ", "").replace("", "  ").strip("  ")

#7
def bounces(h,bounce,window):
    if h > 0 and 1 > bounce > 0 and window < h:
        count = 1
        h = h * bounce
        while h > window:
            count += 2
            h = h * bounce
        return count
    return -1
            