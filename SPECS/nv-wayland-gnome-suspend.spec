Name:           nv-wayland-gnome-suspend
Version:        1.0.1
Release:        1%{?dist}
Summary:        Fix the resume-after-suspend bug for GNOME on NVIDIA Wayland
BuildArch:      noarch

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:       bash

%description
This package installs a script and two systemd units to fix the suspend of GNOME on NVIDIA Wayland

%prep
%setup -q

%install
install -Dpm 0755 suspend-gnome-shell %{buildroot}%{_bindir}/suspend-gnome-shell
install -Dpm 644 gnome-shell-suspend.service %{buildroot}%{_unitdir}/gnome-shell-suspend.service
install -Dpm 644 gnome-shell-resume.service %{buildroot}%{_unitdir}/gnome-shell-resume.service

%post
%systemd_post gnome-shell-suspend.service
%systemd_post gnome-shell-resume.service

%preun
%systemd_preun gnome-shell-suspend.service
%systemd_preun gnome-shell-resume.service

%files
%{_bindir}/suspend-gnome-shell
%{_unitdir}/gnome-shell-suspend.service
%{_unitdir}/gnome-shell-resume.service


%changelog
* Mon Jun 13 2022 Laura Emilia Fäßler
- Initial package release and minor corrections
