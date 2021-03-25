---
title: Data Structure of Emission File 
author: Sadman Ahmed Shanto 
date: 2021-03-25 
geometry: margin=2cm
---


## Data Columns

The following are pretty self explanatory.
- 'event_num': The event number for a given run.
- 'event_time': The time in microsecond at which the event took place (accumulates)
- 'deadtime': The deadtime for a given event.

The following can only hold '0' or '1' as a value. '0' represents no hit registered from the event and '1' represents a hit. The prefix -'l' or 'r'- represents the left or right cable. The suffix - *integer* - represents the tray number.

- 'l1hit': 
- 'l2hit':
- 'l3hit':
- 'l4hit':
- 'r1hit':
- 'r2hit':
- 'r3hit':
- 'r4hit':

These are the ADC outputs from the Scaler Module.

- 'SCh0':
- 'SCh1':
- 'SCh2':
- 'SCh3':
- 'SCh4':
- 'SCh5':
- 'SCh6':
- 'SCh7':
- 'SCh8':
- 'SCh9':
- 'SCh10':
- 'SCh11':

These are the TDC output from each cable on each tray (very important). The prefix -'L' or 'R'- represents the left or right cable. The suffix - *integer* - represents the tray number.

- 'L1':
- 'R1':
- 'L2':
- 'R2':
- 'L3':
- 'R3':
- 'L4':
- 'R4':

These are the ADC outputs from the LeCroy 2249 module.

- 'ADC0':
- 'ADC1':
- 'ADC2':
- 'ADC3':
- 'ADC4':
- 'ADC5':
- 'ADC6':
- 'ADC7':
- 'ADC8':
- 'ADC9':
- 'ADC10':
- 'ADC11':

The TDC value from the Top and Bottom Counters.

- 'TopCounter':
- 'BottomCounter':

The following represent an arithmetic operation - add and subtract - on the TDC values for each tray.

- 'sumL1':
- 'sumL2':
- 'sumL3':
- 'sumL4':
- 'diffL1':
- 'diffL2':
- 'diffL3':
- 'diffL4':

The following is the asymmetry values for each tray calculated as diffTDC/sumTDC.

- 'asymL1':
- 'asymL2':
- 'asymL3':
- 'asymL4':

- 'numLHit': 2 * number of layers hit (8 means all 4 layers hit)

Angle in X and Y using asymmetry coordinates.

- 'theta_x1': 
- 'theta_y1':
- 'theta_x2':
- 'theta_y2':

- 'z_angle': Zenith angle of muon hit
- 'SmallCounter': TDC of small counter
- 'Run_Num': Tracks the run number 

The plane of interest is chosen to be the plane of lead bricks for these values.

- 'xx': Projection of x coordinate in plane of interest using asymmetry.
- 'yy': Projection of y coordinate in plane of interest using asymmetry.

- 'speed': Speed of muon

- 'xx1': Projection of x coordinate in plane of interest using TDC differences.
- 'yy1': Projection of y coordinate in plane of interest using TDC differences.
