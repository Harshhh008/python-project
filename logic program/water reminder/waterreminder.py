import time
from plyer import notification
while True:
    if __name__=="__main__":
        notification.notify(
            title = "Please,Drink water.",
            message = "good for health",
            app_icon = "C:\\Users\\DELL\\OneDrive\\Desktop\\code playground\\python project\\logic program\\water reminder\\icon.png",
            timeout = 5
        )
    time.sleep(10)
