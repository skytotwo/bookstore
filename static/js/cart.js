$(function () {
    var checked_alls = $('.check-all');
    var checked_ones = $('.check-one');
    updateCart();
    checked_alls.click(function () {
        if ($(this).prop('checked')) {
            checked_alls.each(function () {
                $(this).prop('checked', true)
            });
            checked_ones.each(function () {
                $(this).prop('checked', true)
            });
        } else {
            checked_alls.each(function () {
                $(this).prop('checked', false)
            });
            checked_ones.each(function () {
                $(this).prop('checked', false)
            });
        }
        updateCart();
    });
    checked_ones.click(function () {
        var checked_numbers = 0;
        checked_ones.each(function () {
            if ($(this).prop('checked')) {
                checked_numbers += 1;
            }
        });
        if (checked_numbers === checked_ones.length) {
            checked_alls.each(function () {
                $(this).prop('checked', true);
            });
        } else {
            checked_alls.each(function () {
                $(this).prop('checked', false);
            });
        }
        updateCart();
    });

    function updateCart() {
        var checked_items = 0;
        var total_price = 0;
        checked_ones.each(function () {
            if ($(this).prop('checked')) {
                var parents_tr = $(this).parents('tr');
                var current_items = parseInt(parents_tr.find('input[title="数量"]').val());
                var subtotal_price = current_items * parseFloat(parents_tr.find('.discount-price').text().split('￥')[1]);
                parents_tr.find('.subtotal-price').html('￥' + subtotal_price.toFixed(2));
                checked_items += current_items;
                total_price += subtotal_price;
            }
        });
        $('#checked-items').html(checked_items);
        $('#total_price').html('￥' + total_price.toFixed(2));
    }
});

$(function () {
    var navOffset = $("#settlement").offset().top;
    $(window).scroll(function () {
        var scrollPos = $(window).scrollTop();
        if (scrollPos <= navOffset - $(window).height()) {
            $("#settlement").addClass("fixed");
        } else {
            $("#settlement").removeClass("fixed");
        }
    });
});