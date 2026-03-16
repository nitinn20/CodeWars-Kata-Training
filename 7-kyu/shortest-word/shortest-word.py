def find_short(s):
    mini=9999999
    for i in s.split():
        if len(i)<mini:
            mini=len(i)
    return mini        