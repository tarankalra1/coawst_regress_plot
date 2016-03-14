import os 
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt

def get_result_path():
    """get path for coawst source code
    This looks in current directory for the config file
    """
    path = os.getcwd()
    filepath_old = os.path.join(path,'regress_plot_old.txt')
    filepath_new = os.path.join(path,'regress_plot_new.txt')

    with open(filepath_old) as f, open(filepath_new) as g:
        try:
            filepath_old = f.read().strip()
            filepath_new = g.read().strip()
            return filepath_old, filepath_new
        except:
            raise IOError('unable to read the path of the source codes')

#def plot_table():

def plot_zeta(pdf,filepath_old,filepath_new,his_name,testcase,xmin,xmax,ymin,ymax, \
              colormin,colormax):
    """this plots the zeta(water level) in 2D XY plane for
    the old and the new run and the difference between the 
    two zeta values"""  
    x_rho,y_rho,ntime1,zeta_old=get_zeta(filepath_old)
    """ plot old zeta values """ 
    fig = plt.figure()
    ax = fig.add_subplot(3, 1, 1)
    ax = fig.gca()
    plt.pcolormesh(x_rho,y_rho,zeta_old[ntime1-1,:,:],vmin=colormin,vmax=colormax,rasterized=True)
    ax.set_title('Old result: Water level for '+testcase.upper()+'case',fontsize=8)
    ax.set_xlim(xmin, xmax) 
    ax.set_ylim(ymin, ymax) 
    ax.tick_params(axis='x', labelsize=4)
    ax.tick_params(axis='y', labelsize=4)
    plt.colorbar(label='Water level')
    ax.tick_params(labelsize=8)
    plt.ylabel('Lateral direction in kms',fontsize=8)

    x_rho,y_rho,ntime2,zeta_new=get_zeta(filepath_new)
    """ plot new zeta values """ 
    ax = fig.add_subplot(3, 1, 2)
    ax = fig.gca()
    plt.pcolormesh(x_rho,y_rho,zeta_old[ntime2-1,:,:],vmin=colormin,vmax=colormax,rasterized=True)
    ax.set_title('New result: Water level for '+testcase.upper()+'case',fontsize=8)
    ax.set_xlim(xmin, xmax) 
    ax.set_ylim(ymin, ymax) 
    ax.tick_params(axis='x', labelsize=4)
    ax.tick_params(axis='y', labelsize=4)
    plt.colorbar(label='Water level')
    ax.tick_params(labelsize=8)
    plt.ylabel('Lateral direction in kms',fontsize=8)

    """ plot (new-old) zeta values """ 
    ax = fig.add_subplot(3, 1, 3)
    ax = fig.gca()
    plt.pcolormesh(x_rho,y_rho,zeta_new[ntime1-1,:,:]-zeta_old[ntime2-1,:,:],vmin=colormin,vmax=colormax,rasterized=True)
    ax.set_title('Difference between two zeta values '+testcase.upper()+'case',fontsize=8)
    ax.set_xlim(xmin, xmax) 
    ax.set_ylim(ymin, ymax) 
    ax.tick_params(axis='x', labelsize=4)
    ax.tick_params(axis='y', labelsize=4)
    plt.colorbar(label='Water level')
    ax.tick_params(labelsize=8)
    plt.xlabel('Lateral direction in kms',fontsize=10)
    plt.ylabel('Lateral direction in kms',fontsize=8)
#    plt.show() 
    pdf.savefig(fig)

def get_zeta(his_filepath):
    datafile=his_filepath
    ncfile=Dataset(datafile,'r')
    try: 
        x_rho=ncfile.variables['lon_rho'][:]
        y_rho=ncfile.variables['lat_rho'][:]
    except: 
        x_rho=ncfile.variables['x_rho'][:]
        y_rho=ncfile.variables['y_rho'][:]
    try: 
        mask_rho=ncfile.variables['mask_rho'][:]
    except:
        mask_rho=1
    zeta=ncfile.variables['zeta'][:]*mask_rho
    ntime,nx,ny=zeta.shape
    ocean_time=ncfile.variables['ocean_time'][:]
    return x_rho,y_rho,ntime,zeta
