document.getElementById('downloadForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const videoLink = document.getElementById('videoLink').value.trim();
    const videoQuality = document.getElementById('videoQuality').value;
    const statusMessage = document.getElementById('statusMessage');

    // Clear previous messages
    statusMessage.textContent = '';

    if (!videoLink) {
        statusMessage.textContent = 'Please enter a valid YouTube link.';
        return;
    }

    // Send the form data to the server using Fetch API
    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            'videoLink': videoLink,
            'videoQuality': videoQuality
        })
    })
    .then(response => response.text())
    .then(data => {
        statusMessage.textContent = 'Download started. You will receive the file shortly.';
    })
    .catch(error => {
        statusMessage.textContent = 'An error occurred during the download.';
        console.error('Error:', error);
    });
});
