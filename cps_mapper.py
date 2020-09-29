import ctypes
import asyncio  # asyncio is the best, lol! [Theading breaks the timing]
from config import (logger, LBTN_KEY, RBTN_KEY, LBTN_P, LBTN_R, 
					RBTN_P, RBTN_R, LCPS, RCPS, RCLICKING, LCKICKING)

user32 = ctypes.windll.user32


lstat = user32.GetKeyState(LBTN_KEY)
rstat = user32.GetKeyState(RBTN_KEY)


async def lclicker(cps):
	while LCKICKING:
		user32.mouse_event(LBTN_P, 0, 0, 0, 0)
		user32.mouse_event(LBTN_R, 0, 0, 0, 0)
		await asyncio.sleep(1/cps)
	return


async def rclicker(cps):
	while RCLICKING:
		user32.mouse_event(RBTN_P, 0, 0, 0, 0)
		user32.mouse_event(RBTN_R, 0, 0, 0, 0)
		await asyncio.sleep(1/cps)
	return


async def main():
	global lstat, rstat, RCLICKING, LCKICKING

	logger.info(f"Starting... {LCPS}cps|{RCPS}cps [CTRL+C to exit]")

	while True:
		nlstat = user32.GetKeyState(LBTN_KEY)
		nrstat =user32.GetKeyState(RBTN_KEY)
		tasks = []

		if nlstat != lstat:  # Detect LBTN_KEY button stat changes
			if nlstat not in [0, 1]:  # Button pressed
				if LCPS > 0:
					LCKICKING = True
					task = asyncio.create_task(lclicker(LCPS))  # Create lclicker task
					tasks.append(task)
					logger.info("Started left clicking.")
			else:  # Button released
				LCKICKING = False
				logger.info("Stopped left clicking.")

		if nrstat != rstat:  # Detect RBTN_KEY button stat changes
			if nrstat not in [0, 1]:  # Button pressed
				if RCPS > 0:
					RCLICKING = True
					task = asyncio.create_task(rclicker(RCPS))  # Create rclicker task
					tasks.append(task)
					logger.info("Started right clicking.")
			else:  # Button released
				RCLICKING = False
				logger.info("Stopped right clicking.")

		lstat, rstat = nlstat, nrstat  # Swap values to detect next time changes
		await asyncio.sleep(0.001)

	
try:
	asyncio.run(main())
except KeyboardInterrupt:
	logger.info("Exiting...")
	exit()
