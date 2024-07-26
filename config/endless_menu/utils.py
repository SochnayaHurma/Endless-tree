from collections import defaultdict


def check_active(path, tree):
    branches = []
    active_branch = False
    for root, children in tree.items():
        checked_children, active = check_active(path, children)
        if root.named_url == path or root.abs_url == path:
            active_branch = active = True
        branches.append(
            (root, checked_children, active)
        )
        active_branch = active_branch or active
    return branches, active_branch


def build_tree(query_set, url):
    tree, links = defaultdict(dict), defaultdict(dict)
    for item in query_set:
        link = links[item]
        if item.parent:
            links[item.parent][item] = link
        else:
            tree[item] = link
    checked_tree, _ = check_active(url, tree)
    return checked_tree
