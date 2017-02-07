# CX neural compass paper
Full files for reproducing the experiments in the PLOS One paper: A Computational Model of the Integration of Landmarks and Motion in the Insect Central Complex

Linux only supported

## Installing toolchain

### SpineML (simulation)

Install SpineML / SpineCreator (see http://spineml.github.io/ for information).

### Beeworld (simulation)

The model requires a simple raytracing environment called BeeWorld to provide input. The source code can be downloaded here:

https://github.com/ajc158/beeworld

Beeworld is configured by XML files which are loaded once the GUI is running. These can be found in the beeworld_xmls directory.

Please note, by default the XML files specify to hide the bee view in the GUI for speed reasons. This can be changed by modifying the following tag in the XML files to (default value is 0.0):

``` <DisplayScaling value="1.0"/> ``` 

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

## Data logs

To save re-running all experiments the logs for all the simulations described in the paper are in this repository. The logs for Experiments 1 & 2 can be found in ``` data/static_weight_logs ``` and the logs for Experiment 3 are in individual directories in ``` data ```.

## Analysis

### Loading SpineML log files into Python and Matlab/Octave

We provide a simple python script for loading SML log files - this can be found at ```data/clustering_analysis/data_processing_scripts/sml_log_parser.py``` and usage is demonstrated in ```analyse_ring.py``` in the same directory. To load into Matlab/Ocatve you can load the SML log ```_log.bin``` files as binary data. The format of the log files is described in the associated ```_logrep.xml``` files. An example can be found in ```data/non_param_analysis_of_learning.m```.

### Ring attractor vs real heading plots

The log data is logged under your output directory ``` /log/ ``` folder (see SpineCreator setup if you don't know where this is for static model, for learning this is where you asked the script to output to). Simply load into your favourite plotting software (I use Veusz - http://home.gna.org/veusz/) as binary data and modulo by 1080 deg before plotting. the relevant logs are:

Ring attractor direction: ``` ring_direction_av_log* ```

Actual heading direction: ``` changes_for_batch_a_log* ```

### Correlation analysis of the ring attractor vs the actual heading

Analysis of the correlation between the ring attractor direction and the actual heading is undertaken by ``` analyse_corr.py ```, which can be found in each of the results directories under ``` data ```. This script generates two ``` .csv ``` files, ``` corr_mean_sd.csv ``` with the means and standard deviations for each run, and ``` corr_all.csv ``` for the last simulation run (runJ) with three columns: change in ring direction over each 10ms period, change in actual direction over the same, absolute actual direction. In addition a plot of these values with the final column represented by colour, as seen in the paper, is produced.

### Circular mean and sd

We provide an Octave script to analyse the mean and standard deviation of a single simulation run at:

``` data/analyse_mean_and_sd.m ```

The path to the simulation run logs must be modified to analyse each simulation run.

### Non-parametric comparisons

We provide a script to analyse the non-parametric variance analysis comparisons at:

``` data/non_param_analysis_of_learning.m ```

### Analysis of learned weights

The first stage in analysing the learned weights is to compute the preferred ring directions of the weights for each of the input receptive fields. This is undertaken using the ``` analyse_ring.py ``` script which is found in the ``` data/clustering_analysis/data_processing_scripts/ ``` directory. Note that this script requires ``` sml_log_parser.py ``` file in the same directory to run, and only analyses logs in the same directory as it by default. This script outputs two ``` .csv ``` files: ``` datal.csv ``` and ``` datar.csv ```. These files contain one column for each of the left and right RF respectively, with the rows representing each millisecond of the simulation. These logs can be used to create the polar plots from the paper.


The second stage of analysis is the clustering analysis, and this is undertaken by ``` cluster_data.py ``` in the ``` data/clustering_analysis/data_processing_scripts/ ``` directory. This script takes the output of ``` analyse_ring.py ``` as input, so must be in the same directory as that output by default. This script generates cluster plots as seen in the paper.
