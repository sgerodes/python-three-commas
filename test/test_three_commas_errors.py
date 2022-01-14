from src.three_commas import ThreeCommasError
import json


def test_bo_to_small_tc_error_with_pair():
    file_path = 'test/sample_data/errors/bo_too_small_with_pair.json'
    with open(file_path, 'r+') as f:
        error = json.loads(f.read())
        error_model = ThreeCommasError(error)

        bo_error = error_model.bo_to_small_error()
        assert len(bo_error) == 1
        assert bo_error[0].amount == 33.35
        assert bo_error[0].pair == 'USDT_YFI'


def test_multiple_bo_error():
    file_path = 'test/sample_data/errors/multiple_bo_so_errors.json'
    with open(file_path, 'r+') as f:
        error = json.loads(f.read())
        error_model = ThreeCommasError(error)

        bo_error = error_model.bo_to_small_error()
        assert len(bo_error) == 4
        assert set(map(lambda be: be.pair, bo_error)) == {'USDT_1INCH', 'USDT_AAVE', 'USDT_ACM', 'USDT_ADA'}
        assert list(map(lambda be: be.amount, bo_error)) == [10.0, 10.0, 10.0, 10.0]


def test_bo_to_small_tc_error_no_pair():
    file_path = 'test/sample_data/errors/bo_too_small_no_pair.json'
    with open(file_path, 'r+') as f:
        error = json.loads(f.read())
        error_model = ThreeCommasError(error)

        bo_error = error_model.bo_to_small_error()
        assert bo_error[0].amount == 9.4674
        assert not bo_error[0].pair


def test_no_bo_error():
    file_path = 'test/sample_data/errors/signature_invalid.json'
    with open(file_path, 'r+') as f:
        error = json.loads(f.read())
        error_model = ThreeCommasError(error)

        bo_error = error_model.bo_to_small_error()
        assert len(bo_error) == 0

    error_model = ThreeCommasError({'custom_message': 'some error occured'})
    bo_error = error_model.bo_to_small_error()
    assert len(bo_error) == 0
