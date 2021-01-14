from enum import Enum

import sys

class JCSignal(Enum):
	startingUp			   = 'StartingUp'
	restartingBluetooth    = 'RestartingBluetooth'
	advertisingBluetooth   = 'AdvertisingBluetooth'
	waitingForSwitch       = 'WaitingForSwitch'
	connectionEstablished  = 'ConnectionEstablished'
	readyForInput          = 'ReadyForInput'
	failurePortInUse       = 'FailurePortInUse'
	startedCommand         = 'StartedCommand'
	finishedCommand        = 'FinishedCommand'
	disconnected           = 'Disconnected'
	unknown                = 'Unknown'

	def serialstring(self):
		raw = self.value
		serial = 'JC*' + raw
		return serial



def send_signal(signal: JCSignal):
	# sys.stderr.write(signal.serialstring())
	print(signal.serialstring(), flush=True)


