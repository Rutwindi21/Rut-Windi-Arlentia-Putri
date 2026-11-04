def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Sesuaikan data profil diri kamu di sini
my_profile = build_profile(
    'rut', 
    'windi', 
    location='surakarta', 
    field='teknik industri', 
    hobbies='kulineran'
)

print(my_profile)