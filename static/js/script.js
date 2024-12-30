// document.addEventListener('DOMContentLoaded', function () {
//     const signOutBtn = document.getElementById('signout_btn');
    
//     if (signOutBtn) {
//         signOutBtn.addEventListener('click', function (e) {
//             e.preventDefault(); // Prevent form submission to show modal first

//             // Show the modal
//             var signOutModal = new bootstrap.Modal(document.getElementById('signOutModal'));
//             signOutModal.show();
//         });
//     }
// });

// This function will trigger the print dialog when called
function printRecipe() {
    window.print();
}

// Add an event listener to the "Print Recipe" button when the page loads
document.addEventListener('DOMContentLoaded', function () {
    const printButton = document.getElementById('printButton');
    if (printButton) {
        printButton.addEventListener('click', printRecipe);
    }
});