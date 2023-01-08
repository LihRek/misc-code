class Tool:
    def __init__(self, ids, price):
        self.ids = ids
        self.price = price


class Client:
    def __init__(self, name, credits, holding):
        self.name = name
        self.credits = credits
        self.holding = holding

    def ret(self, id_tool):
        print(tools)

        possible = False
        if self.holding is None:
            self.holding = []
        for tool in self.holding:
            if tool == id_tool:
                possible = True
                for sear in tools:
                    print("asdf", sear)
                    if sear.ids == id_tool:
                        self.credits += sear.price
                        shop.inventory.append(sear)
                        break
                break
        if possible:
            print("DONE")
        else:
            print("ERROR")

    def borrow(self, id_tool):
        possible = True
        for tool in tools:
            if tool.ids == id_tool:
                if (self.credits - tool.price) < 0:
                    possible = False
                    continue
                if not shop.has(id_tool):
                    possible = False
                    continue
                else:
                    self.credits -= tool.price
                    if self.holding is None:
                        self.holding = []
                    self.holding.append(id_tool)
                    for j in range(len(shop.inventory)):
                        if shop.inventory[j].ids == id_tool:
                            x = shop.inventory.pop(j)
                            break
        if possible:
            print("DONE")
        else:
            print("ERROR")


class Shop:
    def __init__(self, customers, inventory):
        self.inventory = inventory
        self.customers = customers
    def has(self, id):
        for i in shop.inventory:
            if i.ids == id:
                return True
        return False


c, t, a = input().split()
c = int(c)
t = int(t)
a = int(a)
clients = [Client for i in range(c)]
tools = [Tool for i in range(t)]
for i in range(c):
    id, cred = input().split()
    cred = int(cred)
    clients[i] = Client(id, cred, [])

for i in range(t):
    id, cred, name = input().split()
    cred = int(cred)
    tools[i] = Tool(id, cred)

shop = Shop(clients, tools)

for i in range(a):
    action, client_name, tool_name = input().split()
    print(action, client_name, tool_name, end=' ')
    if action == 'B':
        for j in range(len(clients)):
            if clients[j].name == client_name:
                clients[j].borrow(tool_name)
                break
    if action == 'R':
        for j in range(len(clients)):
            if clients[j].name == client_name:
                clients[j].ret(tool_name)
                break

for i in clients:
    print(i.name, i.credits)


