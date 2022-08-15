my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'}
gra_ds = {'A': 100, 'B': 80, 'C': 40}
i = []
for s_ub in my_ranks:
    print(
        f"My Rank in {s_ub} Is {my_ranks[s_ub]} And This Equal {gra_ds[my_ranks[s_ub]]} Points")
    i.append(gra_ds[my_ranks[s_ub]])
print(f"total point is {sum(i)}".title())
