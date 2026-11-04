def make_sandwich(*items):
    print("\nMembuat sandwich dengan bahan-bahan berikut:")
    for item in items:
        print(f"- {item}")

make_sandwich("keju", "tomat", "selada")
make_sandwich("daging sapi", "keju cheddar")
make_sandwich("telur", "mayones", "timun", "sosis")