import tree_helper


values = [5,3,8,1,4,7,9,None,2]
helper = tree_helper.TreeHelper()
root = helper.build_tree(values)

helper.print_tree(root)