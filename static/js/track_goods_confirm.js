// 加入追蹤清單,確認框
function alert2(goods_img,msg) {

    // 1. 設置 confirm 節點,透過引用傳參給元素內值
    // 設置最外層
    let confirm_div = document.createElement('div');
    // 上層
    let confirm_div2 = document.createElement('div');
    // 上層span
    let confirm_div2_span = document.createElement('span');

    // 如果是為新增要新增,則詢問是否要加入清單中
    let confirm_div2_span_text = ''

    if(msg==1){
        confirm_div2_span_text = document.createTextNode('已將商品加入追蹤清單!');
    }else if(msg==2){
        confirm_div2_span_text = document.createTextNode('已將商品移除追蹤清單!');
    }



    // 中間 (div 內容)
    let confirm_div_goods_content = document.createElement('div');


    // // 3.img
    // // img 內容
    let confirm_div_goods_img = document.createElement('div');
    let confirm_goods_img = document.createElement('img')
    confirm_goods_img.setAttribute('src',goods_img)


    // 4.hr 消除浮動
    let hr = document.createElement('hr')
    hr.style.clear='both'
    hr.style.margin='0px'
    //
    // // 確認按鈕
    // // 按鈕
    let confirm_correct_btn = document.createElement('button')
    // 按鈕文字 設置
    let confirm_btnText = document.createTextNode("YES")



    // // 2. 插入創建的節點
    // // 將設置的節點遷入到 父元素中
    //
    // // 1. 標題(是否將商品加入到購物車中)
    // // 將 span_text 元素遷入到 span 中
    confirm_div2_span.appendChild(confirm_div2_span_text);
    // 將 div2_span 遷入到 div2 中
    confirm_div2.appendChild(confirm_div2_span);
    //



    // // goods img 內容
    // // 將 商品名稱遷入到 p 元素中
    // // 將 img 元素嵌入到 p 元素中
    confirm_div_goods_img.appendChild(confirm_goods_img);
    //

    //
    // // 確認按鈕
    confirm_correct_btn.appendChild(confirm_btnText);

    //
    //
    // // 將上列元素遷入到 div 中
    // // 1. 是否加入購物車提示
    confirm_div.appendChild(confirm_div2)
    // 2. 插入圖片 div
    confirm_div.appendChild(confirm_div_goods_img)
    // 3. 加入商品內容
    confirm_div.appendChild(confirm_div_goods_content)

    confirm_div.appendChild(hr)
    // 3. 確認按鈕
    confirm_div.appendChild(confirm_correct_btn)

    //
    document.getElementsByTagName("body")[0].appendChild(confirm_div);
    //
    //


    confirm_correct_btn.onclick = function(){
        confirm_div.parentNode.removeChild(confirm_div);
        // 點擊後,返回顯示頁面
        document.getElementsByClassName('wrapper')[0].style.opacity="1";

    }
    //
    //
    //
    // // 控制樣式 div 最外層大容器
    css(confirm_div,{
        // 絕對定位
        "position":"fixed",
        "left": 0 ,
        "right": 0,
        "top":"20%",
        "width": "500px",
        // "height":"350px",
        "margin":"0 auto",
        "background":"#c6c2c2",
        "font-size":"20px",
        "z-index":"999999",
        "border-radius":"20px",
        "text-align":"center",
        "border":"2px solid black"
    });



    // // 控制樣式 div2 span 標題容器
    css(confirm_div2,{
        "width":"500px",
        "height":"50px",
        "background":"white",
        "border-radius":"20px 20px 0px 0px",
        "text-align":"left",
        "line-height": "55px",
        "border-bottom":"2px solid",
        "font-weight":"bold",

    })
    // 文本框樣式
    css(confirm_div2_span,{
        "padding-left":"35px",
    })
    //
    //
    // 商品敘述內容容器 div
    css(confirm_div_goods_content,{
        "float":"left",
        "font-weight":"bold",
        "text-align":"left",
        "padding":"1.0rem .5rem 0rem .5rem",
        "position":"relative",
        "right":"40px",
    });




    // 商品內容樣式
    // 商品圖片容器 div
    css(confirm_div_goods_img,{
        "width": "40%",
        "margin":"10px auto",
    })
    // 商品圖片樣式
    css(confirm_goods_img,{
        "width":"90%",
        "border-radius" : "10px",
        "border":"2px solid black"
    })



    // 設置點選的 button 樣式
    css(confirm_correct_btn,{
        "cursor": "pointer",
        "color":"white",
        "background":"#0c1b40",
        "margin":"10px 5px 5px 5px",
        "width": "80px",
        "height": "25px",
        "border":"none",
        "font-weight":"bold",
        "border-radius" : "5px",
    });


    function css(targetObj,cssobj) {
        for(let i in cssobj){
            targetObj.style[i] = cssobj[i];
        }
    }

    document.getElementsByClassName('wrapper')[0].style.opacity="0.3";
}