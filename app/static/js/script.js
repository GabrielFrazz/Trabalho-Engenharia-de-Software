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

    dropdown.classList.toggle('hidden');
    dropdown.classList.toggle('visible');

    // Alterna a rotação da seta 180 graus
    toggleIcon.classList.toggle('rotate');
}