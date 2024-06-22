from twilio.rest import Client

# Masukkan SID akun Twilio Anda dan token autentikasi
account_sid = 'US8ddffe89d2013aec41ff9a6f4207ca99'
auth_token = 'ZJMGXH8C4ESUZ5EVSPM6FFJG'

client = Client(account_sid, auth_token)

# Masukkan nomor telepon yang ingin Anda cari informasinya
phone_number = '+1234567890'  # Ganti dengan nomor telepon yang Anda cari

try:
    phone_info = client.lookups.phone_numbers(phone_number).fetch(type="carrier")

    print(f"Phone Number: {phone_info.phone_number}")
    print(f"Country Code: {phone_info.country_code}")
    print(f"Carrier: {phone_info.carrier['name']}")
    print(f"Carrier Type: {phone_info.carrier['type']}")

except Exception as e:
    print(f"Error: {str(e)}")
