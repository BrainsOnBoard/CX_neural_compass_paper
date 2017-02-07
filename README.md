# CX_neural_compass_paper
Full files for reproducing the experiments in the PLOS One paper

Linux only supported

## Installing toolchain

### SpineML (simulation)

Install SpineML / SpineCreator (see http://spineml.github.io/ for information).

### Beeworld (simulation)

The model requires a simple raytracing environment called BeeWorld to provide input. The source code can be downloaded here:

https://github.com/ajc158/beeworld

Beeworld is configured by XML files which are loaded once the GUI is running. These can be found in the beeworld_xmls directory.

Please note, by default the XML files specify to hide the bee view in the GUI for speed reasons. This can be changed by modifying the following tag in the XML files to (default value is 0.0):

```<DisplayScaling value="1.0"/>``` 

### Octave/Matlab / Circular Statistics Toolbox (analysis)

Installing Matlab is fun ;-) - I assume you have it installed, otherwise just use Octave.

Octave can be installed from this site:

https://www.gnu.org/software/octave/

The Circular Statistics Toolbox can be found here:

https://uk.mathworks.com/matlabcentral/fileexchange/10676-circular-statistics-toolbox--directional-statistics-

This should be installed in the data subdirectory in a folder named circ_toolbox for seamless use.

### Python (SciPy) (analysis)

Analysis requires SciPy and SKLearn for clustering:

SciPy: https://www.scipy.org/

SKLearn: http://scikit-learn.org/stable/

### Veusz

I plot using Veusz, and the clustering data is embedded in Veusz files. These are plaintext so you could extract it or simply load the files into Veusz (or run the clustering analysis again ;-)):

http://home.gna.org/veusz/

## Running experiments

### Static weight experiments

For the static weight experiments simply load the .proj file in ```model_static``` into SpineCreator. In the 'Expts' tab on the right of the SpineCreator UI there are three experiments and descriptions. Select an experiment by clicking on it and it will turn grey and the description will appear. Before running the experiment you must run BeeWorld and load the relevant XML file. Once Beeworld is set up click the 'Run experiment button' to run the experiment, a progress bar will show you your progress (120s takes ~ 40 mins on a quad core i7). The log files are written to your SpineML_2_BRAHMS working directory (configured when installing SpineCreator).

### Learning experiments

As the learning experiments require batched runs we provide a Bash script to simplify simulation. The script can be found with the model in ```model_learn``` and is named ```batch_bee.sh``` (please forgive the bee naming convention for Drosophila simulations!). running this script without arguments will produce instructions for usage. 

## Analysis

### Loading SpineML log files into Python and Matlab/Octave

We provide a simple python script for loading SML log files - this can be found at ```data/clustering_analysis/data_processing_scripts/sml_log_parser.py``` and usage is demonstrated in ```analyse_ring.py``` in the same directory. To load into Matlab/Ocatve you can load the SML log ```_log.bin``` files as binary data. The format of the log files is described in the associated ```_logrep.xml``` files. An example can be found in ```data/non_param_analysis_of_learning.m```.

### Ring attractor vs real heading plots

The log data is logged under your output directory ```/log/``` folder (see SpineCreator setup if you don't know where this is for static model, for learning this is where you asked the script to output to). Simply load into your favourite plotting software (I use Veusz - http://home.gna.org/veusz/) as binary data and modulo by 1080 deg before plotting. the relevant logs are:

Ring attractor direction: ```ring_direction_av_log*```

Actual heading direction: ```changes_for_batch_a_log*```

### Circular mean and sd

We provide an Octave script to analyse the mean and standard deviation of a single simulation run at:

```data/analyse_mean_and_sd.m```

The path to the simulation run logs must be modified before running this script.

### Non-parametric comparisons

We provide a script to analyse the non-parametric comparisons at:


