/*
bin2csv.c - Unpack binary data from Iridium system weather buoy .sbd file
into a dict and convert them into human readable format
rhen dump csv formatted string into stdout

Usage: ./bin2csv FILE.sbd
*/
#include <stdio.h>
#include <stdlib.h>

#include "bin2csv.h"

int main(int argc, char const *argv[])
{
    union Raw_sbd_view sbd = (union Raw_sbd_view){0};

    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s FILE\n       "
                        "Unpack binary data from Iridium weather buoy into csv\n",
                argv[0]);
        exit(EXIT_FAILURE);
    }
    //open bin file
    FILE *rawbin_file = fopen(argv[1], "rb");

    if (!rawbin_file)
    {
        fprintf(stderr, "Error opening file");
        exit(EXIT_FAILURE);
    }
    //bind to struct
    fread(sbd.arr_view, sizeof(sbd), 1, rawbin_file);
    //export as csv
    /*
    printf("%d,",sbd.st_view.);
    printf("%.2f,", sbd.st_view.);
    */
    printf("%d,", sbd.st_view.sbdt);
    printf("%d,", sbd.st_view.sbdr);
    printf("%.1f,", sbd.st_view.vbat * 0.1 + 5);
    printf("%.1f,", sbd.st_view.ht * 0.1 - 40);
    printf("%d,", sbd.st_view.gpsyear + 2015);
    printf("%d,", sbd.st_view.gpsmonth);
    printf("%d,", sbd.st_view.gpsday);
    printf("%d,", sbd.st_view.gpshour);
    printf("%d,", sbd.st_view.gpsminute);
    printf("%d,", sbd.st_view.gpssecond);
    printf("%.5f,", sbd.st_view.gpslatitude * 0.00001 - 90);
    printf("%.5f,", sbd.st_view.gpslongitude * 0.00001);
    printf("%d,", sbd.st_view.gpssatnum);
    printf("%.2f,", sbd.st_view.gpshdop * 0.1);
    printf("%d,", sbd.st_view.gpsttff * 2);
    printf("%.2f,", sbd.st_view.t1 * 0.01 - 20);
    printf("%.2f,", sbd.st_view.t2 * 0.01 - 20);
    printf("%.2f,", sbd.st_view.t3 * 0.01 - 20);
    printf("%.2f,", sbd.st_view.t4 * 0.01 - 20);
    printf("%.2f,", sbd.st_view.t5 * 0.01 - 20);
    printf("%.2f,", sbd.st_view.t6 * 0.01 - 20);
    printf("%.2f,", sbd.st_view.t7 * 0.01 - 20);
    printf("%.2f,", sbd.st_view.t8 * 0.01 - 20);
    printf("%.2f,", sbd.st_view.t9 * 0.01 - 20);
    printf("%.2f\n", sbd.st_view.t10 * 0.01 - 20);

    if (fclose(rawbin_file) == EOF)
    {
        fprintf(stderr, "Error closing file.\n");
    }

    return 0;
}
