import toml

output_file = ".streamlit/secrets.toml"

with open("private/raspberry1-d07d8-firebase-adminsdk-4tlwq-68582b8dbd.json") as json_file:
    json_text = json_file.read()

config = {"textkey": json_text}
toml_config = toml.dumps(config)

with open(output_file, "w") as target:
    target.write(toml_config)