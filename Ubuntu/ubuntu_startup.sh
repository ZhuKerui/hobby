# install input method "rime"
sudo apt install ibus-rime
sudo apt install librime-data-pinyin-simp
# Go to ~/.config/ibus/rime/build, modify the schema order in default.yaml, move the luna_pinyin_simp to the top

# install software using ubuntu-make
echo "add ubuntu-make tools"
sudo add-apt-repository ppa:lyzardking/ubuntu-make
sudo apt update
sudo apt install ubuntu-make
echo "install vscode"
umake ide visual-studio-code
echo "install clion"
umake ide clion
echo "install arduino"
sudo apt install arduino
echo "install Android Studio"
umake android
echo "install libreoffice"
sudo apt install libreoffice
echo "install vim"
sudo apt install vim
echo "setup C/C++ environment"
sudo apt install build-essential
echo "install git"
sudo apt install git
echo "install zsh and oh-my-zsh"
sudo apt install zsh
chsh -s /bin/zsh
sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
echo "install pip3"
sudo apt install python3-pip
echo "install gparted"
sudo apt install gparted
echo "install workrave"
sudo apt install workrave
echo "install video player VLC"
sudo apt install vlc
echo "install screen"
sudo apt install screen
echo "install latex"
sudo apt install texlive-full
echo "install freeplane"
sudo apt install freeplane
# install netease cloud music
# go to https://music.163.com/#/download
