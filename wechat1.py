import pyautogui
import pyperclip
import time

# 预设的回复信息
reply_message = "等一会儿"

def locate_and_click(image, confidence=0.9, retries=5, interval=1):
    """
    尝试多次查找并点击图像。

    :param image: 图像文件名
    :param confidence: 图像匹配的置信度
    :param retries: 重试次数
    :param interval: 重试间隔（秒）
    :return: 是否成功点击
    """
    for attempt in range(retries):
        try:
            location = pyautogui.locateCenterOnScreen(image, confidence=confidence)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=1, interval=0.2, duration=0.2, button="left")
                print(f"成功点击图像: {image}")
                return True
            else:
                print(f"未找到图像: {image}，重试 {attempt + 1}/{retries}")
                time.sleep(interval)
        except pyautogui.ImageNotFoundException:
            print(f"图像查找失败: {image}")
            time.sleep(interval)
    return False

def send_reply():
    """
    在微信聊天窗口中输入并发送回复信息。
    """
    # 复制回复信息到剪贴板
    pyperclip.copy(reply_message)
    # 模拟 Ctrl+V 粘贴
    pyautogui.hotkey('ctrl', 'v')
    # 模拟回车键发送
    pyautogui.press('enter')

# 主函数
def main():
    while True:
        # 检测新消息提示图标（假设提示图标为 read1.png）
        if locate_and_click("read1.png"):
            # 等待聊天窗口打开
            time.sleep(1)
            # 定位聊天输入框（假设输入框图像为 huifu.png）
            if locate_and_click("huifu.png"):
                # 发送回复
                send_reply()
                # 等待一段时间再返回监听状态，以避免频繁检测
                locate_and_click("wenjianzushou.png")

                time.sleep(15)
        else:
            print("监听中...")
        # 等待一段时间再检测
        time.sleep(20)

if __name__ == "__main__":
   main()



##需要准备三张图片，第一张是好友的消息弹窗，第二是聊天输入窗口，第三是文件传输助手