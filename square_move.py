variable_LedID = 0
list_LedList = RmList()
def start():
    global variable_LedID
    global list_LedList
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    media_ctrl.play_sound(rm_define.media_sound_count_down)
    chassis_ctrl.set_trans_speed(2.0)
    chassis_ctrl.move_with_time(0,1)
    time.sleep(1)
    chassis_ctrl.move_with_time(-90,1)
    time.sleep(1)
    chassis_ctrl.move_with_time(-180,1)
    time.sleep(1)
    chassis_ctrl.move_with_time(90,1)
    time.sleep(1)
    rmexit()
