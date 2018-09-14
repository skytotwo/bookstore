$(function () {
    var recipient_id = $('#recipient-content').find('.active').attr('id');
    var payment_method_id = $('#payment_method').find('.active').attr('id');
    update_recipient(recipient_id);
    update_payment(payment_method_id);

    $('.update_recipient').click(function () {
        update_recipient($(this).find('a').attr('href').split('#')[1])
    });

    $('.update_payment').click(function () {
        update_payment($(this).attr('id'))
    });

    function update_recipient(id) {
        $('input[name="recipient_id"]').attr('value', id);
    }

    function update_payment(id) {
        $('input[name="payment_method_id"]').attr('value', id);
    }
});