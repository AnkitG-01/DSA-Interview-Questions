def move(n,fr,to):
    print(f"Disk {n} moved from {fr} to {to}")
def hanoi(n,fr,via,to):
    if n==0:
        return
    else:
        hanoi(n-1,fr,to,via)
        move(n,fr,to)
        hanoi(n-1,via,fr,to)
n=3
hanoi(n,'A','B','C')