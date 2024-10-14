import pytest
from main import invert_dict 

def test_invert_dict_unique_values():
    # Тест для случая с уникальными значениями
    input_dict = {"Ivanov": 97832, "Petrov": 55521}
    expected = {97832: "Ivanov", 55521: "Petrov"}
    assert invert_dict(input_dict) == expected

def test_reverse_dict_duplicate_values():
    # Тест для случая, когда несколько ключей имеют одинаковые значения
    input_dict = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}
    expected = {97832: ("Ivanov", "Kuznecov"), 55521: "Petrov"}
    assert invert_dict(input_dict) == expected

def test_reverse_dict_non_hashable_value():
    # Тест, когда одно из значений не является хешируемым (список)
    input_dict = {"Ivanov": 97832, "Petrov": 55521, "Sidorov": [1, 2, 3]}
    with pytest.raises(TypeError):
        invert_dict(input_dict)

def test_reverse_dict_empty_dict():
    # Тест для пустого словаря
    input_dict = {}
    expected = {}
    assert invert_dict(input_dict) == expected

def test_reverse_dict_single_element():
    # Тест для словаря с одним элементом
    input_dict = {"Ivanov": 97832}
    expected = {97832: "Ivanov"}
    assert invert_dict(input_dict) == expected

def test_reverse_dict_duplicate_values_more_than_two():
    # Тест для случая, когда одно значение соответствует более чем двум ключам
    input_dict = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832, "Sidorov": 97832}
    expected = {97832: ("Ivanov", "Kuznecov", "Sidorov"), 55521: "Petrov"}
    assert invert_dict(input_dict) == expected

if __name__ == "__main__":
    pytest.main()