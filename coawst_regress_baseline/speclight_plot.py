import util_plot
import os
import sys 

def plot_speclight(pdf):
    his_name='ocean_his.nc'
    testcase='Spec_light'
    path_his_old, path_his_new=os.path.join(util_plot.get_result_path())
    path_his_old=path_his_old+'/Projects/'+testcase+'/'+his_name
    print "------------------------------------------------------------"
    print "The history file from older COAWST regression run for",testcase,"case is",path_his_old
    path_his_new=path_his_new+'/Projects/'+testcase+'/'+his_name
    print "------------------------------------------------------------"
    print "The history file from new COAWST regression run for",testcase,"case is",path_his_new
    print "------------------------------------------------------------"
      
    """ set the contour levels for zeta plots """
    colormin=-0.545
    colormax=-0.52
    xmin=-73.5
    xmax=-72.9
    ymin=-39.5
    ymax=-38.5
    """ call the function for zeta (water level) plots """
    util_plot.plot_zeta(pdf,path_his_old,path_his_new,his_name,testcase,xmin,xmax,\
                         ymin,ymax,colormin,colormax)

