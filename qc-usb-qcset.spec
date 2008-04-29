%define sname qc-usb
%define name %{sname}-qcset
%define version 0.6.6
%define release %mkrel 2

Name: %{name}
Version: %version
Release: %release
Summary: Tool for the old Quickcam Express webcams
License: GPL
Source: http://downloads.sourceforge.net/qce-ga/%{sname}-%{version}.tar.gz
URL: http://qce-ga.sourceforge.net/
Group: System/Kernel and hardware
Suggests: kmod(quickcam)
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package contains qcset, a tool that allows to configure the "quickcam" 
module on the fly.

The "quickcam" module can be installed with dkms-qc-usb package, ans is for 
the following webcams :
- Dexxa Webcam
- Labtec Webcam (old model)
- LegoCam
- Logitech QuickCam Express (old model)
- Logitech QuickCam Notebook (some models)
- Logitech QuickCam Web

Generally, any USB camera with a USB vendor ID of 0x46d and a USB product ID 
of 0x840, 0x850, or 0x870 (so, 0x46d:0x840, for example), should work.
You can check the USB IDs with Mandriva Control Center or using command-line 
utilities such as lsusb or "lspcidrake -v".

%prep
%setup -q -n %{sname}-%{version}

%build
%make qcset

%install
rm -rf %{buildroot}
install -D -m 755 qcset %{buildroot}%{_bindir}/qcset

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc APPLICATIONS CREDITS FAQ README.qce TODO qcweb-info.txt debug.sh freeshm.sh quickcam.sh
%attr(0755,root,root) %{_bindir}/qcset
