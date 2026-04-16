import pytest
from unittest.mock import MagicMock
from src.number_asc_order import NumberAscOrder


def test_sort_returns_ascending_list_with_six_mega_sena_numbers():
    # Simula uma pilha de 6 posições com 6 números sorteados (ordem aleatória do sorteio)
    drawn_numbers = [38, 4, 52, 15, 47, 23]

    mock_stack = MagicMock()
    # is_empty() é chamado 1x no if inicial + 6x no while + 1x True para sair = 8 chamadas
    mock_stack.is_empty.side_effect = [False, False, False, False, False, False, False, True]
    mock_stack.pop.side_effect = drawn_numbers

    sorter = NumberAscOrder()
    result = sorter.sort(mock_stack)

    assert result == sorted(drawn_numbers)
    assert mock_stack.is_empty.call_count == 8
    assert mock_stack.pop.call_count == 6


def test_sort_returns_empty_list_when_stack_is_empty():
    # Simula uma pilha de 6 posições, vazia
    mock_stack = MagicMock()
    mock_stack.is_empty.return_value = True

    sorter = NumberAscOrder()
    result = sorter.sort(mock_stack)

    assert result == []
    mock_stack.is_empty.assert_called_once()
    mock_stack.pop.assert_not_called()
