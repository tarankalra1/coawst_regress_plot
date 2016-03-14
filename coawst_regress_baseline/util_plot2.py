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

def plot_zeta(pdf,filepath_old,filepath_new,his_name,testcase, \
              colormin,colormax):
#    """this plots the zeta(water level) in 2D XY plane for
#    the old and the new run and the difference between the 
#    two zeta values"""  

#    x_rho,y_rho,ntime,zeta_old=util_plot.get_zeta(file_path)
    
#    fig = plt.figure()
#    ax = fig.add_subplot(3, 1, 1)
#    ax = fig.gca()
#    plt.pcolormesh(x_rho,y_rho,zeta_old[ntime-1,:,:],vmin=colormin,vmax=colormax)
#    ax.set_title('Old result: Water level for '+testcase.upper()+'case',fontsize=6)
#    ax.set_xlim(0, 30) 
#    ax.tick_params(axis='x', labelsize=4)
#    ax.tick_params(axis='y', labelsize=4)
#    plt.colorbar(label='Water level')
#    ax.tick_params(labelsize=4)
#    plt.ylabel('Lateral direction in kms',fontsize=6)
#    plt.show()

#    ax = fig.add_subplot(3, 1, 2)
#    ax = fig.gca()
#    plt.pcolormesh(x_rho2,y_rho2,zeta2[ntime2-1,:,:],vmin=colormin,vmax=colormax)
#    ax.set_title('Old result: Water level for '+testcase.upper()+' case',fontsize=6)
#    ax.set_xlim(0, 30) 
#    ax.tick_params(axis='x', labelsize=4)
#    ax.tick_params(axis='y', labelsize=4)
#    plt.colorbar(label='Water level')
#    ax.tick_params(labelsize=4)
#    plt.ylabel('Lateral direction in kms',fontsize=6)
#    plt.pcolormesh(x_rho2,y_rho2,zeta2[ntime2-1,:,:],cmap=cmap,edgecolors = 'None',vmin=colormin,vmax=colormax)
##    cb = plt.colorbar(label='Water level')
#    cb.ax.tick_params(labelsize=4)
#    ax.set_xlim(0, 30) 
#    ax.title(figtitle,fontsize=6)
#    ax.set_title('New result: Water level for '+testcase.upper()+' case',fontsize=6)
#    ax.tick_params(axis='x', labelsize=4)
#    ax.tick_params(axis='y', labelsize=4)
#    plt.ylabel('Lateral direction in kms',fontsize=6)

#    ax = fig.add_subplot(3, 1, 3)
#    ax = fig.gca()
#    plt.pcolormesh(x_rho2,y_rho2,zeta1[ntime1-1,:,:]-zeta2[ntime2-1,:,:],cmap=cmap,edgecolors = 'None')
#    cb = plt.colorbar(label='Water level difference')
#    cb.ax.tick_params(labelsize=4)
#    ax.set_title('Difference between old and new results',fontsize=6)
#    ax.tick_params(axis='x', labelsize=4)
#    ax.tick_params(axis='y', labelsize=4)
#    plt.xlabel('Longitudnal direction in kms',fontsize=6)
#    plt.ylabel('Lateral direction in kms',fontsize=6)

#    figname=testcase+'_'+'regress'+'.png'
#    pdf.savefig(fig)
#    pdf.close()
#    plt.savefig(figname,dpi=300,bbox_inches='tight')
#    plt.close(fig)

#def get_zeta(datafile):
#    ncfile=Dataset(datafile,'r')
#    zeta=ncfile.variables['zeta'][:]
#    ntime,nx,ny=zeta.shape
#    xrho=ncfile.variables['x_rho'][:]
#    yrho=ncfile.variables['y_rho'][:]
#    return xrho,yrho,ocean_time,zeta

