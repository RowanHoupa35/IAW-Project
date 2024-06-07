document.addEventListener('DOMContentLoaded', function() {
    const signInButton = document.getElementById('signIn');
    const forgotPasswordLink = document.getElementById('forgotPassword');
    const container = document.getElementById('container');
    const overlayBg = document.getElementById('overlayBg');
    const loginBtns = document.querySelectorAll('#login-btn');

    loginBtns.forEach(function (btn) {
        btn.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent default link behavior
            overlayBg.style.display = 'flex';  // Show the overlay
            document.body.style.overflow = 'hidden';  // Disable background scrolling
        });
    });

    overlayBg.addEventListener('click', function (event) {
        if (event.target === overlayBg) {
            overlayBg.style.display = 'none'; // Hide the overlay
            document.body.style.overflow = ''; // Enable background scrolling
        }
    });
    
    signInButton.addEventListener('click', () => {
        container.classList.remove("right-panel-active");
        container.classList.remove("forgot-password-active");
    });

    forgotPasswordLink.addEventListener('click', () => {
        container.classList.add("forgot-password-active");
        container.classList.remove("right-panel-active");
    });

});

// Récupérer le paramètre 'success' de l'URL
const urlParams = new URLSearchParams(window.location.search);
const success = urlParams.get('success');

// Si le paramètre 'success' est présent et vaut 'true', afficher la boîte de dialogue
if (success === 'true') {
    alert('Invalid e-mail or password.');
}
