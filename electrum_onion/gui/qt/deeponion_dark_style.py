"""onion look and feel."""

import os
from electrum_onion.util import pkg_dir


deeponion_stylesheet = """

/**********************/
/* onion Evolution CSS */
/*
0. OSX Reset
1. Navigation Bar
2. Editable Fields, Labels
3. Containers
4. File Menu, Toolbar
5. Buttons, Spinners, Dropdown
6. Table Headers
7. Scroll Bar
8. Tree View
9. Dialog Boxes
*/
/**********************/


/**********************/
/* 0. OSX Reset */

QWidget { /* Set default style for QWidget, override in following statements */
    border: 0;
    selection-color: #fff;
    selection-background-color: #818181;
}

QGroupBox {
    margin-top: 1em;
    color:#ffffff;
}

QGroupBox::title {
    subcontrol-origin: margin;
}

/**********************/
/* 1. Navigation Bar */

#main_window_nav_bar {
    border:0;
}

#main_window_nav_bar > QStackedWidget {
    background:#222435;
}

#main_window_nav_bar > QTabBar{
    color: #fff;
    border:0;
}

#main_window_nav_bar > QTabBar {
    padding: 0px 0px 0px 17px; /* top - right - bottom - left */
    background: url({pkg_dir}/gui/icons/gold-logo.png) no-repeat center left;
    background-origin: content; /* the left margin of background image will 'obey' the padding-left defined up above (10px) */
}

QTabWidget#main_window_nav_bar::tab-bar {
    alignment: left;
}

QTabWidget#main_window_nav_bar::pane {
    position: absolute;
}

#main_window_nav_bar > QTabBar::tab {
    background-color:#222435;
    color:#fff;
    font-weight:bold;
    min-height: 44px;
    padding-left:1em;
    padding-right:1em;
}

#main_window_nav_bar > QTabBar::tab:first {
    border-left: 0 solid #fff;
    margin-left:180px;
}

#main_window_nav_bar > QTabBar::tab:last {
    border-right: 0 solid #fff;
}

#main_window_nav_bar > QTabBar::tab:selected, #main_window_nav_bar > QTabBar::tab:hover {
    background-color:#4D67BC;
    font-weight:bold;
    color:#fff;
}


/**********************/
/* 2. Editable Fields and Labels */

QCheckBox { /* Checkbox Labels */
    color:#fff;
    background-color:transparent;
}

QCheckBox:hover {
    background-color:transparent;
}

QCheckBox {
    spacing: 5px;
}

QCheckBox::indicator {
    width: 16px;
    height: 16px;
}

QCheckBox::indicator:unchecked {
    image:url({pkg_dir}/gui/icons/checkbox/unchecked-dark.png);
}

QCheckBox::indicator:unchecked:disabled {
    image:url({pkg_dir}/gui/icons/checkbox/unchecked_disabled-dark.png);
}

QCheckBox::indicator:unchecked:pressed {
    image:url({pkg_dir}/gui/icons/checkbox/checked.png);
}

QCheckBox::indicator:checked {
    image:url({pkg_dir}/gui/icons/checkbox/checked.png);
}

QCheckBox::indicator:checked:disabled {
    image:url({pkg_dir}/gui/icons/checkbox/checked_disabled.png);
}

QCheckBox::indicator:checked:pressed {
    image:url({pkg_dir}/gui/icons/checkbox/unchecked-dark.png);
}

QCheckBox::indicator:indeterminate {
    image:url({pkg_dir}/gui/icons/checkbox/indeterminate.png);
}

QCheckBox::indicator:indeterminate:disabled {
    image:url({pkg_dir}/gui/icons/checkbox/indeterminate_disabled.png);
}

QCheckBox::indicator:indeterminate:pressed {
    image:url({pkg_dir}/gui/icons/checkbox/checked.png);
}

QRadioButton {
    padding: 2px;
    spacing: 5px;
    color: #fff;
}

QRadioButton::indicator {
    width: 16px;
    height: 16px;
}

QRadioButton::indicator::unchecked {
    image:url({pkg_dir}/gui/icons/radio/unchecked.png);
}

QRadioButton::indicator:unchecked:disabled {
    image:url({pkg_dir}/gui/icons/radio/unchecked_disabled-dark.png);
}

QRadioButton::indicator:unchecked:pressed {
    image:url({pkg_dir}/gui/icons/radio/checked.png);
}

QRadioButton::indicator::checked {
    image:url({pkg_dir}/gui/icons/radio/checked.png);
}

QRadioButton::indicator:checked:disabled {
    image:url({pkg_dir}/gui/icons/radio/checked_disabled.png);
}

QRadioButton::indicator:checked:pressed {
    image:url({pkg_dir}/gui/icons/radio/checked.png);
}

ScanQRTextEdit, ShowQRTextEdit, ButtonsTextEdit {
    color:#ffffff;
    background-color:#222435;
    border: 1px solid #4D67BC;
}

QValidatedLineEdit, QLineEdit, PayToEdit { /* Text Entry Fields */
    border: 1px solid #4D67BC;
    outline:0;
    padding: 5px 3px;
    background-color:#222435;
    color:#e5e5e5;
}

QValidatedLineEdit:disabled, QLineEdit:disabled, PayToEdit:disabled {
    border: 1px solid #4D67BC;
    background-color: #eeeeee;
}

QValidatedLineEdit:read-only, QLineEdit:read-only, PayToEdit:read-only {
    border: 1px solid #4D67BC;
}

PayToEdit {
    padding: 6px;
}

ButtonsLineEdit {
    color:#e5e5e5;
    background: #222435;
}

QLabel {
    color: #ffffff;
}


/**********************/
/* 3. Containers */


/* Wallet Container */
#main_window_container {
    background: #222435;
    color: #fff;
}


/* History Container */
#history_container {
    margin-top: 0;
}


/* Send Container */
#send_container {
    margin-top: 0;
}

#send_container > QLabel {
    margin-left:10px;
    min-width:150px;
}


/* Receive Container */
#receive_container {
    margin-top: 0;
}

#receive_container > QLabel {
    margin-left:10px;
    min-width:150px;
}


/* Addressses Container */
#addresses_container {
    margin-top: 0;
    background:#222435;
}


/* Contacts Container */
#contacts_container, #utxo_container {
    margin-top: 0;
}


/* Console Container */
#console_container {
    margin-top: 0;
    color:#e5e5e5;
    background:#222435;
}

#console_container > QWidget {
    background:#222435;
}


/* Balance Label */
#main_window_balance {
    color:#ffffff;
    font-weight:bold;
    margin-left:10px;
}


/**********************/
/* 4. File Menu, Toolbar */

#main_window_container QMenuBar {
    color: #fff;
}

QMenuBar {
    background-color:#222435;
    color: #fff;
}

QMenuBar::item {
    background-color:#222435;
    color:#ffffff;
}

QMenuBar::item:selected {
    background-color:#4D67BC;
}

QMenu {
    background-color:#222435;
    border:1px solid #2B2727;
}

QMenu::item {
    color:#ffffff;
}

QMenu::item:selected {
    background-color:#4D67BC;
    color:#ffffff;
}

QToolBar {
    background-color:#3398CC;
    border:0px solid #000;
    padding:0;
    margin:0;
}

QToolBar > QToolButton {
    background-color:#3398CC;
    border:0px solid #ffffff;
    min-height:2.5em;
    padding: 0em 1em;
    font-weight:bold;
    color:#fff;
}

QToolBar > QToolButton:checked {
    background-color:#4D67BC;
    color:#ffffff;
    font-weight:bold;
}

QMessageBox {
    background-color:#222435;
}


QLabel { /* Base Text Size & Color */
    color:#fff;
}


/**********************/
/* 5. Buttons, Spinners, Dropdown */

QPushButton, #blue_toolbutton { /* Global Button Style */
    background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: .01 #4D67BC, stop: .1 #4D67BC, stop: .95 #4D67BC, stop: 1 #4D67BC);
    border:0;
    border-radius:3px;
    color:#ffffff;
    /* font-size:12px; */
    font-weight:bold;
    padding: 7px 25px;
}

#blue_toolbutton {
    padding: 5px 23px;
}

QPushButton:hover, #blue_toolbutton:hover, StatusBarButton:hover {
    background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: .01 #4D67BC, stop: .1 #4D67BC, stop: .95 #4D67BC, stop: 1 #4D67BC);
    color:#fff;
}

StatusBarButton:hover {
    border: 0;
    border-radius:3px;
}

QPushButton:focus, #blue_toolbutton:focus {
    border:none;
    outline:none;
}

QPushButton:pressed, #blue_toolbutton:pressed {
    border:1px solid #4D67BC;
}

QPushButton:disabled, #blue_toolbutton:disabled
{
    color: #D3E8FE;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4D67BC, stop: 1 #4D67BC);
}

QStatusBar {
    color: #fff;
}

QStatusBar QPushButton:pressed {
    border:1px solid #1c75bc;
}

QStatusBar::item {
    border: none;
}

QComboBox { /* Dropdown Menus */
    border:1px solid #1c75bc;
    padding: 5px;
    background:#222435;
    color:#e5e5e5;
    combobox-popup: 0;
}

QComboBox::disabled {
    border: 1px solid #676767;
    background-color: #eeeeee;
}

QComboBox::drop-down {
    width:25px;
    border:0px;
}

QComboBox::down-arrow {
    border-image: url({pkg_dir}/gui/icons/onion_downArrow.png) 0 0 0 0 stretch stretch;
}

QComboBox QListView {
    border: 1px solid #1c75bc;
    color: #e5e5e5;
    padding: 3px;
    background-color: #222435;
    selection-color: #fff;
    selection-background-color: #818181;
}

QAbstractSpinBox {
    border:1px solid #1c75bc;
    padding: 5px 3px;
    background:#222435;
    color:#e5e5e5;
}

QAbstractSpinBox:disabled {
    border: 1px solid #676767;
}

QAbstractSpinBox::up-button {
    subcontrol-origin: border;
    subcontrol-position: top right;
    width:21px;
    background: #222435;
    border-left:0px;
    border-right:1px solid #1c75bc;
    border-top:1px solid #1c75bc;
    border-bottom:0px;
    padding-right:1px;
    padding-left:5px;
    padding-top:2px;
}

QAbstractSpinBox::up-button:disabled {
    border-right: 1px solid #676767;
    border-top: 1px solid #676767;
}

QAbstractSpinBox::down-button {
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width:21px;
    background: #222435;
    border-top:0px;
    border-left:0px;
    border-right:1px solid #1c75bc;
    border-bottom:1px solid #1c75bc;
    padding-right:1px;
    padding-left:5px;
    padding-bottom:2px;
}

QAbstractSpinBox::down-button:disabled {
    border-right: 1px solid #676767;
    border-bottom: 1px solid #676767;
}

QAbstractSpinBox::up-arrow {
    image: url({pkg_dir}/gui/icons/onion_upArrow_small.png);
    width: 10px;
    height: 10px;
}

QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {
    image: url({pkg_dir}/gui/icons/onion_upArrow_small_disabled.png);
}

QAbstractSpinBox::down-arrow {
    image: url({pkg_dir}/gui/icons/onion_downArrow_small.png);
    width: 10px;
    height: 10px;
}

QAbstractSpinBox::down-arrow:disabled, QAbstractSpinBox::down-arrow:off {
    image: url({pkg_dir}/gui/icons/onion_downArrow_small_disabled.png);
}

QSlider::groove:horizontal {
    border: 1px solid #1c75bc;
    background: white;
    height: 10px;
}

QSlider::sub-page:horizontal {
    background-color: #818181;
    border: 1px solid #1c75bc;
    height: 10px;
}

QSlider::add-page:horizontal {
    background: #222435;
    border: 1px solid #1c75bc;
    height: 10px;
}

QSlider::handle:horizontal {
    background-color: #1c75bc;
    border: 1px solid #1c75bc;
    width: 13px;
    margin-top: -2px;
    margin-bottom: -2px;
    border-radius: 2px;
}


QProgressBar {
    color: #ffffff;
}

QProgressBar:horizontal {
    border: 1px solid #1c75bc;
    background-color: #222435;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #ccc;
}


/**********************/
/* 6. Table Headers */

QHeaderView { /* Table Header */
    background-color:transparent;
    border:0px;

}

QHeaderView::section { /* Table Header Sections */
    qproperty-alignment:center;
    background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0.25, stop: 0 #64A3D0, stop: 1 #4D67BC);
    color:#fff;
    font-weight:bold;
    font-size:11px;
    outline:0;
    border:0;
    border-right:1px solid #56ABD8;
    padding-left:2px;
    padding-right:10px;
    padding-top:1px;
    padding-bottom:1px;
}

#contacts_container QHeaderView::section {
}

#contacts_container QHeaderView::section:first {
    padding-left:50px;
    padding-right:40px;
}

QHeaderView::section:last {
    border-right: 0px solid #d7d7d7;
}


/**********************/
/* 7. Scroll Bar */

QAbstractScrollArea::corner {
    background: none;
    border: none;
}

QScrollBar { /* Scroll Bar */
}

QScrollBar:vertical { /* Vertical Scroll Bar Attributes */
    border:0;
    background:#ffffff;
    width:18px;
    margin: 18px 0px 18px 0px;
}

QScrollBar:horizontal { /* Horizontal Scroll Bar Attributes */
    border:0;
    background:#ffffff;
    height:18px;
    margin: 0px 18px 0px 18px;
}


QScrollBar::handle:vertical { /* Scroll Bar Slider - vertical */
    background:#e0e0e0;
    min-height:10px;
}

QScrollBar::handle:horizontal { /* Scroll Bar Slider - horizontal */
    background:#e0e0e0;
    min-width:10px;
}

QScrollBar::add-page, QScrollBar::sub-page { /* Scroll Bar Background */
    background:#F8F6F6;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical, QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { /* Define Arrow Button Dimensions */
    background-color: #222435;
    border: 1px solid #ffffff;
    width:16px;
    height:16px;
}

QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed, QScrollBar::add-line:horizontal:pressed, QScrollBar::sub-line:horizontal:pressed {
    background-color:#e0e0e0;
}

QScrollBar::sub-line:vertical { /* Vertical - top button position */
    subcontrol-position:top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical { /* Vertical - bottom button position */
    subcontrol-position:bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal { /* Vertical - left button position */
    subcontrol-position:left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal { /* Vertical - right button position */
    subcontrol-position:right;
    subcontrol-origin: margin;
}

QScrollBar:up-arrow, QScrollBar:down-arrow, QScrollBar:left-arrow, QScrollBar:right-arrow { /* Arrows Icon */
    width:10px;
    height:10px;
}

QScrollBar:up-arrow {
    background-image: url({pkg_dir}/gui/icons/onion_upArrow_small.png);
}

QScrollBar:down-arrow {
    background-image: url({pkg_dir}/gui/icons/onion_downArrow_small.png);
}

QScrollBar:left-arrow {
    background-image: url({pkg_dir}/gui/icons/onion_leftArrow_small.png);
}

QScrollBar:right-arrow {
    background-image: url({pkg_dir}/gui/icons/onion_rightArrow_small.png);
}


/**********************/
/* 8. Tree Widget */

QTreeView, QTreeWidget, QListWidget, QTableView, QTextEdit, QPlainTextEdit  {
    border: 0px;
    color:#e5e5e5;
    background: #222435;
}

QTreeView:disabled, QTreeWidget:disabled, QListWidget:disabled,
QTableView:disabled, QTextEdit:disabled, QPlainTextEdit:disabled  {
    border: 1px solid #676767;
    background-color: #eeeeee;
}

QTreeView QLineEdit, QTreeWidget QLineEdit {
    min-height: 0;
    padding: 0;
}

QListWidget, QTableView, QTextEdit, QPlainTextEdit,
QDialog QTreeWidget, QDialog QTreeView {
    border: 1px solid #1c75bc;
}

#send_container QTreeWidget, #receive_container QTreeWidget,
#send_container QTreeView, #receive_container QTreeView {
    border: 1px solid #1c75bc;
    background-color: #222435;
}

QTableView {
    background-color: #222435;
}

QTreeView::branch {
    color: #e5e5e5;
    background-color: transparent;
}

QTreeView::branch:selected {
    background-color:#808080;
}

QTreeView::item:selected, QTreeView::item:selected:active {
    color: #fff;
    background-color:#808080;
}

MyTreeView::branch:has-siblings:adjoins-item {
    border-image: url({pkg_dir}/gui/icons/tx_group_mid.png) 0;
}

MyTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: url({pkg_dir}/gui/icons/tx_group_tail.png) 0;
}

/**********************/
/* 9. Dialog Boxes */

QDialog {
    background: #222435;
}

QDialog QScrollArea {
    background: transparent;
}

QDialog QTabWidget {
    border-bottom:1px solid #ffffff;
}

QDialog QTabWidget::pane {
    border: 1px solid #d7d7d7;
    color:#e5e5e5;
    background: #222435;
}

QDialog QTabWidget QTabBar::tab {
    background-color: #222435;
    color:#ffffff;
    padding-left:10px;
    padding-right:10px;
    padding-top:5px;
    padding-bottom:5px;
    border-top: 1px solid #d7d7d7;
}

QDialog QTabWidget QTabBar::tab:first {
    border-left: 1px solid #d7d7d7;
}

QDialog QTabWidget QTabBar::tab:last {
    border-right: 1px solid #d7d7d7;
}

QDialog QTabWidget QTabBar::tab:selected, QDialog QTabWidget QTabBar::tab:hover {
    background-color:#4D67BC;
    color:#ffffff;
}

QDialog HelpButton {
    background-color: transparent;
    color:#ffffff;
}

QDialog QWidget { /* Remove Annoying Focus Rectangle */
    outline: 0;
}

QDialog #settings_tab {
    min-width: 600px;
}

Dip3TabWidget {
    border-bottom:1px solid #ffffff;
}

Dip3TabWidget::pane {
    border: 1px solid #d7d7d7;
    color: #e5e5e5;
    background: #222435;
}

QTabWidget VTabBar::tab {
    background-color: #222435;
    color:#ffffff;
    padding-left:10px;
    padding-right:10px;
    padding-top:5px;
    padding-bottom:5px;
    border-top: 1px solid #d7d7d7;
}

QTabWidget VTabBar::tab:first {
    border-left: 1px solid #d7d7d7;
}

QTabWidget VTabBar::tab:last {
    border-right: 1px solid #d7d7d7;
}

QTabWidget VTabBar::tab:selected, QTabWidget VTabBar::tab:hover {
    background-color: #4D67BC;
    color:#ffffff;
}

QWizard {
    background-color:#222435;
    color: #fff
}

#err-label {
    color: #800000;
}
#info-label {
    color: #008000;
}
"""

pkg_dir_for_css = pkg_dir.replace(os.sep, '/')
deeponion_stylesheet = deeponion_stylesheet.replace('{pkg_dir}', '%s' % pkg_dir_for_css)
