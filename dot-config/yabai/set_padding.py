import subprocess

output = subprocess.run(["yabai","-m","query","--displays"],capture_output=True,text=True)
output_text = output.stdout.strip()
output_obj = eval(output_text)
width = (output_obj[0]["frame"]["w"])

print("Current Width", width)
if width == 1920.0:
    subprocess.run(["yabai","-m","config","top_padding","50"])
    print("Padding set to 50")
else:
    subprocess.run(["yabai","-m","config","top_padding","0"])
    print("Padding set to 0")

