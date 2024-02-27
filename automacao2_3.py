import cv2
from usefuladbplus import activate_pandas_extensions, AdbControlPlus
from PrettyColorPrinter import add_printer
from time import sleep, time

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


def clickfunc(
    fu,
    timeout,
    with_screenshot=True,
    screenshot=None,
    nice=False,
    su=False,
    with_sendevent=True,
    **kwargs,
):
    timeoutfinal = timeout + time()
    while time() < timeoutfinal:
        try:
            df = adb.plus_uidump(
                timeout=timeout,
                with_screenshot=with_screenshot,
                screenshot=screenshot,
                nice=nice,
                su=su,
                with_sendevent=with_sendevent,
            )
            df = fu(df, **kwargs)
            return True

        except Exception as e:
            print(e)
    return False


def abrir_url(df, url):
    df.loc[
        df["aa_resource-id"] == "com.kiwibrowser.browser:id/location_bar"
    ].ff_input_tap.iloc[0]()
    sleep(1)
    adb.input_text(url)
    sleep(1)
    adb.keyevents.KEYCODE_ENTER.longpress()


codigo_para_executar = [
    lambda df: df.loc[
        (df.aa_index == "2") & (df.aa_class == "android.view.View")
    ].ff_input_tap.iloc[0](),
    lambda df: abrir_url(df, url="http://microsoft.com"),
]
for fu in codigo_para_executar:
    deu_certo = clickfunc(
        fu=fu,
        timeout=60,
        with_screenshot=False,
        screenshot=None,
        nice=False,
        su=False,
        with_sendevent=False,
    )
    if not deu_certo:
        print("deu ruim")
        break


# while True:
#     try:
#         df = adb.plus_uidump(
#             timeout=60,
#             with_screenshot=True,
#             screenshot=None,
#             nice=False,
#             su=False,
#             with_sendevent=True,
#         )
#         df.loc[
#             (df.aa_index == "2") & (df.aa_class == "android.view.View")
#         ].ff_input_tap.iloc[0]()
#         break

#     except Exception as e:
#         print(e)
# sleep(1)
# while True:
#     try:
#         df = adb.plus_uidump(
#             timeout=60,
#             with_screenshot=True,
#             screenshot=None,
#             nice=False,
#             su=False,
#             with_sendevent=True,
#         )
#         df.loc[
#             df["aa_resource-id"] == "com.kiwibrowser.browser:id/location_bar"
#         ].ff_input_tap.iloc[0]()
#         break

#     except Exception as e:
#         print(e)

# sleep(1)
# adb.input_text("http://www.bet365.com")
# sleep(1)
# adb.keyevents.KEYCODE_ENTER.longpress()
