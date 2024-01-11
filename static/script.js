function submitForm() {
    var name = document.getElementById("name").value;
    var mobile = document.getElementById("mobile").value;

    // Sending data to Flask backend using fetch
    fetch("/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ name: name, mobile: mobile }),
    })
    
    .then(response => response.json())
    .then(data => {
           // Display the message below the form
           var messageElement = document.getElementById("message");
           messageElement.innerHTML = data.message;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
