document.querySelector('handleFormSubmit').addEventListener('submit', async (evt) => {
    evt.preventDefault();

    const userInput = {
        userName: document.querySelector('#name').value,
        userEmail: document.querySelector('#email').value
    };

    const serverResponse = await fetch('http://localhost:5000/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userInput)
    });

    const serverResult = await serverResponse.text();
    console.log('Server response:', serverResult);
});
