#!/bin/bash 
test $# -ne 1 && echo "usage: $0 <tensorflow-revision>" && exit
revision=$1
build_subfolder=tensorflow/tensorflow/lite/tools/make
if [ ! -d tensorflow ]; then
    git clone "https://github.com/tensorflow/tensorflow.git"
fi
pushd $PWD >/dev/null
cd tensorflow && git checkout $revision && cd ..
source "${build_subfolder}/download_dependencies.sh"
popd >/dev/null
for dependency in $(ls -1 "${build_subfolder}/downloads"); do
    mkdir -p $dependency/source
    cp -rv "${build_subfolder}/downloads/${dependency}"/* $dependency/source
done
