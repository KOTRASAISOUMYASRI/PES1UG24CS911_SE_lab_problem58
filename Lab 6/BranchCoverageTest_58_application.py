import pytest
from restaurant_bill import bill_total, split_bill, table_wait


def test_bill_total_section_validation():
    with pytest.raises(ValueError):
        bill_total("invalid", 100, 2, False)

    assert bill_total("dine_in", 100, 2, False) == 115


def test_bill_total_order_validation():
    with pytest.raises(ValueError):
        bill_total("dine_in", -1, 2, False)

    with pytest.raises(ValueError):
        bill_total("dine_in", 100, 0, False)

    assert bill_total("takeaway", 100, 2, False) == 105


def test_bill_total_happy_hour_conditions():
    assert bill_total("dine_in", 1000, 2, True) == 924
    assert bill_total("takeaway", 1000, 2, True) == 1050
    assert bill_total("dine_in", 1000, 2, False) == 1155


def test_bill_total_large_party_condition():
    assert bill_total("dine_in", 100, 8, False) == 325
    assert bill_total("dine_in", 100, 7, False) == 115


def test_split_bill_validation_and_rounding():
    with pytest.raises(ValueError):
        split_bill(100, 0, 10)

    with pytest.raises(ValueError):
        split_bill(100, 2, -1)

    assert split_bill(100, 4, 0) == 25
    assert split_bill(100, 3, 0) == 34


def test_table_wait_all_branches():
    assert table_wait(13, 2, False) == "call ahead"
    assert table_wait(4, 2, True) == "seat now"
    assert table_wait(4, 0, False) == "waitlist"
    assert table_wait(8, 1, False) == "waitlist"
    assert table_wait(8, 2, False) == "seat now"
    assert table_wait(4, 1, False) == "seat now"