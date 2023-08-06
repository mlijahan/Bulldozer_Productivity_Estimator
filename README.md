# Bulldozer_Productivity

Dozer production rates are controlled by three factors:
■ Type of blade
■ Type and condition of material
■ Cycle time

*****************************************************************************************************************************************************************

Blade load (lcy) = 0.0139HWL 

*****************************************************************************************************************************************************************

The sum of the time required to push a load, backtrack, and maneuver into position to push again represents one dozer production cycle. The time required 
to push and backtrack can be calculated for each dozing situation considering the travel distance and obtaining a speed from the machine’s performance chart.

In this file maneuvering time=0.05, fix time=0.05, spread time=0 and cuttime=0 are assumed. Hauling and returning time are calculated through hauling and returning velositiies of machine which insert by users. Dozing is generally performed at slow speed, 1.5 to 2 mph. The lower  figure is appropriate for very heavy cohesive materials. Return speed is usually the maximum the machine can attain in the available distance, typically less than 300 ft. Machine performance charts identify maximum forward and  reverse speeds for each gear. The average speed should be carefully chosen based on the time required to accelerate to the instantaneous speed indicated on the chart.
In addition, productivity impressed with below factors:
- operatio factor
- material factor
- dozing factor
- visibility factor
- grade factor
In # Bulldozer_Productivity.py file all above factores are mentioned in real productivity calculation.


