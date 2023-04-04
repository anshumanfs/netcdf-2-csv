<!--
 Copyright (c) 2022 Anshuman Nayak
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->
[![Downloads](https://static.pepy.tech/personalized-badge/netcdf2csv?period=total&units=international_system&left_color=black&right_color=green&left_text=Downloads)](https://pepy.tech/project/netcdf2csv)

# Why `netcdf2csv` ?
`netcdf2csv` is a opensource python package to convert NetCDF files to CSV format. This is mainly helpful for those who are working with weather data, GIS data etc.
# Installation
    pip install netcdf2csv

# Usages

## Convert entire NetCdf file directory to csv 
 
    from netcdf2csv import convert_dir
    
    convert_dir(netcdf_dir,csv_dir,cleaned_csv_dir='./',clean_choice=0, chunks=-1, engine='netcdf4')
    


* net_cdf_dir = Directory containing all netcdf (.nc) files

* csv_dir = Directory to output all csv files(uncleaned- containing null values) 

* cleaned_csv_dir = Directory to output cleaned csv files (does not containing null values) (Optional)

* clean_choice = (0 -> if you don't need cleaned csv, 1 -> if you want cleaned csv output)

* chunks = (int, dict, 'auto' or None, optional) – If chunks is provided, it is used to load the new dataset into dask arrays. chunks=-1 loads the dataset with dask using a single chunk for all arrays. chunks={} loads the dataset with dask using engine preferred chunks if exposed by the backend, otherwise with a single chunk for all arrays. In order to reproduce the default behavior of xr.open_zarr(...) use xr.open_dataset(..., engine='zarr', chunks={}). chunks='auto' will use dask auto chunking taking into account the engine preferred chunks. See dask chunking for more details. (optional) (default (if you don't specify) -> -1)

* engine  ={"netcdf4", "scipy", "pydap", "h5netcdf", "pynio", "cfgrib", "pseudonetcdf", "zarr", None} (default  (if you don't specify)-> 'netcdf4') (optional)

&nbsp;
## Convert a single NetCdf file to csv

    from netcdf2csv import convert_file
    
    convert_file(filepath,csv_dir,cleaned_csv_dir,clean_choice=0, chunks=-1, engine='netcdf4')

* filepath = Full path of file

* csv_dir = Directory to output csv files (Uncleaned - containing null)

* cleaned_csv_dir = Directory to output cleaned csv files (does not containing null values) (Optional)

* clean_choice = (0 -> if you don't need cleaned csv, 1 -> if you want cleaned csv output)

* chunks = (int, dict, 'auto' or None, optional) – If chunks is provided, it is used to load the new dataset into dask arrays. chunks=-1 loads the dataset with dask using a single chunk for all arrays. chunks={} loads the dataset with dask using engine preferred chunks if exposed by the backend, otherwise with a single chunk for all arrays. In order to reproduce the default behavior of xr.open_zarr(...) use xr.open_dataset(..., engine='zarr', chunks={}). chunks='auto' will use dask auto chunking taking into account the engine preferred chunks. See dask chunking for more details. (optional) (default (if you don't specify) -> -1)

* engine  ={"netcdf4", "scipy", "pydap", "h5netcdf", "pynio", "cfgrib", "pseudonetcdf", "zarr", None} (default  (if you don't specify)-> 'netcdf4') (optional)


# Donate

Please donate to support further developement of this package https://pmny.in/Sr8zto1GCbdq