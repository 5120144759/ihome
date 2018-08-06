function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function () {
    $.get('/house/area_facility/', function (data) {
        if (data.code == 200) {
            for (i = 0; i < data.areas.length; i++) {
                area_str = '<option value="' + data.areas[i].id + '">' + data.areas[i].name + '</option>';
                $('#area-id').append(area_str)
            }
            for (j = 0; j < data.facilitys.length; j++) {
                facility = '<li><div class="checkbox"><label>';
                facility += '<input type="checkbox" name="facility" value="' + data.facilitys[j].id + '">' + data.facilitys[j].name;
                facility += '</lable></div></li>';
                $('.clearfix').append(facility)
            }
        }
    });
    $('#form-house-info').submit(function (e) {
        e.preventDefault();
        $(this).ajaxSubmit({
            url: '/house/newhouse/',
            type: 'post',
            dataType: 'json',
            success: function (data) {
                if (data.code == 200) {
                    $('#form-house-info').hide();
                    $('#form-house-image').show();
                    $('#house-id').val(data.house_id)
                }
            },
            error: function (data) {
                alert('失败')
            }

        });
    })

    $('#form-house-image').submit(function (e) {
        e.preventDefault();
        $(this).ajaxSubmit({
            url: '/house/house_image/',
            dataType: 'json',
            type: 'post',
            success: function (data) {
                if (data.code == 200) {
                    img_src = '<img src="/static/media/' + data.image_url + '">';
                    $('.house-image-cons').append(img_src)
                }
            },
            error: function (data) {
                alert('失败')
            }
        })
    })
});