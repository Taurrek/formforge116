import numpy as np
import time

def stream_data():
    """
    Simulate a real-time stream of user and golden athlete data.
    """
    while True:
        # Simulate real-time data from sensors
        user_data = np.random.random((10, 2))  # Replace with real user data
        golden_data = np.random.random((10, 2))  # Replace with real golden athlete data

        # Send data to real-time inference pipeline
        from real_time_inference_finalized import real_time_pipeline
        diff_map = real_time_pipeline(user_data, golden_data)
        
        # Print or process the feedback (in real-time)
        print("Real-time feedback:", diff_map)

        # Simulate a short delay between data streams
        time.sleep(1)  # Simulate a 1-second delay between frames

# Start streaming data
stream_data()
