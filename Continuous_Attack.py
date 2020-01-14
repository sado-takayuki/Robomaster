list_angle_list = RmList()
variable_flag = 0
variable_i = 0
def user_defined_shoot():
    global variable_flag
    global variable_i
    global list_angle_list
    variable_i = 1
    for count in range(3):
        gimbal_ctrl.angle_ctrl(list_angle_list[1], list_angle_list[2])
        gun_ctrl.fire_once()
        variable_i = variable_i + 2
        time.sleep(0.2)
def user_defined_storage_angle():
    global variable_flag
    global variable_i
    global list_angle_list
    led_ctrl.gun_led_on()
    list_angle_list.append(gimbal_ctrl.get_axis_angle(rm_define.gimbal_axis_yaw))
    list_angle_list.append(gimbal_ctrl.get_axis_angle(rm_define.gimbal_axis_pitch))
    time.sleep(5)
    led_ctrl.gun_led_off()
def start():
    global variable_flag
    global variable_i
    global list_angle_list
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.set_rotate_speed(180)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_trans_red_heart)
    time.sleep(5)
    user_defined_storage_angle()

    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_three)
    time.sleep(3)
    user_defined_storage_angle()

    user_defined_shoot()
