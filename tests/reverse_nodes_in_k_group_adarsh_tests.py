from typing import Optional
from interview_problems import reverse_nodes_in_k_group_adarsh


def test_case_1(sol: reverse_nodes_in_k_group_adarsh.Solution) -> None:
    """
    Test case. Create a linked list with 5 integers, in order from 1 through 5. Set k to 2. Note that this is LeetCode example test case 1.

    Verify that the returned linked list is reversed in groups of 2. The last integer should be left in the original location.

    :param sol: Object with reverse_k_group solution method
    :return: None
    """
    input_list = [1, 2, 3, 4, 5]
    k = 2
    head = convert_list_to_linked_list(input_list)
    returned = sol.reverse_k_group(head, k)
    assert convert_linked_list_to_list(returned) == [2, 1, 4, 3, 5]


def test_case_2(sol: reverse_nodes_in_k_group_adarsh.Solution) -> None:
    """
    Test case. Create a linked list with 5 integers, in order from 1 through 5. Set k to 3. Note that this is LeetCode example test case 2.

    Verify that the returned linked list is reversed in groups of 3. The last two integers should be left in the original location.

    :param sol: Object with reverse_k_group solution method
    :return: None
    """
    input_list = [1, 2, 3, 4, 5]
    k = 3
    head = convert_list_to_linked_list(input_list)
    returned = sol.reverse_k_group(head, k)
    assert convert_linked_list_to_list(returned) == [3, 2, 1, 4, 5]


def test_case_3(sol: reverse_nodes_in_k_group_adarsh.Solution) -> None:
    """
    Test case. Create a linked list with just one node whose value is 0. Set k to 1. This will test the low end of range of values given in LeetCode.

    Verify that the returned linked list is reversed in groups of 1, meaning essentially that the original linked list is returned.

    :param sol: Object with reverse_k_group solution method
    :return: None
    """
    input_list = [0]
    k = 1
    head = convert_list_to_linked_list(input_list)
    returned = sol.reverse_k_group(head, k)
    assert convert_linked_list_to_list(returned) == [0]


def test_case_4(sol: reverse_nodes_in_k_group_adarsh.Solution) -> None:
    """
    Test case. Create a linked list with just one node whose value is 1000. Set k to 5000. This will test the high end of range of values given in LeetCode.

    Verify that the returned linked list is reversed in groups of 5000, essentially the original linked list is returned unchaged as there are not 5000 elements in the linked list.

    :param sol: Object with reverse_k_group solution method
    :return: None
    """
    input_list = [1000]
    k = 5000
    head = convert_list_to_linked_list(input_list)
    returned = sol.reverse_k_group(head, k)
    assert convert_linked_list_to_list(returned) == [1000]


def test_case_5(sol: reverse_nodes_in_k_group_adarsh.Solution) -> None:
    """
    Test case. Create a linked list with 10 integers. Set k to the length of the list.

    Verify that the returned linked list is fully reversed, because k is the same as the length of the list.

    :param sol: Object with reverse_k_group solution method
    :return: None
    """
    input_list = [11, 0, 3, 4, 5, 6, 7, 9, 1000, 12]
    k = len(input_list)
    head = convert_list_to_linked_list(input_list)
    returned = sol.reverse_k_group(head, k)
    assert convert_linked_list_to_list(returned) == [12, 1000, 9, 7, 6, 5, 4, 3, 0, 11]


def convert_list_to_linked_list(input_list: list[int]) -> Optional[reverse_nodes_in_k_group_adarsh.ListNode]:
    """
    Helper function that traverses the input list of integers to create a linked list with the same values.

    :param input_list: Input list of integers
    :return: head of the linked list with the same values
    """
    temp_head = reverse_nodes_in_k_group_adarsh.ListNode(0)
    current_node = temp_head

    for element in input_list:
        current_node.next = reverse_nodes_in_k_group_adarsh.ListNode(element)
        current_node = current_node.next

    return temp_head.next


def convert_linked_list_to_list(list_head: Optional[reverse_nodes_in_k_group_adarsh.ListNode]) -> list[int]:
    """
    Helper function that traverses the input linked list to create a list of integers with the same values.

    :param list_head: Inputted head of the linked list
    :return: list of integers with same values as inputted linked list
    """
    res = []
    temp = list_head

    while temp:
        res.append(temp.val)
        temp = temp.next

    return res


def main() -> None:
    """
    Runs the test cases.

    :return: None
    """
    sol = reverse_nodes_in_k_group_adarsh.Solution()
    test_case_1(sol)
    test_case_2(sol)
    test_case_3(sol)
    test_case_4(sol)
    test_case_5(sol)


if __name__ == "__main__":
    main()
    print("All tests pass")
