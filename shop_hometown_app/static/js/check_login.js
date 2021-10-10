
// 確認 登入狀態是否記住密碼
function check_login() {
    $.get('/login/check_login/',function (data) {
        // 將元素插入在第一個元素中
        $('.right-nav').html(load_login_msg(data))
    },'json')
}

function load_login_msg(data) {;
    let html = ''
    if(data.Login_Status == '1'){
        html += `<li>
                    <span class="user_login"> Hi : ${data.user_real_name}</span>
                </li>
                <li>
                    <b></b>
                    <a href="/login/sign_out">Sign out</a>
                </li>
                <li>
                    <b></b>
                    <a href="/login/user_member_center">會員中心</a>
                </li><li>
                <b></b>
                <a href="/shop_gbook">會員留言</a>
            </li>
            <li>
                    <b></b>
                    <a href="/shop_description">商城說明</a>
            </li>
            <li>
                <b></b>
                <a href="/shop_cart">
                    <img src="/static/images/shopingcart1.png">
                </a>
                <!-- 購物車商品數量                        -->
                <div class="user_cart_goods_amount">${data.user_cart_count}</div>       
            </li>
            <div class="search">
                <li>
                    <form>
                        <input name="Search" placeholder="Search" type="text">
                        <input type="submit" value="">
                    </form>
                </li>
            </div>`
            //  首頁登入,根據傳送的 login 訊息,將追蹤的商品 愛心換色
            // 獲取 追中的 goods_id heart login
            let user_track_goods_id_arry = JSON.parse(data.user_track_goods_id)
            //  獲取 所有 goods_id 的節點 hidden
            let goods_id_array = document.getElementsByName('goods_id')
            // 加載後 hidden 節點後做判斷 是否又點擊愛心顯示
            setTimeout(function () {
                goods_id_array.forEach(function (item1,index,array) {
                    user_track_goods_id_arry.forEach(function (item2,index,array) {
                        if(item1.value==item2){
                            item1.parentNode.children[1].children[1].setAttribute('class','heart click')
                            // 將兩個愛心 span 都變色
                            let heart_span = item1.parentNode.children[1].children[1].children
                            for(let i=0; i<heart_span.length;i++){
                                heart_span[i].style.background = 'red';
                            }
                        }
                    })
                })
            },50)
    }else if(data.Login_Status == '0'){
        html += `<li>
                    <a href="/login">Sign in</a>
                </li>
                <li>
                    <b></b>
                    <a href="/register">Register</a>
                 </li>
                <li>
                    <b></b>
                    <a href="/shop_description">商城說明</a>
                </li>
                <div class="search">
                    <li>
                        <form>
                            <input name="Search" placeholder="Search" type="text">
                            <input type="submit" value="">
                        </form>
                    </li>
                </div>`
    }
    return html
}



// 確認登入後 , 用戶購物車數量
// 必須先執行登入後,才執行確認購物車數量,否則會沒有登入的uid
// function user_cart_count() {
//     // 先判斷用戶是否登入,再確認用戶id 購物車數量
//     $.get('/login/check_login/',function (data) {
//         if(data.)
//     },'json')
// }
