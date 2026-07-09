document.addEventListener('click', function (event) {
    const openButton = event.target.closest('[data-book-modal]');

    if (openButton) {
        const modalId = openButton.getAttribute('data-book-modal');
        const modal = document.getElementById(modalId);

        if (modal) {
            if (typeof modal.showModal === 'function') {
                modal.showModal();
            } else {
                modal.setAttribute('open', 'open');
            }
        }
    }

    if (event.target.matches('[data-book-modal-close]')) {
        const modal = event.target.closest('dialog');

        if (modal) {
            modal.close();
        }
    }

    if (event.target.classList.contains('book-modal')) {
        event.target.close();
    }
});
