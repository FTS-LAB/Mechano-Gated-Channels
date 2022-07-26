# **MECHANO-GATED CHANNELS ELECTROPHYSIOLOGYCAL PROPERTIES**

Analysis program based on Python3 for Electrophysiological experiments of Mechano-Gated Channels.

TABLE OF CONTENTS
1. INTRODUCTION
   1. FJFJ
   ![Screen_Shot](Resources/img/Program_Screen_Shot.jpg)
2. MAIN PYTHON 3 PACKAGES
   1. Numpy
   2. Pandas
   3. Scipy
   4. Pyqtgraph
   5. PyQT5
3. DATA FORMAT
   1. Our program can not process the .DAT files from HEKA software, so the recordings have to be exported to .ASC file format as shown bellow.
   #
   *(Steps (1-7) need to be followed only once.)*
      1. Press Tweak Button
      2. Select Export Tab.
      3. On File Type Select: **Text**.
      4. Export Choice Select: **Traces** Check-Box only.
      5. Export Choice Select: **NO analysis**.
      6. Trace Time: **Relative to Swepp**.
      7. Text Options: Separator (**Comma**)
      8. Tree Widget:  Select the Sweep to export
      9. Press **Data** Button
      10. Export as **Full Sweep**
   
   ![HEKAEXP](Resources/img/HEKA_EXP.jpg)
4. DATA PREPARATION
   1. Every trace have to be aligned to its sitmuli, leak substracted and linked to its respective indentation value, before any analysis.
   #
      1. ALIGMENT
         1. We extract the index of the first stimulus peak for each trace. (Both traces share their indexes.)
         2. We stablish this index as a reference point in the current traces.
         3. We trimed all current traces using the reference point to get the same lenth in all traces.
      2. LEAK SUBSTRACTION
         1. We select a region from each current trace inactive zone.
         2. We stimate the mean of these regions individually.
         3. We substract the mean value calculated before (leak) of each trace to the original one.
      3. INDENTATION LEVEL LINKING
         1. We generate a dictioray with every indentation levels in μm previously.
         2. We divide in two all stimulus traces to extrac the number of stim peaks. (The division is nevesary due to the nanomotor functioning.)
         3. We use as in index the number of peaks calculated above to extrac each respective indentation value from the dictionay.
         4. We generate a dictionary with all current traces sorted by their indentation values.

5. CHANNEL PARAMETERS
   1. CURRENT RESPONSE
   2. THRESHOLD
   3. INACTIVATION KINETICS (TAU)
6. RESULTS