import pytest
from restaurant_bill import bill_total, split_bill, table_wait


def test_bill_total_normal():
    assert bill_total("dine_in", 1000, 2, False) == 1155


def test_bill_total_happy_hour_and_large_party():
    assert bill_total("rooftop", 500, 8, True) == 693


def test_bill_total_invalid_section():
    with pytest.raises(ValueError, match="unknown section"):
        bill_total("garden", 100, 2, False)


def test_bill_total_invalid_order():
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", -1, 2, False)


def test_split_bill_remainder():
    assert split_bill(100, 3, 10) == 37


def test_split_bill_invalid_people():
    with pytest.raises(ValueError, match="invalid people count"):
        split_bill(100, 0, 10)


def test_split_bill_invalid_tip():
    with pytest.raises(ValueError, match="invalid tip"):
        split_bill(100, 2, -1)


def test_table_wait_all_outcomes():
    assert table_wait(13, 2, False) == "call ahead"
    assert table_wait(4, 2, True) == "seat now"
    assert table_wait(4, 0, False) == "waitlist"
    assert table_wait(8, 1, False) == "waitlist"
    assert table_wait(4, 1, False) == "seat now"