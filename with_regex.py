import re

r = re.compile(
    "(?P<s>Safari)|(?P<c>Chrome/\d+)|(?P<f>Firefox/\d+)|(?P<f_f>Firebird/\d+)|(?P<o>Opera/\d+)|(?P<o_2>OPR/\d+)",
    re.I)


def found_browser_name(string: str) -> str:
    """
    Функция для поиска названия браузера и его версии в строке user agent
    :param string: Строка user agent
    :return: Строка с результатом: Название браузера: ... Версия браузера: ...
    """

    version = 0
    safari = chrome = opera = opera_2 = firefox = firebird = False
    for i in r.finditer(string):
        reg = re.compile("(?P<v>Version/\d+)", re.I)
        if i.group('s'):
            safari = True
            for j in reg.finditer(string):
                if j.group('v'):
                    version = j.group('v').split('/')[-1]
        if i.group('c'):
            chrome = True
            version = i.group('c').split('/')[-1]
        if i.group('f'):
            firefox = True
            version = i.group('f').split('/')[-1]
        if i.group('f_f'):
            firebird = True
            version = i.group('f_f').split('/')[-1]
        if i.group('o'):
            opera = True
            for j in reg.finditer(string):
                if j.group('v'):
                    version = j.group('v').split('/')[-1]
        if i.group('o_2'):
            opera_2 = True
            version = i.group('o_2').split('/')[-1]
    if safari and not chrome:
        return f'Название браузера: Safari \nВерсия: {version}\n'
    if opera or chrome and safari and opera_2:
        return f'Название браузера: Opera \nВерсия: {version}\n'
    if firefox:
        return f'Название браузера: Firefox \nВерсия: {version}\n'
    if firebird:
        return f'Название браузера: Firefox Firebird \nВерсия: {version}\n'
    if chrome and safari:
        return f'Название браузера: Chrome \nВерсия: {version}\n'


def found_os(string: str) -> str:
    """
    Функция определяет ОС по строке user agent
    :param string: Строка user agent
    :return: Строка с названием ОС
    """
    os_dict = {
        'Windows NT 10': 'Windows 10',
        'Windows NT 6.3': 'Windows 8.1',
        'Windows NT 6.2': 'Windows 8',
        'Windows NT 6.1': 'Windows 7',
        'Windows NT 6.0': 'Windows Vista',
        'Windows NT 5.2': 'Windows Server 2003/XP x64',
        'Windows NT 5.1': 'Windows XP',
        'Windows xp': 'Windows XP',
        'Windows NT 5.0': 'Windows 2000',
        'Windows me': 'Windows ME',
        'win98': 'Windows 98',
        'win95': 'Windows 95',
        'win16': 'Windows 3.11',
        'macintosh|mac os x': 'Mac OS X',
        'mac_powerpc': 'Mac OS 9',
        'Linux': 'Linux',
        'Ubuntu': 'Ubuntu',
        'iphone': 'iPhone',
        'ipod': 'iPod',
        'ipad': 'iPad',
        'android': 'Android',
        'blackberry': 'BlackBerry',
        'webos': 'Mobile'
    }
    for i in os_dict.keys():
        if i in string:
            return f'Операционная система: {os_dict[i]}'


user_ua = input('Введите  строку user agent: ')
print('*' * 50)
result = f'{found_browser_name(user_ua)}{found_os(user_ua)}'
print(result)

# Для теста были использованы:
# ua_chrome = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'  # Chrome 53 Win 10
# ua_safari = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'  # Safari 5.1 Win 8
# ua_firefox = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0'  # Firefox 36 Win 8.1
# ua_firefox_2 = 'Mozilla/5.0 (X11; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0'  # Firefox 13  Linux
# ua_opera = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62'  # Opera 40 Win 10
# ua_opera_2 = 'Opera/9.80 (Windows NT 6.2; WOW64) Presto/2.12.388 Version/12.17'  # Opera 12 Win 8
# ua_opera_3 = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/4.0.2308.62'  # Opera 4 Win 10
# ua_firebird = 'Windows; U; Windows NT 5.1; en-US; rv:1.4b) Gecko/20030504 Mozilla Firebird/0.5+' # Firefox Firebird 0 Windows XP
# ua_firebird = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13' # Firefox Firebird 3 Windows 7
