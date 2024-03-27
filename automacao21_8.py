import cv2
from usefuladbplus import activate_pandas_extensions, AdbControlPlus
from PrettyColorPrinter import add_printer
from time import sleep, time
import numpy as np

add_printer(1)
activate_pandas_extensions(
    modules=(
        "plus_find_shapes",
        "plus_template_matching",
        "plus_color_search_c",
        "plus_color_cluster",
        "plus_count_all_colors",
        "plus_count_all_colors_coords",
        "plus_fuzzy_merge",
        "plus_tesser_act",
    )
)
addr = "127.0.0.1:5555"
adb_path = r"C:\Program Files\BlueStacks_nxt\HD-Adb.exe"
AdbControlPlus.connect_to_all_tcp_devices_windows(
    adb_path=adb_path,
)
adb = AdbControlPlus(
    adb_path=adb_path,
    device_serial=addr,
    use_busybox=False,  # uses busybox to decode base64
    connect_to_device=True,
    invisible=True,  # windows only - doesn't open a shell window, when you compile the code with nuitka, for example
    print_stdout=True,
    print_stderr=True,
    limit_stdout=3,  # limits the history of shellcommands - can be checked at blocking_shell.stdout
    limit_stderr=3,  # limits the history of shellcommands - can be checked at blocking_shell.stderr
    limit_stdin=None,  # limits the history of shellcommands - can be checked at blocking_shell.stdin
    convert_to_83=True,  # converts the adb path to 8.3 on Windows
    wait_to_complete=0,  # doesn't matter if global_cmd is True
    flush_stdout_before=True,  # flushes the history in  blocking_shell.stdout
    flush_stdin_before=True,  # flushes the history in blocking_shell.stderr
    flush_stderr_before=True,  # flushes the history in  blocking_shell.stdin
    exitcommand="xxxCOMMANDxxxDONExxx",
    # Written using echo at the end of every command to determine when the output is finished.
    capture_stdout_stderr_first=True,  # doesn't matter if global_cmd is True
    global_cmd=True,  # global, because variables/su status/dirs stay
    global_cmd_timeout=10,  # if a command doesn't return stderr/stdout in a given time
)
adb.sh_input_mouse_swipe(x0=450, y0=100, x1=500, y1=500, t=1.0)