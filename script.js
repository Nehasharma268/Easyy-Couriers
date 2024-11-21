// Function to validate the booking form
function validateBookingForm() {
    var senderName = document.getElementById('senderName').value;
    var receiverName = document.getElementById('receiverName').value;
    var pickupAddress = document.getElementById('pickupAddress').value;
    var deliveryAddress = document.getElementById('deliveryAddress').value;
  
    if (senderName.trim() === '') {
      alert('Please enter the sender\'s name.');
      return false;
    }
  
    if (receiverName.trim() === '') {
      alert('Please enter the receiver\'s name.');
      return false;
    }
  
    if (pickupAddress.trim() === '') {
      alert('Please enter the pickup address.');
      return false;
    }
  
    if (deliveryAddress.trim() === '') {
      alert('Please enter the delivery address.');
      return false;
    }
  
    // Additional validation logic can be added here
  
    return true;
  }
  
  // Function to validate the feedback form
  function validateFeedbackForm() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;
  
    if (name.trim() === '') {
      alert('Please enter your name.');
      return false;
    }
  
    if (email.trim() === '') {
      alert('Please enter your email.');
      return false;
    }
  
    if (message.trim() === '') {
      alert('Please enter your message.');
      return false;
    }
  
    // Additional validation logic can be added here
  
    return true;
  }
  
  // Add event listeners to the form submission buttons
  var bookingForm = document.getElementById('bookingForm');
  if (bookingForm) {
    bookingForm.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission
      if (validateBookingForm()) {
        bookingForm.submit(); // Submit the form if validation passes
      }
    });
  }
  
  var feedbackForm = document.getElementById('feedbackForm');
  if (feedbackForm) {
    feedbackForm.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission
      if (validateFeedbackForm()) {
        feedbackForm.submit(); // Submit the form if validation passes
      }
    });
  }
  
  