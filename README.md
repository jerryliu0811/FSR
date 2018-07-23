# Arduino-da

注意事項：

在Arduino端，用以判別是不是新進來的ODF value的變數 incomming_ODFname，其用以存放的字串陣列長度，必須為10 bytes。
For example:  char incomming[10]={'\0'};

而從Bridge中取回incomming_ODFname時，也要定義取出長度為10 bytes
For example:  Bridge.get("incomming_ODFname",  incomming, 10);

這是因為用起判定是否為新資料的變數incomming_ODFname，是一個序列數字介於 0~10000，序列數字不同時，代表ODFname內有新資料需取回。

BEFORE YOU START: <br>
    1. prepare an Arduino-Yun board with OS version 1.5.3 and <br>
       plug in one micro SD card for storage extension <br>
    2. prepare the FSR(Force Sensitive Resistor) and place it on the Breadboard <br>

HOW TO START: <br>
    1. set Android-Yun wifi AP mode to client mode and make it connect to TARGET_SSID <br>
        1.1 press the wifi reset button about 5~10 seconds and <br>
            then Android-Yun will be reset to wifi AP mode <br>
        1.2 use your smartphone to connect the wifi which <br>
            SSID is 'Android Yun-XXXXXXXX' <br>
        1.3 open your browser and go to '192.168.240.1' (Android-Yun setting page) <br>
            and the password is 'arduino' <br>
        1.4 select TARGET_SSID that You want to connect to <br>
    2. put arduino code(.ino) into Anduino-Yun first <br>
       because Bridge is triggered by arduino <br>
    3. connect to Android-Yun directly and run your program <br>
        3.1 get one laptop and also connect to TARGET_SSID <br>
        3.2 go to the TARGET_SSID setting page <br>
            (different manufacturer's AP will have different setting page IP) <br>
            and get the Arduino-Yun's INTERNAL_IP <br>
        3.3 open terminal and then 'ssh root@INTERNAL_IP' with password 'arduino' <br>
        3.4 place your code and run your program <br>

HOW TO CREATE YOUR APPLICATION: <br>
    1. rewrite 'custom.py' and set the IOTTALK_HOST <br>
    2. create Device Model 'FSR' with Device Feature 'Force-I' <br>
       on IOTTALK_HOST