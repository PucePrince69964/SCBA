from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import time
import pyautogui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options

app = Flask(__name__)
CORS(app)

options = Options()
options.add_experimental_option(
    "debuggerAddress",
    "127.0.0.1:9222"
)

driver = webdriver.Edge(
    service=Service(EdgeChromiumDriverManager().install()),
    options=options
)

driver.maximize_window()

def click_xpath(xpath):
    element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    driver.execute_script("arguments[0].click();", element)

def type_xpath(xpath, text):
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element.clear()
    element.send_keys(text)

def hover_xpath(xpath):
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    ActionChains(driver).move_to_element(element).perform()

def executar_automacao(dataframe):
    df_filtrado = dataframe.iloc[1:11]

    driver.get("http://127.0.0.1:5500/frontend/register.html")
    time.sleep(3)

    for index, linha in df_filtrado.iterrows():
        try:
            nome = str(linha.iloc[1])
            email = str(linha.iloc[2])
            ra = str(linha.iloc[3])
            senha = str(linha.iloc[4])

            type_xpath("/html/body/div[2]/form/input[1]", nome)
            type_xpath("/html/body/div[2]/form/input[2]", ra)
            type_xpath("/html/body/div[2]/form/input[3]", email)
            type_xpath("/html/body/div[2]/form/input[4]", senha)

            click_xpath("/html/body/div[2]/form/button[1]")

            pyautogui.press("enter")
            time.sleep(5)

            driver.switch_to.new_window('tab')
            driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            print("Iniciando envio de relatório")
            to_field = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Destinatários' or @aria-label='To']"))
            )
            to_field.clear()
            to_field.send_keys(email)

            subject_field = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='subjectbox' or @aria-label='Assunto']"))
            )
            subject_field.clear()
            subject_field.send_keys("Confirmação de Cadastro em Benefício Corporativo")

            mensagem = f"""Prezado(a) colaborador(a),

            Informamos que seu cadastro foi realizado com sucesso.

            RA: {ra}
            Senha: {senha}

            Recomendamos alterar sua senha no primeiro acesso.

            Atenciosamente,
            Departamento de Recursos Humanos
            """

            mensagem_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
            )

            mensagem_field.click()
            time.sleep(1)
            mensagem_field.send_keys(mensagem)

            hover_xpath("//div[@role='button' and (contains(@data-tooltip,'Enviar') or contains(@data-tooltip,'Send'))]")

            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.get("http://127.0.0.1:5500/frontend/register.html")
            time.sleep(5)

        except Exception:
            driver.save_screenshot(f"erro_{index}.png")
            continue
    if index > 1:
        pyautogui.alert(f"Os cadastros de {index} colaboradores foram realizados com sucesso!")
    else:
        pyautogui.alert("Cadastro finalizado com sucesso!")

@app.route('/', methods=['GET'])
@app.route('/favicon.ico')
def favicon():
    return '', 204
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'Arquivo sem nome'}), 400

    try:
        df = pd.read_excel(file, engine='openpyxl')
        executar_automacao(df)
        return jsonify({'message': 'Processado com sucesso', 'linhas': len(df)}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=False)