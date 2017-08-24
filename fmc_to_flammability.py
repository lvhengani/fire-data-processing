"""Script for calculating the Flammability Index from Fuel Moisture Content Data"""

import os

LFMC_DATA_DIR = '../data/lfmc/'
VEG_DATA_DIR = None
MEAN_LFMC_DATA_DIR = None
OUTPUT_DIR = None

def main():
    pass


def get_lfmc_file_info(path=LFMC_DATA_DIR):
    """Returns a Dict containing filenames mapped to data extracted from the
    filenames for LFMC data"""

    lfmc_file_list = [filename for filename in os.listdir(path)
                      if filename.endswith('.nc')]

    lfmc_files = {filename : {
        'year': int(filename[9:13]),
        'day_of_year': int(filename[13:16]),
        'date': int(filename[9:16]),
        'hv': int(filename[18:20]) * 1000 + int(filename[21:23])
    } for filename in lfmc_file_list}

    return lfmc_files


def get_veg_file_info(path=VEG_DATA_DIR):
    """Process veg file names"""

    veg_file_list = [filename for filename in os.listdir(path)
                     if filename.endswith('.tif')]

    veg_files = {filename : {
        'year': int(filename[20:24]),
        'hv': int(filename[32:34]) * 1000 + int(filename[35:37])
    } for filename in veg_file_list}

    return veg_files


def get_mean_lfmc_dataset(path=MEAN_LFMC_DATA_DIR):
    """Process mean LFMC dataset filenames"""

    lfmc_mean_file_list = [filename for filename in os.listdir(path)
                           if filename.endswith('.txt')]

    lfmc_mean_files = {filename : {
        'day_of_year': int(filename[9:12]),
        'hv': int(filename[14:16]) * 1000 + int(filename[17:19])
    } for filename in lfmc_mean_file_list}

    return lfmc_mean_files

if __name__ == '__main__':
    main()
