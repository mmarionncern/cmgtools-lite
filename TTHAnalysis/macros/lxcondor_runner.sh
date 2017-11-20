#!/bin/bash
if [[ "$VO_CMS_SW_DIR" != "" ]] && test -f $VO_CMS_SW_DIR/cmsset_default.sh; then 
  source $VO_CMS_SW_DIR/cmsset_default.sh
fi;
export SCRAM_ARCH=slc6_amd64_gcc530
WORK=$1; shift
SRC=$1; shift
cd $SRC; 
pwd
eval $(scramv1 runtime -sh);
cd $WORK;
pwd
ulimit -c 0
##local keras python
#if [ -n "$2" ]; then
source /afs/cern.ch/work/m/mmarionn/private/Keras/py276v2/bin/activate
echo "python activated"
echo "command : ",$*
#fi
exec $*
#if [ -n "$2" ]; then
deactivate
#fi
