import cv2
from usefuladbplus import activate_pandas_extensions, AdbControlPlus
from PrettyColorPrinter import add_printer
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
    use_busybox=False,
    connect_to_device=True,
    invisible=True,
    print_stdout=True,
    print_stderr=True,
    limit_stdout=3,
    limit_stderr=3,
    limit_stdin=None,
    convert_to_83=True,
    wait_to_complete=0.1,
    flush_stdout_before=True,
    flush_stdin_before=True,
    flush_stderr_before=True,
    exitcommand="xxxCOMMANDxxxDONExxx",
    capture_stdout_stderr_first=True,
    global_cmd=False,
    global_cmd_timeout=10,
    use_eval=True,
    eval_timeout=180,
)
