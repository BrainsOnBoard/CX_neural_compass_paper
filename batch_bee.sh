#!/bin/bash

if [ "$#" -ne "4" ]; then
	echo "Usage: batch_bee.sh TYPE(sing,pano,2bar) SPINEML_2_BRAHMS_PATH OUT_PATH SYSTEMML_PATH"
	exit -1
fi

if [ "$1" = "pano" ]; then
	echo "Panorama experiments running"
	stim_type=("pano")
	stim_type_expt=("2")
elif [ "$1" = "sing" ]; then
	echo "Single bar experiments running"
	stim_type=("sing")
	stim_type_expt=("1")
elif [ "$1" = "2bar" ]; then
	echo "Two bar experiments running"
	stim_type=("2bar")
	stim_type_expt=("1")
else
	echo "Unknown experiment type, valide types are pano, sing, and 2bar"
	exit -1
fi

# check beeworld is running
ps -ax | grep [b]eeworld &> /dev/null
if [ $? == 0 ]; then
   echo "Running Beeworld found! Continuing..."
else 
	echo "Beeworld not running, please run beeworld and try again"
	exit -1
fi

S2B_PATH=$2
OUT_PATH=$3
SYSTEMML_INSTALL_PATH=$4
MDL_DIR=$PWD

run_nums=("1" "2" "3" "4" "5" "6" "7" "8" "9" "10")

for ((r=0;r<${#stim_type[@]};++r)); do
	for ((i=0;i<${#run_nums[@]};++i)); do
		sleep 1
		cd $S2B_PATH
		PATH=/bin:/usr/bin:/usr/local/bin:${SYSTEMML_INSTALL_PATH}/BRAHMS/bin/brahms/:. BRAHMS_NS=${SYSTEMML_INSTALL_PATH}/Namespace SYSTEMML_INSTALL_PATH=${SYSTEMML_INSTALL_PATH} ./convert_script_s2b -w $S2B_PATH -m ${MDL_DIR} -e ${stim_type_expt[r]} -o ${OUT_PATH}/${stim_type[r]}/drosphs${run_nums[i]}/
		cd -
	done
done


