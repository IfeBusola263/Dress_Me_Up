// This function popup the login form when the login button is clicked
function openLoginForm() {
    document.getElementById("loginForm").style.display = "block";
    document.getElementById("overlay").style.display = "block";
}

// This function popup the signup form when the signup button is clicked
function openSignupForm() {
    document.getElementById("signupForm").style.display = "block";
    document.getElementById("overlay").style.display = "block";
}
// This function close the form when the 'X' is clicked or anywhere outside the form is clicked
function closeForm() {
    document.getElementById("loginForm").style.display = "none";
    document.getElementById("signupForm").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}

// This function popup the login form when the login button is clicked from the signup form
function showLoginForm() {
    document.getElementById("signupForm").style.display = "none";
    document.getElementById("loginForm").style.display = "block";
}


// This function is responsible for checking if the eventListner is happening in the overlay or outside the overlay
function isDescendant(parent, child) {
    var node = child.parentNode;
    while (node != null) {
        if (node == parent) {
            return true;
        }
        node = node.parentNode;
    }
    return false;
}

document.addEventListener("click", function (event) {
    var overlay = document.getElementById("overlay");
    var loginForm = document.getElementById("loginForm");
    var signupForm = document.getElementById("signupForm");

    if (event.target === overlay && !isDescendant(loginForm, event.target) && !isDescendant(signupForm, event.target)) {
        closeForm();
    }
});

document.getElementById("signupFormLink").addEventListener("click", function (event) {
    event.preventDefault();
    closeForm();
    openLoginForm();
});
