import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

'''
Criar o arquivo feature.feature
Inserir os cenários BDD
No Terminal digitar -> behave features
Criar um diretorio steps
criar uma classe Python steps
rodar o comando no terminal novamente
copiar e colar os step definitions

para rodar todas features 

behave features

para rodar uma feature 
behave features\google_search_outline.feature

Adicionar tags em cima da feature
rodando as features com determinada tag 
behave features --tags=regression

excluindo cenarios com determinada tag
behave features --tags=-regression

Instalar o allure-behave


'''


@given(u'I navigate to google.com')
def step_impl(context):
    context.driver.get('https://www.google.com')
    context.driver.implicitly_wait(10)


@when(u'I validate the page title')
def step_impl(context):
    title = context.driver.title
    print('Title is ', title)
    assert 'Google' in title


@then(u'I enter the text as "{search_text}"')
def step_impl(context, search_text):
    context.driver.find_element(By.NAME, 'q').send_keys(search_text)


@then(u'click the search button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").click()
