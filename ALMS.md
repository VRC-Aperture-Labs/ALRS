# ALMS Format Specification
### What is an ALMS file?
ALMS stands for "Aperture Labs Movement Script." An ALMS file contains commands that specify movement, activation, etc. of various systems such as motors, pneumatics, etc.

---
### ALMS Header Section
Every ALMS file must start with a header section that includes assignments of each motor, pneumatic, drivetrain, etc., including their port and a name for it, and any other relevant information based on the Vex python contructor functions, such as `Motor()`, etc.\
Example header section with all assignment type:
```
# Comments are written using '#' and go until a ';' or newline
Motor lDriveMotor 9 True
# "Motor" specifies assignment type
# "lDriveMotor" is the name of the assigned variable
# "9" is the port
# "True" is whether or not it is reversed
```
# TODO! FINISH SPEC