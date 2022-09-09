import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobilleNo = "+919170066404"
mobilleNo = phonenumbers.parse(mobilleNo)

print(timezone.time_zones_for_number(mobilleNo))
print(carrier.name_for_number(mobilleNo, "en"))
print(geocoder.description_for_number(mobilleNo, "en"))