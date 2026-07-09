(function () {
    var body = document.body;
    var menuToggle = document.querySelector('[data-profile-toggle]');
    var menu = document.querySelector('[data-profile-menu]');
    var themeButtons = document.querySelectorAll('[data-theme-choice]');
    var fallbackImages = document.querySelectorAll('[data-fallback]');

    function setActiveTheme(theme) {
        body.setAttribute('data-theme', theme);
        themeButtons.forEach(function (button) {
            button.classList.toggle('active', button.dataset.themeChoice === theme);
        });
        localStorage.setItem('booklib-theme', theme);
    }

    var storedTheme = localStorage.getItem('booklib-theme');
    if (storedTheme === 'light' || storedTheme === 'dark') {
        setActiveTheme(storedTheme);
    } else {
        setActiveTheme(body.getAttribute('data-theme') || 'light');
    }

    function useFallbackImage(image) {
        var fallbackSrc = image.dataset.fallback;

        if (fallbackSrc) {
            image.removeAttribute('data-fallback');
            image.src = fallbackSrc;
        }
    }

    fallbackImages.forEach(function (image) {
        image.addEventListener('error', function () {
            useFallbackImage(image);
        }, { once: true });

        if (image.complete && image.naturalWidth === 0) {
            useFallbackImage(image);
        }
    });

    if (menuToggle && menu) {
        menuToggle.addEventListener('click', function () {
            var isOpen = menu.classList.toggle('open');
            menuToggle.setAttribute('aria-expanded', String(isOpen));
        });

        document.addEventListener('click', function (event) {
            if (!menu.contains(event.target) && !menuToggle.contains(event.target)) {
                menu.classList.remove('open');
                menuToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }

    themeButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var theme = button.dataset.themeChoice;
            setActiveTheme(theme);

            if (!body.dataset.themeEndpoint) {
                return;
            }

            fetch(body.dataset.themeEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': body.dataset.csrfToken,
                },
                body: new URLSearchParams({ theme: theme }),
            }).catch(function () {});
        });
    });
})();
