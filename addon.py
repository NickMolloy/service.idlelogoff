import xbmc
import xbmcaddon

__settings__ = xbmcaddon.Addon()
max_idle_time = (int(__settings__.getSetting("logoff_time"))) * 60
library_scan_logoff = __settings__.getSetting("logoff_library_scan")
sleep_time = 5000  # Length of time to sleep, in milliseconds
idle_time_delta = 0

while (not xbmc.abortRequested):

    idle_time = xbmc.getGlobalIdleTime() - idle_time_delta

    # "Reset" idle time because media is playing
    if (xbmc.Player().isPlaying()):
        idle_time_delta = idle_time

    # Check if we should ensure we don't log off while a scan is taking place
    elif (library_scan_logoff): 
	# "Reset" idle time if library scan is taking place
        if (xbmc.getCondVisibility("Library.IsScanningMusic") | xbmc.getCondVisibility("Library.IsScanningVideo")):
            idle_time_delta = idle_time

    # Log off if we have exceeded the idle time
    elif (idle_time > max_idle_time):
        xbmc.executebuiltin("System.LogOff")

    if (not xbmc.abortRequested):
        xbmc.sleep(sleep_time)
