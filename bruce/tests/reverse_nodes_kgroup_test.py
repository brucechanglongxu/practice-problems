import reverse_nodes_in_k_group
import array_to_list

def first_test_case(reversed_sol : reverse_nodes_in_k_group.Solution) -> None:
    orig_list = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 1
    list_linked = array_to_list(orig_list)
    assert reversed_sol.reverse_nodes_in_k_group(list_linked) == 0
   
def second_test_case(reversed_sol : reverse_nodes_in_k_group.Solution) -> None:
    orig_list = []
    assert reversed_sol.reverse_nodes_in_k_group(list_linked) == 0

def third_test_case(reversed_sol : reverse_nodes_in_k_group.Solution) -> None:
    orig_list = []
    list_linked
    assert reversed_sol.reverse_nodes_in_k_group(list_linked) == 0
    
def fourth_test_case(reversed_sol : reverse_nodes_in_k_group.Solution) -> None:
    orig_list = []
    list_linked = []
    assert reversed_sol.reverse_nodes_in_k_group(list_linked) == 0
    
def fifth_test_case(reversed_sol : reverse_nodes_in_k_group.Solution) -> None:
    list = []
    assert reversed_sol.reverse_nodes_in_k_group(list_linked) == 0
    
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
    fifth_test_case(solution)

if __name__ == "__main__":
    main()
    print("Our solution passes")
