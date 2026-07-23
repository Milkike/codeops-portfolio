class Branch:
    def init(self, name):
        self.name = name
        self.children = []
        self.accounts = []

    def total_balance(self):
        total = sum(self.accounts)

        for child in self.children:
            total += child.total_balance()

        return total


# Create tree

head_office = Branch("Head Office")

addis = Branch("Addis Ababa")
adama = Branch("Adama")

bole = Branch("Bole Branch")
piassa = Branch("Piassa Branch")


head_office.children.append(addis)
head_office.children.append(adama)

addis.children.append(bole)
addis.children.append(piassa)


# Add balances

head_office.accounts = [1000]
addis.accounts = [2000]
adama.accounts = [1500]
bole.accounts = [500]
piassa.accounts = [700]


print("Total Bank Balance:")
print(head_office.total_balance())





from collections import deque


transfers = {
    "CBE-1": ["CBE-2", "CBE-3"],
    "CBE-2": ["CBE-4"],
    "CBE-3": ["CBE-4"],
    "CBE-4": []
}


def bfs(graph, start):

    visited = set()
    queue = deque([start])

    while queue:

        account = queue.popleft()

        if account not in visited:

            visited.add(account)

            for neighbor in graph[account]:
                queue.append(neighbor)

    return visited



reachable = bfs(transfers, "CBE-1")

print("Reachable accounts:")
print(reachable)




