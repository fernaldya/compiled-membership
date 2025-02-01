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

// function openModal(imageSrc) {
//     // console.log("image source:", imageSrc);
//     const modal = document.getElementById("myModal");
//     const modalImg = document.getElementById("img01");

//     // if (modal && modalImg) {
//     modal.style.display = "block";
//     modalImg.src = imageSrc;

//     modal.onclick = function(event) {
//         if (event.target === modal) {
//             modal.style.display = "none";
//         }
//     };
//     // } else {
//     //     console.error("Modal or modal image not found!");
//     // };
// }
