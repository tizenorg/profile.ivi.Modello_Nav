Name:       Modello_Nav
Summary:    Pure html5 UI
Version:    0.0.2
Release:    0
Group:      Automotive/Modello
License:    Apache-2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.bz2
Source1001: Modello_Nav.manifest

Requires:      Modello_Common
BuildRequires: pkgconfig(libtzplatform-config)
BuildRequires: zip

BuildArchitectures: noarch

%description
A proof of concept pure html5 UI

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1001} .

%build
#empty

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{TZ_SYS_APP_PREINSTALL}
mkdir -p %{buildroot}%{_datadir}/Modello/Common/icons
zip -r %{buildroot}%{TZ_SYS_APP_PREINSTALL}/%{name}.wgt config.xml css Navigation_icon.png images index.html js templates
install -m 0644 Navigation_icon.png %{buildroot}%{_datadir}/Modello/Common/icons

%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{TZ_SYS_APP_PREINSTALL}/Modello_Nav.wgt
%{_datadir}/Modello/Common/icons/Navigation_icon.png
