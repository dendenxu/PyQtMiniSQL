import sys
import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *

"""

Style number 0 is Default
Style number 1 is Comment
Style number 2 is Comment line
Style number 3 is JavaDoc style comment
Style number 4 is Number
Style number 5 is Keyword
Style number 6 is Double-quoted string
Style number 7 is Single-quoted string
Style number 8 is SQL*Plus keyword
Style number 9 is SQL*Plus prompt
Style number 10 is Operator
Style number 11 is Identifier
Style number 12 is 
Style number 13 is SQL*Plus comment
Style number 14 is 
Style number 15 is # comment line
Style number 16 is 
Style number 17 is JavaDoc keyword
Style number 18 is JavaDoc keyword error
Style number 19 is User defined 1
Style number 20 is User defined 2
Style number 21 is User defined 3
Style number 22 is User defined 4
Style number 23 is Quoted identifier
Style number 24 is Quoted operator

call s:h("Comment", { "fg": s:comment_grey, "gui": "italic", "cterm": "italic" }) " any comment
call s:h("Constant", { "fg": s:cyan }) " any constant
call s:h("String", { "fg": s:green }) " a string constant: "this is a string"
call s:h("Character", { "fg": s:green }) " a character constant: 'c', '\n'
call s:h("Number", { "fg": s:dark_yellow }) " a number constant: 234, 0xff
call s:h("Boolean", { "fg": s:dark_yellow }) " a boolean constant: TRUE, false
call s:h("Float", { "fg": s:dark_yellow }) " a floating point constant: 2.3e10
call s:h("Identifier", { "fg": s:red }) " any variable name
call s:h("Function", { "fg": s:blue }) " function name (also: methods for classes)
call s:h("Statement", { "fg": s:purple }) " any statement
call s:h("Conditional", { "fg": s:purple }) " if, then, else, endif, switch, etc.
call s:h("Repeat", { "fg": s:purple }) " for, do, while, etc.
call s:h("Label", { "fg": s:purple }) " case, default, etc.
call s:h("Operator", { "fg": s:purple }) " sizeof", "+", "*", etc.
call s:h("Keyword", { "fg": s:red }) " any other keyword
call s:h("Exception", { "fg": s:purple }) " try, catch, throw
call s:h("PreProc", { "fg": s:yellow }) " generic Preprocessor
call s:h("Include", { "fg": s:blue }) " preprocessor #include
call s:h("Define", { "fg": s:purple }) " preprocessor #define
call s:h("Macro", { "fg": s:purple }) " same as Define
call s:h("PreCondit", { "fg": s:yellow }) " preprocessor #if, #else, #endif, etc.
call s:h("Type", { "fg": s:yellow }) " int, long, char, etc.
call s:h("StorageClass", { "fg": s:yellow }) " static, register, volatile, etc.
call s:h("Structure", { "fg": s:yellow }) " struct, union, enum, etc.
call s:h("Typedef", { "fg": s:yellow }) " A typedef
call s:h("Special", { "fg": s:blue }) " any special symbol
call s:h("SpecialChar", {}) " special character in a constant
call s:h("Tag", {}) " you can use CTRL-] on this
call s:h("Delimiter", {}) " character that needs attention
call s:h("SpecialComment", { "fg": s:comment_grey }) " special things inside a comment
call s:h("Debug", {}) " debugging statements
call s:h("Underlined", { "gui": "underline", "cterm": "underline" }) " text that stands out, HTML links
call s:h("Ignore", {}) " left blank, hidden
call s:h("Error", { "fg": s:red }) " any erroneous construct
call s:h("Todo", { "fg": s:purple }) " anything that needs extra attention; mostly the keywords TODO FIXME and XXX
" +---------------------------------------------+
" |  Color Name  |         RGB        |   Hex   |
" |--------------+--------------------+---------|
" | Black        | rgb(40, 44, 52)    | #282c34 |
" |--------------+--------------------+---------|
" | White        | rgb(171, 178, 191) | #abb2bf |
" |--------------+--------------------+---------|
" | Light Red    | rgb(224, 108, 117) | #e06c75 |
" |--------------+--------------------+---------|
" | Dark Red     | rgb(190, 80, 70)   | #be5046 |
" |--------------+--------------------+---------|
" | Green        | rgb(152, 195, 121) | #98c379 |
" |--------------+--------------------+---------|
" | Light Yellow | rgb(229, 192, 123) | #e5c07b |
" |--------------+--------------------+---------|
" | Dark Yellow  | rgb(209, 154, 102) | #d19a66 |
" |--------------+--------------------+---------|
" | Blue         | rgb(97, 175, 239)  | #61afef |
" |--------------+--------------------+---------|
" | Magenta      | rgb(198, 120, 221) | #c678dd |
" |--------------+--------------------+---------|
" | Cyan         | rgb(86, 182, 194)  | #56b6c2 |
" |--------------+--------------------+---------|
" | Gutter Grey  | rgb(76, 82, 99)    | #4b5263 |
" |--------------+--------------------+---------|
" | Comment Grey | rgb(92, 99, 112)   | #5c6370 |
" +---------------------------------------------+
"""

comment_grey = QColor("#5c6370")
gutter_grey = QColor("#4b5263")
cyan = QColor("#56b6c2")
magenta = QColor("c678dd")
blue = QColor("#61afef")
dark_yellow = QColor("#d19a66")
light_yellow = QColor("#e5c07b")
green = QColor("#98c379")
dark_red = QColor("#be5046")
light_red = QColor("#e06c75")
white = QColor("#abb2bf")
black = QColor("#282c34")
purple = QColor("#d55fdd")
font_name = "Ubuntu"
font_name_mono = "UbuntuMono Nerd Font"
base_font_point_size = 14


class MiniSQLLexer(QsciLexerSQL):
    def __init__(self):
        super(MiniSQLLexer, self).__init__()

        self.setDefaultColor(white)
        self.setDefaultPaper(black)
        self.default_font = QFont(font_name_mono)
        self.default_font.setItalic(False)
        self.default_font.setBold(False)
        self.default_font.setPointSize(base_font_point_size)
        self.setDefaultFont(self.default_font)
        self.setFont(self.default_font)
        # for i in range(25):
        #     color_change = 200
        #     print("Style number {} is {}".format(i, self.description(i)))
        #     if self.check_dark(self.color(i)):
        #         print("The color is a little bit darker, we'll lighten it.")
        #         print("Original color is {}, the lighter color should be {}.".format(
        #             self.color(i).name(),
        #             self.color(i).lighter(
        #                 color_change).name()))
        #         self.setColor(self.color(i).lighter(color_change), i)
        #     else:
        #         print("The color looks fine.")
        self.setColor(white, 0)
        self.comment_font = QFont(font_name_mono)
        self.comment_font.setPointSize(base_font_point_size * 0.9)
        self.comment_font.setItalic(True)
        self.comment_font.setBold(False)
        self.setColor(comment_grey, 1)
        self.setColor(comment_grey, 2)
        self.setFont(self.comment_font, 1)
        self.setFont(self.comment_font, 2)

        self.setColor(green, 6)
        self.setColor(green, 7)
        self.setColor(dark_yellow, 4)
        self.setColor(light_yellow, 8)
        self.setColor(light_red, 9)
        self.setColor(white, 11)
        self.setColor(blue, 5)
        self.keyword_font = QFont(font_name_mono)
        self.keyword_font.setBold(True)
        self.keyword_font.setItalic(True)
        self.keyword_font.setPointSize(14)
        self.setFont(self.keyword_font, 5)
        self.setColor(purple, 10)
        self.setColor(magenta, 3)
        self.setColor(comment_grey, 15)
        self.setColor(comment_grey, 13)

    # def check_dark(self, color: QColor):
    #     if color.red() >= 128 or color.green() >= 128 or color.blue() >= 128:
    #         return False
    #     else:
    #         return True


class CustomMainWindow(QMainWindow):
    def __init__(self):
        super(CustomMainWindow, self).__init__()

        # Window setup
        # --------------

        # 1. Define the geometry of the main window
        init_geometry = (300, 300, 800, 300)

        self.setGeometry(*init_geometry)
        self.setWindowTitle("miniSQL GUI")

        # 2. Create frame and layout
        self.frame = QFrame(self)
        self.layout = QVBoxLayout()
        self.frame.setLayout(self.layout)
        self.setCentralWidget(self.frame)
        self.myFontMono = QFont()
        self.myFontMono.setPointSize(base_font_point_size)
        # self.__myFontMono.setFamily("CMU Typewriter Text BoldItalic")
        self.myFontMono.setFamily(font_name_mono)
        self.myFontUI = QFont()
        self.myFontUI.setPointSize(base_font_point_size)
        self.myFontUI.setFamily(font_name)

        # 3. Place a button
        self.button_run = QPushButton("Run")
        self.button_run.setFixedWidth(100)
        self.button_run.setFixedHeight(50)
        self.button_run.clicked.connect(self.__btn_action)
        self.button_run.setFont(self.myFontUI)
        self.layout.addWidget(self.button_run)

        # adding the SQL lexer to the editor
        self.lexer = MiniSQLLexer()
        # self.lexer.setFont(self.myFontMono)
        # QScintilla editor setup
        # ------------------------

        # ! Make instance of QsciScintilla class!
        self.editor = QsciScintilla()
        self.editor.setUtf8(True)  # Set encoding to UTF-8
        self.editor.setFont(self.myFontUI)  # Will be overridden by lexer!
        self.editor.setLexer(self.lexer)
        self.editor.setMarginsBackgroundColor(black.darker(120))
        self.editor.setMarginsForegroundColor(white.darker(120))
        self.editor.setMarginType(0, QsciScintilla.NumberMargin)
        self.editor.setMarginWidth(0, "000")
        self.editor.setMarginsFont(self.myFontMono)
        self.editor.setScrollWidth(10)  # I'd like to set this to 0, however it doesn't work
        self.editor.setScrollWidthTracking(True)
        # self.editor.setCaretLineBackgroundColor(black.lighter())
        self.editor.setCaretForegroundColor(white)
        self.editor.setCaretWidth(3)
        # ! Add editor to layout !
        self.layout.addWidget(self.editor)

        self.show()

    ''''''

    def __btn_action(self):
        print("You've pressed the run button, will it run?")
        content = self.editor.text()
        print(content)
        # print(self.__editor.scrollWidth())

    ''''''


''' End Class '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    myGUI = CustomMainWindow()
    sys.exit(app.exec_())

''''''
