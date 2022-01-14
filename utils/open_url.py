import time
from selenium_pytest.utils.pil_image_similarity import image_similarity

file = open(r"E:\web\res.txt", "w+", encoding="utf-8")



def OpenUrl(t_browser, test_url, num):  #
    handle = t_browser.current_window_handle
    # 打开一个新的窗口
    t_browser.execute_script('window.open()')
    # 获取当前所有窗口句柄（窗口A、B）
    handles = t_browser.window_handles
    # 对窗口进行遍历
    for new_handle in handles:
        # 筛选新打开的窗口B
        if new_handle != handle:
            # 切换到新打开的窗口B
            t_browser.switch_to.window(new_handle)

    t_browser.get(test_url)
    time.sleep(12)

    t_browser.save_screenshot(r'E:\web\test_web%d.png' % num)
    f1 = r'E:\web\c' + str(num) + '.png'
    f2 = r'E:\web\t' + str(num) + '.png'
    r = image_similarity(f1, f2)
    file.write("开始计算图片差值："+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n")
    if r < 5000:
        file.write("图%d差值:" %num + str(r) + '\n')
    else:
        file.write("图%d差值:" %num + str(r) + '\n')
    t_browser.close()
    t_browser.switch_to.window(handles[0])
    return t_browser