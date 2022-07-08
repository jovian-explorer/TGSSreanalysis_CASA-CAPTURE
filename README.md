# TGSSreanalysis_CASA-CAPTURE

This version of CAPTURE pipeline is result of my radio astronomy master's research project "TIFR-GMRT sky survey (TGSS): an alternate approach to data analysis" http://dspace.iiti.ac.in:8080/jspui/handle/123456789/2936 at IIT I in collab with NCRA-TIFR. The default settings provided allows to immediately image TIFR GMRT SKY SURVEY (TGSS) 150 MHz data with very good dynamic range and accurate flux or any other legacy GMRT data at band 2.

This pipeline contains custom settings 'as is' developed during research project else it is identical to the continuum data reduction pipeline for the Upgraded GMRT developed by Ruta Kale and Ishwara Chandra.https://github.com/ruta-k/uGMRT-pipeline (the vers which works with CASA 5.5 or higher but not 6 was the latest available back then) with few add ons:-

1. Delay calibration  is now done using the flux calibrator in the list which is less flagged instead of which one is first in the list.

2. CAPTURE default all true settings in config_capture.ini flaggs too much for TGSS leaving a non meaningful image - hence derived two settings-  one or the other from my experience allow to image any TGSS data.

3. Functionalities to split out calibrators and / targets as per choice - by setting True in 'dosplitcal' and / 'dosplittar' .

4. Option to specify which casa fluxscale to use through keyword 'standard'.

However the settings/codes if understood properly can be easily implemented in newer versions by the users.

The achievement is data reduction of TGSS at 150 MHz is significantly challenging manually, this ready-to-use pipeline reduces the effort and limits time to hours as well as proves to be accurate even over existing TGSS ADR1 release. It is hoped that this will encourage researchers towards open science with CAPTURE pipeline for both legacy and upgraded GMRT data as they custom fit to their own projects as in our case TGSS.
