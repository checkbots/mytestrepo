#!/bin/sh
export ws=`pwd`
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
export LIB1=${ws}/lib

export CLASSPATH=$CLASSPATH:$JAVA_HOME/lib/tools.jar:$LIB1/pyAntTasks-1.3.3.jar
export PYTHONPATH=$PYTHONPATH:/usr/local/bin

py.test python_proj1/



