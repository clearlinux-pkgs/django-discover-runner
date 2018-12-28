#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB17327D40171DF30 (jannis@leidel.info)
#
Name     : django-discover-runner
Version  : 1.0
Release  : 24
URL      : https://files.pythonhosted.org/packages/d3/60/5ffffcfb2306afd1f67cb7fb820eba66033a2cb4aceda131d8f9c47ff2af/django-discover-runner-1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d3/60/5ffffcfb2306afd1f67cb7fb820eba66033a2cb4aceda131d8f9c47ff2af/django-discover-runner-1.0.tar.gz
Source99 : https://files.pythonhosted.org/packages/d3/60/5ffffcfb2306afd1f67cb7fb820eba66033a2cb4aceda131d8f9c47ff2af/django-discover-runner-1.0.tar.gz.asc
Summary  : A Django test runner based on unittest2's test discovery.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: django-discover-runner-python3
Requires: django-discover-runner-license
Requires: django-discover-runner-python
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
======================

%package license
Summary: license components for the django-discover-runner package.
Group: Default

%description license
license components for the django-discover-runner package.


%package python
Summary: python components for the django-discover-runner package.
Group: Default
Requires: django-discover-runner-python3

%description python
python components for the django-discover-runner package.


%package python3
Summary: python3 components for the django-discover-runner package.
Group: Default
Requires: python3-core

%description python3
python3 components for the django-discover-runner package.


%prep
%setup -q -n django-discover-runner-1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532325542
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/django-discover-runner
cp LICENSE %{buildroot}/usr/share/doc/django-discover-runner/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/django-discover-runner/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
