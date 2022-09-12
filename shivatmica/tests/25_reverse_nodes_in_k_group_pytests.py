from solutions import 25_reverse_nodes_in_k_group

def l_to_ll(list):
    """
    Converts a list into a linked list
    """
    a = 25_reverse_nodes_in_k_group.ListNode()
    linked_list = a
    for i in list:
        linked_list.next = 25_reverse_nodes_in_k_group.ListNode(i)
        linked_list = linked_list.next
    return a.next
  
def ll_to_l(linked_list: 25_reverse_nodes_in_k_group.ListNode()):
    """
    Converts a linked list into a list
    """
    list = []
    a = linked_list

    while a:
        list.append(a)
        a = a.next
    return list

def test_case_1(sol = 25_reverse_nodes_in_k_group.Problem25()) -> None:
    """
    Test case 1: Leetcode example test case #1
    Expected output: [2, 1, 4, 3, 5]
    
    Parameters
    ----------
    sol : object
        consists of the reverse_nodes_in_k_group question's solution
        
    Returns
    -------
    None
    """
    list = [1, 2, 3, 4, 5]
    k = 2
    head = l_to_ll(list)
    assert ll_to_l(sol.reverse_k_group(head, k)) == [2, 1, 4, 3, 5]
    
def test_case_2(sol = 25_reverse_nodes_in_k_group.Problem25()) -> None:
    """
    Test case 2: Leetcode example test case #2
    Expected output: [3, 2, 1, 4, 5]
    
    Parameters
    ----------
    sol : object
        consists of the reverse_nodes_in_k_group question's solution
        
    Returns
    -------
    None
    """
    list = [1, 2, 3, 4, 5]
    k = 3
    head = l_to_ll(list)
    assert ll_to_l(sol.reverse_k_group(head, k)) == [3, 2, 1, 4, 5]
    
def test_case_3(sol = 25_reverse_nodes_in_k_group.Problem25()) -> None:
    """
    Test case 3: linked list with 5000 nodes, the maximum number of nodes possible in the list
    Expected output: [5, 4, 3, 2, 1, 5, 4, 3, 2, 1] * 500
    
    Parameters
    ----------
    sol : object
        consists of the reverse_nodes_in_k_group question's solution
        
    Returns
    -------
    None
    """
    list = [1, 2, 3, 4, 5] * 1000
    k = 10
    head = l_to_ll(list)
    assert ll_to_l(sol.reverse_k_group(head, k)) == [5, 4, 3, 2, 1, 5, 4, 3, 2, 1] * 500

def test_case_4(sol = 25_reverse_nodes_in_k_group.Problem25()) -> None:
    """
    Test case 4: linked list with 1 node with the value 0 (minimum values in the ranges for k, n, and node.val)
    Expected output: [0]
    
    Parameters
    ----------
    sol : object
        consists of the reverse_nodes_in_k_group question's solution
        
    Returns
    -------
    None
    """
    list = [0]
    k = 1
    head = l_to_ll(list)
    assert ll_to_l(sol.reverse_k_group(head, k)) == [0]

def test_case_5(sol = 25_reverse_nodes_in_k_group.Problem25()) -> None:
    """
    Test case 5: linked list with 5000 nodes, the maximum number of nodes possible in the list and also includes the maximum value for node.val (1000)
    Expected output: [1000, 999, 998, 997, 996, 1000, 999, 998, 997, 996] * 500
    
    Parameters
    ----------
    sol : object
        consists of the reverse_nodes_in_k_group question's solution
        
    Returns
    -------
    None
    """
    list = [996, 997, 998, 999, 1000] * 1000
    k = 10
    head = l_to_ll(list)
    assert ll_to_l(sol.reverse_k_group(head, k)) == [1000, 999, 998, 997, 996, 1000, 999, 998, 997, 996] * 500

def test_case_5(sol = 25_reverse_nodes_in_k_group.Problem25()) -> None:
    """
    Test case 6: linked list with 5000 nodes, the maximum number of nodes possible in the list and the maximum value for k (5000)
    Expected output: [14] * 5000
    
    Parameters
    ----------
    sol : object
        consists of the reverse_nodes_in_k_group question's solution
        
    Returns
    -------
    None
    """
    list = [14] * 5000
    k = 5000
    head = l_to_ll(list)
    assert ll_to_l(sol.reverse_k_group(head, k)) == [14] * 5000
    
def main() -> None:
    """
    Executes each of the test cases
    
    Returns
    -------
    None
    """
    sol = 25_reverse_nodes_in_k_group.Problem25()
    test_case_1(sol)
    test_case_2(sol)
    test_case_3(sol)
    test_case_4(sol)
    test_case_5(sol)
    test_case_6(sol)

if __name__ == "__main__":
    main()
    print("Accepted solution")
