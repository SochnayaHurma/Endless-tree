def check_active(path, tree):
    branches = []
    active_branch = False
    for root, children in tree.items():
        if root.named_url == path or root.abs_url == path:
            active_branch = True
            branches.append(
                (root, check_active(path, children)[0], True)
            )
        else:
            checked_children, active = check_active(path, children)
            branches.append(
                (root, checked_children, active)
            )
            active_branch = active_branch or active
    return branches, active_branch
