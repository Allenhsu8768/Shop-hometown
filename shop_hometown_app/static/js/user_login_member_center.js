
// {#  新品展示  begin #}
function New_Arrival_goods() {
    $('.user_msg_content').children().css('display','none');
    $('.user_new_goods_msg').css('display','block');
}

// {#  新品展示  end #}





// {# 1. 會員查詢  begin   #}
function user_member_msg() {
    // 將 user_msg_content 的 子節點都隱藏
    $('.user_msg_content').children().css('display','none');
    var params = {
        'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
    }

    $.post('/login/api_user_member_msg/',params,function (data) {
        if(data.status == 200){
            let show_user_msg = '';
            show_user_msg += `<h2>會員基本資料:</h2>
                              <li>
                                <p>會員帳號:<span>${data.user_member_msg_dic.user_name}</span></p>
                              </li>
                              <li>
                                <p>會員姓名:<span>${data.user_member_msg_dic.realname}</span></p>
                              </li>
                              <li>
                                <p>會員信箱:<span>${data.user_member_msg_dic.email}</span></p>
                              </li>
                              <li>
                                <p>會員生日:<span>${data.user_member_msg_dic.birthday}</span></p>
                              </li>
                              <li>
                                <p>會員電話:<span>${data.user_member_msg_dic.phone_number}</span></p>
                              </li>
                              <li>
                                <p>會員居住國家:<span>${data.user_member_msg_dic.country}</span></p>
                              </li>
                              <li>
                                <p>會員居住城市:<span style="width: 400px;">${data.user_member_msg_dic.city}</p>
                              </li>
                              <li>
                                <p>會員註冊時間:<span>${data.user_member_msg_dic.registered_time}</span></p>
                              </li>
                              <li>
<!--                                    {# 判斷 用戶是否驗證 #}-->
                                    <p style="position: relative; top: -15px">會員是否驗證成功:${data.user_member_msg_dic.is_Active?
                                        '<span style="width: 100px; background: url(/static/images/is_active_ok.png) no-repeat -2px #dbd0d0; position: relative; top: 10px"></span>':
                                        '<span style="width: 100px; background: url(/static/images/is_active_not_ok.png) no-repeat 20px #dbd0d0; position: relative; top: 15px; right: 10px"></span>' +
                '                       <button type="button" class="check_mail_button" onclick="send_to_maill(this)">重新發送驗證信</button>'}
                                    </p>
                              </li>`
            $('.user_member_msg_list').html(show_user_msg);
            $('.user_member_msg').css('display','block');
        }
    },'json')
}

// {# 重新發送驗證信   #}
function send_to_maill(obj) {
    // {# 設置 傳給後端的 user_name (token) 和 e-mail(發送地址) ,realname, 處理發送郵件#}
    let user_name = obj.parentNode.parentNode.parentNode.children[1].children[0].children[0].innerText
    let user_realname = obj.parentNode.parentNode.parentNode.children[2].children[0].children[0].innerText
    let user_email = obj.parentNode.parentNode.parentNode.children[3].children[0].children[0].innerText

    // {# 將 按鈕 設置加入 class click , 讓 before 偽元素出現 #}
    obj.className = 'check_mail_button click'

    let user_msg_dict = {
        'user_name': user_name,
        'user_email':user_email,
        'user_real_name':user_realname,
    }

   $.get('/login/api_send_user_mail',user_msg_dict,function (data) {
        if(data.status==200){
             // {#當接收到,信箱驗證訊息成功後,將樣式改回,然後 before 隱藏#}
            obj.className = 'check_mail_button'
            alert('已發送驗證信,至信箱,請前去確認!!')
        }else if (data.status==400){
             // {#當接收到,信箱驗證訊息成功後,將樣式改回,然後 before 隱藏#}
            obj.className = 'check_mail_button'
           alert('發送驗證信,失敗!')
        }
    },'json')
}

//   1. 會員查詢  end




// {# 2. 修改會員資料  begin #}
function update_user_member_msg() {
    console.log('update_user_member_msg')
}





// {# 3. 查詢商品清單追追蹤 begin #}

// 價格格式改變
function price_change(price){
    return parseInt(price).toLocaleString()
}

function user_track_goods_msg() {
    $('.user_msg_content').children().css('display','none');
    // 透過 get 方式 獲取,user_member track 追蹤清單的資料
    $.get('/login/api_user_track_goods_msg',function (data) {
        // 用戶有追蹤商品 status = 1
        let show_track_msg = '';
        if(data.user_track_goods_msg_status==1){
            // 將 data.user_track_goods_msg 轉為 json 對象
            let track_goods_msg = JSON.parse(data.user_track_goods_msg)
            show_track_msg += `<h2>追蹤商品:</h2>`
            track_goods_msg.forEach(function (item) {
                show_track_msg += `<li class="track_goods_msg_li">
                                        <p>
                                            <a href="/shop_goods_detail?GOODS_ID=${item.goods_id}">
                                                <img src="/${item.goods_img}">
                                            </a>
                                        </p>
                                        <div class="track_goods_desc">
                                        <!--   goods_name                                         -->
                                            <h3>${item.goods_name}</h3>
                                            <h4>NT$ : ${price_change(item.goods_price)}</h4>
                                            <!-- 多少人點擊追蹤此商品-->
                                            <div class="user_like_content">
                                                <span class="track_goods_like_heart"></span>
                                                ${item.goods_heart} people like this.
                                            </div>
                                            <div class="track_goods_size_color_content">
                                                <h5>Existing Color and Size:</h5>
                                        <!--    利用 map 的方式將所有的 顏色對應尺寸(庫存) 顯示出來 -->
                                                ${item.goods_color_img_color.map((item2,index,array)=>{
                                                    return `<ul class="track_goods_color">
                                                                <div class="color_size">
                                                                    <span class="track_gods_background" style="background: url(/${item2[Object.keys(array[index])[0]]}) no-repeat;"></span>
                                                                    <span class="track_gods_color_name">${Object.keys(array[index])[0]}</span>
                                                                </div>
                                                                <li>XXS</li>
                                                                <li>XS</li>
                                                                <li>S</li>
                                                                <li>M</li>
                                                                <li>L</li>
                                                                <li>XL</li>
                                                                <li>XXL</li>
                                                           </ul>`
                                                    }).join('')}
                                            </div>
                                        </div>
                                        <div class="delete_track_goods_content">
                                            <div class="click_delete_button" onclick="delete_track_goods(this)">
                                                <span class="click_rectangle"></span>
                                            <!--   設置 goods_id 點擊刪除 傳給後端處理-->
                                                <input type="hidden" name="goods_id" value=${item.goods_id}>
                                                <input type="hidden" name="goods_img" value=/${item.goods_img}>
                                            </div>
                                        </div>
                                   </li>`
            })
        $('.user_track_goods_list').html(show_track_msg);
        $('.user_track_good_msg').css('display','block');
        // 用戶沒有追蹤商品 status = 0,調用 not_goods_to_track
        }else if(data.user_track_goods_msg_status==0){
            show_track_msg += not_goods_to_track()
        }
    },'json')
}
// 如果沒有追蹤的商品,則調用此函數 (當節點刪除時到商品時調用,及一開始就沒有數據時調用)
function not_goods_to_track() {
    let show_track_msg = '';
    show_track_msg += `<h2>追蹤商品:</h2>
                      <div class="not_goods_track">
                        <h1>您沒有追蹤商品的紀錄!</h1>
                        <div class="img_content">
                            <img src="/static/images/no_track_goods.png">
                        </div>
                        <div class="to_shop_button_content">
                            <button type="button" onclick="to_index()" class="to_index_button">前往首頁</button>
                        </div>
                      </div>`
    $('.user_track_goods_list').html(show_track_msg);
    $('.user_track_good_msg').css('display','block');
}

// 點選前往首頁
function to_index() {
    location.href = '/'
}

// 刪除追蹤商品
function delete_track_goods(obj) {
    // 設置 要刪除的追蹤商品 傳給後端
    let goods_id = obj.children[1]
    let goods_img = obj.children[2].value

    // 獲取 li 元素節點
    let delete_li = obj.parentNode.parentNode
    // 獲取 li 元素父節點
    let li_parent = obj.parentNode.parentNode.parentNode

    // 將子節點 li 元素刪除
    li_parent.removeChild(delete_li)

    let delete_goods = {
        'goods_id':goods_id.value
    }

    // 將要刪除的追蹤商品 傳給後端
    $.get('/login/api_track_goods',delete_goods,function (data) {
        if(data.status==200){
            alert2(goods_img,2)
        }else {
            alert('商品移除清單失敗!')
        }
    },'json')


    // 計算 li 元素,當 li.length = 0 時,調用 not_goods_to_track
    setTimeout(function () {
        let li_length = $('.user_track_goods_list li').length
        console.log(li_length)
        if(li_length == 0){
            not_goods_to_track();
        }
    },50)

}






//  3. 查詢商品清單追追蹤 end






// {# 4. 查詢訂單紀錄  #}
function user_order_msg() {
    $('.user_msg_content').children().css('display','none');
    $('.user_order_content').css('display','block');
    $('.user_order_content').css('display') == 'block'?
        $('.send_order_msg_search').removeAttr('disabled'):
        $('.send_order_msg_search').attr('disabled','disabled')
}



function send_search_msg(){
    let order_number = document.getElementsByName('order_number')[0].value
    let order_date_begin = document.getElementsByName('order_date_begin')[0].value
    let order_date_end = document.getElementsByName('order_date_end')[0].value

    // 判斷 起始日期不可以大於結束日期
    if(order_date_begin > order_date_end){
        alert('日期輸入有誤(起始日期大於結束日期)!!')
        return false
    }

    // 組要傳到後端的數據 用 post 請求的方式 (查詢訂單)
    let user_order_seach_dict = {
        'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
        'order_number': order_number,
        'order_date_begin': order_date_begin,
        'order_date_end': order_date_end,
    }

    // 接收後端數據,將數據整理顯示在畫面上
    $.post('/order_system/api_query_user_order/',user_order_seach_dict,function (data) {
        if(data.user_order_status==1){
            $('.user_search_order_info_content').html(load_order_msg(data));
        }else if(data.user_order_status==0){
            console.log('not data is found!')
        }
    },'json')
}


function load_order_msg(data) {
    let show_order_msg = '';
    data.user_order_info_msg.forEach(function (item,index,array) {
        show_order_msg += `<table class="user_search_order_msg_table" cellpadding="2" border="1">
                                <thead>
                                    <tr>
                                        <th>訂單編號</th>
                                        <th>訂單時間</th>
                                        <th>支付方式</th>
                                        <th>運費</th>
                                        <th>訂單金額</th>
                                        <th>收件人姓名</th>
                                        <th>收件人電話</th>
                                        <th>收件人地址</th>
                                        <th>訂單狀態</th>
                                        <th>訂單處理時間</th>
                                    </tr>
                                </thead>
                                <tbody>
                                     <tr>
                                        <th>${item.order_number}</th>
                                        <th>${item.order_time}</th>
                                        <th>${item.order_pay_chose_pay}</th>
                                        <th>${item.order_pay_send_price}</th>
                                        <th>${price_change(item.order_total_price)}</th>
                                        <th>${item.recipient_name}</th>
                                        <th>${item.recipient_phone_number}</th>
                                        <th>${item.recipient_address}</th>
                                        <!--  根據訂單狀態顯示 如下資訊 -->
                                        ${item.order_status ? 
                                        '<th>已處理</th>'+ '<th>' + item.order_check_time + '</th>':
                                        '<th>未處理</th><th><button onclick="delete_order()" class="delete_order_msg">Delete</button></th>'}
                                     </tr>
                                </tbody>
                           </table>
                           <div class="user_order_detail_msg_content">
                                <div class="user_order_detail_box">
                                    <div class="user_click_order_detail_msg">
                                        <h3>訂單明細<span class="triangle"></span></h3>
                                    </div>
                                    <ul class="user_order_detail_list">
                                        ${item.user_order_info_detail.map(function (item2,index,array) {
                                            //  list li 明細頁面
                                            return `<li class="order_goods_li">
                                                        <p>
                                                          <a href="/shop_goods_detail?GOODS_ID=${item2.goods_id}&GOODS_COLOR=${item2.goods_color}">
                                                            <img src=${item2.goods_img_url}>
                                                          </a>
                                                        </p>
                                                        <div class="order_goods_desc">
                                                            <h4>${item2.goods_name}</h4>
                                                            <h5>NT$ : ${price_change(item2.goods_price)} </h5>
                                                            <div class="order_goods_other_info">
                                                            <!--  將商品詳細資訊放入 ul 中的 li 中 顯示    -->
                                                                <ul class="order_goods_other_list">
                                                                    <li class="order_goods_size_color_amount" style="background: #0e3047">${item2.goods_size}</li>
                                                                    <li class="order_goods_size_color_amount" style="background: darkkhaki">${item2.goods_color}</li>
                                                                    <li class="order_goods_size_color_amount" style="background: red">${item2.goods_amount}</li>
                                                                    <li>
                                                                        <span class="order_goods_color_img" style="background: url(/${item2.goods_color_img}) no-repeat;"></span>
                                                                    </li>
                                                                </ul>
                                                            </div>
                                                        </div>
                                                    </li>`
                                        }).join('')}                       
                                    </ul>
                                </div>
                           </div>`
    })
    return show_order_msg
}

function delete_order() {
    console.log('hello world');
}
