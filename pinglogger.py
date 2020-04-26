import subprocess
import re
import os
import time
from datetime import datetime
import winsound


def pinghost():
    cmd = "ping google.com"
    ret = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    ret = ret.decode("utf8")
    return ret


i = 0
while True:
    ret = pinghost()
    # print(ret)
    # ips = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", ret)
    # print(ips)

    delay_time = re.findall(r"\b\d{1,5}ms\b", ret)
    if int(delay_time[-1].replace("ms", "")) > 100:
        winsound.Beep(500, 200)
    # print(delay_time)
    if not os.path.exists("ping_logs.txt"):
        open("ping_logs.txt", "w").close()
    else:
        with open("ping_logs.txt", "a") as logger:
            curtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = f"{curtime}->{delay_time[-1]}\n"
            logger.write(data)
    print(f"[{i}]Sleeping Now")
    time.sleep(1)  # seconds
    i += 1
