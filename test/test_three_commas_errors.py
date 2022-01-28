from src.three_commas.error import ThreeCommasError
import json


def read_error_from_json(file_path) -> ThreeCommasError:
    with open(file_path, 'r+') as f:
        error = json.loads(f.read())
        error_model = ThreeCommasError(error)
    return error_model


def test_bo_to_small_tc_error_with_pair():
    error = read_error_from_json('test/sample_data/errors/bo_too_small_with_pair.json')

    assert error.is_base_order_to_small_error()
    bo_error = error.get_base_order_to_small_error()
    assert len(bo_error) == 1
    assert bo_error[0].amount == 33.35
    assert bo_error[0].pair == 'USDT_YFI'


def test_multiple_bo_error():
    error = read_error_from_json('test/sample_data/errors/multiple_bo_so_errors.json')

    bo_error = error.get_base_order_to_small_error()
    assert len(bo_error) == 4
    assert set(map(lambda be: be.pair, bo_error)) == {'USDT_1INCH', 'USDT_AAVE', 'USDT_ACM', 'USDT_ADA'}
    assert list(map(lambda be: be.amount, bo_error)) == [10.0, 10.0, 10.0, 10.0]


def test_bo_to_small_tc_error_no_pair():
    error = read_error_from_json('test/sample_data/errors/bo_too_small_no_pair.json')

    bo_error = error.get_base_order_to_small_error()
    assert bo_error[0].amount == 9.4674
    assert not bo_error[0].pair


def test_no_bo_error():
    error = read_error_from_json('test/sample_data/errors/signature_invalid.json')

    bo_error = error.get_base_order_to_small_error()
    assert len(bo_error) == 0
    assert not error.is_base_order_to_small_error()

    error = ThreeCommasError({'custom_message': 'some error occured'})
    bo_error = error.get_base_order_to_small_error()
    assert len(bo_error) == 0


def test_api_key_invalid_or_expired():
    error = read_error_from_json('test/sample_data/errors/api_key_invalid_or_expired_error.json')
    assert error.is_api_key_invalid_or_expired()


def test_api_key_has_no_permission_error():
    error = read_error_from_json('test/sample_data/errors/api_key_has_no_permission_error.json')
    assert error.is_api_key_has_no_permission_error()

