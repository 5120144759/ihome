function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function () {
        setTimeout(function () {
            $('.popup_con').fadeOut('fast', function () {
            });
        }, 1000)
    });
}

$(document).ready(function () {
    $('#form-auth').submit(function (e) {
        e.preventDefault();
        real_name = $('#real-name').val();
        id_card = $('#id-card').val();
        $.ajax({
            url: '/user/auth/',
            dataType: 'json',
            data: {'real_name': real_name, 'id_card': id_card},
            type: 'patch',
            success: function (data) {
                if (data.code == 200) {
                    alert('成功');
                    location.href = '/user/my/'
                } else {
                    $('.error-msg').html('<i class="fa fa-exclamation-circle"></i>' + data.msg);
                    $('.error-msg').show()
                }
            },
            error: function (data) {
                alert('请求失败')
            }
        })
    });

    $.get('/user/ready_auth/', function (data) {
        if (data.code == 200) {
            $('#real-name').val(data.user.id_name);
            $('#id-card').val(data.user.id_card);
            if ($('#real-name').val()){
                $('#success').hide();
            }
        }
    })
});
