$(function () {
    var checked_alls = $('.check-all');
    var checked_ones = $('.check-one');
    updateCheckedAll();
    updateCart();

    // 全选按钮的全选和全取效果
    checked_alls.change(function () {
        if ($(this).prop('checked')) {
            checked_alls.each(function () {
                $(this).prop('checked', true)
            });
            checked_ones.each(function () {
                $(this).prop('checked', true);
                changeItemChecked($(this));
            });
        } else {
            checked_alls.each(function () {
                $(this).prop('checked', false)
            });
            checked_ones.each(function () {
                $(this).prop('checked', false);
                changeItemChecked($(this));
            });
        }
        updateCart();
    });

    checked_ones.change(function () {
        updateCheckedAll();
        updateCart();
        changeItemChecked($(this));
    });

    // 后端改变checked状态
    function changeItemChecked(item) {
        if (item.prop('checked')) {
            $.ajax({
                url: '/cart/item-checked/checked/' + item.attr('id'),
                type: 'get',
                success: function (arg) {
                    console.log(arg);
                },
                error: function (arg) {
                    console.log(arg);
                }
            })
        } else {
            $.ajax({
                url: '/cart/item-checked/cancel/' + item.attr('id'),
                type: 'get',
                success: function (arg) {
                    console.log(arg);
                },
                error: function (arg) {
                    console.log(arg);
                }
            })
        }
    }

    // 查看目前是否是全选状态，如果是则选中全选按钮，否则取消全选
    function updateCheckedAll() {
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
    }

    // 更新购物车的选中数目和价格
    function updateCart() {
        var checked_items = 0;
        var total_price = 0;
        checked_ones.each(function () {
            if ($(this).prop('checked')) {
                var parents_tr = $(this).parents('tr');
                var current_items = parseInt(parents_tr.find('input[title="quantity"]').val());
                var subtotal_price = current_items * parseFloat(parents_tr.find('.discount-price').text().split('￥')[1]);
                parents_tr.find('.subtotal-price').html('￥' + subtotal_price.toFixed(2));
                checked_items += current_items;
                total_price += subtotal_price;
            }
        });
        $('#checked-items').html(checked_items);
        $('#total_price').html('￥' + total_price.toFixed(2));
        // 如果选中为0则disabled按钮
        if (checked_items === 0) {
            $('#settlement-btn').attr('disabled', 'disabled');
        } else {
            $('#settlement-btn').removeAttr('disabled');
        }
    }
});

// 结算条显示效果
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

// 数量input
$(function () {
    $('input[title="quantity"]').change(function () {
        window.location.href = '/cart/update/' + $(this).attr('id') + '/' + $(this).val();
    })
});