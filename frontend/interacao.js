const scbaBtn = document.getElementById('scba');
const container1 = document.getElementById('container1');
const container = document.getElementById('container');
const sair = document.getElementById('x');
const planilha = document.getElementById('fileUpload');
const validarBtn = document.querySelector('.validar');
const img = document.createElement('img');
const msg = document.getElementById('msg');
const btn3 = document.getElementById('btn3');
const nome = document.getElementById('username')
const ra = document.getElementById('ra')
const email = document.getElementById('email')
const senha = document.getElementById('password')

if (scbaBtn && container1) {
    scbaBtn.addEventListener('click', () => {
        container1.style.display = 'grid';
        container.style.display = 'none';
    });
}

if (sair && container1) {
    sair.addEventListener('click', () => {
        container1.style.display = 'none';
        container.style.display = 'block';
    });
}

if (validarBtn) {
    validarBtn.addEventListener('click', verificarFormatoArquivo);
}

btn3.addEventListener('click', (event) => {
    event.preventDefault();

    if (nome.value.trim() !== '' && ra.value.trim() !== '' && email.value.trim() !== '' && senha.value.trim() !== '') {
        if (isNaN(Number(ra.value))) {
            alert('RA deve conter apenas números.');
            return;
        }
        switch (email.value.split('@')[1]) {
            case 'empresa.org':
                break;
            default:
                alert('Email deve ter domínio, como @empresa.org');
                return;
        }
        if (senha.value.length < 6) {
            alert('A senha deve conter pelo menos 6 caracteres.');
            return;
        }
        alert('Cadastro realizado com sucesso!');
        nome.value = ''
        ra.value = ''
        email.value = ''
        senha.value = ''
        window.location.reload()
    }
})

function verificarFormatoArquivo() {
    if (!planilha.files || planilha.files.length === 0) {
        alert('Selecione um arquivo primeiro');
        return;
    }

    const arquivo = planilha.files[0];
    const extensao = arquivo.name.split('.').pop().toLowerCase();

    if (extensao === 'xlsx') {
        img.src = '../acessos/marca.png';
        img.classList.add('img');
        if (!container1.contains(img)) {
            container1.appendChild(img);
        }
        msg.textContent = 'Arquivo válido. Enviando ao servidor...';
        msg.style.color = 'green';
        
        // Chamada da função que faz a ponte com o Python
        enviarArquivoParaPython(arquivo);
    } else {
        img.src = '../acessos/botao-apagar.png';
        img.classList.add('img');
        if (!container1.contains(img)) {
            container1.appendChild(img);
        }
        msg.textContent = 'Arquivo inválido. Precisa estar no formato .xlsx (Excel)';
        msg.style.color = 'red';
    }
}

// NOVA FUNÇÃO: Conectando com o backend Python
function enviarArquivoParaPython(arquivo) {
    const formData = new FormData();
    formData.append('file', arquivo);

    // Envia o arquivo para o servidor Flask local rodando na porta 5000
    fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Sucesso:', data);
        msg.textContent = 'Arquivo processado com sucesso pelo Pandas!';
    })
    .catch(error => {
        console.error('Erro:', error);
        msg.textContent = 'Erro ao enviar o arquivo para o Python.';
        msg.style.color = 'red';
    });
}