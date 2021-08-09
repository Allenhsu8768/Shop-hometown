// ============================ 設置住冊頁面加載 國家、地區 資訊  begin =======================

// {# 編寫 加載國家的 function #}
function load_country_msg() {
    var show = '';
    show += `<option value="-1"> ----Please Chose Your Country ----- </option>`
    $.get('/register/ajax_country_msg',function (data) {
        $.each(data,function (index,obj) {
            show += `<option value="${obj.pk}">${obj.fields.Country_name}
                    </option>`
        })
        $('#srm_country').html(show);
    },'json')
}

// 註冊驗證信箱頁面跳轉

// 根據 user 點擊的 國家 顯示 各自的地區
$(function () {
    // 1.============ 註冊功能  begin =========
    // ================= 根據點擊國家顯示各自的地區
    $('#srm_country').change(function () {
        var Counrty = {
            'Country':$(this).val()
        }
        var show = '';
        show += '<option value="-1"> ----Please Chose Your City ----- </option>'
        $.get('/register/ajax_city_msg',Counrty,function (data) {
            $.each(data,function (index,obj) {
                show += `<option value="${obj.pk}">${obj.fields.City_name}
                        </option>`
            })
            $('#srm_city').html(show);
        },'json')
    })
    // ===============================================================
    // 註冊 表單時必須進行的驗證
    // 設置 變量 registerStatus1 來 讓表單 去判斷 , 用戶如果已註冊,就不能將 註冊資訊送出
    let registerStatus1 = 0;
    // 設置 變量 registerStatus2 來讓表單判斷,用戶的email 不可以重複
    let registerStatus2 = 0;

    // 1. 帳號驗證(是否重複)

    $('#user_name').blur(function () {
        // 判斷如果失去焦點內容為空就不做任何動作
        if($(this).val().trim().length==0){
            // 當焦點失去沒有值的時候, 要刪除新增的class 屬性
            $('.check_user_name').attr('class','check_user_name');
            registerStatus1 = parseInt(3);
            return
        }

        // 如果輸入的 文本框有內容則做以下程序
        // 必須設置 csrf 驗證,才能通過 post ˇ請求獲得數據
        var params = {
            'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
            'user_name': $(this).val().trim(),
        }

        $.post('/register/post_user_name_msg/',params,function (data) {
            // 根據後端 送回來的信息做判斷 (Status==1 表示存在, Status ==0 表示不存在可以註冊)
            // 接收 data 的 Status 值
            // 透過 這個值去判斷 表單是否可以提交
            registerStatus1 = data.Status;

            if(data.Status =='1'){
                // 三元運算 必須要清掉 未修改前可能增加的樣式
                $('.check_user_name').attr('class') == 'check_user_name can_register'?
                    $('.check_user_name').removeClass('can_register'):$('.check_user_name').removeClass('not_register')
                $('.check_user_name').addClass('not_register');
            }else if(data.Status=='0'){
                // 獲取 div 標籤節點
                // 三元運算 必須要清掉 未修改前可能增加的樣式
                $('.check_user_name').attr('class') == 'check_user_name can_register'?
                    $('.check_user_name').removeClass('can_register'):$('.check_user_name').removeClass('not_register')
                $('.check_user_name').addClass('can_register');
            }
        },'json')
    })

    // 2. 驗證信箱是否重複
    $('#user_mail').blur(function () {
        // 判斷如果失去焦點內容為空就不做任何動作
        if($(this).val().trim().length==0){
            $('.check_user_email').attr('class') == 'check_user_email can_register'?
                $('.check_user_email').removeClass('can_register'):$('.check_user_email').removeClass('not_register')
            return
        }

        // 如果輸入的 文本框有內容則做以下程序
        // 必須設置 csrf 驗證,才能通過 post ˇ請求獲得數據
        var params = {
            'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
            'user_email': $(this).val().trim(),
        }

        $.post('/register/post_user_email_msg/',params,function (data) {
            // 根據後端 送回來的信息做判斷 (Status==1 表示存在, Status ==0 表示不存在可以註冊)
            // 接收 data 的 Status 值
            // 透過 這個值去判斷 表單是否可以提交
            registerStatus2 = data.Status;
            if(data.Status =='1'){
                $('.check_user_email').attr('class') == 'check_user_email can_register'?
                    $('.check_user_email').removeClass('can_register'):$('.check_user_email').removeClass('not_register')
                $('.check_user_email').addClass('not_register');
            }else if(data.Status=='0'){
                // 獲取 div 標籤節點
                $('.check_user_email').attr('class') == 'check_user_email can_register'?
                    $('.check_user_email').removeClass('can_register'):$('.check_user_email').removeClass('not_register')
                $('.check_user_email').addClass('can_register');
            }
        },'json')
    })

    // 表單提交時做的驗證
    $('.register_form').submit(function () {
        // 1. registerStatus1 = 1 的時候 ,用戶名稱重複
        if(registerStatus1==1){
            alert('用戶名稱已註冊, 請檢查!');
            return false
        // 2. registerStatus2 = 1 的時候, 信箱重複
        }else if(registerStatus1==3){
            alert('用戶名稱不可以空白!');
            return false
        }else if (registerStatus2==1){
            alert('用戶信箱已註冊, 請檢查!');
            return false
        // 3. 做確認密碼的動作
        }else if($('#pswd').val() != $('#check_pswd').val()){
            alert('密碼與確認密碼不相符,請檢查!');
            return false
        }else if($('#srm_country').val()=='-1'){
            alert('請選擇所在城市!');
            return false
        }else if($('#srm_city').val()=='-1' || $('#srm_city').val()=='-2'){
            alert('請選擇所在地區');
            return false
        }
        return true
    })

})
// ============================ 設置住冊頁面加載 國家、地區 資訊  end =======================