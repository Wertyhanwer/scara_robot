import roboticstoolbox as rtb
import numpy as np
import spatialmath as sm


class RobotModel:
    def __init__(self):
        self.L1 = rtb.RevoluteDH(d=0, a=0.300, alpha=0)  # 300 мм = 0.3 м
        self.L2 = rtb.RevoluteDH(d=0, a=0.321, alpha=0)  # 321 мм = 0.321 м

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

    def reverse_kinematics(self, target_x, target_y):

        # Создаем целевую позу в 3D (SE3)
        target_pose = sm.SE3(target_x, target_y, 0)

        print(f"Целевая точка: ({target_x * 1000}мм, {target_y * 1000}мм)")

        # Решаем обратную кинематику
        solution = self.robot.ikine_LM(target_pose)

        if solution.success:
            angles_rad = solution.q
            angles_deg = np.degrees(angles_rad)

            print(f"✅ Найдено решение!")
            print(f"Углы в радианах: {angles_rad}")
            print(f"Углы в градусах: {angles_deg}")

            # Проверяем решение через прямую кинематику
            check_pose = self.robot.fkine(angles_rad)
            print(f"Проверка: робот окажется в ({check_pose.t[0] * 1000:.1f}мм, {check_pose.t[1] * 1000:.1f}мм)")

        else:
            print("❌ Цель недостижима!")

        print(solution)
        return solution