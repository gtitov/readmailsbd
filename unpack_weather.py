from os.path import join, isfile, basename
from bitstruct import unpack_dict
import sys

"""
Unpack binary data from Iridium system weather buoy .sbd file
into a dict and convert them into human readable format
then dump csv formatted string into stdout
Binary struct(MSB):
        >u8u8u7u10u5u4u6u5u6u6u25u26u5u6u6u12u12u12u12u12u12u12u12u12u12u3
Field names:
        SBDT SBDR Vbat HT GPSYear GPSMonth GPSDay GPSHour GPSMinute GPSSecond 
        GPSLatitude GPSLongitude GPSSatNum GPSHDOP GPSTTFF T1 T2 T3 T4 T5 T6 
        T7 T8 T9 T10 Unused
"""


file_structure = {
    "SBDT": "u8",
    "SBDR": "u8",
    "Vbat": "u7",
    "HT": "u10",
    "GPSYear": "u5",
    "GPSMonth": "u4",
    "GPSDay": "u6",
    "GPSHour": "u5",
    "GPSMinute": "u6",
    "GPSSecond": "u6",
    "GPSLatitude": "u25",
    "GPSLongitude": "u26",
    "GPSSatNum": "u5",
    "GPSHDOP": "u6",
    "GPSTTFF": "u6",
    "T1": "u12",
    "T2": "u12",
    "T3": "u12",
    "T4": "u12",
    "T5": "u12",
    "T6": "u12",
    "T7": "u12",
    "T8": "u12",
    "T9": "u12",
    "T10": "u12",
    "Unused": "u3",
}

bin_struct = ">" + "".join(file_structure.values())
bin_fields = list(file_structure.keys())

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




def __convert_temp(n):
    return 0.01 * n - 20


def convert(raw_dict: dict):
    """Naively apply conversion formulas provided by Iridium documentation
    in Attachment A (Приложение А)"""
    converted_dict = {
        "SBDT": raw_values["SBDT"],
        "SBDR": raw_values["SBDR"],
        "Vbat": raw_values["Vbat"] * 0.1 + 5,
        "HT": raw_values["HT"] * 0.1 - 40,
        "GPSYear": raw_values["GPSYear"] + 2015,
        "GPSMonth": raw_values["GPSMonth"],
        "GPSDay": raw_values["GPSDay"],
        "GPSHour": raw_values["GPSHour"],
        "GPSMinute": raw_values["GPSMinute"],
        "GPSSecond": raw_values["GPSSecond"],
        "GPSLatitude": raw_values["GPSLatitude"] * 0.00001 - 90,
        "GPSLongitude": raw_values["GPSLongitude"] * 0.00001,
        "GPSSatNum": raw_values["GPSSatNum"],
        "GPSHDOP": raw_values["GPSHDOP"] * 0.1,
        "GPSTTFF": raw_values["GPSTTFF"] * 2,
        "T1": __convert_temp(raw_values["T1"]),
        "T2": __convert_temp(raw_values["T2"]),
        "T3": __convert_temp(raw_values["T3"]),
        "T4": __convert_temp(raw_values["T4"]),
        "T5": __convert_temp(raw_values["T5"]),
        "T6": __convert_temp(raw_values["T6"]),
        "T7": __convert_temp(raw_values["T7"]),
        "T8": __convert_temp(raw_values["T8"]),
        "T9": __convert_temp(raw_values["T9"]),
        "T10": __convert_temp(raw_values["T10"]),
        "Unused": 0,
    }
    return converted_dict

def float_to_str(float_number):
    return ("%f" % float_number).rstrip("0").rstrip(".")



try:
    sbd = sys.argv[1]
    folder_for_csv = sys.argv[2]
    with open(sbd, "rb") as f:
        raw_values = unpack_dict(bin_struct, bin_fields, f.read())
    human_readable = convert(raw_values)
    values_list = map(float_to_str, human_readable.values())  # convert to str to join further
    values_str = ",".join(values_list)
    # print(values_str)

    # print(*human_readable.values(), sep=",")

    csv = check_imei(sbd, folder_for_csv, file_structure)
    with open(csv, mode="a") as f:
        f.write(values_str)
        f.write("\n")

        # print(*human_readable.values(), sep=",")
except (IOError, IndexError):
    sys.stderr.write(
        "Usage: ./"
        + sys.argv[0]
        + " FILE.sbd\n"
        + "       Unpack binary data from Iridium weather buoy into csv\n"
    )
    sys.stderr.flush()
    exit()
