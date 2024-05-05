$(document).ready(function() {
    $('input[type="checkbox"]').change(function() {
        var id = $(this).data('id');
        var name = $(this).data('name');
        if ($(this).is(':checked')) {
        } else {
        }
    });

    $("#filter_button").click(function() {
    });
});
