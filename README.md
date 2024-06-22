# Create python virtual environment
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
To export the package list use the following command once the virtual environment is activated :
```bash
pip freeze > requirements.txt
```

# Generate code from .proto
## Python
```bash
python -m grpc_tools.protoc -I interface/ --python_out=interface/ --pyi_out=interface/--grpc_python_out=interface/ interface/camera-inteface.proto
```

# Screen brightness control Python on Linux
Please run the following commands before expecti,g any change on the brightness of your screen. A reboot may be needed.
```bash
echo 'SUBSYSTEM=="backlight",RUN+="/bin/chmod 666 /sys/class/backlight/%k/brightness /sys/class/backlight/%k/bl_power"' | sudo tee -a /etc/udev/rules.d/backlight-permissions.rules

sudo udevadm control --reload-rules && udevadm trigger
```