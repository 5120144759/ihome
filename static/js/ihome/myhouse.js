$(document).ready(function () {
    $.get('/house/house_info/', function (data) {
        if (data.code == 200) {
            $('.auth-warn').hide();
            $('#houses-list').show();
            for (i = 0; i < data.house_list.length; i++) {
                var house_li = '';
                house_li += '<li><a href="/house/detail/?house_id=' + data.house_list[i].id + '"><div ' +
                    'class="house-title"><h3>房屋ID:' + data.house_list[i].id + '</h3></div><img ' +
                    'src="/static/media/' + data.house_list[i].image + '" style="height: 206px; width: 279px">';
                house_li += '<div class="house-text"><ul>';
                house_li += '<li>位于：' + data.house_list[i].address + '</li>';
                house_li += '<li>价格：￥' + data.house_list[i].price + '/晚</li>';
                house_li += '<li>发布时间：' + data.house_list[i].create_time + '</li>';
                house_li += '</ul></div></div></a></li>';
                $('#houses-list').append(house_li)
            }
        } else {
            $(".auth-warn").show();
            $('#houses-list').hide();
        }

    });

});