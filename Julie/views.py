from django.shortcuts import render, redirect

def index(req):
    ctx = {}
    base_path = "/static/image/"
    
    nav_link_ul = ["主站","番剧","游戏中心","直播","会员购","漫画","赛事","嘉年华","BML","下载APP","search","大会员","消息","动态","收藏","历史","创作中心","投稿"]
    ctx['nav_link_ul'] = nav_link_ul
    
    theme_ul = ["动画","音乐","舞蹈","知识","生活","时尚","娱乐","放映厅","番剧","国创","游戏","科技","鬼畜","资讯","影视","更多"]
    ctx['theme_ul'] = theme_ul
    
    func_ul = ["专栏","活动"," 小黑屋","直播","课堂","新歌热榜"]
    ctx['func_ul'] = func_ul
    
    video_img_ul = []
    for i in range(1, 7):
        video_img_ul.append(base_path + "video" + str(i) + ".jpg")
    ctx['video_img_ul'] = video_img_ul
    
    but_img_ul = []
    for i in range(1, 5):
        but_img_ul.append(base_path + 'button' + str(i) + '.jpg')
    but_title_ul = ['首页','动态','热门','频道']
    but_ul = []
    for img,title in zip(but_img_ul, but_title_ul):
        but_ul.append({'img':img,'title':title})
    ctx['but_ul'] = but_ul

    cnt_img_ul = []
    for i in range(1, 9):
        cnt_img_ul.append(base_path + 'lifevideo' + str(i) + '.jpg')
    cnt_title_ul = ['我在校园歌手大赛的那些年','【射箭之王】的确挺容易的。。。','【北航回忆】小小镜框承载青葱岁月','宝贝摩天轮捧在我手心【天津行】','【小可爱的古装之旅】宝 宝 大 变 身','最美不过遇见你','【淘气多】可可爱爱 米有脑袋~','爱在泥塑旁，爱在心坎里']
    cnt_author_ul = ['Julie','Julie','Julie','Julie','Julie','Julie','Julie','Julie']
    cnt_ul = []
    for img,title,author in zip(cnt_img_ul, cnt_title_ul, cnt_author_ul):
        cnt_ul.append({'img':img, 'title':title, 'author':author})
    ctx['cnt_ul'] = cnt_ul
    
    rank_img_ol = []
    for i in range(9, 19):
        rank_img_ol.append(base_path + 'lifevideo' + str(i) + '.jpg')
    rank_title_ol = ['歌唱小天后入驻B站！！！','最 强 仙 女','【4K60FPS】韩良越《被驯服的象》神级现场！','绝美！当小良越遇上国风舞','还在“笨猪”？北航学霸带你学法语','《 神 奇 小 猫 咪 》','【Julie宝宝】105°C的爱送给你们~','满足你对所有女友的幻想！yueyueCindy','九球天后Miss.Han的传奇人生','越越的奇妙冒险']
    rank_score_ol = ['9999.9万','9999.9万','9999.9万','9999.9万','9999.9万','9999.9万','9999.9万','9999.9万','9999.9万','9999.9万']
    rank_ol = []
    for img,title,score in zip(rank_img_ol, rank_title_ol, rank_score_ol):
        rank_ol.append({'img':img, 'title':title, 'score':score})
    ctx['rank_ol'] = rank_ol
    
    if req.POST and req.POST['keywords'] == '我的小宝宝最可爱':
        return redirect('letter/')
    
    return render(req, 'index.html', ctx)

def letter(req):
    ctx = {}
    
    return render(req, "letter.html", ctx)
