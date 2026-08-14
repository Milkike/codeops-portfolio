const { PHONE } = require("../../../../../Downloads/app");
const form = document.querySelector("#signupForm");
const nameInput = document.querySelector("#name");
const phoneInput = document.querySelector("#phone");
const errorMessage = document.querySelector("#error");
const countMessage = document.querySelector("#count");


// Ethiopian phone number:
// 0912345678
// +251912345678
const PHONE = /^(?:\+251|0)9\d{8}$/;

// Load saved people
function loadPeople() {
    try {
        const saved = localStorage.getItem("people");
        return saved ? JSON.parse(saved) : [];
    } catch (error) {
        return [];
    }
}

// Show how many people have signed up
function updateCount() {
    const people = loadPeople();

    countMessage.textContent =
        `${people.length} people have signed up.`;
}

// Validate the form
function validate(name, phone) {

    if (!name) {
        return "Please enter your full name.";
    }

    if (name.length < 2) {
        return "Name must be at least 2 characters.";
    }

    if (!phone) {
        return "Please enter your phone number.";
    }

    if (!PHONE.test(phone)) {
        return "Please enter a valid Ethiopian phone number.";
    }

    return "";
}

// Handle form submission
form.addEventListener("submit", (e) => {

    // Stop the page from reloading
    e.preventDefault();

    // Read and clean the input
    const name = nameInput.value.trim();
    const phone = phoneInput.value.trim();

    // Validate
    const error = validate(name, phone);

    if (error) {
        errorMessage.textContent = error;
        return;
    }

    // Get existing people
    const people = loadPeople();

    // Create new person
    const person = {
        name: name,
        phone: phone
    };

    // Add person to array
    people.push(person);

    // Save array as JSON
    localStorage.setItem(
        "people",
        JSON.stringify(people)
    );

    // Clear error
    errorMessage.textContent = "";

    // Clear form
    form.reset();

    // Update number of people
    updateCount();
});

// Run when page loads
updateCount();
