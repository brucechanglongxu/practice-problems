import reverse_nodes_in_k_group
import array_to_list
import list_to_array

def first_test_case(reversed_sol : reverse_nodes_in_k_group.Solution) -> None:
    """
    Reversing all of the nodes at once
    """
    orig_list = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 8
    list_linked = array_to_list(orig_list)
    assert reversed_sol.reverse_nodes_in_k_group(list_to_array(list_linked)) == [8, 7, 6, 5, 4, 3, 2, 1]
   
def second_test_case(reversed_sol : reverse_nodes_in_k_group.Solution) -> None:
    """
    Reversing n/4 of all of the nodes
    """
    orig_list = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 2
    list_linked = array_to_list(orig_list)
    assert reversed_sol.reverse_nodes_in_k_group(list_to_array(list_linked)) == [2, 1, 4, 3, 6, 5, 8 ,7]

def third_test_case(reversed_sol : reverse_nodes_in_k_group.Solution) -> None:
    """
    Reversing half of all of the nodes
    """
    orig_list = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 4
    list_linked = array_to_list(orig_list)
    assert reversed_sol.reverse_nodes_in_k_group(list_to_array(list_linked)) == [4, 3, 2, 1, 8, 7, 6, 5]
    
def fourth_test_case(reversed_sol : reverse_nodes_in_k_group.Solution) -> None:
    """
    Reversing only one node at a time
    """
    orig_list = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 1
    list_linked = array_to_list(orig_list)
    assert reversed_sol.reverse_nodes_in_k_group(list_to_array(list_linked)) == [1, 2, 3, 4, 5, 6, 7, 8]
    
def main() -> None:
    """
    Runs the test cases.
    :return: None
    """
    solution = reverse_nodes_in_k_group.Solution()
    first_test_case(solution)
    second_test_case(solution)
    third_test_case(solution)
    fourth_test_case(solution)

if __name__ == "__main__":
    main()
    print("Our solution passes")
