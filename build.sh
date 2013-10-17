#!/bin/sh
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
echo "calling the build script"
ws=`pwd`
${ws}/test.py
ant -f Java_Proj1/build.xml
