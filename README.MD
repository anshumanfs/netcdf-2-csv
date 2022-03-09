<!--
 Copyright (c) 2022 Anshuman Nayak
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->
# Why `netcdf2csv` ?
`netcdf2csv` is a opensource python package to convert NetCDF files to CSV format. This is mainly helpful for those who are working with weather data, GIS data etc.
# Installation
    pip install netcdf2csv

# Usages

## Convert entire NetCdf file directory to csv 
 
    from netcdf2csv import convert_dir
    
    convert_dir(netcdf_dir,csv_dir,cleaned_csv_dir='./',clean_choice=0)
    


* net_cdf_dir = Directory containing all netcdf (.nc) files

* csv_dir = Directory to output all csv files(uncleaned- containing null values) 

* cleaned_csv_dir = Directory to output cleaned csv files (does not containing null values) (Optional)

* clean_choice = (0 -> if you don't need cleaned csv, 1 -> if you want cleaned csv output)


&nbsp;
## Convert a single NetCdf file to csv

    from netcdf2csv import convert_dir
    
    convert_file(filepath,csv_dir,cleaned_csv_dir,clean_choice=0)

* filepath = Full path of file

* csv_dir = Directory to output csv files (Uncleaned - containing null)

* cleaned_csv_dir = Directory to output cleaned csv files (does not containing null values) (Optional)

* clean_choice = (0 -> if you don't need cleaned csv, 1 -> if you want cleaned csv output)


# Donate

Please donate to support further developement of this package https://pmny.in/Sr8zto1GCbdq