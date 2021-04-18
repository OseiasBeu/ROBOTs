from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import clipboard
import time
from PIL import Image
import loadImagem

class WhatsappBot:
    def __init__(self):
        options = Options()
        options.add_argument('lang=pt-br')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self,contatos,mensagem, imagem):
        self.driver.get('https://www.google.com.br/?gws_rd=ssl')
        for contato in contatos:
            url = f'https://api.whatsapp.com/send?phone=+55{contato}'
            clipboard.copy(url)
            pyautogui.hotkey('ctrl', 't',interval=1)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'tab',interval=1)
            pyautogui.hotkey('ctrl','w',interval=1)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter',interval=1)
            time.sleep(3)
            pyautogui.press('tab',interval=1)
            pyautogui.press('tab',interval=1)
            pyautogui.press('enter',interval=1)
            time.sleep(5)
            if imagem != '':
                loadImagem.readImage(imagem)
                time.sleep(5)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(1)
            clipboard.copy(mensagem)
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter',interval=1)
            pyautogui.hotkey('alt', 'tab')
            time.sleep(1)
        
        self.driver.quit()
        return 'Fim'


    def EnviarVideo(self,contatos,mensagem, video):
        actions = ActionChains(self.driver)
        self.driver.get('https://www.google.com.br/?gws_rd=ssl')
        for contato in contatos:
            url = f'https://api.whatsapp.com/send?phone=+55{contato}'
            clipboard.copy(url)
            pyautogui.hotkey('ctrl', 't',interval=1)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'tab',interval=1)
            pyautogui.hotkey('ctrl','w',interval=1)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter',interval=1)
            time.sleep(3)
            pyautogui.press('tab',interval=1)
            pyautogui.press('tab',interval=1)
            pyautogui.press('enter',interval=1)
            pyautogui.moveTo(100, 200)
            time.sleep(5)
            pyautogui.press('esc',interval=1)
            pyautogui.click('modulos\img\clip.png',interval=1)
            pyautogui.click('modulos\img\inserirImagem.png',interval=1)
            clipboard.copy(video)
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(2)
            pyautogui.press('enter',interval=1)
            clipboard.copy(mensagem)
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.click('modulos\img\sendVideo.png', interval=2)
            time.sleep(5)
            pyautogui.hotkey('alt', 'tab')
        self.driver.quit()
        return 'Fim'