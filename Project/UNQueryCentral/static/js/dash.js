document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.querySelector(".toggle");
    const navigation = document.querySelector(".navigation");
    const main = document.querySelector(".main");
    const contentSections = document.querySelectorAll(".content-section");
    const newQueryBtn = document.getElementById("new-query-btn");
    const overlay = document.getElementById("overlay");
    const closeBtn = document.getElementById("close-btn");
    const homeBtn = document.getElementById("homeBtn");
    const historyBtn = document.getElementById("historyBtn");
    const messagesBtn = document.getElementById("messagesBtn");
    const settingsBtn = document.getElementById("settingsBtn");
    const confirmSignout = document.getElementById("confirm-signout");
    const userIcon = document.getElementById("userIcon");
    
    // Handle the navigation toggle
    toggle.addEventListener("click", () => {
        navigation.classList.toggle("active");
        main.classList.toggle("active");
    });

    // Handle section switching
    function switchSection(targetSectionId) {
        contentSections.forEach(section => {
            if (section.id === targetSectionId) {
                section.style.display = "block";
            } else {
                section.style.display = "none";
            }
        });
    }

    // Initial section display setup
    switchSection("home-section");

    // Add event listeners to navigation links
    document.querySelectorAll(".navigation ul li a").forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const targetSectionId = e.currentTarget.getAttribute("href").replace("#", "");
            switchSection(targetSectionId);
        });
    });

    // Handle "New Query" button click
    newQueryBtn.addEventListener("click", () => {
        overlay.style.display = "block";
    });

    // Handle "Close" button click on the popup
    closeBtn.addEventListener("click", () => {
        overlay.style.display = "none";
    });

    homeBtn.addEventListener("click", () => {
        switchSection("home-section");
    });

    historyBtn.addEventListener("click", () => {
        switchSection("history-section");
    });

    messagesBtn.addEventListener("click", () => {
        switchSection("messages-section");
    });

    // Handle "History" button click to switch to history section
    settingsBtn.addEventListener("click", () => {
        switchSection("settings-section");
    });

    // Handle "Sign Out" button click
    confirmSignout.addEventListener("click", () => {
        // Implement the logout logic here, such as clearing user data, etc.
        // For now, we simply redirect to the homepage
        window.location.href = "index.html";
    });

    // Ajout de l'événement de clic pour l'icône "personne"
    userIcon.addEventListener("click", () => switchSection("settings-section"));
});