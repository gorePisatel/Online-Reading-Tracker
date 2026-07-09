const readerRoot = document.querySelector('[data-reader]');
const pages = document.querySelectorAll('.page');
const pageContent = document.querySelectorAll('.page-content');
const progressBar = document.getElementById('progress-bar');
const csrfToken = document.querySelector('meta[name="csrf-token"]').content;

let currentPage = Number(readerRoot.dataset.startPage || 0);
let currentFont = 24;
let saveTimer = null;

function saveProgress() {
    if (readerRoot.dataset.canSaveProgress !== 'true') {
        return;
    }

    window.clearTimeout(saveTimer);

    saveTimer = window.setTimeout(function () {
        fetch(readerRoot.dataset.saveProgressUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({
                current_page: currentPage + 1,
            }),
        }).catch(function () {
            return null;
        });
    }, 250);
}

function showPage(index) {
    if (!pages.length) {
        return;
    }

    index = Math.max(0, Math.min(index, pages.length - 1));
    currentPage = index;

    pages.forEach(function (page) {
        page.classList.remove('active');
    });

    pages[index].classList.add('active');
    progressBar.style.width = ((index + 1) / pages.length) * 100 + '%';
    saveProgress();
}

function nextPage() {
    if (currentPage < pages.length - 1) {
        showPage(currentPage + 1);
    }
}

function prevPage() {
    if (currentPage > 0) {
        showPage(currentPage - 1);
    }
}

function updateFont() {
    pageContent.forEach(function (item) {
        item.style.fontSize = currentFont + 'px';
    });
}

showPage(currentPage);

document.getElementById('next').onclick = nextPage;
document.getElementById('prev').onclick = prevPage;
document.getElementById('right').onclick = nextPage;
document.getElementById('left').onclick = prevPage;

document.addEventListener('keydown', function (event) {
    if (event.key === 'ArrowRight') {
        nextPage();
    }

    if (event.key === 'ArrowLeft') {
        prevPage();
    }
});

document.getElementById('increase-font').onclick = function () {
    if (currentFont < 40) {
        currentFont++;
        updateFont();
    }
};

document.getElementById('decrease-font').onclick = function () {
    if (currentFont > 16) {
        currentFont--;
        updateFont();
    }
};
