import roboticstoolbox as rtb
import numpy as np
import spatialmath as sm
from exceptions.coordinates_unreachable_exception import CoordinatesUnreachableException
from robot_models.scara_model.default_config import DefaultConfig


class ScaraModel:
    def __init__(self, config: DefaultConfig=DefaultConfig()) -> None:
        self._config = config
        self._upper_arm_length = config.upper_arm_length
        self._forearm_length = config.forearm_length
        self._rotate_restrictions_deg = config.rotate_restrictions_deg

        self._init_robot_model()
        self._init_robot_restrictions()


        # Выводим информацию о роботе
        print(self._robot)
        print("test")



    def _init_robot_model(self):
        self._L1 = rtb.RevoluteDH(d=0, a=self._upper_arm_length, alpha=0)
        self._L2 = rtb.RevoluteDH(d=0, a=self._forearm_length, alpha=0)

        # Создаем робота из звеньев
        self._robot = rtb.DHRobot([self._L1, self._L2], name="2DOF_Robot")

    def _init_robot_restrictions(self):
        # Устанавливаем ограничения углов поворота
        self._robot.qlim = np.array([
            [-np.radians(self._rotate_restrictions_deg), np.radians(self._rotate_restrictions_deg)],  # -135° to 135°
            [-np.radians(self._rotate_restrictions_deg), np.radians(self._rotate_restrictions_deg)]  # -135° to 135°
        ])

    def get_angle_degrees_from_coordinates(self, target_x, target_y):
        solution = self._calculate_reverse_kinematics(target_x, target_y)

        if not solution.success:
            raise CoordinatesUnreachableException([target_x, target_y])

        solution_rad = solution.q
        solution_deg = np.degrees(solution_rad)

        return solution_deg

    def _calculate_reverse_kinematics(self, target_x, target_y):
        target_z = 0
        target_pose = sm.SE3(target_x, target_y, target_z)
        solution = self._robot.ikine_LM(target_pose)

        return solution

    def get_coordinates_from_angles(self, angles_deg):
        x, y, z = self.forward_kinematics(angles_deg)

        return [x, y]

    def forward_kinematics(self, angles_deg):
        angles_rad = np.radians(angles_deg)
        pose = self._robot.fkine(angles_rad)

        x = pose.t[0]
        y = pose.t[1]
        z = pose.t[2]

        return x, y, z

    def get_camera_coordinates(self, angles_deg, offset_from_joint=0.050):
        q1_rad = np.radians(angles_deg[0])

        joint_x = self._L1.a * np.cos(q1_rad)
        joint_y = self._L1.a * np.sin(q1_rad)

        q_total_rad = np.radians(angles_deg[0] + angles_deg[1])
        camera_x = joint_x + offset_from_joint * np.cos(q_total_rad)
        camera_y = joint_y + offset_from_joint * np.sin(q_total_rad)

        return camera_x, camera_y, 0

    def get_camera_angle(self, angles_deg):
        camera_angle = angles_deg[0] + angles_deg[1]

        return camera_angle

