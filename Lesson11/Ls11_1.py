# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

sbis_site = 'https://sbis.ru/'
driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get(sbis_site)
    contacts_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__container [href="/contacts"]')
    contacts_btn.click()
    sleep(2)
    banner_button = driver.find_element(By.CSS_SELECTOR, '[class="sbisru-Contacts__logo-tensor mb-8"]')
    banner_button.click()
    driver.switch_to.window(driver.window_handles[1])
    power = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    assert power.text == 'Сила в людях'
    assert power.is_displayed(), 'Новость "Сила в людях" не отображается'
    actions = ActionChains(driver)
    sleep(2)
    more = driver.find_element(By.CSS_SELECTOR, '[class="nl-LastCovers__header_newsLink"]')
    actions.move_to_element(more)
    actions.perform()
    about = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg .tensor_ru-link')
    about.click()
    assert driver.current_url == 'https://tensor.ru/about', 'Неверная адрес страницы'
    sleep(5)

finally:
    driver.quit()
