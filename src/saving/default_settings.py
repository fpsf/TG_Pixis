import os


class DefaultSettings:
    gain = 2
    temp = -70
    time_shooting = 300
    acq_wait = 15
    binning = 1
    exp = 5
    if os.name == "nt":
        path = "C:/Users/" + os.path.expandvars("%USERNAME%") + "/Pictures/CCD_Pixis"
    else:
        path = os.path.expandvars("$HOME") + "/CCD_Pixis"
