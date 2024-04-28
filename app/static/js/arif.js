//   // Get references to the checkbox and the new address form
//   const addressCheckbox = document.getElementById('addressCheckbox');
//   const newAddressForm = document.getElementById('newAddressForm');
//   const userAddressForm = document.getElementById('user-addr-btn');

//   // Add an event listener to the checkbox
//   addressCheckbox.addEventListener('change', function() {
//       // Toggle the visibility of the new address form based on the checkbox state
//       newAddressForm.style.display = addressCheckbox.checked ? 'block' : 'none';
//       userAddressForm.style.display = addressCheckbox.checked ? 'none' : 'flex';
//   });




// document.addEventListener('DOMContentLoaded', function() {
// // Get references to the "Next" buttons
// const nextButton1 = document.querySelector('.first-btn');
// const nextButton2 = document.querySelector('.second-btn');
// const nextButton2copy = document.querySelector('.second-btn-2');
// const nextButton3 = document.querySelector('.third-btn');
// const check1 = document.querySelector('.check1');
// const check2 = document.querySelector('.check2');
// const check3 = document.querySelector('.check3');
// const paymentMethodRadioGroup = document.getElementsByName('pay-method');


// // Get references to the accordion panels
// const accordion1 = document.querySelector('#panelsStayOpen-collapseOne');
// const accordion2 = document.querySelector('#panelsStayOpen-collapseTwo');
// const accordion3 = document.querySelector('#panelsStayOpen-collapseThree');


// const accordionButton1 = document.querySelector('.accordion-button1');
// const accordionButton2 = document.querySelector('.accordion-button2');
// const accordionButton3 = document.querySelector('.accordion-button3');

// // Initialize the state of the second and third accordion panels as locked
// let isAccordion2Locked = true;
// let isAccordion3Locked = true;



// // Add click event listener to the first "Next" button
// nextButton1.addEventListener('click', function() {
//   // Close the first accordion panel and remove active color
//   accordion1.classList.remove('show');
//   check1.style.display = 'block';

 
//   accordionButton1.classList.add('collapsed');
//   // Unlock and open the second accordion panel
//   if (isAccordion2Locked) {
//       isAccordion2Locked = false;
//       accordionButton2.classList.remove('collapsed');
//       accordion2.classList.add('show');
//   }
// });

// // Add click event listener to the second "Next" button
// nextButton2.addEventListener('click', function() {
//   // Close the second accordion panel and remove active color
//   accordion2.classList.remove('show');
//   check2.style.display = 'block';
//   accordionButton2.classList.add('collapsed');
//   // Unlock and open the third accordion panel
//   if (isAccordion3Locked) {
//       isAccordion3Locked = false;
//       accordionButton3.classList.remove('collapsed');
//       accordion3.classList.add('show');
//   }
// });


// nextButton2copy.addEventListener('click', function() {
//   // Close the second accordion panel and remove active color
//   accordion2.classList.remove('show');
//   check2.style.display = 'block';
//   accordionButton2.classList.add('collapsed');

//   // Unlock and open the third accordion panel
//   if (isAccordion3Locked) {
//       isAccordion3Locked = false;
//       accordionButton3.classList.remove('collapsed');
//       accordion3.classList.add('show');
//   }
// });

// for (const radioButton of paymentMethodRadioGroup) {
// radioButton.addEventListener('change', () => {
//   check3.style.display = 'block';
// });
// }

// // Prevent default toggling of accordion panels for locked panels
// document.querySelector('#accordionPanelsStayOpenExample').addEventListener('show.bs.collapse', function(event) {
//   const target = event.target;
//   if ((target === accordion2 && isAccordion2Locked) || (target === accordion3 && isAccordion3Locked)) {
//       // Prevent the accordion panel from opening if it is locked
//       event.preventDefault();
//   }
// });
// });




// const coupon = document.getElementById('have_coupon');
// const dis_coupon = document.getElementById('check_have_coupon');

// coupon.addEventListener('change', function() {
// dis_coupon.style.display = coupon.checked ? 'none' : 'block';
// dis_coupon.style.display = coupon.checked ? 'block' : 'none';
//   });
