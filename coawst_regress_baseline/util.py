import os            # issues system commands
import sys           # system commands 
import errno         # raise errors if files exist 
import time          # internal module to get time
import shutil        # file copying 
import fileinput     # replacing string in files
import os.path       # to copy files after checking if they exist on this path
import subprocess    # for PBS commands
import time          # to put test case on hold 
import re            # regular expressions package for checking queue 

def get_coawst():
    """ get the coawst source code """
    timestr = time.strftime("%Y%m%d")  
    srcdirname = "COAWST_src_"+timestr  
    code_path=os.path.abspath(srcdirname)
    try:
        os.makedirs(srcdirname)
        os.chdir(srcdirname)  
        os.system('svn checkout https://coawstmodel.sourcerepo.com/coawstmodel/COAWST .' %locals())

        src_wrf_make = os.path.abspath('../coawst_regress_baseline/WRF_config_file/makefile')
        shutil.copy(src_wrf_make,code_path)

        return code_path

    except Exception, OSError:
        code_path=os.path.abspath(srcdirname)
        return code_path
        if exception.errno !=errno.EEXIST:
            print "COAWST source directory for this day already exists"
            raise  

def get_testcaselist(code_path):
    """ get a list of test cases from code path """ 
    """ Always include Inlet_test and JOE_TC in the ignored list """
    ignored = ['.svn']
    path=os.path.join(code_path,'Projects')
    testcase= [x for x in os.listdir(path) if x not in ignored]
 
    return testcase 

def edit_bashfile(bashfile,each_case,code_path,project_path): 
    """ edit the bashfile for each case """ 
    upper_testcase=each_case.upper()
    for line in fileinput.input([bashfile],inplace=True): 
        oldinput = "COAWST_APPLICATION=INLET_TEST"
        newinput = "COAWST_APPLICATION=" + upper_testcase
        line = line.replace(oldinput,newinput)
  
        oldinput = "MY_PROJECT_DIR=${MY_ROOT_DIR}"
        newinput = "MY_PROJECT_DIR="+project_path
        line = line.replace(oldinput,newinput)

        oldinput = "MY_ROOT_DIR=/cygdrive/e/data/models/COAWST"
        newinput = "MY_ROOT_DIR=" + code_path 
        line = line.replace(oldinput,newinput)

        oldinput=  "MY_HEADER_DIR=${MY_PROJECT_DIR}/Projects/Inlet_test/Coupled"
        newinput=  "MY_HEADER_DIR=" + project_path
        line = line.replace(oldinput,newinput)

        oldinput= "MY_ANALYTICAL_DIR=${MY_PROJECT_DIR}/Projects/Inlet_test/Coupled"
        newinput= "MY_ANALYTICAL_DIR=" + project_path 
        line = line.replace(oldinput,newinput)

        oldinput= "USE_MPIF90=  "
        newinput= "USE_MPIF90=on"
        line = line.replace(oldinput,newinput)

        oldinput= "export         which_MPI=openmpi"
        newinput= "#export         which_MPI=openmpi"
        line = line.replace(oldinput,newinput)

        oldinput="export              FORT=ifort"
        newinput= "#export              FORT=     "
        line = line.replace(oldinput,newinput)

        oldinput="#export              FORT=pgi"
        newinput=" export              FORT=pgi"
        line = line.replace(oldinput,newinput)

        sys.stdout.write(line)

def edit_jobscript(runfile,inputfile,each_case,project_str,code_path,tot_nproc,nodes):
    """edit the job script for each case  """ 
    for line in fileinput.input([runfile],inplace=True): 
        oldinput = "-N cwstv3"
        newinput = "-N " + each_case
        line = line.replace(oldinput,newinput)

        oldinput = "-e isabel_105.err"
        newinput = "-e " + each_case + ".err"
        line = line.replace(oldinput,newinput)

        oldinput = "-o isabel_105.out"
        newinput = "-o " + each_case + ".out"
        line = line.replace(oldinput,newinput)

        oldinput="#PBS -l nodes=1:ppn=8,walltime=120:00:00"
        newinput="#PBS -l nodes=%s:ppn=8,walltime=120:00:00" %(nodes)
        line = line.replace(oldinput,newinput)

        oldinput = "PBS -M jcwarner@usgs.gov"
        newinput = "##PBS -M jcwarner@usgs.gov"
        line = line.replace(oldinput,newinput)

        oldinput = "cd /raid3/jcwarner/Projects/coawst_v3.1/coawst_v3.1_114/"
        newinput = "cd " + code_path 
        line = line.replace(oldinput,newinput)

        oldinput = "-np 8"
        newinput = "-np %s"  % (tot_nproc)
        line = line.replace(oldinput,newinput)

        oldinput = "Projects/Sandy/coupling_sandy1.in"
        newinput =  project_str+'/'+inputfile
        """ for swanonly need two input files """
        newinput2 = ' '+project_str+'/'+'swan_inlet_test_ref5.in'
        if each_case=="Inlet_test_Swanonly":
            newinput=newinput+newinput2 
        line = line.replace(oldinput,newinput)

        oldinput = "cwstv3.out"
        newinput =  'log.out_' + each_case
        line = line.replace(oldinput,newinput)

        sys.stdout.write(line)

def edit_oceaninfile(inputfile,ntilex,ntiley): 
    """ edit the input file for each case """ 
    for line in fileinput.input([inputfile],inplace=True): 
            oldinput = "NtileI == 1"
            newinput = "NtileI == %s" % (ntilex)
            line = line.replace(oldinput,newinput)
  
            oldinput = "NtileJ == 1"
            newinput = "NtileJ == %s" % (ntiley)
            line = line.replace(oldinput,newinput)

            sys.stdout.write(line)

def edit_couplefile(couplefile,natm,nwav,nocn,couple_flag): 
    """ edit the input file for each case """ 
    for line in fileinput.input([couplefile],inplace=True):
        if couple_flag=='2way':
            oldinput = "NnodesATM =  0"
            newinput = "NnodesATM =  %s" %(natm) 
            line = line.replace(oldinput,newinput)
  
            oldinput = "NnodesWAV =  1"
            newinput = "NnodesWAV =  %s" %(nwav)
            line = line.replace(oldinput,newinput)

            oldinput = "NnodesOCN =  1"
            newinput = "NnodesOCN =  %s" %(nocn)
            line = line.replace(oldinput,newinput)

            sys.stdout.write(line)
        
        elif couple_flag=='3way':
            oldinput = "NnodesATM =  1"
            newinput = "NnodesATM =  %s" %(natm)
            line = line.replace(oldinput,newinput)
  
            oldinput = "NnodesWAV =  1"
            newinput = "NnodesWAV =  %s" %(nwav)
            line = line.replace(oldinput,newinput)

            oldinput = "NnodesOCN =  1"
            newinput = "NnodesOCN =  %s" %(nocn)
            line = line.replace(oldinput,newinput)

            sys.stdout.write(line)

def edit_ref_oceaninfile(inputfile,ntilex_ref,ntiley_ref):
    """ edit the input file for each case """
    for line in fileinput.input([inputfile],inplace=True):

        oldinput= "NtileI == 1 1"
        newinput= "NtileI == %s "  %(ntilex_ref)
        line = line.replace(oldinput,newinput)

        oldinput= "NtileJ == 1 1"
        newinput= "NtileJ == %s"  %(ntiley_ref)
        line = line.replace(oldinput,newinput)

        sys.stdout.write(line)

def edit_wrfinfile(wrfinput,nprocx_atm,nprocy_atm):
    """ edit the input file for each case """
    for line in fileinput.input([wrfinput],inplace=True):
            oldinput= "nproc_x                             = 1"
            newinput= "nproc_x                             = %s" %(nprocx_atm)
            line = line.replace(oldinput,newinput)
         
            oldinput= "nproc_y                             = 1"
            newinput= "nproc_y                             = %s" %(nprocy_atm)
            line = line.replace(oldinput,newinput)

            sys.stdout.write(line)

def check_queue(stdout_case):
    time.sleep(10) # added a ten second pause just in case case goes out of the queue
    while True:
        p = subprocess.Popen("qstat",shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout=p.communicate()
        flag=0  # initialize flag to zero value"
        for line in stdout:
             columns=line.split()
             for piece in columns:
                 get_jobid=re.findall(r"^[0-9]{5}",piece)
                 str_get_jobid=("".join(get_jobid))  # convert the get_jobid to string
                 if stdout_case[:5]==str_get_jobid:
                     print "The test case that is queued/running"
                     print "Check every 10 minutes"
                     flag=1
                     time.sleep(600) # ten minutes
        if flag==0:
            print "The last test case is out of the queue"
            break

def move_casefiles(project_path,case_name,bashfile,runfile,buildfile,execute,stdout,logfile):
#   Moving output files to each projects folder
    outfile1=case_name+'.e'+stdout[:5]
    outfile2=case_name+'.o'+stdout[:5]
   
#   Move the build folder first
    src_dir='Build'
    dst_dir=os.path.join(project_path,'Build')
    try: 
        shutil.move(src_dir,dst_dir)
    except:
        print"-------------------------------------"
        print"Build folder for this case already exists"
        print"-------------------------------------"
     
#   Now move output files
    outputfilelist= [outfile1,outfile2,bashfile,runfile,buildfile,execute,logfile]

    for filename in outputfilelist:
        if (os.path.isfile(filename)):
            shutil.move(filename,project_path)

#   Now move all the files with these extensions or prefixes
    for filename in os.listdir('.'):
        if filename.endswith(('.nc','.mat')):
            shutil.move(filename,project_path)

    for filename in os.listdir('.'):
        if filename.startswith(('swaninit','wrfout','PRINT','Sandy_',\
            'depth','force','qb','hsig','dissip','tmbot','rtp','ubot',\
            'wdir','wlen','botlev','fric','vel','point1','watlev',\
            'wind','setup.mat','joe_tc_init2.hot','swangrid','xp','yp',\
            'swan_inlet_','swan_intest_')):
            shutil.move(filename,project_path)
    
    outputfilelist2=['namelist.output','nodes.list']
    for filename in outputfilelist2:
        if (os.path.isfile(filename)):
            shutil.move(filename,project_path)
