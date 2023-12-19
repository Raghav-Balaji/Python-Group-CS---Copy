const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

// so by clicking the signup or signin button the animation moves showing the intended forms for the clicked button
signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

function validateLogin() {
    var dbUsername = document.getElementById("dbUsername").value;
    var dbPassword = document.getElementById("dbPassword").value;
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Basic client-side validation
    if (dbUsername === '' || dbPassword === '' || username === '' || password === '') {
        document.getElementById("errorMessage").innerHTML = "Please fill in all fields.";
        return false;
    }

    // Use AJAX to send the data to the server for validation
    $.ajax({
        type: "POST",
        url: "/login",
        data: {
            dbUsername: dbUsername,
            dbPassword: dbPassword,
            username: username,
            password: password
        },
        success: function (response) {
            if (response.success) {
                window.location.href = "dashboard.html";
            } else {
                document.getElementById("errorMessage").innerHTML = "Invalid username or password. Please try again.";
            }
        },
        error: function () {
            document.getElementById("errorMessage").innerHTML = "Error during login. Please try again.";
        }
    });

    // Prevent the form from submitting in the traditional way
    return false;
}
