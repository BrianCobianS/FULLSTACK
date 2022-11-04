import logging
import os4690
import sys
import os

print("Accepting the maintenance of ACE...")

RCP_CMD='adx_spgm:adxcsh0l.286 BACKGRND N'
SELECTION_FILE='adx_idt1:adxcshcf.dat'
CMD_FILE='adx_idt1:eamrcp1f.dat'
STATUS_FILE='/mnt/c/adx_sdt1/adxcshsf.dat'

FUNCTION=["Test", "Cancel", "Accept","Transfer"]
F_SELECTION=(FUNCTION.index(sys.argv[1]) + 1)
#ACTIVATE_OS=('ADXCST0L Y 3AG BY\r\n')
ACTIVATE_OS=('ADXCST0L Y ' + str(F_SELECTION) + 'AG BY\r\n')

selectionFile = open(SELECTION_FILE,'w')
selectionFile.write(CMD_FILE+'\r\n')
selectionFile.close()

cmdFile = open(CMD_FILE, 'w')
cmdFile.write(ACTIVATE_OS)
cmdFile.close()

os4690.system(RCP_CMD)

print("More info, please check the cadx_sdt1:adxcshsf.dat file")