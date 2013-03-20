$(function() {
    $(".imgvideo").each(function() 
    {
        $(this).hover(
            function () {
                $(this).stop().animate({opacity: 1.0}, 800);
            },
            function () {
                $(this).stop().animate({opacity: 0.3}, 800);
            })
    });
});
