// Base API URL for all passenger operations
const API_URL = "http://127.0.0.1:5000/passengers";


// Load all passengers and display them in the table
async function loadPassengers() {
    const res = await fetch(API_URL);
    const data = await res.json();

    const list = document.getElementById("passengerList");
    list.innerHTML = "";

    // Create table rows for each passenger
    data.forEach(p => {
        const row = `
            <tr>
                <td>${p.name}</td>
                <td>${p.age}</td>
                <td>${p.destination}</td>
                <td>${p.ticket}</td>
                <td>
                    <button class="action-btn edit-btn" onclick="editPassenger(${p.id})">Edit</button>
                    <button class="action-btn delete-btn" onclick="deletePassenger(${p.id})">Delete</button>
                </td>
            </tr>
        `;
        list.innerHTML += row;
    });
}


// Add a new passenger using form input
async function addPassenger() {
    const passenger = {
        name: document.getElementById("name").value,
        age: document.getElementById("age").value,
        destination: document.getElementById("destination").value,
        ticket: document.getElementById("ticket").value
    };

    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(passenger)
    });

    loadPassengers();   // refresh list
}


// Delete a passenger by ID
async function deletePassenger(id) {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
    loadPassengers();
}


// Edit passenger using simple prompts
async function editPassenger(id) {
    const newName = prompt("Enter new name:");
    const newAge = prompt("Enter new age:");
    const newDest = prompt("Enter new destination:");
    const newTicket = prompt("Enter new ticket number:");

    const updated = {
        name: newName,
        age: newAge,
        destination: newDest,
        ticket: newTicket
    };

    await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updated)
    });

    loadPassengers();
}


// Load passengers when page opens
loadPassengers();
