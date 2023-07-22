import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kuzminovig')
def test_decorator_steps():
    open_url('https://github.com')
    find_repository('eroshenkoam/allure-example')
    open_repository('eroshenkoam/allure-example')
    open_issues_tab()
    check_issue()


@allure.step('Открываем главную страницу GitHub')
def open_url(url):
    browser.open(url)


@allure.step('Находим репозиторий {repo}')
def find_repository(repo):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type(repo)
    browser.element('#query-builder-test').press_enter()


@allure.step('Переходим в репозиторий {repo}')
def open_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем Issues')
def open_issues_tab():
    browser.element("#issues-tab").click()


@allure.step('Проверяем наличие Issue с номером 76')
def check_issue():
    browser.element(by.partial_text("#76")).should(be.visible)
