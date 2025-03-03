#!/usr/bin/env python3

import yaml
import numpy as np

# Read input YAML file
with open('roahmlab_combined.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Extract relevant camera parameters
cam_data = data['cam0']
intrinsics = cam_data['intrinsics']
distortion = cam_data['distortion_coeffs'] 
resolution = cam_data['resolution']
T_cam_imu = cam_data['T_cam_imu']

# Create output dictionary in ORB-SLAM3 format
output = {
    'File.version': '1.0',
    'Camera.type': 'PinHole',
    'Camera1.fx': intrinsics[0],
    'Camera1.fy': intrinsics[1], 
    'Camera1.cx': intrinsics[2],
    'Camera1.cy': intrinsics[3],
    'Camera1.k1': distortion[0],
    'Camera1.k2': distortion[1],
    'Camera1.p1': distortion[2], 
    'Camera1.p2': distortion[3],
    'Camera.width': resolution[0],
    'Camera.height': resolution[1],
    'Camera.fps': 30,
    'Camera.RGB': 1
}

# Add camera-IMU transformation
T_cam_imu_matrix = np.array(T_cam_imu)
output['Camera.T_b_c'] = {
    'rows': 4,
    'cols': 4,
    'dt': 'f',
    'data': [
        [T_cam_imu_matrix[0].tolist()],
        [T_cam_imu_matrix[1].tolist()],
        [T_cam_imu_matrix[2].tolist()],
        [T_cam_imu_matrix[3].tolist()]
    ]
}

# Add IMU parameters
output['IMU.NoiseGyro'] = data['imu0']['gyroscope_noise_density']
output['IMU.NoiseAcc'] = data['imu0']['accelerometer_noise_density'] 
output['IMU.GyroWalk'] = data['imu0']['gyroscope_random_walk']
output['IMU.AccWalk'] = data['imu0']['accelerometer_random_walk']
output['IMU.Frequency'] = data['imu0']['update_rate']

# Add IMU-camera transformation (identity since already in body frame)
output['IMU.T_b_c1'] = {
    'rows': 4,
    'cols': 4,
    'dt': 'f', 
    'data': [
        [[1.0, 0.0, 0.0, 0.0]],
        [[0.0, 1.0, 0.0, 0.0]],
        [[0.0, 0.0, 1.0, 0.0]],
        [[0.0, 0.0, 0.0, 1.0]]
    ]
}

# Add default ORB parameters
output['ORBextractor.nFeatures'] = 1000
output['ORBextractor.scaleFactor'] = 1.2
output['ORBextractor.nLevels'] = 8
output['ORBextractor.iniThFAST'] = 20
output['ORBextractor.minThFAST'] = 7

# Add default viewer parameters
output['Viewer.KeyFrameSize'] = 0.05
output['Viewer.KeyFrameLineWidth'] = 1.0
output['Viewer.GraphLineWidth'] = 0.9
output['Viewer.PointSize'] = 2.0
output['Viewer.CameraSize'] = 0.08
output['Viewer.CameraLineWidth'] = 3.0
output['Viewer.ViewpointX'] = 0.0
output['Viewer.ViewpointY'] = -0.7
output['Viewer.ViewpointZ'] = -3.5
output['Viewer.ViewpointF'] = 500.0

# Write output YAML file
with open('roahmlab_caminfo.yaml', 'w') as f:
    f.write('%YAML:1.0\n\n')  # Add YAML version header
    yaml.dump(output, f, default_flow_style=False)
