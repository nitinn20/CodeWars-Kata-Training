def remove_url_anchor(url):
    ur=''
    for i in url:
        if i=='#':
            break
        else:
            ur+=i
    return ur        