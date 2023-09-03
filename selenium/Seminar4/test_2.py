import requests
import logging


def get_my_posts(token):
    logging.debug('Open posts page')
    g = requests.get('https://test-stand.gb.ru/api/posts',
                     headers={'X-Auth-Token': token})
    if g:
        listcont = [i['content'] for i in g.json()['data']]
        return listcont
    else:
        logging.error('Страница с постами не открылась')


def get_notmy_posts(token):
    logging.debug('Open posts page')
    g = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token},
                     params={'owner': 'notMe'})
    if g:
        listcont = [i['content'] for i in g.json()['data']]
        return listcont
    else:
        logging.error('Страница с постами не открылась')


def createpost(token):
    logging.debug('Create new post')
    p = requests.post('https://test-stand.gb.ru/gateway/posts', headers={'X-Auth-Token': token},
                      data={'title': 'Новый пост для тестирования',
                            'description': 'informaition about post',
                            'content': 'Добавить в задание с REST API еще один тест, в котором создается новый пост,'
                                       'а потом проверяется его наличие на сервере по полю “описание”.'})
    if p:
        return p.json()
    else:
        logging.error('Пост не создан')


def findpost(token):
    logging.debug('Find created post')
    d = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
    if d:
        listdescript = [i['description'] for i in d.json()['data']]
        return listdescript
    else:
        logging.error('Пост не найден')


def test_2(login, not_my_post):
    assert not_my_post in get_notmy_posts(login)


def test_3(login, my_post):
    assert my_post in get_my_posts(login)

def test_step2(hello_user, browser, alert_text):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_good_login()
    page.enter_good_pass()
    page.click_login_button()
    # SendMail()
    assert page.get_hello_user() == hello_user
    page.click_contact_button()
    time.sleep(3)
    page.enter_name()
    page.enter_email()
    page.enter_content()
    time.sleep(3)
    page.click_contact_us_button()
    time.sleep(3)
    assert page.alert() == alert_text
