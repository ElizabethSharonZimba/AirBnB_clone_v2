$(document).ready(function() {
    $('input[type="checkbox"]').change(function() {
        var amenityID = $(this).data('id');
        var amenityName = $(this).data('name');
        
        if ($(this).is(':checked')) {
            // Checkbox is checked
            // Store Amenity ID
            // Update h4 tag with list of checked amenities
        } else {
            // Checkbox is unchecked
            // Remove Amenity ID
            // Update h4 tag with list of checked amenities
        }
    });
});
