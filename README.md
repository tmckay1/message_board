# message_board
This program is used to light up a message board powered by a Raspberry Pi 3. The hardware setup is described <a href="http://www.thetylermckay.com/rpi/overview/">here</a>. For a full in-depth description of how this program was designed, go <a href="http://www.thetylermckay.com/rpi/message-board-programming">here</a>.`

## Assumptions
When writing this program I assumed:
- You are running Jessie on the Raspberry Pi 3
- You have already setup the hardware and circuit
- You are using hardware supported by the Software Requirements below

## Software Requirements
In order to use the program you will need the following:
- Python 3 installed
- <a href="https://github.com/ManiacalLabs/BiblioPixel">BiblioPixel</a> Installed (any any dependency it requires)

## Getting Started
The file <code>animateMessageBoard.py</code> is a sample script that executes the program. All animations, algorithms, character sets, and parsers can be subclassed to fit the needs of your setup.
