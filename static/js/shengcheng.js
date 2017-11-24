$(function () {
    var oExports = {
        initialize: fInitialize,
        encode: fEncode
    };
    oExports.initialize();

    function fInitialize() {
        var that = this;
        $("#down").hide();
        $(".content2-agile").hide();

        var sImageId = window.imageId;
        var oCmtIpt = $('#message');
        var oListDv = $('ul.js-discuss-list');


        // 点击添加评论
        var bSubmit = false;
        $('#btn').on('click', function () {
         $('#images').attr("src","")
         $('#images').attr("alt","加载中...")
            var sCmt = $.trim(oCmtIpt.val());
            //获取的值


            if (!sCmt) {
                return alert('填写不能为空');
            }
            // 上一个提交没结束之前，不再提交新的评论
            if (bSubmit) {
                return;
            }
            bSubmit = true;
            $.ajax({
                url: '/shengcheng_image/',
                type: 'post',
                dataType: 'json',
                data: {message:sCmt ,}
            }).done(function (oResult) {
                if (oResult.code !== 0) {
                    return alert(oResult.msg || '提交失败，请重试');
                }
                // 清空输入框
//                oCmtIpt.val('');
                // 渲染新的评论
                    $(".content2-agile").show();
                $('#images').attr("src",that.encode(oResult.images))


                $('#pic1').attr("href",that.encode(oResult.images))

                 $('#pic1').attr("download",that.encode(oResult.images))
                  $("#down").show();

            }).fail(function (oResult) {
                alert(oResult.msg || '提交失败，请重试');
            }).always(function () {
                bSubmit = false;
            });
        });
    }

    function fEncode(sStr, bDecode) {
        var aReplace =["&#39;", "'", "&quot;", '"', "&nbsp;", " ", "&gt;", ">", "&lt;", "<", "&amp;", "&", "&yen;", "¥"];
        !bDecode && aReplace.reverse();
        for (var i = 0, l = aReplace.length; i < l; i += 2) {
             sStr = sStr.replace(new RegExp(aReplace[i],'g'), aReplace[i+1]);
        }
        return sStr;
    };

});