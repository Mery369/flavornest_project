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

const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}