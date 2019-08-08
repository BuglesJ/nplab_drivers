from time import sleep, time
import numpy as np

import qcodes as qc
from qcodes import Instrument, VisaInstrument, validators as vals
from qcodes.instrument.channel import InstrumentChannel


class Keithley_617(VisaInstrument):
	def __init__(self, name, address, **kwargs):
		super().__init__(name, address, terminator='\r', **kwargs)

		self.add_parameter('display_mode',
							set_cmd='D{}X')


		self.add_parameter('backgate_voltage', unit='V', 
							set_cmd='V{:.2f}X',
							get_cmd='B4X',
							get_parser=float)
		self.connect_message()