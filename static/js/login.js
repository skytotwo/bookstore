$('.back_top').hide();

// 点击图片更换验证码
$(function () {
    $('#validate-img').css('cursor', 'pointer').click(function () {
        $('#validate-img').attr('src', $('#validate-img').attr('src') + "?1")
    });
});

// 加密传输
function encrypt() {
    // 获取加密密钥
    var pubKey = $('#public-key').val();
    // 设置加密函数
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(pubKey);
    // 加密
    var password = $('#inputPassword');
    var cipher = encrypt.encrypt(password.val());
    // 设置input的值
    password.val(cipher);
    return true;
}