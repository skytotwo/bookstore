$(function () {
    $('#pay_btn').click(function () {
        var recipient_id = $('#recipient-name').find('.active').attr('id');
        var payment_method_id = $('#pay_ul').find('.active').attr('id');
        $.ajax({
            url: '/user/order/',
            type: 'POST',
            data: {'recipient_id': recipient_id, 'payment_method_id': payment_method_id},
            headers: {"X-CSRFtoken": $.cookie("csrftoken")}
        });
    });
});