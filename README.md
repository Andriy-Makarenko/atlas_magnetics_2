# atlas_magnetics

**Task 1**
You with your friend both work at a very confidential and secure company. That's why your PCs
don't have an internet connection. There isn't any local internal messenger too. Both of you work on
different floors. But you would like to have the ability to call your friend for lunch with you. As your
computers are inside the same local network, here is your task:
  • Develop a python desktop app "I'm about to lunch" that has only one function - to send
  a message that you're about to have lunch.
  • Develop a desktop app "Are you going to have lunch?". Its only purpose is to notify
  when the message about lunch is received.
Tasks requirements:
  • Any kind of UI framework
  • The app "Are you going to have lunch?" should open some port and listen to it. The app
  "I'm about to lunch" should send a request to it.
  • For demo purposes, both apps should be run on the same machine.
  • Both application sources should be uploaded to git.

**Task 2**
Calculate the resistive voltage divider: at the input voltage of 12V at the output should be 3V. The
maximum current through the divider should not exceed 5mA. Resistor values should be selected from
the E24 series.


## Installing using Github

```shell
git clone https://github.com/Andriy-Makarenko/atlas_magnetics_2
git checkout main
python -m venv venv
source venv/bin/activate (Linux and macOS) or venv\Scripts\activate (Windows)
pip install -r requirements.txt
```
