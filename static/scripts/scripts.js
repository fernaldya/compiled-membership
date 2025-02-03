function toggleFields() {
    const imageInput = document.getElementById("file");
    const numberInput = document.getElementById("number");
    const errorMessage = document.getElementById("error-message");

    if (imageInput.files.length === 0) {
        numberInput.required = true;
    } else {
        numberInput.required = false;
    }

    if (!numberInput.value) {
        imageInput.required = true;
    } else {
        imageInput.required = false;
    }

    validateFileSize(imageInput, errorMessage);
}

function validateFileSize(imageInput, errorMessage) {
    if (imageInput.files.length > 0) {
        const fileSize = imageInput.files[0].size / 1024 / 1024;
        if (fileSize > 2) {
            errorMessage.textContent = "File size should be less than 2MB!";
            imageInput.value = "";
        } else {
            errorMessage.textContent = "";
        }
    }
}

function submitForm(event) {
    event.preventDefault();

    const form = document.querySelector("form");
    const formData = new FormData(form);
    const successMessage = document.getElementById("success-message");
    const errorMessage = document.getElementById("error-message");

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            errorMessage.textContent = data.error;
            successMessage.textContent = "";
        } else {
            successMessage.textContent = data.message;
            errorMessage.textContent = "";
            form.reset();
        }
    })
    .catch(error => {
        errorMessage.textContent = "An error occurred while submitting the membership!";
        successMessage.textContent = "";
    });
}

function deleteMembership(name) {
    if (confirm("Are you sure you want to delete this membership?")) {
        fetch(`/delete`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name: name })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                location.reload();
            }
        })
        .catch(error => {
            alert("An error occurred while deleting the membership!");
        });
    }
}
