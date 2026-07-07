(function () {
    var body = document.body;
    var menuToggle = document.querySelector("[data-profile-toggle]");
    var menu = document.querySelector("[data-profile-menu]");
    var themeButtons = document.querySelectorAll("[data-theme-choice]");

    function setActiveTheme(theme) {
        body.setAttribute("data-theme", theme);
        themeButtons.forEach(function (button) {
            button.classList.toggle("active", button.dataset.themeChoice === theme);
        });
        localStorage.setItem("booklib-theme", theme);
    }

    var storedTheme = localStorage.getItem("booklib-theme");
    if (storedTheme === "light" || storedTheme === "dark") {
        setActiveTheme(storedTheme);
    } else {
        setActiveTheme(body.getAttribute("data-theme") || "light");
    }

    if (menuToggle && menu) {
        menuToggle.addEventListener("click", function () {
            var isOpen = menu.classList.toggle("open");
            menuToggle.setAttribute("aria-expanded", String(isOpen));
        });

        document.addEventListener("click", function (event) {
            if (!menu.contains(event.target) && !menuToggle.contains(event.target)) {
                menu.classList.remove("open");
                menuToggle.setAttribute("aria-expanded", "false");
            }
        });
    }

    themeButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var theme = button.dataset.themeChoice;
            setActiveTheme(theme);

            if (!window.BookLIBTheme || !window.BookLIBTheme.endpoint) {
                return;
            }

            fetch(window.BookLIBTheme.endpoint, {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": window.BookLIBTheme.csrfToken,
                },
                body: new URLSearchParams({ theme: theme }),
            }).catch(function () {});
        });
    });
})();
