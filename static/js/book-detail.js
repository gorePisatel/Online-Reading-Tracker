document.addEventListener('click', function (event) {
    const button = event.target.closest('[data-tab-button]');

    if (!button) {
        return;
    }

    const tabs = button.closest('[data-tabs]');
    const tabName = button.getAttribute('data-tab-button');

    tabs.querySelectorAll('[data-tab-button]').forEach(function (item) {
        item.classList.toggle('active', item === button);
    });

    tabs.querySelectorAll('[data-tab-panel]').forEach(function (panel) {
        panel.classList.toggle(
            'active',
            panel.getAttribute('data-tab-panel') === tabName
        );
    });
});
