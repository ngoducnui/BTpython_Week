import urllib.request, urllib.error
def check_url (url):
    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        return format(e.code)
    except urllib.error.URLError as e:
        return format(e.reason)
    else:
        return 'good'
print('enter list url')
string = input()
arr = string.split('<<>>')
print("danh sách website đã kiểm tra:\n")
for x in arr:
    print(x, "=>", check_url(x))

