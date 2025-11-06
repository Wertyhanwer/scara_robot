import roboticstoolbox as rtb
import numpy as np
import spatialmath as sm
from exceptions.coordinates_unreachable_exception import CoordinatesUnreachableException


class ScaraModel:
    def __init__(self):
        self.L1 = rtb.RevoluteDH(d=0, a=0.29835, alpha=0)  # 300 мм = 0.3 м
        self.L2 = rtb.RevoluteDH(d=0, a=0.16584, alpha=0)  # 321 мм = 0.321 м

        # Создаем робота из звеньев
        self.robot = rtb.DHRobot([self.L1, self.L2], name="2DOF_Robot")

        # Устанавливаем ограничения углов поворота
        self.robot.qlim = np.array([
            [-np.radians(135), np.radians(135)],  # -135° to 135°
            [-np.radians(135), np.radians(135)]  # -135° to 135°
        ])

        # Выводим информацию о роботе
        print(self.robot)
        print("test")


    def get_angle_degrees_from_coordinates(self, target_x, target_y):
        solution = self.calculate_reverse_kinematics(target_x, target_y)

        if not solution.success:
            raise CoordinatesUnreachableException([target_x, target_y])

        solution_rad = solution.q
        solution_deg = np.degrees(solution_rad)

        return solution_deg

    def calculate_reverse_kinematics(self, target_x, target_y):
        target_pose = sm.SE3(target_x, target_y, 0)
        solution = self.robot.ikine_LM(target_pose)

        return solution

    def get_coordinates_from_angles(self, angles_deg):
        x, y, z = self.forward_kinematics(angles_deg)

        return [x, y]

    def forward_kinematics(self, angles_deg):
        angles_rad = np.radians(angles_deg)
        pose = self.robot.fkine(angles_rad)

        x = pose.t[0]
        y = pose.t[1]
        z = pose.t[2]

        return x, y, z

    def get_camera_coordinates(self, angles_deg, offset_from_joint=0.050):
        q1_rad = np.radians(angles_deg[0])

        joint_x = self.L1.a * np.cos(q1_rad)
        joint_y = self.L1.a * np.sin(q1_rad)

        q_total_rad = np.radians(angles_deg[0] + angles_deg[1])
        camera_x = joint_x + offset_from_joint * np.cos(q_total_rad)
        camera_y = joint_y + offset_from_joint * np.sin(q_total_rad)

        return camera_x, camera_y, 0

    def get_camera_angle(self, angles_deg):
        camera_angle = angles_deg[0] + angles_deg[1]

        return camera_angle