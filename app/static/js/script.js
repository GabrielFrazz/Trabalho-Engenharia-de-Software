let sidebar = document.querySelector('.sidebar');
let mainContent = document.querySelector('.main-content');
let header = document.querySelector('header');

btn.onclick = function () {
    sidebar.classList.toggle('active');
    mainContent.classList.toggle('sidebar-active');
    header.classList.toggle('sidebar-active');
};

// Defina o usuário e a senha correta
const correctUsername = "usuario";
const correctPassword = "senha123";

// Adicione um evento de envio ao formulário
document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    // Obtenha os valores do campo de entrada
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Verifique se a senha está correta
    if (username === correctUsername && password === correctPassword) {
        // Redireciona para outro site se a senha estiver correta
        window.location.href = "https://github.com/patricknperes";
    } else {
        // Exibe uma mensagem de erro se a senha estiver incorreta
        document.getElementById("errorMessage").textContent = "Usuário ou senha incorretos!";
    }
});

function toggleMenu() {
    const dropdown = document.querySelector('.profile-dropdown');
    const toggleIcon = document.querySelector('.profile-toggle i');
    
    if (dropdown.classList.contains('hidden')) {
        dropdown.classList.remove('hidden');
        dropdown.classList.add('visible');
        toggleIcon.classList.add('rotate');
    } else {
        dropdown.classList.remove('visible');
        dropdown.classList.add('hidden');
        toggleIcon.classList.remove('rotate');
    }
}

// Seleção dos elementos necessários
const fileInput = document.getElementById('file-upload');
const previewImage = document.getElementById('preview-image');
const removeButton = document.getElementById('remove-image');
const salesForm = document.getElementById('sales-form');

// Função para exibir a imagem após o upload
fileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();

        // Exibe a imagem assim que o arquivo é carregado
        reader.onload = function(e) {
            previewImage.src = e.target.result;
            previewImage.style.display = 'block'; // Mostra a imagem
            removeButton.style.display = 'block'; // Mostra o botão de remover
        };

        reader.readAsDataURL(file);
    }
});

// Função para remover a imagem
removeButton.addEventListener('click', function() {
    fileInput.value = ''; // Limpa o input de arquivo
    previewImage.src = ''; // Remove o source da imagem
    previewImage.style.display = 'none'; // Esconde a imagem
    removeButton.style.display = 'none'; // Esconde o botão de remover
});

// Captura o envio do formulário
salesForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Previne o envio padrão

    // Cria um FormData com os dados do formulário
    const formData = new FormData(salesForm);

    // Se a imagem foi carregada, adiciona ao FormData
    if (fileInput.files[0]) {
        formData.append('image', fileInput.files[0]);
    }

    // Debug para verificar o conteúdo do FormData
    for (const pair of formData.entries()) {
        console.log(pair[0], pair[1]);
    }

    // Envio dos dados via fetch (verifique o caminho '/submit-form' no backend)
    fetch('/submit-form', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('Formulário enviado com sucesso!');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocorreu um erro ao enviar o formulário.');
    });
});
