import util_plot
from matplotlib.backends.backend_pdf import PdfPages
import trench_plot
import estuary_test2_plot
#import wetdry_plot
#import ducknc_plot 
#import speclight_plot
#import sedbed_toy_plot
#import sed_floc_toy_plot
#import sandy_plot
##import ripcurrent_plot
#import inlettest_plot
#import joetc_plot
#import shoreface_plot
#
def plot_testcase():
    """Plot the variables for each test"""
    with PdfPages('regress_pdf.pdf') as pdf:
        trench_plot.plot_trench(pdf) 
        estuary_test2_plot.plot_estuary_test2(pdf)
#    wetdry_plot.plot_wetdry(code_path)
#    ducknc_plot.plot_ducknc(code_path) 
#    speclight_plot.plot_speclight(code_path) 
#    sedbed_toy_plot.plot_sedbed_toy(code_path) 
#    sed_floc_toy_plot.plot_sed_floc_toy(code_path) 
#    ripcurrent_plot.plot_ripcurrent(code_path) 
#    inlettest_plot.plot_inlet(code_path) 
#    joetc_plot.plot_joetc(code_path) 
##    sandy_plot.plot_sandy(code_path) 
#    shoreface_plot.plot_shoreface(code_path)
