import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Human_Label_Tool(QWidget):

    def __init__(self):
        super(Human_Label_Tool, self).__init__()
        self.setFocusPolicy(Qt.StrongFocus)
        self.ui_init()
        self.file_buffer_init()

    def ui_init(self):
        self.title_text = QLabel('Title')
        title_font = QFont('Times New Roman', 30, QFont.Bold)
        self.title_text.setFont(title_font)

        self.section_text = QLabel('Section')
        section_font = QFont('Times New Roman', 20, QFont.Bold)
        self.section_text.setFont(section_font)

        self.display_board = QTextBrowser()

        self.load_file_button = QPushButton('Load File')
        self.load_file_button.clicked.connect(self.open_file)
        self.dump_file_button = QPushButton('Dump Result')
        self.dump_file_button.clicked.connect(self.save_file)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.load_file_button)
        button_layout.addWidget(self.dump_file_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_text)
        main_layout.addWidget(self.section_text)
        main_layout.addWidget(self.display_board)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def file_buffer_init(self):
        self.title_dict = {}
        self.section_dict = {}
        self.read_buffer = []
        self.write_buffer = []
        self.line_pointer = -1
        

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Left:
            self.write_buffer[self.line_pointer] = 0
            self.down()
        elif e.key() == Qt.Key_Right:
            self.write_buffer[self.line_pointer] = 1
            self.down()
        elif e.key() == Qt.Key_Up:
            self.up()
        elif e.key() == Qt.Key_Down:
            self.down()


    def down(self):
        if self.line_pointer >= len(self.read_buffer) -1:
            return
        self.line_pointer += 1
        if self.line_pointer in self.section_dict:
            self.section_text.setText(self.section_dict[self.line_pointer][1])
            if self.line_pointer in self.title_dict:
                self.title_text.setText(self.title_dict[self.line_pointer][1])
        self.display_board.setText(self.read_buffer[self.line_pointer])

    def up(self):
        if self.line_pointer <= 0:
            return
        if self.line_pointer in self.section_dict:
            self.section_text.setText(self.section_dict[self.line_pointer][0])
            if self.line_pointer in self.title_dict:
                self.title_text.setText(self.title_dict[self.line_pointer][0])
        self.line_pointer -= 1
        self.display_board.setText(self.read_buffer[self.line_pointer])

    def open_file(self):
        fileName,fileType = QtWidgets.QFileDialog.getOpenFileName(None, "choose file", os.getcwd(), "All Files(*)")
        if not fileName:
            return
        
        # Read the file
        read_file = open(fileName)
        pre_section = ''
        pre_title = ''
        self.read_buffer = []
        for line in read_file:
            line = line.strip()
            line_num = len(self.read_buffer)
            if not line:
                continue
            if line[0] == '!':
                self.title_dict[line_num] = [pre_title, line[1:]]
                pre_title = line[1:]
            elif line[0] == '>':
                self.section_dict[line_num] = [pre_section, line[1:]]
                pre_section = line[1:]
            else:
                self.read_buffer.append(line)
        
        self.write_buffer = [0] * len(self.read_buffer)
        self.line_pointer = -1
        self.down()


    def save_file(self):
        fileName,fileType = QtWidgets.QFileDialog.getSaveFileName(None, "choose file", os.path.join(os.getcwd(),'out.txt'), "All Files(*)")
        if not fileName:
            return
        
        with open(fileName, 'w', encoding='utf-8') as file_save:
            content = []
            for i in range(len(self.read_buffer)):
                if i in self.title_dict:
                    content.append('!%s' % self.title_dict[i][1])
                if i in self.section_dict:
                    content.append('>%s' % self.section_dict[i][1])
                content.append('%s\t%d' % (self.read_buffer[i], self.write_buffer[i]))

            file_save.write('\n'.join(content))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Human_Label_Tool()
    demo.show()
    sys.exit(app.exec_())