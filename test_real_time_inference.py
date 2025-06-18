import unittest
from formforge.real_time_inference_finalized import real_time_pipeline

class TestRealTimeInference(unittest.TestCase):
    def test_pipeline(self):
        # Test the real-time pipeline with mock data streams
        user_data_stream = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]
        golden_data_stream = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]

        # Run the pipeline
        result = real_time_pipeline(user_data_stream, golden_data_stream)

        # Assert the expected result format, e.g., that it's a list
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)  # Ensure there's some output

if __name__ == '__main__':
    unittest.main()

