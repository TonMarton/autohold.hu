$( document ).ready(function() {

    if($(window).innerWidth() < 960) {
        $('#header-text').css('color', 'white');
    }

    $('#carousel').bind('slide.bs.carousel', function (e) {
        var index = $(e.target).find(".active").index();
        if (index === 2) {//  (2 - 1) index is zero based
            if($(window).innerWidth() < 960) {
                $('#header-text').css('color', 'white');
            } else {
                $('#header-text').css('color', 'black');
            }
        } else {
            $('#header-text').css('color', 'black');
        }
    });
});
