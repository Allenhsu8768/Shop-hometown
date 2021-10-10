// 利用原生 的 js 設計彈框的樣式,註冊彈框
window.alert = alert

//  加入 login 時,調用 alert 函數參數,判斷是 login 啟用的 alert 還是 register
function alert(msg,errmsg=null) {

    // ===========================彈框節點設置 begin ======================
    // 最外層
    let alert_div = document.createElement('div');
    // 上層
    let alert_div2 = document.createElement('div');
    // 上層span
    let alert_div2_span = document.createElement('span');
    let alert_div2_span_text = '';
    // span 中的文字

    if(errmsg==null){
        alert_div2_span_text = document.createTextNode('註冊資料有誤!');
    //    登入錯誤問題 errmsg = 1
    }else if(errmsg==1){
        alert_div2_span_text = document.createTextNode('登入資料有誤!');
    //    商品有誤問題 errmsg = 3
    }else if(errmsg==3){
        alert_div2_span_text = document.createTextNode('選擇商品資料有誤!')
    }else if(errmsg==4){
        alert_div2_span_text = document.createTextNode('刪除商品資料!')
    }else if(errmsg==5){
        alert_div2_span_text = document.createTextNode('輸入商品數量有誤!')
    }else if(errmsg==6){
        alert_div2_span_text = document.createTextNode('資料輸入有誤!')
    }

    // 中間
    let alert_p = document.createElement('p');
    // 按鈕
    let alert_btn = document.createElement('button')
    // 提示內容文字 (根據 設置 alert 傳值 msg 做三元運算)
    let alert_textNode = document.createTextNode(msg ? msg:"");
    // 按鈕文字 設置
    let alert_btnText = document.createTextNode("確定")


    // 透過內部套入
    // p 中嵌入 文本內容
    alert_p.appendChild(alert_textNode);
    // btn 中嵌入按鈕文字
    alert_btn.appendChild(alert_btnText);

    // alert_div2_span 插入文字
    alert_div2_span.appendChild(alert_div2_span_text)
    // alert_div2 中插入span
    alert_div2.appendChild(alert_div2_span);

    // 將 alert_p 和 alert_btn 嵌入到 alert_div 中
    alert_div.appendChild(alert_div2);
    alert_div.appendChild(alert_p);
    alert_div.appendChild(alert_btn);


    // 整體顯示到頁面中
    document.getElementsByTagName("body")[0].appendChild(alert_div);

    //  ============================== 彈框節點設置 end ========================


    // 確認點擊綁定事件 (點選確認後要將彈窗整個刪除)
    alert_btn.onclick = function () {
        // 如果點擊確認 就將 整個div 刪除
        // alert_div 父元素中的子元素為 alert_div
        alert_div.parentNode.removeChild(alert_div);
        // 點擊後,返回顯示頁面
        document.getElementsByClassName('wrapper')[0].style.opacity="1";

        // 判斷 errmsg 來打開按鈕點擊
        if(errmsg==1){
            document.getElementById('send_login_msg').removeAttribute('disabled')
        }else if(errmsg==3){
            document.getElementById('send_goods_msg').removeAttribute("disabled")
        }else if(errmsg==null){
            document.getElementById('send_register_msg').removeAttribute("disabled")
        }else if(errmsg==4){
            // 購物車 小框頁面  delete
            // 獲取 頁面 delet-cart-goods 節點
            let delete_button = document.getElementsByClassName('delet_cart_goods')
            for(let i=0;i<delete_button.length;i++){
                delete_button[i].removeAttribute("disabled")
            }
        }else if(errmsg==5){
            // check cart _amount 數量, delete
            // 獲取頁面節點 delet_cart_goods
            let delete_buttin = document.getElementsByClassName('delet_cart_goods')
            for(let i=0; i<delete_buttin.length; i++){
                delete_buttin[i].removeAttribute('disabled')
            }
        }
    }

    // ===========彈框控制樣式 begin ===============================
    css(alert_div,{
        // 絕對定位
        "position":"fixed",
        "left": 0 ,
        "right": 0,
        "top":"20%",
        "width": "500px",
        "height":"250px",
        "margin":"0 auto",
        "background":"#c6c2c2",
        "font-size":"20px",
        "z-index":"999999",
        "border-radius":"20px",
        "text-align":"center",
        "border":"2px solid black"
    });

    css(alert_div2,{
        "width":"500px",
        "height":"50px",
        "background":"white",
        "border-radius":"20px 20px 0px 0px",
        "text-align":"left",
        "line-height": "55px",
        "border-bottom":"2px solid",
        "font-weight":"bold",

    })
    css(alert_div2_span,{
        "padding-left":"35px",
    })


    css(alert_p,{
        'line-height':"165px",
        "font-weight":"bold"
    });

    css(alert_btn,{
        "cursor": "pointer",
        "color":"white",
        "background":"#0c1b40",
        "margin":"0px 5px 5px 5px",
        "width": "80px",
        "height": "25px",
        "border":"none",
        "font-weight":"bold",
        "border-radius" : "5px",
    });

    function css(targetObj, cssobj) {
        for(var i in cssobj){
            targetObj.style[i] = cssobj[i];
        }
    }


    //=================彈框控制樣式 end ===============================

    // 彈框彈出後 , 背景透明度變化
    document.getElementsByClassName('wrapper')[0].style.opacity="0.3";

    // 判斷 errmsg , 根據 傳入的參數判斷鎖住哪個按鈕
    if(errmsg==null){
        document.getElementById('send_register_msg').setAttribute('disabled','disabled')
    }else if(errmsg==3){
        document.getElementById('send_goods_msg').setAttribute('disabled','disabled')
    }else if(errmsg==1){
        document.getElementById('send_login_msg').setAttribute('disabled','disabled')
    }else if(errmsg==4){
        let delete_button = document.getElementsByClassName('delet_cart_goods')
        for(let i=0;i<delete_button.length;i++){
            delete_button[i].setAttribute('disabled','disabled')
        }
    }else if (errmsg==5) {
        // check cart _amount 數量, delete
        // 獲取頁面節點 delet_cart_goods
        let delete_buttin = document.getElementsByClassName('delet_cart_goods')
        for (let i = 0; i < delete_buttin.length; i++) {
            delete_buttin[i].setAttribute('disabled','disabled')
        }
    }
}








