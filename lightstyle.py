'''
 * The MIT License (MIT)
 *
 * Copyright (c) <2013-2014> <Colin Duquesnoy>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:

 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.

 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
'''

css = '''
QToolTip
{
    border: 1px solid #76797C;
    background-color: rgb(90, 102, 117);;
    color: white;
    padding: 5px;
    opacity: 200;
}

QWidget
{
    color: #161616;
    background-color: #ededed;
    selection-background-color:#3daee9;
    selection-color: #161616;
    background-clip: border;
    border-image: none;
    border: 0px transparent black;
    outline: 0;
    background-image:url("wallpapers/img1.jpg");
    background-position: right;
}

QWidget:item:hover
{
    background-color: #3daee9;
    color: #161616;
}

QWidget:item:selected
{
    background-color: #3daee9;
}

QCheckBox
{
    background:none;
    spacing: 5px;
    outline: none;
    color: #161616;
    margin-bottom: 2px;
}

QCheckBox::indicator,
QGroupBox::indicator
{
    width: 18px;
    height: 18px;
}
QGroupBox::indicator
{
    margin-left: 2px;
}

QCheckBox::indicator:unchecked
{
    image: url(icons/checkbox_unchecked.png);
}

QCheckBox::indicator:unchecked:hover,
QCheckBox::indicator:unchecked:focus,
QCheckBox::indicator:unchecked:pressed,
QGroupBox::indicator:unchecked:hover,
QGroupBox::indicator:unchecked:focus,
QGroupBox::indicator:unchecked:pressed
{
  border: none;
    image: url(icons/checkbox_unchecked_focus.png);
}

QCheckBox::indicator:checked
{
    image: url(icons/checkbox_checked.png);
}

QCheckBox::indicator:checked:hover,
QCheckBox::indicator:checked:focus,
QCheckBox::indicator:checked:pressed,
QGroupBox::indicator:checked:hover,
QGroupBox::indicator:checked:focus,
QGroupBox::indicator:checked:pressed
{
  border: none;
    image: url(icons/checkbox_checked_focus.png);
}


QCheckBox::indicator:indeterminate
{
    image: url(icons/checkbox_indeterminate.png);
}

QCheckBox::indicator:indeterminate:focus,
QCheckBox::indicator:indeterminate:hover,
QCheckBox::indicator:indeterminate:pressed
{
    image: url(icons/checkbox_indeterminate_focus.png);
}

QCheckBox::indicator:checked:disabled,
QGroupBox::indicator:checked:disabled
{
    image: url(icons/checkbox_checked_disabled.png);
}

QCheckBox::indicator:unchecked:disabled,
QGroupBox::indicator:unchecked:disabled
{
    image: url(icons/checkbox_unchecked_disabled.png);
}

QRadioButton
{
    spacing: 5px;
    outline: none;
    color: #161616;
    margin-bottom: 2px;
}

QRadioButton:disabled
{
    color: #76797C;
}
QRadioButton::indicator
{
    width: 21px;
    height: 21px;
}

QRadioButton::indicator:unchecked
{
    image: url(icons/radio_unchecked.png);
}


QRadioButton::indicator:unchecked:hover,
QRadioButton::indicator:unchecked:focus,
QRadioButton::indicator:unchecked:pressed
{
    border: none;
    outline: none;
    image: url(icons/radio_unchecked_focus.png);
}

QRadioButton::indicator:checked
{
    border: none;
    outline: none;
    image: url(icons/radio_checked.png);
}

QRadioButton::indicator:checked:hover,
QRadioButton::indicator:checked:focus,
QRadioButton::indicator:checked:pressed
{
    border: none;
    outline: none;
    image: url(icons/radio_checked_focus.png);
}

QRadioButton::indicator:checked:disabled
{
    outline: none;
    image: url(icons/radio_checked_disabled.png);
}

QRadioButton::indicator:unchecked:disabled
{
    image: url(icons/radio_unchecked_disabled.png);
}


QMenuBar
{
    background-color: #ededed;
    color: #161616;
}

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background: transparent;
    border: 1px solid #76797C;
}

QMenuBar::item:pressed
{
    border: 1px solid #76797C;
    background-color: #3daee9;
    color: #161616;
    margin-bottom:-1px;
    padding-bottom:1px;
}

QMenu
{
    border: 1px solid #76797C;
    color: #161616;
    margin: 2px;
}

QMenu::icon
{
    margin: 5px;
}

QMenu::item
{
    padding: 5px 30px 5px 30px;
    margin-left: 5px;
    border: 1px solid transparent; /* reserve space for selection border */
}

QMenu::item:selected
{
    color: #161616;
}

QMenu::separator {
    height: 2px;
    background: lightblue;
    margin-left: 10px;
    margin-right: 5px;
}

QMenu::indicator {
    width: 18px;
    height: 18px;
}

/* non-exclusive indicator = check box style indicator
   (see QActionGroup::setExclusive) */
QMenu::indicator:non-exclusive:unchecked {
    image: url(icons/checkbox_unchecked.png);
}

QMenu::indicator:non-exclusive:unchecked:selected {
    image: url(icons/checkbox_unchecked_disabled.png);
}

QMenu::indicator:non-exclusive:checked {
    image: url(icons/checkbox_checked.png);
}

QMenu::indicator:non-exclusive:checked:selected {
    image: url(icons/checkbox_checked_disabled.png);
}

/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */
QMenu::indicator:exclusive:unchecked {
    image: url(icons/radio_unchecked.png);
}

QMenu::indicator:exclusive:unchecked:selected {
    image: url(icons/radio_unchecked_disabled.png);
}

QMenu::indicator:exclusive:checked {
    image: url(icons/radio_checked.png);
}

QMenu::indicator:exclusive:checked:selected {
    image: url(icons/radio_checked_disabled.png);
}

QMenu::right-arrow {
    margin: 5px;
    image: url(icons/right_arrow.png)
}


QWidget:disabled
{
    color: #454545;
    background-color: #ededed;
}

QAbstractItemView
{
    alternate-background-color: #ededed;
    color: #161616;
    border: 1px solid 3A3939;
    border-radius: 2px;
}

QWidget:focus, QMenuBar:focus
{
    border: 1px solid #3daee9;
}

QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus
{
    border: none;
}

QLineEdit
{
    background:none;
    background:rgba(255,255,255,0.5);
    padding: 5px;
    border-style: solid;
    border: 1px solid #76797C;
    border-radius: 2px;
    color: #161616;
}

QGroupBox {
    border:1px solid #76797C;
    border-radius: 2px;
    margin-top: 20px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 10px;
}

QAbstractScrollArea
{
    border-radius: 2px;
    border: 1px solid #76797C;
    background-color: transparent;
}

QScrollBar:horizontal
{
    height: 15px;
    margin: 3px 15px 3px 15px;
    border: 1px transparent #2A2929;
    border-radius: 4px;
    background-color: #2A2929;
}

QScrollBar::handle:horizontal
{
    background-color: #605F5F;
    min-width: 5px;
    border-radius: 4px;
}

QScrollBar::add-line:horizontal
{
    margin: 0px 3px 0px 3px;
    border-image: url(icons/right_arrow_disabled.png);
    width: 10px;
    height: 10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal
{
    margin: 0px 3px 0px 3px;
    border-image: url(icons/left_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on
{
    border-image: url(icons/right_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}


QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on
{
    border-image: url(icons/left_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{
    background: none;
}


QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
    background: none;
}

QScrollBar:vertical
{
    background-color: #2A2929;
    width: 15px;
    margin: 15px 3px 15px 3px;
    border: 1px transparent #2A2929;
    border-radius: 4px;
}

QScrollBar::handle:vertical
{
    background-color: #605F5F;
    min-height: 5px;
    border-radius: 4px;
}

QScrollBar::sub-line:vertical
{
    margin: 3px 0px 3px 0px;
    border-image: url(icons/up_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical
{
    margin: 3px 0px 3px 0px;
    border-image: url(icons/down_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
{

    border-image: url(icons/up_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}


QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
{
    border-image: url(icons/down_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
{
    background: none;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
    background: none;
}

QTextEdit
{
    background:none;
    background-color: #cccccc;
    color: #161616;
    border: 1px solid #76797C;
}

QPlainTextEdit
{
    background:none;
    background-color: #cccccc;;
    color: #161616;
    border-radius: 2px;
    border: 1px solid #76797C;
}

QHeaderView::section
{
    background-color: #76797C;
    color: #161616;
    padding: 5px;
    border: 1px solid #76797C;
}

QSizeGrip {
    image: url(icons/sizegrip.png);
    width: 12px;
    height: 12px;
}


QMainWindow::separator
{
    background:none;
    background-color: #ededed;
    color: white;
    padding-left: 4px;
    spacing: 2px;
    border: 1px dashed #76797C;
}

QMainWindow::separator:hover
{

    background-color: #787876;
    color: white;
    padding-left: 4px;
    border: 1px solid #76797C;
    spacing: 2px;
}

QMenu::separator
{
    height: 1px;
    background-color: #76797C;
    color: white;
    padding-left: 4px;
    margin-left: 10px;
    margin-right: 5px;
}


QFrame
{
    border-radius: 2px;
    border: 1px solid #76797C;
}

QFrame[frameShape="0"]
{
    border-radius: 2px;
    border: 1px transparent #76797C;
}

QStackedWidget
{
    border: 1px transparent black;
}

QToolBar {
    border: 1px transparent #393838;
    background: 1px solid #ededed;
    font-weight: bold;
}

QToolBar::handle:horizontal {
    image: url(icons/Hmovetoolbar.png);
}
QToolBar::handle:vertical {
    image: url(icons/Vmovetoolbar.png);
}
QToolBar::separator:horizontal {
    image: url(icons/Hsepartoolbar.png);
}
QToolBar::separator:vertical {
    image: url(icons/Vsepartoolbar.png);
}
QToolButton#qt_toolbar_ext_button {
    background: #58595a
}

QPushButton
{
    color: #161616;
    background-color: #ededed;
    background:rgba(255,255,255,0.3);
    border-width: 1px;
    border-color: #76797C;
    border-style: solid;
    padding: 5px;
    border-radius: 2px;
    outline: none;
}

QPushButton:disabled
{
    background-color: #ededed;
    background: none;
    border-width: 1px;
    border-color: #76797C;
    border-style: solid;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 10px;
    padding-right: 10px;
    border-radius: 2px;
    color: transparent;
    border: none;
}

QPushButton:focus {
    background:rgba(255,255,255,0.3);
    color: #161616;
    border-color: #76797C;
}

QPushButton:pressed
{
    background-color: #3daee9;
    padding-top: -15px;
    padding-bottom: -17px;
}

QComboBox
{
    background:rgba(255,255,255,0.35);
    selection-background-color: #3daee9;
    border-style: solid;
    border: 1px solid #76797C;
    border-radius: 2px;
    padding: 5px;
    min-width: 75px;
}

QPushButton:checked{
    background-color: #76797C;
    border-color: #6A6969;
}

QComboBox:hover,QPushButton:hover,QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover
{
    border: 1px solid #3daee9;
    color: #161616;
}

QComboBox:on
{
    padding-top: 3px;
    padding-left: 4px;
    selection-background-color: #4a4a4a;
}

QComboBox QAbstractItemView
{
    background-color: white;
    border-radius: 2px;
    border: 1px solid #76797C;
    selection-background-color: #3daee9;
}

QComboBox::drop-down
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;

    border-left-width: 0px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow
{
    image: url(icons/down_arrow_disabled.png);
}

QComboBox::down-arrow:on, QComboBox::down-arrow:hover,
QComboBox::down-arrow:focus
{
    image: url(icons/down_arrow.png);
}

QAbstractSpinBox {
    padding: 5px;
    border: 1px solid #76797C;
    background-color: #cccccc;
    color: #161616;
    border-radius: 2px;
    min-width: 75px;
}

QAbstractSpinBox:up-button
{
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: center right;
}

QAbstractSpinBox:down-button
{
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: center left;
}

QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {
    image: url(icons/up_arrow_disabled.png);
    width: 10px;
    height: 10px;
}
QAbstractSpinBox::up-arrow:hover
{
    image: url(icons/up_arrow.png);
}


QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off
{
    image: url(icons/down_arrow_disabled.png);
    width: 10px;
    height: 10px;
}
QAbstractSpinBox::down-arrow:hover
{
    image: url(icons/down_arrow.png);
}


QLabel
{
    background:none;
    border: 0px solid black;
}

QTabWidget{
    border: 0px transparent black;
}

QTabWidget::pane {
    border: 1px solid #76797C;
    padding: 5px;
    margin: 0px;
}

QTabWidget::tab-bar {
    left: 5px; /* move to the right by 5px */
}

QTabBar
{
    qproperty-drawBase: 0;
    border-radius: 3px;
}

QTabBar:focus
{
    border: 0px transparent black;
}

QTabBar::close-button  {
    image: url(icons/close.png);
    background: transparent;
}

QTabBar::close-button:hover
{
    image: url(icons/close-hover.png);
    background: transparent;
}

QTabBar::close-button:pressed {
    image: url(icons/close-pressed.png);
    background: transparent;
}

/* TOP TABS */
QTabBar::tab:top {
    color: #161616;
    border: 1px solid #76797C;
    border-bottom: 1px transparent black;
    background-color: #ededed;
    padding: 5px;
    min-width: 50px;
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
}

QTabBar::tab:top:!selected
{
    color: #161616;
    background-color: #54575B;
    border: 1px solid #76797C;
    border-bottom: 1px transparent black;
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;    
}

QTabBar::tab:top:!selected:hover {
    background-color: #3daee9;
}

/* BOTTOM TABS */
QTabBar::tab:bottom {
    color: #161616;
    border: 1px solid #76797C;
    border-top: 1px transparent black;
    background-color: #ededed;
    padding: 5px;
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px;
    min-width: 50px;
}

QTabBar::tab:bottom:!selected
{
    color: #161616;
    background-color: #54575B;
    border: 1px solid #76797C;
    border-top: 1px transparent black;
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px;
}

QTabBar::tab:bottom:!selected:hover {
    background-color: #3daee9;
}

/* LEFT TABS */
QTabBar::tab:left {
    color: #161616;
    border: 1px solid #76797C;
    border-left: 1px transparent black;
    background-color: #ededed;
    padding: 5px;
    border-top-right-radius: 2px;
    border-bottom-right-radius: 2px;
    min-height: 50px;
}

QTabBar::tab:left:!selected
{
    color: #161616;
    background-color: #54575B;
    border: 1px solid #76797C;
    border-left: 1px transparent black;
    border-top-right-radius: 2px;
    border-bottom-right-radius: 2px;
}

QTabBar::tab:left:!selected:hover {
    background-color: #3daee9;
}


/* RIGHT TABS */
QTabBar::tab:right {
    color: #161616;
    border: 1px solid #76797C;
    border-right: 1px transparent black;
    background-color: #ededed;
    padding: 5px;
    border-top-left-radius: 2px;
    border-bottom-left-radius: 2px;
    min-height: 50px;
}

QTabBar::tab:right:!selected
{
    color: #161616;
    background-color: #54575B;
    border: 1px solid #76797C;
    border-right: 1px transparent black;
    border-top-left-radius: 2px;
    border-bottom-left-radius: 2px;
}

QTabBar::tab:right:!selected:hover {
    background-color: #3daee9;
}

QTabBar QToolButton::right-arrow:enabled {
     image: url(icons/right_arrow.png);
 }

 QTabBar QToolButton::left-arrow:enabled {
     image: url(icons/left_arrow.png);
 }

QTabBar QToolButton::right-arrow:disabled {
     image: url(icons/right_arrow_disabled.png);
 }

 QTabBar QToolButton::left-arrow:disabled {
     image: url(icons/left_arrow_disabled.png);
 }


QDockWidget {
    background: #ededed;
    border: 1px solid #403F3F;
    titlebar-close-icon: url(icons/close.png);
    titlebar-normal-icon: url(icons/undock.png);
}

QDockWidget::close-button, QDockWidget::float-button {
    border: 1px solid transparent;
    border-radius: 2px;
    background: transparent;
}

QDockWidget::close-button:hover, QDockWidget::float-button:hover {
    background: rgba(255, 255, 255, 10);
}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {
    padding: 1px -1px -1px 1px;
    background: rgba(255, 255, 255, 10);
}

QTreeView, QListView
{
    background:none;
    border: 1px solid #76797C;
    background-color: #cccccc;
}

QTreeView:branch:selected, QTreeView:branch:hover
{
    background: url(icons/transparent.png);
}

QTreeView::branch:has-siblings:!adjoins-item {
    border-image: url(icons/transparent.png);
}

QTreeView::branch:has-siblings:adjoins-item {
    border-image: url(icons/transparent.png);
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: url(icons/transparent.png);
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
    image: url(icons/branch_closed.png);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings  {
    image: url(icons/branch_open.png);
}

QTreeView::branch:has-children:!has-siblings:closed:hover,
QTreeView::branch:closed:has-children:has-siblings:hover {
    image: url(icons/branch_closed-on.png);
    }

QTreeView::branch:open:has-children:!has-siblings:hover,
QTreeView::branch:open:has-children:has-siblings:hover  {
    image: url(icons/branch_open-on.png);
    }

QListView::item:!selected:hover, QTreeView::item:!selected:hover  {
    background: rgba(167,218,245, 0.3);
    outline: 0;
    color: #161616
}

QListView::item:selected:hover, QTreeView::item:selected:hover  {
    background: #3daee9;
    color: #161616;
}

QSlider::groove:horizontal {
    border: 1px solid #565a5e;
    height: 4px;
    background: #565a5e;
    margin: 0px;
    border-radius: 2px;
}

QSlider::handle:horizontal {
    background: #cccccc;
    border: 1px solid #565a5e;
    width: 16px;
    height: 16px;
    margin: -8px 0;
    border-radius: 9px;
}

QSlider::groove:vertical {
    border: 1px solid #565a5e;
    width: 4px;
    background: #565a5e;
    margin: 0px;
    border-radius: 3px;
}

QSlider::handle:vertical {
    background: #cccccc;
    border: 1px solid #565a5e;
    width: 16px;
    height: 16px;
    margin: 0 -8px;
    border-radius: 9px;
}

QToolButton {
    background-color: transparent;
    border: 1px transparent #76797C;
    border-radius: 2px;
    margin: 3px;
    padding: 5px;
}

QToolButton[popupMode="1"] { /* only for MenuButtonPopup */
 padding-right: 20px; /* make way for the popup button */
 border: 1px #76797C;
 border-radius: 5px;
}

QToolButton[popupMode="2"] { /* only for InstantPopup */
 padding-right: 10px; /* make way for the popup button */
 border: 1px #76797C;
}


QToolButton:hover, QToolButton::menu-button:hover {
    background-color: transparent;
    border: 1px solid #3daee9;
    padding: 5px;
}

QToolButton:checked, QToolButton:pressed,
        QToolButton::menu-button:pressed {
    background-color: #3daee9;
    border: 1px solid #3daee9;
    padding: 5px;
}

/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */
QToolButton::menu-indicator {
    image: url(icons/down_arrow.png);
    top: -7px; left: -2px; /* shift it a bit */
}

/* the subcontrols below are used only in the MenuButtonPopup mode */
QToolButton::menu-button {
    border: 1px transparent #76797C;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    /* 16px width + 4px for border = 20px allocated above */
    width: 16px;
    outline: none;
}

QToolButton::menu-arrow {
    image: url(icons/down_arrow.png);
}

QToolButton::menu-arrow:open {
    border: 1px solid #76797C;
}

QPushButton::menu-indicator  {
    subcontrol-origin: padding;
    subcontrol-position: bottom right;
    left: 8px;
}

QTableView
{
    background:none;
    border: 1px solid #76797C;
    gridline-color: #ededed;
    background-color: #cccccc;
}


QTableView, QHeaderView
{
    border-radius: 0px;
}

QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {
    background: #3daee9;
    color: #161616;
}

QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {
    background: #3daee9;
    color: #161616;
}


QHeaderView
{
    background:none;
    background-color: #ededed;
    border: 1px transparent;
    border-radius: 0px;
    margin: 0px;
    padding: 0px;

}

QHeaderView::section  {
    background-color: #ededed;
    color: #161616;
    padding: 5px;
    border: 1px solid #76797C;
    border-radius: 0px;
    text-align: center;
}

QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one
{
    border-top: 1px solid #76797C;
}

QHeaderView::section::vertical
{
    border-top: transparent;
}

QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one
{
    border-left: 1px solid #76797C;
}

QHeaderView::section::horizontal
{
    border-left: transparent;
}


QHeaderView::section:checked
 {
    color: white;
    background-color: #334e5e;
 }

 /* style the sort indicator */
QHeaderView::down-arrow {
    image: url(icons/down_arrow.png);
}

QHeaderView::up-arrow {
    image: url(icons/up_arrow.png);
}


QTableCornerButton::section {
    background-color: #ededed;
    border: 1px transparent #76797C;
    border-radius: 0px;
}

QToolBox  {
    padding: 5px;
    border: 1px transparent black;
}

QToolBox::tab {
    color: #161616;
    background-color: #ededed;
    border: 1px solid #76797C;
    border-bottom: 1px transparent #ededed;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QToolBox::tab:selected { /* italicize selected tabs */
    font: italic;
    background-color: #ededed;
    border-color: #3daee9;
 }

QStatusBar::item {
    border: 0px transparent dark;
 }


QFrame[height="3"], QFrame[width="3"] {
    background-color: #76797C;
}


QSplitter::handle {
    border: 1px dashed #76797C;
}

QSplitter::handle:hover {
    background-color: #787876;
    border: 1px solid #76797C;
}

QSplitter::handle:horizontal {
    width: 1px;
}

QSplitter::handle:vertical {
    height: 1px;
}

QProgressBar {
    border: 1px solid #76797C;
    border-radius: 5px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #05B8CC;
}

QDateEdit
{
    selection-background-color: #3daee9;
    border-style: solid;
    border: 1px solid #3375A3;
    border-radius: 2px;
    padding: 1px;
    min-width: 75px;
}

QDateEdit:on
{
    padding-top: 3px;
    padding-left: 4px;
    selection-background-color: #4a4a4a;
}

QDateEdit QAbstractItemView
{
    background-color: #cccccc;
    border-radius: 2px;
    border: 1px solid #3375A3;
    selection-background-color: #3daee9;
}

QDateEdit::drop-down
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    border-left-width: 0px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QDateEdit::down-arrow
{
    image: url(icons/down_arrow_disabled.png);
}

QDateEdit::down-arrow:on, QDateEdit::down-arrow:hover,
QDateEdit::down-arrow:focus
{
    image: url(icons/down_arrow.png);
}

QSpinBox{
    background:rgba(255,255,255,0.35);
}

QListWidget{
    background:rgba(255,255,255,0.5)
}

QTableWidget{
    background:rgba(255,255,255,0.75)
}

QComboBox:disabled, QLineEdit:disabled, QCheckBox:disabled, QSpinBox:disabled{
    background: transparent;
    color: transparent;
    border: none;
}

QLabel:disabled{
    background: transparent;
    color: transparent;
}

QComboBox::down-arrow:disabled, 
QSpinBox::up-arrow:disabled, 
QSpinBox::down-arrow:disabled, 
QCheckBox::indicator:checked:disabled, 
QCheckBox::indicator:unchecked:disabled{
    image: none;
}

QMenuBar{
    background:none;
}

#line:disabled, #line_2:disabled{
    background: transparent;
    border: none;
}



'''