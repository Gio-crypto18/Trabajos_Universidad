const modalLogin = document.getElementById("modal-login");
const modalRegister = document.getElementById("modal-register");
const loginButton = document.getElementById("login-button");
const showRegisterButton = document.getElementById("show-register-button");
const showLoginButton = document.getElementById("show-login-button");
const closeModalButtons = document.getElementsByClassName("close-modal");

loginButton.addEventListener("click", () => {
    modalLogin.style.display = "flex";
});

showRegisterButton.addEventListener("click", () => {
    modalLogin.style.display = "none";
    modalRegister.style.display = "flex";
})

showLoginButton.addEventListener("click", () => {
    modalRegister.style.display = "none";
    modalLogin.style.display = "flex";
})

for (let i = 0; i < closeModalButtons.length; i++) {
    closeModalButtons[i].addEventListener('click', function() {
        modalLogin.style.display = "none";
        modalRegister.style.display = "none";
    });
}