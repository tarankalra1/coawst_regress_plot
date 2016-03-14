import util_plot
import os
import sys 

def plot_ripcurrent(pdf):
    his_name='ocean_rip_current_his.nc'
    testcase='Rip_current'
    path_his_old, path_his_new=os.path.join(util_plot.get_result_path())
    path_his_old=path_his_old+'/Projects/'+testcase+'/'+his_name
    path_his_new=path_his_new+'/Projects/'+testcase+'/'+his_name
    if os.path.isfile(path_his_old) and os.path.isfile(path_his_new):
        print "------------------------------------------------------------"
        print "The history file from OLDER COAWST regression run for",testcase,"case is",path_his_old
        print "------------------------------------------------------------"
        print "The history file from NEW COAWST regression run for",testcase,"case is",path_his_new
        """ set the contour levels for zeta plots """
        colormin=0.8
        colormax=0.96
        xmin=0.0
        xmax=300.0
        ymin=0.0
        ymax=550.0 
        """ call the function for zeta (water level) plots """
        util_plot.plot_zeta(pdf,path_his_old,path_his_new,his_name,testcase,xmin,xmax,\
                         ymin,ymax,colormin,colormax)
    else:
        print "-------------------xx---------------------------------------"
        print "One or both HISTORY files for", testcase, "don't exist in the path"
