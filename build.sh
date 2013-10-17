#!/bin/sh
echo "calling the build script"
ws=`pwd`
${ws}/test.py
ant -f Java_Proj1/build.xml
