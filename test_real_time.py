import unittest
import numpy as np
from real_time_inference_finalized import real_time_pipeline

class TestRealTimePipeline(unittest.TestCase):
    
    def test_pipeline(self):
        user_data_stream = np.random.random((10, 2))  # Simulated user data
        golden_data_stream = np.random.random((10, 2))  # Simulated golden data

        result = real_time_pipeline(user_data_stream, golden_data_stream)
        
        # Verify if output is valid (i.e., a difference map is generated)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, (10,))

if __name__ == "__main__":
    unittest.main()
