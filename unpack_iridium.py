from os.path import join, isfile, basename
import sys

"""
It is actually text in .sbd format so we read it as a regular text file
"""


file_structure = {  # use dict to preserve universal logic
    "YR00": "",
    "date": "",
    "UTCtime": "",
    "lat": "",
    "lon": ""
}

def check_imei(sbdpath, csvfolder, sbdstructure):
    """Checks if CSV for the imei exists
    If not create CSV for the imei
    """
    sbdfile = basename(sbdpath)
    imei = sbdfile.split("_")[0]
    csvfile = "{}.csv".format(imei)
    csvpath = join(csvfolder, csvfile)
    if(isfile(csvpath)):
        return csvpath
    else:
        with open(csvpath, mode="w") as f:
            headers_list = list(sbdstructure.keys())
            headers = ",".join(headers_list)
            f.write(headers)
            f.write("\n")
        return csvpath

try:
    sbd = sys.argv[1]
    folder_for_csv = sys.argv[2]
    with open(sbd, "r") as f:
        values_str = f.read()
        # if values_str == "no data":
        #     exit()
    # print(values_str)

    csv = check_imei(sbd, folder_for_csv, file_structure)
    with open(csv, mode="a") as f:
        f.write(values_str)
        f.write("\n")

except (IOError, IndexError):
    sys.stderr.write(
        "Usage: ./"
        + sys.argv[0]
        + " FILE.sbd FOLDER_FOR_CSV\n"
        + "       Unpack binary data from Iridium weather buoy into csv\n"
    )
    sys.stderr.flush()
    exit()
