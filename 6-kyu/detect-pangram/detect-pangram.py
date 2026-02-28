def is_pangram(st):
    letters=set()
    for i in st.lower():
        if i.isalpha():
            letters.add(i)
    if len(letters)==26:
        return True
    return False 