from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

PACKAGE_NAME = 'com.goldze.mvvmhabit'

poco = AndroidUiautomationPoco()
poco.device.wake()
stop_app(PACKAGE_NAME)
start_app(PACKAGE_NAME)
auto_setup(__file__)

screenWidth,screenHeight = poco.get_screen_size()

viewed = []

current_count,last_count = len(viewed),len(viewed)

while True:
    last_count = len(viewed)
    result = poco('android.support.v7.widget.RecyclerView').child('android.widget.LinearLayout').child('android.widget.LinearLayout')
    result.wait(timeout=10)
    for item in result:
        text_view = item.child(type='android.widget.TextView')
        if not text_view.exists():
            continue
        name = text_view.get_text()
        if not name in viewed:
            viewed.append(name)
            print('name',name)
    current_count = len(viewed)
    print('开始滑动')
    poco.swipe([0.5,0.8],[0.5,0.2],duration=2)
    print('滑动结束')
    sleep(5)

    if current_count == last_count:
        print('数量不再变化，抓取结束')
        break
