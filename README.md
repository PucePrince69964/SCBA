# Sistema de Cadastro de Beneficiários Automatizado (SCBA)

## Descrição
O Sistema de Cadastro de Beneficiários Automatizado é uma solução desenvolvida para automatizar o processo de cadastro de colaboradores em plataformas de benefícios corporativos, como planos de saúde e convênios empresariais. O sistema realiza a leitura de planilhas fornecidas pelo RH, valida os dados dos funcionários e executa automaticamente o registro nas plataformas parceiras integradas.

## Objetivo
Reduzir tarefas manuais, minimizar erros operacionais e aumentar a eficiência do processo de inclusão de beneficiários em sistemas corporativos.

## Dados de teste
As planilhas utilizadas neste projeto possuem dados fictícios e foram criadas apenas para simulação do fluxo de automação.

Nenhuma informação real de colaboradores é utilizada.

## Envio de relatórios por e-mail

O sistema realiza o envio de relatórios utilizando uma conta do Gmail autenticada no navegador.

### Importante:
- O usuário deve estar previamente logado no Microsoft Edge.
- O sistema não realiza login automático por questões de segurança.
- Pode ser utilizada uma conta pessoal ou de testes.

## Funcionalidades

### Requisitos Funcionais
- Importação de planilhas .xlsx
- Validação automática de dados
- Cadastro automatizado de beneficiários
- Integração com plataformas parceiras
- Geração de logs e relatórios
- Monitoramento de status dos cadastros

### Requisitos Não Funcionais
- Tratamento de erros e inconsistências de dados durante o processamento
- Compatibilidade com diferentes formatos de planilha (.xlsx e .csv)
- Execução estável mesmo com falhas em registros individuais

## Tecnologias utilizadas
### Frontend
- HTML5
- CSS3
- JavaScript

### Backend / Automação
- Python

### Bibliotecas
- Flask → API backend
- Pandas → leitura de planilhas
- Selenium → automação web
- PyAutoGUI → automação de interface

## Estrutura do Projeto
```
Sistema de Cadastro de Benefícios Automatizado (SCBA)/
├── acessos/
│ ├── botao-apagar.png
│ ├── Exemplo.xlsx
│ └── marca.png
│
├── backend/
│ └── app.py
│
└── frontend/
├── estilo1.css
├── estilo3.css
├── interacao.js
├── menu.html
└── register.html
```

## Arquitetura do Sistema
- __Entrada de dados__: Planilha do RH
- __Processamento de dados__: Uso da biblioteca Pandas
- __Validação de dados__: Regras internas do sistema
- __Automação de cadastro__: Uso das bibliotecas PyAutoGUI e Selenium
- __Saída__: Registros e relatórios aos funcionários cadastrados via Gmail

## Fluxo de Funcionamento
- **1.** O RH envia a planilha que contém informações sobre os colaboradores
- **2.** O sistema lê e valida os dados da planilha
- **3.** As informações são processadas
- **4.** O cadastro é realizado automaticamente na plataforma parceira
- **5.** O sistema emite um relatório conforme os resultados

## Como executar
### 1. Pré-requisitos
- Python 3.10 ou superior
- Microsoft Edge instalado
- Git

### 2. Clonar o repositório
```
git clone https://github.com/PucePrince69964/SCBA.git
cd SCBA
```

### 3. Criar ambiente virtual
- Pelo PowerShell
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

- Pelo CMD:
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências
```
pip install -r requirements.txt
```

### 5. Abrir o navegador
```
 msedge --remote-debugging-port=9222 --user-data-dir="C:\EdgeDebug"
```

### 6. Executar o programa
```
python backend/app.py
```

### 7. Acessar o navegador
```
http://127.0.0.1:5000 (ou porta do backend Flask)
Caso esteja usando Live Server do VS Code, abra o arquivo register.html diretamente.
```

### 8. Envio da planilha de exemplo
Envie a planilha Exemplo.xlsx,que está na pasta .\acessos
```
.\acessos\Exemplos.xlsx
```

## Problemas comuns
### Erro: módulo não encontrado
pip install -r requirements.txt

### Edge não abre
Verifique o caminho de instalação do navegador

### Automação não funciona
Certifique-se de que a tela está ativa e desbloqueada

## Observações
Este sistema utiliza automação de interface gráfica e requer que o computador esteja desbloqueado durante a execução.

Durante a execução da automação, o usuário não deve interagir com o mouse ou teclado, pois o sistema controla a interface gráfica.

## Autor
Gabriel Yago Alves Mendonça
Sistema de Cadastro de Beneficiários Automatizado (SCBA)
