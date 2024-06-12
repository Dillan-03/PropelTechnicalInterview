document.addEventListener("DOMContentLoaded", () => {
    fetchRecords();

    document.getElementById("addRecordForm").addEventListener("submit", function(event) {
        event.preventDefault();
        addRecord();
    });
});

function fetchRecords() {
    fetch('/records')
        .then(response => response.json())
        .then(data => {
            const recordsDiv = document.getElementById('records');
            recordsDiv.innerHTML = '';
            data.forEach((record, index) => {
                const recordDiv = document.createElement('div');
                recordDiv.classList.add('record');
                recordDiv.innerHTML = `
                    <p><strong>${record.first_name} ${record.last_name}</strong></p>
                    <p>Phone: ${record.phone}</p>
                    <p>Email: ${record.email}</p>
                    <button onclick="deleteRecord(${index})">Delete</button>
                `;
                recordsDiv.appendChild(recordDiv);
            });
        });
}

function addRecord() {
    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    const phone = document.getElementById("phone").value;
    const email = document.getElementById("email").value;

    fetch('/records', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            first_name: firstName,
            last_name: lastName,
            phone: phone,
            email: email
        })
    })
    .then(response => response.json())
    .then(data => {
        fetchRecords();
        document.getElementById("addRecordForm").reset();
    });
}

function deleteRecord(index) {
    fetch(`/records/${index}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        fetchRecords();
    });
}
