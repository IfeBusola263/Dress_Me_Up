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

document.getElementById("overlay").addEventListener("click", function (event) {
    var loginForm = document.getElementById("loginForm");
    var signupForm = document.getElementById("signupForm");

    if (event.target === this || (event.target.classList.contains('overlay') && !isDescendant(loginForm, event.target) && !isDescendant(signupForm, event.target))) {
        closeForm();
    }
});

// Add a function to check if an element is a child of another element
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

document.getElementById("signupFormLink").addEventListener("click", function (event) {
    event.preventDefault();
    closeForm();
    openLoginForm();
});
