import util_plot
import os
import sys 

def plot_sandy(pdf):
    his_name='Sandy_ocean_his.nc'
    testcase='Sandy'
    path_his_old, path_his_new=os.path.join(util_plot.get_result_path())
    path_his_old=path_his_old+'/Projects/'+testcase+'/'+his_name
    path_his_new=path_his_new+'/Projects/'+testcase+'/'+his_name
    if os.path.isfile(path_his_old) and os.path.isfile(path_his_new):
        print "------------------------------------------------------------"
        print "The history file from OLDER COAWST regression run for",testcase,"case is",path_his_old
        print "------------------------------------------------------------"
        print "The history file from NEW COAWST regression run for",testcase,"case is",path_his_new
        """ set the contour levels for zeta plots """
        colormin=-1.3
        colormax=0.9
        xmin=-82.0
        xmax=-65.0
        ymin=27.5
        ymax=43.0 
        """ call the function for zeta (water level) plots """
        util_plot.plot_zeta(pdf,path_his_old,path_his_new,his_name,testcase,xmin,xmax,\
                         ymin,ymax,colormin,colormax)
    else:
        print "-------------------xx---------------------------------------"
        print "One or both HISTORY files for", testcase, "don't exist in the path"
