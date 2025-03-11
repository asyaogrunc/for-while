n = int(input("Bir sayı girin: "))

toplam_for = 0
for i in range(1, n+1):
    toplam_for += i
print("For döngüsü ile toplam: " + str(toplam_for))

toplam_while = 0
i = 1
while i <= n:
    toplam_while += i
    i += 1
print("While döngüsü ile toplam: " + str(toplam_while))