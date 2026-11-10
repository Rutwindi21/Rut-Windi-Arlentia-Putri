from random import choice

def make_random_ticket(pool):
    """Membuat tiket acak berisi 4 elemen."""
    ticket = []
    while len(ticket) < 4:
        item = choice(pool)
        if item not in ticket:
            ticket.append(item)
    return ticket

def check_ticket(played_ticket, winning_ticket):
    """Memeriksa apakah semua elemen dalam tiket bermain ada di tiket pemenang."""
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    return True

# Setup data
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
my_ticket = [7, 'B', 3, 10]
winning_ticket = []

# Mencari tahu berapa kali iterasi hingga menang
loop_count = 0
won = False

while not won:
    new_winning_ticket = make_random_ticket(lottery_pool)
    loop_count += 1
    if check_ticket(my_ticket, new_winning_ticket):
        winning_ticket = new_winning_ticket
        won = True

print(f"Tiket Saya: {my_ticket}")
print(f"Tiket Pemenang yang ditarik: {winning_ticket}")
print(f"Loop harus berjalan sebanyak {loop_count} kali hingga tiket saya menang!")