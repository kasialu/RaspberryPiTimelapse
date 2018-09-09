# Raspberry Pi Camera Timelapse

## Run locally

To run the script go to the directory containing the code:
```bash
cd ~/timelapse
``` 
create environment 
```bash
pipenv shell
``` 

and run
```bash
python capture.py
```

## Service

To enable timelapse script on boot create a service by copying ``timelapse.servise`` to
``/lib/systemd/system/timelapse.servise``. Enable  and start the service

```bash
sudo systemctl deamon-reload
sudo systemctl enable timelapse.service
```

and reboot by

```bash
sudo reboot
```
