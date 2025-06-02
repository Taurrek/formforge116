import numpy as np

class SensorFusion:
    def __init__(self):
        self.pose_data_buffer = []
        self.imu_data_buffer = []
        self.hr_data_buffer = []
        self.gps_data_buffer = []

    def add_pose_data(self, keypoints):
        self.pose_data_buffer.append(keypoints)

    def add_imu_data(self, imu_readings):
        self.imu_data_buffer.append(imu_readings)

    def add_hr_data(self, hr_reading):
        self.hr_data_buffer.append(hr_reading)

    def add_gps_data(self, gps_reading):
        self.gps_data_buffer.append(gps_reading)

    def fuse_data(self):
        """
        Combine buffered data streams using a weighted average or ML model.
        """
        # Simple example: normalize and average all available data
        fused_output = {}

        if self.pose_data_buffer:
            fused_output['pose'] = np.mean(self.pose_data_buffer, axis=0)
        if self.imu_data_buffer:
            fused_output['imu'] = np.mean(self.imu_data_buffer, axis=0)
        if self.hr_data_buffer:
            fused_output['heart_rate'] = np.mean(self.hr_data_buffer)
        if self.gps_data_buffer:
            fused_output['gps'] = np.mean(self.gps_data_buffer, axis=0)

        return fused_output

if __name__ == "__main__":
    fusion = SensorFusion()

    # Simulate streaming data
    for i in range(10):
        fusion.add_pose_data(np.random.rand(33, 3))
        fusion.add_imu_data(np.random.rand(6))  # e.g. 3-axis accel + gyro
        fusion.add_hr_data(np.random.randint(60, 100))
        fusion.add_gps_data(np.random.rand(2))  # lat, lon

    fused = fusion.fuse_data()
    print("Fused sensor output:", fused)
