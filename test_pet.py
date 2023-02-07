from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_pet():
    #Подключаем вебдрайвер и указываем путь к нему
    driver = webdriver.Chrome(executable_path='C:\\Users\\play-\\PycharmProjects\\Selenium\\Chrome\\chromedriver.exe')
    driver.get('https://petfriends.skillfactory.ru/my_pets')

    #Делаем клик по кнопке регистрации
    reg_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/button').click()

    #Делаем клик по кнопке "Уже есть аккаунт"
    auth_button = driver.find_element(By.XPATH, '/html/body/div/div/form/div[4]/a').click()

    #Вводим email и пароль
    email_regist = driver.find_element(By.ID, 'email')
    email_regist.clear()
    email_regist.send_keys('oxtka@bk.ru')
    password_regist = driver.find_element(By.ID, 'pass')
    password_regist.clear()
    password_regist.send_keys('oxtkaip23')

    #Нажимаем на кнопку "Войти"
    auth2_button = driver.find_element(By.XPATH, '/html/body/div/div/form/div[3]/button').click()

    #Нажимаем на кнопку "Мои питомцы"
    my_pet_button = driver.find_element(By.CLASS_NAME, 'nav-link').click()

    #Ищем количество питомцев в таблице и статистике и проверяем, что есть все питомцы
    all_pets = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody')
    all = [pet.text.split('\n') for pet in all_pets][0][::2]
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    statistic = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[1]')
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])
    assert len(all) == number

    #Проверяем, что больше половины питомцев имеют фото
    src = []
    have_photo = 0
    not_have_photo = 0
    for i in range(1, len(all) + 1):
        img = driver.find_element(By.XPATH, f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/th/img')
        src.append(img.size)
    for i in src:
        if i.get('height') != 0:
            have_photo += 1
        else:
            not_have_photo += 1
    assert (have_photo / (have_photo + not_have_photo)) * 100 >= 50

    #Проверяем, что у всех питомцев есть Имя, Возраст, Порода
    pet_elements = []
    for i in range(1, len(all) + 1):
        for j in range(1, 4):
            driver.implicitly_wait(10)
            pets = driver.find_element(By.XPATH, f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[{j}]')
            pet_elements.append(pets.text)
    assert len(all) * 3 == len(pet_elements)

    #Проверяем, что у всех питомцев разные имена
    pet_name = []
    for i in range(1, len(all) + 1):
        elements = driver.find_element(By.XPATH, f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[1]')
        pet_name.append(elements.text)
    uniq_pet_name = set(pet_name)
    assert len(pet_name) == len(uniq_pet_name)

    #Проверяем, что нет повторяющихся питомцев
    all_pets2 = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    pets_data = [pet.text for pet in all_pets2]
    uniq_pets = set(pets_data)
    assert len(pets_data) == len(uniq_pets)
