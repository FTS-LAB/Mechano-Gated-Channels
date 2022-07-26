import pyqtgraph as pg
import numpy as np
import os, sys, csv
import pandas as pd
import PyQt5 as pq5
from PyQt5 import QtWidgets, QtGui, QtCore
import PyQt5.QtGui
import PyQt5.QtCore
import statistics as st
from scipy.signal import  find_peaks
from scipy.optimize import curve_fit
from PyQt5.QtWidgets import QWidget, QGridLayout, QSplitter, QFormLayout, QLabel,QLineEdit, QPushButton, QTreeWidget, QFileDialog, QMessageBox, QTabWidget, QSpinBox ,QComboBox
from PyQt5.QtGui import QPixmap


stim_dictionary={1:0.48,
                2:0.96,
                3:1.44,
                4:1.92,
                5:2.4,
                6:2.88,
                7:3.36 ,
                8:3.84,
                9:4.32 ,
                10:4.8 ,
                11:5.28 ,
                12:5.76 ,
                13:6.24 ,
                14:6.72 ,
                15:7.2 ,
                16:7.68 ,
                17:8.16 ,
                18:8.64,
                19:9.12,
                20:9.6,
                21:10.08,
                22:10.56,
                23:11.04,
                24:11.52}




app=pg.mkQApp('Poking Analysis V4')

def divider():
    div = QLabel ('')
    div.setStyleSheet ("QLabel {background-color: #F56D91; padding: 0; margin: 0; border-bottom: 2 solid #DAEAF1; border-top: 1 solid #7F8487;}")
    div.setMaximumHeight (2)
    return div
def spacer():
    div = QLabel ('')
    return div

######TAB ORGANIZATION#############################################################
###################################################################################
tabs = QTabWidget()
tabs.resize(1500,1000)
#global_layout=QGridLayout()

#global_layout.addWidget(tabs)
tab1=QWidget()
tab2=QWidget()
tab3=QWidget()
tabs.addTab(tab1, "General")
tabs.addTab(tab2, "Settings")
tabs.addTab(tab3, "Info")



################# SETTINGS TAB2 #########################################################

### TAB2 COLUMN DISTRIBUTION


tab2_layout=QGridLayout()
tab2.setLayout(tab2_layout)
tab2_hsplit=QSplitter(pg.QtCore.Qt.Horizontal)
tab2_layout.addWidget(tab2_hsplit)
tab2_hsplit_2=QSplitter(pg.QtCore.Qt.Horizontal)



tab2_left=QWidget()
tab2_center=QWidget()
tab2_right=QWidget()
#QFormLayout el correcto para texto
tab2_left_l=QFormLayout()
tab2_left.setLayout(tab2_left_l)
tab2_center_l=QFormLayout()
tab2_center.setLayout(tab2_center_l)
tab2_right_l=QFormLayout()
tab2_right.setLayout(tab2_right_l)


tab2_hsplit.addWidget(tab2_left)
tab2_hsplit.addWidget(tab2_hsplit_2)
tab2_hsplit_2.addWidget(tab2_center)
tab2_hsplit_2.addWidget(tab2_right)



###################
#### DRAWING SETTINGS WINDOW ####################################

###FULL SWEEP###
FS_settings_window=QWidget()
FS_sw=FS_settings_window
FS_sw.setGeometry(30,800,350,200)
FS_sw.setWindowTitle('Full Sweep Plotting settings')
FS_sw_layout=QFormLayout()
FS_sw.setLayout(FS_sw_layout)

####Buttons and Line Edits######
#FS_color_but=QPushButton('Custom Color')
FS_line_color_lab=QLabel('Trace Color')
FS_line_color_le=QLineEdit('#9D9D9D')
FS_line_thickness_lab=QLabel('Trace Thickness')
FS_line_thickness_sb=QSpinBox()
FS_line_thickness_sb.setValue(2)
FS_last_line_color_lab=QLabel('Last Trace Color')
FS_last_line_color_le=QLineEdit('#0F52BA')
FS_last_line_thickness_lab=QLabel('Last Trace Thickness')
FS_last_line_thickness_sb=QSpinBox()
FS_last_line_thickness_sb.setValue(4)
FS_apply_but=QPushButton('Apply Changes')


#############

####Rows####
#FS_sw_layout.addRow(FS_color_but)
FS_sw_layout.addRow(FS_line_color_lab,FS_line_color_le)
FS_sw_layout.addRow(FS_line_thickness_lab,FS_line_thickness_sb)
FS_sw_layout.addRow(FS_last_line_color_lab,FS_last_line_color_le)
FS_sw_layout.addRow(FS_last_line_thickness_lab,FS_last_line_thickness_sb)
FS_sw_layout.addRow(FS_apply_but)

###ZOOMED SWEEP###
ZS_settings_window=QWidget()
ZS_sw=ZS_settings_window
ZS_sw.setGeometry(30,800,350,200)
ZS_sw.setWindowTitle('Zoomed Sweep Plotting settings')
ZS_sw_layout=QFormLayout()
ZS_sw.setLayout(ZS_sw_layout)

####Labels, line Edits and buttons######
ZS_line_color_lab=QLabel('Trace Color')
ZS_line_color_le=QLineEdit('#9D9D9D')
ZS_line_thickness_lab=QLabel('Trace Thickness')
ZS_line_thickness_sb=QSpinBox()
ZS_line_thickness_sb.setValue(2)
ZS_last_line_color_lab=QLabel('Last Trace Color')
ZS_last_line_color_le=QLineEdit('#0F52BA')
ZS_last_line_thickness_lab=QLabel('Last Trace Thickness')
ZS_last_line_thickness_sb=QSpinBox()
ZS_last_line_thickness_sb.setValue(4)
ZS_fit_line_color_lab=QLabel('Fit Line Color')
ZS_fit_line_color_le=QLineEdit('#DFBB9D')
ZS_fit_line_thickness_lab=QLabel('Fit Line Thickness')
ZS_fit_line_thickness_sb=QSpinBox()
ZS_fit_line_thickness_sb.setValue(2)
ZS_apply_but=QPushButton('Apply Changes')

####Rows####
ZS_sw_layout.addRow(ZS_line_color_lab,ZS_line_color_le)
ZS_sw_layout.addRow(ZS_line_thickness_lab,ZS_line_thickness_sb)
ZS_sw_layout.addRow(ZS_last_line_color_lab,ZS_last_line_color_le)
ZS_sw_layout.addRow(ZS_last_line_thickness_lab,ZS_last_line_thickness_sb)
ZS_sw_layout.addRow(ZS_fit_line_color_lab, ZS_fit_line_color_le)
ZS_sw_layout.addRow(ZS_fit_line_thickness_lab,ZS_fit_line_thickness_sb)
ZS_sw_layout.addRow(ZS_apply_but)


###STIM-RESPONSE###
SR_settings_window=QWidget()
SR_sw=SR_settings_window
SR_sw.setGeometry(30,800,350,200)
SR_sw.setWindowTitle('Stim-Response Plotting settings')
SR_sw_layout=QFormLayout()
SR_sw.setLayout(SR_sw_layout)

####Labels, line Edits and buttons######
SR_symbol_type_lab=QLabel('Symbol Type')
SR_symbol_type_cb=QComboBox()
#sybols#
SR_symbol_type_cb.addItem('o')
SR_symbol_type_cb.addItem('t')
SR_symbol_type_cb.addItem('s')
SR_symbol_type_cb.addItem('x')
SR_symbol_type_cb.addItem('+')
SR_symbol_type_cb.addItem('p')
#
SR_symbol_color_lab=QLabel('Symbol Color')
SR_symbol_color_le=QLineEdit('#ff0000')
SR_symbol_size_lab=QLabel('Symbol Size')
SR_symbol_size_sb=QSpinBox()
SR_symbol_size_sb.setValue(8)
SR_line_color_lab=QLabel('Line Color')
SR_line_color_le=QLineEdit('#000000')
SR_line_size_lab=QLabel('Line Size')
SR_line_size_sb=QSpinBox()
SR_line_size_sb.setValue(2)
SR_apply_but=QPushButton('Apply Changes')

####Rows####
SR_sw_layout.addRow(SR_symbol_type_lab, SR_symbol_type_cb)
SR_sw_layout.addRow(SR_symbol_color_lab,SR_symbol_color_le)
SR_sw_layout.addRow(SR_symbol_size_lab,SR_symbol_size_sb)
SR_sw_layout.addRow(SR_line_color_lab,SR_line_color_le)
SR_sw_layout.addRow(SR_line_size_lab,SR_line_size_sb)
SR_sw_layout.addRow(SR_apply_but)




###STIM-THRESHOLD###
TH_settings_window=QWidget()
TH_sw=TH_settings_window
TH_sw.setGeometry(30,800,350,200)
TH_sw.setWindowTitle('Stim-Response Plotting settings')
TH_sw_layout=QFormLayout()
TH_sw.setLayout(TH_sw_layout)

####Labels, line Edits and buttons######
TH_symbol_type_lab=QLabel('Symbol Type')
TH_symbol_type_cb=QComboBox()
#sybols#
TH_symbol_type_cb.addItem('o')
TH_symbol_type_cb.addItem('t')
TH_symbol_type_cb.addItem('s')
TH_symbol_type_cb.addItem('x')
TH_symbol_type_cb.addItem('+')
TH_symbol_type_cb.addItem('p')
#
TH_symbol_color_lab=QLabel('Symbol Color')
TH_symbol_color_le=QLineEdit('#FFB562')
TH_symbol_size_lab=QLabel('Symbol Size')
TH_symbol_size_sb=QSpinBox()
TH_symbol_size_sb.setValue(8)
TH_line_color_lab=QLabel('Line Color')
TH_line_color_le=QLineEdit('#3AB0FF')
TH_line_size_lab=QLabel('Line Size')
TH_line_size_sb=QSpinBox()
TH_line_size_sb.setValue(2)
TH_apply_but=QPushButton('Apply Changes')

####Rows####
TH_sw_layout.addRow(TH_symbol_type_lab, TH_symbol_type_cb)
TH_sw_layout.addRow(TH_symbol_color_lab,TH_symbol_color_le)
TH_sw_layout.addRow(TH_symbol_size_lab,TH_symbol_size_sb)
TH_sw_layout.addRow(TH_line_color_lab,TH_line_color_le)
TH_sw_layout.addRow(TH_line_size_lab,TH_line_size_sb)
TH_sw_layout.addRow(TH_apply_but)


###TAU STIMATION###
TAV_settings_window=QWidget()
TAV_sw=TAV_settings_window
TAV_sw.setGeometry(30,800,350,200)
TAV_sw.setWindowTitle('Stim-Response Plotting settings')
TAV_sw_layout=QFormLayout()
TAV_sw.setLayout(TAV_sw_layout)

####Labels, line Edits and buttons######
TAV_bar_color_lab=QLabel('Bar Color')
TAV_bar_color_le=QLineEdit('#ff0000')
TAV_border_color_lab=QLabel('Border Color')
TAV_border_color_le=QLineEdit('#000000')
TAV_border_thickness_lab=QLabel('Border Thickness')
TAV_border_thickness_sb=QSpinBox()
TAV_border_thickness_sb.setValue(1)
TAV_apply_but=QPushButton('Apply Changes')

####Rows#####
TAV_sw_layout.addRow(TAV_bar_color_lab, TAV_bar_color_le)
TAV_sw_layout.addRow(TAV_border_color_lab,TAV_border_color_le)
TAV_sw_layout.addRow(TAV_border_thickness_lab,TAV_border_thickness_sb)
TAV_sw_layout.addRow(TAV_apply_but)


#Fild for entering the fibre identifier
#Create labels and line edit for inputs


divisor=divider()



#LEFT COLUMN
#Create labels and line edit for inputs
tab2_left_title=QLabel("PLOT SETTINGS")
tab2_left_title.setFont(QtGui.QFont('Arial', 18, weight=3))

#CURRENT OVERVIEW PLOT SETTINGS
tab2_left_subtitle1=QLabel("CURRENT OVERVIEW AND ZOOMED ZONE PLOT") #CPO
tab2_left_subtitle1.setFont(QtGui.QFont('Arial', 14, weight=3))

tab2_left_CPO_line_c_label=QLabel("Line color:")
tab2_left_CPO_line_c=QLineEdit('#9D9D9D')
tab2_left_CPO_line2_c_label=QLabel("Last line color:")
tab2_left_CPO_line2_c=QLineEdit('#0F52BA')
tab2_left_CPO_fitline_c_label=QLabel("Fit color:")
tab2_left_CPO_fitline_c=QLineEdit('#DFBB9D')

tab2_left_CPO_line_t1_label=QLabel("Current Overview Line Thickness:")
tab2_left_CPO_line_t1=QLineEdit('2')
tab2_left_CPO_line2_t2_label=QLabel("Current Overview Last Line Thickness:")
tab2_left_CPO_line2_t2=QLineEdit('4')
tab2_left_CPO_line_t3_label=QLabel("Zoomed Zone Line Thickness:")
tab2_left_CPO_line_t3=QLineEdit('4')
tab2_left_CPO_line2_t4_label=QLabel("Zoomed Zone Last Line Thickness:")
tab2_left_CPO_line2_t4=QLineEdit('6')
tab2_left_CPO_fitline_t_label=QLabel("Fit Line Thickness:")
tab2_left_CPO_fitline_t=QLineEdit('2')


tab2_left_l.addRow(tab2_left_title)
tab2_left_l.addRow(spacer())
tab2_left_l.addRow(tab2_left_subtitle1)
tab2_left_l.addRow(divider())
tab2_left_l.addRow(tab2_left_CPO_line_c_label, tab2_left_CPO_line_c)
tab2_left_l.addRow(tab2_left_CPO_line2_c_label,tab2_left_CPO_line2_c)
tab2_left_l.addRow(tab2_left_CPO_fitline_c_label,tab2_left_CPO_fitline_c)

tab2_left_l.addRow(tab2_left_CPO_line_t1_label, tab2_left_CPO_line_t1)
tab2_left_l.addRow(tab2_left_CPO_line2_t2_label, tab2_left_CPO_line2_t2)
tab2_left_l.addRow(tab2_left_CPO_line_t3_label, tab2_left_CPO_line_t3)
tab2_left_l.addRow(tab2_left_CPO_line2_t4_label, tab2_left_CPO_line2_t4)
tab2_left_l.addRow(tab2_left_CPO_fitline_t_label, tab2_left_CPO_fitline_t)




symbol_election_label=QLabel("SYMBOL PROPERTIES")
symbol_election_label.setFont(QtGui.QFont('Arial', 15, weight=3))

selected_symbol_label=QLabel("Select symbol")
selected_symbol=QLineEdit("o")

size_symbol_label=QLabel("Select size of the symbol")
size_symbol=QLineEdit("4")

symbol_fill_color_label=QLabel("Select symbol filling color")
symbol_fill_color=QLineEdit('#3AB0FF')

plot_line_color_label=QLabel("Select line color")
plot_line_color=QLineEdit('#3AB0FF')

#Arrange in Rows within the FormLayout

#Import Button
apply_but=QPushButton('Apply changes')
#Arrange buttons within the FormLayout
tab2_left_l.addRow(apply_but)


##CENTER COLUMN
#Create labels and line edit for inputs
import_panel_label2=QLabel("LOLOOLLOOLOOL")
import_panel_label2.setFont(QtGui.QFont('Arial', 15, weight=3))

#Arrange in Rows within the FormLayout
tab2_center_l.addRow(import_panel_label2)
tab2_center_l.addRow(divider())

#Import Button
import_but2=QPushButton('Import Sweeps')
tab2_center_l.addRow(spacer())
tab2_center_l.addRow(divider())
tab2_center_l.addRow(import_but2)

#RIGHT COLUMN
#Create labels and line edit for inputs
import_panel_label2=QLabel("IMPORT PANEL")
import_panel_label2.setFont(QtGui.QFont('Arial', 15, weight=3))

#Arrange in Rows within the FormLayout
tab2_right_l.addRow(import_panel_label2)
tab2_right_l.addRow(divider())

#Import Button
import_but2=QPushButton('Import Sweeps')
tab2_right_l.addRow(spacer())
tab2_right_l.addRow(divider())
tab2_right_l.addRow(import_but2)


############

################# INFO tab1 #########################################################
#Main tab layout
tab1_layout=QGridLayout()
tab1.setLayout(tab1_layout)

#####Plots######

#Full Sweeps
FS=pg.PlotWidget()
FS.setBackground((255,255,255))
FS.setTitle('Current Overview', size='15pt')
FS.setLabel('left',text='Current',units='A')
FS.setLabel('bottom',text='Time',units='mS')
FS.setYRange(-2E-9, 0)
#Zommed Sweeps
ZS=pg.PlotWidget()
ZS.setBackground((255,255,255))
ZS.setTitle('Zoomed Zone', size='15pt')
ZS.setLabel('left',text='Current',units='A')
ZS.setLabel('bottom',text='Time',units='mS')
ZS.setYRange(-2E-9, 0)
#Stim-Response Curve
SR=pg.PlotWidget()
SR.setTitle('Stim-Response Curve', size='15pt')
SR.setLabel('left',text='Current',units='A')
SR.setLabel('bottom',text='Indentation',units='µm')
SR.setBackground((255,255,255))
#Thershold plot
TH=pg.PlotWidget()
TH.setBackground((255,255,255))
TH.setTitle('Stim-Threshold Plot', size='15pt')
TH.setLabel('left',text='Threshold',units='µm')
TH.setLabel('bottom',text='Indentation',units='µm')
#Tau Value
TAV=pg.PlotWidget()
TAV.setBackground((255,255,255))
TAV.setTitle('Tau Stimation', size='15pt')
TAV.setLabel('left',text='T',units='ms')
TAV.setLabel('bottom',text='Indentation',units='µm')

### Plot arranging####
### Add each plot to the desired region of the GUI


'''Bloque A '''
tab1_vsplit1=QSplitter(pg.QtCore.Qt.Vertical)
tab1_a=QWidget()
tab1_a_l=QGridLayout()
tab1_a.setLayout(tab1_a_l)
##Stim-resmponse plot
tab1_a_l.addWidget(SR)

'''Bloque B '''
tab1_vsplit2=QSplitter(pg.QtCore.Qt.Vertical)
tab1_b=QWidget()
tab1_b_l=QFormLayout()
tab1_b.setLayout(tab1_b_l)
##Threshold plot
tab1_b_l.addWidget(TH)

'''Bloque C '''
tab1_c=QWidget()
tab1_c_l=QGridLayout()
tab1_c.setLayout(tab1_c_l)
####

tab1_layout.addWidget(tab1_vsplit2)
tab1_vsplit2.addWidget(tab1_vsplit1)
tab1_vsplit1.addWidget(tab1_a)
tab1_vsplit1.addWidget(tab1_b)
tab1_vsplit2.addWidget(tab1_c)

tab1_hsplit1=QSplitter(pg.QtCore.Qt.Horizontal)
tab1_layout.addWidget(tab1_hsplit1)
#Tau Stimation
tab1_c_l.addWidget(TAV)


'''Bloque D '''

tab1_d=QWidget()
tab1_d_l=QGridLayout()
tab1_d.setLayout(tab1_d_l)

tab1_hsplit1.addWidget(tab1_d)
tab1_hsplit1.addWidget(tab1_vsplit2)

tab1_d_l.addWidget(ZS)

####

tab1_vsplit3=QSplitter(pg.QtCore.Qt.Vertical)
tab1_layout.addWidget(tab1_vsplit3)
'''Bloque E '''
tab1_e=QWidget()
tab1_e_l=QGridLayout()
tab1_e.setLayout(tab1_e_l)
tab1_vsplit3.addWidget(tab1_e)
tab1_vsplit3.addWidget(tab1_hsplit1)

#Plot FULL SWEEP
tab1_e_l.addWidget(FS)

####
tab1_vsplit4=QSplitter(pg.QtCore.Qt.Vertical)
tab1_layout.addWidget(tab1_vsplit4)

'''Bloque F '''
tab1_f=QWidget()
tab1_f_l=QFormLayout()
tab1_f.setLayout(tab1_f_l)

######
'''importing panel (left top panel)'''
#Fill for entering the cell identifier
###Create labels, line edit for inputs and buttons###
tab1_import_panel_label=QLabel("IMPORT PANEL")
tab1_import_panel_label.setAlignment(QtCore.Qt.AlignCenter)
tab1_import_panel_label.setFont(QtGui.QFont('Arial', 15, weight=3))
tab1_experimenter_lab=QLabel("Researcher initials")
tab1_experimenter=QLineEdit("SSF")
tab1_cell_ID_lab=QLabel('Cell_ID')
tab1_cell_ID=QLineEdit('Cell_0')
tab1_record_data_lab=QLabel("Recording data")
tab1_record_data=QLineEdit("01_07_22")
tab1_label_MutantID=QLabel("Mutant")
tab1_Mutant_ID=QLineEdit("P2")
#tab1_color_input_lab=QLabel('Color Input: #HEX')
#tab1_color_input=QLineEdit('#004099')
tab1_adq_settings_lab=QLabel('ADQUISITION SETTINGS')
tab1_adq_settings_lab.setFont(QtGui.QFont('Arial', 15, weight=3))
tab1_adq_settings_lab.setAlignment(QtCore.Qt.AlignCenter)
tab1_th_lab=QLabel('Threshold Factor')
tab1_Samp_lab=QLabel('Sampling (KHz)')
tab1_Samp=QLineEdit('50')
tab1_Ind_V_lab=QLabel('Indentation Velocity (μm/ms)')
tab1_Ind_V=QLineEdit('1')
tab1_import_but=QPushButton('Import Sweeps')
tab1_replot_but=QPushButton('Replot Graph')
tab1_plot_min_but=QPushButton('Clear')
tab1_save_results_but=QPushButton('Save Results as CSV')
tab1_plot_settings_lab=QLabel('PLOT SETTINGS')
tab1_plot_settings_lab.setFont(QtGui.QFont('Arial', 15, weight=3))
tab1_plot_settings_lab.setAlignment(QtCore.Qt.AlignCenter)
tab1_FS_settings_but=QPushButton('Current Overview')
tab1_ZS_settings_but=QPushButton('Zoomed Zone')
tab1_SR_settings_but=QPushButton('Stim-Response Curve')
tab1_TH_settings_but=QPushButton('Stim-Threshold')
tab1_TAV_settings_but=QPushButton('Tau Stimation')


#Arrange in Rows within the FormLayout
tab1_f_l.addRow(tab1_import_panel_label)
tab1_f_l.addRow(divider())
tab1_f_l.addRow(tab1_experimenter_lab,tab1_experimenter)
tab1_f_l.addRow(tab1_record_data_lab,tab1_record_data)
tab1_f_l.addRow(tab1_cell_ID_lab,tab1_cell_ID)
tab1_f_l.addRow(tab1_label_MutantID,tab1_Mutant_ID)
#tab1_f_l.addRow(tab1_color_input_lab,tab1_color_input)
tab1_f_l.addRow(spacer())
tab1_f_l.addRow(tab1_adq_settings_lab)
tab1_f_l.addRow(divider())
tab1_f_l.addRow(tab1_Samp_lab,tab1_Samp)
tab1_f_l.addRow(tab1_Ind_V_lab,tab1_Ind_V)
tab1_f_l.addRow(spacer())
tab1_f_l.addRow(divider())
tab1_f_l.addRow(tab1_import_but)
tab1_f_l.addRow(tab1_replot_but)
tab1_f_l.addRow(tab1_plot_min_but)
tab1_f_l.addRow(tab1_save_results_but)
tab1_f_l.addRow(spacer())
tab1_f_l.addRow(tab1_plot_settings_lab)
tab1_f_l.addRow(divider())
tab1_f_l.addRow(tab1_FS_settings_but)
tab1_f_l.addRow(tab1_ZS_settings_but)
tab1_f_l.addRow(tab1_SR_settings_but)
tab1_f_l.addRow(tab1_TH_settings_but)
tab1_f_l.addRow(tab1_TAV_settings_but)
####

'''Bloque G '''
tab1_g=QWidget()
tab1_g_l=QGridLayout()
tab1_g.setLayout(tab1_g_l)
#tab1_etiqueta_g=QLabel('g')
#tab1_g_l.addWidget(tab1_etiqueta_g)

tab1_vsplit4.addWidget(tab1_f)
tab1_vsplit4.addWidget(tab1_g)

tab1_hsplit2=QSplitter(pg.QtCore.Qt.Horizontal)
tab1_hsplit2.addWidget(tab1_vsplit4)
tab1_hsplit2.addWidget(tab1_vsplit3)
tab1_layout.addWidget(tab1_hsplit2)

####Tree
tree =QTreeWidget()
#Seleccionas uno y arrastras para seleccionar el resto
tree.setSelectionMode(2)
tree.setHeaderLabels(['Cell', 'Stimulus'])
tree.setColumnWidth(0, 100)
tab1_g_l.addWidget(tree)

################# INFO TAB3 #########################################################
tab3_layout=QGridLayout()
tab3.setLayout(tab3_layout)

####Splitters
tab3_hsplit1=QSplitter(pg.QtCore.Qt.Horizontal)
tab3_vsplit1=QSplitter(pg.QtCore.Qt.Vertical)
tab3_vsplit2=QSplitter(pg.QtCore.Qt.Vertical)
tab3_hsplit2=QSplitter(pg.QtCore.Qt.Horizontal)
tab3_vsplit3=QSplitter(pg.QtCore.Qt.Vertical)


####Bloque A

tab3_a=QWidget()
tab3_a_l=QFormLayout()
tab3_a.setLayout(tab3_a_l)

###LABLES###
font_tab3_a=QtGui.QFont('Arial', 20, weight=3, italic=True)
font_tab3_a.setBold(True)

tab3_a_0=QLabel('Patch-Master Next Export Options')
tab3_a_0.setFont(font_tab3_a)
tab3_a_i=QLabel('Steps (1-7) need to be followed only once.')
tab3_a_i.setFont(QtGui.QFont('Arial', 10, weight=3))
tab3_a_i.setStyleSheet('color: red')
tab3_a_1=QLabel('1. Press Tweak Button')
tab3_a_1.setFont(QtGui.QFont('Arial', 14, weight=3))
tab3_a_2=QLabel('2. Select Export Tab.')
tab3_a_2.setFont(QtGui.QFont('Arial', 14, weight=3))
tab3_a_3=QLabel('3. On File Type Select: Text.')
tab3_a_3.setFont(QtGui.QFont('Arial', 14, weight=3))
tab3_a_4=QLabel('4. Export Choice Select: Traces Check-Box only and NO analysis.')
#tab3_a_4.setWordWrap(True)
tab3_a_4.setFont(QtGui.QFont('Arial', 14, weight=3))
tab3_a_5=QLabel('5. Export Choice Select: NO analysis.')
tab3_a_5.setFont(QtGui.QFont('Arial', 14, weight=3))
tab3_a_6=QLabel('6. Trace Time: Relative to Swepp.')
tab3_a_6.setFont(QtGui.QFont('Arial', 14, weight=3))
tab3_a_7=QLabel('7. Text Options: Separator (Comma)')
tab3_a_7.setFont(QtGui.QFont('Arial', 14, weight=3))
tab3_a_8=QLabel('8. Tree Widget:  Select the Sweep to export')
tab3_a_8.setFont(QtGui.QFont('Arial', 14, weight=3))
tab3_a_9=QLabel('9. Press Data Button')
tab3_a_9.setFont(QtGui.QFont('Arial', 14, weight=3))
tab3_a_10=QLabel('10. Export as Full Sweep')
tab3_a_10.setFont(QtGui.QFont('Arial', 14, weight=3))


##ROWS##
tab3_a_l.addRow(tab3_a_0)
tab3_a_l.addRow(tab3_a_i)
tab3_a_l.addRow(tab3_a_1)
tab3_a_l.addRow(tab3_a_2)
tab3_a_l.addRow(tab3_a_3)
tab3_a_l.addRow(tab3_a_4)
tab3_a_l.addRow(tab3_a_5)
tab3_a_l.addRow(tab3_a_6)
tab3_a_l.addRow(tab3_a_7)
tab3_a_l.addRow(tab3_a_8)
tab3_a_l.addRow(tab3_a_9)
tab3_a_l.addRow(tab3_a_10)



###Bloque B#####

tab3_b=QWidget()
tab3_b_l=QFormLayout()
tab3_b.setLayout(tab3_b_l)

### Lables
tab3_b_img_1=QLabel()
tab3_b_img_1.setPixmap(QPixmap(r'C:\Users\Sergio\Documents\PATCH\SCRIPTS\PROGRAMAS\Poking_Analysis_GUI\Resources\img\12.jpg'))
tab3_b_img_1.resize(5000,2000)

### Rows
tab3_b_l.addRow(tab3_b_img_1)

#Bloque C
tab3_c=QWidget()
tab3_c_l=QFormLayout()
tab3_c.setLayout(tab3_c_l)

####Labels####
font_tab3_c=QtGui.QFont('Arial', 20, weight=3, italic=True)
font_tab3_c.setBold(True)
font_tab3_c_i=QtGui.QFont('Arial', 14, weight=3, italic=True)
font_tab3_c_i.setBold(True)

tab3_c_0=QLabel('Data Preparation (Aligment, Leak Substraction and Indentation Linking)')
tab3_c_0.setFont(font_tab3_c)
tab3_c_0.setWordWrap(True)
tab3_c_0.setAlignment(QtCore.Qt.AlignCenter)
tab3_c_1=QLabel('After the process detailled bellow all the current traces will be aligned to the stim, leak substracted and sorted by their indentation value.')
tab3_c_1.setWordWrap(True)
tab3_c_1.setAlignment(QtCore.Qt.AlignJustify)
tab3_c_1.setFont(QtGui.QFont('Arial', 12, weight=3, italic=True))
tab3_c_1.setStyleSheet('color: grey')
tab3_c_i1=QLabel('Aligment')
tab3_c_i1.setFont(font_tab3_c_i)
tab3_c_2=QLabel('1. We extract the index of the first stimulus peak for each trace. The indexes can be extracted form any trace source (Stimulus or Current) because both traces share their indexes.')
tab3_c_2.setWordWrap(True)
tab3_c_2.setAlignment(QtCore.Qt.AlignJustify)
tab3_c_2.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_c_3=QLabel('2. We stablish this index as a reference point in the current traces.')
tab3_c_3.setWordWrap(True)
tab3_c_3.setAlignment(QtCore.Qt.AlignJustify)
tab3_c_3.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_c_4=QLabel('3. We trimed all current traces using the reference point to get the same lenth in all traces.')
tab3_c_4.setWordWrap(True)
tab3_c_4.setAlignment(QtCore.Qt.AlignJustify)
tab3_c_4.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_c_i2=QLabel('Leak Substraction')
tab3_c_i2.setFont(font_tab3_c_i)
tab3_c_5=QLabel('1. We select a region from each current trace inactive zone')
tab3_c_5.setWordWrap(True)
tab3_c_5.setAlignment(QtCore.Qt.AlignJustify)
tab3_c_5.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_c_6=QLabel('2. We stimate the mean of these regions individually')
tab3_c_6.setWordWrap(True)
tab3_c_6.setAlignment(QtCore.Qt.AlignJustify)
tab3_c_6.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_c_7=QLabel('3. We substract the mean value calculated before (leak) of each trace to the original one.')
tab3_c_7.setWordWrap(True)
tab3_c_7.setAlignment(QtCore.Qt.AlignJustify)
tab3_c_7.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_c_i3=QLabel('Indentation Level Linking')
tab3_c_i3.setFont(font_tab3_c_i)
tab3_c_8=QLabel('1. We generate a dictioray with every indentation levels in μm.')
tab3_c_8.setWordWrap(True)
tab3_c_8.setAlignment(QtCore.Qt.AlignJustify)
tab3_c_8.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_c_9=QLabel('2. We divide in two all stimulus traces to extrac the number of stim peaks. The division is nevesary due to the nanomotor functioning.')
tab3_c_9.setWordWrap(True)
tab3_c_9.setAlignment(QtCore.Qt.AlignJustify)
tab3_c_9.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_c_10=QLabel('3. We use as in index the number of peaks calculated above to extrac each respective indentation value from the dictionay.')
tab3_c_10.setWordWrap(True)
tab3_c_10.setAlignment(QtCore.Qt.AlignJustify)
tab3_c_10.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_c_11=QLabel('4. We generate a dictionary with all current traces sorted by their indentation values.')
tab3_c_11.setWordWrap(True)
tab3_c_11.setAlignment(QtCore.Qt.AlignJustify)
tab3_c_11.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))

####Rows#####
tab3_c_l.addRow(tab3_c_0)
tab3_c_l.addRow(tab3_c_1)
tab3_c_l.addRow(tab3_c_i1)
tab3_c_l.addRow(tab3_c_2)
tab3_c_l.addRow(tab3_c_3)
tab3_c_l.addRow(tab3_c_4)
tab3_c_l.addRow(tab3_c_i2)
tab3_c_l.addRow(tab3_c_5)
tab3_c_l.addRow(tab3_c_6)
tab3_c_l.addRow(tab3_c_7)
tab3_c_l.addRow(tab3_c_i3)
tab3_c_l.addRow(tab3_c_8)
tab3_c_l.addRow(tab3_c_9)
tab3_c_l.addRow(tab3_c_10)
tab3_c_l.addRow(tab3_c_11)
###Bloque D####
tab3_d=QWidget()
tab3_d_l=QFormLayout()
tab3_d.setLayout(tab3_d_l)


#labels
font_tab3_d=QtGui.QFont('Arial', 20, weight=3, italic=True)
font_tab3_d.setBold(True)

tab3_d_0=QLabel('Stim-Response')
tab3_d_0.setFont(font_tab3_d)
tab3_d_1=QLabel('1. We take the dictionary generated previously with all current traces ready to stimate the desired parameters.')
tab3_d_1.setWordWrap(True)
tab3_d_1.setAlignment(QtCore.Qt.AlignJustify)
tab3_d_1.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_d_2=QLabel('2. We calculate the min current value of each trace, as these are the current peaks generated in response of each stimulus.')
tab3_d_2.setWordWrap(True)
tab3_d_2.setAlignment(QtCore.Qt.AlignJustify)
tab3_d_2.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
#Rows
tab3_d_l.addRow(tab3_d_0)
tab3_d_l.addRow(tab3_d_1)
tab3_d_l.addRow(tab3_d_2)
###Bloque E####
tab3_e=QWidget()
tab3_e_l=QFormLayout()
tab3_e.setLayout(tab3_e_l)

#labels
font_tab3_e=QtGui.QFont('Arial', 20, weight=3, italic=True)
font_tab3_e.setBold(True)
tab3_e_0=QLabel('Threshold Stimation')
tab3_e_0.setFont(font_tab3_e)
tab3_e_1=QLabel('1. We extract the index of the first stimulus peak, to trim the aligned and leak substracted traces from this point.')
tab3_e_1.setWordWrap(True)
tab3_e_1.setAlignment(QtCore.Qt.AlignJustify)
tab3_e_1.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_e_2=QLabel('2. We calculte the mean and standard deviation from a inactive region of each current trace after the stimulus.')
tab3_e_2.setWordWrap(True)
tab3_e_2.setAlignment(QtCore.Qt.AlignJustify)
tab3_e_2.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_e_3=QLabel('3. mean and sd are used to set a threshold (mean+10*sd), to determine when the current response starts.')
tab3_e_3.setWordWrap(True)
tab3_e_3.setAlignment(QtCore.Qt.AlignJustify)
tab3_e_3.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_e_4=QLabel('4. If the current value is greather than our threshold, the index of this current value is saved.')
tab3_e_4.setWordWrap(True)
tab3_e_4.setAlignment(QtCore.Qt.AlignJustify)
tab3_e_4.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_e_5=QLabel('5. The threshold in µm is caluculated multiplying the index extracted by the indentaiton velocity and dividing all by the sampling ratio.')
tab3_e_5.setWordWrap(True)
tab3_e_5.setAlignment(QtCore.Qt.AlignJustify)
tab3_e_5.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
#Rows
tab3_e_l.addRow(tab3_e_0)
tab3_e_l.addRow(tab3_e_1)
tab3_e_l.addRow(tab3_e_2)
tab3_e_l.addRow(tab3_e_3)
tab3_e_l.addRow(tab3_e_4)
tab3_e_l.addRow(tab3_e_5)
###Bloque F####
tab3_f=QWidget()
tab3_f_l=QFormLayout()
tab3_f.setLayout(tab3_f_l)

#labels
font_tab3_f=QtGui.QFont('Arial', 20, weight=3, italic=True)
font_tab3_f.setBold(True)

tab3_f_0=QLabel('Tau Stimation')
tab3_f_0.setFont(font_tab3_f)
tab3_f_1=QLabel('1. We find the index of the first stimulus peak to trim the current trace, as we have done previously')
tab3_f_1.setWordWrap(True)
tab3_f_1.setAlignment(QtCore.Qt.AlignJustify)
tab3_f_1.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_f_2=QLabel('2. We stimate the initial guessings for the parameters a and c of the exponential fit model (b was previously calculated with a current trace model).')
tab3_f_2.setWordWrap(True)
tab3_f_2.setAlignment(QtCore.Qt.AlignJustify)
tab3_f_2.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_f_3=QLabel('3. The current trace was trimmed again from the minimal current value, since to adjust our data to an exponential fit only need to evaluate the region from the current peak until it becomes inactive again.')
tab3_f_3.setWordWrap(True)
tab3_f_3.setAlignment(QtCore.Qt.AlignJustify)
tab3_f_3.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_f_4=QLabel('4. Exponential model was stimated and ploted along with the current trace in the zoomed zone plot')
tab3_f_4.setWordWrap(True)
tab3_f_4.setAlignment(QtCore.Qt.AlignJustify)
tab3_f_4.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_f_5=QLabel('5. Tau value in mS is calculated using the optimal b parameter returned by the curve fit function (scipy). The invers of the b value is multiplied by the sampling ratio in KHz')
tab3_f_5.setWordWrap(True)
tab3_f_5.setAlignment(QtCore.Qt.AlignJustify)
tab3_f_5.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
tab3_f_6=QLabel('6. The tau value is only considered if it is between 1 and 50 mS, and the rSquared of the fiting model is greater than 0.6')
tab3_f_6.setWordWrap(True)
tab3_f_6.setAlignment(QtCore.Qt.AlignJustify)
tab3_f_6.setFont(QtGui.QFont('Arial', 13, weight=3, italic=True))
#Rows
tab3_f_l.addRow(tab3_f_0)
tab3_f_l.addRow(tab3_f_1)
tab3_f_l.addRow(tab3_f_2)
tab3_f_l.addRow(tab3_f_3)
tab3_f_l.addRow(tab3_f_4)
tab3_f_l.addRow(tab3_f_5)
tab3_f_l.addRow(tab3_f_6)
######
tab3_vsplit1.addWidget(tab3_a)
tab3_vsplit1.addWidget(tab3_b)
#
#tab3_layout.addWidget(tab3_vsplit1)
#
tab3_hsplit1.addWidget(tab3_vsplit1)
tab3_vsplit2.addWidget(tab3_c)
tab3_vsplit2.addWidget(tab3_d)
tab3_hsplit1.addWidget(tab3_vsplit2)
#
#tab3_layout.addWidget(tab3_hsplit1)
#
tab3_hsplit2.addWidget(tab3_hsplit1)
tab3_vsplit3.addWidget(tab3_e)
tab3_vsplit3.addWidget(tab3_f)
tab3_hsplit2.addWidget(tab3_vsplit3)
#
tab3_layout.addWidget(tab3_hsplit2) #Add tab3_hsplit2 only to the main layout, because every other splitters were added to tab3_hsplit2 previously
#################################################################

#DATA IMPORT
Data=[]
min_current=[]
DATA_WIDGET={}
STIM_WIDGET={}
SYNC_STIM={}
DATA_WIDGET_ALIGNED_SUBSTRACTED={}
THRESHOLD_D={}
TAU_DATA_WIDGET={}
TAU_VALUES={}
R_MIN={}
u=0
dictio5={}
peak_index=[]
def import_sweeps():
    '''This function imports the patch data from a .asc file containing data from a single cell exported from Patch Master Next. To get this file, Select the cell to export, next press the data button on top of the data tree.
        Here export as full sweep. First check if the export configuration is as follows: RELLENAR
        It fills the following dictionaries:
            CURRENT_WIDGET: the keys are the micrometers of indentation  and the values are the  RAW current traces.
            STIM_WIDGET: the keys are the micrometers of indentation  and the values are the RAW stim traces (Nanomotor Signal).
            SYNC_STIM: the keys are the micrometers of indentation  and the values are the stim traces aligned and trimmed (from -2000 points before the first stimul peak to 35000 points).
            DATA_WIDGET_ALIGNED_SUBSTRACTED: the keys are the micrometers of indentation  and the values are the current trace for indenteation, aligned to to the stimulus and leak substracted.
            THRESHOLD_D: the keys are the micrometers of indentation  and the values are the mechanical threshold values (µm) Calculated with the indentation speed and the sampling frequency and the time from the stimulation till the current.
            TAU_VALUES: the keys are the micrometers of indentation  and the values are the stimated TAU values (mS).
        '''
    
    global DATA_WIDGET_ALIGNED_SUBSTRACTED, STIM_WIDGET, THRESHOLD_D, TAU_DATA_WIDGET, TAU_VALUES
    Data.clear()
    DATA_WIDGET.clear()
    STIM_WIDGET.clear()
    DATA_WIDGET_ALIGNED_SUBSTRACTED.clear()
    file_filter = 'Data File (*.asc)'
    files = QFileDialog.getOpenFileNames(None,caption='Select Your records',directory=os.getcwd(),filter=file_filter)
    for file in files[0]:
        t=pd.read_csv(file, sep=',',skiprows=1, header=None,low_memory=False) 
        t.replace(' ', '')
        Sweep_split(t)
        #print(Data)
        #print(len(Data))
        for sweep in range(len(Data)):
            #print(sweep)
            Current_int=extract_current(Data,sweep)
            Nivel_indent=extract_indent(Data,sweep)
            Stim=extract_stim(Data,sweep)
            aa=st.mean(Current_int[0:100])
            a=st.mean(Current_int[0:800]-aa)
            b=st.mean(Current_int[int(len(Current_int)-1000): int(len(Current_int))]-aa)
            if abs(b)>= abs(300*a) :
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Sweep Deleted")
                msg.setInformativeText('Review your Data')
                msg.setWindowTitle("Warning")
                msg.exec_()
                #print('**Warning** Sweep Deleted')
            else:
                DATA_WIDGET[Nivel_indent]=Current_int
                STIM_WIDGET[Nivel_indent]=Stim
        SYNC_STIM=stim_sync(STIM_WIDGET)
        DATA_WIDGET_ALIGNED_SUBSTRACTED= stim_aling(STIM_WIDGET,DATA_WIDGET)
        THRESHOLD_D=threshold(SYNC_STIM,DATA_WIDGET_ALIGNED_SUBSTRACTED)
        TAU_VALUES=tau_calc(DATA_WIDGET_ALIGNED_SUBSTRACTED,SYNC_STIM)
#Import Button's logic
tab1_import_but.clicked.connect(import_sweeps)

def Sweep_split(t):
    '''This function extracs the full sweep from a DataFrame using its index and converts each sweep into a numpy array (dtype: float64) that is stored in the global variable data.
    t must be a dataframe'''
    global Data
    u=0
    l=(t.index[t.iloc[:,0].str.contains('Sweep')].tolist())
    for u in range(len(l)):
        if u==len(l)-1:
            g=t.iloc[l[-1]+2:,:].to_numpy().astype(np.float64)
        else:
            g=t.iloc[l[u]+2:l[u+1],:].to_numpy().astype(np.float64)
            Data.append(g)
def extract_current(Data,i):
    '''Data is a list of numpy arrays
    This function extracts the current vector from DATA numpy array'''
    temp2=Data[i][2:,3]
    return temp2
def baseline_sub(dictio):
    ''' This function takes a dictionary with keys beiing indentation amount and the values are curremt 
    traces obtained with the indentantion
    It produces a dictionary with the same keys and the base line substraction'''
    dict2={}
    for key in dictio.keys():
        temp=dictio.get(key)  
        b=st.mean(temp[0:80000])
        temp=temp-b
        dict2[key]=temp
    return dict2
    
def stim_aling(dictio1, dictio2):
    ''' This function takes two dictionaris:
        the first  keys beiing indentation amount and the values are curremt 
            traces obtained with the indentantion
        the second  with keys beiing indentation amount and the values are stim traces 
            traces obtained with the indentantion
    It produces a dictionary with the same keys and current traces aling to the stim'''
    temp0=baseline_sub(dictio2)
    dictio3={}
    for key in dictio1.keys():
        temp_dict=dictio1.get(key)
        stim_index, prominence = find_peaks (temp_dict, prominence = (5*1e-2, 5), width=0.001)
        temp2=temp0.get(key)
        temp2=temp2[stim_index[0]-2000:stim_index[0]+35000]
        dictio3[key]=temp2
    print('la data')
    print(dictio3)
    return (dictio3)
def extract_indent(Data,i):
    '''This function looks for the indentation value from the stim_dictionary. To do so, we split in two the stim trace and we count the numbers of peaks from the first half
    It produces a list with the number of stim peaks per each indentation'''
    temp2=Data[i][2:,1]
    temp3=int(int(len(temp2))/2)
    temp2=temp2[0:temp3]
    stim_index, prominence = find_peaks (temp2, prominence = (5*1e-2, 5), width=0.001)
    output=stim_dictionary.get(int(len(stim_index)))
    return output

def extract_stim(Data,i):
    '''This function extracts the stimulus vector from DATA numpy array
    Data is a list of numpy arrays'''
    temp1=Data[i][2:,1]
    return temp1
def stim_sync(dictio1):
    '''This function takes one dictionary and return another dictioary with the stim values trimmed '''
    temp3={}
    for key in dictio1.keys():
        temp_list=dictio1.get(key)
        stim_index, prominence = find_peaks (temp_list, prominence = (5*1e-2, 5), width=0.001)
        temp2=temp_list[stim_index[0]-2000:stim_index[0]+35000]
        temp3[key]=temp2
    return (temp3)
#Plotting
h=0
def plotting():
    '''This function plots full sweeps, the zoomed region with the TAU model and the tau bargraph '''
    '''The X-axis is divided by the sampling ratio to convert the indexes to ms'''
    i=0
    FS.clear()
    ZS.clear()
    TAV.clear()
    x=np.linspace(0,37000,37000)
    x2=x*float(1/int(tab1_Samp.text()))
    for key in DATA_WIDGET_ALIGNED_SUBSTRACTED.keys():
        lr = pg.LinearRegionItem([30,30+60])
        lr.setZValue(-10)
        if i==len(DATA_WIDGET_ALIGNED_SUBSTRACTED.keys())-1:
            #FS.plot(DATA_WIDGET_ALIGNED_SUBSTRACTED.get(key), pen=color_input.text(), width=15)
            FS.plot(x2,DATA_WIDGET_ALIGNED_SUBSTRACTED.get(key),
                    pen = pg.mkPen(FS_last_line_color_le.text(), width=float(FS_last_line_thickness_sb.value())))
            ZS.plot(x2,DATA_WIDGET_ALIGNED_SUBSTRACTED.get(key),
                    pen = pg.mkPen(ZS_last_line_color_le.text(), width=float(ZS_last_line_thickness_sb.value())))
        else:
            FS.plot(x2,DATA_WIDGET_ALIGNED_SUBSTRACTED.get(key), width=0.1,
                    pen = pg.mkPen(FS_line_color_le.text(), width=float(FS_line_thickness_sb.value())))
            ZS.plot(x2,DATA_WIDGET_ALIGNED_SUBSTRACTED.get(key), width=0.1,
                    pen = pg.mkPen(ZS_line_color_le.text(), width=float(ZS_line_thickness_sb.value())))
        def updatePlot():
            ZS.setXRange(*lr.getRegion(), padding=0)
        def updateRegion():
            lr.setRegion(ZS.getViewBox().viewRange()[0])
        lr.sigRegionChanged.connect(updatePlot)
        #ZS.sigXRangeChanged.connect(updateRegion)
        i=i+1
    tau_plot(dictio5,peak_index)
    #Añadir la región Zoom
    FS.addItem(lr)
    updatePlot()

#Connect the import data button with plotting funtion
tab1_import_but.clicked.connect(plotting)
tab1_replot_but.clicked.connect(plotting)
FS_apply_but.clicked.connect(plotting)
ZS_apply_but.clicked.connect(plotting)
TAV_apply_but.clicked.connect(plotting)
def find_min():
    '''This function takes a dictionary with the current values aligned to the stim and leak substracted.
    It produces a dictionary beeing the keys the indentation level and the values the minimum current values. '''
    i=0
    min_current.clear()
    SR.clear()
    for key in DATA_WIDGET_ALIGNED_SUBSTRACTED.keys():
        min_current.append(-1*min(DATA_WIDGET_ALIGNED_SUBSTRACTED.get(key)))
        R_MIN[key]=min(DATA_WIDGET_ALIGNED_SUBSTRACTED.get(key))  
    for key in DATA_WIDGET_ALIGNED_SUBSTRACTED.keys():
        if i==len(DATA_WIDGET_ALIGNED_SUBSTRACTED.keys())-1:
             SR.plot(list(DATA_WIDGET_ALIGNED_SUBSTRACTED.keys()),min_current, symbolBrush=SR_symbol_color_le.text(), pen=pg.mkPen(SR_line_color_le.text(), width=float(SR_line_size_sb.value())),symbol=SR_symbol_type_cb.currentText(),symbolSize =SR_symbol_size_sb.value())
        else:
            SR.plot(list(DATA_WIDGET_ALIGNED_SUBSTRACTED.keys()),min_current, symbolBrush=SR_symbol_color_le.text(), pen=pg.mkPen(SR_line_color_le.text(), width=float(SR_line_size_sb.value())),symbol=SR_symbol_type_cb.currentText(),symbolSize=SR_symbol_size_sb.value())
        R_MIN[key]=min(DATA_WIDGET_ALIGNED_SUBSTRACTED.get(key))  
        i=i+1
tab1_import_but.clicked.connect(find_min)
tab1_replot_but.clicked.connect(find_min)
SR_apply_but.clicked.connect(find_min)


def thershld_index(lst, t):
    '''This function stablishes a trheshold to extract the frist index of the stimuly since it starts, and returns the indexes values '''
    for i in lst:
        if abs(i) >abs(t):
            break
    return lst.index(i)

def threshold(dictio1,dictio2):
    '''This function calculate the threshold in micrometers
        This function takes two dictionaries:
            The first keys being the indentation level and values the stimulus traces
            The second keys being the indentation level and values the current traces leak substracted and aligned to the stimulus
        This function produces a dictionary being keys the indentation level and values the threshold values in Um
            The threshold is calculated using the extracted stimulus indexes. Multiplying these indexes by the indentation velocity and dividing all by the sample ratio in KHz'''
    dictio3={}
    for key in dictio1.keys():
        temp1=dictio1.get(key)
        temp2=dictio2.get(key)
        stim_index, prominence = find_peaks (temp1, prominence = (5*1e-2, 5), width=0.001)
        temp3=temp2[stim_index[0]:len(temp2)]
        m=st.mean(temp3[0:100])
        ds=st.stdev(temp3[0:100])
        th=float(abs(m)+float(10*ds))
        threshold_index=thershld_index(list(temp3),th)
        if threshold_index >= 1000:
            dictio3[key]=0
        else:    
            dictio3[key]=float(tab1_Ind_V.text())*threshold_index/int(tab1_Samp.text()) #ms desde que empieza el estímulo hasta que se inicia la corriente
    return dictio3

def stim_threshold_plot():
    '''This function plots the threshlold values in Um in the Y-axis and the indentation values in Um in the X-axis'''
    TH.clear()
    TH.plot(list(THRESHOLD_D.keys()),list(THRESHOLD_D.values()), pen=pg.mkPen(TH_line_color_le.text(), width=float(TH_line_size_sb.value())),symbol=TH_symbol_type_cb.currentText(),symbolSize =TH_symbol_size_sb.value())
tab1_import_but.clicked.connect(stim_threshold_plot)
tab1_replot_but.clicked.connect(stim_threshold_plot)
TH_apply_but.clicked.connect(stim_threshold_plot)


def refresh():
    '''This function clears all list and dictionaries when we press the refress button'''
    Data.clear()
    min_current.clear()
    DATA_WIDGET.clear()
    STIM_WIDGET.clear()
    SYNC_STIM.clear()
    DATA_WIDGET_ALIGNED_SUBSTRACTED.clear()
    THRESHOLD_D.clear()
    TAU_DATA_WIDGET.clear()
    TAU_VALUES.clear()
    R_MIN.clear()
    u=0
    dictio5.clear()
    peak_index.clear()
    SR.clear()
    ZS.clear()
    FS.clear()
    TH.clear()
    TAV.clear()
    msg1 = QMessageBox()
    msg1.setIcon(QMessageBox.Information)
    msg1.setText("All Data Cleared")
    msg1.setInformativeText('Please Import New Data')
    msg1.setWindowTitle("Data Info")
    msg1.exec_()
tab1_plot_min_but.clicked.connect(refresh)

def exp_fit(x,a,b,c):
    '''This function distibute our data as an exponetial function'''
    y=a*np.exp(b*x)+c
    return y
def tau_plot(dictio,peak_index):
    '''This function takes a dictionary and a list:
        Dictionary: being the keys the indentation level and the values the current traces leak substracted and aligned to the stim.
        List: the indexes of the minimum current values of each trace.
    This function plots the exponential fitting model of the current traces in the zoomed zone plot being the first point of the model the minimum value of the current trace (peak_index).'''
    '''The X-axis is divided by the sampling ratio to convert the indexes to ms'''
    dictio5=dictio
    peaks=peak_index
    i=0
    for key in dictio5.keys():
        indice=peaks[i]
        x=np.linspace(indice/int(tab1_Samp.text()),10000/int(tab1_Samp.text()),10000)
        if  dictio5[key][0]!=0 and dictio5[key][1]!=0 and dictio5[key][2]!=0:
            ZS.plot(x + 2000/int(tab1_Samp.text()), exp_fit(x, *dictio5.get(key)), pen = pg.mkPen(ZS_fit_line_color_le.text(), width=float(ZS_fit_line_thickness_sb.value())))
        i=i+1
        #2000 aditional points to aling the fit to the trace
        #Pen --> Edits the border.
        #Brush --> Edits the bar.
    bargraph = pg.BarGraphItem(x=list(TAU_VALUES.keys()), height = list(TAU_VALUES.values()), width = 0.48, pen=pg.mkPen(TAV_border_color_le.text(),width=float(TAV_border_thickness_sb.value())), brush=TAV_bar_color_le.text())
    TAV.addItem(bargraph)   
def tau_calc(dictio1, dictio2):
    '''This function stimates the TAU values
        This function takes two dictionaries:
            The first being the keys the indentation level and the values the current traces leak substracted and aligned to the stimulus.
            The second being the keys the indentation level and the values the stimules traces.
        (1) Extracts the index of the frist minimum value of each stimulus trace
        (2) Trims the current traces from the index extracted above (stim_index) to 35000 points.
        (3) Stablish the initial guessings for the fitting model
                a0 = The minimum current value of each trace.
                c0 = The mean of the first 200 points of each current trace model.
        (4) Calculates the fiting model with the initial guessings and the curve_fit function
                Populate a dictionary being the keys the indentation level and the values the optimal params for the fitting model.
                Returns the R2 value and the function equation.
        (5) Calculates the TAU value in ms dividing the invers of the b param by the sample ratio in KHz.
            The main function returns a dictionary being the keys the indentation level and the values the TAU values in ms.'''
    
    '''The X-axis is divided by the sampling ratio to convert the indexes to ms'''
    global dictio5,peak_index
    dictio3={}
    dictio4={}
    for key in dictio1.keys():
        temp1=dictio1.get(key)
        temp2=dictio2.get(key)
        stim_index, prominence = find_peaks (temp2, prominence = (5*1e-2, 5), width=0.001)
        temp3=temp1[stim_index[0]:stim_index[0]+35000]
        base=st.mean(temp1[0:200])
        m=min(temp3)
        temp3=temp3.tolist()
        temp_peak_index=int(temp3.index(min(temp3)))
        peak_index.append(temp_peak_index)
        temp4=temp3[int(temp3.index(min(temp3))):int(temp3.index(min(temp3)))+10000]
        x=np.linspace(temp_peak_index,10000,len(temp4))/int(tab1_Samp.text())
        #Los parámetros los he sacado de la función que si podía calcular el fit
        #a=-9.6*1e-9
        a0=m 
        #b0=-4.43*1e-3
        b0=-0.30
        #c=-8.44*1e-3
        c0=base
        dictio3[key]=temp4
        p0=(a0,b0,c0)
        #print(dictio3)
        try:
            params,cv=curve_fit(exp_fit,x,temp4,p0)
            a,b,c= params
            tau=(1/abs(b))
            tau=round(tau,2)
            print('PARAMSSS')
            #print(a,b,c)
            print(tau)
           # determine quality of the fit
            squaredDiffs = np.square(temp4 - exp_fit(x, *params))
            squaredDiffsFromMean = np.square(temp4 - np.mean(temp4))
            rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
            print(f"R² = {rSquared}")
            print(f"Y = {a} * e^({b} * x) + {c}")
            if  1 < tau< 50 and abs(rSquared) > 0.6:
                dictio4[key]=tau
                dictio5[key]=params
            else:
                dictio4[key]=0
                dictio5[key]=0,0,0
        except RuntimeError:
            pass
            print('Tau Calculus Skipped')
    return dictio4
"""
def save_mim_results():
    '''This function takes the data dictionaries and saves them into three csv files '''
    csv_path='R_'+tab1_record_data.text()+'/'+tab1_Mutant_ID.text()+'/'
    csv_name_ta=csv_path+tab1_cell_ID.text()+'_TAU_VALUES.csv'
    csv_name_th=csv_path+tab1_cell_ID.text()+'_THESHOLD_STIMATION.csv'
    csv_name_src=csv_path+tab1_cell_ID.text()+'_STIM_CURRENT_RESONSE.csv'
    ta=pd.DataFrame(TAU_VALUES,columns=TAU_VALUES.keys(), index=[0])
    th=pd.DataFrame(THRESHOLD_D,columns=THRESHOLD_D.keys(), index=[0])
    src=pd.DataFrame(R_MIN,columns=R_MIN.keys(), index=[0])
    os.makedirs(csv_path, exist_ok=True)  
    ta.to_csv(csv_name_ta,sep='\t')
    th.to_csv(csv_name_th,sep='\t')
    src.to_csv(csv_name_src,sep='\t')
#tab1_save_results_but.clicked.connect(save_mim_results)
"""

def save_files():
    csv_path='C:'+'/'+'Users'+'/'+ str(os.getlogin())+'/'+'Documents'+'/'+'Results'+'/'+tab1_record_data.text()+'/'+tab1_Mutant_ID.text()+'/'+tab1_cell_ID.text()+'/'
    os.makedirs(csv_path,exist_ok=True)
    ta=pd.DataFrame(TAU_VALUES,columns=TAU_VALUES.keys(), index=['TAU (ms)'])
    th=pd.DataFrame(THRESHOLD_D,columns=THRESHOLD_D.keys(), index=['Threshold (ms)'])
    scr=pd.DataFrame(R_MIN,columns=R_MIN.keys(), index=['Current (A)'])
    name_ta = QFileDialog.getSaveFileName(None,caption='TAU VALUES',directory= csv_path , filter='CSV (*.csv)')
    name_th = QFileDialog.getSaveFileName(None,caption='THRESHOLD VALUES',directory=csv_path, filter='CSV (*.csv)')
    name_scr = QFileDialog.getSaveFileName(None,caption='STIM CURRENT RESPONSE',directory=csv_path, filter='CSV (*.csv)')
    file_ta = open(str(name_ta[0]),'w')
    file_th = open(str(name_th[0]),'w')
    file_scr = open(str(name_scr[0]),'w')
    ta.to_csv(str(name_ta[0]),sep='\t')
    th.to_csv(str(name_th[0]),sep='\t')
    scr.to_csv(str(name_scr[0]),sep='\t')
    file_ta.close()
    file_th.close()
    file_scr.close()
tab1_save_results_but.clicked.connect(save_files)








def update_plottings_settings():
    global color_traces, color_fit, line_pen, symbol_pen, symbol_color
    FS.clear()
    ZS.clear()
    plotting()

    color_traces = (174, 175, 176)
    color_fit = (196, 112, 2)
    line_pen = pg.mkPen(plot_line_color.text(), width=6)
    symbol_pen = pg.mkPen('#FFB562', width=2)
    symbol_color = (symbol_fill_color.text())
    TH.clear()
    stim_threshold_plot()

apply_but.clicked.connect(update_plottings_settings)

###PLOT SETINGS WINDOWS SHOW FUNCTIONS###

def FS_settings_window_show():
    FS_settings_window.show()
tab1_FS_settings_but.clicked.connect(FS_settings_window_show)

def ZS_settings_window_show():
    ZS_settings_window.show()
tab1_ZS_settings_but.clicked.connect(ZS_settings_window_show)


def SR_settings_window_show():
    SR_settings_window.show()
tab1_SR_settings_but.clicked.connect(SR_settings_window_show)

def TH_settings_window_show():
    TH_settings_window.show()
tab1_TH_settings_but.clicked.connect(TH_settings_window_show)

def TAV_settings_window_show():
    TAV_settings_window.show()
tab1_TAV_settings_but.clicked.connect(TAV_settings_window_show)

tabs.show()
if __name__ == '__main__':
    pg.exec()
