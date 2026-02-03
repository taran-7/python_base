def get_user_status(user_id):
    # Імітація пошуку в базі
    if user_id == 1:
        return True, "Admin"  # Python автоматично пакує це в (True, "Admin")
    else:
        return False, "Guest"

# Розпаковка результату в дві змінні
is_admin, role = get_user_status(1)
print(f"Is Admin: {is_admin}, Role: {role}")
