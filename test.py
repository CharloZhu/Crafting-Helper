import pyautogui
import cv2
import keyboard
import time


def button_work(button_img, button_tag, work_time=0):
    # 等待开始按钮出现，最多等待 15 秒钟
    timeout = time.time() + 15
    while True:
        # 在屏幕上查找按钮的位置
        match = pyautogui.locateOnScreen(button_img)

        # 如果找到了按钮，则点击按钮的中心位置
        if match is not None:
            button_pos = pyautogui.center(match)
            pyautogui.click(button_pos.x, button_pos.y, clicks=2, interval=0.25)
            print("已找到", button_tag, "键：", button_pos.x, button_pos.y)

            if work_time:
                end_time = time.time() + work_time
                while time.time() < end_time:
                    if keyboard.is_pressed("esc"):
                        print("ESC pressed")
                        break
            return 1

        # 如果超时了，则退出循环
        if time.time() > timeout:
            break

        # 等待 5 秒钟再进行下一次检查
        time.sleep(3)
    return 0


def main():
    start_button = cv2.imread("start.png")
    work_button = cv2.imread("ysp.png")

    count = 0
    maxCount = 58
    work_time = 30

    while not keyboard.is_pressed("esc") and count < maxCount:
        print("正在执行第", count, "次行动：")

        if not button_work(start_button, "开始"):
            print("无法找到开始键")
            break

        time.sleep(2)

        if not button_work(work_button, "工作", work_time):
            print("无法找到工作键")
            break

        count += 1

    print("结束工作")


main()
