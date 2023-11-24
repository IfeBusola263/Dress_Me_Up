function openLoginForm() {
    document.getElementById("loginForm").style.display = "block";
    document.getElementById("overlay").style.display = "block";
}

function openSignupForm() {
    document.getElementById("signupForm").style.display = "block";
    document.getElementById("overlay").style.display = "block";
}

function closeForm() {
    document.getElementById("loginForm").style.display = "none";
    document.getElementById("signupForm").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}

function showLoginForm() {
    document.getElementById("signupForm").style.display = "none";
    document.getElementById("loginForm").style.display = "block";
}


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