// 設置 mobile 的 選單點擊効果
$(function () {
    //===========================index.html============ js 動態效果  =====

    //============================Banner  begin =======================
    // 1. Banner 透過引用 jquery.easyfader.min.js , 來設置Banner 樣式
    // 透過 easyFader  + base.css 來調整橫幅的顯示方式
    // $('#banner').easyFader();

    //============================= Baner end ===============================

    //============================ mobile nav begin ======================
    // 2. 設置 mobile-nav 的樣式, user 訪問網頁的 js 互動
    // 獲取 h2 節點
    var oH2 = $('h2');
    // 獲取 dl 選單列表節點
    var oUl = $('dl');

    // user click oH2 事件 , span 標籤 ,漢堡的時候出現的效果,將選單所有的菜單呈現
    oH2.click(function () {
        var style = oUl;
        style.display = style.display == 'block'? 'none':'block';
        style.display == 'block'?
            style.css('display','none') && oH2.removeClass('open'):
            style.css('display','block') && oH2.addClass('open');
    })


    // 以下為操作 mobile 裝置  的時候 要做的選單操作
    $('.list_dt').on('click',function () {
       $('.list_dd').stop();
       // 設置所有的 list_dt元素下,纇名為dt 的,刪除 id 屬性
       $(this).siblings('dt').removeAttr('id');
       $(this).siblings('.list_dt').children('.mobile_traingle').removeClass('open');
       $(this).attr('id')=='open'?
            //如果點擊第二次則,刪除id屬性,且將 屬性為'dd' 的收都回,
           // 且 刪除 子元素 .mobile_trangle 的 class='open' 三角標 樣式 三角形朝下
           $(this).removeAttr('id').siblings('dd').slideUp() && $(this).children('.mobile_traingle').removeClass('open'):
           // 如果點擊第一次, list_dt , attr 新增 id 屬性為 open , 且透過next 展開下一個兄弟元素 dd, 且將其他展開的'dd',屬性給收回,
           // 且新增 子元素 .mobile_trangle 的 class='open' 三角標 樣式 三角形朝上
           $(this).attr('id','open').next().slideDown().siblings('dd').slideUp() && $(this).children('.mobile_traingle').addClass('open');
    })

    // ====================== mobile - nav  end ================================




    //=============== 首頁商品、woman、men、kid、baby、sport js動態效果點擊 愛心顯示  begin  =====================
    // 利用點擊 div  class = heart 來判斷,點擊愛心的結果
    // $('.heart').click(function() {
    //     // 做 js 三元運算, 當第一次點擊時 class= heart open 且 背景色修改為紅色,
    //     // 如果是第二次點擊, 則會修改  class = heart , 變回原本背景色
    //     $(this).attr('class') == 'heart' ? $(this).addClass('open'):$(this).removeClass('open');
    //     $(this).attr('class') == 'heart open' ?
    //         $(this).children().css('background','red'):
    //         $(this).children().css('background','rgb(54, 64, 71)');
    // })

    //=============== 首頁商品、woman、men、kid、baby、sport js動態效果點擊 愛心顯示  end  =====================


    //  ===============動態加載數據,重新設置 click 愛心點擊事件 begin =======================================
    //       {# 因為動態加載頁面,重新處理點擊事件    #}
    //       {# 1.處理愛心點擊   #}
    $('#goods').on('click','.heart',function () {
        // {# 設置 $(this) 關鍵字,讓下面做判斷#}
        let click_heart = $(this)
                // {# 判斷用戶是否登入#}
        $.get('/login/check_login/',function (data) {
            if(data.Login_Status==1){

                // {# 獲取點擊的商品id#}
                let click_heart_id = click_heart.parent().next()
                let click_heart_img_url = click_heart_id.next()

                // {# 點擊後出現,確認框 (根據後端傳的 data.msg 值, 讓表單控件去判斷是移除還是新增)#}

                let params = {
                    'goods_id': click_heart_id.val(),
                }

                // {# 透過 $.get 方式,傳數據給後端 #}
                $.get('/login/api_track_goods',params,function (data) {
                    alert2(click_heart_img_url.val(),data.msg)
                },'json')

                // {# 商品id,點擊後展開 open 樣式 #}
                click_heart.attr('class') == 'heart' ?
                    click_heart.addClass('click'):
                    click_heart.removeClass('click');

                click_heart.attr('class') == 'heart click' ?
                click_heart.children().css('background','red'):
                click_heart.children().css('background','rgb(54, 64, 71)');





            }else if(data.Login_Status==0){
                alert('請先登入!才能將商品加入追蹤名單!');
                location.href = '/login'
            }
        },'json')
    })

    // ================= click heart event end ==================================



    // ============= 點擊 woman 、man 、 kid、 baby、  sport 列表 New Arrival 和 Top 選單變化 begin ========
    // 1. woman、man  主頁標籤
    $('.goods_list_dt').on('click',function () {
        $(this).next().stop();
        $(this).siblings('dt').removeAttr('id');
        $('.triangle').removeClass('open');
        if($(this).attr('id')=='open'){
            $(this).children('.triangle').removeClass('open');
            $(this).removeAttr('id').siblings('dd').slideUp();
        }else{
            $(this).attr('id','open').next().slideDown().siblings('dd').slideUp();
            $(this).children('.triangle').addClass('open');
        }
    });


    // 2.kid、 baby、sport 主頁 標籤
    $('.goods_list_dd .gender_type').click(function () {
        $(this).next().stop();
        $(this).siblings('.gender_type').removeAttr('id');
        $('.gender_type .triangle').removeClass('open');
        if($(this).attr('id')=='open'){
            $(this).children().children('.triangle').removeClass('open');
            $(this).removeAttr('id').siblings('.gender_type_kind').slideUp();
        }else{
            $(this).attr('id','open').next().slideDown().siblings('.gender_type_kind').slideUp();
            $(this).children().children('.triangle').addClass('open');
        }
    })


    // ============= 點擊 woman 、man 、 kid、 baby、  sport 列表 New Arrival 和 Top 選單變化 end ========



    // ============= 點擊  woman 、man 、 kid、 baby、  sport 列表 連接改變 商品內容 begin ==========
    // 1.( Woman 、 man  主頁 商品內容)
    var goods_title = $('#goods_title a');
    var goods_title_name = goods_title.text();

    //  1.點擊 New Arrival 、 Top  商品樣式改變 (連結)
    $('.goods_list_dt .goods_change').click(function () {
        $('.goods_change').removeAttr('id');
        $(this).attr('id','img_change');
        if($(this).attr('id')){
            if($(this).text() == 'New Arrival'){
                goods_title.text(goods_title_name+' > New Arrival');
            }else if($(this).text()== 'Top'){
                goods_title.text(goods_title_name+" > Top");
            }
        }
    })
    //    1.1 點擊 New Arrival 以下的 列表(Coats & Jackets 、 Clothes、 Trousers、 Blouse)
    $('.goods_list_dd .new_arrival').click(function () {
        if($(this).text()=='Coats & Jackets'){
        }else if ($(this).text()=='Clothes'){
            goods_title.text(goods_title_name +" > New Arrival > Clothes");
        }else if($(this).text()=='Trousers'){
            goods_title.text(goods_title_name +" > New Arrival > Trousers")
        }else if($(this).text()=='Blouse'){
            goods_title.text(goods_title_name +" > New Arrival > Blouse")
        }else  if($(this).text()=='Shirt'){
            goods_title.text(goods_title_name +" > New Arrival > Shirt")
        }
    })
    //    1.2 點擊 Top 以下的 列表(Coats & Jackets 、 Clothes、 Trousers、 Blouse)
    $('.goods_list_dd .top').click(function () {
        if($(this).text()=='Coats & Jackets'){
            goods_title.text(goods_title_name +" > Top > Coats & Jackets");
        }else if ($(this).text()=='Clothes'){
            goods_title.text(goods_title_name +" > Top > Clothes");
        }else if($(this).text()=='Trousers'){
            goods_title.text(goods_title_name +" > Top > Trousers");
        }else if($(this).text()=='Blouse'){
            goods_title.text(goods_title_name +" > Top > Blouse")
        }else  if($(this).text()=='Shirt'){
            goods_title.text(goods_title_name +" > Top > Shirt")
        }
    })

    //  2. 點擊 列表 Coats & Jackets 、 Clothes、 Trousers、 Blouse (連結)
    $('.goods_list_dt .other_goods').click(function () {
        if($(this).text()=='Coats & Jackets'){
            goods_title.text(goods_title_name +" > Coats & Jackets");
        }else if ($(this).text()=='Clothes'){
            goods_title.text(goods_title_name +" > Clothes");
        }else if($(this).text()=='Trousers'){
            goods_title.text(goods_title_name +" > Trousers")
        }else if($(this).text()=='Blouse'){
            goods_title.text(goods_title_name +" > Blouse")
        }else if($(this).text()=='Shirt'){
            goods_title.text(goods_title_name +" > Shirt")
        }

    })


    //================================ click 選單內容 左上地址修改 begin=======================================
    // 2. 點擊 ( kid 、baby 、 Sport主頁商品內容)
    //  1. New Arrival
    // ( KID 、 Baby )
    //     1.1  boy
    $('.goods_list_dd .gender_type_kind .boy_new_arrival ').click(function () {
        if($(this).text()=='Coats & Jackets'){
            goods_title.text(goods_title_name +" > New Arrival > boy's > Coats & Jackets");
        }else if ($(this).text()=='Clothes'){
            goods_title.text(goods_title_name +" > New Arrival > boy's > Clothes");
        }else if($(this).text()=='Trousers'){
            goods_title.text(goods_title_name +" > New Arrival > boy's > Trousers")
        }else  if($(this).text()=='Shirt'){
            goods_title.text(goods_title_name +" > New Arrival > boy's > Shirt")
        }
    })
    //     1.2  girl
    $('.goods_list_dd .gender_type_kind .girl_new_arrival').click(function () {
        if($(this).text()=='Coats & Jackets'){
            goods_title.text(goods_title_name +" > New Arrival > girl's > Coats & Jackets");
        }else if ($(this).text()=='Clothes'){
            goods_title.text(goods_title_name +" > New Arrival > girl's > Clothes");
        }else if($(this).text()=='Trousers'){
            goods_title.text(goods_title_name +" > New Arrival > girl's > Trousers")
        }else  if($(this).text()=='Shirt'){
            goods_title.text(goods_title_name +" > New Arrival > girl's > Shirt")
        }
    })


    //  2. Top
    //     2.1 boy
    $('.goods_list_dd .gender_type_kind .boy_top').click(function () {
        if($(this).text()=='Coats & Jackets'){
            goods_title.text(goods_title_name +" > Top > boy's > Coats & Jackets");
        }else if ($(this).text()=='Clothes'){
            goods_title.text(goods_title_name +" > Top > boy's > Clothes");
        }else if($(this).text()=='Trousers'){
            goods_title.text(goods_title_name +" > Top > boy's > Trousers")
        }else  if($(this).text()=='Shirt'){
            goods_title.text(goods_title_name +" > Top > boy's > Shirt")
        }
    })
    //     2.2 girl
    $('.goods_list_dd .gender_type_kind .girl_top').click(function () {
        if($(this).text()=='Coats & Jackets'){
            goods_title.text(goods_title_name +" > Top > girl's > Coats & Jackets");
        }else if ($(this).text()=='Clothes'){
            goods_title.text(goods_title_name +" > Top > girl's > Clothes");
        }else if($(this).text()=='Trousers'){
            goods_title.text(goods_title_name +" > Top > girl's > Trousers")
        }else  if($(this).text()=='Shirt'){
            goods_title.text(goods_title_name +" > Top > girl's > Shirt")
        }
    })



    // (Sport)

    //  1.New_arrival
    //      1. Men
    $('.goods_list_dd .gender_type_kind .Men_new_arrival ').click(function () {
        if($(this).text()=='Coats & Jackets'){
            goods_title.text(goods_title_name +" > New Arrival > Men's > Coats & Jackets");
        }else if ($(this).text()=='Clothes'){
            goods_title.text(goods_title_name +" > New Arrival > Men's > Clothes");
        }else if($(this).text()=='Trousers'){
            goods_title.text(goods_title_name +" > New Arrival > Men's > Trousers")
        }else  if($(this).text()=='Shirt'){
            goods_title.text(goods_title_name +" > New Arrival > Men's > Shirt")
        }
    })
    //      2. Women
    $('.goods_list_dd .gender_type_kind .Women_new_arrival').click(function () {
        if($(this).text()=='Coats & Jackets'){
            goods_title.text(goods_title_name +" > New Arrival > Women's > Coats & Jackets");
        }else if ($(this).text()=='Clothes'){
            goods_title.text(goods_title_name +" > New Arrival > Women's > Clothes");
        }else if($(this).text()=='Trousers'){
            goods_title.text(goods_title_name +" > New Arrival > Women's > Trousers")
        }else  if($(this).text()=='Shirt'){
            goods_title.text(goods_title_name +" > New Arrival > Women's > Shirt")
        }
    })


    //  2. Top
    //      1.Men
    $('.goods_list_dd .gender_type_kind .Men_top').click(function () {
        if($(this).text()=='Coats & Jackets'){
            goods_title.text(goods_title_name +" > Top > Men's > Coats & Jackets");
        }else if ($(this).text()=='Clothes'){
            goods_title.text(goods_title_name +" > Top > Men's > Clothes");
        }else if($(this).text()=='Trousers'){
            goods_title.text(goods_title_name +" > Top > Men's > Trousers")
        }else  if($(this).text()=='Shirt'){
            goods_title.text(goods_title_name +" > Top > Men's > Shirt")
        }
    })
    //     2. Women
    $('.goods_list_dd .gender_type_kind .Women_top').click(function () {
        if($(this).text()=='Coats & Jackets'){
            goods_title.text(goods_title_name +" > Top > Women's > Coats & Jackets");
        }else if ($(this).text()=='Clothes'){
            goods_title.text(goods_title_name +" > Top > Women's > Clothes");
        }else if($(this).text()=='Trousers'){
            goods_title.text(goods_title_name +" > Top > Women's > Trousers")
        }else  if($(this).text()=='Shirt'){
            goods_title.text(goods_title_name +" > Top > Women's > Shirt")
        }
    })




    // kid、baby、sport(共同的列表點選顯示)
    // 3. 點擊列表 Coats & Jackets 、 Clothes、 Trousers、 shirt
    //  3.1 、Coats & Jackets
    $('.goods_list_dd_coat_jackets ul li a').click(function () {
        if($(this).text()=="boy's"){
            goods_title.text(goods_title_name + " > Coats & Jackets > boy's ")
        }else if($(this).text()=="girl's"){
            goods_title.text(goods_title_name + " > Coats & Jackets > girl's ")
        }else if($(this).text()=="Men's"){
            goods_title.text(goods_title_name + " > Coats & Jackets > Men's ")
        }else if($(this).text()=="Women's"){
            goods_title.text(goods_title_name + " > Coats & Jackets > Women's ")
        }
    })
    //  3.2 Clothes
    $('.goods_list_dd_clothes ul li a').click(function () {
        if($(this).text()=="boy's"){
            goods_title.text(goods_title_name + " > Clothes > boy's ")
        }else if($(this).text()=="girl's"){
            goods_title.text(goods_title_name + " > Clothes > girl's ")
        }else if($(this).text()=="Men's"){
            goods_title.text(goods_title_name + " > Clothes > Men's ")
        }else if($(this).text()=="Women's"){
            goods_title.text(goods_title_name + " > Clothes > Women's ")
        }
    })
    //  3.3 Trousers
    $('.goods_list_dd_trousers ul li a').click(function () {
        if($(this).text()=="boy's"){
            goods_title.text(goods_title_name + " > Trousers > boy's ")
        }else if($(this).text()=="girl's"){
            goods_title.text(goods_title_name + " > Trousers > girl's ")
        }else if($(this).text()=="Men's"){
            goods_title.text(goods_title_name + " > Trousers > Men's ")
        }else if($(this).text()=="Women's"){
            goods_title.text(goods_title_name + " > Trousers > Women's ")
        }
    })
    //  3.4 shirt
    $('.goods_list_dd_shirt ul li a').click(function () {
        if($(this).text()=="boy's"){
            goods_title.text(goods_title_name + " > Shirt > boy's ")
        }else if($(this).text()=="girl's"){
            goods_title.text(goods_title_name + " > Shirt > girl's ")
        }else if($(this).text()=="Men's"){
            goods_title.text(goods_title_name + " > Shirt > Men's ")
        }else if($(this).text()=="Women's"){
            goods_title.text(goods_title_name + " > Shirt > Women's ")
        }
    })



    //================================ click 選單內容 左上地址修改 end=======================================


    // ================================ click 選單下的 filter 操作 begin =============================
    // 設置 filter 商品 span 標籤變化,及內容展開 (sort_by)
    // 1. sort_by
    $('#sort_by').click(function () {
        $('.filters_to_goods_Sort').attr('class')=='filters_to_goods_Sort'? $('.filters_to_goods_Sort').addClass('open'):$('.filters_to_goods_Sort').removeClass('open');
        $('.filters_to_goods_Sort').attr('class')=='filters_to_goods_Sort open'?
            $('.sort_choose').slideDown() && $('#sort_by').children('.icon').css('border','1px dashed #808080'):
            $('.sort_choose').slideUp() && $('#sort_by').children('.icon').css('border','none');
    })
    // 點選 filter 條件後 將 選單收回
    $('.sort_choose').click(function () {
        $('.sort_choose').slideUp();
        $(this).children().children('.radio-group').css('border','1px dashed black');
        // 因為 goods_detail 設置加入框線 所以這邊要設定,消除其他的 border
        $(this).children().children().siblings('.radio-group').css('border','none');
        $('#sort_by').children('.icon').css('border','none');
        $('.filters_to_goods_Sort').removeClass('open');
    })

    // 獲取點選的user 點選的值 將值輸出在畫面中
    $('.radio-group').click(function () {
        $(this).parent().parent().prev().children('.user_filter_goods').css('display','block').html($(this).children('.radio-label').text());
    })



    //2. size
    $('#size').click(function () {
        $(this).parent().attr('class')=='filters_to_goods'?$(this).parent().addClass('open'):$(this).parent().removeClass('open');
        $(this).parent().attr('class')=='filters_to_goods open'?
            $(this).next('.other_choose').slideDown() && $(this).children('.icon').css('border','1px dashed #808080'):
            $(this).next('.other_choose').slideUp() && $(this).children('.icon').css('border','none');
    })

    // 點選size 選單尺寸 顯示在畫面上
    $('.size_ul li').click(function () {
        $(this).css({'background':'#364047','color':'#EBEBEB'});
        $(this).siblings('li').addClass('open').css({'background':'#ffffff','color':'black'});
        $(this).parent().parent().prev().children('.user_filter_goods').css('display','block').html($(this).text());
    })


    // 3.Color
        $('#color').click(function () {
        $(this).parent().attr('class')=='filters_to_goods'?$(this).parent().addClass('open'):$(this).parent().removeClass('open');
        $(this).parent().attr('class')=='filters_to_goods open'?
            $(this).next('.other_choose').slideDown() && $(this).children('.icon').css('border','1px dashed #808080'):
            $(this).next('.other_choose').slideUp() && $(this).children('.icon').css('border','none');
    })


    // 點選 Color 選單衣服顏色樣式 顯示在畫面上
    $('.color_ul li').click(function () {
        $(this).css({'background':'#364047','color':'#EBEBEB'});
        $(this).siblings('li').addClass('open').css({'background':'#ffffff','color':'black'});
        $(this).parent().parent().prev().children('.user_filter_goods').css('display','block').html($(this).text());
    })

    //  點選 size 和 Color 選單值的變化(點選後收回選單)
    $('.other_choose').click(function () {
        $(this).slideUp();
        $(this).prev().children('.icon').css('border','none');
        $(this).parent().removeClass('open');
    })


    //4. clear all filter點擊  (清除所有) filter
    $('#Clear-all-filter').click(function () {
        // sort_by 的選單值清除
        var sort_by = $('.radio-group');
        sort_by.parent().parent().prev().children('.user_filter_goods').css('display','block').html('');
        //  利用 prop 設置所有的 checked = false ,
        $('#sort_by_frm .radio-group .radio_input').prop('checked', false);

        // size 的 選單清除
        var size = $('.size_ul li');
        size.parent().parent().prev().children('.user_filter_goods').css('display','block').html('');
        size.removeClass('open').css({'background':'#ffffff','color':'black'});

        // color 的 選單清除
        var color = $('.color_ul li');
        color.parent().parent().prev().children('.user_filter_goods').css('display','block').html('');
        color.removeClass('open').css({'background':'#ffffff','color':'black'});
    })


    // ================================ click 選單下的 filter 操作 end =============================



    // ===============根據選單點擊的值 做商品的排序  begin ========================================================

    // {# 根據 filter 去篩選 商品的樣式及價格排序 #}
    $('.radio-group .radio_input').click(function () {
        // {# 獲取 #goods ul li 的節點 做以下的filter 操作#}
        var goods_list_filter = $('#goods ul li')
        // {# 價格 由 低到高 #}
        if ($(this).val()=='LowtoHigh') {
            goods_list_filter.sort(function (a, b) {
                var goods_a = parseInt($(a).find('.price_order').val())
                var goods_b = parseInt($(b).find('.price_order').val())
                // {# 價格 由低到高 #}
                return goods_a < goods_b ? -1:1;
            })
            goods_list_filter.detach().appendTo('#goods ul')
        // {# 價格 由 高到低 #}
        }else if($(this).val()=='HightoLow'){
            goods_list_filter.sort(function (a, b) {
                var goods_a = parseInt($(a).find('.price_order').val())
                var goods_b = parseInt($(b).find('.price_order').val())
                // {# 價格 由高到低 #}
                return goods_a < goods_b ? 1:-1;
            })
            goods_list_filter.detach().appendTo('#goods ul')

        // {#  根據 hidden 的 愛心值 做排序(由多到少)  #}
        }else if($(this).val()=='Best Match'){
            goods_list_filter.sort(function (a,b) {
                var goods_a = parseInt($(a).find('.heartamount').val());
                var goods_b = parseInt($(b).find('.heartamount').val());
                // {# 由 愛心最多 到愛心最少 #}
                return goods_a < goods_b ? 1:-1;
            })
            goods_list_filter.detach().appendTo('#goods ul')
        // {#  根據 hidden 的 日期做排序 由最後上架優先  #}
        }else if($(this).val()=='Newest'){
            // {# 根據日期做排序 (排序做 三元運算 return 1 or -1) 由日期最新 到日期最小#}
            goods_list_filter.sort(function (a,b) {
                return $(a).find('.putondate').val() > $(b).find('.putondate').val() ? -1:1;
            })
            goods_list_filter.detach().appendTo('#goods ul')
        }
    })


    //// ===============根據選單點擊的值 做商品的排序 order by end ========================================================





    // ===================== user-cart- box 設置 begin ==========================================


    // 設置打開 user-cart- box 三角標樣式
    $('.open-close').click(function () {
        // 獲取 購物車 li 元素共有多少個,決定修改 .user-cart-list 的樣式
        let cart_count = $('.insert_cart_goods li').length

        // 下列做三元式判斷,購物車商品
        cart_count >= 3 ?
        //   如果購物車商品超過3個,則出現可下拉式的 scroll
        $('.user-cart-list').css('height','470px').css('overflow','auto'):
        $('.user-cart-list').css('height','').css('overflow','');

        $(this).children().attr('class') == 'open-triangle'?
            $(this).children().addClass('open') && $('.user-cart-list').slideDown() && $('#buy_goods').css('display','block'):
            $(this).children().removeClass('open') && $('.user-cart-list').slideUp() && $('#buy_goods').css('display','none');
    })


    // // 設置 當鼠標滑到移動 圖片 li 時,顯示 刪除按鈕
    //
    // $('.insert_cart_goods li').mouseover(function () {
    //     $(this).children('.delet-cart-goods').css('display','block').css('transition','all 0.7s');
    // })
    //
    // // 設置 當鼠標移出 圖片 li , 刪除按鈕消失
    // $('.insert_cart_goods li').mouseout(function () {
    //     $(this).children('.delet-cart-goods').css('display','none').css('transition','all 0.7s');
    // })

    // 因為是動態加載元素,所以要重新設置綁定事件,滑鼠移入圖片顯示 刪除的 button 按鈕
    $('.insert_cart_goods').on('mouseover','li',function () {
        $(this).children('.delet-cart-goods').css('display','block').css('transition','all 0.7s');
    })

    $('.insert_cart_goods').on('mouseout','li',function () {
        $(this).children('.delet-cart-goods').css('display','none').css('transition','all 0.7s');
    })



    //================================= usercart end ===============================================



    // ====================== /goods_detail 點擊相關事件  begin ===================================

    // click other_goods_img_change li 中 圖片後, 將 '.goods_detail_img' 的獲取網址位置修改成小圖的圖片
    // $('.other_goods_img_change li').click(function () {
    //     var img_src = $(this).children().attr('src');
    //     $('.goods_detail_img img').attr('src',img_src);
    // })

    // 因為動態加載 所以要修改
    $('.goods_detail_main').on('click','.other_goods_img_change li',function () {
        var img_src = $(this).children().attr('src');
        $('.goods_detail_img img').attr('src',img_src);
    })



    // 因為動態加載 需要再增加點擊事件

    // color 設置點擊 樣式改變
    $('.radio-label').click(function () {
        $(this).children('.radio-button').css('border','1px solid black');
        $(this).parent().css('border','1px dashed black');
        $(this).parent().parent().siblings('.radio-group').children('.click_color_border').children('.radio-label').children('.radio-button').css('border','1px solid #a8a0a0');
        $(this).parent().parent().siblings('.radio-group').children('.click_color_border').css('border','none');
    })
    // ============================== click size & Fit 事件 begin ==================================
    // 點擊 size & Fit
    $('#size_fit').click(function () {
        $(this).attr('class')=='size_fit open'?
            $(this).removeClass('open') && $(this).next().slideUp():
            $(this).addClass('open') && $(this).next().slideDown().parent().siblings('.goods_other_detail_list').children('button').removeClass('open').next('.detail_info').slideUp();
    })

    // 點擊 detail_material
    $('#detail_material').click(function () {
        $(this).attr('class')=='detail_meterial open'?
            $(this).removeClass('open') && $(this).next().slideUp():
            $(this).addClass('open') && $(this).next().slideDown().parent().siblings('.goods_other_detail_list').children('button').removeClass('open').next('.detail_info').slideUp();
    })

    // ============================== 點擊 click & Fit 事件 end ==================================

    // ============= 詳細商品資訊 點選頁面切換 begin ============================

    // button 1.size 2.how to measure
    $('.btn_Description').click(function () {
        $(this).parent().siblings('div').css('display','none');
        $(this).css('color','black').siblings('button').css('color','#939597');
        $(this).css('border','2px dashed black').siblings('button').css('border','none');
        if($(this).text()=='Size & Fit'){
            $('.size_table').css('display','block');
        }else if($(this).text()=='How to measure'){
            $('.how_to_measure').css('display','block');
        }
    })

    // ============= 詳細商品資訊 點選頁面切換 end ============================

    // ====================== /goods_detail 點擊相關事件  end ===================================


// ============================= 詳細商品點擊顏色後 商品圖片改變 begin======================================
    $('.click_color_border').click(function () {
        let color = '';
        let goods_id = '';
        color = $(this).children('.goods_color').val();
        goods_id = $(this).children('.goods_id').val();
        // {# 設置get 傳送過去的 值  #}
        let dic = {
            'Goods_id': goods_id,
            'color': color,
        }
        // {# 透過發送 $.get 獲取 顏色相關圖片 #}
        $.get('/shop_goods_detail/ajax_goods_color_change_msg',dic,function (data) {
            // 將顯示的小圖圖片 改變
            $('.other_goods_img_change').html(load_chang_color_data(data));
        },'json')
    })


    function load_chang_color_data(data) {
        let show = '';
        $.each(data,function (index,obj) {
            show += `<li>
                       <img src="/${obj.fields.goods_color_img_1}">
                     </li>
                     ${obj.fields.goods_color_img_2 ? '<li><img src="/'+ obj.fields.goods_color_img_2 + '"></li>':''}
                     ${obj.fields.goods_color_img_3 ? '<li><img src="/'+ obj.fields.goods_color_img_3 + '"></li>':''}
                     ${obj.fields.goods_color_img_4 ? '<li><img src="/'+ obj.fields.goods_color_img_4 + '"></li>':''}
                     ${obj.fields.goods_color_img_5 ? '<li><img src="/'+ obj.fields.goods_color_img_5 + '"></li>':''}
                     `
            // 商品圖修改
            $('.goods_detail_img img').attr('src','/' + obj.fields.goods_color_img_1);
            // 標籤顏色修改
            $('.goods_shown').html('Shown In ' + obj.fields.goods_color)
        })
        return show
    }


// ============================= 詳細商品點擊顏色後 商品圖片改變 end======================================

    //============ 返回頂部 動態效果 =========================================================
    // 設置返回頂部的鏈接,剛滑鼠滾到對應的 x y 軸位置
    var offset = 300,
        offset_opacity =1200,
        scroll_top_duration=700,
        $back_to_top = $('.cd-top');
    $(window).scroll(function () {
        ($(this).scrollTop()>offset) ? $back_to_top.addClass('cd-is-visible'):$back_to_top.removeClass('cd-is-visible cd-fade-out');
        if($(this).scrollTop()>offset_opacity){
            $back_to_top.addClass('cd-fade-out');
        }
    })
    $back_to_top.on('click',function (event) {
        event.preventDefault();
        $('body,html').animate({
            scrollTop: 0,
        }, scroll_top_duration);
    })
})

// ====================================================================================

// 1. 設置 處理 $.get 方法請求到數據後做模板的處理(封裝程函數 load_goods_template)
// 設置 透過 es6 模板方法 讓參數將數據返回

//  1.加載 母列表(數據模板 ALL_GOODS, New_Arrival、 Top 、 Coat&jackets 、Toursers、Clothes、Shirt、shirt、Blouse)
function load_goods_template(data) {
    var show = '';
    $.each(data,function (index,obj) {
        show += `<li>
                    <p>
                        <a href="/shop_goods_detail?GOODS_ID=${obj.pk}">
                            <img src="/${obj.fields.Images_url}">
                        </a>
                    </p>
                    <div class="content">
                        <a href="/shop_goods_detail?GOODS_ID=${obj.pk}">
                            <img src="/static/images/shopingcart1.png">
                        </a>
                        <div class="heart">
                            <span class="heart1"></span>
                            <span class="heart2"></span>
                        </div>
                        <p class="good_desc">
                            <b>${obj.fields.title}</b>
                        </p>
                        <span class="good_price"> 
                            NT$ : ${price_change(obj.fields.price)}
                        </span>
                        <input type="hidden" class="heartamount" value="${obj.fields.heart}">
                        <input type="hidden" class="putondate" value="${obj.fields.goods_put_on}">
                        <input type="hidden" class="price_order" value="${obj.fields.price}">
                    </div>
                    <input type="hidden" name="goods_id" value="${obj.pk}">
                    <input type="hidden" name="goods_img_url" value="/${obj.fields.Images_url}">
                </li>`;
    })
    return show
}

//  2.加載母列表下的數據 (New_Arriva (Coat & jackets、 Tousers、Clothes、Shirt、Blouse), Top(Coat & jackets、 Tousers、Clothes、Shirt、Blouse)......)
function load_goods_chirdren_template(obj) {
    var show = '';
    show += `<li>
                <p>
                    <a href="/shop_goods_detail?GOODS_ID=${obj.pk}">
                        <img src="/${obj.fields.Images_url}">
                    </a>
                </p>
                <div class="content">
                    <a href="/shop_goods_detail?GOODS_ID=${obj.pk}">
                        <img src="/static/images/shopingcart1.png">
                    </a>
                    <div class="heart">
                        <span class="heart1"></span>
                        <span class="heart2"></span>
                    </div>
                    <p class="good_desc">
                        <b>${obj.fields.title}</b>
                    </p>
                    <span class="good_price"> 
                        NT$ : ${price_change(obj.fields.price)}
                    </span>
                    <input type="hidden" class="heartamount" value="${obj.fields.heart}">
                    <input type="hidden" class="putondate" value="${obj.fields.goods_put_on}">
                    <input type="hidden" class="price_order" value="${obj.fields.price}">
                </div>
                <input type="hidden" name="goods_id" value="${obj.pk}">
                <input type="hidden" name="goods_img_url" value="/${obj.fields.Images_url}">
            </li>`;
    return show
}

// 寫函數 將價格透過 toLocaleString 轉換成進位逗號格式
function price_change(price){
    return parseInt(price).toLocaleString()
}



//===================================== 商品介面 和詳細介面商品 加載 Your cart 介面 ========= begin ===========
// 2. 設置user 點擊頁面 user_cart 展開的load 商品數量及數據
// {# user_cart 中,的商品數據#}
function load_user_cart_data() {
    let params = {
        'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
    }
    $.post('/shop_cart/query_goods_in_cart/',params, function (data) {
        let show_user_cart = ''
        if(data.user_cart_status==0){
            show_user_cart +=`<h3 style="font-size: 15px; color: #0f1452; font-weight: bold">Your Cart is Empty</h3>`
        }else if(data.user_cart_status==1){
            // 將數據內的 data.user_cart_msg 轉成 json 物件對象
            let user_cart_msg = JSON.parse(data.user_cart_msg)
            // 再透過 $.each 遍歷出商品資訊,組user_cart 模板資訊
            $.each(user_cart_msg,function (index,obj) {
                show_user_cart += `<li>
                                      <div class="user_cart_info_content">
                                        <span class="user_cart_size">${obj.fields.goods_size}</span>
                                        <span class="user_cart_amount">${obj.fields.goods_amount}</span>
                                        <!-- 利用上面的方法,做價格處理                                     -->
                                        <span class="user_cart_price">${price_change(obj.fields.goods_price)}</span>
                                      </div>
                                      <a href="/shop_goods_detail?GOODS_ID=${obj.fields.goods}&GOODS_COLOR=${obj.fields.goods_color}">
                                            <img src="${obj.fields.goods_img_url}">
                                      </a>  
                                      <!--  獲取用戶點擊的當前節點                                    -->
                                      <button class="delet-cart-goods" onclick="delet_goods(this,${obj.fields.goods_amount})">Delete</button>
                                        <!-- 設置 color、goods_id、size、amount 讓用戶點選 butoon 後 ,後端處理刪除 -->
                                      <input type="hidden" name="color" value="${obj.fields.goods_color}">
                                      <input type="hidden" name="cart_goods_id" value="${obj.fields.goods}">
                                      <input type="hidden" name="size" value="${obj.fields.goods_size}">
                                      <input type="hidden" name="amount" value="${obj.fields.goods_amount}">
                                    </li>`
            })
        }else if(data.user_cart_status==2){
            let user_cart_box_node = document.getElementById('wrapper').children[3]
            document.getElementById('wrapper').removeChild(user_cart_box_node)
        }
        $('.insert_cart_goods').html(show_user_cart);
    },'json')
}
// 點擊刪除後刪除節點當前 li 節點
function delet_goods(obj,amount){

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
            alert('刪除商品成功!',4)
        }else if(data.delete_user_goods_status==0){
            alert('刪除商品失敗!',4)
        }
    },'json')


    // 購物車節點刪除
    // 2.點擊後刪除,onclick 節點 button 的 父元素 li
    let delete_li = obj.parentNode
    let li_parent = document.getElementById('insert_cart_goods')
    li_parent.removeChild(delete_li)

    // 購物車數量減少
    // 3.獲得參數 amount ,減去購物車的數量
    let user_cart_old_amount = parseInt(document.getElementsByClassName('user_cart_goods_amount')[0].innerText)
    let user_cart_new_amount = document.getElementsByClassName('user_cart_goods_amount')[0]
    // 減去 用戶點選商品數量
    user_cart_new_amount.innerText = user_cart_old_amount-amount

    // 當減去 購物車　li 元素,判斷數量來設置 user_cart_box 樣式, 設置 setTimeout , 來解決 js非同步問題
    setTimeout(function () {
        // 設置 li_length 數量
        let li_length = $('.insert_cart_goods li').length
        let show_user_cart = '';
        // 如果 購物車商品數量 < 2 , 則修改樣式
        if(li_length == 2){
            // 如果數量 == 3 則 修改樣式
            $('.user-cart-list').css('height','').css('overflow','');
        }else if(li_length==0){
            // 如果等於0,則插入節點
            show_user_cart +=`<h3 style="font-size: 15px; color: #0f1452; font-weight: bold">Your Cart is Empty</h3>`
             $('.insert_cart_goods').html(show_user_cart)
        }
    },50)
}

//===================================== 商品介面 和詳細介面商品 加載 Your cart 介面 ========= end ===========


// ====================================== 加載 login 後的,愛心訊息 (針對點擊個別GoodsType2欄位) begin=============
//  加載 login 後的,愛心訊息 (針對點擊個別GoodsType2欄位)
function track_goods_msg(login_track_goods){
    let user_track_goods_id_arry = login_track_goods
    //  獲取 所有 goods_id 的節點 hidden
    let goods_id_array = document.getElementsByName('goods_id')
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
}


// ====================================== 加載 login 後的,愛心訊息 (針對點擊個別GoodsType2欄位) end=============