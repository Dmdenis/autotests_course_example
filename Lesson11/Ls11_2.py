# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep

driver = webdriver.Chrome()
sbis_site = 'https://fix-online.sbis.ru/'
user_login = 'кабинет600'
user_password = 'кабинет6000'


try:
    driver.maximize_window()
    print('открываем страницу авторизации https://fix-online.sbis.ru/')
    driver.get(sbis_site)
    sleep(3)
    print('вводим логин и пароль и авторизуемся')
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(5)
    print('открываем реестр контакты')
    contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    contacts.click()
    sleep(2)
    dialogs = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    dialogs.click()
    sleep(5)
    print('нажимаем на кнопку плюс')
    add_contact = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')
    add_contact.click()
    sleep(5)
    print('В строку поиска адрессата вводим данные')
    find_contact = driver.find_element(By.CSS_SELECTOR, '.addressee-selector-popup__browser '
                                                        '.controls-InputBase__nativeField_hideCustomPlaceholder')
    sleep(2)

    find_contact.send_keys('Василенко Вячеслав', Keys.ENTER)
    sleep(5)
    print('Открываем окно нового сообщения адрессату')
    address = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]')
    address.click()
    sleep(5)
    print('Вводим сообщение')
    message = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    message_txt = 'Cообщение'
    message.send_keys(message_txt)
    print('Нажимаем отправить')
    send_message = driver.find_element(By.CSS_SELECTOR, '[title="Отправить"]')
    send_message.click()
    sleep(2)
    print('Находим последнее сообщение, проверяем текст')
    new_message = driver.find_elements(By.CSS_SELECTOR, '.controls-BaseControl .msg-dialogs-item__message-text')[0]
    assert new_message.text == message_txt, 'Неверное сообщение'
    sleep(2)
    print('удаляем сообщение')
    action = ActionChains(driver)
    action.move_to_element(new_message).perform()
    sleep(2)
    delete_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    delete_button.click()
    sleep(2)
    print('Проверяем что удалилось')
    last_message = driver.find_elements(By.CSS_SELECTOR, '.controls-BaseControl .msg-dialogs-item__message-text')[0]
    assert last_message != message_txt
finally:
    driver.quit()
