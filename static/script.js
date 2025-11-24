// Verificar el modo guardado y aplicar al cargar la página
document.addEventListener("DOMContentLoaded", function() {
    const darkModeToggle = document.getElementById("darkModeToggle");
    const isDarkMode = localStorage.getItem("darkMode") === "true";

    if (darkModeToggle) {
        darkModeToggle.checked = isDarkMode;
        document.body.classList.toggle("dark-mode", isDarkMode);
    }
});

// Alternar modo oscuro
function toggleDarkMode() {
    const isDarkMode = document.body.classList.toggle("dark-mode");
    localStorage.setItem("darkMode", isDarkMode);
}
