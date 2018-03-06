$(function () {
    var backButton = $('.back_top');

    function backToTop() {
        $('html,body').animate({
            scrollTop: 0
        }, 500);
    }

    backButton.on('click', backToTop);

    /*当滚动条的垂直位置大于浏览器所能看到的页面的那部分的高度时，回到顶部按钮就显示 */
    $(window).on('scroll', function () {
        if ($(window).scrollTop() > $(window).height() / 2)
            backButton.fadeIn();
        else
            backButton.fadeOut();
    });

    /*触发滚动事件，避免刷新的时候显示回到顶部按钮*/
    $(window).trigger('scroll');

    // 定位
    $.ajax({
        url: 'http://restapi.amap.com/v3/ip',
        data: {key: '049d254de7046935c431b8db38ce95b3'},
        success: function (arg) {
            $('#location').text(arg.city);
        },
        error: function (arg) {
            $('#location').text(arg.info);
        }
    })
});