// 利用原生 的 js 設計彈框的樣式,註冊彈框
window.confirm =  confirm

function confirm(img_url,goods_name,goods_price,color,size,mount,color_img,resCallback) {

    // 1. 設置 confirm 節點,透過引用傳參給元素內值
    // 設置最外層
    let confirm_div = document.createElement('div');
    // 上層
    let confirm_div2 = document.createElement('div');
    // 上層span
    let confirm_div2_span = document.createElement('span');
    let confirm_div2_span_text = document.createTextNode('Add this product to the shopping cart ?');


    // 中間 (div 內容)
    let confirm_div_goods_content = document.createElement('div');


    // 商品提示內容
    // 1. goods_name
    let confirm_goods_name_h2 = document.createElement('h2')
    let confirm_goods_name_h2_text = document.createTextNode(goods_name)

    // 2. goods_price
    let confirm_goods_price_p = document.createElement('p')
    let confirm_goods_price_text = document.createTextNode('NT$: ' + (parseInt(goods_price).toLocaleString()))

    // 3. goods_size
    let confirm_goods_size_p = document.createElement('p')
    let confiim_goods_size_text = document.createTextNode('Size: ')
    let confirm_goods_size_span = document.createElement('span')
    let confirm_goods_size_span_text = document.createTextNode(size)


    // 4. goods_color
    let confirm_goods_color_p = document.createElement('p')
    let confirm_goods_color_text = document.createTextNode("Color: " + color)
    let confirm_goods_color_img_url = document.createElement('span')

    // 5. goods_amount
    let confirm_goods_amount_p = document.createElement('p')
    let confirm_goods_amount_text = document.createTextNode('Amount: ' + mount + '件')


    // 6. goods_total_price
    let confirm_goods_total_price_p = document.createElement('p')
    // // 將 price 和 數量做加總
    let confirm_goods_total_price_text = document.createTextNode('Total-Price : NT$:  ' + (parseInt(goods_price) * parseInt(mount)).toLocaleString())

    // 3.img
    // img 內容
    let confirm_div_goods_img = document.createElement('div');
    let confirm_goods_img = document.createElement('img')
    confirm_goods_img.setAttribute('src',img_url)


    // 4.hr 消除浮動
    let hr = document.createElement('hr')
    hr.style.clear='both'
    hr.style.margin='0px'

    // 確認按鈕
    // 按鈕
    let confirm_correct_btn = document.createElement('button')
    // 按鈕文字 設置
    let confirm_btnText = document.createTextNode("YES")


    // 取消按鈕
    let confirm_cancel_btn = document.createElement('button')
    let confirm_cancel_text = document.createTextNode('NO')


    // 2. 插入創建的節點
    // 將設置的節點遷入到 父元素中

    // 1. 標題(是否將商品加入到購物車中)
    // 將 span_text 元素遷入到 span 中
    confirm_div2_span.appendChild(confirm_div2_span_text);
    // 將 div2_span 遷入到 div2 中
    confirm_div2.appendChild(confirm_div2_span);

    // goods_content 內容:
    // 1. goods_name
    // 將 goods_name_text 遷入
    confirm_goods_name_h2.appendChild(confirm_goods_name_h2_text)



    // 2. goods_size

    confirm_goods_size_p.appendChild(confiim_goods_size_text)
    confirm_goods_size_span.appendChild(confirm_goods_size_span_text)
    confirm_goods_size_p.appendChild(confirm_goods_size_span)


    // 3. goods_color
    confirm_goods_color_p.appendChild(confirm_goods_color_text)
    confirm_goods_color_p.appendChild(confirm_goods_color_img_url)


    // 4. goods_price
    // 將 goods_price 嵌入
    confirm_goods_price_p.appendChild(confirm_goods_price_text)
    // 5. goods_mount
    confirm_goods_amount_p.appendChild(confirm_goods_amount_text)
    // 6. goods_total_price
    confirm_goods_total_price_p.appendChild(confirm_goods_total_price_text)


    // goods img 內容
    // 將 商品名稱遷入到 p 元素中
    // 將 img 元素嵌入到 p 元素中
    confirm_div_goods_img.appendChild(confirm_goods_img);



    // 將 商品名稱 遷入到 div_goods_content 容器中
    // goods_name
    confirm_div_goods_content.appendChild(confirm_goods_name_h2)

    // goods_size、goods_color
    confirm_div_goods_content.appendChild(confirm_goods_size_p)
    confirm_div_goods_content.appendChild(confirm_goods_color_p)

    //goods_price、goods_amount、goods_totla_price
    confirm_div_goods_content.appendChild(confirm_goods_price_p)
    confirm_div_goods_content.appendChild(confirm_goods_amount_p)
    confirm_div_goods_content.appendChild(confirm_goods_total_price_p)





    // 確認按鈕
    confirm_correct_btn.appendChild(confirm_btnText);
    // 取消按鈕
    confirm_cancel_btn.appendChild(confirm_cancel_text);


    // 將上列元素遷入到 div 中
    // 1. 是否加入購物車提示
    confirm_div.appendChild(confirm_div2)
    // 2. 插入圖片 div
    confirm_div.appendChild(confirm_div_goods_img)
    // 3. 加入商品內容
    confirm_div.appendChild(confirm_div_goods_content)

    confirm_div.appendChild(hr)
    // 3. 確認按鈕
    confirm_div.appendChild(confirm_correct_btn)
    // 4. 取消按鈕
    confirm_div.appendChild(confirm_cancel_btn)

    document.getElementsByTagName("body")[0].appendChild(confirm_div);


    // 綁定點擊事件
    //  取消事件點擊
    confirm_cancel_btn.onclick = function(){
        // 如果點擊取消 就將 整個div 刪除
        // confirm_div 父元素中的子元素為 confirm_div
        confirm_div.parentNode.removeChild(confirm_div);
        // 點擊後,返回顯示頁面
        document.getElementsByClassName('wrapper')[0].style.opacity="1";

        // 當用戶點擊確認框事件後,將 disabled 屬性移除
        send_goods_msg_btn.removeAttribute('disabled')
        resCallback({
            'status':false,
        })
    }

    confirm_correct_btn.onclick = function(){
        confirm_div.parentNode.removeChild(confirm_div);
        // 點擊後,返回顯示頁面
        document.getElementsByClassName('wrapper')[0].style.opacity="1";

        // 當用戶點擊確認框事件後,將 disabled 屬性移除
        send_goods_msg_btn.removeAttribute('disabled')
        resCallback({
            'status':true,
        })
    }



    // 控制樣式 div 最外層大容器
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

    // 控制樣式 div2 span 標題容器
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


    // 商品敘述內容容器 div
    css(confirm_div_goods_content,{
        "float":"left",
        "font-weight":"bold",
        "text-align":"left",
        "padding":"1.0rem .5rem 0rem .5rem",
        "position":"relative",
        "right":"40px",
    });

    // 1. 商品標題
    css(confirm_goods_name_h2,{
        "font-size":".9rem",
        "font-weight":"bold",
        "color":"#091632",
        "margin-bottom":"30px"
    })

    // 2.商品 size
    css(confirm_goods_size_p,{
        "font-size":".9rem",
        "color":"#091632",
        "margin-bottom":"5px",
    })
    //  size span 顯示樣式
    css(confirm_goods_size_span,{
        "color":"white",
        "width":"32px",
        "height":"20px",
        "background":"rgb(54, 64, 71)",
        "font-weight":"bold",
        "display":"inline-block",
        "text-align":"center",
        "border-radius":"4px",
        "margin-left":"10px",
    })


    // 3. 商品顏色
    css(confirm_goods_color_p,{
        "font-size":".9rem",
        "color":"#091632",
        "margin-bottom":"30px",
    })
    //  彈框顯示,選擇的商品顏色小圖
    css(confirm_goods_color_img_url,{
        "background": color_img,
        "width":"20px",
        "height":"20px",
        "border-radius":"50%",
        "display": "inline-block",
        "position":"relative",
        "top":"7px",
        "right":"-10px",
        "border":"1px dashed black",
    })



    // 4.商品價格
    css(confirm_goods_price_p,{
        "font-size":".9rem",
        "color":"#091632",
        "margin-bottom":"5px",
    })

    // 5. 商品數量
    css(confirm_goods_amount_p,{
        "font-size":".9rem",
        "color":"#091632",
        "margin-bottom":"5px",
    })

    // 6. 商品總價鉻
    css(confirm_goods_total_price_p,{
        "font-size":".9rem",
        "color":"#091632",
        "margin-bottom":"20px",
    })


    // 商品內容樣式
    // 商品圖片容器 div
    css(confirm_div_goods_img,{
        "float": "left",
        "width": "40%",
        "margin":"15px 50px 10px 0px",
    })
    // 商品圖片樣式
    css(confirm_goods_img,{
        "width":"80%",
        "border-radius" : "10px",
        "margin-left":"1.5rem"
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

    css(confirm_cancel_btn,{
        "cursor": "pointer",
        "color":"white",
        "background":"#0c1b40",
        "margin":"10px 5px 5px 5px",
        "width": "80px",
        "height": "25px",
        // "outline":"none",
        "border":"none",
        "font-weight":"bold",
        "border-radius" : "5px",
    });

    function css(targetObj,cssobj) {
        for(var i in cssobj){
            targetObj.style[i] = cssobj[i];
        }
    }

    document.getElementsByClassName('wrapper')[0].style.opacity="0.3";

    //設置對象
    let send_goods_msg_btn = document.getElementById('send_goods_msg')
    send_goods_msg_btn.setAttribute("disabled","disabled")
}


