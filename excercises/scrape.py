from contextlib import closing
from urllib import urlopen
import re



def get_current_packages():
    package_count_patern = r'<strong>\s*(\d{5,6})\s*</strong>\s*packages'
    url = 'https://pypi.python.org/pypi'
    with closing (urllib.urlopen(url)) as u:
        page = u.read()
    return int(re.search(package_count_patern, page).group(1))
#print re.findall(r'<strong>\s*(\d{5,6})\s*</strong>\s*packages', page)



if __name__ == '__main__':
    print get_current_packages()
