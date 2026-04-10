async function register() {
    clearErrors();

    const full_name = document.getElementById('full_name').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const address = document.getElementById('address').value.trim();

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

    if (hasError) return;

    try {
        const response = await fetch('http://127.0.0.1:8080/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            
            body: JSON.stringify({ full_name, email, password, phone, address }),
            
            credentials: 'include'
        });

        const data = await response.json();

        if (data.success) {
            sessionStorage.setItem('full_name', data.full_name);
            sessionStorage.setItem('email', data.email);
            sessionStorage.setItem('user_type', data.user_type);

            
            window.location.href = 'welcome.html';
        } else {
            
            showError('general_error', data.message);
        }
    } catch (error) {
        showError('general_error', 'Could not connect to server. Is the backend running?');
    }
}

function showError(elementId, message) {
    const element = document.getElementById(elementId);
    element.textContent = message;
    element.style.display = 'block';
}

function clearErrors() {
    const errors = document.querySelectorAll('.error');
    errors.forEach(error => {
        error.textContent = '';
        error.style.display = 'none';
    });
}