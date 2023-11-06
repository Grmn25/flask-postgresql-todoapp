document.addEventListener("DOMContentLoaded", function() {
  const flashMessages = document.querySelectorAll(".flash");

  flashMessages.forEach((message) => {
    // Elimina la clase 'shake' después de la animación
    message.addEventListener("animationend", () => {
      message.classList.remove("shake");
    });
  });
  const contentSection = document.querySelector('[transition-style="in:circle:center"]');

  // Agregar la animación al elemento
  contentSection.style.animation = "2.5s cubic-bezier(.25, 1, .30, 1) circle-in-center both";

  // Escuchar el evento de finalización de la animación
  contentSection.addEventListener("animationend", function() {
    // Eliminar la animación una vez que se complete
    contentSection.style.animation = "none";
  });
});


