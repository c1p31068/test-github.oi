document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('imageForm');
    const imageInput = document.getElementById('imageInput');
    const submitBtn = document.getElementById('submitBtn');
    const resultDiv = document.getElementById('result');

    submitBtn.addEventListener('click', function () {
        const formData = new FormData(form);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(message => {
            resultDiv.textContent = message;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
