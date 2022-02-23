"""Demonstrations of dictionary capabilities."""


schools: dict[str, int]

schools = dict()

schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150
print(schools)
print(f"UNC has {schools['UNC']} students.")


schools.pop("Duke")


is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")


for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")