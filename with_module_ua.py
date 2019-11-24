from user_agents import parse

ua_user = input('Введите строку user agent: ')


def search_by_ua(string_ua: str) -> str:
    """
    Функция поиска названия браузера, его версии и операционной системы ua
    :param string: Строка user agent
    :return: Строка с названием браузера, версии и ос
    """

    us_agent = parse(string_ua)
    info = str(us_agent).split('/')
    print(info)
    # browser_info = info[2].split()
    # name_browser = browser_info[0]
    # version = browser_info[1].split('.')[0]
    # os = info[1]
    name_browser = us_agent.browser.family
    version = us_agent.browser.version[0]
    os = us_agent.os.family + us_agent.os.version_string

    return f'Название браузера: {name_browser}\nВерсия: {version}\nОперационная система: {os}'


print('*' * 50)
print(search_by_ua(ua_user))

#Для примера использованы:
# ua_chrome = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'  # Chrome 53 Win 10
# ua_safari = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'  # Safari 5.1 Win 8
# ua_firefox = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0'  # Firefox 36 Win 8.1
# ua_firefox_2 = 'Mozilla/5.0 (X11; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0'  # Firefox 13  Linux
# ua_opera = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62'  # Opera 40 Win 10
# ua_opera_2 = 'Opera/9.80 (Windows NT 6.2; WOW64) Presto/2.12.388 Version/12.17'  # Opera 12 Win 8
# ua_opera_3 = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/4.0.2308.62'  # Opera 4 Win 10
# ua_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
# Для firebird необходимо в версии убирать [0], определяется как Other без версии