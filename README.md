Arduino-da
===
注意事項：
---
在Arduino端，用以判別是不是新進來的ODF value的變數 incomming_ODFname，其用以存放的字串陣列長度，必須為10 bytes。
For example:  char incomming[10]={'\0'};

而從Bridge中取回incomming_ODFname時，也要定義取出長度為10 bytes
For example:  Bridge.get("incomming_ODFname",  incomming, 10);

這是因為用起判定是否為新資料的變數incomming_ODFname，是一個序列數字介於 0~10000，序列數字不同時，代表ODFname內有新資料需取回。

BEFORE YOU START:
---
<ol>
    <li>prepare an Arduino-Yun board with OS version 1.5.3 and  
       plug in one micro SD card for storage extension  
    <li>prepare the FSR(Force Sensitive Resistor) and place it on the Breadboard  
</ol>
HOW TO START:
---
<ol>
    <li>set Android-Yun wifi AP mode to client mode and make it connect to TARGET_SSID  
    <ol>
        <li>press the wifi reset button about 5~10 seconds and  
            then Android-Yun will be reset to wifi AP mode  
        <li>use your smartphone to connect the wifi which  
            SSID is 'Android Yun-XXXXXXXX'  
        <li>open your browser and go to '192.168.240.1' (Android-Yun setting page) 
            and the password is 'arduino'  
        <li>select TARGET_SSID that You want to connect to  
    </ol>
    <li>put arduino code(.ino) into Anduino-Yun first  
       because Bridge is triggered by arduino  
    <li> connect to Android-Yun directly and run your program  
    <ol>
        <li>get one laptop and also connect to TARGET_SSID  
        <li>go to the TARGET_SSID setting page  
            (different manufacturer's AP will have different setting page IP)  
            and get the Arduino-Yun's INTERNAL_IP  
        <li>open terminal and then 'ssh root@INTERNAL_IP' with password 'arduino'  
        <li>place your code and run your program  
    </ol>
</ol>

HOW TO CREATE YOUR APPLICATION:
---
<ol>
    <li>rewrite 'custom.py' and set the IOTTALK_HOST  
    <li>create Device Model 'FSR' with Device Feature 'Force-I'  
       on IOTTALK_HOST  
</ol>

