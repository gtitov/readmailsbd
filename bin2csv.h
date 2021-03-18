/*
bin2csv.h - header file for
bin2csv.c - Unpack binary data from Iridium system weather buoy .sbd file
and convert them into human readable format
then dump csv formatted string into stdout

Usage: ./bin2csv FILE.sbd

Field names:
        SBDT SBDR Vbat HT GPSYear GPSMonth GPSDay GPSHour GPSMinute GPSSecond 
        GPSLatitude GPSLongitude GPSSatNum GPSHDOP GPSTTFF T1 T2 T3 T4 T5 T6 
        T7 T8 T9 T10 Unused
*/
#pragma once

#pragma pack(1)                             //__attribute__ ((__packed__))
#pragma scalar_storage_order big-endian 
struct Raw_sbd
{
    unsigned int sbdt : 8;
    unsigned int sbdr : 8;
    unsigned int vbat : 7;
    unsigned int ht : 10;                 
    unsigned int gpsyear : 5;
    unsigned int gpsmonth : 4;
    unsigned int gpsday : 6;
    unsigned int gpshour : 5;
    unsigned int gpsminute : 6;               
    unsigned int gpssecond : 6;
    unsigned int gpslatitude : 25;
    unsigned int gpslongitude : 26;            
    unsigned int gpssatnum : 5;
    unsigned int gpshdop : 6;
    unsigned int gpsttff : 6;                  
    unsigned int t1 : 12;
    unsigned int t2 : 12;
    unsigned int t3 : 12;
    unsigned int t4 : 12;
    unsigned int t5 : 12;
    unsigned int t6 : 12;
    unsigned int t7 : 12;
    unsigned int t8 : 12;
    unsigned int t9 : 12;
    unsigned int t10 : 12;                           
    unsigned int unused : 3;
}; 

union Raw_sbd_view
{
    struct Raw_sbd st_view;
    unsigned char arr_view[32];
};
