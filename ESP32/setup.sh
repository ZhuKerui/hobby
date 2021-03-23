mkdir -p ~/esp
cd ~/esp
git clone --recursive git://github.com/espressif/esp-idf.git
cd esp-idf
./install.sh
. $HOME/esp/esp-idf/export.sh
