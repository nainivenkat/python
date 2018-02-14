from contextlib import closing
import requests
import re



def get_current_packages():
    package_count_patern = r'<strong>\s*(\d{5,6})\s*</strong>\s*packages'
    url = requests.get('https://pypi.python.org/pypi')
    with closing (url) as u:
        page = u.text
    return int(re.search(package_count_patern, page).group(1))
#print re.findall(r'<strong>\s*(\d{5,6})\s*</strong>\s*packages', page)



if __name__ == '__main__':
    print get_current_packages()
