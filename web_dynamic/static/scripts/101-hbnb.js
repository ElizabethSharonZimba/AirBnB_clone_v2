$(document).ready(function() {
    $("#toggle_reviews").click(function() {
        if ($(this).text() === "show") {
            // Fetch, parse, display reviews
            $(this).text("hide");
        } else {
            // Remove all Review elements from the DOM
            $(this).text("show");
            $("#reviews").empty();
        }
    });
});
