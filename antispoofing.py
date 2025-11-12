import socket, time, os, re
from plyer import notification
from collections import Counter
from typing import Final

mac_re = re.compile(r"([0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2})")

facebook: Final = socket.gethostbyname("facebook.com")
instagram: Final = socket.gethostbyname("instagram.com")
linkedin: Final = socket.gethostbyname("linkedin.com")
while True:
    try:
        if socket.gethostbyname("facebook.com") == facebook and socket.gethostbyname("instagram.com") == instagram and socket.gethostbyname("linkedin.com") == linkedin:
            continue
        else:
            notification.notify(
            title="Dikkatli Ol",
            message="Dikkat şu anda eğer bir devlet ağında değilseniz, Lütfen facebook, instagram, vb. bir sitede oturum açmadan önce sitenin doğruluğunu kontrol edin",
            timeout=5)
        arp_output = os.popen("arp -a").read()
        macs = [m.replace("-", ":").lower() for m in mac_re.findall(arp_output)]
        duplicates = {m: c for m, c in Counter(macs).items() if c > 2}

        if duplicates:
            if "ff:ff:ff:ff:ff:ff" not in duplicates:
                notification.notify(
                    title="Dikkatli Ol",
                    message="Ağınızda aynı MAC adresine sahip birden fazla cihaz var! Lütfen HTTP kullanan sitelere bilgilerinizi vermeyiniz.",
                    timeout=5)
    except KeyboardInterrupt:
        break
    except Exception:
        continue

    time.sleep(10)
