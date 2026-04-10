async function register() {
    // Clear any previous error messages
    clearErrors();

    // Get the values from each input field
    const full_name = document.getElementById('full_name').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const address = document.getElementById('address').value.trim();

    // Basic frontend validation before sending to backend
    // This gives instant feedback without needing to wait for the server
    let hasError = false;

    if (!full_name) {
        showError('name_error', 'Full name is required');
        hasError = true;
    }
    if (!email) {
        showError('email_error', 'Email is required');
        hasError = true;
    }
    if (!password) {
        showError('password_error', 'Password is required');
        hasError = true;
    }

    // Stop here if there are frontend errors
    if (hasError) return;

    try {
        // Send a POST request to the Flask backend with the form data as JSON
        // fetch() is the modern way to make HTTP requests from JavaScript
        const response = await fetch('http://127.0.0.1:8080/auth/register', {
            method: 'POST',
            headers: {
                // Tells the backend we're sending JSON data
                'Content-Type': 'application/json'
            },
            // Convert the JavaScript object to a JSON string
            body: JSON.stringify({ full_name, email, password, phone, address }),
            // credentials: 'include' is needed for sessions to work across ports
            credentials: 'include'
        });

        // Parse the JSON response from the backend
        const data = await response.json();

        if (data.success) {
            // Store user details in sessionStorage so welcome.html can access them
            // sessionStorage is cleared when the browser tab is closed
            sessionStorage.setItem('full_name', data.full_name);
            sessionStorage.setItem('email', data.email);
            sessionStorage.setItem('user_type', data.user_type);

            // Redirect to welcome page
            window.location.href = 'welcome.html';
        } else {
            // Show the error message returned from the backend
            showError('general_error', data.message);
        }
    } catch (error) {
        // This runs if the fetch itself fails e.g. backend is not running
        showError('general_error', 'Could not connect to server. Is the backend running?');
    }
}

function showError(elementId, message) {
    // Finds the error span element and makes it visible with the message
    const element = document.getElementById(elementId);
    element.textContent = message;
    element.style.display = 'block';
}

function clearErrors() {
    // Hides all error messages before each submission attempt
    const errors = document.querySelectorAll('.error');
    errors.forEach(error => {
        error.textContent = '';
        error.style.display = 'none';
    });
}