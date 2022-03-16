# AIY-face-tracker

My proud work on google AIY vision kit

# Google-AIY-voice-kit
Note:
I have created this readme file for reference during the amazon interview the day before.Please apologize if unable to understand :)
Platform: Google AIY kit(vision)
Language: Python

Google aiy kit is nothing but a project built on Raspberry pi Zero along with GPU and other devices(mic obviously for voice kit,camera for vision kit)
In this project,We have used the gpio pins in the vision kit to control the servo motor in a face tracker

This project consists of two servo motors.
One for up and down movement.
one for left and right movement
Inspired from:
https://www.youtube.com/watch?v=sIHQZVZAoXE

The face tracker works by adjust the position of servo motor to keep the face of the viewer at the centre of the camera as possible.
Issues faced:
We have to fine tune the movement speed,over speed will result in movement of servo far from person.very slow movement will lead to face untracked for even slow movements.
choose optimum point.
High movement speed will also lead to a issue where the motor moves the position continuously left and right of the face
(Reason:
When the face is at left,after a movement it will come to right end.It will move right to adjust which will cause same issue again.)

I shall update this readme later.Thanks
