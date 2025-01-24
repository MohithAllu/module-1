document.addEventListener("DOMContentLoaded", () => {
    const navLinks = document.querySelectorAll(".nav-links a");

    navLinks.forEach(link => {
        link.addEventListener("click", event => {
            event.preventDefault();
            const sectionId = link.getAttribute("href").substring(1);
            const section = document.getElementById(sectionId);

            if (section) {
                section.scrollIntoView({ behavior: "smooth" });
            } else {
                window.location.href = link.getAttribute("href");
            }
        });
    });
});