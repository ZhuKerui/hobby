ssh-keygen -o
# install input method "rime"
sudo apt install ibus-rime
sudo apt install librime-data-pinyin-simp
# Go to ~/.config/ibus/rime/build, modify the schema order in default.yaml, move the luna_pinyin_simp to the top

echo "install vscode"
sudo snap install code --classic
echo "install clion"
sudo snap install clion --classic
echo "install Android Studio"
sudo snap install android-studio --classic
echo "install vim"
sudo apt install vim
echo "setup C/C++ environment"
sudo apt install build-essential
sudo apt install cmake
echo "install git"
sudo apt install git
echo "install zsh and oh-my-zsh"
sudo apt install zsh
chsh -s /bin/zsh
sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
echo "install pip3"
sudo apt install python3-pip
mkdir ~/.pip
touch ~/.pip/pip.conf
echo "[global]" >> ~/.pip/pip.conf
echo "index-url = https://pypi.tuna.tsinghua.edu.cn/simple/" >> ~/.pip/pip.conf
echo "trusted-host = pypi.tuna.tsinghua.edu.cn" >> ~/.pip/pip.conf
echo "install virtualenvwrapper"
pip3 install virtualenv
pip3 install virtualenvwrapper
echo "export WORKON_HOME=~/Envs" >> ~/.zshrc
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.zshrc
echo "export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv" >> ~/.zshrc
echo "source ~/.local/bin/virtualenvwrapper.sh" >> ~/.zshrc
echo "install gparted"
sudo apt install gparted
echo "install workrave"
sudo apt install workrave
echo "install video player VLC"
sudo snap install vlc
echo "install screen"
sudo apt install screen
echo "install latex"
sudo apt install texlive-full
echo "install freeplane"
sudo apt install freeplane
echo "install gimp"
sudo snap install gimp
echo "install java"
sudo apt-get remove --purge icedtea-\* openjdk-\*
sudo apt install openjdk-11-jdk
echo "install maven"
sudo apt install maven
