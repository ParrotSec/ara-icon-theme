#
# Spec file for package ara-icon-theme
#
# Copyright (c) 2018 Sam Hewitt
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

Name:           ara-icon-theme
Version:        1.0
Release:        0
License:        CC-BY-SA-4.0
Summary:        Ara Icon theme
Url:            https://nest.parrotsec.org/packages/ara-icon-theme
Group:          System/GUI/Other
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  icon-naming-utils >= 0.8.7
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Ara is simple and modern icon theme with material design influences.

%prep
%setup -q
find -L . -type l -print -delete
chmod +x autogen.sh
chmod a-x AUTHORS README.md

%build
./autogen.sh
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}
rm -f %{buildroot}%{_datadir}/icons/ara/AUTHORS
%fdupes %{buildroot}%{_datadir}/icons/ara

%post
%icon_theme_cache_post ara

%files
%defattr(-,root,root)
%doc AUTHORS COPYING LICENSE README.md
%{_datadir}/icons/ara
%ghost %{_datadir}/icons/ara/icon-theme.cache
