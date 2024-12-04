// // Sample data for Beneficiaries
// const beneficiaries = [
//     { name: "John Doe", contact: "123-456-7890", location: "Village A" },
//     { name: "Jane Smith", contact: "987-654-3210", location: "Village B" }
// ];

// // Sample data for Aid Items
// const aidItems = [
//     { name: "Rice", description: "10kg bags of rice", quantity: 50 },
//     { name: "Water", description: "Bottled drinking water", quantity: 100 }
// ];

// // Sample data for Distributions
// const distributions = [
//     { beneficiary: "John Doe", item: "Rice", quantity: 2, date: "2024-11-30" },
//     { beneficiary: "Jane Smith", item: "Water", quantity: 10, date: "2024-11-28" }
// ];

// // Function to populate table data
// function populateTable(id, data) {
//     const tableBody = document.getElementById(id);
//     data.forEach(item => {
//         const row = document.createElement("tr");
//         for (const key in item) {
//             const cell = document.createElement("td");
//             cell.textContent = item[key];
//             row.appendChild(cell);
//         }
//         tableBody.appendChild(row);
//     });
// }

// // Populate tables on page load
// window.onload = () => {
//     populateTable("beneficiaries-list", beneficiaries);
//     populateTable("aid-items-list", aidItems);
//     populateTable("distributions-list", distributions);
// };

// script.js
// document.addEventListener("DOMContentLoaded", () => {
//     const dropdowns = document.querySelectorAll(".dropdown");

//     dropdowns.forEach((dropdown) => {
//         dropdown.addEventListener("click", (event) => {
//             // Close other dropdowns
//             document.querySelectorAll(".dropdown-content").forEach((content) => {
//                 if (content !== dropdown.querySelector(".dropdown-content")) {
//                     content.style.display = "none";
//                 }
//             });

//             // Toggle the current dropdown
//             const content = dropdown.querySelector(".dropdown-content");
//             content.style.display =
//                 content.style.display === "block" ? "none" : "block";

//             // Prevent the click from closing the menu immediately
//             event.stopPropagation();
//         });
//     });

//     // Close dropdowns when clicking outside
//     document.addEventListener("click", () => {
//         document.querySelectorAll(".dropdown-content").forEach((content) => {
//             content.style.display = "none";
//         });
//     });
// });

document.addEventListener('DOMContentLoaded', () => {
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
    
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', (event) => {
            event.preventDefault();
            const dropdown = toggle.nextElementSibling;
            
            // Toggle visibility of the dropdown content
            if (dropdown.style.display === 'block') {
                dropdown.style.display = 'none';
            } else {
                dropdown.style.display = 'block';
            }
        });
    });
});
