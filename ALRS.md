# ALRS Format Specification
### What is an ALRS file?
ALRS stands for "Aperture Labs Recorded Script." An ALRS file contains one or more snapshots, each recorded 25ms apart. These snapshots contain the current values of each of the axes on the Vex V5 controller, as well as any button events that happened in the last 25ms.

---
### How are snapshots formatted?
Snapshots contain all buttons and axes (even if they are 0) so they can be easily indexed, rather than using larger values that require more space. A snapshot follows the following order:
`axis1,axis2,axis3,axis4,buttonL1,buttonL2,buttonR1,buttonR2,buttonLeft,buttonUp,buttonDown,buttonRight,buttonY,buttonX,buttonB,buttonA;`\
**Note: ';' is interchangeable with a newline to separate the snapshots.**\
The axes will simply have the axis value at the time of the snapshot, and the button values will have one of three values:\
`0`: No button event\
`1`: Button pressed\
`2`: Button released