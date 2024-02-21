$(document).ready(function() {
    // Form submission using AJAX
    $('#menu-form').submit(function(event) {
        event.preventDefault(); // Prevent default form submission

        // Collect form data
        var formData = {
            'item_name': $('#item_name').val(),
            'item_description': $('#item_description').val(),
            'item_price': $('#item_price').val()
        };

        // Submit form data to Flask route
        $.ajax({
            type: 'POST',
            url: '/submit',
            data: formData,
            dataType: 'json',
            encode: true
        })
        .done(function(data) {
            // Display success message or handle response
            console.log(data);
        })
        .fail(function(data) {
            // Handle error
            console.log(data);
        });
    });
});
