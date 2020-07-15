# CA_AI_2020

This repository contains the notebooks for the CA_AI_2020 course.

As this repository and the notebooks within it will be updated constantly, it is recommended
to separate the current course contents after cloning the repository as given below:

![GitHub Platform | Workspace Split Recommendations](/github.png)

**Note**: This is only a recommendation. If you are well acquainted with GitHub and feel comfortable
forking, don't hesitate doing so. I've simply had situations where students spent ages debugging platform issues instead of focusing on the learning material, so this should help to avoid any possible merge conflicts. 

# Setting up
The setup instructions specified below apply for **Unix** (tested on various Ubuntu versions) or **MacOS**, though **Windows users** can follow  
the official conda installation instructions procided [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html). 
After that, the remaining instructions are more or less the same. 

We will be be using Python along with a few open-source libraries, as well as a 
virtual environment and package management tool [conda](https://conda.io/docs/).

In the below instructions, any text styled `like this` should be executed in the terminal. 
Do this **by hand one-by-one**, for pedagogical and debugging purposes. 
Read and heed any warnings *and especially errors* you may encounter.

 
## 1. Install conda
1. Check you don't already have conda installed
    1. `which conda`
    1. if you already have it installed, skip ahead to Create an Environment
1. Download the latest version of miniconda
    1. `cd ~/Downloads` (you can make a Downloads folder if you don't have one)
    1. Download the installer for python 3 depending on your system [here](https://conda.io/miniconda.html):
1. Install miniconda3 *with default settings*
    1. `sh Miniconda3-latest-Linux-x86_64.sh` <-- installer file name
    1. Follow the prompt - **type `yes` and hit `enter` to accept all default
    settings when asked**
1. Close Terminal and reopen
1. Try executing `conda -h`. If it works, you can delete the installer
`rm ~/Downloads/Miniconda3-latest-Linux-x86_64.sh`

## 2a. Create an environment for the course (CA_AI_2020)
1. Update conda: `conda update conda` (update the conda to the latest version)
1. Create the environment for the course. `conda create --name cai python=3`

## 2b. What's an environment (OPTIONAL)?
An environment is a collection of packages of specific versions. You can have
multiple environments and switch between them for different projects. Conda is
a tool for managing such environments *and* the packages within them. Here's a quick intro:

1. Show a list of your environments: `conda env list`
1. Print `$PATH`, one of your system's [environment variables](https://en.wikipedia.org/wiki/Environment_variable), in the
terminal: `echo $PATH`
    * `$PATH` is the list of directories your terminal can search to find
anything you execute:
1. Print a list of python installations on your `$PATH` (the top one is the one
    that will get executed if you type `python` in the terminal):
    `which python -a`
1. Activate the new environment: `source activate iaml`
1. Show list of python installations on your system *now*: `which python -a`
1. Show your system `$PATH` again: `echo $PATH`
1. Deactivate the new environment: `source deactivate`
1. Observer how your $PATH has changed again: `echo $PATH`
1. Make an empty environment: `conda create --name empty`
1. You can clone environments; this is useful for backing up: `conda create
--name empty_bkp --clone empty`
1. Make a python 3 environment with numpy already installed: `conda create
--name py3 python=3 numpy`
1. `conda env list`
1. Activate py3: `source activate py3`
1. Show the installed packages: `conda list`
1. Switch environments: `source deactivate; source activate empty`
1. `conda list` to show packages (note that python and, crucially,
    [pip](https://pip.pypa.io/en/stable/) are not installed)
1. Q: What python would get used now? `which python` A: the conda root
environment installation of python i.e. *not* this environment's python.
1. Install numpy: `conda install numpy`
1. Q: What python would get used *now*? `which python` A: You may have clocked
that conda installed a dependency of numpy (a python package)...python!
1. Let's delete these test environments:
    * `source deactivate`
    * `conda env list`
    * `conda remove --name empty --all`
    * `conda remove --name empty_bkp --all`
    * `conda remove --name py3 --all`
    * `conda env list`

**Further Reading** - **Conda getting started** - 30 minute practical well worth going through https://conda.io/docs/user-guide/getting-started.html


## 3. Install all the packages for CA_AI_2020
1. Activate the environment: `source activate cai`
1. {May take 5 minutes+} Install all required packages: 
`conda install jupyter matplotlib pandas numpy scikit-learn scipy seaborn`
1. Get some space back: `conda clean -a`

### **IMPORTANT**
Before starting any CA_AI_20 work in a new terminal **you must always activate the
iaml conda environment** using `source activate cai`. If the environment is not
activated, you will be using your base python with its own set of packages. If
you are ever in any doubt of which python version is being used, execute
`which python`.

**N.B. Windows** to activate the `cai` environment, note that you don't type `source activate cai`
but instead just `activate cai`

## 4. Get started!!!
Once you have set up your conda requirement, you are ready to start working with Jupyter notebooks. You are advised
to navigate via terminal to the folder containing your course files before running Jupyter.

**Note:** You will also have to get the files first. To do so, install Git by running `conda install -c anaconda git` and clone this repository via `git clone https://github.com/povilaspazera/CA_AI_2020.git`.

1. Activate the conda environment: `source activate cai`
2. Navigate to the folder containing course files, e.g.: `cd /home/povilas/Desktop/CA_AI_2020`
2. Start a jupyter notebook
    * `jupyter notebook`
3. This should automatically open your browser
    * Click on `/01_Python_Crash_Course/01_Introduction_to_Python_and_Jupyter.ipynb` to open it


## Troubleshooting

### Trashing your environment
If you install incorrect packages, or a package breaks for some reason, you can
just delete your environment and start again. Execute `conda remove --name iaml
--all` then install the package as described above.

### Trashing your whole conda installation
This is fairly extreme but as a final resort can be done quickly and easily.
Please note that you will lose *all* your environments if you do this, so check
this will not affect you before proceeding...[follow instructions here](https://conda.io/docs/user-guide/install/linux.html?highlight=uninstall#uninstalling-anaconda-or-miniconda)

### conda: command not found or 'Conda never works in new terminal'
Unix solution: First try closing your terminal and reopening. If that doesn't fix, it's likely that, in the conda installation, you didn't allow conda to add the it's bin directory to your $PATH. 

```
Try appending Miniconda to your path by (adjust based on your system):
```

```
echo "export PATH=\""\$PATH":$HOME/miniconda3/bin\"" >> ~/.benv
```

Update the Path variable with:

```
source ~/.benv
```

For all future terminal sessions you should now be able to access
Miniconda by typing `conda` in your terminal

### 'source' is not recognized as an internal or external command, ...
You're on windows aren't you! Please see the note at the top of the file (you
can omit `source`)

### 'which' is not recognized as an internal or external command, ...
You're on windows aren't you! Please see the note at the top of the file (
`which` = `where` on windows).

### $PATH?
You're on windows aren't you! Please see the note at the top of the file (
`echo $PATH` == `echo %PATH%` on windows).
