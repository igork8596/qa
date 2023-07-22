from allure_commons.types import Severity
from selene import browser, by, be
import allure


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kuzminovig')
def test_allure_steps():
    with allure.step('Открываем главную страницу GitHub'):
        browser.open('https://github.com')

    with allure.step('Находим репозиторий'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('eroshenkoam/allure-example')
        browser.element('#query-builder-test').press_enter()

    with allure.step('Переходим в репозиторий'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем Issues'):
        browser.element("#issues-tab").click()

    with allure.step('Проверяем наличие Issue с номером 76'):
        browser.element(by.partial_text("#76")).should(be.visible)
