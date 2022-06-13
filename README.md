# nv-wayland-gnome-suspend
Fix the resume-after-suspend bug for GNOME on NVIDIA Wayland

## Usage
The repository is prepared to be build as `rpm`, but the containing files  can also be used for other Linux systems.
Place the files in your `rpmbuild` directory, `cd` into the `SPECS` directory and build the package using:
```
rpmbuild -ba nv-wayland-gnome-suspend.spec
```
After that install the package using `dnf`, `yum`, `rpm-ostree` or your preffered package manager. Activate the systemd units using the following command:
```
systemctl enable gnome-shell-suspend.service gnome-shell-resume.service
```

## Further instructions
Ensure you are using the NVIDIA proprietary driver and the video memory allication is activated. Using Fedora Silverblue, you can do it like that:
```
rpm-ostree kargs --append=rd.driver.blacklist=nouveau --append=modprobe.blacklist=nouveau \
  --append=nvidia-drm.modeset=1 --append=nvidia.NVreg_PreserveVideoMemoryAllocations=1 \
  --append=nvidia.NVreg_EnableS0ixPowerManagement=1
```
Don't forget to activate the corresponding systemd unit files:
```
systemctl enable nvidia-suspend.service nvidia-hibernate.service nvidia-resume.service
```
You can check the success entering the following command, which should result in three `enabled` messages printed to the shell:
```
systemctl is-enabled nvidia-suspend nvidia-hibernate nvidia-resume
```
