// Function to toggle password visibility
function show() {
    const passwordField = document.getElementById("password");
    if (passwordField.type === "password") {
        passwordField.type = "text";
    } else {
        passwordField.type = "password";
    }
}


// Spinner Loader:
// const spinnerBox = document.getElementById('spinner-box');
// const loginForm = document.getElementById('loginForm');

// spinnerBox.classList.remove('not-visible');

// setTimeout(() => {
//     spinnerBox.classList.add('not-visible');  // Hide the spinner
//     loginForm.style.display = 'block';  // Show the form
// }, 1000); 