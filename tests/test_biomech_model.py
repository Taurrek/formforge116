import pytest
import numpy as np
from modules.biomech_model import BiomechModel

@pytest.fixture
def model():
    return BiomechModel()

def test_calibrate_single_joint(model):
    angles = {'knee': 45}
    info = {'height': 1.8, 'weight': 75}
    params = model.calibrate(angles, info)
    assert 'ranges' in params and 'knee' in params['ranges']
    assert np.isclose(params['ranges']['knee'], np.pi/4)

def test_calibrate_multiple_joints(model):
    angles = {'hip': 30, 'ankle': 60}
    info = {'height': 1.7, 'weight': 65}
    params = model.calibrate(angles, info)
    expected = {k: np.deg2rad(v) for k, v in angles.items()}
    for joint, rad in expected.items():
        assert np.isclose(params['ranges'][joint], rad)

def test_calibrate_requires_height(model):
    with pytest.raises(ValueError):
        model.calibrate({'hip': 45}, {'weight': 70})

def test_predict_risk_structure(model):
    joint_df = [{'joint': 'hip', 'angle': 20}, {'joint': 'knee', 'angle': 40}]
    result = model.predict_risk(joint_df)
    assert isinstance(result, dict)
    assert 'risk_score' in result
    rs = result['risk_score']
    assert isinstance(rs, float)
    assert 0.0 <= rs <= 1.0

def test_predict_risk_after_calibration(model):
    model.calibrate({'hip': 30, 'knee': 45}, {'height': 1.75, 'weight': 70})
    joint_df = [{'joint': 'hip', 'angle': 30}, {'joint': 'knee', 'angle': 45}]
    result = model.predict_risk(joint_df)
    assert 'risk_score' in result
    assert isinstance(result['risk_score'], float)
