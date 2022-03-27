standards = {
    "tech": "python",
    "country": "korea",
    "limit": 100,
}


class Tech(dict):
    def __missing__(self, key):
        standards[key] = "default value"


tech_specs = Tech()
tech1 = tech_specs["arch"]
print(standards)
