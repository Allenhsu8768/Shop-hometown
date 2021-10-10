 // ============================ 購物車 確認結帳流程 1,2,3,4,  頁面變動及價格修改 begin ==========================================
// 結帳頁面 計算價錢
$(function () {
    //     // 設置 節點 計算總值的(總數量、總金額) =============================begin//
    // 1 decrease 減少數量
    $('.cart_goods_info').on('click','.decreaseamount',function () {
        // 獲取 input[type=hidden] 節點的數據
        let user_cart_msg = $(this).parent().parent().next().children('input')
        // 根據 hidden 排序 color 、 gid 、 size
        // 組數據字典給後端做處理數據動作
        let user_decrease_amount_goods_msg ={
            'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
            'action': 'decreases',
            'color' : user_cart_msg[0].value,
            'gid' : user_cart_msg[1].value,
            'size': user_cart_msg[2].value,
        }

        // 利用 post 請求刪除數量,且將後端給的值(總數量和總價),輸出到模板上
        $.post('/shop_cart/cart_goods_amount_change/', user_decrease_amount_goods_msg,function (data) {
            if(data.status==200){
                // 將值傳給模板做修改,總價,總數量
                change_total_ampunt_price_text(data.user_cart_total_amount, data.user_cart_total_price)
            }else if(data.status==400){
                location.href = '/login'
            }
        },'json')


        // 獲取 input 內的 value 做減數量
        let amount = $(this).next().val();

        // 獲取 要變換的單一總價格節點
        let singo_totla_price_node = $(this).parent().next().children()
        // 獲取 單件價格
        let price = Number($(this).parent().prev('.goods_price').children('span').text().replace(',',''));



        // 如果數量剩下 1 , 點選減少,則刪除節點,後端同時刪除商品資訊
        if(amount == 1){
            let li = $(this).parent().parent().parent();
            li.remove();
            alert('刪除商品成功!',4)
        }

        // input 的 amount -1
        amount --;

        // 計算扣掉後的總價
        let singo_total_price = price * Number(amount)


        // 減少數量加入 節點中
        $(this).next().val(amount);
        // 將總價插入節點中
        singo_totla_price_node.text(singo_total_price.toLocaleString())

        // 當減去 購物車　li 元素,判斷數量來設置 user_cart_box 樣式, 設置 setTimeout , 來解決 js非同步問題
        setTimeout(function () {
            // 設置 li_length 數量
            let li_length = $('.cart_goods_info li').length
            // 如果 購物車商品數量 = 0 , 則修改樣式
            if(li_length == 0){
                Cart_Empty()
            }
        },50)
    })

    // 2.increase 增加數量
    $('.cart_goods_info').on('click','.increaseamount',function () {
        // 獲取 input[type=hidden] 節點的數據
        let user_cart_msg = $(this).parent().parent().next().children('input')

        // 根據 hidden 排序 color 、 gid 、 size
        // 組數據字典給後端做處理數據動作
        let user_increase_amount_goods_msg ={
            'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
            'action': 'increase',
            'color' : user_cart_msg[0].value,
            'gid' : user_cart_msg[1].value,
            'size': user_cart_msg[2].value,
        }


        // 利用 post 請求增加數量
        $.post('/shop_cart/cart_goods_amount_change/', user_increase_amount_goods_msg,function (data) {
            if(data.status == 200){
                // 將值傳給模板做修改,總價,總數量
                change_total_ampunt_price_text(data.user_cart_total_amount, data.user_cart_total_price)
            }else if(data.status== 400){
                location.href = '/login';
            }
        },'json')

        // 獲取 input 內的 value 做加數量
        let amount = $(this).prev().val();
        // 獲取 要變換的單一總價格節點
        let singo_totla_price_node = $(this).parent().next().children()
        // 獲取 單件價格
        let price = Number($(this).parent().prev('.goods_price').children('span').text().replace(',',''));


        amount ++;
        // 增加數量加入
        // 計算單一總價格
        let singo_total_price = price * Number(amount)
        $(this).prev().val(amount);

        // 將總價插入節點中
        singo_totla_price_node.text(singo_total_price.toLocaleString())
    })

    // 直接修改 input 的值
    $('.cart_goods_info').on('change','.amount_change input',function () {

        // 獲取 change 的值
        let amount = $(this).val();
        // 獲取 price 價格
        let price = Number($(this).parent().prev('.goods_price').children('span').text().replace(',',''));



        // 獲取 input[type=hidden] 節點的數據
        let user_cart_msg = $(this).parent().parent().next().children('input')
        // 根據 hidden 排序 color 、 gid 、 size
        // 組數據字典給後端做處理數據動作
        let user_input_amount_goods_msg ={
            'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
            'action': 'input_change',
            'color' : user_cart_msg[0].value,
            'gid' : user_cart_msg[1].value,
            'size': user_cart_msg[2].value,
            'amount':amount,
        }

        // 利用 post 請求刪除數量,且將後端給的值(總數量和總價),輸出到模板上
        $.post('/shop_cart/cart_goods_amount_change/', user_input_amount_goods_msg,function (data) {

            if(data.status==200){
                // 將值傳給模板做修改,總價,總數量
                change_total_ampunt_price_text(data.user_cart_total_amount, data.user_cart_total_price)
            }else if(data.status==400){
                console.log('errmsg: ',data.messages);
            }
        },'json')


        // // 獲取 要變換的單一總價格節點
        let singo_totla_price_node = $(this).parent().next().children()
        // 獲取數量修改後總價格
        let singo_total_price = Number(price) * amount

        // 將總價插入節點中
        singo_totla_price_node.text(singo_total_price.toLocaleString())

        // 判斷用戶輸入的資料,如果為0 刪除商品, 如果為空則提醒數量不可為空
        if(amount==='0'){
            let li = $(this).parent().parent().parent();
            li.remove();
            alert('刪除商品成功!',4)
        }else if(amount===''){
            alert('商品數量不可空白!',5)
        }

        // 當減去 購物車　li 元素,判斷數量來設置 user_cart_box 樣式, 設置 setTimeout , 來解決 js非同步問題
        setTimeout(function () {
            // 設置 li_length 數量
            let li_length = $('.cart_goods_info li').length
            // 如果 購物車商品數量 = 0 , 則修改樣式
            if(li_length == 0){
                Cart_Empty()
            }
        },50)

    })
    // ============================ 購物車 數量修改價格變動 end ==========================================



    // ============================ 結帳流程 頁面轉換 begin=========================================

    // 點選結帳流程的 button 來改變流程顯示的圖
    // 1. cheack cart _ goods_list 點選 下一步
    $('.cart_next').click(function () {
        if($(this).text()=='下一步'){
            // cart 確認購物車頁面消失
            $('.cart_goods_info').css('display','none');
            // 展開 畫面 2 .cart_pay_send 頁面
            $('.cart_pay_send').css('display','block');

            // 將流程2樣式改變 新增 class='open'
            $('#process_2').addClass('open');
            // 將 流程 1 箭頭顯示展開
            $('#process_1').children('.arrow').css('display','inline-block');

            // 將 繼續購物的 button 修改為 返回前一個頁面 購物車確認頁面
            $('.cart_back').html('<a href="#top">' + '返回購物車' + '</a>');
            // 將 下一步 的 button 按鈕修改為名稱為 填寫收件人資料
            $(this).html('<a href="#top">' + '填寫收件人資料' +'</a>');

        }else if($(this).text()=='填寫收件人資料'){
            // 關閉  2.cart_pay_send 頁面
            $('.cart_pay_send').css('display','none');
            // 展開  3.add_infomation 頁面
            $('.add_infomation').css('display','block');

            // 將流程3 樣式改變新增 class='open'
            $('#process_3').addClass('open');
            // 將流程2 箭頭顯示展開
            $('#process_2').children('.arrow').css('display','inline-block');

            // 將一般按鈕 button 給隱藏
            $(this).css('display','none');

            // 將返回購物車 的按鈕修改名稱為 返回填寫付費方式
            $('.cart_back').html('<a href="#top">' + '返回填寫付費及運送' + '</a>')

            // 將設置好的 submit 表單提交按鈕展開,且解開鎖住的點擊
            $(this).next('.send_info_to').removeAttr('disabled').css('display','block');
        }
    })

    $('.cart_back').click(function () {
        //  進入 畫面 2  cart_pay_send 頁面
        if($(this).text()=='返回購物車'){
            // 1. cart 確認購物車頁面展開
            $('.cart_goods_info').css('display','block');
            // 2. 展開的cart_pay_send 頁面隱藏
            $('.cart_pay_send').css('display','none');
            $(this).next('button').html('<a href="#">' + '下一步' + '</a>');
            $(this).html('<a href="woman.html">' + '繼續購物' + '</a>');
            // 刪除展開樣式 流程 2
            $('#process_2').removeClass('open');
            // 將箭頭隱藏
            $('#process_1').children('.arrow').css('display','none');

            $(this).next('.send_infor_to').css('display','none');
        //    進入畫面 3 add_infomation 頁面
        }else if($(this).text()=='返回填寫付費及運送'){
            $('.cart_pay_send').css('display','block');
            $('.add_infomation').css('display','none');

            // 刪除展開樣式 流程 3
            $('#process_3').removeClass('open');
            // 隱藏流程 2 箭頭
            $('#process_2').children('.arrow').css('display','none');

            $(this).html('<a href="#top">' + '返回購物車' + '</a>');
            $(this).next('button').css('display','block');
            $(this).next('button').next('.send_info_to').css('display','none');
        }
})


    //2 .點擊提交按鈕 (送出按鈕,檢核用戶輸入的數據)
    $('.cart_goods_container').on('submit','#cart_frm',function () {
        // 獲取 li元素中, 數量節點(商品數量)
        let input_number_node = $(this).children('.cart_goods_list').children('.cart_goods_info').children('li').children('.cart_goods_desc').children('.amount_change').children('input[type=number]')

        // 獲取 radio的值 (付款方式和運送方式)
        let input_radio = $(this).children('.cart_goods_list').children('.cart_pay_send').children('li').children('input[type=radio]:checked')

        // 獲取 輸入的收件人地址訊息
        let input_text_node =$(this).children('.cart_goods_list').children('.add_infomation').children('.add_information_text').children('li').children('input[type=text]')

        // 遍歷,如果 value 為 0 則,顯示輸入數量不可空白的彈框
        for(let i=0;i<input_number_node.length;i++){
            if(input_number_node[i].value ==""){
                alert('輸入的商品數量不可以空白!',errmsg=5)
                return false
            }
        }

        if(input_radio.val()==null){
            alert('請選擇付款方式和運送方式',errmsg=6)
            return false;
        }

        for(let i=0;i<input_text_node.length;i++){
            if(input_text_node[i].value==''){
                alert('寄件人資料不可以空白!',errmsg=6)
                return false;
            }
        }
        return true;
    })

    // ============================ 結帳流程 頁面轉換 end=========================================

})


// 透過 post 傳參將參數傳入 function, 做總價和數量的改變
//  單次增加、單次減少、即直接修改數量,都會傳參到這個函數做總價的更換
function change_total_ampunt_price_text(amount,price) {

    //購物車數量改變
    let user_cart_new_amount =document.getElementsByClassName('user_cart_goods_amount')[0]
    // 減去 用戶點選商品數量
    user_cart_new_amount.innerText = amount

    //總數量
    $('.cart_goods_amount').html(amount)
    $('.pay_goods_amount').html(amount)
    // 價錢
    $('.cart_goods_total_price').html(price.toLocaleString())
    $('.pay_goods_price').html(price.toLocaleString())
    $('.total_count').html(price.toLocaleString())
}



// 購物車內無商品則掉用函數 Cart_Empty
 function Cart_Empty() {
        let check_goods_cart = '';
        check_goods_cart += `<div class="no_goods_in_cart">
                                <h1 class="no_goods_title">
                                    Your Cart is Empty !! 
                                </h1>
                                <div class="no_goods_in_cart_img_content">
                                    <img src="/static/images/no_goods_in_cart.png">
                                </div>
                                <button class="to_goods_index_button" onclick="enter_index()">前往首頁</button>
                            </div>`
        $('.cart_main').html(check_goods_cart);
        // 如果購物車為 0 , 將下列節點都刪除
        $('.cart_process').remove();
        $('.cart_goods_container').remove();

        $('.cart_pay_send').remove();
        $('.add_infomation').remove();
        $('.order_complete').remove();
        $('.total_price_container').remove();
        $('.cart_next_button').remove();
}

// 購物車無商品,點擊 button 跳轉首頁
function enter_index() {
    location.href = '/';
}



// 寫函數 將價格透過 toLocaleString 轉換成進位逗號格式
function price_change(price){
    return parseInt(price).toLocaleString()
}

//=================================== check-goods 確認結帳 商品介面 數據 begin ===============================
function load_check_goods_cart() {
    let params = {
        'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
    }
    $.post('/shop_cart/cart_goods_check/', params, function (data) {
        let check_goods_cart = '';
        // 如果 uid 存在購物車商品,則將資料顯示出來
        if(data.user_cart_info_status==1){
            // 設置 user_cart_goods 遍歷取值
            let user_cart_goods = data.user_cart_msg_list
            $.each(user_cart_goods,function (index,obj) {
                check_goods_cart += `<li>
                                        <div class="img_content">
                                            <a href="/shop_goods_detail?GOODS_ID=${obj.goods_id}&GOODS_COLOR=${obj.goods_color}">
                                                <img src="${obj.goods_img_url}">
                                            </a>
                                        </div>
                                        <!--  cart_goods_desc -->
                                        <div class="cart_goods_desc">
                                                <!-- goods_type -->
                                            <h2 class="goods_type">${obj.goods_type}'s</h2>
                                                <!-- goods_name -->
                                            <h3 class="goods_name">${obj.goods_title}</h3>
                                            <p class="goods_price">
                                                NT$: <span>${price_change(obj.goods_price)}</span>
                                            </p>
                                            <div class="amount_change">
                                                <p class="goods_size">
                                                    <span class="goods_size_text">Size: 
                                                        <span class="goods_size_background">${obj.goods_size}</span>
                                                    </span>
                                                    <span class="goods_color_text" style="display: block">
                                                        Color: 
                                                        <span class="goods_color_background" style="background: url(/${obj.goods_color_img_url}) repeat-x left top;"></span>
                                                        ${obj.goods_color}
                                                    </span>
                                                </p>
                                                <h4>Amount</h4>
                                                <button class="decreaseamount" type="button">-</button>
                                                <input type="number" value="${obj.goods_amount}" name="goods_amount">
                                                <button class="increaseamount" type="button">+</button>
                                            </div>
                                            <div class="singo_goods_total_price">
                                                NT$: <span>${price_change(obj.goods_total_price)}</span>
                                            </div>
                                        </div>
                                        <div class="delete_goods">
                                            <button type="button" onclick="delet_cart_goods(this,${obj.goods_amount})" class="delet_cart_goods">Delete</button>
                                            <input type="hidden" name="goods_color" value="${obj.goods_color}">
                                            <input type="hidden" name="goods_id" value="${obj.goods_id}">
                                            <input type="hidden" name="goods_size" value="${obj.goods_size}">
                                        </div>
                                    </li>`
            })
            //  將 商品數據插入 cart_goods_info 中
            $('.cart_goods_info').html(check_goods_cart);

            // 將參數傳入,改變計算的值

            $('.cart_goods_amount').html(data.user_cart_total_amount)
            $('.pay_goods_amount').html(data.user_cart_total_amount)
            // 價錢
            $('.cart_goods_total_price').html(data.user_cart_total_price.toLocaleString())
            $('.pay_goods_price').html(data.user_cart_total_price.toLocaleString())
            $('.total_count').html(data.user_cart_total_price.toLocaleString())

        }else if(data.user_cart_info_status==0){
            // 如果沒有商品則 插入 h1 元素
            Cart_Empty();
        }
    },'json')
}

//=================================== check-goods 確認結帳 商品介面 數據 end ===============================

 //===============點選刪除商品,執行的 function=================
function delet_cart_goods(obj,amount) {
    // 獲取上面的 hidden 對象(color、goods_id、size)
    let color = obj.nextElementSibling
    let goods_id = color.nextElementSibling
    let size = goods_id.nextElementSibling


    // 設置要傳給後端的數據字典
    delete_goods_msg = {
        // post 請求數據頭
        'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
        // 將上面的對象,取值放進字典中
        'color': color.value,
        'goods_id':goods_id.value,
        'size':size.value,
    }

    // 設置 post 請求 將數據刪除
    $.post('/shop_cart/delete_goods_in_cart/',delete_goods_msg,function (data) {
        if(data.delete_user_goods_status==1){

            // 購物車節點刪除
            // 2.點擊後刪除,onclick 節點 button 的 父元素 li
            let delete_li = (obj.parentNode).parentNode
            let li_parent = document.getElementById('cart_goods_info')
            li_parent.removeChild(delete_li)
            // 如果數量 和 價格 > 0,才做修改,如果 == 0 會直接切換到 no goods_in cart
            if(data.user_cart_total_amount>0 && data.user_cart_total_price>0){
                change_total_ampunt_price_text(data.user_cart_total_amount, data.user_cart_total_price)
            }
            //提示框刪除商品成功
            alert('刪除商品成功!',4)
        }else if(data.delete_user_goods_status==0){
            alert('刪除商品失敗!',4)
        }
    },'json')

    // 減去 用戶點選商品數量
    // 3.獲得參數 amount ,減去購物車的數量
    let user_cart_old_amount = parseInt(document.getElementsByClassName('user_cart_goods_amount')[0].innerText)
    let user_cart_new_amount = document.getElementsByClassName('user_cart_goods_amount')[0]
    // 減去 用戶點選商品數量
    user_cart_new_amount.innerText = user_cart_old_amount-amount


    // 當減去 購物車　li 元素,判斷數量來設置 user_cart_box 樣式, 設置 setTimeout , 來解決 js非同步問題
    setTimeout(function () {
        // 設置 li_length 數量
        let li_length = $('.cart_goods_info li').length
        // 如果 購物車商品數量 = 0 , 則修改樣式
        if(li_length == 0){
            Cart_Empty()
        }
    },50)
}



//===============獲取,支付方式的訊息===========
function load_pay_send_msg() {
    // 請求支付方式的數據
    $.get('/shop_cart/cart_goods_pay_send',function (data) {
        let show_pay_send = '<h3>台灣及離島</h3>';
        $.each(data,function (index,obj) {
           show_pay_send += `<li class="radio_group">
                                <input type="radio"  name="send_pay" id=${index} class="radio_input" value="${obj.chose_pay_send}">
                                <label for=${index} class="radio_label"><span class="radio_button"></span>${obj.chose_pay_send}</label>
                                <input type="hidden" name="send_price" value=${obj.send_price}>
                             </li>`
        })
        $('.cart_pay_send').html(show_pay_send)
    },'json')
}




