# Real-Time Voice Cloning
## Video Demonstration:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/U7OMHGiCOhw/0.jpg)](https://youtu.be/U7OMHGiCOhw)

## Setup:
### 1. Install Dependencies:
- Install PyTorch (preferably with GPU supported)
- Run `pip install ffmpeg`.
- Run `pip install -r requirements.txt`

### 2. Download Pre-trained Model:
In this project, I use the pre-trained model that was trained by CorentinJ [here](https://github.com/CorentinJ/Real-Time-Voice-Cloning/wiki/Pretrained-models).

### 3. Run Programs:
- Make sure that you edit the IP address in `client_SpeechSynthesiser.py` and `server.py` to match your current IP address. If using 1 computer to run the 2 programs, uncomment the `HOST= 'localhost'`.

![image](https://user-images.githubusercontent.com/85148280/137258355-270f470e-6811-4af3-931b-ff58b617f1be.png)

figure 1: server.py IP address declaration

![image](https://user-images.githubusercontent.com/85148280/137258288-af971915-157f-4eed-8ac5-70b8e31d8ce0.png)

figure 2: client_SpeechSynthesiser.py IP address declaration

- Run `python server.py` and `python client_SpeechSynthesiser.py` in 2 separated terminals.
- Choose an audio file of the target speaker that you want to clone.
- Press both buttons in the 2 programs to establish the connection and start the voice conversion.

## Reference:
J. Corentin, “Real time voice cloning,” GitHub, 14 02 2021. [Online]. Available:
https://github.com/CorentinJ/Real-Time-Voice-Cloning. [Accessed 15 08 2021].
