# Copyright (c) 2022 Anshuman Nayak
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# Copyright (c) 2022 Anshuman Nayak
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

def convert_dir(netcdf_dir, csv_dir, cleaned_csv_dir='./', clean_choice=0, chunks=-1, engine='netcdf4'):
    """
        Call this function to convert entire NetCDF directory to CSV
        @params:
            netcdf_dir   - Required  : Directory containing all NetCDF files (Ex:-"D:/NetCdf/") \n
            csv_dir       - Required  : Directory for getting CSV output (Ex:-"D:/Csv/")\n
            cleaned_csv_dir      - Optional  : Specify if only you put clean_choice=1 Directory for getting Cleaned CSV output (Ex:-"D:/Cleaned_csv") \n
            clean_choice      - Optional  : 0/1 (Specify if you want csv without null values)\n
            chunks      - Optional  : Specify if you want to chunk the data (Ex:- 1000) (default = -1)\n
            engine      - Optional  : Specify if you want to use different engine (Ex:- "h5netcdf") (default = 'netcdf4')\n
    """
    import pandas as pd
    import xarray as xr
    import os
    # showing progress bar of complete process
    # Print iterations progress

    def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                         (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
        # Print New Line on Complete
        if iteration == total:
            print()

    file_list = [f for f in os.listdir(netcdf_dir) if f.endswith('.nc')]
    l = len(file_list)
    printProgressBar(0, l, prefix='Progress:', suffix='Complete')
    for i, filename in enumerate(file_list):
        printProgressBar(i + 1, l, prefix='Progress:', suffix='Complete')
        ds = xr.open_dataset(os.path.join(
            netcdf_dir, filename), chunks=chunks, engine=engine)
        for i, chunk in enumerate(ds.chunks):
            df = chunk.to_dataframe()
            chunk_flag = ''
            if chunks != -1:
                chunk_flag = '_chunk_' + str(i)
            df.to_csv(os.path.join(csv_dir, 'uncleaned_' +
                      filename[:-3] + chunk_flag + '.csv'))
            # print (filename + ' has been processed to csv and saved to :-',csv_dir +'uncleaned_'+ filename[:-3] + '.csv')
            if clean_choice == 1:
                data = pd.read_csv(os.path.join(
                    csv_dir, 'uncleaned_' + filename[:-3] + chunk_flag + '.csv'))
                data.dropna().to_csv(os.path.join(cleaned_csv_dir,
                                                  'cleaned_' + filename[:-3] + chunk_flag + '.csv'), index=False)
                print(filename + ' has been cleaned and saved to :- ' +
                      os.path.join(cleaned_csv_dir, 'cleaned_' + filename[:-3] + chunk_flag + '.csv'))
        printProgressBar(i + 1, l, prefix='Progress:', suffix='Complete')


def convert_file(filepath, csv_dir, cleaned_csv_dir, clean_choice=0, chunks=-1, engine='netcdf4'):
    """
        Call this function to convert NetCDF file to CSV
        @params:
            filepath     - Required : NetCdf path ( Ex:- "D:/cdf/demo.nc")\n
            csv_dir       - Required  : Directory for getting CSV output (Ex:- "D:/Csv/")\n
            cleaned_csv_dir      - Optional  : Specify if only you put clean_choice=1 Directory for getting Cleaned CSV output ( Ex:-"D:/Cleaned_csv")\n
            clean_choice      - Optional  : 0/1 (Specify 1 if you want csv without null values)\n
            chunks      - Optional  : Specify if you want to chunk the data (Ex:- 1000) (default = -1)\n
            engine      - Optional  : Specify if you want to use different engine (Ex:- "h5netcdf") (default = 'netcdf4')\n
    """
    import pandas as pd
    import xarray as xr
    import os
    # showing progress bar of complete process
    # Print iterations progress

    def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                         (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
        # Print New Line on Complete
        if iteration == total:
            print()

    ds = xr.open_dataset(filepath, chunks=chunks, engine=engine)
    filename = os.path.basename(filepath)
    for i, chunk in enumerate(ds.chunk()):
        df = chunk.to_dataframe()
        df.to_csv(os.path.join(csv_dir, 'uncleaned_' + filename[:-3] + '.csv'))
        chunk_flag = ''
        if chunks != -1:
            chunk_flag = '_chunk_' + str(i)
        print(filename + ' has been processed to csv and saved to :-' +
              os.path.join(csv_dir, 'uncleaned_' + filename[:-3] + chunk_flag + '.csv'))
        if clean_choice == 1:
            data = pd.read_csv(os.path.join(
                csv_dir, 'uncleaned_' + filename[:-3] + '.csv'))
            data.dropna().to_csv(os.path.join(cleaned_csv_dir,
                                              'cleaned_' + filename[:-3] + chunk_flag + '.csv'), index=False)
            print(filename + ' has been cleaned and saved to :- ' +
                  os.path.join(cleaned_csv_dir, 'cleaned_' + filename[:-3] + chunk_flag + '.csv'))
    printProgressBar(1, 1, prefix='Progress:', suffix='Complete')
