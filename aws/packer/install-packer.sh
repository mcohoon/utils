/bin/bash

function packerInstall {
  echo "Downloading Packer"
  `wget https://dl.bintray.com/mitchellh/packer/packer_0.7.5_linux_386.zip`

  echo "installing unzip"
  sudo apt-get install unzip

  which unzip
  if [ $? -ne 0 ]; then
    echo "unzip did not install properly"
    exit 1
  fi

  echo "installing Packer"
  unzip packer_0.7.5_linux_386.zip -d packer
}

function addToPath {
  which packer
  if [ $? -ne 0 ]; then
    echo PATH=$PATH:~/packer >> ~/.profile
    source ~/.profile
    echo "added packer to path $PATH"
    echo "Please source ~/.profile"
  fi
}

packerInstall
addToPath
