#!/bin/sh
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
export LIB1=/eclipse/eclipse/plugins/org.apache.ant_1.8.4.v201303080030/lib

export CLASSPATH=$CLASSPATH:$JAVA_HOME/lib/tools.jar:$LIB1/pyAntTasks-1.3.3.jar
export PYTHONPATH=$PYTHONPATH:/usr/local/bin
echo "calling the build script"

echo "*****************************"
echo "Calling a python script..."
echo ""
ws=`pwd`
${ws}/test.py
echo ""
echo "*****************************"
echo ""

ant -f Java_Proj1/build.xml
ant -f python_proj1/build.xml
