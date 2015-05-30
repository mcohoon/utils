#!/bin/bash

function DarwinPackerInstall {
  # Install on Darwin OS X

  echo "Downloading Packer"
  `curl -L https://dl.bintray.com/mitchellh/packer/packer_0.7.5_darwin_amd64.zip > packer_0.7.5_darwin.zip`

  if [ -s "packer_0.7.5_darwin.zip" ]; then
    echo "installing Packer to /usr/local/bin"
    sudo unzip packer_0.7.5_darwin.zip -d /usr/local/bin
  else
    echo "packer_0.7.5_darwin.zip filesize was 0, download error"
  fi

}

function UbuntuPackerInstall {
  # Install on Ubuntu

  echo "Downloading Packer"
  `wget https://dl.bintray.com/mitchellh/packer/packer_0.7.5_linux_386.zip`

  echo "installing unzip"
  sudo apt-get install unzip

  which unzip
  if [ $? -ne 0 ]; then
    echo "unzip did not install properly"
    exit 1
  fi

  echo "installing Packer to /usr/local/sbin"
  unzip packer_0.7.5_linux_386.zip -d /usr/local/sbin
}

function addToPath {

# because executing a shell script causes fork and the spawning of a 
# subshell -- there is no way to source the current shell's ~/.profile
# or ~/.bashrc  from a shell script.

  which packer
  if [ $? -ne 0 ]; then
    echo PATH=$PATH:~/packer >> ~/.profile
    source ~/.profile
    echo "added packer to path $PATH"
    echo "Please source ~/.profile"
  fi
}

UNAME_STRING=`uname`
echo "$UNAME_STRING here"
if [ $UNAME_STRING == 'Darwin'  ]; then
  DarwinPackerInstall
elif [ $UNAME_STRING == 'Linux'  ]; then
  UbuntuPackerInstall
fi

#packerInstall
#addToPath
