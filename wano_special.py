
def start():
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    chassis_ctrl.set_trans_speed(0.5)
    gimbal_ctrl.set_rotate_speed(100)
    vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_three)
    gun_ctrl.fire_once()
    gun_ctrl.set_fire_count(1)
    for count in range(2):
        media_ctrl.play_sound(rm_define.media_sound_solmization_1C)
        gimbal_ctrl.angle_ctrl(25, 35)
        gimbal_ctrl.angle_ctrl(0, 0)
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_green)
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    chassis_ctrl.move_with_time(0,5)
